from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any


HEADING_RE = re.compile(r"^(#+)\s+(.*)$")
NUMERIC_RE = re.compile(r"^(\d+(?:\.\d+)*)\s*(.*)$")
ANNEX_RE = re.compile(r"^Annex\s+([A-Z])\b", re.IGNORECASE)
HTML_ROW_RE = re.compile(r"<tr>(.*?)</tr>", re.IGNORECASE | re.DOTALL)
HTML_CELL_RE = re.compile(r"<t[dh][^>]*>(.*?)</t[dh]>", re.IGNORECASE | re.DOTALL)
HTML_TABLE_RE = re.compile(r"<table>.*?</table>", re.IGNORECASE | re.DOTALL)
LIST_ITEM_RE = re.compile(r"^[a-z]\)\s*(.*)$", re.IGNORECASE)
FORMATTED_AE_RE = re.compile(r"^### A\. Tài liệu gốc của ", re.MULTILINE)

KNOWN_SECTION_HEADINGS = {
    "control",
    "purpose",
    "guidance",
    "other information",
}

TITLE_VI_HINTS = [
    ("policies for information security", "thiết lập và duy trì chính sách an toàn thông tin"),
    ("information security roles and responsibilities", "xác định và phân bổ vai trò, trách nhiệm an toàn thông tin"),
    ("segregation of duties", "phân tách nhiệm vụ và trách nhiệm xung đột"),
    ("management responsibilities", "làm rõ trách nhiệm của quản lý trong việc buộc nhân sự tuân thủ yêu cầu an toàn thông tin"),
    ("contact with authorities", "duy trì liên hệ với cơ quan có thẩm quyền hoặc cơ quan quản lý liên quan"),
    ("contact with special interest groups", "duy trì liên hệ với các nhóm chuyên môn, diễn đàn hoặc hiệp hội an toàn thông tin"),
    ("threat intelligence", "thu thập và phân tích thông tin tình báo về mối đe dọa"),
    ("information security in project management", "tích hợp an toàn thông tin vào quản lý dự án"),
    ("inventory of information and other associated assets", "xây dựng và duy trì danh mục tài sản thông tin và tài sản liên quan"),
    ("acceptable use of information and other associated assets", "thiết lập quy tắc sử dụng và xử lý tài sản thông tin đúng cách"),
    ("return of assets", "bảo đảm tài sản được hoàn trả khi thay đổi hoặc chấm dứt quan hệ làm việc"),
    ("classification of information", "phân loại thông tin theo mức độ nhạy cảm và yêu cầu bảo vệ"),
    ("labelling of information", "gắn nhãn thông tin phù hợp với sơ đồ phân loại"),
    ("information transfer", "kiểm soát việc truyền tải thông tin trong và ngoài tổ chức"),
    ("access control", "thiết lập và thực thi kiểm soát truy cập"),
    ("identity management", "quản lý toàn bộ vòng đời danh tính"),
    ("authentication information", "kiểm soát việc cấp phát và quản lý thông tin xác thực"),
    ("access rights", "cấp, rà soát, điều chỉnh và thu hồi quyền truy cập"),
    ("supplier", "quản lý rủi ro an toàn thông tin trong quan hệ với nhà cung cấp"),
    ("cloud services", "kiểm soát việc sử dụng dịch vụ đám mây"),
    ("incident", "chuẩn bị và xử lý sự cố an toàn thông tin"),
    ("collection of evidence", "thu thập và bảo toàn bằng chứng liên quan đến sự kiện an toàn thông tin"),
    ("business continuity", "duy trì an toàn thông tin và khả năng liên tục hoạt động"),
    ("legal, statutory, regulatory and contractual requirements", "xác định và duy trì tuân thủ các yêu cầu pháp lý, quy định và hợp đồng"),
    ("intellectual property rights", "bảo vệ quyền sở hữu trí tuệ"),
    ("protection of records", "bảo vệ hồ sơ khỏi mất mát, sửa đổi hoặc truy cập trái phép"),
    ("privacy and protection of pii", "bảo vệ quyền riêng tư và dữ liệu nhận dạng cá nhân"),
    ("independent review of information security", "đánh giá độc lập cách tổ chức quản lý an toàn thông tin"),
    ("compliance with policies, rules and standards for information security", "rà soát việc tuân thủ chính sách, quy tắc và tiêu chuẩn an toàn thông tin"),
    ("documented operating procedures", "duy trì thủ tục vận hành được lập thành văn bản"),
]


