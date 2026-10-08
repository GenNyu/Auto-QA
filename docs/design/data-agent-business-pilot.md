# Pilot data agent: câu hỏi nghiệp vụ và report theo mẫu của team

Trạng thái: **thiết kế để review, chưa triển khai**.

PR này chỉ thêm tài liệu. Không sửa code, sinh dataset, gọi OpenWebUI,
gọi judge hoặc chạy truy vấn. Các bước bên dưới là công việc của PR triển khai sau.

## 1. Mục tiêu, hiện trạng và phụ thuộc

Người dùng chính là Head/BOD, CSM và Partnership. Technical team leader cũng dùng
agent để thống kê hoặc tra cứu mã nghiệp vụ. Câu hỏi phải giống nhu cầu công việc
của những người này. Người hỏi không cần biết bảng, cột hoặc SQL.

Report dùng cách trình bày quen thuộc của team. Người đọc thấy yêu cầu, câu trả lời
và lý do chấm trước khi mở SQL hoặc dữ liệu kỹ thuật.

**FACT tại thời điểm thiết kế (08/10/2026):**

- Workspace có mode `data_agent_auto` và pilot 50 câu đã chạy, đã freeze.
- Pipeline này chưa có trong `origin/main` khi chuẩn bị PR tài liệu.
- Report mẫu do người dùng cung cấp là HTML `Báo cáo bd_sol`. Style của mẫu khớp
  renderer RAG trong `core/report.py`. Không đưa câu hỏi hoặc câu trả lời của mẫu
  vào PR này.
- Renderer data agent hiện hiển thị nhiều card và JSON kỹ thuật. Câu hỏi sinh ra
  có thể chứa tên bảng, cột và điều kiện SQL.

**Phụ thuộc bắt buộc:** PR code phải đưa pipeline `data_agent_auto` nền cùng các
kiểm thử liên quan lên base trước khi triển khai thiết kế này. Không lấy các thay
đổi chưa commit của workspace vào PR tài liệu. Khi chuẩn bị PR code, kiểm tra lại
base và chỉ đưa các thay đổi thuộc phạm vi đã duyệt.

**Luồng mục tiêu:**

```text
KB đã index
  → gen: sinh câu hỏi theo persona
  → filter: kiểm tra nguồn, ý nghĩa và cách hỏi
  → questions.json: 10 câu chính thức
  → ask: một chat mới/câu, chỉ gửi question
  → traces.json + raw/ + answers.json
  → score: judge riêng + kiểm tra bằng mã
  → benchmark.json
  → report.html: bố cục của team, mở rộng bằng chứng khi cần
```

Đợt triển khai sau chạy đủ 10 câu để người dùng kiểm tra đề và report có kết quả
thật. Không mở rộng 50/500 câu hoặc tự freeze dataset mới trước khi người dùng review.
Giữ nguyên dataset và kết quả pilot 50 câu cũ.

## 2. Hợp đồng dataset và cách sinh/lọc câu hỏi

Giữ mode `data_agent_auto` và năm lệnh hiện có. Tạo project mới
`urdata_auto_business_10`, với `questions: 10`. Kết quả nằm trong
`runs/urdata_auto_business_10/`.

| Trường | Nội dung | Gửi vào chat benchmark? |
|---|---|---|
| `question` | Câu hỏi tự nhiên, tự đứng độc lập | Có |
| `business_check` — mới | Yêu cầu cần đáp ứng bằng tiếng Việt dễ đọc | Không |
| `persona` — mới | `head_bod`, `csm`, `partnership`, `technical_leader` | Không |
| `use_case` — mới | Mục đích sử dụng kết quả, bằng tiếng Việt | Không |
| `expectations` | Metric, grain, filter, thời gian và join có căn cứ | Không |
| `sources` | Trích dẫn KB đã được truy xuất thật | Không |
| `id`, `file`, `chunk`, `check`, `verification` | Giữ vai trò hiện có | Không |

Ba trường mô tả mới bắt buộc cho profile câu hỏi nghiệp vụ của project này.
Dataset cũ thiếu các trường mới vẫn đọc được. Giữ `check` để tương thích.
Không tạo SQL gold hoặc đáp án số liệu gold.

Thêm các trường mới vào fingerprint xác minh và fingerprint case.
Đổi câu hỏi, nguồn hoặc tiêu chí phải filter lại. Trace không tương thích không
được resume. Không dùng lại trace pilot 50 câu cho dataset mới.

