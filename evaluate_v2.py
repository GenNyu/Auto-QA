"""
Evaluate QA outputs against gold answers using LLM semantic grading.

Compares qa/output/qa_output.json with qa/full_qa.json.
Outputs a scored JSON file with evaluate/score/check fields.
"""
import argparse
import json
import os
import re
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

from config import (
    DEFAULT_PROVIDER,
    OLLAMA_TIMEOUT,
    PROVIDER_API_KEYS,
    PROVIDER_CONFIGS,
    PROVIDER_KIND_MAP,
)
from providers.base import LLMProvider
from providers.factory import create_provider, normalize_provider_name

# Constants
DEFAULT_TEMPERATURE = 0.0
DEFAULT_SLEEP = 0.3
ENV_FILE = ".env"
UTC_TS_PATTERN = re.compile(r".*_\d{8}T\d{6}Z$")
QA_PROMPT_FILE = Path("qa/qa_prompt_v2.txt")


def load_system_prompt() -> str:
    if not QA_PROMPT_FILE.exists():
        raise FileNotFoundError(f"Missing system prompt file: {QA_PROMPT_FILE}")
    return QA_PROMPT_FILE.read_text(encoding="utf-8").strip()


SYSTEM_PROMPT = load_system_prompt()


@dataclass(frozen=True)
class EvaluatorConfig:
    pred_path: str
    gold_path: str
    output_path: str
    provider: str
    temperature: float
    sleep_time: float
    ollama_model: str
    ollama_url: str
    base_url: Optional[str] = None
    model: Optional[str] = None
    debug: bool = False


def append_utc_timestamp(output_path: Path) -> Path:
    stem = output_path.stem
    if UTC_TS_PATTERN.match(stem):
        return output_path

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return output_path.with_name(f"{stem}_{ts}{output_path.suffix}")


def normalize_question(text: str) -> str:
    if not text:
        return ""
    return re.sub(r"\s+", " ", text.strip().lower())


def strip_citations(text: str) -> str:
    if not text:
        return ""
    # Remove patterns like 【1】, [1], (1) that are likely citations.
    text = re.sub(r"【\d+】", "", text)
    text = re.sub(r"\[\d+\]", "", text)
    return text.strip()


def build_user_prompt(question: str, reference: str, candidate: str) -> str:
    return f"""
Question:
{question}

Reference Answer:
{reference}

Candidate Answer:
{candidate}
""".strip()


def build_messages(provider_name: str, prompt: str) -> List[Dict[str, str]]:
    if provider_name == "anthropic":
        # Anthropic: include system instructions in user content to enforce JSON-only output
        combined = f"{SYSTEM_PROMPT}\n\n{prompt}\n\nIMPORTANT: Return ONLY valid JSON. No extra text."
        return [{"role": "user", "content": combined}]

    return [
        {"role": "system", "content": f"{SYSTEM_PROMPT}\n\nIMPORTANT: Return ONLY valid JSON. No extra text."},
        {"role": "user", "content": prompt},
    ]


def call_llm(provider: LLMProvider, provider_name: str, question: str, reference: str, candidate: str, temperature: float) -> Dict:
    prompt = build_user_prompt(question, reference, candidate)
    messages = build_messages(provider_name, prompt)

    response_text = provider.chat(
        messages,
        temperature=temperature,
        max_tokens=2000,
    )

    if not response_text:
        raise ValueError("Empty response from LLM")

    try:
        # Prefer JSON inside code fences if present
        fence_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", response_text, re.DOTALL | re.IGNORECASE)
        if fence_match:
            return json.loads(fence_match.group(1))

        # Otherwise, extract the first JSON object in the text
        json_match = re.search(r"\{.*\}", response_text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(0))

        # Last resort: try parsing whole response
        return json.loads(response_text)
    except json.JSONDecodeError as exc:
        preview = response_text.strip().replace("\n", "\\n")
        if len(preview) > 500:
            preview = preview[:500] + "...(truncated)"
        raise ValueError(f"Invalid JSON response: {exc}. Raw: {preview}")


def map_score_to_evaluate(score: int) -> str:
    if score >= 6:
        return "correct"
    if score == 5:
        return "unclear"
    return "incorrect"