def strip_md(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[*_`#>\[\]\(\)]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
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


def first_nonempty_line(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return ""


def title_vi_hint(title: str) -> str:
    lowered = title.lower()
    for needle, hint in TITLE_VI_HINTS:
        if needle in lowered:
            return hint
    return f"xử lý nội dung liên quan đến {title}"


def codes_phrase(codes: list[str]) -> str:
    if len(codes) == 2:
        return f"{codes[0]} và {codes[1]}"
    return ", ".join(codes)


def grouped_items_phrase(codes: list[str]) -> str:
    if len(codes) == 1:
        return f"mục {codes[0]}"
    if len(codes) == 2:
        return f"mục {codes[0]} và {codes[1]}"
    return f"mục {', '.join(codes[:-1])}, {codes[-1]}"


def compact_title_bullet(block: dict[str, Any]) -> str:
    return f"- `{block['code']}`: {block['title']} - {title_vi_hint(block['title'])}"


def compact_attr_name(name: str) -> str:
    return (
        name.replace("Informationsecurity", "Information security")
        .replace("Cybersecurityconcepts", "Cybersecurity concepts")
        .replace("Operationalcapabilities", "Operational capabilities")
        .replace("Informationsecurity properties", "Information security properties")
    )


def parse_intro_attributes(intro: str) -> list[tuple[str, str]]:
    table_match = HTML_TABLE_RE.search(intro)
    if not table_match:
        return []
    rows = html_table_to_rows(table_match.group(0))
    if len(rows) < 2 or len(rows[0]) != len(rows[1]):
        return []
    return [(compact_attr_name(left), right) for left, right in zip(rows[0], rows[1])]


def parse_tag_values(value: str) -> list[str]:
    tags = re.findall(r"#[A-Za-z0-9_-]+", value)
    return tags


def metadata_meaning(block: dict[str, Any]) -> list[str]:
    attrs = dict(parse_intro_attributes(block["sections"].get("__intro__", "")))
    bullets: list[str] = []
    control_type = parse_tag_values(attrs.get("Control type", ""))
    if control_type:
        control_desc = ", ".join(control_type)
        bullets.append(f"`{block['code']}` được phân loại là kiểm soát {control_desc}.")
    concepts = parse_tag_values(attrs.get("Cybersecurity concepts", ""))
    if concepts:
        bullets.append(f"`{block['code']}` gắn với các khái niệm {', '.join(concepts)}.")
    domains = parse_tag_values(attrs.get("Security domains", ""))
    if domains:
        bullets.append(f"`{block['code']}` tác động tới các miền {', '.join(domains[:3])}.")
    return bullets


def risk_hint_from_title(title: str) -> str:
    lowered = title.lower()
    if "segregation" in lowered:
        return "Nếu không phân tách nhiệm vụ hợp lý, tổ chức dễ phát sinh gian lận nội bộ, sai sót vận hành hoặc tình huống một cá nhân có thể tự vượt qua các lớp kiểm soát."
    if "management responsibilities" in lowered:
        return "Nếu cấp quản lý không thực sự thực thi vai trò của mình, chính sách an toàn thông tin sẽ khó chuyển thành hành vi tuân thủ hàng ngày."
    if "authorities" in lowered or "special interest groups" in lowered:
        return "Nếu thiếu đầu mối liên hệ bên ngoài, tổ chức có thể phản ứng chậm với sự cố, bỏ lỡ cảnh báo quan trọng hoặc cập nhật pháp lý mới."
    if "supplier" in lowered:
        return "Nếu quan hệ với nhà cung cấp không được kiểm soát, rủi ro lan truyền từ bên thứ ba có thể ảnh hưởng trực tiếp đến thông tin và dịch vụ của tổ chức."
    if "incident" in lowered:
        return "Nếu quy trình xử lý sự cố không rõ hoặc không được luyện tập, tổ chức có thể chậm phát hiện, chậm phân loại và phản ứng kém hiệu quả."
    if "access" in lowered or "identity" in lowered or "authentication" in lowered:
        return "Nếu vòng đời danh tính và quyền truy cập không được kiểm soát chặt, nguy cơ truy cập trái phép hoặc lạm dụng quyền sẽ tăng lên."
    if "asset" in lowered or "classification" in lowered or "labelling" in lowered:
        return "Nếu tài sản và thông tin không được nhận diện, phân loại hoặc gắn nhãn rõ, các biện pháp bảo vệ dễ bị áp dụng sai hoặc không đầy đủ."
    return "Nếu triển khai không đầy đủ, control này có thể mất hiệu lực trong thực tế và làm suy yếu khả năng quản trị an toàn thông tin."


def control_implication(block: dict[str, Any]) -> str:
    title = block["title"]
    lowered = title.lower()
    if "segregation" in lowered:
        return f"`{block['code']}` yêu cầu phân tách các nhiệm vụ hoặc vùng trách nhiệm xung đột để không một cá nhân nào có thể tự mình thực hiện trọn vẹn chuỗi hành động nhạy cảm."
    if "management responsibilities" in lowered:
        return f"`{block['code']}` yêu cầu cấp quản lý chủ động bảo đảm nhân sự hiểu vai trò an toàn thông tin của mình và có đủ điều kiện để tuân thủ yêu cầu đã ban hành."
    if "contact with authorities" in lowered:
        return f"`{block['code']}` yêu cầu tổ chức duy trì kênh liên hệ với cơ quan có thẩm quyền để phục vụ báo cáo sự cố, đáp ứng yêu cầu pháp lý và nắm bắt kỳ vọng quản lý mới."
    if "contact with special interest groups" in lowered:
        return f"`{block['code']}` yêu cầu tổ chức duy trì liên hệ với các nhóm chuyên môn để cập nhật thực hành tốt, cảnh báo sớm và kinh nghiệm ứng phó sự cố."
    if "inventory" in lowered:
        return f"`{block['code']}` yêu cầu tổ chức nhận diện và duy trì danh mục tài sản để có cơ sở phân loại, gán chủ sở hữu và áp dụng biện pháp bảo vệ phù hợp."
    if "acceptable use" in lowered:
        return f"`{block['code']}` yêu cầu tổ chức xác lập quy tắc sử dụng và xử lý tài sản thông tin rõ ràng để hạn chế lạm dụng hoặc thao tác sai."
    control = first_sentence(block["sections"].get("control", ""))
    if control:
        return f"`{block['code']}` tập trung vào việc {title_vi_hint(title)}."
    return f"`{block['code']}` tập trung vào việc {title_vi_hint(title)}."


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


def split_control_blocks(body: str) -> tuple[str, list[dict[str, Any]]]:
    doc_title = ""
    blocks: list[dict[str, Any]] = []
    current_block: dict[str, Any] | None = None
    current_section = "__intro__"

    for line in body.splitlines():
        m = HEADING_RE.match(line)
        if m and len(m.group(1)) >= 2:
            heading = strip_md(m.group(2))
            heading_lower = heading.lower()
            numeric = NUMERIC_RE.match(heading)

            is_control_heading = bool(
                numeric
                and "." in numeric.group(1)
                and heading_lower not in KNOWN_SECTION_HEADINGS
            )

            if is_control_heading:
                code, title = numeric.groups()
                current_block = {
                    "code": code,
                    "title": title.strip(),
                    "sections": {"__intro__": []},
                }
                blocks.append(current_block)
                current_section = "__intro__"
                continue

            if not blocks and not doc_title and numeric and "." not in numeric.group(1):
                doc_title = heading
                continue

            if current_block and heading_lower in KNOWN_SECTION_HEADINGS:
                current_section = heading_lower
                current_block["sections"].setdefault(current_section, [])
                continue

        if current_block:
            current_block["sections"].setdefault(current_section, []).append(line)

    normalized_blocks: list[dict[str, Any]] = []
    for block in blocks:
        normalized_sections = {
            key: "\n".join(value).strip()
            for key, value in block["sections"].items()
        }
        normalized_blocks.append(
            {
                "code": block["code"],
                "title": block["title"],
                "sections": normalized_sections,
            }
        )
    return doc_title, normalized_blocks


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


def infer_group_label(title: str, doc_title: str, blocks: list[dict[str, Any]]) -> tuple[str, str]:
    if not blocks:
        return infer_label(title)

    chapter_match = NUMERIC_RE.match(strip_md(doc_title))
    if chapter_match and "." not in chapter_match.group(1):
        chapter_code = chapter_match.group(1)
        controls = ", ".join(block["code"] for block in blocks)
        label = f"Chương {chapter_code} (Control {controls})"
        return label, label

    if len(blocks) == 1:
        code = blocks[0]["code"]
        block_title = blocks[0]["title"]
        base = f"Section {code}"
        return base, f"{base} - {block_title}" if block_title else base

    first_code = blocks[0]["code"]
    last_code = blocks[-1]["code"]
    base = f"Section {first_code}-{last_code}"
    return base, base


def summarize_overview(label: str, full_title: str, sections: dict[str, str], body: str) -> list[str]:
    overview: list[str] = []
    intro = sections.get("__intro__", "")
    control = sections.get("control", "")
    purpose = sections.get("purpose", "")
    guidance = sections.get("guidance", "")

    if control:
        overview.append(
            f"Tài liệu này mô tả **{full_title}** trong tài liệu nguồn, tập trung vào yêu cầu hoặc kiểm soát cốt lõi của mục này."
        )
        sentence = first_sentence(purpose or control)
        if sentence:
            overview.append(sentence)
    elif intro:
        overview.append(
            f"Tài liệu này mô tả **{full_title}**, tập trung vào nội dung khái niệm, định nghĩa hoặc hướng dẫn ở phạm vi mục này."
        )
        sentence = first_sentence(intro)
        if sentence:
            overview.append(sentence)
    else:
        overview.append(f"Tài liệu này mô tả **{full_title}**.")
        sentence = first_sentence(body)
        if sentence:
            overview.append(sentence)

    if guidance and len(overview) < 3:
        sentence = first_sentence(guidance)
        if sentence and sentence not in overview:
            overview.append(sentence)
    return overview[:3]


def summarize_group_overview(
    title: str,
    blocks: list[dict[str, Any]],
) -> list[str]:
    codes = [block["code"] for block in blocks]
    grouped_phrase = grouped_items_phrase(codes)
    overview = [
        (
            f"Tài liệu này mô tả chi tiết **{grouped_phrase}** "
            f"trong **{title}**, tập trung vào các cơ chế quản trị và vận hành cần thiết để triển khai an toàn thông tin một cách nhất quán."
        )
    ]

    hints = [title_vi_hint(block["title"]) for block in blocks[:3]]
    if hints:
        hint_text = ", ".join(hints[:-1] + [f"và {hints[-1]}"] if len(hints) > 1 else hints)
        overview.append(f"Mục tiêu chung của nhóm nội dung này là **bảo đảm** {hint_text}.")

    overview.append("Gồm các control chính:")
    for block in blocks:
        overview.append(compact_title_bullet(block))

    overview.append(
        "Áp dụng cho các cá nhân, bộ phận và vai trò liên quan đến việc thiết lập, triển khai hoặc vận hành yêu cầu an toàn thông tin trong phạm vi nội dung của tài liệu."
    )
    return overview


def key_points(sections: dict[str, str], body: str) -> list[str]:
    points: list[str] = []
    control = sections.get("control", "")
    purpose = sections.get("purpose", "")
    guidance = sections.get("guidance", "")
    other = sections.get("other information", "")

    if control:
        points.append(f"**Yêu cầu chính:** {first_sentence(control)}")
    if purpose:
        points.append(f"**Mục tiêu:** {first_sentence(purpose)}")
    if guidance:
        g = bullets_from_text(guidance, limit=1)
        if g:
            points.append(f"**Yêu cầu vận hành:** {g[0]}")
    if other:
        o = bullets_from_text(other, limit=1)
        if o:
            points.append(f"**Lưu ý thực tế:** {o[0]}")

    if points:
        return points[:4]

    fallback = first_sentence(body)
    return [fallback] if fallback else []


def key_points_for_blocks(blocks: list[dict[str, Any]]) -> list[str]:
    if not blocks:
        return []
    first = blocks[0]
    last = blocks[-1]
    range_label = first["code"] if len(blocks) == 1 else f"{first['code']}-{last['code']}"
    hints = [title_vi_hint(block["title"]) for block in blocks[:3]]
    hint_text = ", ".join(hints[:-1] + [f"và {hints[-1]}"] if len(hints) > 1 else hints)
    points = [f"**Mục tiêu quản trị:** Nhóm control này giúp tổ chức {hint_text}."]

    if len(blocks) >= 2:
        points.append(
            f"**Yêu cầu chính của {range_label}:** "
            + " ".join(control_implication(block) for block in blocks[:2])
        )
    else:
        points.append(f"**Yêu cầu chính của {range_label}:** {control_implication(first)}")

    operational = strip_md(first_nonempty_line(first["sections"].get("guidance", "")))
    if operational:
        points.append(
            f"**Điểm vận hành quan trọng:** Tổ chức cần đặc biệt lưu ý rằng {operational[:180].rstrip('.')}."
        )

    points.append(f"**Lưu ý thực tế:** {risk_hint_from_title(first['title'])}")
    return points[:5]


def deep_summary(sections: dict[str, str], body: str) -> dict[str, list[str]]:
    context = first_sentence(sections.get("__intro__", "") or sections.get("control", "") or body)
    core_items = []
    for key in ("control", "purpose", "guidance"):
        content = sections.get(key, "")
        for bullet in bullets_from_text(content, limit=4):
            core_items.append(bullet)
            if len(core_items) >= 4:
                break
        if len(core_items) >= 4:
            break

    notable = []
    attrs = sections.get("__intro__", "")
    if attrs and "control type" in attrs.lower():
        notable.append("Có metadata phân loại control và thuộc tính bảo mật đi kèm.")
    refs = re.findall(r"ISO/IEC\s+\d+", body)
    for ref in dict.fromkeys(refs):
        notable.append(f"Viện dẫn tiêu chuẩn liên quan: {ref}.")
        if len(notable) >= 3:
            break

    risks = bullets_from_text(sections.get("other information", "") or sections.get("guidance", ""), limit=4)
    return {
        "context": [context] if context else [],
        "core": core_items[:4],
        "notable": notable[:4],
        "risks": risks[:4],
    }


def deep_summary_for_blocks(blocks: list[dict[str, Any]]) -> dict[str, list[str]]:
    first = blocks[0]
    last = blocks[-1]
    context = [
        f"Nhóm control `{first['code']}-{last['code']}` tập trung vào việc biến định hướng quản trị an toàn thông tin thành các cơ chế triển khai cụ thể trong phạm vi nội dung được gom trong cùng tài liệu."
    ]
    core: list[str] = []
    notable: list[str] = []
    risks: list[str] = []

    for block in blocks:
        core.append(control_implication(block))
        for item in metadata_meaning(block):
            if item not in notable:
                notable.append(item)
            if len(notable) >= 4:
                break
        risk = risk_hint_from_title(block["title"])
        if risk not in risks:
            risks.append(risk)

    return {
        "context": context,
        "core": core[:5],
        "notable": notable[:4],
        "risks": risks[:4],
    }


def html_table_to_rows(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for row_html in HTML_ROW_RE.findall(text):
        cells = []
        for cell_html in HTML_CELL_RE.findall(row_html):
            cell = strip_html(cell_html)
            if cell:
                cells.append(cell)
        if cells:
            rows.append(cells)
    return rows


def markdown_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    normalized = [row + [""] * (width - len(row)) for row in rows]
    header = normalized[0]
    separator = ["---"] * width
    body = normalized[1:] or [[]]
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(separator) + " |",
    ]
    for row in body:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def attributes_block_from_intro(intro: str) -> str:
    table_match = HTML_TABLE_RE.search(intro)
    if not table_match:
        plain = strip_md(intro)
        if not plain:
            return ""
        return f"- {plain}"

    rows = html_table_to_rows(table_match.group(0))
    if len(rows) >= 2 and len(rows[0]) == len(rows[1]):
        pairs = [["Field", "Value"]]
        pairs.extend([[left, right] for left, right in zip(rows[0], rows[1])])
        return markdown_table(pairs)
    return markdown_table(rows)


def normalize_content_lines(text: str) -> list[str]:
    if not text.strip():
        return []

    def repl_table(match: re.Match[str]) -> str:
        table = markdown_table(html_table_to_rows(match.group(0)))
        return f"\n{table}\n" if table else "\n"

    text = HTML_TABLE_RE.sub(repl_table, text)
    raw_lines = [line.rstrip() for line in text.splitlines()]
    lines: list[str] = []
    prev_blank = True

    for raw in raw_lines:
        line = raw.strip()
        if not line:
            if not prev_blank:
                lines.append("")
            prev_blank = True
            continue

        list_item = LIST_ITEM_RE.match(line)
        if list_item:
            lines.append(f"- {list_item.group(1).strip()}")
            prev_blank = False
            continue

        heading_match = re.match(r"^#{2,6}\s+(.*)$", line)
        if heading_match:
            label = strip_md(heading_match.group(1)).rstrip(":")
            if label:
                lines.append(f"***{label}:***")
                prev_blank = False
                continue

        lines.append(line)
        prev_blank = False

    while lines and not lines[-1]:
        lines.pop()
    return lines


def extract_examples_block(lines: list[str]) -> tuple[list[str], tuple[str, list[str]] | None]:
    for idx, line in enumerate(lines):
        lower = line.lower()
        if "examples of" in lower and lower.endswith("include:"):
            items: list[str] = []
            j = idx + 1
            while j < len(lines):
                candidate = lines[j]
                if not candidate:
                    j += 1
                    continue
                if not candidate.startswith("- "):
                    break
                items.append(candidate)
                j += 1
            if items:
                label = line.rstrip(":")
                remaining = lines[:idx] + lines[j:]
                while remaining and not remaining[-1]:
                    remaining.pop()
                return remaining, (label, items)
    return lines, None


def append_labeled_block(lines: list[str], label: str, content_lines: list[str]) -> None:
    if not content_lines:
        return
    if lines:
        lines.append("")
    lines.append(f"**{label}:**")
    lines.extend(content_lines)


def append_minor_labeled_block(lines: list[str], label: str, content_lines: list[str]) -> None:
    if not content_lines:
        return
    if lines:
        lines.append("")
    lines.append(f"***{label.rstrip(':')}:***")
    lines.extend(content_lines)


def format_control_block(block: dict[str, Any]) -> str:
    sections = block["sections"]
    lines: list[str] = [
        f"**Section:** {block['code']}",
        f"**Title:** {block['title']}",
    ]

    attrs = attributes_block_from_intro(sections.get("__intro__", ""))
    if attrs:
        lines.append("")
        lines.append("**Attributes:**")
        lines.extend(attrs.splitlines())

    append_labeled_block(lines, "Control", normalize_content_lines(sections.get("control", "")))
    append_labeled_block(lines, "Purpose", normalize_content_lines(sections.get("purpose", "")))

    guidance_lines = normalize_content_lines(sections.get("guidance", ""))
    guidance_lines, examples_block = extract_examples_block(guidance_lines)
    append_labeled_block(lines, "Guidance", guidance_lines)
    if examples_block:
        append_minor_labeled_block(lines, examples_block[0], examples_block[1])

    append_labeled_block(lines, "Other information", normalize_content_lines(sections.get("other information", "")))

    return "\n".join(lines)


def format_structured_output(title: str, sections: dict[str, str], body: str) -> str:
    label, full_title = infer_label(title)
    intro = sections.get("__intro__", "")
    control = sections.get("control", "")
    purpose = sections.get("purpose", "")
    guidance = sections.get("guidance", "")
    other = sections.get("other information", "")

    if control or purpose or guidance:
        lines = [
            f"**Section:** {label.replace('Section ', '')}" if label.startswith("Section ") else f"**Section:** {label}",
            f"**Title:** {full_title.replace(label + ' - ', '').replace(label + ' ', '')}",
            "",
        ]
        if intro and "control type" in intro.lower():
            attrs = strip_md(intro)
            lines.extend(
                [
                    "**Attributes:**",
                    f"- {attrs}",
                    "",
                ]
            )
        if control:
            lines.extend(["**Control:**  ", control, ""])
        if purpose:
            lines.extend(["**Purpose:**  ", purpose, ""])
        if guidance:
            lines.extend(["**Guidance:**  ", guidance, ""])
        if other:
            lines.extend(["**Other information:**  ", other, ""])
        return "\n".join(lines).strip()

    return body.strip()


def format_structured_output_for_blocks(blocks: list[dict[str, Any]]) -> str:
    chunks = [format_control_block(block) for block in blocks]
    return "\n\n---\n\n".join(chunk for chunk in chunks if chunk.strip())


def build_output(title: str, body: str) -> str:
    doc_title, blocks = split_control_blocks(body)

    if blocks:
        label, full_title = infer_group_label(title, doc_title, blocks)
        overview = summarize_group_overview(doc_title or title, blocks)
        points = key_points_for_blocks(blocks)
        deep = deep_summary_for_blocks(blocks)
        structured = format_structured_output_for_blocks(blocks)
    else:
        label, full_title = infer_label(title)
        sections = parse_headed_sections(body)
        overview = summarize_overview(label, full_title, sections, body)
        points = key_points(sections, body)
        deep = deep_summary(sections, body)
        structured = format_structured_output(title, sections, body)

    lines: list[str] = []
    lines.append(f"### A. Tài liệu gốc của {label}")
    lines.append("")
    lines.append(f"### B. Summary Overview của {label}")
    lines.extend(overview or [f"Tài liệu này mô tả **{full_title}**."])
    lines.append("")
    lines.append(f"### C. Key Points của {label}")
    for item in points or ["Không trích xuất được key point rõ ràng từ nội dung nguồn."]:
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
        lines.append(f"- {item}")
    lines.append("")
    lines.append("**Rủi ro / Lưu ý:**")
    for item in deep["risks"] or ["Cần đối chiếu với ngữ cảnh triển khai thực tế vì đây là nội dung chuẩn/hướng dẫn gốc."]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append(f"### E. Structured Output của {label}")
    lines.append(structured)
    lines.append("")
    return "\n".join(lines)


def is_already_formatted(raw: str) -> bool:
    return bool(FORMATTED_AE_RE.search(raw))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    count = 0
    for path in sorted(input_dir.glob("*.md")):
        raw = path.read_text(encoding="utf-8").strip()
        if not raw:
            continue
        lines = raw.splitlines()
        first = lines[0]
        title = strip_md(first.lstrip("#").strip()) if first.startswith("#") else path.stem
        out_path = output_dir / path.name
        output = raw if is_already_formatted(raw) else build_output(title, raw)
        out_path.write_text(output, encoding="utf-8")
        count += 1

    print(f"formatted={count}")


if __name__ == "__main__":
    main()