### Prompt generator

- Viết nhu cầu làm báo cáo, theo dõi vận hành hoặc tra cứu thông tin.
- Không đưa tên bảng, tên cột, phép join hoặc SQL vào `question`.
- Cho phép thuật ngữ nghiệp vụ như PO, mã chiến dịch, đơn hàng và đối tác.
- Dùng thời gian tuyệt đối nhưng tự nhiên, ví dụ “tháng 9/2026”.
- Không bịa tên khách hàng, ID hoặc mã chiến dịch. Khi không có mã thật trong nguồn,
  dùng câu hỏi danh sách, tổng hợp hoặc xếp hạng.
- Không gọi ngân sách, giá trị giao dịch hoặc tiền nạp là doanh thu nếu KB không
  xác nhận định nghĩa đó.
- Không sinh câu phụ thuộc hội thoại trước hoặc cần người dùng bổ sung tham số.
- Viết `business_check` theo nội dung cần trả lời, không đưa kết quả số liệu vào đó.
- Lưu cách ánh xạ sang schema trong `expectations`, có căn cứ từ `sources`.

**Ví dụ minh họa, chưa phải câu pilot đã xác minh:**

> Tháng 9/2026 có bao nhiêu lượt đổi quà UrCard? Chia theo từng ngày để tôi đưa vào báo cáo.

Mục đích: theo dõi lượt đổi quà theo ngày. `business_check` mô tả kỳ báo cáo và
nội dung thống kê. Bảng, trường thời gian và cách đếm nằm trong `expectations`.
Chỉ giữ ví dụ thành case thật khi KB đủ căn cứ cho từng tiêu chí.

### Phân bổ và ngân sách sinh câu hỏi

| Persona | Số câu mục tiêu | Nhóm tác vụ |
|---|---:|---|
| Head/BOD | 3 | aggregate, grouping, combined |
| CSM | 3 | lookup, grouping, combined |
| Partnership | 2 | aggregate, ranking |
| Technical team leader | 2 | lookup, ranking |

Mỗi cặp persona/tác vụ ở bảng tương ứng một slot. Mục tiêu là hai câu mỗi nhóm
tác vụ, ít nhất năm tài liệu nguồn và tối đa ba câu cùng tài liệu chính.
Tài liệu chính là trường `file` của case.

Sinh tối đa 30 ứng viên cho project mới. Bộ lọc chọn câu theo các slot và phân tán
nguồn, không chỉ lấy 10 câu đầu tiên. Nếu thiếu câu phù hợp, giữ phần đã xác minh,
báo thiếu theo persona/tác vụ/nguồn và lý do. Không nới tiêu chí để đủ số lượng.
Đây là profile riêng; không thay quota hay cách chọn của các project cũ.

### Filter

1. Code phát hiện tên bảng đã biết và cú pháp SQL trong `question`.
2. Verifier riêng kiểm tra tên cột hoặc chi tiết schema lộ trong câu hỏi, mức độ
   tự nhiên, persona và mục đích công việc. Không cấm từ nghiệp vụ chỉ vì trùng
   một tên kỹ thuật. Mã có căn cứ không bị coi mặc định là cú pháp SQL.
3. Kiểm tra `business_check` khớp câu hỏi, `expectations` và nguồn.
4. Giữ kiểm tra nguồn truy xuất thật, thiếu tham số, trùng ý và định nghĩa chưa
   xác minh. Không bổ sung quy tắc từ suy đoán của verifier.
5. Lưu câu không được chọn cùng lý do. Manifest ghi rõ phân bố thực tế và phần thiếu.

## 3. Report theo mẫu của team

Tái sử dụng style hiện có của renderer RAG: nền xám nhạt, card trắng, chiều rộng
920px, nút lọc dạng pill và câu hỏi dạng `details`. Không áp dụng logic verdict RAG
cho data agent. Không sửa behavior của report các mode khác.

### Bố cục tổng quan

- Tên project, số câu, agent và thời điểm tạo theo giờ Việt Nam.
- Khối chính: tỷ lệ đạt `PASS / toàn dataset`, ghi cả số đếm và mẫu số.
- Thanh phân bố và nút lọc giữ riêng năm verdict: Đạt, Không đạt, Cần xem lại,
  Lỗi chạy và Chưa chạy. Không gộp lỗi hoặc chưa chạy vào không đạt.
