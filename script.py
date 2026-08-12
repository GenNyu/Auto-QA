"""
RAG Evaluation Dataset Generator with LLM
Generates Vietnamese questions based on 4W1H framework (What, Why, When, How)
"""
import argparse
import json
import os
import re
from datetime import datetime, timezone
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional

from config import (
    DEFAULT_NUM_QUESTIONS,
    DEFAULT_OLLAMA_MODEL,
    DEFAULT_OLLAMA_URL,
    DEFAULT_OUTPUT,
    DEFAULT_PROVIDER,
    MAX_RETRY,
    MAX_TOKENS,
    OLLAMA_TIMEOUT,
    PROVIDER_CONFIGS,
    PROVIDER_KIND_MAP,
    TEMPERATURE,
)
from core.env import load_env_file, resolve_api_key, resolve_env_override
from core.text import normalize_text
from prompts import SYSTEM_MESSAGE, build_user_prompt
from providers.base import LLMProvider
from providers.factory import create_provider, normalize_provider_name

JSON_LIST_PATTERN = re.compile(r"\[.*\]", re.DOTALL)
UTC_TS_PATTERN = re.compile(r".*_\d{8}T\d{6}Z$")
PREVIEW_COUNT = 5
PREVIEW_CHUNK_LEN = 200
ENV_FILE = ".env"
CHUNK_MAX_CHARS = 2000
CHUNK_MIN_CHARS = 400
CHUNK_OVERLAP_PARAGRAPHS = 1


def append_utc_timestamp(output_path: str) -> str:
    """Append UTC timestamp to output filename if missing."""
    path = Path(output_path)
    stem = path.stem
    if UTC_TS_PATTERN.match(stem):
        return output_path

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return str(path.with_name(f"{stem}_{ts}{path.suffix}"))


