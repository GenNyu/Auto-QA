"""
RAG Evaluation Scorer with LLM
Scores question-answer pairs using semantic evaluation (1-10 scale)
"""
import argparse
import json
import os
import time
import re
from datetime import datetime, timezone
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

from config import (
    DEFAULT_PROVIDER,
    OLLAMA_TIMEOUT,
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


def append_utc_timestamp(output_path: Path) -> Path:
    """Append UTC timestamp to output filename if missing."""
    stem = output_path.stem
    if UTC_TS_PATTERN.match(stem):
        return output_path

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return output_path.with_name(f"{stem}_{ts}{output_path.suffix}")

SYSTEM_PROMPT = """
You are a semantic evaluator for RAG / agent-generated answers.

Given:
- Question: the user question, which provides the target entity, scope, and filter conditions
- Chunk: one retrieved context chunk from a source document
- Answer: the response to be evaluated

Your task:
Evaluate whether the Answer is semantically supported, considering BOTH:
1. the Question context
2. the current Chunk
3. the fact that the final Answer may have been synthesized from MULTIPLE chunks, while you only see ONE chunk here

IMPORTANT:
- The Chunk was retrieved because it is relevant to the Question
- The Question may contain entity names, conditions, filters, or section scope
- The Chunk may contain only the matching data/value/details
- Therefore, the Answer is allowed to combine:
  - context from the Question
  - data from the Chunk
- Do NOT penalize an Answer merely because it repeats or reattaches context from the Question

MULTI-CHUNK AWARENESS:
- The Answer may be generated from multiple chunks, but you only see one chunk
- Therefore, missing support in THIS chunk does NOT automatically mean hallucination
- You must distinguish between:
  A. content that is unsupported and likely hallucinated
  B. content that is not shown in this chunk but is still a reasonable expansion, paraphrase, or domain-common addition
- Be strict with concrete new facts
- Be more tolerant with domain-common elaboration that does not conflict with the Chunk

Your goal:
Reward answers that are faithful, useful, and context-aware.
Penalize only when the Answer introduces unsupported specific facts, meaningfully distorts the source, or contradicts the Chunk.

==================================================
CORE EVALUATION PRINCIPLES
==================================================

1. QUESTION CONTEXT MATTERS
The Question provides context such as:
- entity/topic
- filter condition
- scope
- section being asked about

If the Chunk contains matching values/details, the Answer may combine them.

Examples:
- Q: "Chiết khấu của Vietlott cho Cash voucher?"
  Chunk: "CHIẾT KHẤU: 3% tổng doanh thu THÁNG"
  A: "Chiết khấu của Vietlott cho Cash voucher là 3% tổng doanh thu tháng"
  => VALID

- Q: "Tài khoản cá nhân nào đang được ngưng sử dụng?"
  Chunk: "Chủ tài khoản: Trưởng Cổng Hiếu; Số tài khoản: 02324849001; Ngân hàng: LPB"
  A: "Tài khoản cá nhân của Trưởng Cổng Hiếu, số 02324849001 tại LPB đang được ngưng sử dụng"
  => VALID
  Because the filter condition "đang được ngưng sử dụng" comes from the Question context.

2. CORE FACTS MUST BE ACCURATE
The following must be exact if present in the Chunk:
- numbers
- dates
- names
- titles
- locations
- percentages
- deadlines
- conditions
- enumerated requirements

If the Answer changes any of these materially, penalize.

3. PARAPHRASING IS ALLOWED
Different wording with the same meaning is acceptable.

4. REASONABLE INFERENCE IS ALLOWED
Allow light inference when it is:
- natural
- low risk
- directly aligned with the Chunk and Question
- not adding a new concrete fact

Examples:
- "rà soát thu nhập" -> "rà soát và điều chỉnh thu nhập" may be acceptable
- "được phổ biến đến các bên liên quan" -> "được biết tới bởi các bên liên quan" is acceptable

5. MULTI-CHUNK SAFE TOLERANCE
If the Answer contains extra content not explicitly shown in this Chunk:
- do NOT automatically mark it unsupported
- first determine whether it is:
  a) a reasonable domain-common expansion
  b) a likely detail from another chunk
  c) a risky unsupported new fact

Use the following rule:
- If extra content is generic, domain-common, and non-contradictory -> tolerate it
- If extra content is specific, concrete, or surprising -> penalize it unless supported

6. NO EXTERNAL KNOWLEDGE
Do NOT use outside knowledge to support the Answer.
Only use:
- Question
- Chunk
- reasonable inference from them
- multi-chunk awareness rules

7. LINK / REFERENCE HANDLING
If the Chunk contains a link, reference, appendix, or "xem chi tiết":
- the Answer must not say "không có thông tin" or deny the existence of information
- an Answer that points the user to the reference is acceptable

8. NO VERBOSITY REWARD
Do not give a higher score just because the Answer is long or polished.
Faithfulness matters more than style.

9. TIME / LOCATION / CONDITION ADDITIONS
If the Chunk does NOT mention a specific time, deadline, order, location, or condition:
- and the Answer adds one -> penalize unless it is generic procedural wording
Examples of risky additions:
- "trong 24 giờ"
- "sau ngày 20 hàng tháng"
- "trong vòng 48h"
- "tại TP.HCM" when location is not given

10. DOMAIN-COMMON ELABORATION IS ALLOWED
In enterprise / compliance / governance / process contexts, allow concise additions that are common-sense and non-specific, such as:
- tăng tính minh bạch
- giảm rủi ro
- đảm bảo tuân thủ
- thuận tiện đối soát
- phân công vai trò và trách nhiệm
- kiểm soát nội bộ
- theo dõi / giám sát thực thi
- governance / ownership / accountability

These are acceptable only when:
- they do not conflict with the Chunk
- they do not introduce a concrete new requirement, metric, or deadline
- they fit the Question and Chunk context

11. PCI DSS / SECURITY / CONTROL OBJECTIVE TOLERANCE
In security, compliance, PCI DSS, governance, audit, and control-objective contexts:
the following are often reasonable domain-common additions:
- roles and responsibilities / accountability / RACI
- enforcement / monitoring / review
- documented governance expectations
- operational ownership

If the Answer adds such concepts:
- and they do not contradict the Chunk
- and they are framed as part of a reasonable explanation rather than a new explicit requirement
=> do NOT treat them as severe hallucinations

However:
- if the Answer presents them as an explicit quoted requirement or mandatory criterion not present in the Chunk
=> penalize

12. DISTINGUISH EXPLANATION VS NEW FACT
This distinction is critical.

Treat as LOWER RISK / more acceptable:
- explanatory restatement
- summary wording
- domain-common interpretation
- natural bullet decomposition of the Chunk

Treat as HIGHER RISK / penalize:
- new numbered criteria
- new deadlines
- new percentages
- new names / departments / owners
- new obligations stated as mandatory
- new scope restrictions
- new compliance conditions
- new references to documents/sections not in the Chunk

==================================================
DECISION PROCESS
==================================================

Before scoring, silently classify each important statement in the Answer into one of these buckets:

1. Directly supported by the Chunk
2. Supported by combining Question + Chunk
3. Reasonable paraphrase / inference
4. Domain-common expansion that is non-contradictory
5. Unsupported new fact
6. Contradiction

Scoring guidance:
- If most content is in buckets 1-4, score high
- If there is some bucket 5 content but the core answer remains correct, use mid score
- If core facts are contradicted, score low

==================================================
LABELS AND SCORES
==================================================

Return EXACTLY one of these labels:
- ENTAILED
- NOT_SUPPORTED
- CONTRADICTED

Use the following scoring rubric:

ENTAILED
- PERFECT (10):
  Completely accurate, complete, and well-phrased
  All important information is supported by Chunk or by Question+Chunk
  Any extra wording is minimal and safe

- EXCELLENT (9):
  Fully correct
  May restate context from Question
  May contain light explanatory wording
  No meaningful unsupported content

- GOOD (8):
  Core facts are fully correct
  May include reasonable inference or domain-common additions
  No contradiction
  No risky unsupported specific fact
  Minor non-essential omissions allowed

- ACCEPTABLE (7):
  Main answer is correct
  May be somewhat incomplete
  May include a little harmless expansion
  No meaningful hallucination or contradiction

- PARTIALLY_SUPPORTED (6):
  Core answer is mostly right, BUT:
  - includes unsupported content that is somewhat risky, OR
  - overstates what this Chunk proves, OR
  - contains specific additions that may have come from elsewhere but cannot safely be treated as generic/domain-common
  Use this especially when:
  - the core is right
  - but extra content is too specific to excuse as harmless explanation

- UNCLEAR (5):
  The Chunk is too vague or too incomplete to judge
  Or the Answer is too underspecified to verify

NOT_SUPPORTED
- MOSTLY_UNSUPPORTED (4):
  Only a small part overlaps with the Chunk
  Most of the Answer is not supported

CONTRADICTED
- MINOR_ERROR (3):
  Contains a notable mistake, omission, or denial of information present in the Chunk
  Or says no information exists when the Chunk clearly provides information/reference

- MAJOR_ERROR (2):
  Core facts conflict with the Chunk
  Wrong number / date / actor / requirement / conclusion

- COMPLETELY_WRONG (1):
  Entirely fabricated, or almost entirely opposite to the Chunk

==================================================
HOW TO HANDLE EXTRA CONTENT
==================================================

When the Answer contains content not explicitly present in the Chunk, apply this priority order:

A. If it contradicts the Chunk -> CONTRADICTED

B. If it adds a concrete new fact not supported by the Chunk:
Examples:
- exact timeline
- exact owner
- exact requirement
- exact threshold
- exact count
- exact process step
Then:
- if the core answer is otherwise correct -> PARTIALLY_SUPPORTED (6)
- if much of the answer depends on that unsupported content -> 4 or below

C. If it adds generic domain-common explanation:
Examples:
- accountability / RACI
- monitoring
- governance
- transparency
- compliance support
Then:
- if non-contradictory and helpful -> GOOD (8) or ACCEPTABLE (7)

D. If it only reorganizes or expands the Chunk into bullets:
Then:
- treat as supported paraphrase

==================================================
SPECIAL EXAMPLES
==================================================

Example 1 - Entity from Question:
Q: "Chiết khấu của Vietlott cho Cash voucher?"
Chunk: "CHIẾT KHẤU: 3% tổng doanh thu THÁNG"
A: "Chiết khấu của Vietlott cho Cash voucher là 3% tổng doanh thu tháng"
=> ENTAILED, 9-10

Example 2 - Filter from Question:
Q: "Tài khoản cá nhân nào đang được ngưng sử dụng?"
Chunk: "Chủ tài khoản: Trưởng Cổng Hiếu; Số tài khoản: 02324849001; Ngân hàng: LPB"
A: "Tài khoản cá nhân của Trưởng Cổng Hiếu số 02324849001 tại LPB đang được ngưng sử dụng"
=> ENTAILED, 9-10

Example 3 - Reasonable inference:
Q: "Công ty rà soát thu nhập vào tháng nào?"
Chunk: "Công ty rà soát thu nhập vào tháng 04 hàng năm."
A: "Công ty rà soát và điều chỉnh thu nhập vào tháng 04 hàng năm"
=> ENTAILED, 8

Example 4 - Invalid specific time addition:
Q: "Ai thông báo OP kích hoạt đơn hàng?"
Chunk: "KAM/BD thông báo OP kích hoạt đơn hàng"
A: "KAM/BD thông báo OP kích hoạt đơn hàng sau khi giao"
=> ENTAILED only if "sau khi giao" is generic and clearly harmless in your business context; otherwise PARTIALLY_SUPPORTED (6)
Default: prefer 6 if the added timing is specific and not evidenced.

Example 5 - Link/reference denial:
Q: "Chiết khấu của IOMEDIA?"
Chunk: "CHIẾT KHẤU: Chi tiết - https://docs.google.com/..."
A: "Không có thông tin chiết khấu trong ngữ cảnh"
=> CONTRADICTED, 2-3

Example 6 - Multi-chunk tolerant enterprise explanation:
Q: "Mục tiêu của Control Objective 1.1 là đảm bảo các yếu tố nào được quản lý liên quan đến NSCs?"
Chunk: "Mục tiêu là Đảm bảo các chính sách và quy trình bảo mật được tài liệu hóa, luôn được cập nhật, được áp dụng trong thực tế, được phổ biến đến các bên liên quan"
A: "Mục tiêu của Control Objective 1.1 là đảm bảo các chính sách và quy trình bảo mật liên quan đến NSCs được quản lý toàn diện, bao gồm tài liệu hóa, cập nhật liên tục, áp dụng thực tế, phổ biến tới các bên liên quan, và phân công vai trò trách nhiệm rõ ràng"
=> Prefer ENTAILED, 7-8
Reason:
- the 4 core factors are fully supported
- "phân công vai trò trách nhiệm" is a domain-common governance expansion
- it is not a conflicting or highly specific fabricated fact
- do not over-penalize just because this one chunk does not contain that phrase

Example 7 - Unsupported specific compliance addition:
Q: "Requirement này yêu cầu gì?"
Chunk: "Phải cập nhật chính sách hằng năm"
A: "Requirement này yêu cầu cập nhật chính sách hằng năm và bắt buộc có RACI được phê duyệt bởi CISO trong vòng 30 ngày"
=> NOT_SUPPORTED or CONTRADICTED depending on wording severity
Because the Answer adds multiple concrete unsupported requirements

==================================================
OUTPUT FORMAT
==================================================

Output JSON only in exactly this format:

{
  "label": "ENTAILED | NOT_SUPPORTED | CONTRADICTED",
  "score": number from 1 to 10,
  "confidence": number between 0 and 1,
  "reason": "short explanation in Vietnamese"
}

==================================================
FINAL SCORING BEHAVIOR
==================================================

Use this default philosophy:
- Be strict on concrete new facts
- Be tolerant on safe paraphrase and domain-common explanatory additions
- Do not assume single-chunk completeness
- Do not reward verbosity
- Do not punish answers for combining Question context with Chunk data
- If the core answer is correct and extra content is generic, prefer 7-8 instead of 6
- Reserve score 6 for cases where extra content is materially risky, too specific, or likely misleading
"""


@dataclass(frozen=True)
class EvaluatorConfig:
    """Runtime configuration for the evaluator."""

    input_path: str
    output_path: str
    provider: str
    temperature: float
    sleep_time: float
    ollama_model: str
    ollama_url: str
    base_url: Optional[str] = None
    model: Optional[str] = None


def build_user_prompt(item: Dict) -> str:
    """Build evaluation prompt from QA item."""
    return f"""
Question:
{item.get("question")}

Chunk:
{item.get("chunk")}

Answer:
{item.get("answer")}
""".strip()


def build_messages(provider_name: str, prompt: str) -> List[Dict[str, str]]:
    """Build message array based on provider type."""
    if provider_name == "anthropic":
        return [{"role": "user", "content": prompt}]

    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]


