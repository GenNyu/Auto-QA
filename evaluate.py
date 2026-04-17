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
from providers.base import LLMProvider
from providers.factory import create_provider, normalize_provider_name

# Constants
DEFAULT_TEMPERATURE = 0.0
DEFAULT_SLEEP = 0.3
ENV_FILE = ".env"
RECHECK_THRESHOLD = 7  # Re-evaluate with full file if score is in range [5, threshold]

# ─────────────────────────────────────────────
# SYSTEM PROMPTS
# ─────────────────────────────────────────────

SYSTEM_PROMPT = """
You are a Professional Quality Assurance Evaluator for Corporate Compliance AI Systems.

### GOAL:
Evaluate whether the AI Answer matches the Expected Answer (ground truth) in meaning, based on PCI DSS compliance intent.

---

### INPUTS:
- Question
- Requirement Context
- Main Content
- Expected Answer
- AI Answer

---

### CORE PRINCIPLE (VERY IMPORTANT):

- The Expected Answer is a **reference**, NOT the only valid expression.
- The AI Answer must be evaluated based on:
  - correctness of compliance meaning
  - audit usefulness
  - alignment with security intent

- If the AI Answer is correct in meaning, it MUST receive a high score (≥ 8),
  even if wording, terminology, or structure differs.

---

### EVALUATION PHILOSOPHY:

Focus on:
1. Correct control (what is enforced)
2. Correct scope (where it applies)
3. Correct intent (why it exists)

Do NOT over-penalize:
- verbosity
- paraphrasing
- additional correct context

---

### WHAT COUNTS AS A STRONG MATCH:

An AI Answer is strong if:
- It captures the same compliance meaning
- It reflects real audit reasoning
- It would be acceptable in an audit explanation

---

### SCORING RUBRIC (CALIBRATED):

#### ENTAILED (High confidence match)
- 10:
  - Correct conclusion + correct reasoning + correct scope
  - Clear, sufficiently deep, and audit-ready
  - Can be used directly in a real audit explanation
  - No incorrect or misleading information

- 9:
  - Fully correct in meaning, scope, and intent
  - Slightly less depth (e.g., missing explicit risk/example/implication)
  - Still fully acceptable for audit

- 8:
  - Correct core compliance meaning (correct conclusion and scope)
  - Somewhat generic OR reasoning not clearly articulated
  - Lacks clear audit-level explanation

---

#### PARTIAL
- 7:
  - Correct core direction
  - Missing important elements such as:
    - reasoning
    - risk
    - handling approach
  - Not sufficient for audit, but shows correct understanding

- 6:
  - Correct direction but missing key component (control / scope / intent)

- 5:
  - Vague or insufficient for audit use

---

#### NOT_MATCH
- 4: Only partially related, misses main compliance idea
- 3: Misinterprets core intent

---

#### CONTRADICTED
- 2: Contains contradiction with compliance meaning
- 1: Completely incorrect / irrelevant / empty

---

### CORE MATCH GUIDELINE (CRITICAL):

- If the AI Answer:
  - has the correct conclusion
  - has the correct scope
  - contains no incorrect or misleading information

→ Minimum score MUST be 8

- To achieve score = 9:
  - must include clear reasoning (why / impact / logic)

- To achieve score = 10:
  - must include:
    - clear reasoning
    - sufficient depth
    - audit-ready explanation

IMPORTANT:
- Do NOT automatically assign 10 just because the answer is correct
- Score 10 is reserved for answers that are strong enough for real audit usage

---

### 10 SCORE CLARIFICATION (VERY IMPORTANT):

Score 10 MUST be assigned when:
- The AI Answer is fully correct in meaning, scope, and intent
- The reasoning is clearly expressed or strongly implied
- The answer is usable in an audit context without correction

The AI Answer does NOT need to:
- Use the same wording or terminology as the Expected Answer
- Explicitly mention all examples (e.g., "forensics")
- Match structure or phrasing

If the reasoning already implies the same concept,
it MUST be considered complete.

---

### WORDING vs MEANING RULE (CRITICAL):

Do NOT penalize the AI Answer for:
- Not using specific keywords (e.g., "forensics")
- Not explicitly naming concepts if they are clearly implied

Focus on meaning, NOT wording.

Examples:
- "investigation", "incident analysis", "determine impact"
  ≈ "forensics"

→ MUST be treated as equivalent

---

### EXPECTED ANSWER INTERPRETATION:

- The Expected Answer may include:
  - examples
  - scenarios
  - elaborations

→ These are NOT mandatory.

Missing examples MUST NOT reduce score if:
- the core compliance reasoning is correct

---

### EXTRA INFORMATION RULE:

Do NOT penalize if extra content is:
- correct
- aligned with PCI DSS
- helpful

Penalize ONLY if extra content:
- is incorrect
- is misleading
- introduces unsupported claims

---

### VERBOSITY RULE:

Do NOT penalize longer answers if:
- content is correct
- content remains relevant

Penalize ONLY if:
- the answer drifts away from the compliance point
- introduces confusion

---

### NEVER FORGIVE:

- Wrong compliance meaning
- Wrong scope
- Contradictions

---

### SPECIAL CASE:

- If the AI Answer is empty → score = 1

---

### EVALUATION ORDER:

1. Read Requirement Context + Main Content → identify audit intent
2. Read Expected Answer → extract semantic ground truth
3. Compare AI Answer based on:
   - intent
   - scope
   - reasoning
4. Ignore wording differences
5. Prioritize correctness over wording completeness

---

### OUTPUT FORMAT (JSON ONLY):

{
  "label": "ENTAILED | PARTIAL | NOT_MATCH | CONTRADICTED",
  "score": number (1-10),
  "confidence": number (0-1),
  "reason": "Brief explanation in Vietnamese describing alignment, missing elements, or issues."
}
"""

