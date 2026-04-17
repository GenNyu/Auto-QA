---
name: format-text-kb
description: Create or normalize knowledge-base Markdown files into a 5-part A/B/C/D/E structure. Use when converting raw or semi-structured text into sections A-E, rewriting sections B/C/D to read naturally in Vietnamese, and reformatting section E into compact Markdown-first structured blocks.
---

# Format Text KB

Use this skill when a Markdown knowledge-base file needs a consistent five-part structure:

- `A. Tài liệu gốc`
- `B. Summary Overview`
- `C. Key Points`
- `D. Deep Summary`
- `E. Structured Output`

This skill is for text normalization and editorial formatting, not for factual enrichment beyond the source file.

## Outcome

Produce a file where:

- `A` is a heading placeholder for the original source section.
- `B`, `C`, and `D` are rewritten in natural Vietnamese and optimized for readability.
- `E` keeps the source meaning intact but is reformatted into compact, readable Markdown blocks with explicit labels.

## Workflow

1. Read the target file and identify whether it is:
   - raw source content,
   - partially formatted A-E content,
   - or already structured but poorly written.
2. Identify the document label from the main title.
   - Examples: `Section 5.28`, `Chương 5 (Control 5.7, 5.8)`, `Annex A`, `Chapter 1`, `Control Objective 1.1`.
3. Build or normalize the file into five sections:
   - `### A. Tài liệu gốc của <label>`
   - `### B. Summary Overview của <label>`
   - `### C. Key Points của <label>`
   - `### D. Deep Summary của <label>`
   - `### E. Structured Output của <label>`
   - For grouped chapter parts, prefer labels like `Chương 5 (Control 5.7, 5.8)` over `Section 5.7-5.8`.
4. Rewrite `B`, `C`, `D`.
5. Reformat `E` without changing source meaning, preferring Markdown over HTML.
6. Verify the file still reads as one consistent document.

## Writing Rules For B/C/D/E

- Write in natural Vietnamese.
- Prefer concise but complete business-style prose.
- Do not copy OCR noise, table headers, or raw layout artifacts into summaries.
- Do not invent facts not supported by the source.
- Avoid mixing English source sentences into `B`, `C`, or `D` except when keeping the official control title for identification.
- Prefer clear interpretations of:
  - mục tiêu,
  - phạm vi,
  - yêu cầu chính,
  - rủi ro vận hành,
  - lưu ý pháp lý hoặc triển khai.

### Section B

Write `B` as one compact overview block.

Content should:

- state what the section is about,
- explain the main objective,
- mention any especially important implementation or legal context.

Preferred style:

- Start with a concise overview of the section or group of controls.
- State the management or operational objective explicitly.
- When referring to grouped controls in the opening sentence, prefer `mục 5.7 và 5.8` or `mục 5.27, 5.28, 5.29` over `2 control` or `control liên tiếp`.
- If the file contains multiple controls, include a short `Gồm ... control chính:` list naming each control, with each bullet using this compact form:
  - `` `5.x`: English control title - diễn giải ngắn bằng tiếng Việt ``
- End with a short scope or applicability line when helpful.
- Prefer natural Vietnamese over literal translation.
- Reduce blank lines. In the preferred format:
  - keep the heading line,
  - then write the overview sentence,
  - the objective sentence,
  - the `Gồm ... control chính:` line,
  - the bullet list,
  - and the applicability sentence,
  - without extra blank lines between them.

### Section C

Use flat bullets.

- Prefer 3-5 bullets.
- Each bullet should capture one important point.
- Keep all bullets in Vietnamese, except for control identifiers or official English titles when needed.
- Use bold labels when helpful, for example:
  - `**Mục tiêu quản trị:**`
  - `**Yêu cầu chính của 5.x-5.y:**`
  - `**Điểm vận hành quan trọng:**`
  - `**Lưu ý thực tế:**`
- Prefer synthesizing related controls into one bullet when that makes the section easier to scan.
- Do not paste raw English requirement sentences as bullets unless there is a strong reason.

### Section D

Use this exact internal pattern:

- `**Bối cảnh:**`
- `**Nội dung cốt lõi:**`
- `**Dữ liệu đáng chú ý:**`
- `**Rủi ro / Lưu ý:**`

Guidance:

- `Bối cảnh`: 1 short paragraph.
- `Nội dung cốt lõi`: 3-5 bullets.
- `Dữ liệu đáng chú ý`: bullets for classification, references, scope, notable constraints, or meaningful distinctions across controls.
- `Rủi ro / Lưu ý`: concrete operational or legal cautions.
- `D` should be analytical, not mechanical.
- Avoid generic lines such as "nhóm control này liên quan đến..." unless they are followed by concrete interpretation.
- Do not simply restate raw control text. Explain what each control does in practice and why it matters.
- In `Dữ liệu đáng chú ý`, do not waste bullets on "có metadata". Extract the meaning of the metadata instead.
- In `Rủi ro / Lưu ý`, prefer realistic failure modes, implementation gaps, or governance consequences.

