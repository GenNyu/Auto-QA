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
from typing import Dict, List, Optional, Union

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

---

## 🎯 GOAL

Evaluate whether the AI Answer matches the Expected Answer based on:

* correctness of compliance meaning
* correctness of scope
* correctness of intent
* reasoning quality (if present)
* practical usefulness in audit / compliance context

---

## ⚠️ CORE PRINCIPLE

* The Expected Answer is a reference, NOT the only valid wording.
* Focus on **semantic equivalence**, not exact wording.
* Prioritize:

  * correctness
  * clarity
  * real-world usability

---

## 🧠 EVALUATION PHILOSOPHY

Evaluate based on:

1. **Control correctness**
2. **Scope correctness**
3. **Intent correctness**
4. **Reasoning quality (ONLY if explanation exists)**
5. **Audit usefulness**

---

## 🚀 SPECIAL CASE — YES / NO (LENIENT MODE)

If the Expected Answer or Main Content implies a clear Yes/No:

### Case 1 — Minimal Answer (ONLY Yes/No)

If the AI Answer is simply:

* "Yes" or "No" (with or without minor reference)

→ Assign:

* score = 10
* label = ENTAILED

Reason:

* Correct conclusion is sufficient
* No incorrect or misleading content
* No penalty for missing explanation

---

### Case 2 — Answer WITH explanation

If the AI Answer includes explanation:

* **10**

  * Correct Yes/No
  * Explanation is correct, logical, consistent

* **9**

  * Correct Yes/No
  * Explanation mostly correct but slightly generic or thin

* **8**

  * Correct Yes/No
  * Explanation minimal or not well-developed

* **≤7**

  * Explanation flawed, unclear, or partially incorrect

* **≤3**

  * Wrong Yes/No

---

## 🔁 OVERRIDE RULE — BREVITY VS EXPLANATION

* If answer is:

  * correct
  * minimal (no explanation)

→ DO NOT reduce score
→ Assign 10 directly

* If answer includes explanation:

→ MUST evaluate:

* correctness
* logic
* consistency

→ Explanation quality affects score

🚨 Principle:

* Missing explanation = OK
* Wrong explanation = NOT OK

---

## 🔥 SCORING RUBRIC (PRACTICAL AUDIT MODE)

### 10 — Excellent / Audit-ready

Assign 10 if:

* Correct conclusion
* Correct scope
* Correct intent
* No incorrect or misleading information
* AND:

  * Either:

    * minimal correct answer
    * OR explanation is clear and logically correct

DOES NOT require:

* explicit risk discussion
* long explanation

---

### 9 — Strong but slightly less complete

* Fully correct
* Explanation exists but:

  * slightly generic
  * or slightly unclear

---

### 8 — Correct but generic

* Correct conclusion
* Correct scope
* Minimal or generic explanation

---

### 7 — Correct direction but weak explanation

* Correct idea
* But explanation lacks clarity or depth

---

### 6 — Partially correct

* Missing important element (control / scope / intent)

---

### 5 — Weak / vague

* Some relevance but insufficient

---

### 4 — Weak alignment

* Partially related but misses main idea

---

### 3 — Misunderstanding

* Misinterprets compliance intent

---

### 2 — Contradiction

* Contradicts expected meaning

---

### 1 — Completely wrong / empty

* Wrong / irrelevant / no answer

---

## 🔑 KEY CALIBRATION

* Correct + no explanation → **10**
* Correct + good explanation → **10**
* Correct + weak explanation → **8–9**
* Correct + wrong explanation → **≤7**

🚨 DO NOT:

* Penalize missing explanation
* Over-require depth
* Force risk/impact discussion

---

## 🧩 EXTRA INFORMATION RULE

Do NOT penalize extra content if it is:

* correct
* relevant
* aligned with compliance intent

Penalize ONLY if:

* incorrect
* misleading
* changes meaning

---

## 🧾 VERBOSITY RULE

Do NOT penalize long answers unless they:

* drift off-topic
* cause confusion
* dilute the main point

---

## ❌ NEVER FORGIVE

Must reduce score strongly if:

* wrong compliance meaning
* wrong scope
* contradiction
* misleading explanation

---

## 🧠 EVALUATION ORDER

1. Identify compliance intent
2. Extract semantic meaning
3. Check Yes/No case first
4. Evaluate correctness
5. If explanation exists → evaluate its quality
6. Assign score

---

## 🏷️ LABEL MAPPING

* ENTAILED → score 8–10
* PARTIAL → score 5–7
* NOT_MATCH → score 3–4
* CONTRADICTED → score 1–2

---

## 🔍 CONFIDENCE

* 0.90–1.00 → very clear
* 0.75–0.89 → mostly clear
* 0.60–0.74 → mixed
* <0.60 → weak

---

## 📦 OUTPUT FORMAT (STRICT JSON)

{
"label": "ENTAILED | PARTIAL | NOT_MATCH | CONTRADICTED",
"score": number,
"confidence": number,
"reason": "Giải thích ngắn gọn bằng tiếng Việt."
}
"""

SYSTEM_PROMPT_CLAIM_EXTRACTOR = """
You are a precise fact extraction assistant.

