# Auto-QA — Hướng dẫn sử dụng

Công cụ đo **chất lượng trả lời của chatbot**. Nó tự sinh câu hỏi từ tài liệu của bạn, hỏi chatbot từng câu, chấm điểm câu trả lời, rồi xuất ra một báo cáo đọc được.

Bạn chỉ cần nhớ một lệnh: `just run <tên bộ đánh giá>`.

---

## Mục lục

1. [Cài đặt lần đầu](#1-cài-đặt-lần-đầu)
2. [Chạy đánh giá](#2-chạy-đánh-giá)
3. [Đọc báo cáo](#3-đọc-báo-cáo)
4. [Tạo bộ đánh giá mới](#4-tạo-bộ-đánh-giá-mới)
5. [Cách chấm điểm](#5-cách-chấm-điểm)
6. [Khi gặp sự cố](#6-khi-gặp-sự-cố)
7. [Bảng tra lệnh](#7-bảng-tra-lệnh)
8. [Dành cho người phát triển](#8-dành-cho-người-phát-triển)

---

## 1. Cài đặt lần đầu

Chỉ làm một lần trên mỗi máy.

### Bước 1 — cài `just`

`just` là trình chạy lệnh, giúp bạn gõ `just run iso27001` thay vì phải nhớ đường dẫn Python trong môi trường ảo.

```bash
brew install just          # macOS
```

> Không muốn cài cũng được — xem [cách chạy không cần `just`](#không-dùng-just) ở mục 7.

### Bước 2 — chạy trình cài đặt

```bash
just setup
```

Lệnh này tự lo: môi trường Python, thư viện, Playwright, trình duyệt Chromium, và tạo file `.env`.

### Bước 3 — điền thông tin đăng nhập

Mở file `.env` vừa được tạo, điền:

```env
OPENAI_API_KEY=sk-...        # key của LLM, dùng để sinh câu hỏi và chấm điểm
CHAT_EMAIL=ten@example.com   # tài khoản đăng nhập chatbot
CHAT_PASSWORD=matkhau

CHAT_URL=https://chat.urbox.dev/   # trang chat sẽ mở
CHAT_MODEL=BD Solution             # model chọn trên trang đó
```

`CHAT_MODEL` phải viết **đúng từng chữ** như hiển thị trong ô chọn model trên giao diện
(`BD Solution`, `ENGR Test1`, `Risk Assesment`…). Sai một chữ là bước hỏi chatbot dừng
ngay và in ra danh sách model đang có để bạn sửa lại.

Đây là hai thứ hay đổi nhất khi chuyển sang đánh giá một trợ lý khác, nên để ở `.env`
là đổi một chỗ, mọi bộ đánh giá dùng theo. Muốn một bộ chạy khác thì khai đè trong
`projects/<tên>.yaml` — xem mục 4.

> File `.env` không bao giờ bị đưa lên git. Đừng dán key vào bất kỳ file nào khác.

### Bước 4 — kiểm tra

```bash
just check
```

Lệnh này soát từng thứ và chỉ đúng chỗ nào còn thiếu:

```
  ✅  Python                     3.9.6
  ✅  Thư viện Python            đã cài đủ
  ✅  Node / npx                 /usr/local/bin/npx
  ✅  Playwright                 đã cài
  ✅  File .env                  .env
  ✅    CHAT_EMAIL               đã có
  ❌    CHAT_PASSWORD            chưa điền

Cần xử lý:
   • Điền CHAT_PASSWORD vào file .env
```

Khi mọi dòng đều ✅ là dùng được.

---

## 2. Chạy đánh giá

### Xem có sẵn những bộ nào

```bash
just list
```

```
  engr           ENGR Security Q&A  ·  30 câu  ·  engr_qa/
  iso27001       ISO 27001  ·  25 câu  ·  iso_test/
```

### Chạy

```bash
just run iso27001
```

Công cụ chạy tuần tự 4 bước và tự nối kết quả giữa các bước:

| Bước | Việc | Kết quả |
|------|------|---------|
| 1 | Đọc tài liệu, sinh câu hỏi | `runs/iso27001/questions.json` |
| 2 | Mở trình duyệt, hỏi chatbot từng câu | `runs/iso27001/answers.json` |
| 3 | Chấm điểm từng câu trả lời | `runs/iso27001/answers_semantic_scored.json` |
| 4 | Dựng báo cáo | `runs/iso27001/report.html` |

Xong bước 4, báo cáo tự mở trong trình duyệt.

> **Bước 2 mất nhiều thời gian nhất.** Trình duyệt sẽ hiện lên và tự thao tác — đừng đóng nó. Với 25 câu, dự kiến 15–30 phút tuỳ tốc độ chatbot.

### Chạy lại một bước

Nếu một bước lỗi, sửa xong chạy lại đúng bước đó, không phải làm lại từ đầu:

```bash
just gen    iso27001    # chỉ sinh lại câu hỏi
just ask    iso27001    # chỉ hỏi lại chatbot
just score  iso27001    # chỉ chấm lại điểm
just report iso27001    # chỉ dựng lại báo cáo
```

Ví dụ hay gặp: chatbot trả lời xong rồi nhưng bước chấm điểm bị lỗi mạng — chỉ cần chạy lại `score`, không mất công hỏi lại từ đầu.

---

## 3. Đọc báo cáo

`report.html` là một file duy nhất, mở bằng trình duyệt, gửi qua chat hay email được, không cần cài gì thêm.

Trên cùng là tỉ lệ đạt, số câu theo từng nhóm, và điểm trung bình. Bên dưới là danh sách câu hỏi; bấm vào một câu để mở ra ba phần:

- **Vì sao chấm điểm này** — giải thích của hệ thống chấm
- **Đáp án mong đợi** — đáp án lấy từ tài liệu gốc
- **Chatbot trả lời** — nguyên văn câu trả lời

Bốn nút lọc ở đầu trang: `Tất cả`, `Chỉ câu sai`, `Chưa rõ`, `Đạt`. Khi rà soát chất lượng, bấm **Chỉ câu sai** trước.

Nhãn `đối chiếu sâu` trên một câu nghĩa là câu đó đã được kiểm tra thêm một vòng với tài liệu gốc (xem [mục 5](#5-cách-chấm-điểm)).

---

## 4. Tạo bộ đánh giá mới

Cách nhanh nhất: chỉ vào thư mục tài liệu, file cấu hình được viết sẵn cho bạn.

```bash
just new input/kb/urbox
```

```
✅ Đã tạo projects/urbox.yaml
────────────────────────────────────────────────────────────
  Tài liệu   54 file · 210,883 ký tự · trung bình 3,905/file
  Câu hỏi    16 câu/file  →  khoảng 864 câu tổng cộng
  Chatbot    ENGR Test1
────────────────────────────────────────────────────────────
```

Số câu hỏi được suy từ độ dài trung bình của tài liệu — khoảng **1 câu cho mỗi 250 ký tự**,
giới hạn trong khoảng 8–30. Đặt cứng 30 câu cho mọi file là nguồn gốc của các câu hỏi trùng ý:
một tài liệu 3.500 ký tự không có đủ 30 chi tiết riêng biệt để hỏi.

Mở file vừa tạo ra chỉnh lại `chatbot.model` và số câu hỏi cho vừa ý, rồi `just run urbox`.

Đặt tên khác tên thư mục, hoặc ghi đè file đã có:

```bash
just new input/kb/urbox banhang          # → projects/banhang.yaml
just new input/kb/urbox banhang --force  # ghi đè
```

### Viết tay

Tạo một file trong thư mục `projects/`, tên file chính là tên bộ đánh giá. Ví dụ `projects/pcidss.yaml`:

```yaml
name: PCI DSS              # tên hiển thị trên báo cáo
source: pcidss/            # thư mục chứa tài liệu nguồn (.md)
questions: 30              # số câu hỏi sẽ sinh ra

chatbot:
  model: "ENGR Test1"      # tên model đúng như hiển thị trên giao diện chat
  batch_size: 10           # khởi động lại trình duyệt sau mỗi N câu

scoring:
  threshold: 6             # từ 6 điểm trở lên là ĐẠT
  deep_check: true         # đối chiếu lại tài liệu gốc khi điểm lưng chừng

llm:
  provider: anthropic      # LLM dùng để sinh câu hỏi và chấm điểm
```

Chạy: `just run pcidss`

### Các trường có thể dùng

| Trường | Bắt buộc | Mặc định | Ý nghĩa |
|--------|----------|----------|---------|
| `source` | **có** | — | Thư mục hoặc file tài liệu nguồn |
| `name` | không | tên file | Tên hiển thị trên báo cáo |
| `questions` | không | `25` | Số câu hỏi sinh ra |
| `chatbot.model` | không | theo `.env` | Tên model trên giao diện chat — đè lên `CHAT_MODEL` |
| `chatbot.url` | không | theo `.env` | Địa chỉ chatbot — đè lên `CHAT_URL` |
| `chatbot.spec` | không | `tests/KB.spec.ts` | Kịch bản điều khiển trình duyệt |
| `chatbot.batch_size` | không | `10` | Khởi động lại trình duyệt sau mỗi N câu |
| `scoring.threshold` | không | `6` | Từ mấy điểm trở lên thì tính là đạt |
| `scoring.deep_check` | không | `true` | Bật vòng đối chiếu tài liệu gốc |
| `scoring.kb_dir` | không | theo `source` | Thư mục tài liệu dùng để đối chiếu |
| `llm.provider` | không | `anthropic` | `anthropic`, `openai`, `deepseek`, `ollama` |
| `llm.model` | không | theo provider | Tên model cụ thể |

| `llm.base_url` | không | theo `.env` | Gateway của công ty (giao thức OpenAI) |

File tối giản chỉ cần đúng một dòng:

```yaml
source: tai_lieu_cua_toi/
```

### Dùng bộ câu hỏi có sẵn (bỏ qua bước sinh)

Khi đã có sẵn file câu hỏi — tự soạn tay, lọc lại từ lần chạy trước, hay nhận từ người khác —
không cần chạy bước 1. Chỉ cần đặt file đúng chỗ mà bước 1 vẫn ghi ra, rồi chạy 3 bước còn lại.

**1. File câu hỏi phải có 4 trường này**, là một mảng JSON:

```json
[
  {
    "question": "Phiếu quà tặng giấy có những mệnh giá nào?",
    "file": "20260119_BD_OPS_BD_Training_DaoTao_San_Pham_URBOX.md",
    "chunk": "Mệnh giá: Có 4 mệnh giá phiếu quà tặng giấy là 50.000đ, 100.000đ, 200.000đ, 500.000đ",
    "check": "Có 4 mệnh giá: 50.000đ, 100.000đ, 200.000đ, 500.000đ"
  }
]
```

| Trường | Bắt buộc | Ý nghĩa |
|--------|----------|---------|
| `question` | **có** | Câu hỏi sẽ gửi cho chatbot |
| `file` | **có** | Tên file tài liệu chứa câu trả lời — dùng cho vòng đối chiếu sâu |
| `chunk` | **có** | Đoạn trích nguyên văn từ tài liệu, chứa câu trả lời |
| `check` | **có** | Đáp án mong đợi. **Để trống là chấm mù** — xem cảnh báo bên dưới |

> ⚠️ `check` rỗng thì vòng 1 chấm với đáp án mẫu để trống, điểm không có ý nghĩa.
> Bộ câu hỏi do `script.py` sinh ra **không** tự điền `check` — phải bổ sung trước khi chấm.

**2. Tạo project trỏ vào thư mục tài liệu nguồn** (`projects/urbox.yaml`):

```yaml
name: UrBox BD_OPS Q&A
source: input/kb/urbox/     # thư mục chứa các file .md nêu ở trường "file"
questions: 30               # không dùng tới, vì bỏ qua bước sinh

chatbot:
  model: "ENGR Test1"
  batch_size: 10

scoring:
  threshold: 6
  deep_check: true

llm:
  provider: openai
```

Thư mục `source` vẫn bắt buộc: vòng đối chiếu sâu cần chính các file .md đó để tra lại từng ý.
Thiếu nó thì bước chấm điểm vẫn chạy nhưng bỏ qua toàn bộ phần đối chiếu nguồn.

**3. Đặt file câu hỏi vào chỗ bước 1 thường ghi ra, rồi chạy tiếp:**

```bash
mkdir -p runs/urbox
cp qa_filtered.json runs/urbox/questions.json

just ask urbox      # hỏi chatbot  → runs/urbox/answers.json
just score urbox    # chấm điểm    → runs/urbox/answers_semantic_scored.json
just report urbox   # dựng báo cáo → runs/urbox/report.html
```

Đừng chạy `just run urbox` — lệnh đó bao gồm cả bước 1 và sẽ ghi đè `questions.json` của bạn.

Bước hỏi chatbot ghi dồn sau mỗi câu, nên nếu đứt giữa chừng thì chạy lại `just ask urbox`
là chạy tiếp từ câu dở, không mất phần đã hỏi.

---

## 5. Cách chấm điểm

Mỗi câu trả lời được một LLM chấm theo thang **1–10**, đối chiếu với đáp án lấy từ tài liệu gốc:

| Điểm | Xếp loại | Nghĩa |
|------|----------|-------|
| ≥ 6 | **Đạt** | Câu trả lời dùng được |
| 5 | **Chưa rõ** | Không đủ căn cứ để kết luận |
| ≤ 4 | **Sai** | Trả lời sai hoặc lạc đề |

Ngưỡng 6 đổi được bằng `scoring.threshold`.

### Vòng đối chiếu sâu

Khi bật `deep_check: true`, những câu ở mức lưng chừng (5–7 điểm) được kiểm tra thêm một vòng nữa. Hệ thống tách ra các ý mà chatbot nói **thêm** so với đáp án mẫu, rồi tra từng ý trong tài liệu gốc:

| Kết quả tra cứu | Ảnh hưởng tới điểm |
|-----------------|--------------------|
| Tài liệu xác nhận ý đó | Nâng điểm lên 8–10 |
| Không tìm thấy trong tài liệu | Giữ sàn 7 điểm |
| Tài liệu nói ngược lại | Chặn trần 6 điểm |

Điểm ở vòng này **chỉ được tăng, không bao giờ bị giảm**. Lý do: *không tìm thấy* khác với *sai* — chatbot có thể nói đúng một ý mà tài liệu không nhắc tới, không nên phạt vì điều đó.

Câu dưới 5 điểm bỏ qua vòng này (đã sai rõ ràng), câu từ 8 điểm trở lên cũng bỏ qua (đã đủ tin cậy).

### Chỉnh tiêu chí chấm

Toàn bộ tiêu chí nằm trong `prompts_evaluate.py`, tách riêng khỏi mã nguồn:

| Prompt | Dùng ở đâu |
|--------|------------|
| `SYSTEM_PROMPT` | Vòng 1 — thang điểm 1–10 và quy tắc chấm |
| `SYSTEM_PROMPT_CLAIM_EXTRACTOR` | Tách các ý chatbot nói thêm ngoài đáp án mẫu |
| `SYSTEM_PROMPT_PASS2` | Vòng đối chiếu sâu — tra từng ý trong tài liệu gốc |

Sửa xong chạy lại `just score <tên>` là áp dụng ngay, không phải hỏi lại chatbot.

---

## 6. Khi gặp sự cố

**Luôn chạy `just check` trước.** Phần lớn sự cố là thiếu key, thiếu tài khoản, hoặc chưa cài trình duyệt — lệnh này chỉ thẳng ra.

| Hiện tượng | Nguyên nhân thường gặp | Cách xử lý |
|------------|------------------------|------------|
| `Thiếu cấu hình: CHAT_EMAIL` | Chưa điền `.env` | Mở `.env`, điền tài khoản chatbot |
| `Không tìm thấy project 'x'` | Sai tên bộ đánh giá | `just list` xem tên đúng |
| `Chưa có câu hỏi` | Chưa chạy bước 1 | `just gen <tên>` |
| `Chưa có câu trả lời` | Chưa chạy bước 2 | `just ask <tên>` |
| `API key required` | Thiếu key của provider đang dùng | Điền `<PROVIDER>_API_KEY` vào `.env` |
| Bước 2 dừng giữa chừng | Chatbot chậm hoặc mất mạng | Chạy lại `just ask <tên>` |
| Đăng nhập chatbot thất bại | Sai mật khẩu, hoặc model không tồn tại | Kiểm tra `.env` và `chatbot.model` trong file YAML |
| Sinh được ít câu hơn yêu cầu | Tài liệu ngắn hoặc khó tách ý | Giảm `questions`, hoặc bổ sung tài liệu |

Tên model trong `chatbot.model` phải khớp với chuỗi hiển thị trên giao diện chat. Sai tên thì công cụ vẫn chạy nhưng hỏi nhầm model.

---

## 7. Bảng tra lệnh

Gõ `just` không kèm gì để xem toàn bộ danh sách.

```bash
just setup             # cài đặt, chạy một lần
just check             # kiểm tra máy đã sẵn sàng chưa
just list              # liệt kê các bộ đánh giá
just new <thư mục>     # tạo bộ đánh giá mới từ thư mục tài liệu

just run    <tên>      # chạy trọn 4 bước rồi mở báo cáo
just gen    <tên>      # chỉ sinh câu hỏi
just ask    <tên>      # chỉ hỏi chatbot
just score  <tên>      # chỉ chấm điểm
just report <tên>      # chỉ dựng lại báo cáo

just open   <tên>      # mở lại báo cáo đã có, không chạy gì
just clean  <tên>      # xoá kết quả của một bộ để chạy lại từ đầu
just tidy              # dọn file tạm
just shell             # mở shell đã bật sẵn venv (gõ 'exit' để thoát)
```

Kết quả của mỗi bộ nằm trong `runs/<tên>/`. Xoá thư mục đó là chạy lại từ đầu.

### Không dùng `just`

Mọi lệnh đều gọi thẳng được. Lưu ý phải dùng Python **trong môi trường ảo**, vì Python hệ thống không có sẵn thư viện cần thiết:

```bash
./setup.sh                              # thay cho: just setup
.venv/bin/python qa.py check            # thay cho: just check
.venv/bin/python qa.py run iso27001     # thay cho: just run iso27001
```

Hoặc activate môi trường ảo một lần rồi gõ ngắn trong suốt phiên làm việc:

```bash
source .venv/bin/activate
python qa.py run iso27001
```

`just shell` làm đúng việc đó — mở một shell mới đã bật sẵn venv, gõ `exit` để thoát:

```bash
just shell
python script.py --input input/kb/engr/ --num-questions 15
exit
```

> `just setup` (hay bất kỳ lệnh `just` nào) không thể tự activate venv cho terminal của bạn —
> nó chạy trong tiến trình con, thoát ra là mất. Nhưng các lệnh `just` đều gọi thẳng
> `.venv/bin/python` nên vốn đã chạy đúng môi trường; chỉ khi gõ `python` thủ công mới cần
> `just shell` hoặc `source .venv/bin/activate`.

---

## 8. Dành cho người phát triển

### Cấu trúc

```
qa.py                 Điểm vào duy nhất
setup.sh              Cài đặt một bước
projects/*.yaml       Cấu hình từng bộ đánh giá
core/
  project.py          Đọc file cấu hình
  env.py              Đọc .env, phân giải API key
  text.py             Chuẩn hoá chuỗi
  report.py           Dựng báo cáo HTML
script.py             Bước 1 — sinh câu hỏi từ tài liệu
script_json.py        Bước 1 — biến thể cho PCI DSS
tests/KB.spec.ts      Bước 2 — điều khiển chatbot (Playwright)
tests/QA.spec.ts      Bước 2 — biến thể cho PCI DSS
tests/env.ts          Đọc .env phía TypeScript
evaluate.py           Bước 3 — chấm điểm
prompts.py            Prompt cho bước sinh câu hỏi
prompts_evaluate.py   Prompt cho bước chấm điểm — sửa tiêu chí chấm ở đây
providers/            Lớp trừu tượng LLM (DeepSeek / OpenAI / Anthropic / Ollama)
tools/                Script chuẩn bị dữ liệu, chạy tay khi cần
runs/<tên>/           Kết quả mỗi lần chạy (đã gitignore)
```

### Gọi trực tiếp từng công cụ

`qa.py` chỉ là lớp bọc. Ba công cụ bên dưới vẫn dùng độc lập được với đầy đủ tham số:

```bash
.venv/bin/python script.py   --help
.venv/bin/python evaluate.py --help
npx playwright test tests/KB.spec.ts
```

Kịch bản Playwright nhận cấu hình qua biến môi trường: `QA_INPUT`, `QA_OUTPUT`, `CHAT_MODEL`, `CHAT_URL`, `QA_MAX_PER_SESSION`.

### Join mode

`evaluate.py` ghép được file câu trả lời với file yêu cầu tuân thủ theo `id` — dùng cho bộ PCI DSS:

```bash
.venv/bin/python evaluate.py \
  --qa-file  outputs/PCI_DSS_qa_output.json \
  --pci-file outputs/PCI_DSS_filtered.json
```

Đổi tên trường bằng `--id-field`, `--context-field`, `--main-field`, `--expected-field`.

### Schema file kết quả

| Trường | Nguồn | Ý nghĩa |
|--------|-------|---------|
| `question` | bước 1 | Câu hỏi |
| `gold` / `check` | bước 1 | Đáp án mong đợi (`check` dùng ở join mode) |
| `answer` | bước 2 | Câu trả lời của chatbot |
| `score` | bước 3 | Điểm 1–10 |
| `evaluate` | bước 3 | `correct` / `unclear` / `incorrect` / `error` |
| `reason` | bước 3 | Giải thích vì sao chấm điểm đó |
| `rechecked` | bước 3 | Có chạy vòng đối chiếu sâu hay không |
| `pass1_score`, `pass1_reason` | bước 3 | Kết quả vòng 1 |
| `pass2_score`, `pass2_reason`, `extra_claims` | bước 3 | Kết quả vòng đối chiếu sâu |
| `pass1_needs_source_check` | bước 3 | Vòng 1 thấy chi tiết không xác minh được từ chunk → buộc chạy vòng 2 |
| `version_conflict` | bước 3 | Các file nguồn mâu thuẫn nhau vì trùng tên khác version — lỗi nằm ở KB, không phải ở câu trả lời |

> Các file chấm bằng bản cũ dùng `check` / `pass1_check` / `pass2_check` cho phần giải thích. Công cụ vẫn đọc được cả hai định dạng.

### KB có nhiều version trùng tên

KB chứa nhiều file cùng tên tài liệu nhưng khác version/ngày (`..._ver_8.md` vs `..._Ver7.md`,
`20260206_...` vs `20260128_...`), và các version này nói khác nhau về cùng một con số.

Vòng 1 chỉ thấy một chunk, nên câu trả lời trích từ version khác trông như bịa. Vì vậy:

- vòng 2 nạp **tất cả** version của mỗi file trong `source`, không chỉ file được retrieve;
- vòng 2 chạy cả khi vòng 1 chấm thấp — chỉ bỏ qua khi nhãn là `CONTRADICTED`;
- thông tin tìm thấy ở **bất kỳ** version nào đều tính là SUPPORTED;
- câu trả lời nêu nhiều giá trị **có ghi rõ nguồn** được chấm 9–10; chỉ gộp lẫn không phân biệt mới bị 6–7.

Khi `version_conflict: true`, việc cần làm là dọn file trùng trong KB chứ không phải sửa chatbot.

### Cấu hình bí mật

API key và tài khoản chatbot **chỉ** đọc từ `.env` hoặc tham số dòng lệnh, không bao giờ nằm trong mã nguồn. Xem `.env.example`.

Thứ tự ưu tiên: tham số CLI → biến môi trường → file `.env`.

### Công cụ đưa tài liệu lên KB

```bash
npm run kb:setup -- --url https://kb.urbox.vn    # đăng nhập một lần, lưu phiên
npm run kb:add-iso -- --dry-run --limit 3        # chạy thử
npm run kb:add-iso                               # đẩy toàn bộ iso_test/ lên KB
```