## Formatting Rules For E

`E` is structured output, not a freeform summary.

- Preserve source meaning.
- Reformat dense raw content into readable labeled blocks.
- Prefer pure Markdown. Avoid raw HTML tables unless there is no practical Markdown alternative.
- Replace raw HTML tables with Markdown tables, labeled fields, or bullets.
- Keep key labels explicit, for example:
  - `**Section:**`
  - `**Title:**`
  - `**Attributes:**`
  - `**Control:**`
  - `**Purpose:**`
  - `**Guidance:**`
  - `**Other information:**`
- For control entries, prefer this block order:
  - `**Section:**`
  - `**Title:**`
  - `**Attributes:**`
  - `**Control:**`
  - `**Purpose:**`
  - `**Guidance:**`
  - `***Examples ...:***` when the source contains examples or topic lists
  - `**Other information:**`
- Put metadata tables into compact Markdown tables, for example:
  - `| Field | Value |`
  - `| --- | --- |`
- If one file contains multiple controls, keep them in the same `E` section and separate each control clearly with headings or horizontal rules.
- Convert inline enumerations like `a)`, `b)`, `c)` into markdown bullets if that improves readability.
- Keep quotations, normative language, and standard references accurate.
- Reduce noise and character count where possible without losing meaning.
- Prefer compact spacing:
  - `**Section:**` and `**Title:**` should be consecutive lines with no blank line between them.
  - Use a single blank line only between major blocks such as `Title` -> `Attributes`, table -> `Control`, `Control` -> `Purpose`, `Purpose` -> `Guidance`, and `Guidance` -> `Other information`.
  - After labels such as `**Control:**`, `**Purpose:**`, `**Guidance:**`, and `**Other information:**`, put the content on the next line immediately, without an extra blank line.
  - For small subsection labels inside `Guidance` or other content blocks, use `***Label:***` instead of markdown headings like `## Label`.
  - Inside `Guidance`, avoid decorative blank lines. Keep paragraphs and bullet lists compact.
  - Do not add blank lines between consecutive bullet items.
  - When a bullet list ends and the next content is a paragraph, keep exactly one blank line before that paragraph.
  - When a bullet list follows a lead-in sentence, place the bullets directly after that sentence with no extra blank line.
  - When separating multiple controls in one file, use `---` and continue the next control block immediately after it.

## Heuristics By Content Type

### Definition entries

Examples: `3.1.1 access control`

- `B` should define the term plainly.
- `C` can be as short as 1-3 bullets.
- `D` should stay compact.
- `E` should preserve the original definition with minimal formatting, using simple labeled blocks rather than heavy tables.

### Control entries

Examples: `5.1`, `5.28`, `8.34`

- `B` should explain the control and why it matters.
- If several controls are grouped in one file, `B` should summarize the group first, then list the included controls briefly.
- `C` should emphasize requirement, objective, operational expectation, and caution.
- `D` should describe implementation and evidence/risk implications.
- `E` should present attributes and control details in labeled Markdown blocks.
- Convert source comparison tables or classification tables into Markdown tables.
- Prefer concise bullets in `Guidance` rather than large raw text walls when readability improves and meaning remains intact.
- For grouped controls, `C` and `D` should compare or connect the controls where useful, not treat them as isolated fragments.

### Annex or reference sections

- `B` should explain the annex purpose.
- `C` should focus on practical takeaways.
- `D` should explain how the annex is used.
- `E` may remain longer, but should still be reformatted for readability.

## Execution

If many files need conversion, use the bundled script:

- Read `scripts/format_text_kb.py`
- Run it on a directory of markdown files

If only one file needs refinement, edit manually and keep `E` aligned with the same file style.

## Bundled Script

Use `scripts/format_text_kb.py` for repeatable conversion of a directory of markdown files into A-E format. The script is a baseline generator. After generation, manually refine important files when the user asks for higher-quality editorial output.

## Reference Style

Use these files as the current reference style:

- `iso_test/chapter5_parts/5.1_5.2_part_01.md`
  - reference for strong analytical `D`
  - reference for labeled Markdown structure in `E`
- `iso_test/chapter5_parts/5.3_5.6_part_02.md`
  - reference for compact `B`
  - reference for Vietnamese-first `C`
  - reference for concrete, non-mechanical `D`
  - reference for compact-spacing `E`
- `iso_test/chapter5_parts/5.7_5.8_part_03.md`
  - reference for chapter-style labels such as `Chương 5 (Control 5.7, 5.8)`