- Điểm trung bình ghi rõ số case có tổng điểm xác định. Không có điểm thì dùng `—`.
- Ba chỉ số thành phần: “Truy vấn đáp ứng yêu cầu”, “Số liệu được kết quả truy vấn
  hỗ trợ”, “Trả lời đủ nội dung”. Mỗi số đếm dùng trạng thái `met` và mẫu số toàn dataset.
- Chú thích: **Trả lời đủ nội dung chưa xác nhận truy vấn và số liệu đúng.**
- Giữ thông báo: chất lượng theo KB và bằng chứng thực thi, chưa phải độ chính xác
  nghiệp vụ được DE xác nhận.

“Thông tin bộ đánh giá” mở rộng chứa toàn bộ metric bổ sung hiện có: tỷ lệ đạt trên
case đã kết luận, độ bao phủ kết luận, tỷ lệ REVIEW/ERROR/NOT_RUN, số nguồn KB,
trace completeness, số tool call, target, phân bố dataset, fingerprint và freeze.
Giải thích số nguồn là tài liệu trong case, không phải số bảng được kiểm tra.

### Bố cục từng câu

```text
#1  Câu hỏi tự nhiên                         [verdict] [điểm]
└─ Vì sao có kết quả này
   Yêu cầu cần đáp ứng  |  Agent trả lời
   Ba thành phần chấm và nguồn KB
   ▸ Bằng chứng kỹ thuật
     SQL/output liên quan, call_id, tiêu chí, claim bindings và raw trace
```

| Phần | Quy tắc |
|---|---|
| Dòng đóng | Số thứ tự, câu hỏi, verdict, điểm; score chưa xác định hiển thị `—` |
| Giải thích | Tóm tắt từ reason/component đã lưu; không gọi LLM để viết lại |
| Cột trái | `business_check`, nhãn “Yêu cầu cần đáp ứng” |
| Cột phải | Câu trả lời cuối của agent, loại tool card khỏi phần đọc chính như hiện có |
| Điểm thành phần | Trạng thái, số điểm biết được và giải thích bằng tiếng Việt |
| Nguồn | Tên tài liệu; trích dẫn đầy đủ trong phần mở rộng |
| Bằng chứng | SQL, output, call reference và bindings; giữ đúng quan hệ query/output |

Với case cũ thiếu `business_check`, diễn đạt các aspect hiện có thành danh sách yêu
cầu có nhãn tiếng Việt. Nếu không đủ dữ liệu thì ghi rõ thiếu, không tạo yêu cầu mới.
Không dùng “Đáp án mong đợi”. Không đưa raw JSON tiêu chí/binding vào phần đọc chính.

REVIEW phải nói rõ bộ chấm chưa đủ căn cứ, không mặc định agent trả lời sai.
Nếu FAIL đồng thời có phần unknown, hiển thị cả lỗi ghi nhận và phần chưa xác định.
Không dùng nội dung hoặc điểm trong report mẫu làm tiêu chí mới.

HTML là một file độc lập, không cần server, framework, thư viện mới hoặc tài nguyên
ngoài. Escape nội dung agent, KB và tool. Giữ nút lọc có số đếm, `aria-pressed` và
thông báo khi nhóm không có câu. Màn hình hẹp chuyển hai cột thành một.

Nếu giới hạn dòng output trên giao diện, ghi rõ giới hạn hiển thị. Không sửa trace
hoặc suy ra result bị truncated chỉ từ giới hạn đó. Raw reference phải giữ để tra
cứu tại workspace, không nhúng raw chats vào report chia sẻ.

## 4. Công việc triển khai và vận hành pilot

| Bước | Công việc | Hoàn thành khi |
|---|---|---|
| T0 | Đưa pipeline nền lên base của PR code | Code và test nền có trong base hoặc chuỗi PR phụ thuộc rõ ràng |
| T1 | Thêm profile nghiệp vụ, trường mô tả và fingerprints | Dataset cũ đọc được; profile mới kiểm tra đủ trường |
| T2 | Thay prompt gen/filter, chọn theo slot và nguồn | 10 câu hợp lệ hoặc báo thiếu rõ; tối đa 30 ứng viên |
| T3 | Dựng report theo style team | Đủ verdict, metric, hai cột và bằng chứng mở rộng |
| T4 | Kiểm thử offline và kiểm tra giao diện | Test đạt; report đọc được trên desktop và màn hình hẹp |
| T5 | Chạy pilot mới 10 câu | Có câu hỏi, answer, trace, benchmark và report thật |
| T6 | Giao kết quả cho người dùng review | Báo phân bố, các điểm chưa xác định; chưa freeze/mở rộng |

