"""
Normalize PCI DSS test cases from PCI_DSS_filtered.json with LLM-generated questions.
Output schema:
{
  "id": "<id of testing procedure if any>",
  "context": "<pci_dss_requirements>",
  "question": "<rewritten audit-style question>",
  "main_content": "<testing procedures>",
  "check": "<customer only>",
  "file": "",
  "answer": ""
}
"""

import argparse
import json
import os
from pathlib import Path
from typing import Dict, List, Optional

from config import (
    DEFAULT_OLLAMA_MODEL,
    DEFAULT_OLLAMA_URL,
    DEFAULT_PROVIDER,
    MAX_RETRY,
    MAX_TOKENS,
    OLLAMA_TIMEOUT,
    PROVIDER_API_KEYS,
    PROVIDER_CONFIGS,
    PROVIDER_KIND_MAP,
    TEMPERATURE,
)
from providers.base import LLMProvider
from providers.factory import create_provider, normalize_provider_name


DEFAULT_INPUT = "outputs/PCI_DSS_filtered.json"
DEFAULT_OUTPUT = "outputs/PCI_DSS_qa.json"
ENV_FILE = ".env"


SYSTEM_PROMPT = """
You are a PCI DSS auditor.

Your task is to generate a compliance question based on the Testing Procedure.

You are also given internal reference information (DO NOT mention it directly), which represents how a company actually implements the requirement.

Instructions:

* Rewrite the Testing Procedure into a natural, audit-style question
* Use the internal reference ONLY to better understand what the question should focus on
* DO NOT mention any company name, system name, or internal terms
* DO NOT copy phrases directly from the internal reference
* Keep the question neutral and generic (applicable to any organization)
* Focus on compliance outcomes (e.g., approval, testing, documentation)
* Do NOT include PCI DSS requirement IDs or step labels (e.g., "1.1.1.a")

Input:
PCI DSS Requirement:
{{pci_dss_requirements}}

Testing Procedure:
{{testing_procedures}}

Internal Reference (DO NOT EXPOSE):
{{customer_only}}

Output:
A single, clear compliance question.
"""

LABEL_PATTERN = r"\b\d+(?:\.\d+)+(?:\.[a-z])?\b"


def normalize_text(value: str) -> str:
    if value is None:
        return ""
    return " ".join(str(value).split()).strip()


def build_context(pci: str) -> str:
    return pci.strip()


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
    env_value = os.getenv(env_key)
    if env_value:
        return env_value
    return PROVIDER_API_KEYS.get(provider_name)


def resolve_env_override(provider_name: str, suffix: str) -> Optional[str]:
    env_key = f"{provider_name.upper()}_{suffix}"
    value = os.getenv(env_key)
    if value:
        return value
    if provider_name == "anthropic" and suffix == "MODEL":
        return os.getenv("ANTHROPIC_DEFAULT_SONNET_MODEL")
    return None


def build_prompt(req: str, pci: str, testing: str, customer_only: str) -> str:
    return f"""
PCI DSS Requirements:
{pci}

Testing Procedures:
{testing}

Customer Only:
{customer_only}

Yêu cầu:
- Viết đúng 1 câu hỏi tiếng Việt.
- Câu hỏi rõ ràng, tự nhiên, mang phong cách audit.
- Không nhắc hoặc trích lại mã điều khoản/bước kiểm thử (ví dụ: "1.1.1.a").
- KHÔNG nhắc đến tên công ty, hệ thống nội bộ, hoặc thông tin riêng.
- Có thể tham khảo Customer Only để hiểu ý nghĩa, nhưng KHÔNG được lộ nội dung đó.
- Bám theo nội dung PCI DSS Requirements và Testing Procedures.
- Tập trung đúng bước kiểm thử trong Testing Procedures.
- Trả lời chỉ là câu hỏi, không thêm giải thích.
""".strip()


def generate_question(
    provider: LLMProvider,
    provider_name: str,
    req: str,
    pci: str,
    testing: str,
    customer_only: str,
) -> str:
    prompt = build_prompt(req, pci, testing, customer_only)
    if provider_name == "anthropic":
        messages = [{"role": "user", "content": prompt}]
    else:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ]

    response_text = provider.chat(
        messages,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
    )
    return normalize_text(response_text)


def extract_label(text: str) -> str:
    import re
    m = re.search(LABEL_PATTERN, text)
    return m.group(0) if m else ""


def contains_customer_terms(question: str, customer_only: str) -> bool:
    import re
    q = question.lower()
    tokens = re.findall(r"[a-z0-9][a-z0-9\\-_/]+", customer_only.lower())
    tokens = [t for t in tokens if len(t) >= 4]
    if not tokens:
        return False
    for t in set(tokens):
        if t in q:
            return True
    return False


