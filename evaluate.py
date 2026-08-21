"""
RAG Evaluation Scorer with LLM
Scores question-answer pairs using semantic evaluation (1-10 scale)

Pass 1: Evaluate using retrieved chunk
Pass 2: If score <= RECHECK_THRESHOLD, re-evaluate using full source file from KB dir
"""
import argparse
import json
import os
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

from config import (
    DEFAULT_PROVIDER,
    OLLAMA_TIMEOUT,
    PROVIDER_CONFIGS,
    PROVIDER_KIND_MAP,
)
from core.env import load_env_file, resolve_api_key, resolve_env_override
from prompts_evaluate import (
    SYSTEM_PROMPT,
    SYSTEM_PROMPT_CLAIM_EXTRACTOR,
    SYSTEM_PROMPT_PASS2,
)
from providers.base import LLMProvider
from providers.factory import create_provider, normalize_provider_name

# Constants
DEFAULT_TEMPERATURE = 0.0
DEFAULT_SLEEP = 0.3
RECHECK_THRESHOLD = 7  # Re-evaluate with full file if score is in range [5, threshold]

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────

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
    kb_dir: Optional[str] = None          # NEW: directory containing KB .md files
    recheck_threshold: int = RECHECK_THRESHOLD  # NEW: re-evaluate if score <= this
    disable_pass2: bool = False           # NEW: force 1-pass only

    # Join mode: merge a QA output file with a compliance file (e.g. PCI-DSS) by id.
    qa_file: Optional[str] = None
    pci_file: Optional[str] = None
    context_field: str = "pci_dss_requirements"
    expected_field: str = "customer_only"
    main_field: str = "testing_procedures"
    id_field: str = "id"

    @property
    def join_mode(self) -> bool:
        return bool(self.qa_file and self.pci_file)


# ─────────────────────────────────────────────
# KB FILE LOOKUP
# ─────────────────────────────────────────────

# Trailing version marker: _v2, _ver_8, _Ver7, _final_10 …
_VERSION_SUFFIX_RE = re.compile(r'(?:[_-](?:v|ver|version)[_-]?\d+)+$', re.IGNORECASE)
# Leading date stamp: 20260206_
_DATE_PREFIX_RE = re.compile(r'^\d{6,8}[_-]')
# Random hash suffix added by the KB uploader: __76vsy07
_HASH_SUFFIX_RE = re.compile(r'__[a-z0-9]{5,}$', re.IGNORECASE)


def version_base(file_name: str) -> str:
    """
    Normalize a KB filename down to the identity of the DOCUMENT, dropping the
    markers that only distinguish one version of it from another.

        20260619_BD_OPS_..._Chinh_sach_ban_hang_ver_8.md ─┐
        20260127_BD_OPS_..._Chinhsach_ban_hang_Ver7.md   ─┴→ bdops...chinhsachbanhang

    Separators are dropped as well, because the two versions of a document are often
    typed inconsistently ("Chinhsach" vs "Chinh_sach"). Numbering that carries meaning
    survives: Requirement_1_1 and Requirement_1_2 stay distinct documents.

    Two files sharing a base are two versions of the same document, and the KB
    genuinely contains such pairs with conflicting values. The evaluator must see
    all of them, otherwise it flags a correct answer as fabricated.
    """
    stem = Path(file_name).stem
    stem = _HASH_SUFFIX_RE.sub("", stem)
    stem = _DATE_PREFIX_RE.sub("", stem)
    stem = _VERSION_SUFFIX_RE.sub("", stem)
    return re.sub(r'[_\-\s]+', '', stem).lower()


def find_kb_files(file_name: str, kb_dir: str) -> List[Path]:
    """
    Locate every version of a KB document on disk.

    The 'file'/'source' field in JSON is like: 20260206_PRT_DanhSach_Danh_sach_MC_final_10.md
    The actual file on disk may have a random hash suffix added:
        20260206_PRT_DanhSach_Danh_sach_MC_final_10__76vsy07.md

    Strategy:
    1. Exact match, then prefix/loose match, to find the referenced file itself.
    2. Add every other file whose version_base() matches — the sibling versions.

    Returns the referenced file first, siblings after it (sorted by name for
    deterministic prompts). Empty list when nothing matches.
    """
    kb_path = Path(kb_dir)
    if not kb_path.is_dir():
        return []

    stem = Path(file_name).stem
    candidates = sorted(kb_path.glob("*.md"))

    primary: Optional[Path] = None
    exact = kb_path / file_name
    if exact.exists():
        primary = exact
    else:
        for candidate in candidates:
            if candidate.stem.startswith(stem) or stem.startswith(candidate.stem):
                primary = candidate
                break
    if primary is None:
        for candidate in candidates:
            if stem in candidate.stem or candidate.stem in stem:
                primary = candidate
                break

    base = version_base(primary.name if primary else file_name)
    siblings = [
        c for c in candidates
        if c != primary and base and version_base(c.name) == base
    ]

    found = ([primary] if primary else []) + siblings
    return found


