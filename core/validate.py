"""
Kiểm duyệt câu hỏi sinh ra, loại bỏ những câu "vô tri" — câu mà chatbot RAG
không thể trả lời đúng dù hệ thống hoạt động hoàn hảo.

Dùng được hai cách:
  1. Chặn ngay lúc sinh (script.py gọi QuestionValidator cho từng câu).
  2. Lọc file đã sinh sẵn (filter_questions.py gọi filter_questions()).

Các luật ở đây đều dựa trên lỗi đo được trong dữ liệu thật, không phải phỏng đoán.
"""
import re
import unicodedata
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Iterable, List, Optional, Set, Tuple


class ValidationReason(Enum):
    """Lý do một câu hỏi bị loại."""

    OK = "ok"
    MISSING_FIELDS = "missing_fields"          # thiếu câu hỏi hoặc đáp án mẫu
    TOO_SHORT = "too_short"                    # cụt, không đủ thông tin để hỏi
    DUPLICATE = "duplicate"                    # đã có câu y hệt
    DANGLING_REFERENCE = "dangling_reference"  # "tài liệu này", "bộ slide này"...
    METADATA_METRIC = "metadata_metric"        # hỏi về metadata thay vì nội dung
    GENERIC_PURPOSE = "generic_purpose"        # hỏi chung chung, tài liệu nào cũng đúng
    NOT_GROUNDED = "not_grounded"              # không bám vào chunk nguồn


@dataclass
class ValidationResult:
    is_valid: bool
    reason: ValidationReason = ValidationReason.OK
    details: str = ""
    confidence: float = 1.0


@dataclass
class FilterConfig:
    """Cấu hình lọc.

    min_confidence   : dưới mức này thì loại (0.0 - 1.0)
    exclude_reasons  : chỉ loại theo các lý do này; None = áp dụng tất cả luật
    """

    min_confidence: float = 0.7
    exclude_reasons: Optional[List[ValidationReason]] = None


# ─────────────────────────────────────────────
# CÁC MẪU NHẬN DIỆN
# ─────────────────────────────────────────────

# "tài liệu này", "bộ slide này", "biểu mẫu email này" — RAG không biết "này" là gì.
# Cố ý KHÔNG bắt chữ "trên" đứng một mình, vì "trên HubSpot" / "trên 15 ngày"
# là giới từ bình thường chứ không phải tham chiếu treo.
_GENERIC_NOUNS = (
    r"tài liệu|văn bản|chính sách|quy định|thông báo|thông tư|mẫu|biểu mẫu|template|"
    r"bảng|biểu|quy trình|hướng dẫn|file|bộ slide|slide|bộ tài liệu|nội dung|đoạn|"
    r"chương|mục|phần|điều khoản|form|brief"
)
DANGLING_PATTERNS = [
    re.compile(rf"\b({_GENERIC_NOUNS})\b[^?.!]{{0,40}}?\bnày\b", re.IGNORECASE),
    re.compile(r"\b(nêu trên|kể trên|nói trên|sau đây|dưới đây|ở trên)\b", re.IGNORECASE),
    re.compile(r"\b(đoạn|phần|mục)\s+(văn bản|trích|này|đó)\b", re.IGNORECASE),
]

# Hỏi về metadata của tài liệu chứ không phải kiến thức trong tài liệu.
METADATA_PATTERNS = [
    re.compile(r"\b(phiên bản|version|ver\.?)\s*(bao nhiêu|nào|là gì)", re.IGNORECASE),
    re.compile(r"\b(ngày ban hành|ngày hiệu lực|ngày cập nhật|ngày soạn)\b", re.IGNORECASE),
    re.compile(r"\b(mã|tên)\s+(tài liệu|văn bản|file)\b", re.IGNORECASE),
    re.compile(r"\b(ai là )?(người soạn|người biên soạn|tác giả)\s+(tài liệu|văn bản)", re.IGNORECASE),
]

# Câu hỏi mà tài liệu nào cũng trả lời được như nhau → không đo được gì.
GENERIC_PATTERNS = [
    re.compile(r"^\s*(tài liệu|văn bản|nội dung)\s+.{0,30}\b(nói|đề cập|trình bày)\s+về\s+(cái\s+)?gì",
               re.IGNORECASE),
    # Chỉ bắt khi KHÔNG nêu tên tài liệu cụ thể. "Mục đích của tài liệu
    # Assessment Matrix là gì?" là câu hợp lệ vì đã định danh rõ.
    re.compile(r"\bmục đích\s+(chính\s+)?của\s+(tài liệu|văn bản|bộ slide)\s+(này|là gì)",
               re.IGNORECASE),
    re.compile(r"\btài liệu\s+này\s+(dùng|dành)\s+để\s+làm\s+gì", re.IGNORECASE),
]

MIN_QUESTION_WORDS = 5
# Từ chức năng tiếng Việt — bỏ qua khi đo mức độ bám nguồn
_STOPWORDS = {
    "là", "và", "của", "có", "được", "cho", "khi", "nào", "gì", "ai", "sao", "thế",
    "những", "các", "một", "này", "đó", "trong", "với", "từ", "đến", "theo", "về",
    "phải", "sẽ", "bao", "nhiêu", "ra", "vào", "trên", "dưới", "tại", "bởi", "hay",
    "hoặc", "nếu", "thì", "mà", "để", "cần", "nên", "không", "như", "vì", "do",
}


def _normalize(text: str) -> str:
    """Chuẩn hoá để so trùng: bỏ dấu câu, gộp khoảng trắng, về chữ thường."""
    text = unicodedata.normalize("NFC", str(text or "").lower())
    text = re.sub(r"[^\w\s]", " ", text)
    return " ".join(text.split())