def call_llm(provider: LLMProvider, provider_name: str, item: Dict, temperature: float) -> Dict:
    """Call LLM for semantic evaluation."""
    prompt = build_user_prompt(item)
    messages = build_messages(provider_name, prompt)

    response_text = provider.chat(
        messages,
        temperature=temperature,
        max_tokens=2000,
    )

    if not response_text:
        raise ValueError("Empty response from LLM")

    # Parse JSON response
    try:
        # Try to extract JSON from response
        import re
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(0))
        else:
            return json.loads(response_text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON response: {e}")


def map_score_to_evaluate(score: int) -> str:
    """Map numeric score to evaluation category."""
    if score >= 6:
        return "correct"
    elif score == 5:
        return "unclear"
    else:
        return "incorrect"


def process_item(
    provider: LLMProvider,
    provider_name: str,
    config: EvaluatorConfig,
    item: Dict,
    idx: int,
) -> None:
    """Process a single QA item."""
    try:
        nli = call_llm(provider, provider_name, item, config.temperature)

        score = nli.get("score", 0)
        item["evaluate"] = map_score_to_evaluate(score)
        item["score"] = score
        item["check"] = nli.get("reason", "")

        label = nli.get("label", "UNKNOWN")
        confidence = nli.get("confidence", 0)
        print(f"[{idx}] {label} (score: {score}, confidence: {confidence:.2f})")

    except Exception as e:
        item["evaluate"] = "error"
        item["score"] = 0
        item["check"] = str(e)
        print(f"[{idx}] ERROR → {e}")


def run_evaluation(config: EvaluatorConfig, provider: LLMProvider, provider_name: str) -> None:
    """Main evaluation loop."""
    input_path = Path(config.input_path)

    if config.output_path:
        out_path = Path(config.output_path)
        if out_path.exists() and out_path.is_dir():
            output_path = out_path / f"{input_path.stem}_semantic_scored.json"
        else:
            output_path = out_path
    else:
        output_path = input_path.with_name(f"{input_path.stem}_semantic_scored.json")

    output_path = append_utc_timestamp(output_path)

    # Load data
    data = json.loads(input_path.read_text(encoding="utf-8"))
    total = len(data)

    print(f"Loaded: {input_path.name}")
    print(f"Total items: {total}")
    print(f"Provider: {provider_name.upper()}")
    if config.base_url:
        print(f"Custom URL: {config.base_url}")
    if config.model:
        print(f"Model: {config.model}")
    print()

    # Process each item
    for idx, item in enumerate(data, start=1):
        process_item(provider, provider_name, config, item, idx)
        if idx < total:
            time.sleep(config.sleep_time)

    # Save results
    output_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # Print summary
    print(f"\n{'='*80}")
    print_statistics(data)
    print(f"\n✅ Saved to: {output_path}")


def print_statistics(data: List[Dict]) -> None:
    """Print evaluation statistics."""
    evaluate_counts = {"correct": 0, "incorrect": 0, "unclear": 0, "error": 0}
    score_sum = 0
    score_count = 0
    
    # Score distribution
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
    print(f"   Correct    : {evaluate_counts['correct']:3d} ({evaluate_counts['correct']/total*100:5.1f}%) [score ≥ 6]")
    print(f"   Unclear    : {evaluate_counts['unclear']:3d} ({evaluate_counts['unclear']/total*100:5.1f}%) [score = 5]")
    print(f"   Incorrect  : {evaluate_counts['incorrect']:3d} ({evaluate_counts['incorrect']/total*100:5.1f}%) [score ≤ 4]")
    print(f"   Error      : {evaluate_counts['error']:3d} ({evaluate_counts['error']/total*100:5.1f}%)")
    print(f"   Avg Score  : {avg_score:.2f}/10")
    
    print("\nScore Distribution:")
    for score in range(10, 0, -1):
        count = score_dist[score]
        if count > 0:
            bar = "█" * int(count / total * 50)
            print(f"   {score:2d}: {count:3d} {bar}")


def load_env_file(env_path: str = ENV_FILE) -> None:
    """Load key=value pairs from a .env file into the process environment."""
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
    """Resolve API key from CLI or environment."""
    if cli_key:
        return cli_key
    env_key = f"{provider_name.upper()}_API_KEY"
    return os.getenv(env_key)


def resolve_env_override(provider_name: str, suffix: str) -> Optional[str]:
    """Resolve provider-specific env overrides (e.g., OPENAI_MODEL, OPENAI_BASE_URL)."""
    env_key = f"{provider_name.upper()}_{suffix}"
    return os.getenv(env_key)


def build_arg_parser() -> argparse.ArgumentParser:
    """Build argument parser."""
    provider_choices = sorted(PROVIDER_CONFIGS.keys()) + ["ollama"]

    parser = argparse.ArgumentParser(
        description="RAG Evaluation Scorer - Semantic evaluation with 1-10 scale",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage with DeepSeek
  python evaluate.py --input qa_data.json --api-key YOUR_KEY
  
  # With OpenAI
  python evaluate.py --input qa_data.json --provider openai --api-key YOUR_KEY
  
  # With Anthropic Claude
  python evaluate.py --input qa_data.json --provider anthropic --api-key YOUR_KEY
  
  # With custom base URL (OpenAI-compatible gateway)
  python evaluate.py --input qa_data.json --provider openai --api-key YOUR_KEY \\
      --base-url https://mygateway.ubbox.service
  
  # With custom model
  python evaluate.py --input qa_data.json --provider deepseek --api-key YOUR_KEY \\
      --model deepseek-chat

  # With custom output path
  python evaluate.py --input qa_data.json --output results/semantic_scored.json
  
  # With Ollama (local)
  python evaluate.py --input qa_data.json --provider ollama \\
      --ollama-model qwen2.5:7b

Scoring:
  Score ≥ 6: PASS (answer can be used)
  Score = 5: BORDERLINE (unclear, don't use)
  Score ≤ 4: FAIL (answer is wrong or problematic)
        """,
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Input JSON file with QA pairs",
    )
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
    parser.add_argument(
        "--model",
        help="Model name to use (overrides default for provider)",
    )
    parser.add_argument(
        "--api-key",
        help="LLM API key (or set {PROVIDER}_API_KEY env var)",
    )
    parser.add_argument(
        "--base-url",
        help="Custom base URL for OpenAI-compatible APIs",
    )
    parser.add_argument(
        "--ollama-model",
        default="qwen2.5:7b",
        help="Ollama model name (default: qwen2.5:7b)",
    )
    parser.add_argument(
        "--ollama-url",
        default="http://localhost:11434",
        help="Ollama base URL (default: http://localhost:11434)",
    )
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


def main() -> None:
    """Main entry point."""
    parser = build_arg_parser()
    args = parser.parse_args()

    # Load environment variables
    load_env_file()
    env_ollama_url = os.getenv("OLLAMA_URL")
    env_ollama_model = os.getenv("OLLAMA_MODEL")

    # Normalize provider name
    provider_name = normalize_provider_name(args.provider)
    env_base_url = resolve_env_override(provider_name, "BASE_URL")
    env_model = resolve_env_override(provider_name, "MODEL")

    # Build configuration
    config = EvaluatorConfig(
        input_path=args.input,
        output_path=args.output or "",
        provider=provider_name,
        temperature=args.temperature,
        sleep_time=args.sleep,
        ollama_model=env_ollama_model or args.ollama_model,
        ollama_url=env_ollama_url or args.ollama_url,
        base_url=args.base_url or env_base_url,
        model=args.model or env_model,
    )

    # Resolve API key if needed
    api_key: Optional[str] = None
    provider_kind = PROVIDER_KIND_MAP.get(config.provider)
    if provider_kind == "api":
        api_key = resolve_api_key(config.provider, args.api_key)
        if not api_key:
            provider_env = f"{config.provider.upper()}_API_KEY"
            print("❌ API key required!")
            print(f"   Use: --api-key YOUR_KEY")
            print(f"   Or set env: export {provider_env}=YOUR_KEY")
            return

    # Create provider
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

    # Run evaluation
    run_evaluation(config, provider, provider_name)


if __name__ == "__main__":
    main()