def read_kb_file(file_name, kb_dir: str, max_chars: int = 100_000) -> Optional[str]:
    """
    Read full content of the KB source files backing an answer, including every
    sibling version of each one.

    - file_name may be a single filename or a list (the 'source' field is a list).
    - Each file is separated with a clear header so the LLM can attribute claims
      to a specific version.
    - The max_chars budget is split evenly across files, so a later version is
      never dropped entirely just because an earlier one was long.
    """
    files: List[str] = []
    if isinstance(file_name, list):
        for f in file_name:
            if isinstance(f, str) and f.strip():
                files.append(f.strip())
    elif isinstance(file_name, str) and file_name.strip():
        files.append(file_name.strip())
    if not files:
        return None

    paths: List[Path] = []
    for f in files:
        for path in find_kb_files(f, kb_dir):
            if path not in paths:
                paths.append(path)
    if not paths:
        return None

    per_file = max(2_000, max_chars // len(paths))
    parts: List[str] = []
    for path in paths:
        content = path.read_text(encoding="utf-8")
        if len(content) > per_file:
            content = content[:per_file] + f"\n\n[... TRUNCATED AT {per_file} CHARS ...]"
        parts.append(f"\n\n===== FILE: {path.name} =====\n{content}")

    return "".join(parts)


# ─────────────────────────────────────────────
# PROMPT BUILDERS
# ─────────────────────────────────────────────

def strip_citations(text: str) -> str:
    """
    Normalize KB citation artifacts in AI answers before evaluation.

    File references are KEPT, rewritten as [SOURCE: ...]. Deleting them used to
    turn a careful answer ("theo nguồn 1 [ver_8]: 3 tỷ / theo nguồn 2 [Ver7]: 2 tỷ")
    into what looked like a self-contradiction, and the evaluator scored it as a
    hallucination. The version marker is the evidence that the answer is right.
    """
    if not text:
        return ""
    # Normalize truncated file refs like: 20251121_PDT_Da...1leq8gc.md
    text = re.sub(
        r'\d{8}_[A-Za-z0-9_]+(?:\.\.\.)?[A-Za-z0-9_]*\.md',
        lambda m: f'[SOURCE: {m.group(0)}]',
        text,
    )
    # Remove "Nguồn tham khảo:" lines (with or without URL)
    text = re.sub(r'Nguồn tham khảo:[^\n]*', '', text)
    # Remove bare URLs
    text = re.sub(r'https?://\S+', '', text)
    # Clean up leftover punctuation artifacts (standalone dots, multiple newlines)
    text = re.sub(r'\n\s*\.\s*\n', '\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def get_expected_answer(item: Dict) -> str:
    """Get expected answer from item (gold/check/expected)."""
    return str(item.get("gold") or item.get("check") or item.get("expected") or "").strip()


def get_ai_answer(item: Dict) -> str:
    """Get AI answer from item, with citation artifacts removed."""
    raw = str(item.get("answer") or "").strip()
    return strip_citations(raw)


def get_requirement_context(item: Dict) -> str:
    """Get compliance requirement context (join mode only, empty otherwise)."""
    return str(item.get("context") or item.get("pci_dss_requirements") or "").strip()


def get_main_content(item: Dict) -> str:
    """Get the source excerpt backing the question.

    "chunk" is what script.py writes for freshly generated questions; the other
    two names come from the compliance join mode.
    """
    return str(
        item.get("main_content")
        or item.get("testing_procedures")
        or item.get("chunk")
        or ""
    ).strip()


# Shown in place of the expected answer when the item has none, so the judge
# grades against the source excerpt instead of against a blank reference.
NO_EXPECTED_ANSWER = (
    "(none — this item has no expected answer; "
    "grade the AI Answer against the Chunk above)"
)

# Nothing to verify against at all — the rubric says score 5 / NOT_MATCH.
NO_REFERENCE_AT_ALL = (
    "(none — and there is no Chunk either; "
    "you have nothing to verify against, so return score 5 / NOT_MATCH)"
)


def build_user_prompt(item: Dict) -> str:
    """
    Build Pass 1 evaluation prompt from QA item (gold vs AI answer).

    Requirement Context and Main Content are only emitted when the item carries
    them (join mode), so plain KB items keep the original prompt shape.
    """
    sections = [f'Question:\n{item.get("question", "")}']

    requirement_context = get_requirement_context(item)
    if requirement_context:
        sections.append(f"Requirement Context:\n{requirement_context}")

    main_content = get_main_content(item)
    if main_content:
        # Nhãn "Chunk" khớp đúng từ vựng dùng trong prompts_evaluate.py
        sections.append(f"Chunk:\n{main_content}")

    if expected := get_expected_answer(item):
        reference = expected
    else:
        reference = NO_EXPECTED_ANSWER if main_content else NO_REFERENCE_AT_ALL
    sections.append(f"Expected Answer:\n{reference}")
    sections.append(f"AI Answer:\n{get_ai_answer(item)}")

    return "\n\n".join(sections)


def build_user_prompt_claim_extractor(item: Dict) -> str:
    """Build prompt for Claim Extractor — identifies extra claims beyond the expected answer.

    With no reference answer, the source excerpt takes its place so the extractor
    still has something to measure "extra" against.
    """
    reference = get_expected_answer(item) or get_main_content(item) or NO_EXPECTED_ANSWER
    return f"""
Question:
{item.get("question", "")}

Expected Answer:
{reference}

AI Answer:
{get_ai_answer(item)}
""".strip()


def build_user_prompt_pass2(
    item: Dict,
    file_content: str,
    original_chunk: str,
    extra_claims: List[str],
) -> str:
    """Build Pass 2 verification prompt — verifies each extra claim against the full file."""
    if extra_claims:
        claims_block = "\n".join(f"  - {c}" for c in extra_claims)
    else:
        claims_block = "  (none identified — re-evaluate the answer freely against the full file)"

    # Không có đáp án mẫu thì lấy chunk gốc làm chuẩn; không có nữa thì dựa hẳn
    # vào file nguồn đầy đủ bên dưới.
    reference = get_expected_answer(item) or original_chunk.strip() or (
        "(none — verify the AI Answer directly against the Full Source File below)"
    )
    return f"""
Question:
{item.get("question", "")}

Expected Answer:
{reference}

Extra Claims to Verify (identified by Claim Extractor — these were NOT in the Expected Answer above):
{claims_block}

Full Source File Content (search here to verify each claim):
{file_content}

AI Answer:
{get_ai_answer(item)}
""".strip()


def build_messages(provider_name: str, prompt: str, system: str = SYSTEM_PROMPT) -> List[Dict[str, str]]:
    """Build message array based on provider type."""
    if provider_name == "anthropic":
        return [{"role": "user", "content": f"{system}\n\n{prompt}"}]
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": prompt},
    ]


# ─────────────────────────────────────────────
# LLM CALLS
# ─────────────────────────────────────────────

def _strip_code_fences(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        # Remove leading fence with optional language
        text = re.sub(r"^```[a-zA-Z0-9_-]*\s*", "", text)
        # Remove trailing fence
        text = re.sub(r"\s*```$", "", text)
    return text.strip()


def _extract_json_candidate(text: str) -> str:
    start = text.find("{")
    if start == -1:
        return text
    # Find the last position where braces are balanced, respecting strings
    in_str = False
    escape = False
    depth = 0
    last_complete = None
    for i in range(start, len(text)):
        ch = text[i]
        if in_str:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == "\"":
                in_str = False
            continue
        else:
            if ch == "\"":
                in_str = True
                continue
            if ch == "{":
                depth += 1
            elif ch == "}":
                if depth > 0:
                    depth -= 1
                    if depth == 0:
                        last_complete = i
    if last_complete is not None:
        return text[start:last_complete + 1]
    return text[start:]


def _repair_json(text: str) -> str:
    # Best-effort repair for common LLM artifacts
    text = _strip_code_fences(text)
    text = _extract_json_candidate(text)
    # Remove trailing commas before closing braces/brackets
    text = re.sub(r",(\s*[}\]])", r"\1", text)
    return text


def _escape_control_chars_in_strings(text: str) -> str:
    """Escape raw control characters that appear inside JSON strings."""
    chars: List[str] = []
    in_str = False
    escape = False

    for ch in text:
        if in_str:
            if escape:
                chars.append(ch)
                escape = False
                continue
            if ch == "\\":
                chars.append(ch)
                escape = True
                continue
            if ch == "\"":
                chars.append(ch)
                in_str = False
                continue
            if ch == "\n":
                chars.append("\\n")
                continue
            if ch == "\r":
                chars.append("\\r")
                continue
            if ch == "\t":
                chars.append("\\t")
                continue
            chars.append(ch)
            continue

        chars.append(ch)
        if ch == "\"":
            in_str = True

    return "".join(chars)


def _extract_partial_json_fields(response_text: str) -> Optional[Dict]:
    """
    Recover a structured result from malformed or truncated JSON.

    This handles common LLM failures such as:
    - raw newlines inside string values
    - missing closing quote/brace near EOF
    - markdown fences wrapped around a partial object
    """
    text = _strip_code_fences(response_text).strip()
    if not text:
        return None

    result: Dict[str, object] = {}

    label_match = re.search(r'"label"\s*:\s*"([^"]+)"', text, re.DOTALL)
    if label_match:
        result["label"] = label_match.group(1).strip()

    score_match = re.search(r'"score"\s*:\s*(-?\d+(?:\.\d+)?)', text)
    if score_match:
        score_value = float(score_match.group(1))
        result["score"] = int(score_value) if score_value.is_integer() else score_value

    confidence_match = re.search(r'"confidence"\s*:\s*(-?\d+(?:\.\d+)?)', text)
    if confidence_match:
        result["confidence"] = float(confidence_match.group(1))

    reason_match = re.search(
        r'"reason"\s*:\s*"((?:\\.|[^"\\])*)"',
        text,
        re.DOTALL,
    )
    if reason_match:
        reason = bytes(reason_match.group(1), "utf-8").decode("unicode_escape")
        result["reason"] = reason.strip()
    else:
        reason_start = re.search(r'"reason"\s*:\s*"', text, re.DOTALL)
        if reason_start:
            reason = text[reason_start.end():]
            reason = re.sub(r"\s*```$", "", reason).strip()
            reason = reason.rstrip('",} \n\r\t')
            result["reason"] = reason.strip()

    required = {"label", "score", "confidence", "reason"}
    if required.issubset(result):
        return result
    return None


def parse_llm_response(response_text: str) -> Dict:
    """Extract and parse JSON from LLM response with best-effort repair."""
    if not response_text:
        raise ValueError("Empty response from LLM")
    # First, try strict extraction
    json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group(0))
        except json.JSONDecodeError:
            pass
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        repaired = _escape_control_chars_in_strings(_repair_json(response_text))
        try:
            return json.loads(repaired)
        except json.JSONDecodeError:
            partial = _extract_partial_json_fields(response_text)
            if partial is not None:
                return partial
            raise


def _retry_prompt_for_json_repair(prompt: str) -> str:
    return (
        f"{prompt}\n\n"
        "Return exactly one valid JSON object only. "
        "Do not use markdown fences. "
        "Escape all newlines inside JSON strings."
    )


def call_llm(
    provider: LLMProvider,
    provider_name: str,
    item: Dict,
    temperature: float,
    system: str = SYSTEM_PROMPT,
    prompt_override: Optional[str] = None,
) -> Dict:
    """Call LLM for semantic evaluation. Returns parsed JSON dict."""
    prompt = prompt_override if prompt_override is not None else build_user_prompt(item)
    last_error: Optional[Exception] = None
    last_response_text = ""

    prompts_to_try = [prompt, _retry_prompt_for_json_repair(prompt)]
    for attempt, prompt_text in enumerate(prompts_to_try, start=1):
        messages = build_messages(provider_name, prompt_text, system=system)
        response_text = provider.chat(
            messages,
            temperature=temperature,
            max_tokens=2000,
        )
        last_response_text = response_text

        # Gọi hỏng ở tầng mạng thì không có gì để sửa: nhắc lại prompt cũng vô
        # ích, mà còn che mất nguyên nhân thật dưới nhãn "Invalid JSON".
        if not response_text and provider.last_error:
            raise ValueError(f"LLM call failed: {provider.last_error}")

        try:
            return parse_llm_response(response_text)
        except (json.JSONDecodeError, ValueError) as e:
            last_error = e
            if attempt == len(prompts_to_try):
                break

    raise ValueError(f"Invalid JSON response: {last_error}\nRaw: {last_response_text[:300]}")


def extract_claims(
    provider: LLMProvider,
    provider_name: str,
    item: Dict,
    temperature: float,
) -> List[str]:
    """
    Claim Extractor: identify specific factual claims in the Answer
    that go BEYOND what the Chunk already provides.
    Returns a list of claim strings, or [] on failure.
    """
    prompt = build_user_prompt_claim_extractor(item)
    messages = build_messages(provider_name, prompt, system=SYSTEM_PROMPT_CLAIM_EXTRACTOR)

    response_text = provider.chat(
        messages,
        temperature=temperature,
        max_tokens=1000,
    )

    try:
        result = parse_llm_response(response_text)
        claims = result.get("extra_claims", [])
        # Ensure it's a list of strings
        return [str(c) for c in claims if c]
    except Exception:
        # If extraction fails, return empty list — Pass 2 will still run but without claim list
        return []


# ─────────────────────────────────────────────
# SCORE MAPPING
# ─────────────────────────────────────────────

def map_score_to_evaluate(score: int) -> str:
    """Map numeric score to evaluation category."""
    if score >= 6:
        return "correct"
    elif score == 5:
        return "unclear"
    else:
        return "incorrect"


# ─────────────────────────────────────────────
# PROCESS ITEM (3-step: Pass1 → Claim Extract → Pass2)
# ─────────────────────────────────────────────

def process_item(
    provider: LLMProvider,
    provider_name: str,
    config: EvaluatorConfig,
    item: Dict,
    idx: int,
) -> None:
    """
    Evaluate a single QA item.

    Step 1 — Pass 1   : evaluate Answer vs retrieved Chunk → score
    Step 2 — Extract  : if score <= threshold or Pass 1 flagged unverified details,
                        extract the claims in the Answer that go beyond the Chunk
    Step 3 — Pass 2   : verify each claim against the full KB source files, including
                        every sibling version of them → final score

    Only an explicit CONTRADICTED verdict from Pass 1 skips the recheck.
    """
    try:
        # ── STEP 1: PASS 1 ──────────────────────
        nli = call_llm(provider, provider_name, item, config.temperature)
        score = nli.get("score", 0)
        label = nli.get("label", "UNKNOWN")
        confidence = nli.get("confidence", 0)

        needs_source_check = bool(nli.get("needs_source_check"))

        item["pass1_score"] = score
        item["pass1_reason"] = nli.get("reason", "")
        item["pass1_needs_source_check"] = needs_source_check
        item["rechecked"] = False

        print(f"[{idx}] Pass1 → {label} (score: {score}, conf: {confidence:.2f})", end="")

        # ── STEP 2 + 3: CLAIM EXTRACT → PASS 2 ─
        # Recheck when the score is at or below the threshold, OR when Pass 1 saw
        # details it could not verify from the chunk.
        #
        # A low score is NOT a reason to skip: Pass 1 only sees one retrieved chunk,
        # so an answer quoting another version of the same document looks fabricated
        # to it. Those are exactly the items that must be checked against the files.
        # Only an explicit CONTRADICTED verdict skips Pass 2.
        should_recheck = (
            (score <= config.recheck_threshold or needs_source_check)
            and label != "CONTRADICTED"
            and bool(config.kb_dir)
            and not config.disable_pass2
        )

        if not should_recheck:
            if label == "CONTRADICTED" and config.kb_dir:
                print(f"  →  pass2 skipped (contradicted, score={score})")
            print()
        else:
            # "source" is the current field (a list of retrieved files); "file" is legacy.
            file_name = item.get("file") or item.get("source") or ""
            if not file_name:
                print(f"  →  skipped (no source/file field)")
                print()
            else:
                file_content = read_kb_file(file_name, config.kb_dir)
                if not file_content:
                    print(f"  →  skipped (file not found: {file_name})")
                    print()
                else:
                    # Step 2: extract extra claims
                    extra_claims = extract_claims(provider, provider_name, item, config.temperature)
                    print(f"  →  {len(extra_claims)} extra claim(s)", end="")

                    # Step 3: Pass 2 — verify claims against full file
                    original_chunk = item.get("chunk", "")
                    pass2_prompt = build_user_prompt_pass2(
                        item, file_content, original_chunk, extra_claims
                    )
                    nli2 = call_llm(
                        provider,
                        provider_name,
                        item,
                        config.temperature,
                        system=SYSTEM_PROMPT_PASS2,
                        prompt_override=pass2_prompt,
                    )
                    score2 = nli2.get("score", 0)
                    label2 = nli2.get("label", "UNKNOWN")
                    conf2 = nli2.get("confidence", 0)

                    # Pass 2 can only raise the score, never lower it.
                    pass1_score = item["pass1_score"]
                    score2 = max(score2, pass1_score)
                    nli2["score"] = score2

                    print(f"  →  Pass2 → {label2} (score: {score2}, conf: {conf2:.2f})")

                    # Use Pass 2 result (has richer context)
                    nli = nli2
                    score = score2
                    item["rechecked"] = True
                    item["extra_claims"] = extra_claims
                    item["pass2_score"] = score2
                    item["pass2_reason"] = nli2.get("reason", "")
                    item["pass2_verified_claims"] = nli2.get("verified_claims", [])
                    item["version_conflict"] = bool(nli2.get("version_conflict"))

        # ── FINAL RESULT ────────────────────────
        # The scoring rationale goes to "reason", never to "check": "check" is an
        # INPUT field holding the expected answer in join mode, and overwriting it
        # destroyed the expected answer on every scored file.
        item["evaluate"] = map_score_to_evaluate(score)
        item["score"] = score
        item["reason"] = nli.get("reason", "")

    except Exception as e:
        item["evaluate"] = "error"
        item["score"] = 0
        item["reason"] = str(e)
        item["rechecked"] = False
        print(f"\n[{idx}] ERROR → {e}")


# ─────────────────────────────────────────────
# EVALUATION LOOP
# ─────────────────────────────────────────────

def build_joined_items(config: EvaluatorConfig) -> List[Dict]:
    """Join a QA output file with a compliance file (e.g. PCI-DSS) by id."""
    qa_path = Path(config.qa_file)
    pci_path = Path(config.pci_file)
    if not qa_path.exists():
        raise FileNotFoundError(f"QA file not found: {qa_path}")
    if not pci_path.exists():
        raise FileNotFoundError(f"Compliance file not found: {pci_path}")

    qa_data = json.loads(qa_path.read_text(encoding="utf-8"))
    pci_data = json.loads(pci_path.read_text(encoding="utf-8"))

    pci_by_id = {}
    for row in pci_data:
        pid = str(row.get(config.id_field, "")).strip()
        if pid:
            pci_by_id[pid] = row

    joined: List[Dict] = []
    missing = 0
    for row in qa_data:
        qid = str(row.get(config.id_field, "")).strip()
        pci_row = pci_by_id.get(qid) if qid else None
        if not pci_row:
            missing += 1
            continue

        joined.append({
            "id": qid,
            "question": row.get("question", ""),
            "answer": row.get("answer", ""),
            "context": pci_row.get(config.context_field, ""),
            "main_content": pci_row.get(config.main_field, ""),
            "check": pci_row.get(config.expected_field, ""),
            "source": row.get("source", []),
        })

    if missing > 0:
        print(f"⚠ join mode: skipped {missing} item(s) with no matching id")

    return joined


def run_evaluation(config: EvaluatorConfig, provider: LLMProvider, provider_name: str) -> None:
    """Main evaluation loop."""
    if config.join_mode:
        input_path = Path(config.qa_file)
        data = build_joined_items(config)
    else:
        input_path = Path(config.input_path)
        data = json.loads(input_path.read_text(encoding="utf-8"))

    output_path = input_path.with_name(f"{input_path.stem}_semantic_scored.json")
    total = len(data)

    print(f"Loaded   : {input_path.name}")
    print(f"Total    : {total}")
    print(f"Provider : {provider_name.upper()}")
    if config.base_url:
        print(f"URL      : {config.base_url}")
    if config.model:
        print(f"Model    : {config.model}")
    if config.kb_dir:
        if config.disable_pass2:
            print(f"KB dir   : {config.kb_dir}  (pass2 disabled)")
        else:
            print(f"KB dir   : {config.kb_dir}  (2-pass enabled for score ≤ {config.recheck_threshold})")
    else:
        print(f"KB dir   : not set  (1-pass only)")
    print()

    for idx, item in enumerate(data, start=1):
        process_item(provider, provider_name, config, item, idx)
        if idx < total:
            time.sleep(config.sleep_time)

    output_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"\n{'='*80}")
    print_statistics(data)
    print_error_classification_table(data)
    print(f"\n✅ Saved to: {output_path}")


