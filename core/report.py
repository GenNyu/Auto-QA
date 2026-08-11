"""
Dựng báo cáo HTML tĩnh từ file kết quả đã chấm điểm.

Báo cáo là một file duy nhất, không cần server, gửi qua chat được.
Nội dung lấy trực tiếp từ các trường mà evaluate.py đã ghi ra:
  score     điểm 1-10
  evaluate  correct | unclear | incorrect
  check     lý do chấm điểm (tiếng Việt)
  rechecked có chạy đối chiếu lại với tài liệu gốc hay không
"""
import html
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

VERDICTS = {
    "correct": ("dat", "Đạt"),
    "unclear": ("lung-chung", "Chưa rõ"),
    "incorrect": ("sai", "Sai"),
}


def _to_int(value, default: int = 0) -> int:
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return default


def _verdict(item: Dict, threshold: int) -> Tuple[str, str]:
    """Xếp loại một câu, ưu tiên nhãn sẵn có rồi mới suy từ điểm."""
    label = str(item.get("evaluate") or "").strip().lower()
    if label in VERDICTS:
        return VERDICTS[label]

    score = _to_int(item.get("score"), -1)
    if score < 0:
        return ("lung-chung", "Chưa rõ")
    if score >= threshold:
        return VERDICTS["correct"]
    if score == threshold - 1:
        return VERDICTS["unclear"]
    return VERDICTS["incorrect"]


def _expected_answer(item: Dict) -> str:
    """Đáp án mong đợi.

    Ở chế độ join, đáp án nằm trong `check`. Chỉ dùng `check` khi file được chấm
    bởi bản mới — nhận biết qua sự có mặt của `reason`; ở bản cũ `check` bị ghi đè
    bằng lý do chấm điểm nên không dùng được.
    """
    expected = item.get("gold") or item.get("expected")
    if not expected and "reason" in item:
        expected = item.get("check")
    return str(expected or "").strip()


def summarize(data: List[Dict], threshold: int) -> Dict:
    counts = {"dat": 0, "lung-chung": 0, "sai": 0}
    scores = []
    for item in data:
        css, _ = _verdict(item, threshold)
        counts[css] += 1
        score = _to_int(item.get("score"), -1)
        if score >= 0:
            scores.append(score)

    total = len(data) or 1
    return {
        "total": len(data),
        "counts": counts,
        "pass_rate": round(counts["dat"] * 100 / total),
        "avg_score": round(sum(scores) / len(scores), 1) if scores else 0,
    }


def _row(index: int, item: Dict, threshold: int) -> str:
    css, label = _verdict(item, threshold)
    esc = html.escape
    score = item.get("score", "—")
    # "check" is the pre-rename field name, kept for files scored by an older version.
    reason = str(item.get("reason") or item.get("check") or "").strip() or "(không có giải thích)"
    expected = _expected_answer(item) or "(không có đáp án mẫu)"
    answer = str(item.get("answer") or "").strip() or "(chatbot không trả lời)"
    source = str(item.get("file") or "").strip()
    rechecked = str(item.get("rechecked", "")).lower() == "true"

    badges = f'<span class="badge {css}">{label}</span>'
    if rechecked:
        badges += '<span class="badge deep" title="Đã đối chiếu lại với tài liệu gốc">đối chiếu sâu</span>'

    return f"""
<details class="item" data-verdict="{css}">
  <summary>
    <span class="num">#{index}</span>
    <span class="q">{esc(str(item.get("question", "")).strip())}</span>
    {badges}
    <span class="score {css}">{esc(str(score))}/10</span>
  </summary>
  <div class="body">
    <div class="why"><h4>Vì sao chấm điểm này</h4><p>{esc(reason)}</p></div>
    <div class="cols">
      <div><h4>Đáp án mong đợi</h4><p>{esc(expected)}</p></div>
      <div><h4>Chatbot trả lời</h4><p>{esc(answer)}</p></div>
    </div>
    {f'<p class="src">Nguồn: {esc(source)}</p>' if source else ""}
  </div>
</details>"""