SYSTEM_PROMPT_CLAIM_EXTRACTOR = """
You are a precise fact extraction assistant for compliance evaluation.

### GOAL:
Given a Question, Expected Answer, and AI Answer, extract ONLY the specific claims in the AI Answer
that go BEYOND what the Expected Answer already provides.

### RULES:
1. A "claim" is any specific factual statement: a number, a name, a date, a status, a field value, a scope item, a step, a rule, a URL, or a role.
2. SKIP claims that are:
   - Already stated in the Expected Answer (even if rephrased slightly)
   - Clearly inherited from the Question
   - Generic professional language ("đảm bảo tuân thủ", "theo quy trình", "giúp minh bạch")
   - File name citations or metadata
3. INCLUDE claims that are:
   - Specific field values, system names, dates, numbers, approvals, scopes, records, or steps that are NOT in the Expected Answer
   - Strongly specific operational details not present in the Expected Answer
4. If the AI Answer only paraphrases the Expected Answer more generically, return no extra claims.

### OUTPUT FORMAT (JSON ONLY):
{
  "extra_claims": [
    "claim 1",
    "claim 2"
  ],
  "claim_count": number
}

If there are no extra claims, return: {"extra_claims": [], "claim_count": 0}
"""

SYSTEM_PROMPT_PASS2 = """
You are a Professional Quality Assurance Evaluator for Corporate Compliance AI Systems.

### GOAL:
Re-evaluate a borderline AI Answer using the FULL SOURCE FILE.
Your final judgment must consider BOTH:
1. Whether the AI Answer is supported by the Full Source File, and
2. Whether the AI Answer still matches the Expected Answer in meaning.

### CONTEXT:
- Pass 1 compared AI Answer vs Expected Answer and gave a borderline score (5-7).
- A Claim Extractor identified extra claims in the AI Answer that were not explicit in the Expected Answer.
- Your job is to verify those extra claims against the Full Source File.
- Pass 2 is primarily intended to RAISE confidence for borderline answers that may be correct but more detailed.
- Your score will only be used if it is HIGHER than Pass 1.

### VERIFICATION PROCESS:
For each extra claim:
  ✅ SUPPORTED     — found verbatim or clearly implied in the full file
  ❌ CONTRADICTED  — the file says something explicitly different
  ❓ NOT_FOUND     — cannot be found in the file

### HOW TO SCORE:
1. First, judge whether the AI Answer matches the Expected Answer semantically.
   - If it clearly contradicts or misses the core meaning of the Expected Answer, do NOT raise the score.
2. Then verify the extra claims against the Full Source File.
3. Use this guidance:
   - Strong semantic match + all/most extra claims SUPPORTED → 8-10
   - Strong semantic match + extra claims mostly NOT_FOUND but harmless/non-specific → 7-8
   - Strong semantic match + extra claims include unsupported specific details → at most 7
   - Any CONTRADICTED extra claim → at most 6
   - Semantic mismatch with Expected Answer → keep score low, even if some file evidence exists

### IMPORTANT RULES:
1. NOT_FOUND is not the same as wrong. It only limits how much confidence you can gain.
2. CONTRADICTED is wrong.
3. Do NOT reward extra facts if they drift away from the Expected Answer's core meaning.
4. Ignore company names / proprietary names if the answer preserves the same compliance meaning.
5. If extra_claims is empty, you may still use the Full Source File to determine whether the AI Answer is a faithful, acceptable paraphrase of the Expected Answer.

### OUTPUT FORMAT (JSON ONLY):
{
  "label": "ENTAILED | PARTIAL | NOT_MATCH | CONTRADICTED",
  "score": number (1-10),
  "confidence": number (0-1),
  "reason": "Giải thích ngắn gọn bằng tiếng Việt. Nêu rõ AI Answer có khớp Expected Answer không và các extra claim có được file hỗ trợ hay không.",
  "verified_claims": [
    {"claim": "...", "status": "SUPPORTED | NOT_FOUND | CONTRADICTED", "note": "lý do ngắn gọn"}
  ]
}
"""


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