# ─────────────────────────────────────────────
# STATISTICS
# ─────────────────────────────────────────────

def print_statistics(data: List[Dict]) -> None:
    """Print evaluation statistics."""
    evaluate_counts = {"correct": 0, "incorrect": 0, "unclear": 0, "error": 0}
    score_sum = 0
    score_count = 0
    score_dist = {i: 0 for i in range(1, 11)}

    rechecked_total = 0
    rechecked_improved = 0

    for item in data:
        evaluate = item.get("evaluate", "error")
        evaluate_counts[evaluate] = evaluate_counts.get(evaluate, 0) + 1

        score = item.get("score", 0)
        if score > 0:
            score_sum += score
            score_count += 1
            if 1 <= score <= 10:
                score_dist[score] += 1

        if item.get("rechecked"):
            rechecked_total += 1
            p1 = item.get("pass1_score", 0)
            p2 = item.get("pass2_score", 0)
            if p2 > p1:
                rechecked_improved += 1

    total = len(data)
    avg_score = score_sum / score_count if score_count > 0 else 0

    print("Evaluation Summary:")
    print(f"   Total      : {total}")
    print(f"   Correct    : {evaluate_counts['correct']:3d} ({evaluate_counts['correct']/total*100:5.1f}%) [score ≥ 6]")
    print(f"   Unclear    : {evaluate_counts['unclear']:3d} ({evaluate_counts['unclear']/total*100:5.1f}%) [score = 5]")
    print(f"   Incorrect  : {evaluate_counts['incorrect']:3d} ({evaluate_counts['incorrect']/total*100:5.1f}%) [score ≤ 4]")
    print(f"   Error      : {evaluate_counts['error']:3d} ({evaluate_counts['error']/total*100:5.1f}%)")
    print(f"   Avg Score  : {avg_score:.2f}/10")

    if rechecked_total > 0:
        print(f"\n2-Pass Stats:")
        print(f"   Rechecked        : {rechecked_total}")
        print(f"   Improved         : {rechecked_improved} ({rechecked_improved/rechecked_total*100:.1f}% of rechecked)")

        # Claim verification breakdown across all rechecked items
        total_claims = 0
        supported = 0
        not_found = 0
        contradicted = 0
        for item in data:
            for vc in item.get("pass2_verified_claims", []):
                total_claims += 1
                status = vc.get("status", "")
                if status == "SUPPORTED":
                    supported += 1
                elif status == "CONTRADICTED":
                    contradicted += 1
                else:
                    not_found += 1

        if total_claims > 0:
            print(f"\n   Claim Verification ({total_claims} total extra claims):")
            print(f"   ✅ Supported    : {supported} ({supported/total_claims*100:.1f}%)")
            print(f"   ❓ Not found    : {not_found} ({not_found/total_claims*100:.1f}%)")
            print(f"   ❌ Contradicted : {contradicted} ({contradicted/total_claims*100:.1f}%)")

    print("\nScore Distribution:")
    for score in range(10, 0, -1):
        count = score_dist[score]
        if count > 0:
            bar = "█" * int(count / total * 50)
            print(f"   {score:2d}: {count:3d} {bar}")


