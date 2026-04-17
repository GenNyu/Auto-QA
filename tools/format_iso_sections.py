from __future__ import annotations

import argparse
import re
from pathlib import Path


HEADING_RE = re.compile(r"^(#+)\s+(.*)$")
NUMERIC_RE = re.compile(r"^(\d+(?:\.\d+)*)\s*(.*)$")
ANNEX_RE = re.compile(r"^Annex\s+([A-Z])\b", re.IGNORECASE)


def strip_md(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[*_`#>\[\]\(\)]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def first_sentence(text: str) -> str:
    plain = strip_md(text)
    if not plain:
        return ""
    m = re.search(r"(?<=[.!?])\s+", plain)
    if m:
        return plain[: m.start()].strip()
    return plain


def bullets_from_text(text: str, limit: int = 4) -> list[str]:
    plain = strip_md(text)
    if not plain:
        return []
    parts = re.split(r"\s+(?=[a-z]\))|\s*;\s+|\.\s+", plain)
    out: list[str] = []
    for part in parts:
        item = part.strip(" -")
        if len(item) < 25:
            continue
        if item.lower().startswith(("table ", "figure ")):
            continue
        out.append(item)
        if len(out) >= limit:
            break
    return out


def parse_headed_sections(body: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current = "__intro__"
    sections[current] = []
    for line in body.splitlines():
        m = HEADING_RE.match(line)
        if m and len(m.group(1)) >= 2:
            current = strip_md(m.group(2)).lower()
            sections.setdefault(current, [])
            continue
        sections.setdefault(current, []).append(line)
    return {k: "\n".join(v).strip() for k, v in sections.items()}


def infer_label(title: str) -> tuple[str, str]:
    clean = strip_md(title)
    annex = ANNEX_RE.match(clean)
    if annex:
        annex_letter = annex.group(1).upper()
        suffix = clean[len(annex.group(0)) :].strip(" -:()")
        base = f"Annex {annex_letter}"
        return base, f"{base}" + (f" - {suffix}" if suffix else "")

    num = NUMERIC_RE.match(clean)
    if num:
        code, rest = num.groups()
        base = f"Section {code}"
        return base, f"{base}" + (f" - {rest}" if rest else "")

    lowered = clean.lower()
    if "bibliography" in lowered:
        return "Bibliography", "Bibliography"
    if "foreword" in lowered:
        return "Foreword", "Foreword"
    if "introduction" in lowered:
        return "Introduction", "Introduction"
    return clean, clean


def summarize_overview(label: str, full_title: str, sections: dict[str, str], body: str) -> list[str]:
    overview: list[str] = []
    intro = sections.get("__intro__", "")
    control = sections.get("control", "")
    purpose = sections.get("purpose", "")
    guidance = sections.get("guidance", "")

    if control:
        overview.append(
            f"Tài liệu này mô tả **{full_title}**, tập trung vào yêu cầu hoặc kiểm soát cốt lõi của mục này trong ISO/IEC 27002:2022."
        )
        source = purpose or control
        sentence = first_sentence(source)
        if sentence:
            overview.append(sentence)
    elif intro:
        overview.append(
            f"Tài liệu này mô tả **{full_title}** trong ISO/IEC 27002:2022, tập trung vào nội dung khái niệm, định nghĩa hoặc hướng dẫn ở phạm vi mục này."
        )
        sentence = first_sentence(intro)
        if sentence:
            overview.append(sentence)
    else:
        overview.append(f"Tài liệu này mô tả **{full_title}** trong ISO/IEC 27002:2022.")
        sentence = first_sentence(body)
        if sentence:
            overview.append(sentence)

    if guidance and len(overview) < 3:
        sentence = first_sentence(guidance)
        if sentence and sentence not in overview:
            overview.append(sentence)
    return overview[:3]


def key_points(full_title: str, sections: dict[str, str], body: str) -> list[str]:
    points: list[str] = []
    for heading, content in sections.items():
        if heading in {"__intro__", "control", "purpose", "guidance", "other information"}:
            continue
        heading_label = heading.title()
        sentence = first_sentence(content)
        if sentence:
            points.append(f"**{heading_label}:** {sentence}")
        if len(points) >= 4:
            return points

    for key in ("control", "purpose", "guidance", "other information", "__intro__"):
        content = sections.get(key, "")
        for bullet in bullets_from_text(content, limit=4):
            label = {
                "control": "Yêu cầu chính",
                "purpose": "Mục tiêu",
                "guidance": "Hướng dẫn",
                "other information": "Lưu ý thêm",
                "__intro__": "Nội dung",
            }[key]
            points.append(f"**{label}:** {bullet}")
            if len(points) >= 4:
                return points
    fallback = first_sentence(body)
    return [fallback] if fallback else []


def deep_summary(sections: dict[str, str], body: str) -> dict[str, list[str]]:
    context = first_sentence(sections.get("__intro__", "") or sections.get("control", "") or body)
    core_items = []
    for key in ("control", "purpose", "guidance"):
        content = sections.get(key, "")
        if not content:
            continue
        for bullet in bullets_from_text(content, limit=3):
            core_items.append(bullet)
            if len(core_items) >= 4:
                break
        if len(core_items) >= 4:
            break

    notable = []
    for heading in sections:
        if heading not in {"__intro__", "control", "purpose", "guidance", "other information"}:
            notable.append(heading.title())
        if len(notable) >= 5:
            break

    risks = bullets_from_text(sections.get("other information", "") or sections.get("guidance", ""), limit=4)
    return {
        "context": [context] if context else [],
        "core": core_items[:4],
        "notable": notable[:5],
        "risks": risks[:4],
    }


def build_output(title: str, body: str) -> str:
    label, full_title = infer_label(title)
    sections = parse_headed_sections(body)
    overview = summarize_overview(label, full_title, sections, body)
    points = key_points(full_title, sections, body)
    deep = deep_summary(sections, body)

    lines: list[str] = []
    lines.append(f"### A. Tài liệu gốc của {label}")
    lines.append("")
    lines.append(f"### B. Summary Overview của {label}")
    for item in overview:
        lines.append(item)
    lines.append("")
    lines.append(f"### C. Key Points của {label}")
    for item in points or ["- Không trích xuất được key point rõ ràng từ nội dung nguồn."]:
        prefix = "- " if not item.startswith("- ") else ""
        lines.append(f"{prefix}{item}")
    lines.append("")
    lines.append(f"### D. Deep Summary của {label}")
    lines.append("**Bối cảnh:**")
    lines.extend(deep["context"] or ["Nội dung mục này thiên về định nghĩa hoặc mô tả trực tiếp từ tài liệu nguồn."])
    lines.append("")
    lines.append("**Nội dung cốt lõi:**")
    for item in deep["core"] or ["Không có nhóm nội dung con rõ ràng ngoài phần văn bản chính."]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("**Dữ liệu đáng chú ý:**")
    for item in deep["notable"] or ["Không có chỉ số định lượng nổi bật; trọng tâm là nội dung quy định/hướng dẫn."]:
        prefix = "- "
        lines.append(f"{prefix}{item}")
    lines.append("")
    lines.append("**Rủi ro / Lưu ý:**")
    for item in deep["risks"] or ["Cần đối chiếu với ngữ cảnh triển khai thực tế vì đây là nội dung chuẩn/hướng dẫn gốc."]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append(f"### E. Structured Output của {label}")
    lines.append(body.strip())
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", default="iso")
    parser.add_argument("--output-dir", default="iso_formatted")
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)

    index_lines = ["# ISO Formatted Index", ""]
    count = 0
    for path in sorted(input_dir.glob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        raw = path.read_text(encoding="utf-8").strip()
        if not raw:
            continue
        lines = raw.splitlines()
        first = lines[0]
        title = strip_md(first.lstrip("#").strip()) if first.startswith("#") else path.stem
        body = "\n".join(lines)
        formatted = build_output(title, body)
        out_path = output_dir / path.name
        out_path.write_text(formatted, encoding="utf-8")
        count += 1
        index_lines.append(f"- `{path.name}`")

    index_lines.insert(2, f"Total files: {count}")
    (output_dir / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(f"formatted={count}")


if __name__ == "__main__":
    main()