# ─────────────────────────────────────────────
# KB FILE LOOKUP
# ─────────────────────────────────────────────

def find_kb_file(file_name: str, kb_dir: str) -> Optional[Path]:
    """
    Locate a KB file on disk.

    The 'file' field in JSON is like: 20260206_PRT_DanhSach_Danh_sach_MC_final_10.md
    The actual file on disk may have a random hash suffix added:
        20260206_PRT_DanhSach_Danh_sach_MC_final_10__76vsy07.md

    Strategy:
    1. Exact match first.
    2. Strip .md, use as prefix, find first file that starts with it.
    """
    kb_path = Path(kb_dir)
    if not kb_path.is_dir():
        return None

    # 1. Exact match
    exact = kb_path / file_name
    if exact.exists():
        return exact

    # 2. Prefix match (handle hash suffix)
    stem = Path(file_name).stem  # filename without .md
    for candidate in kb_path.glob("*.md"):
        # candidate stem starts with our stem (ignoring trailing hash)
        if candidate.stem.startswith(stem) or stem.startswith(candidate.stem):
            return candidate

    # 3. Loose match: check if stem is a substring of candidate stem
    for candidate in kb_path.glob("*.md"):
        if stem in candidate.stem or candidate.stem in stem:
            return candidate

    return None


def read_kb_file(file_name: str, kb_dir: str, max_chars: int = 100_000) -> Optional[str]:
    """
    Read full content of one or more KB source files. Truncates at max_chars to stay within LLM limits.

    - If file_name is a list, concatenate all found files (in order).
    - Each file is separated with a clear header to help the LLM attribute claims.
    - Enforce a global max_chars budget across all files.
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

    parts: List[str] = []
    total_len = 0
    for f in files:
        path = find_kb_file(f, kb_dir)
        if path is None:
            continue
        content = path.read_text(encoding="utf-8")
        header = f"\n\n===== FILE: {path.name} =====\n"
        remaining = max_chars - total_len
        if remaining <= 0:
            break
        chunk = header + content
        if len(chunk) > remaining:
            chunk = chunk[:remaining] + f"\n\n[... FILE TRUNCATED AT {max_chars} CHARS TOTAL ...]"
        parts.append(chunk)
        total_len += len(chunk)

    if not parts:
        return None
    return "".join(parts)


# ─────────────────────────────────────────────
# PROMPT BUILDERS
# ─────────────────────────────────────────────

def get_expected_answer(item: Dict) -> str:
    """Get expected answer from item (gold/check/expected)."""
    return str(item.get("gold") or item.get("check") or item.get("expected") or "").strip()


def get_ai_answer(item: Dict) -> str:
    """Get AI answer from item."""
    return str(item.get("answer") or "").strip()


def build_user_prompt(item: Dict) -> str:
    """Build Pass 1 evaluation prompt from QA item (gold vs AI answer)."""
    return f"""
Question:
{item.get("question", "")}

Expected Answer:
{get_expected_answer(item)}

AI Answer:
{get_ai_answer(item)}
""".strip()


def build_user_prompt_claim_extractor(item: Dict) -> str:
    """Build prompt for Claim Extractor — identifies extra claims beyond the expected answer."""
    return f"""