Sau khi triển khai code, chạy:

```bash
just gen urdata_auto_business_10
just filter urdata_auto_business_10
just ask urdata_auto_business_10
just score urdata_auto_business_10
just report urdata_auto_business_10
```

Trước ask, xác nhận dataset có đúng 10 câu đã xác minh. Nếu không đủ, giao danh sách
và báo thiếu để xử lý chất lượng nguồn; không chạy case chưa xác minh.

Giữ runner chat mới, thu raw records và resume theo fingerprint. Judge riêng dùng
provider cấu hình trong `llm`. Giữ rubric SQL 4, đối chiếu output 4, đủ nội dung 2.
Không thực thi lại SQL trong scorer, không hạ ngưỡng PASS và không nâng REVIEW thành đạt.
SQL khác cách viết được chấp nhận nếu có căn cứ tương đương về ngữ nghĩa.

**Ngoài phạm vi:** sửa toàn diện bộ trích claim, thiết kế gold dataset, xác nhận toàn
bộ nghiệp vụ bởi DE, benchmark 50/500 câu, hội thoại nhiều lượt và thêm UI framework.
REVIEW do giới hạn claim extractor vẫn phải được report thể hiện rõ.

## 5. Kiểm thử, nghiệm thu và quay lại

### Kiểm thử tự động cho PR code

- [ ] Câu tự nhiên hợp lệ được giữ; câu lộ bảng/cột hoặc chỉ dẫn SQL bị loại.
- [ ] Thuật ngữ nghiệp vụ và mã có căn cứ không bị loại nhầm.
- [ ] ID bịa, metric mơ hồ, join chưa xác minh hoặc business_check lệch tiêu chí bị loại.
- [ ] Source binding vẫn yêu cầu tài liệu gốc và nội dung truy xuất thật.
- [ ] Slots, source cap, budget 30 và báo thiếu hoạt động đúng.
- [ ] Đổi câu hỏi/tiêu chí làm mất hiệu lực xác minh và trace cũ.
- [ ] Report giữ verdict, score trống, mẫu số và component counts.
- [ ] Nút lọc giữ số đếm, trạng thái chọn và empty state.
- [ ] HTML từ agent/KB/tool không được thực thi.
- [ ] Giới hạn hiển thị không sửa hoặc gộp output giữa các call.
- [ ] Dataset/report cũ vẫn đọc được; RAG và gold scorer không đổi behavior.
- [ ] Chạy toàn bộ `python -m unittest discover -p 'test_*.py' -q`.

### Nghiệm thu pilot

- [ ] Có 10 câu qua filter; báo phân bố persona, tác vụ và nguồn thực tế.
- [ ] Người dùng không cần biết schema hoặc SQL để hiểu câu hỏi.
- [ ] Có kết quả chạy/chấm cho toàn bộ 10 câu; ERROR và REVIEW thể hiện đúng.
- [ ] Đọc được yêu cầu, câu trả lời và lý do chấm mà không mở JSON.
- [ ] Kiểm tra trực quan desktop và màn hình hẹp.
- [ ] Giữ nguyên kết quả 50 câu cũ.
- [ ] Chưa freeze hoặc chạy thêm câu trước khi người dùng review.

### Giới hạn và cách quay lại

KB thiếu định nghĩa có thể làm một số slot không có câu phù hợp. Số liệu có thể
thay đổi giữa các lần chạy. REVIEW có thể đến từ judge, không chỉ agent.
Không dùng tỷ lệ pilot làm accuracy nghiệp vụ chuẩn hoặc tự suy rộng cho mọi người dùng.

Không đưa raw chats, credentials hoặc dữ liệu thực thi vào PR tài liệu/code.
Artifact pilot nằm riêng trong `runs/`, theo quy tắc ignore hiện có.

Nếu người dùng chưa chấp nhận thiết kế hoặc pilot, giữ artifact để review và không
mở rộng. Có thể quay lại code trước PR triển khai mà vẫn giữ pilot 50 câu cũ.
PR tài liệu không thay đổi runtime nên không cần migration hoặc rollback dữ liệu.
