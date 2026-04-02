import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


DEFAULT_INPUT = "qa/full_qa.json"
QA_FULL_INPUT = "qa/qa_full.json"
DEFAULT_OUTPUT = "qa/input/qa_input.json"


def ensure_parent_dir(path: str) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def extract_items(data: Any) -> List[Dict[str, Any]]:
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in ("items", "data", "questions", "records"):
            value = data.get(key)
            if isinstance(value, list):
                return value
    raise ValueError("Unsupported JSON structure: expected list or dict with list field")


def to_kb_input(items: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    output: List[Dict[str, Any]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        question = item.get("question")
        if not question:
            continue
        out: Dict[str, Any] = {"question": question}
        if "id" in item:
            out["id"] = item["id"]
        output.append(out)
    return output


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate KB.spec.ts input from a QA JSON file",
    )
    parser.add_argument("--input", default=DEFAULT_INPUT, help="Input JSON file")
    parser.add_argument(
        "--qa-full",
        action="store_true",
        help=f"Use {QA_FULL_INPUT} as input (override default only)",
    )
    parser.add_argument("--output", default=DEFAULT_OUTPUT, help="Output JSON file")
    args = parser.parse_args()

    if args.qa_full and args.input != DEFAULT_INPUT:
        raise SystemExit("--qa-full cannot be used together with --input")

    if args.qa_full:
        args.input = QA_FULL_INPUT

    input_path = Path(args.input)
    if not input_path.exists():
        raise SystemExit(f"Input not found: {input_path}")

    data = json.loads(input_path.read_text(encoding="utf-8"))
    items = extract_items(data)
    kb_input = to_kb_input(items)

    ensure_parent_dir(args.output)
    Path(args.output).write_text(
        json.dumps(kb_input, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"✅ Wrote {len(kb_input)} questions to {args.output}")


if __name__ == "__main__":
    main()