ERROR_CATEGORIES = [
    "Information Inaccuracy",
    "Source Retrieval Error",
    "Missing Information",
]


def classify_error_category(item: Dict) -> str:
    """
    Rule-based classification for incorrect answers.

    Categories:
    - Source Retrieval Error: answer refuses or claims missing KB/context
    - Missing Information: answer is incomplete, vague, or fails to provide required points
    - Information Inaccuracy: answer is wrong, contradictory, or off-topic
    """
    # pass*_check / check are the pre-rename field names, kept so files scored
    # by an older version still classify.
    text_parts = [
        str(item.get("reason") or item.get("check", "")),
        str(item.get("pass1_reason") or item.get("pass1_check", "")),
        str(item.get("pass2_reason") or item.get("pass2_check", "")),
        str(item.get("answer", "")),
    ]
    text = " ".join(part.lower() for part in text_parts if part)

    source_retrieval_patterns = [
        r"từ chối trả lời",
        r"không có thông tin",
        r"không đủ thông tin",
        r"kiến thức cơ sở không đủ",
        r"knowledge base",
        r"\bkb\b",
        r"không tìm thấy",
        r"không được cung cấp trong .* (?:file|nguồn|tài liệu|context|ngữ cảnh)",
        r"thiếu ngữ cảnh",
        r"không có trong tài liệu",
    ]
    if any(re.search(pattern, text) for pattern in source_retrieval_patterns):
        return "Source Retrieval Error"

    missing_information_patterns = [
        r"thiếu",
        r"không đầy đủ",
        r"chưa đầy đủ",
        r"vague",
        r"mơ hồ",
        r"generic",
        r"không đủ chi tiết",
        r"missing important",
        r"missing key",
        r"thiếu ý",
        r"thiếu thành phần",
        r"thiếu yếu tố",
    ]
    if any(re.search(pattern, text) for pattern in missing_information_patterns):
        return "Missing Information"

    information_inaccuracy_patterns = [
        r"mâu thuẫn",
        r"trái với",
        r"sai lệch",
        r"sai lầm",
        r"không chính xác",
        r"hoàn toàn sai",
        r"sai về ý nghĩa",
        r"contradict",
        r"incorrect",
        r"off-topic",
        r"không liên quan",
        r"không đúng",
        r"vi phạm yêu cầu",
    ]
    if any(re.search(pattern, text) for pattern in information_inaccuracy_patterns):
        return "Information Inaccuracy"

    return "Information Inaccuracy"