def _content_words(text: str) -> Set[str]:
    return {w for w in _normalize(text).split() if w not in _STOPWORDS and len(w) > 1}


# ─────────────────────────────────────────────
# BỘ KIỂM DUYỆT
# ─────────────────────────────────────────────

class QuestionValidator:
    """Kiểm duyệt từng câu hỏi. Có trạng thái: nhớ các câu đã gặp để chống trùng.

    Dùng CHUNG một instance cho cả lần chạy, và nạp sẵn câu hỏi đã có trong file
    output — nếu không, chạy lại `gen` sẽ nhân bản câu hỏi cũ.
    """

    # Mặc định TẮT kiểm tra bám nguồn theo từ vựng (0.0). Đo trên dữ liệu thật cho
    # thấy nó loại nhầm câu tốt: chunk là danh sách cột tiếng Anh
    # ("Owner, Contact Type, First Name...") còn câu hỏi mô tả bằng tiếng Việt
    # ("Bảng thông tin khách hàng gồm những cột nào?") → 0% trùng từ nhưng câu hỏi
    # hoàn toàn hợp lệ. Chỉ bật (vd 0.15) khi tài liệu và câu hỏi cùng ngôn ngữ.
    def __init__(self, seen_questions: Optional[Iterable[str]] = None,
                 min_grounding: float = 0.0) -> None:
        self._seen: Set[str] = set()
        self.min_grounding = min_grounding
        for q in seen_questions or []:
            self.remember(q)

    def remember(self, question: str) -> None:
        """Ghi nhận một câu đã tồn tại, để lần sau coi là trùng."""
        key = _normalize(question)
        if key:
            self._seen.add(key)

    def __len__(self) -> int:
        return len(self._seen)

    def validate(self, question: str, chunk: str = "", gold: str = "") -> ValidationResult:
        """Kiểm một câu hỏi. KHÔNG tự ghi nhớ — gọi remember() khi đã nhận câu đó."""
        question = (question or "").strip()

        if not question:
            return ValidationResult(False, ValidationReason.MISSING_FIELDS,
                                    "Câu hỏi rỗng", 0.0)

        if len(question.split()) < MIN_QUESTION_WORDS:
            return ValidationResult(False, ValidationReason.TOO_SHORT,
                                    f"Chỉ có {len(question.split())} từ", 0.0)

        key = _normalize(question)
        if key in self._seen:
            return ValidationResult(False, ValidationReason.DUPLICATE,
                                    "Đã có câu hỏi giống hệt", 0.0)

        for pattern in DANGLING_PATTERNS:
            found = pattern.search(question)
            if found:
                return ValidationResult(
                    False, ValidationReason.DANGLING_REFERENCE,
                    f"Tham chiếu treo: '{found.group(0)}' — chatbot không biết đang nói tài liệu nào",
                    0.0,
                )

        for pattern in METADATA_PATTERNS:
            if pattern.search(question):
                return ValidationResult(False, ValidationReason.METADATA_METRIC,
                                        "Hỏi về metadata tài liệu, không phải nội dung", 0.0)

        for pattern in GENERIC_PATTERNS:
            if pattern.search(question):
                return ValidationResult(False, ValidationReason.GENERIC_PURPOSE,
                                        "Câu hỏi chung chung, tài liệu nào cũng đúng", 0.0)

        # Bám nguồn: câu hỏi phải dùng lại từ vựng của chunk. Chỉ chấm khi bật.
        if chunk and self.min_grounding > 0:
            q_words = _content_words(question)
            if q_words:
                overlap = len(q_words & _content_words(chunk)) / len(q_words)
                if overlap < self.min_grounding:
                    return ValidationResult(
                        False, ValidationReason.NOT_GROUNDED,
                        f"Chỉ {overlap:.0%} từ khoá của câu hỏi xuất hiện trong chunk nguồn",
                        round(overlap, 3),
                    )
                return ValidationResult(True, ValidationReason.OK, "", round(min(1.0, overlap * 2), 3))

        return ValidationResult(True, ValidationReason.OK, "", 1.0)


def filter_questions(
    qa_pairs: List[Dict],
    config: Optional[FilterConfig] = None,
) -> Tuple[List[Dict], Dict]:
    """Lọc một danh sách QA pair, trả về (danh sách hợp lệ, thống kê)."""
    config = config or FilterConfig()
    validator = QuestionValidator()

    kept: List[Dict] = []
    by_reason: Dict[str, int] = {}

    for pair in qa_pairs:
        question = pair.get("question", "")
        result = validator.validate(
            question,
            pair.get("chunk", ""),
            pair.get("check", "") or pair.get("gold", ""),
        )

        rejected = not result.is_valid
        # exclude_reasons giới hạn luật được áp dụng; lý do ngoài danh sách thì bỏ qua.
        if rejected and config.exclude_reasons is not None:
            rejected = result.reason in config.exclude_reasons
        # Câu qua hết luật nhưng độ tin cậy thấp cũng bị loại.
        if not rejected and result.is_valid and result.confidence < config.min_confidence:
            rejected = True
            result = ValidationResult(False, ValidationReason.NOT_GROUNDED,
                                      f"Độ tin cậy {result.confidence} < {config.min_confidence}",
                                      result.confidence)

        if rejected:
            by_reason[result.reason.value] = by_reason.get(result.reason.value, 0) + 1
            continue

        validator.remember(question)
        kept.append(pair)

    stats = {
        "total": len(qa_pairs),
        "valid": len(kept),
        "rejected": len(qa_pairs) - len(kept),
        "by_reason": by_reason,
    }
    return kept, stats