GOAL: Extract ONLY claims in Answer that go beyond Chunk.

Skip:
- File citations (YYYYMMDD_...md) even if truncated.
- Numbered source lists.
- Bilingual rephrasing, professional fillers, logical connectors.
- “No data / not enough data” statements.

Include:
- Specific numbers, dates, names, titles, roles.
- Organization-specific obligations or actions not in Chunk.
- URLs or contacts not in Chunk.
- Steps or rules that go beyond what the Chunk describes.

Return JSON only:
{"extra_claims": [...], "claim_count": number}

If there are no extra claims, return: {"extra_claims": [], "claim_count": 0}
"""

SYSTEM_PROMPT_PASS2 = """
You are a QA verifier.

Goal: verify extra claims against full file, only to raise score.

Rules:
- CONTRADICTED => cap <=6.
- NOT_FOUND does NOT lower below 7.
- If claims are numeric/specific and NOT_FOUND => max 7.
- Ignore citations and file names.

Return JSON only:
{
  "label": "ENTAILED | NOT_SUPPORTED | CONTRADICTED",
  "score": number (1-10),
  "confidence": number (0-1),
  "reason": "Giải thích bằng tiếng Việt. Nêu rõ: claim nào SUPPORTED/NOT_FOUND/CONTRADICTED.",
  "verified_claims": [
    {"claim": "...", "status": "SUPPORTED | NOT_FOUND | CONTRADICTED", "note": "trích dẫn ngắn từ file hoặc lý do không tìm thấy"}
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

    The 'source' (or legacy 'file') field in JSON is like:
        20260206_PRT_DanhSach_Danh_sach_MC_final_10.md
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


def read_kb_file(file_name: Union[str, List[str]], kb_dir: str, max_chars: int = 80_000) -> Optional[str]:
    """
    Read full content of KB source file(s). Truncates at max_chars to stay within LLM limits.

    - If file_name is a list, concatenate all found files (in order).
    - Each file is separated with a clear header to help the LLM attribute claims.
    """
    # Normalize to list of strings
    if isinstance(file_name, list):
        names = [f for f in file_name if isinstance(f, str) and f.strip()]
    else:
        names = [file_name] if isinstance(file_name, str) and file_name else []

    if not names:
        return None

    parts: List[str] = []
    total_len = 0
    for name in names:
        path = find_kb_file(name, kb_dir)
        if path is None:
            continue
        content = path.read_text(encoding="utf-8")
        header = f"\n\n===== FILE: {path.name} =====\n"
        # Enforce global max_chars across all files
        remaining = max_chars - total_len
        if remaining <= 0:
            break
        chunk = (header + content)
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

def build_user_prompt(item: Dict) -> str:
    """Build Pass 1 evaluation prompt from QA item (uses chunk)."""
    return f"""
Question:
{item.get("question")}

Chunk:
{item.get("chunk")}

Answer:
{item.get("answer")}
""".strip()


def build_user_prompt_claim_extractor(item: Dict) -> str:
    """Build prompt for Claim Extractor — identifies extra claims beyond the chunk."""
    return f"""
Question:
{item.get("question")}

Chunk (retrieved context):
{item.get("chunk")}

Answer:
{item.get("answer")}
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
{item.get("question")}

Original Chunk (what Pass 1 used):
{original_chunk}

Extra Claims to Verify (identified by Claim Extractor — these were NOT in the Chunk above):
{claims_block}

Full Source File Content (search here to verify each claim):
{file_content}

Original Answer (for reference):
{item.get("answer")}
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

def parse_llm_response(response_text: str) -> Dict:
    """Extract and parse JSON from LLM response."""
    if not response_text:
        raise ValueError("Empty response from LLM")

    def _loads_relaxed(text: str) -> Dict:
        # Many model outputs are valid JSON except for unescaped newlines/control chars
        # inside string values. strict=False accepts those while still parsing the object.
        return json.loads(text, strict=False)

    candidates: List[str] = []

    fence_match = re.search(
        r"```(?:json)?\s*(\{.*?\})\s*```", response_text, re.DOTALL | re.IGNORECASE
    )
    if fence_match:
        candidates.append(fence_match.group(1).strip())

    json_match = re.search(r"\{.*\}", response_text, re.DOTALL)
    if json_match:
        candidates.append(json_match.group(0).strip())

    candidates.append(response_text.strip())

    last_error: Optional[Exception] = None
    for candidate in candidates:
        try:
            return _loads_relaxed(candidate)
        except json.JSONDecodeError as exc:
            last_error = exc

    raise last_error or json.JSONDecodeError("Unable to parse JSON", response_text, 0)


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
    messages = build_messages(provider_name, prompt, system=system)

    response_text = provider.chat(
        messages,
        temperature=temperature,
        max_tokens=2000,
    )

    try:
        return parse_llm_response(response_text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON response: {e}\nRaw: {response_text[:300]}")


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
            # Prefer "source" field for KB filename (newer datasets), fallback to "file"
            file_name = item.get("source", "") or item.get("file", "")
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