def load_env_file(env_path: str = ENV_FILE) -> None:
    path = Path(env_path)
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def resolve_api_key(provider_name: str, cli_key: Optional[str]) -> Optional[str]:
    if cli_key:
        return cli_key
    env_key = f"{provider_name.upper()}_API_KEY"
    env_val = os.getenv(env_key)
    if env_val:
        return env_val
    config_key = PROVIDER_API_KEYS.get(provider_name)
    if config_key:
        return config_key
    return None


def resolve_env_override(provider_name: str, suffix: str) -> Optional[str]:
    env_key = f"{provider_name.upper()}_{suffix}"
    return os.getenv(env_key)


def build_arg_parser() -> argparse.ArgumentParser:
    provider_choices = sorted(PROVIDER_CONFIGS.keys()) + ["ollama"]

    parser = argparse.ArgumentParser(
        description="QA Output Evaluator - Semantic grading vs gold answers",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python evaluate_v2.py --pred qa/output/qa_output.json --gold qa/full_qa.json --api-key YOUR_KEY

  # With custom output path
  python evaluate_v2.py --pred qa/output/qa_output.json --gold qa/full_qa.json \\
      --output results/qa_output_scored.json

Scoring:
  Score >= 6: PASS
  Score = 5: BORDERLINE
  Score <= 4: FAIL
        """,
    )
    parser.add_argument("--pred", required=True, help="Predicted QA JSON file")
    parser.add_argument("--gold", required=True, help="Gold QA JSON file")
    parser.add_argument(
        "--output",
        help="Output file path. If a directory, the file will be created inside it.",
    )
    parser.add_argument(
        "--provider",
        choices=provider_choices,
        default=DEFAULT_PROVIDER,
        help=f"LLM provider (default: {DEFAULT_PROVIDER})",
    )
    parser.add_argument("--model", help="Model name to use (overrides default)")
    parser.add_argument("--api-key", help="LLM API key (or set {PROVIDER}_API_KEY env var)")
    parser.add_argument("--base-url", help="Custom base URL for OpenAI-compatible APIs")
    parser.add_argument("--ollama-model", default="qwen2.5:7b", help="Ollama model name")
    parser.add_argument("--ollama-url", default="http://localhost:11434", help="Ollama base URL")
    parser.add_argument(
        "--temperature",
        type=float,
        default=DEFAULT_TEMPERATURE,
        help=f"Temperature for LLM (default: {DEFAULT_TEMPERATURE})",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=DEFAULT_SLEEP,
        help=f"Sleep time between requests in seconds (default: {DEFAULT_SLEEP})",
    )

    return parser


def print_statistics(data: List[Dict]) -> None:
    evaluate_counts = {"correct": 0, "incorrect": 0, "unclear": 0, "error": 0}
    score_sum = 0
    score_count = 0
    score_dist = {i: 0 for i in range(1, 11)}

    for item in data:
        evaluate = item.get("evaluate", "error")
        evaluate_counts[evaluate] = evaluate_counts.get(evaluate, 0) + 1

        score = item.get("score", 0)
        if score > 0:
            score_sum += score
            score_count += 1
            if 1 <= score <= 10:
                score_dist[score] += 1

    total = len(data)
    avg_score = score_sum / score_count if score_count > 0 else 0

    print("Evaluation Summary:")
    print(f"   Total      : {total}")
    print(f"   Correct    : {evaluate_counts['correct']:3d} ({evaluate_counts['correct']/total*100:5.1f}%) [score >= 6]")
    print(f"   Unclear    : {evaluate_counts['unclear']:3d} ({evaluate_counts['unclear']/total*100:5.1f}%) [score = 5]")
    print(f"   Incorrect  : {evaluate_counts['incorrect']:3d} ({evaluate_counts['incorrect']/total*100:5.1f}%) [score <= 4]")
    print(f"   Error      : {evaluate_counts['error']:3d} ({evaluate_counts['error']/total*100:5.1f}%)")
    print(f"   Avg Score  : {avg_score:.2f}/10")

    print("\nScore Distribution:")
    for score in range(10, 0, -1):
        count = score_dist[score]
        if count > 0:
            bar = "█" * int(count / total * 50)
            print(f"   {score:2d}: {count:3d} {bar}")


def run_evaluation(config: EvaluatorConfig, provider: LLMProvider, provider_name: str) -> None:
    pred_path = Path(config.pred_path)

    if config.output_path:
        out_path = Path(config.output_path)
        if out_path.exists() and out_path.is_dir():
            output_path = out_path / f"{pred_path.stem}_gold_scored.json"
        else:
            output_path = out_path
    else:
        output_path = pred_path.with_name(f"{pred_path.stem}_gold_scored.json")

    output_path = append_utc_timestamp(output_path)

    pred_data = json.loads(pred_path.read_text(encoding="utf-8"))
    gold_data = json.loads(Path(config.gold_path).read_text(encoding="utf-8"))

    gold_by_id = {item.get("id"): item for item in gold_data if item.get("id")}
    gold_by_question = {
        normalize_question(item.get("question", "")): item for item in gold_data
    }

    total = len(pred_data)
    print(f"Loaded: {pred_path.name}")
    print(f"Gold: {Path(config.gold_path).name}")
    print(f"Total items: {total}")
    print(f"Provider: {provider_name.upper()}")
    if config.base_url:
        print(f"Custom URL: {config.base_url}")
    if config.model:
        print(f"Model: {config.model}")
    print()

    for idx, item in enumerate(pred_data, start=1):
        qid = item.get("id")
        question = item.get("question", "")
        gold_item = gold_by_id.get(qid) or gold_by_question.get(normalize_question(question))

        if not gold_item:
            item["evaluate"] = "error"
            item["score"] = 0
            item["check"] = "Không tìm thấy đáp án chuẩn (gold)"
            print(f"[{idx}] ERROR → missing gold for id={qid}")
            if idx < total:
                time.sleep(config.sleep_time)
            continue

        reference = gold_item.get("answer", "")
        candidate = item.get("answer", "")

        # Clean candidate for evaluation prompt
        candidate_clean = strip_citations(candidate)

        try:
            nli = call_llm(
                provider,
                provider_name,
                question=question,
                reference=reference,
                candidate=candidate_clean,
                temperature=config.temperature,
            )

            score = int(nli.get("score", 0) or 0)
            item["evaluate"] = map_score_to_evaluate(score)
            item["score"] = score
            item["check"] = nli.get("reason", "")
            item["label"] = nli.get("label", "UNKNOWN")
            item["confidence"] = nli.get("confidence", 0)
            item["reference_answer"] = reference

            label = item.get("label", "UNKNOWN")
            conf = float(item.get("confidence", 0) or 0)
            print(f"[{idx}] {label} (score: {score}, confidence: {conf:.2f})")

        except Exception as exc:
            item["evaluate"] = "error"
            item["score"] = 0
            item["check"] = str(exc)
            item["label"] = "ERROR"
            item["confidence"] = 0
            item["reference_answer"] = reference
            print(f"[{idx}] ERROR → {exc}")

        if idx < total:
            time.sleep(config.sleep_time)

    output_path.write_text(
        json.dumps(pred_data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"\n{'='*80}")
    print_statistics(pred_data)
    print(f"\n✅ Saved to: {output_path}")


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()

    load_env_file()
    env_ollama_url = os.getenv("OLLAMA_URL")
    env_ollama_model = os.getenv("OLLAMA_MODEL")

    provider_name = normalize_provider_name(args.provider)
    env_base_url = resolve_env_override(provider_name, "BASE_URL")
    env_model = resolve_env_override(provider_name, "MODEL")

    config = EvaluatorConfig(
        pred_path=args.pred,
        gold_path=args.gold,
        output_path=args.output or "",
        provider=provider_name,
        temperature=args.temperature,
        sleep_time=args.sleep,
        ollama_model=env_ollama_model or args.ollama_model,
        ollama_url=env_ollama_url or args.ollama_url,
        base_url=args.base_url or env_base_url,
        model=args.model or env_model,
    )

    api_key: Optional[str] = None
    provider_kind = PROVIDER_KIND_MAP.get(config.provider)
    if provider_kind == "api":
        api_key = resolve_api_key(config.provider, args.api_key)
        if not api_key:
            provider_env = f"{config.provider.upper()}_API_KEY"
            print("❌ API key required!")
            print("   Use: --api-key YOUR_KEY")
            print(f"   Or set env: export {provider_env}=YOUR_KEY")
            return

    try:
        provider = create_provider(
            provider_name=config.provider,
            api_key=api_key,
            ollama_url=config.ollama_url,
            ollama_model=config.ollama_model,
            ollama_timeout=OLLAMA_TIMEOUT,
            base_url=config.base_url,
            model=config.model,
        )
    except ValueError as exc:
        print(f"❌ {exc}")
        return

    run_evaluation(config, provider, provider_name)


if __name__ == "__main__":
    main()
