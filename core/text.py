"""Text helpers shared by the generator and the evaluator."""


def normalize_text(value) -> str:
    """Collapse all whitespace runs into single spaces, for fuzzy matching."""
    if value is None:
        return ""
    return " ".join(str(value).split()).strip()