def ensure_parent_dir(path: str) -> None:
    """Ensure parent directory exists for a file path."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)


@dataclass
class QAPair:
    """Question-Answer pair with context."""

    question: str
    file: str
    chunk: str
    answer: str = ""
    evaluate: str = ""
    score: str = ""
    check: str = ""


@dataclass(frozen=True)
class AppConfig:
    """Runtime configuration for the generator."""

    input_path: str
    output_path: str
    num_questions: int
    provider: str
    preview: bool
    ollama_model: str
    ollama_url: str
    use_sampling: bool = True
    base_url: Optional[str] = None
    model: Optional[str] = None


def parse_json_list(response_text: str) -> List[Dict]:
    """Extract and parse the first JSON list from a response."""

    json_match = JSON_LIST_PATTERN.search(response_text)
    if not json_match:
        return []

    raw_json = json_match.group(0)
    try:
        return json.loads(raw_json)
    except json.JSONDecodeError:
        repaired = repair_invalid_json_escapes(raw_json)
        try:
            return json.loads(repaired)
        except json.JSONDecodeError as exc:
            print(f"⚠️  Invalid JSON returned by LLM: {exc}")
            return []


def repair_invalid_json_escapes(raw_json: str) -> str:
    """Best-effort fix for invalid backslash escapes in JSON strings."""

    valid_escapes = {'"', "\\", "/", "b", "f", "n", "r", "t"}
    chars: List[str] = []
    idx = 0

    while idx < len(raw_json):
        ch = raw_json[idx]
        if ch != "\\":
            chars.append(ch)
            idx += 1
            continue

        if idx + 1 >= len(raw_json):
            chars.append("\\\\")
            idx += 1
            continue

        nxt = raw_json[idx + 1]
        if nxt in valid_escapes:
            chars.append(ch)
            chars.append(nxt)
            idx += 2
            continue

        if nxt == "u" and idx + 5 < len(raw_json):
            hex_part = raw_json[idx + 2 : idx + 6]
            if all(c in "0123456789abcdefABCDEF" for c in hex_part):
                chars.append(ch)
                chars.append(nxt)
                chars.append(hex_part)
                idx += 6
                continue

        chars.append("\\\\")
        idx += 1

    return "".join(chars)


class QuestionGenerator:
    """Main generator - chunked document analysis."""

    def __init__(
        self,
        document_path: str,
        provider: LLMProvider,
        provider_name: str,
        max_doc_tokens: int = 50000
    ):
        self.document_path = Path(document_path)
        self.provider = provider
        self.provider_name = provider_name
        self.max_doc_tokens = max_doc_tokens

        raw_content = self.document_path.read_text(
            encoding="utf-8", errors="ignore"
        )
        self.filename = self.document_path.name

        print(f"Loaded: {self.filename}")
        print(f"   Size: {len(raw_content):,} characters")
        print(f"   Provider: {self.provider_name.upper()}")
        
        self.document_content = raw_content
        self.chunks = build_chunks(raw_content)
        if not self.chunks:
            self.chunks = [raw_content]
        print(f"   Chunks: {len(self.chunks)}")


    def generate_questions(
        self, num_questions: int = DEFAULT_NUM_QUESTIONS
    ) -> List[QAPair]:
        target = num_questions
        valid_pairs: List[QAPair] = []

        print(f"\nTarget questions: {target}")
        per_chunk_target = max(1, int(round(target / len(self.chunks))))

        print(f"Chunk strategy: ~{per_chunk_target} questions/chunk")

        for idx, chunk in enumerate(self.chunks, 1):
            if len(valid_pairs) >= target:
                break

            remaining = target - len(valid_pairs)
            ask_for = min(remaining, per_chunk_target)
            added = self._generate_for_chunk(chunk, idx, ask_for, target, valid_pairs)
            if added == 0:
                print("   ⚠️  No valid questions added for this chunk")

        # Retry passes if still short
        pass_num = 0
        prev_count = len(valid_pairs)
        while len(valid_pairs) < target and pass_num < MAX_RETRY:
            pass_num += 1
            remaining = target - len(valid_pairs)
            print(f"\nRetry pass {pass_num} (need {remaining} more)")
            for idx, chunk in enumerate(self.chunks, 1):
                if len(valid_pairs) >= target:
                    break
                ask_for = min(remaining, max(1, per_chunk_target // 2))
                self._generate_for_chunk(chunk, idx, ask_for, target, valid_pairs)
                remaining = target - len(valid_pairs)

            if len(valid_pairs) == prev_count:
                print("   ⚠️  No progress in retry pass, stopping early")
                break
            prev_count = len(valid_pairs)

        if len(valid_pairs) < target:
            print(f"\n⚠️  Only generated {len(valid_pairs)}/{target} valid questions")
            print(f"   💡 Tips:")
            print(f"      - Document may be too large (try splitting)")
            print(f"      - Try different provider (--provider anthropic)")
            print(f"      - Reduce number of questions (--num-questions 10)")
        else:
            print(f"\n✅ Successfully generated {len(valid_pairs)} questions")

        return valid_pairs

    def _build_prompt(self, remaining: int, chunk: str, chunk_id: int) -> str:
        return build_user_prompt(
            chunk,
            self.filename,
            remaining,
            chunk_id=chunk_id,
            total_chunks=len(self.chunks),
        )

    def _build_messages(self, prompt: str) -> List[Dict[str, str]]:
        if self.provider_name == "anthropic":
            return [{"role": "user", "content": prompt}]

        return [
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": prompt},
        ]

    def _parse_questions(self, response_text: str) -> List[Dict]:
        if not response_text:
            print("   ❌ Empty response from LLM")
            return []
        
        questions = parse_json_list(response_text)
        if questions:
            print(f"   ✅ Generated {len(questions)} questions from LLM")
            return questions

        preview = response_text[:500].replace('\n', ' ')
        print(f"   ⚠️  No valid JSON found in response")
        print(f"   📝 Response preview: {preview}...")
        
        if self.provider.last_error:
            print(f"   ❌ Provider error: {self.provider.last_error}")

        return []

    def _extend_valid_pairs(
        self,
        generated: List[Dict],
        chunk: str,
        target: int,
        valid_pairs: List[QAPair],
    ) -> int:
        rejected_count = 0
        rejected_reasons = {
            'missing_fields': 0,
            'duplicate': 0
        }
        added = 0

        for item in generated:
            if len(valid_pairs) >= target:
                break

            question = item.get("question", "").strip()
            gold_answer = item.get("gold_answer", "").strip()

            if not question or not gold_answer:
                rejected_count += 1
                rejected_reasons['missing_fields'] += 1
                continue

            if any(q.question == question for q in valid_pairs):
                rejected_count += 1
                rejected_reasons['duplicate'] += 1
                continue

            valid_pairs.append(
                QAPair(
                    question=question,
                    file=self.filename,
                    chunk=chunk,
                    check=gold_answer,  # Gold answer từ LLM
                )
            )
            added += 1
        
        if rejected_count > 0:
            print(f"   ℹ️  Rejected: {rejected_count} questions")
            for reason, count in rejected_reasons.items():
                if count > 0:
                    print(f"      - {reason}: {count}")
        return added

    def _generate_for_chunk(
        self,
        chunk: str,
        chunk_id: int,
        ask_for: int,
        target: int,
        valid_pairs: List[QAPair],
    ) -> int:
        if ask_for <= 0:
            return 0

        print(f"\nChunk {chunk_id}/{len(self.chunks)} | Requesting: {ask_for} questions")
        prompt = self._build_prompt(ask_for, chunk, chunk_id)
        messages = self._build_messages(prompt)
        response_text = self.provider.chat(
            messages,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
        )

        generated = self._parse_questions(response_text)
        print(f"   Raw generated: {len(generated)}")
        added = self._extend_valid_pairs(generated, chunk, target, valid_pairs)
        print(f"   Valid so far: {len(valid_pairs)}")
        return added

    def _print_statistics(self, qa_pairs: List[QAPair]) -> None:
        if not qa_pairs:
            return

        type_counts: Dict[str, int] = {}
        for pair in qa_pairs:
            q_type = classify_question_type(pair.question)
            type_counts[q_type] = type_counts.get(q_type, 0) + 1

        print("\nQuestion Distribution:")
        for q_type, count in sorted(type_counts.items(), key=lambda x: -x[1]):
            ratio = count / len(qa_pairs) * 100
            print(f"   {q_type:<10}: {count:2d} ({ratio:.1f}%)")

        print(f"   TOTAL     : {len(qa_pairs)}")


def classify_question_type(question: str) -> str:
    q = question.lower().strip()

    if any(w in q for w in ["ai ", "ai là ", "ai chịu", "ai có trách nhiệm"]):
        return "who"

    if any(w in q for w in ["ở đâu", "tại đâu", "thuộc đâu", "áp dụng ở"]):
        return "where"

    if any(
        w in q
        for w in ["khi nào", "thời gian", "thời điểm", "lúc nào", "deadline"]
    ):
        return "when"

    if any(w in q for w in ["tại sao", "vì sao", "lý do"]):
        return "why"

    if any(w in q for w in ["như thế nào", "làm thế nào", "làm sao", "cách"]):
        return "how"

    if any(
        w in q
        for w in ["điều kiện", "trường hợp", "khi nào thì", "nếu", "ngoại lệ"]
    ):
        return "condition"

    if any(
        w in q
        for w in ["gồm những", "bao gồm", "liệt kê", "các bước", "những gì"]
    ):
        return "list"

    if any(w in q for w in ["là gì", "gì", "nội dung"]):
        return "what"

    return "unknown"


def extract_chunk_verbatim(document_text: str, answer_text: str) -> str:
    """
    Trả về đoạn trích NGUYÊN VĂN nếu answer_text xuất hiện trong document_text.
    Nếu không match 100% → trả về chuỗi rỗng.
    """

    if not answer_text:
        return ""

    start = document_text.find(answer_text)
    if start == -1:
        return ""

    return document_text[start : start + len(answer_text)]


def split_into_paragraphs(text: str) -> List[str]:
    """Split text into paragraphs using blank lines as separators."""
    blocks = re.split(r"\n\s*\n", text)
    return [b.strip() for b in blocks if b.strip()]


def build_chunks(
    text: str,
    max_chars: int = CHUNK_MAX_CHARS,
    min_chars: int = CHUNK_MIN_CHARS,
    overlap_paragraphs: int = CHUNK_OVERLAP_PARAGRAPHS,
) -> List[str]:
    """Build chunks from paragraphs with max/min char limits and overlap."""
    paragraphs = split_into_paragraphs(text)
    if not paragraphs:
        return []

    chunks: List[str] = []
    current: List[str] = []
    current_len = 0

    def flush() -> None:
        nonlocal current, current_len
        if not current:
            return
        chunks.append("\n\n".join(current))
        if overlap_paragraphs > 0:
            current = current[-overlap_paragraphs:]
            current_len = sum(len(p) for p in current) + (2 * (len(current) - 1))
        else:
            current = []
            current_len = 0

    for para in paragraphs:
        para_len = len(para)
        if not current:
            current.append(para)
            current_len = para_len
            if current_len >= max_chars:
                flush()
            continue

        if current_len + 2 + para_len <= max_chars:
            current.append(para)
            current_len += 2 + para_len
            continue

        if current_len >= min_chars:
            flush()
            current.append(para)
            current_len = para_len
            if current_len >= max_chars:
                flush()
            continue

        # If current is too small, force add even if it exceeds max
        current.append(para)
        current_len += 2 + para_len
        flush()

    if current:
        chunks.append("\n\n".join(current))

    return chunks


def build_arg_parser() -> argparse.ArgumentParser:
    provider_choices = sorted(PROVIDER_CONFIGS.keys()) + ["ollama", "api"]

    parser = argparse.ArgumentParser(
        description="RAG Evaluation Generator - Vietnamese questions based on 4W1H",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single file
  python script.py --input document.txt
  
  # Nhiều files
  python script.py --input file1.md file2.md file3.md
  
  # Truyền cả thư mục (tự scan .md/.txt bên trong)
  python script.py --input kb_files/
  
  # With custom provider
  python script.py --input kb_files/ --provider openai --api-key YOUR_KEY
        """
    )
    parser.add_argument(
        "--input", required=True, nargs="+",
        help="Input: 1+ files hoặc 1 thư mục (ví dụ: --input kb_files/)"
    )
    parser.add_argument("--output", default=DEFAULT_OUTPUT, help="Output JSON file")
    parser.add_argument(
        "--num-questions",
        type=int,
        default=DEFAULT_NUM_QUESTIONS,
        help="Number of questions per file (default: 20)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate even if files were already processed (clears cache)",
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
    parser.add_argument(
        "--base-url",
        help="Custom base URL for OpenAI-compatible APIs",
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Preview questions without saving",
    )
    parser.add_argument(
        "--no-timestamp",
        action="store_true",
        help="Use --output verbatim instead of appending a UTC timestamp",
    )
    parser.add_argument(
        "--model",
        help="Model name to use (Overrides default for provider)",
    )
    return parser


def preview_dataset(dataset: List[Dict]) -> bool:
    print("\n" + "=" * 80)
    print("PREVIEW (first 5 questions)")
    print("=" * 80)

    for i, item in enumerate(dataset[:PREVIEW_COUNT], 1):
        chunk_preview = item["chunk"][:PREVIEW_CHUNK_LEN]
        print(f"\n[{i}] Câu hỏi: {item['question']}")
        print(f"    File: {item['file']}")
        print(f"    Chunk: {chunk_preview}...")
        print("-" * 80)

    save = input("\nSave to file? (y/n): ").strip().lower()
    return save == "y"


# ============================
# MULTI-FILE SUPPORT
# ============================

def resolve_input_paths(inputs: List[str]) -> List[str]:
    """
    Nếu input là thư mục → scan .md/.txt bên trong.
    Nếu là file → dùng trực tiếp.
    """
    paths: List[str] = []
    for inp in inputs:
        p = Path(inp)
        if p.is_dir():
            for f in sorted(p.iterdir()):
                if f.is_file() and f.suffix in (".md", ".txt") and not f.name.startswith("_"):
                    paths.append(str(f))
        elif p.is_file():
            paths.append(str(p))
        else:
            print(f"⚠️  Skipping: {inp} (not found)")
    return paths


def get_processed_tracker_path(output_path: str) -> str:
    """Get cache path based on output file - mỗi project có cache riêng."""
    output = Path(output_path)
    # runs/engr/questions.json → cache/engr_processed.json
    project_name = output.parent.name if output.parent.name else "default"
    return f"cache/{project_name}_processed.json"

def load_processed(output_path: str) -> Dict[str, int]:
    """Load danh sách file đã process + số câu hỏi generated."""
    tracker_path = get_processed_tracker_path(output_path)
    if not Path(tracker_path).exists():
        return {}
    try:
        return json.loads(Path(tracker_path).read_text(encoding="utf-8"))
    except:
        return {}

def save_processed(processed: Dict[str, int], output_path: str):
    tracker_path = get_processed_tracker_path(output_path)
    ensure_parent_dir(tracker_path)
    Path(tracker_path).write_text(
        json.dumps(processed, ensure_ascii=False, indent=2), encoding="utf-8"
    )


# ============================
# MAIN
# ============================

def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()
    if not args.no_timestamp:
        args.output = append_utc_timestamp(args.output)
    ensure_parent_dir(args.output)

    load_env_file()
    env_ollama_url = os.getenv("OLLAMA_URL")
    env_ollama_model = os.getenv("OLLAMA_MODEL")

    provider_name = normalize_provider_name(args.provider)
    env_base_url = resolve_env_override(provider_name, "BASE_URL")
    env_model = resolve_env_override(provider_name, "MODEL")

    # ── Setup provider 1 lần ──
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

    # ── Resolve input files ──
    input_files = resolve_input_paths(args.input)
    if not input_files:
        print("❌ No valid input files found.")
        return

    print(f"📂 Found {len(input_files)} input files:")
    for f in input_files:
        print(f"   📄 {f}")

    # ── Resume: load đã process ──
    processed = load_processed(args.output)

    # ── Force flag: clear cache if --force ──
    if args.force:
        print("🔄 Force mode: clearing processed cache...")
        processed = {}
        save_processed({}, args.output)
        # Also clear existing output file
        if Path(args.output).exists():
            print(f"🗑️  Clearing existing output: {args.output}")
            Path(args.output).unlink()

    # ── Load existing output nếu có ──
    all_questions: List[Dict] = []
    if Path(args.output).exists():
        try:
            all_questions = json.loads(Path(args.output).read_text(encoding="utf-8"))
            print(f"📌 Loaded {len(all_questions)} existing questions from {args.output}")
        except:
            all_questions = []

    # ── Loop từng file ──
    skipped = 0
    total_new = 0

    for idx, file_path in enumerate(input_files):
        file_name = Path(file_path).name
        print(f"\n{'=' * 50}")
        print(f"📄 [{idx + 1}/{len(input_files)}] {file_name}")
        print(f"{'=' * 50}")

        # Skip nếu đã process
        if file_name in processed:
            print(f"   ⏭️  Already processed ({processed[file_name]} questions). Skipping.")
            skipped += 1
            continue

        # Generate questions cho file này
        generator = QuestionGenerator(
            file_path,
            provider=provider,
            provider_name=provider_name,
        )

        qa_pairs = generator.generate_questions(args.num_questions)
        if not qa_pairs:
            print(f"   ❌ No questions generated for {file_name}")
            continue

        generator._print_statistics(qa_pairs)

        new_questions = [asdict(pair) for pair in qa_pairs]
        all_questions.extend(new_questions)
        total_new += len(new_questions)

        # Mark processed + save output incremental sau mỗi file
        processed[file_name] = len(new_questions)
        save_processed(processed, args.output)

        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(all_questions, f, ensure_ascii=False, indent=2)

        print(f"   ✅ +{len(new_questions)} questions. Total: {len(all_questions)}")

    # ── Preview nếu cần ──
    if args.preview and not preview_dataset(all_questions):
        print("Cancelled.")
        return

    # ── Final summary ──
    print(f"\n{'=' * 50}")
    print(f"✅ Done!")
    print(f"   📥 New questions:  {total_new}")
    print(f"   ⏭️  Skipped files: {skipped}")
    print(f"   📁 Total in {args.output}: {len(all_questions)}")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    main()