def print_error_classification_table(data: List[Dict]) -> None:
    """Print error classification summary for incorrect items."""
    total = len(data)
    incorrect_items = [item for item in data if item.get("evaluate") == "incorrect"]
    incorrect_total = len(incorrect_items)

    if incorrect_total == 0:
        return

    counts = {category: 0 for category in ERROR_CATEGORIES}
    for item in incorrect_items:
        category = classify_error_category(item)
        counts[category] = counts.get(category, 0) + 1

    name_width = 25
    count_width = 5
    incorrect_pct_width = 15
    total_pct_width = 10

    print(f"\n{'='*80}")
    print("📊 THỐNG KÊ PHÂN LOẠI LỖI (ERROR CLASSIFICATION)")
    print(f"{'='*80}")
    print(
        f"{'Error Category':<{name_width}} | "
        f"{'Count':>{count_width}} | "
        f"{'% of Incorrect':>{incorrect_pct_width}} | "
        f"{'% of Total':>{total_pct_width}}"
    )
    print(f"{'-'*80}")

    for category in ERROR_CATEGORIES:
        count = counts.get(category, 0)
        incorrect_pct = (count / incorrect_total * 100) if incorrect_total else 0
        total_pct = (count / total * 100) if total else 0
        print(
            f"{category:<{name_width}} | "
            f"{count:>{count_width}d} | "
            f"{incorrect_pct:>{incorrect_pct_width}.1f}% | "
            f"{total_pct:>{total_pct_width}.1f}%"
        )

    print(f"{'='*80}")