def build_dataset(
    rows: List[Dict],
    provider: LLMProvider,
    provider_name: str,
    limit: Optional[int],
) -> List[Dict]:
    dataset: List[Dict] = []
    skipped = 0
    failed = 0
    total = len(rows) if limit is None else min(len(rows), max(0, limit))

    if limit is not None:
        rows = rows[: max(0, limit)]

    for idx, row in enumerate(rows, 1):
        req = normalize_text(row.get("req", ""))
        raw_pci = row.get("pci_dss_requirements", "") or ""
        raw_testing = row.get("testing_procedures", "") or ""
        raw_customer_only = row.get("customer_only", "") or ""

        pci = normalize_text(raw_pci)
        testing = normalize_text(raw_testing)
        customer_only = normalize_text(raw_customer_only)

        if not pci or not testing or not customer_only:
            skipped += 1
            continue

        question = ""
        for _ in range(MAX_RETRY):
            question = generate_question(
                provider, provider_name, req, pci, testing, customer_only
            )
            if not question:
                continue
            if contains_customer_terms(question, customer_only):
                continue
            break

        if not question:
            failed += 1
            continue

        item = {
            "id": extract_label(testing),
            "context": build_context(raw_pci),
            "question": question,
            "main_content": raw_testing,
            "check": raw_customer_only,
            "file": "",
            "answer": "",
        }
        dataset.append(item)

        if idx % 25 == 0:
            print(f"Processed {idx}/{total} rows...")

    print(f"Loaded rows: {len(rows)}")
    print(f"Generated items: {len(dataset)}")
    print(f"Skipped rows: {skipped}")
    print(f"Failed LLM rows: {failed}")
    return dataset


def build_arg_parser() -> argparse.ArgumentParser:
    provider_choices = sorted(PROVIDER_CONFIGS.keys()) + ["ollama", "api"]
    parser = argparse.ArgumentParser(
        description="Normalize PCI DSS test cases (LLM questions)",
    )
    parser.add_argument("--input", default=DEFAULT_INPUT, help="Input JSON file")
    parser.add_argument("--output", default=DEFAULT_OUTPUT, help="Output JSON file")
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit number of rows to process (for quick test)",
    )
    parser.add_argument("--api-key", help="LLM API key")
    parser.add_argument(
        "--provider",
        choices=provider_choices,
        default=DEFAULT_PROVIDER,
        help=f"LLM provider (default: {DEFAULT_PROVIDER})",
    )
    parser.add_argument(
        "--ollama-model",
        default=DEFAULT_OLLAMA_MODEL,
        help=f"Ollama model (default: {DEFAULT_OLLAMA_MODEL})",
    )
    parser.add_argument(
        "--ollama-url",
        default=DEFAULT_OLLAMA_URL,
        help=f"Ollama base URL (default: {DEFAULT_OLLAMA_URL})",
    )
    parser.add_argument("--base-url", help="Custom base URL for OpenAI-compatible APIs")
    parser.add_argument("--model", help="Model name to use (Overrides default)")
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()

    load_env_file()
    env_ollama_url = os.getenv("OLLAMA_URL")
    env_ollama_model = os.getenv("OLLAMA_MODEL")

    provider_name = normalize_provider_name(args.provider)
    env_base_url = resolve_env_override(provider_name, "BASE_URL")
    env_model = resolve_env_override(provider_name, "MODEL")

    api_key: Optional[str] = None
    provider_kind = PROVIDER_KIND_MAP.get(provider_name)
    if provider_kind == "api":
        api_key = resolve_api_key(provider_name, args.api_key)
        if not api_key:
            provider_env = f"{provider_name.upper()}_API_KEY"
            print("API key required!")
            print("   Use: --api-key YOUR_KEY")
            print(f"   Or set env: export {provider_env}=YOUR_KEY")
            return

    try:
        provider = create_provider(
            provider_name=provider_name,
            api_key=api_key,
            ollama_url=env_ollama_url or args.ollama_url,
            ollama_model=env_ollama_model or args.ollama_model,
            ollama_timeout=OLLAMA_TIMEOUT,
            base_url=args.base_url or env_base_url,
            model=args.model or env_model,
        )
    except ValueError as exc:
        print(f"{exc}")
        return

    in_path = Path(args.input)
    if not in_path.exists():
        raise FileNotFoundError(f"Input not found: {in_path}")

    rows = json.loads(in_path.read_text(encoding="utf-8"))
    if not isinstance(rows, list):
        raise ValueError("Input JSON must be a list of rows")

    dataset = build_dataset(
        rows, provider, provider_name, args.limit
    )

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(dataset, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()