Question:
{item.get("question", "")}

Expected Answer:
{get_expected_answer(item)}

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
    return f"""
Question:
{item.get("question", "")}

Expected Answer:
{get_expected_answer(item)}

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
    Step 2 — Extract  : if 5 <= score <= threshold, extract extra claims from Answer beyond Chunk
    Step 3 — Pass 2   : verify each extra claim against the full KB source file → final score

    Items with score ≤ 4 (incorrect) are NOT rechecked — their errors are real, not caused
    by a truncated chunk.
    """
    try:
        # ── STEP 1: PASS 1 ──────────────────────
        nli = call_llm(provider, provider_name, item, config.temperature)
        score = nli.get("score", 0)
        label = nli.get("label", "UNKNOWN")
        confidence = nli.get("confidence", 0)

        item["pass1_score"] = score
        item["pass1_check"] = nli.get("reason", "")
        item["rechecked"] = False

        print(f"[{idx}] Pass1 → {label} (score: {score}, conf: {confidence:.2f})", end="")

        # ── STEP 2 + 3: CLAIM EXTRACT → PASS 2 ─
        # Only recheck if score is in the "borderline" range (5-threshold).
        # score ≤ 4 → genuinely incorrect answer, skip pass 2.
        # score > threshold → already good enough, skip pass 2.
        should_recheck = (
            (5 <= score <= config.recheck_threshold)
            and bool(config.kb_dir)
            and not config.disable_pass2
        )

        if not should_recheck:
            if score <= 4 and config.kb_dir:
                print(f"  →  pass2 skipped (incorrect, score={score})")
            print()
        else:
            # Only use legacy "file" field for KB filename
            file_name = item.get("file", "")
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
                    item["pass2_check"] = nli2.get("reason", "")
                    item["pass2_verified_claims"] = nli2.get("verified_claims", [])

        # ── FINAL RESULT ────────────────────────
        item["evaluate"] = map_score_to_evaluate(score)
        item["score"] = score
        item["check"] = nli.get("reason", "")

    except Exception as e:
        item["evaluate"] = "error"
        item["score"] = 0
        item["check"] = str(e)
        item["rechecked"] = False
        print(f"\n[{idx}] ERROR → {e}")


# ─────────────────────────────────────────────
# EVALUATION LOOP
# ─────────────────────────────────────────────

def run_evaluation(config: EvaluatorConfig, provider: LLMProvider, provider_name: str) -> None:
    """Main evaluation loop."""
    input_path = Path(config.input_path)
    output_path = input_path.with_name(f"{input_path.stem}_semantic_scored.json")

    data = json.loads(input_path.read_text(encoding="utf-8"))
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
    text_parts = [
        str(item.get("check", "")),
        str(item.get("pass1_check", "")),
        str(item.get("pass2_check", "")),
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
    return os.getenv(f"{provider_name.upper()}_API_KEY")


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
  Step 2 — Extract : if 5 <= score <= threshold, extract extra claims beyond the Chunk
  Step 3 — Pass 2  : verify each claim against full KB source file → final score

  score ≤ 4 (incorrect) → skip pass 2, error is real
  score 5-7 (borderline) → run claim extract + pass 2
  score ≥ 8 (good)       → skip pass 2, already reliable

  Claim verification outcome:
    SUPPORTED    → score raised toward 9-10
    NOT_FOUND    → floor at 7 (absence of evidence ≠ wrong)
    CONTRADICTED → score capped at 6 or lower
        """,
    )
    parser.add_argument("--input", required=True, help="Input JSON file with QA pairs")
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
        help=f"Run Pass 2 if Pass 1 score is in range [5, threshold] (default: {RECHECK_THRESHOLD}). Score ≤ 4 always skipped.",
    )
    parser.add_argument(
        "--no-pass2",
        action="store_true",
        help="Disable Pass 2 even if --kb-dir is provided (force 1-pass only).",
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

    config = EvaluatorConfig(
        input_path=args.input,
        output_path="",
        provider=provider_name,
        temperature=args.temperature,
        sleep_time=args.sleep,
        ollama_model=env_ollama_model or args.ollama_model,
        ollama_url=env_ollama_url or args.ollama_url,
        base_url=args.base_url,
        model=args.model,
        kb_dir=args.kb_dir,
        recheck_threshold=args.recheck_threshold,
        disable_pass2=args.no_pass2,
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