# ─────────────────────────────────────────────
# ENV / ARG PARSING
# ─────────────────────────────────────────────

def build_arg_parser() -> argparse.ArgumentParser:
    provider_choices = sorted(PROVIDER_CONFIGS.keys()) + ["ollama"]

    parser = argparse.ArgumentParser(
        description="RAG Evaluation Scorer - Semantic evaluation with 1-10 scale (2-pass support)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # 1-pass (original behaviour)
  python evaluate.py --input qa_data.json --api-key YOUR_KEY

  # 2-pass with KB directory
  python evaluate.py --input qa_data.json --api-key YOUR_KEY --kb-dir ./kb_files/

  # 2-pass with custom threshold (default: 6)
  python evaluate.py --input qa_data.json --api-key YOUR_KEY --kb-dir ./kb_files/ --recheck-threshold 7

  # With Anthropic Claude
  python evaluate.py --input qa_data.json --provider anthropic --api-key YOUR_KEY --kb-dir ./kb_files/

  # With Ollama (local)
  python evaluate.py --input qa_data.json --provider ollama --ollama-model qwen2.5:7b --kb-dir ./kb_files/

Scoring:
  Score ≥ 6: PASS (answer can be used)
  Score = 5: BORDERLINE (unclear, don't use)
  Score ≤ 4: FAIL (answer is wrong or problematic)

2-Pass Logic (3 steps when --kb-dir is set):
  Step 1 — Pass 1  : evaluate Answer vs retrieved Chunk → score
  Step 2 — Extract : if score <= threshold or Pass 1 flagged unverified details,
                     extract the claims that go beyond the Chunk
  Step 3 — Pass 2  : verify each claim against the full KB source files — including
                     every sibling VERSION of them → final score

  label CONTRADICTED     → skip pass 2, the answer really does conflict
  score ≤ threshold      → run claim extract + pass 2
  needs_source_check     → run claim extract + pass 2, whatever the score
  otherwise              → skip pass 2, already reliable

  Claim verification outcome:
    SUPPORTED    → score raised toward 9-10 (any version of the document counts)
    NOT_FOUND    → floor at 7 (absence of evidence ≠ wrong)
    CONTRADICTED → score capped low (value found in no file at all)
        """,
    )
    parser.add_argument("--input", help="Input JSON file with QA pairs (omit when using --qa-file/--pci-file)")
    parser.add_argument(
        "--provider",
        choices=provider_choices,
        default=DEFAULT_PROVIDER,
        help=f"LLM provider (default: {DEFAULT_PROVIDER})",
    )
    parser.add_argument("--model", help="Model name to use (overrides default for provider)")
    parser.add_argument("--api-key", help="LLM API key (or set {PROVIDER}_API_KEY env var)")
    parser.add_argument("--base-url", help="Custom base URL for OpenAI-compatible APIs")
    parser.add_argument("--ollama-model", default="qwen2.5:7b", help="Ollama model name (default: qwen2.5:7b)")
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
    # NEW args
    parser.add_argument(
        "--kb-dir",
        default=None,
        help="Directory containing KB source .md files (enables 2-pass evaluation)",
    )
    parser.add_argument(
        "--recheck-threshold",
        type=int,
        default=RECHECK_THRESHOLD,
        help=f"Run Pass 2 if Pass 1 score <= threshold (default: {RECHECK_THRESHOLD}). Also runs whenever Pass 1 flags unverified details; skipped only on a CONTRADICTED verdict.",
    )
    parser.add_argument(
        "--no-pass2",
        action="store_true",
        help="Disable Pass 2 even if --kb-dir is provided (force 1-pass only).",
    )

    join = parser.add_argument_group(
        "join mode",
        "Merge a QA output file with a compliance file by id, instead of --input.",
    )
    join.add_argument("--qa-file", help="QA output JSON (questions + AI answers)")
    join.add_argument("--pci-file", help="Compliance JSON providing context and expected answers")
    join.add_argument("--id-field", default="id", help="Field used to match rows (default: id)")
    join.add_argument(
        "--context-field",
        default="pci_dss_requirements",
        help="Compliance field holding the requirement context (default: pci_dss_requirements)",
    )
    join.add_argument(
        "--main-field",
        default="testing_procedures",
        help="Compliance field holding the source excerpt (default: testing_procedures)",
    )
    join.add_argument(
        "--expected-field",
        default="customer_only",
        help="Compliance field holding the expected answer (default: customer_only)",
    )
    return parser


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()

    load_env_file()
    env_ollama_url = os.getenv("OLLAMA_URL")
    env_ollama_model = os.getenv("OLLAMA_MODEL")

    provider_name = normalize_provider_name(args.provider)

    if bool(args.qa_file) != bool(args.pci_file):
        print("❌ Join mode needs both --qa-file and --pci-file.")
        return
    if not args.input and not args.qa_file:
        print("❌ Provide --input, or --qa-file together with --pci-file.")
        return

    config = EvaluatorConfig(
        input_path=args.input or "",
        output_path="",
        provider=provider_name,
        temperature=args.temperature,
        sleep_time=args.sleep,
        ollama_model=env_ollama_model or args.ollama_model,
        ollama_url=env_ollama_url or args.ollama_url,
        # CLI thắng env, env thắng mặc định của provider.
        base_url=args.base_url or resolve_env_override(provider_name, "BASE_URL"),
        model=args.model or resolve_env_override(provider_name, "MODEL"),
        kb_dir=args.kb_dir,
        recheck_threshold=args.recheck_threshold,
        disable_pass2=args.no_pass2,
        qa_file=args.qa_file,
        pci_file=args.pci_file,
        context_field=args.context_field,
        expected_field=args.expected_field,
        main_field=args.main_field,
        id_field=args.id_field,
    )

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