CSS = """
*{box-sizing:border-box}
body{margin:0;padding:2rem 1rem;font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
     background:#f6f7f9;color:#1a1d21}
.wrap{max-width:920px;margin:0 auto}
h1{margin:0 0 .25rem;font-size:1.5rem}
.meta{color:#61676e;margin:0 0 1.5rem;font-size:.9rem}
.card{background:#fff;border:1px solid #e3e6ea;border-radius:12px;padding:1.25rem;margin-bottom:1.5rem}
.bigrate{font-size:2.5rem;font-weight:700;line-height:1}
.bar{height:10px;border-radius:5px;background:#eceef1;overflow:hidden;display:flex;margin:.75rem 0}
.bar i{display:block;height:100%}
.bar .dat{background:#1a9e5c}.bar .lung-chung{background:#d99a06}.bar .sai{background:#d4483b}
.tallies{display:flex;gap:1.5rem;flex-wrap:wrap;color:#41464c;font-size:.92rem}
.dot{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:.4rem}
.dot.dat{background:#1a9e5c}.dot.lung-chung{background:#d99a06}.dot.sai{background:#d4483b}
.filters{display:flex;gap:.5rem;flex-wrap:wrap;margin-bottom:1rem}
.filters button{font:inherit;font-size:.9rem;padding:.4rem .9rem;border-radius:999px;cursor:pointer;
     border:1px solid #d5d9de;background:#fff;color:#41464c}
.filters button[aria-pressed="true"]{background:#1a1d21;border-color:#1a1d21;color:#fff}
.item{background:#fff;border:1px solid #e3e6ea;border-radius:10px;margin-bottom:.6rem}
.item[hidden]{display:none}
summary{display:flex;gap:.7rem;align-items:center;padding:.85rem 1rem;cursor:pointer;list-style:none}
summary::-webkit-details-marker{display:none}
.num{color:#8b9199;font-variant-numeric:tabular-nums;font-size:.85rem;min-width:2.2rem}
.q{flex:1;min-width:0}
.badge{font-size:.75rem;padding:.15rem .55rem;border-radius:999px;white-space:nowrap}
.badge.dat{background:#e4f4ea;color:#127443}
.badge.lung-chung{background:#fdf1d8;color:#8a6100}
.badge.sai{background:#fbe6e4;color:#a32f24}
.badge.deep{background:#e8eefc;color:#2f4d9e}
.score{font-weight:700;font-variant-numeric:tabular-nums;white-space:nowrap}
.score.dat{color:#127443}.score.lung-chung{color:#8a6100}.score.sai{color:#a32f24}
.body{padding:0 1rem 1rem;border-top:1px solid #eef0f3}
h4{margin:1rem 0 .3rem;font-size:.8rem;text-transform:uppercase;letter-spacing:.04em;color:#7b8189}
.body p{margin:0;white-space:pre-wrap;overflow-wrap:anywhere}
.why p{background:#f6f7f9;border-left:3px solid #c7ccd2;padding:.6rem .8rem;border-radius:0 6px 6px 0}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:1.25rem}
.src{margin-top:1rem;color:#8b9199;font-size:.82rem}
.empty{text-align:center;color:#8b9199;padding:2rem}
@media(max-width:640px){.cols{grid-template-columns:1fr}}
"""

JS = """
const buttons = document.querySelectorAll(".filters button");
buttons.forEach(btn => btn.addEventListener("click", () => {
  const want = btn.dataset.filter;
  buttons.forEach(b => b.setAttribute("aria-pressed", String(b === btn)));
  let shown = 0;
  document.querySelectorAll(".item").forEach(el => {
    const match = want === "all" || el.dataset.verdict === want;
    el.hidden = !match;
    if (match) shown++;
  });
  document.querySelector(".empty").hidden = shown > 0;
}));
"""


def build_report(project, data: List[Dict], output_path: Path) -> Path:
    """Ghi báo cáo HTML và trả về đường dẫn."""
    stats = summarize(data, project.threshold)
    counts = stats["counts"]
    total = stats["total"] or 1
    generated = datetime.now().strftime("%d/%m/%Y %H:%M")

    segments = "".join(
        f'<i class="{css}" style="width:{counts[css] * 100 / total}%"></i>'
        for css in ("dat", "lung-chung", "sai")
        if counts[css]
    )
    rows = "".join(_row(i, item, project.threshold) for i, item in enumerate(data, 1))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Báo cáo {html.escape(project.name)}</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
  <h1>{html.escape(project.name)}</h1>
  <p class="meta">{stats['total']} câu hỏi · chatbot {html.escape(project.resolved_chat_model())} · {generated}</p>

  <div class="card">
    <div class="bigrate">{stats['pass_rate']}% đạt</div>
    <div class="bar">{segments}</div>
    <div class="tallies">
      <span><i class="dot dat"></i>{counts['dat']} đạt</span>
      <span><i class="dot lung-chung"></i>{counts['lung-chung']} chưa rõ</span>
      <span><i class="dot sai"></i>{counts['sai']} sai</span>
      <span>Điểm trung bình {stats['avg_score']}/10</span>
    </div>
  </div>

  <div class="filters">
    <button data-filter="all" aria-pressed="true">Tất cả ({stats['total']})</button>
    <button data-filter="sai" aria-pressed="false">Chỉ câu sai ({counts['sai']})</button>
    <button data-filter="lung-chung" aria-pressed="false">Chưa rõ ({counts['lung-chung']})</button>
    <button data-filter="dat" aria-pressed="false">Đạt ({counts['dat']})</button>
  </div>

  {rows}
  <p class="empty" hidden>Không có câu nào thuộc nhóm này.</p>
</div>
<script>{JS}</script>
</body>
</html>
""", encoding="utf-8")
    return output_path
