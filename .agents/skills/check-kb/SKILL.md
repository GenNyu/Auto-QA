---
name: check-kb
description: Audit knowledge-base question JSON against source documents, identify unsupported or poor-fit questions, and remove the entire JSON object when a question is not suitable.
---

# Check KB

Use this skill when a KB question set needs to be reviewed for fit against the source material.

Typical target files are JSON question banks such as `qa/iso/full_iso.json`, with source evidence in matching markdown files under `iso_test/` or related summary files.

## Goal

- Keep questions that are supported by the source and useful for retrieval or assessment.
- Remove questions that are duplicate, off-topic, too vague, misleading, or not grounded in the source.
- When a question is not suitable, delete the whole object `{...}` instead of editing it in place.

## Workflow

1. Read the target JSON and identify each object with its `id`, `question`, `gold`, and `file` fields.
2. Compare the question against the referenced source files.
3. Classify each question as:
   - `keep` if it is clear, source-backed, and non-duplicative.
   - `remove` if it is unsupported, redundant, malformed, overly ambiguous, or clearly out of scope.
4. Be conservative:
   - If the fit is uncertain, keep the question.
   - Prefer removing only when the mismatch is clear.
5. Apply edits by removing the entire JSON object for every `remove` decision.
6. Validate the file remains valid JSON after edits.

## Removal Heuristics

Remove a question when one or more of these apply:

- It duplicates another question in meaning or intent.
- It asks about a detail not present in the source file.
- It is too generic and does not test a specific concept from the source.
- It is awkwardly phrased in a way that changes the intended meaning.
- It combines multiple concepts in a way that makes the answer unreliable.
- It is obviously less useful than a nearby sibling question covering the same source point.

## Editing Rules

- Preserve array order unless a removal is required.
- Do not rewrite question text unless the task explicitly asks for rewording.
- Remove the full object, including `id`, `question`, `gold`, and `file`.
- Keep JSON formatting clean and machine-readable.
- After edits, re-run a JSON parse check.

## Practical Reading Order

1. `question`
2. `gold`
3. `file`
4. Source markdown content

Use that order to decide whether the question is actually grounded in the source before deleting anything.
