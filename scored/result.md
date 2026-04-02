### BẢNG ĐÁNH GIÁ CHI TIẾT (Q001 - Q150)

| ID | Nhãn | Điểm | Lý do đánh giá (Tiếng Việt) |
| :--- | :--- | :--- | :--- |
| **Q001** | CONTRADICTED | 3 | **Anchor Mismatch:** Gold yêu cầu 6.5.2, 11.3.1.3, 11.4.5. Candidate dẫn 11.4.6 (sai ID) và 6.3 (không khớp Gold). |
| **Q002** | CONTRADICTED | 2 | **Hallucination:** Candidate gán mã 12.5.3 cho quy trình nhân sự nghỉ việc, thực tế mã 12.5.3 trong Gold là về Scope. |
| **Q003** | ENTAILED | 8 | Khớp Fact cốt lõi nhưng đưa thêm con số "3 ngày, 7 ngày" không có trong Gold/PDF tiêu chuẩn. |
| **Q004** | ENTAILED | 9 | Khớp hoàn toàn Fact và Requirement ID. Trừ 1 điểm vì bổ sung quy trình SMS OTP ngoài Gold. |
| **Q005** | CONTRADICTED | 3 | **Anchor Drift:** Gold yêu cầu 3.7.3, 3.7.6, 7.2.1. Candidate thiếu mã 7.2.1 về phân tách nhiệm vụ. |
| **Q006** | ENTAILED | 10 | Khớp hoàn hảo Fact và các mã Requirement (10.4.1.1, 10.7.2, 11.5.1). |
| **Q007** | ENTAILED | 9 | Khớp nội dung và mã yêu cầu. Bổ sung chi tiết rà soát hàng quý (vượt quá Gold). |
| **Q008** | ENTAILED | 9 | Khớp Fact (Môi trường tách biệt - 6.5.3). Giải trình tốt các bước của SDLC. |
| **Q009** | ENTAILED | 8 | Khớp Requirement ID (1.5.1, 2.2.1, 5.2.1, 8.4.2). Bổ sung thêm nhiều mã 5.x không có trong Gold. |
| **Q010** | ENTAILED | 10 | Khớp Fact về chính sách AUP (12.2.1) và đào tạo phishing (12.6.3.1). |
| **Q011** | ENTAILED | 10 | Khớp hoàn toàn quy trình phản ứng sự cố cho thiết bị POI (9.5.1.x). |
| **Q012** | ENTAILED | 9 | Khớp Fact về quét WAP định kỳ hàng quý (11.2.1). |
| **Q013** | CONTRADICTED | 3 | **Anchor Mismatch:** Candidate gán mã 1.5.1 cho tài khoản hệ thống (Gold yêu cầu 7.2.5, 8.6.2, 8.6.3). |
| **Q014** | ENTAILED | 9 | Khớp Fact về FIM (10.3.4) và bảo vệ log. |
| **Q015** | NOT_SUPPORTED | 1 | **Retrieval Failure:** Candidate báo không đủ dữ liệu mặc dù Gold có đáp án rõ (12.3.1). |
| **Q016** | ENTAILED | 10 | Khớp Fact về Masking PAN (3.4.1) và ngăn sao chép (3.4.2). |
| **Q017** | ENTAILED | 10 | Khớp Fact về ma trận trách nhiệm (12.8.5) và kiến trúc mật mã (3.6.1.1). |
| **Q018** | ENTAILED | 8 | Khớp Fact thay đổi mật khẩu mặc định (2.2.2) nhưng thiếu mã xác nhận lại (12.4.2). |
| **Q019** | ENTAILED | 10 | Khớp Fact về quản lý script (6.4.3) và phát hiện thay đổi (11.6.1). |
| **Q020** | CONTRADICTED | 4 | **Anchor Drift:** Candidate dẫn mã 12.11.x (không có trong PCI v4.0.1 gốc hoặc Gold). Gold yêu cầu 6.2.2, 6.3.1. |
| **Q021** | ENTAILED | 9 | Khớp Fact cấm lưu trữ SAD (3.3.1). Bổ sung thêm quy trình xử lý sự cố. |
| **Q022** | ENTAILED | 10 | Khớp Fact kiểm tra lý lịch (12.7.1) và đào tạo định kỳ (12.6.1). |
| **Q023** | ENTAILED | 9 | Khớp Fact về ranh giới NSC (1.4.1) và từ chối mặc định. |
| **Q024** | ENTAILED | 10 | Khớp hoàn toàn Fact về NTP (10.6.1) và tính nhất quán log (10.2.2). |
| **Q025** | CONTRADICTED | 3 | **Anchor Mismatch:** Candidate gán mã 1.5.x cho laptop (Gold yêu cầu 1.5.1, 2.2.1, 5.2.1). |
| **Q026** | NOT_SUPPORTED | 1 | **Retrieval Failure:** Không tìm thấy quy trình tiêu hủy dữ liệu máy chủ cũ (9.4.6). |
| **Q027** | ENTAILED | 10 | Khớp hoàn toàn quy trình quản lý TPSP (12.8.x). |
| **Q028** | ENTAILED | 8 | Khớp Fact đào tạo (12.6.x) nhưng không nhấn mạnh việc rà soát 3 tháng/lần (12.4.2) như Gold. |
| **Q029** | ENTAILED | 10 | Khớp Fact loại bỏ dịch vụ không cần thiết (2.2.4) và chặn cổng (1.2.5). |
| **Q030** | ENTAILED | 10 | Khớp Fact xử lý PAN lạc chỗ (12.10.7) và xóa an toàn (3.2.1). |
| **Q031** | ENTAILED | 10 | Khớp hoàn hảo Fact mã hóa truyền tin (4.2.1) và chứng chỉ (4.2.1.1). |
| **Q032** | CONTRADICTED | 3 | **Anchor Mismatch:** Candidate tự gán các mã 9.5.x cho backup (Gold yêu cầu 9.4.1.1, 9.4.5). |
| **Q033** | ENTAILED | 9 | Khớp Fact về IDS/IPS (11.5.1) và phản hồi sự cố. |
| **Q034** | CONTRADICTED | 3 | **Anchor Drift:** Candidate dẫn Requirement 1 trong khi Gold yêu cầu rà soát 6 tháng (7.2.4). |
| **Q035** | ENTAILED | 8 | Khớp Fact đào tạo (12.6.1) nhưng thiếu mã 12.6.2 về cập nhật nội dung. |
| **Q036** | ENTAILED | 9 | Khớp Fact cấm gửi PAN qua email (4.2.2). |
| **Q037** | ENTAILED | 10 | Khớp Fact về Cryptoperiod (3.7.4) và Rotation (3.7.5). |
| **Q038** | ENTAILED | 10 | Khớp Fact diễn tập sự cố hàng năm (12.10.2). |
| **Q039** | ENTAILED | 10 | Khớp Fact giám sát 24/7 (9.2.1) và vô hiệu hóa cổng mạng (9.2.3). |
| **Q040** | ENTAILED | 10 | Khớp Fact tiếp nhận báo cáo lỗ hổng bên ngoài (6.3.1) và vá lỗi (6.3.3). |
| **Q041** | CONTRADICTED | 3 | **Anchor Mismatch:** Candidate dẫn mã 12.3.x, 12.5.x sai chức năng (Gold yêu cầu 2.2.7, 8.4.2). |
| **Q042** | ENTAILED | 9 | Khớp Fact render unreadable (3.5.1). |
| **Q043** | ENTAILED | 8 | Khớp Fact quản lý script (6.4.3) nhưng thiếu mã đánh giá trước triển khai (6.2.1). |
| **Q044** | ENTAILED | 9 | Khớp Fact cảnh báo dung lượng (10.4.1.1) và lưu trữ tập trung (10.5.1). |
| **Q045** | CONTRADICTED | 3 | **Anchor Drift:** Candidate dẫn Requirement 7 & 10 chung chung, thiếu mã rà soát cấu hình (1.2.7) của Gold. |
| **Q046** | ENTAILED | 9 | Khớp Fact lọc gói anti-spoofing (1.4.3). |
| **Q047** | NOT_SUPPORTED | 1 | **Retrieval Failure:** Không tìm thấy thông tin xử lý hệ thống cũ (Legacy). |
| **Q048** | ENTAILED | 9 | Khớp Fact kỹ thuật viên là khách thăm (9.3.2) và giám sát (10.2.1.1). |
| **Q049** | ENTAILED | 10 | Khớp Fact về lập trình an toàn (6.2.4) và WAF (6.4.1). |
| **Q050** | ENTAILED | 9 | Khớp Fact khóa tài khoản (8.3.4). |
| **Q051** | ENTAILED | 9 | Khớp Fact so sánh cấu hình chuẩn (1.2.7) và SSH (2.2.7). |
| **Q052** | ENTAILED | 10 | Khớp Fact cấm dịch vụ đám mây không phê duyệt (12.2.1). |
| **Q053** | ENTAILED | 10 | Khớp Fact cảnh báo Rogue AP (11.2.1) và phản ứng sự cố (12.10.1). |
| **Q054** | ENTAILED | 8 | Khớp Fact thử nghiệm môi trường tách biệt (6.5.3) nhưng dẫn sai mã 6.5.x phụ. |
| **Q055** | ENTAILED | 10 | Khớp Fact ngăn nhân viên tự cài phần mềm (2.2.1) và Anti-malware (5.2.1). |
| **Q056** | ENTAILED | 10 | Khớp Fact Masking số thẻ (3.4.1) và tiêu hủy báo cáo giấy (9.4.6). |
| **Q057** | ENTAILED | 10 | Khớp Fact giám sát tài khoản đặc quyền (10.2.1.2) và nỗ lực thất bại (10.2.1.4). |
| **Q058** | ENTAILED | 9 | Khớp Fact quyền truy cập bên thứ ba (7.2.2) và MFA (8.4.2). |
| **Q059** | ENTAILED | 10 | Khớp Fact tiêu chuẩn Hardening (2.2.1) và rà soát định kỳ (12.4.2). |
| **Q060** | ENTAILED | 10 | Khớp Fact quét mã độc USB (5.3.3) và cấm thiết bị ngoài (12.2.1). |
| **Q061** | ENTAILED | 10 | Khớp Fact danh mục thuật toán (3.6.1) và rà soát kiến trúc (12.3.3). |
| **Q062** | ENTAILED | 10 | Khớp Fact đào tạo trước khi cấp quyền (12.6.1) và ký cam kết (12.1.3). |
| **Q063** | ENTAILED | 9 | Khớp Fact tách vùng IoT (1.2.1) và Hardening (2.2.2). |
| **Q064** | ENTAILED | 10 | Khớp Fact phân tích rủi ro lỗ hổng trung bình/thấp (11.3.1.1, 12.3.1). |
| **Q065** | ENTAILED | 10 | Khớp Fact loại bỏ SAD khỏi ghi âm (3.3.1) và tiêu hủy (9.4.6). |
| **Q066** | ENTAILED | 10 | Khớp Fact Disaster Recovery (12.10.1) và diễn tập (12.10.2). |
| **Q067** | ENTAILED | 10 | Khớp Fact thẻ từ (9.2.1) và chính sách bàn làm việc sạch (12.2.1). |
| **Q068** | CONTRADICTED | 3 | **Anchor Drift:** Candidate dẫn Requirement 4 và 11 sai mục tiêu. Gold yêu cầu phê duyệt thay đổi (6.5.1). |
| **Q069** | ENTAILED | 9 | Khớp Fact sử dụng MDM (2.2.1) và cấm lưu trữ PAN trên thiết bị (12.2.1). |
| **Q070** | ENTAILED | 9 | Khớp Fact dịch vụ chống DDoS và giám sát (10.4.1). |
| **Q071** | ENTAILED | 10 | Khớp Fact thẩm định TPSP (12.8.3) và cam kết hợp đồng (12.8.2). |
| **Q072** | ENTAILED | 9 | Khớp Fact Peer review (6.2.3) và SAST (6.2.4). |
| **Q073** | ENTAILED | 10 | Khớp Fact chặn email lừa đảo (5.4.1) và MFA (8.4.2). |
| **Q074** | ENTAILED | 9 | Khớp Fact thu hồi quyền (8.2.6) và đổi khóa re-key (3.7.5). |
| **Q075** | ENTAILED | 10 | Khớp Fact danh mục thư viện (6.3.2) và công cụ SCA (6.3.1). |
| **Q076** | NOT_SUPPORTED | 1 | **Retrieval Failure:** Báo thiếu dữ liệu về Call Center trong khi Gold có (3.3.1, 12.6.1). |
| **Q077** | NOT_SUPPORTED | 1 | **Retrieval Failure:** Không tìm thấy thông tin phát hiện Skimmers cổng mạng. |
| **Q078** | ENTAILED | 9 | Khớp Fact quản lý tập trung (12.1.1) và đánh giá chi nhánh (12.4.2). |
| **Q079** | ENTAILED | 10 | Khớp Fact Tokenization trong phân tích (3.5.1) và RBAC (7.2.2). |
| **Q080** | ENTAILED | 10 | Khớp Fact xác thực người yêu cầu (12.2.1) và đào tạo kỹ xã hội (12.6.1). |
| **Q081** | ENTAILED | 10 | Khớp hoàn hảo Fact xử lý ASV failed và rescan (11.3.2). |
| **Q082** | ENTAILED | 10 | Khớp Fact bảo vệ dữ liệu migration (6.5.1) và truyền tin an toàn (4.2.1). |
| **Q083** | ENTAILED | 9 | Khớp Fact đào tạo tái sử dụng mật khẩu (12.6.1) và MFA (8.4.2). |
| **Q084** | NOT_SUPPORTED | 1 | **Retrieval Failure:** Thất bại truy xuất về cập nhật Firmware thiết bị mạng. |
| **Q085** | ENTAILED | 10 | Khớp Fact đối chiếu quyền hạn (7.2.4) và đặc quyền tối thiểu (7.2.2). |
| **Q086** | ENTAILED | 9 | Khớp Fact cấm thiết bị ghi hình (12.2.1) và camera giám sát. |
| **Q087** | ENTAILED | 9 | Khớp Fact outsourced IT phải thẩm định (12.8.3) và tuân thủ chính sách (12.8.2). |
| **Q088** | ENTAILED | 9 | Khớp Fact giám sát tính toàn vẹn (11.6.1) và khôi phục sạch (12.10.1). |
| **Q089** | ENTAILED | 9 | Khớp Fact ngăn dừng phần mềm bảo mật (2.2.1) và ghi nhật ký nỗ lực (10.2.1.7). |
| **Q090** | ENTAILED | 10 | Khớp Fact ứng dụng mobile đã chứng nhận (6.2.1) và mã hóa (3.5.1, 4.2.1). |
| **Q091** | ENTAILED | 10 | Khớp Fact giám sát lối thoát hiểm bằng cảm biến/camera (9.2.1.1). |
| **Q092** | ENTAILED | 9 | Khớp Fact vô hiệu hóa dump bộ nhớ (2.2.1) và xóa an toàn (3.7.3). |
| **Q093** | ENTAILED | 10 | Khớp Fact thẩm định dịch vụ phân tích (12.8.3) và cấm thu thập SAD (3.3.1). |
| **Q094** | ENTAILED | 10 | Khớp Fact xác thực hỗ trợ kỹ thuật (12.2.1) và danh sách liên hệ chính thức. |
| **Q095** | ENTAILED | 10 | Khớp Fact thông báo lỗi chung (6.2.4) và nhật ký nội bộ (10.2.1). |
| **Q096** | ENTAILED | 10 | Khớp Fact cấm mang media chứa PAN ra ngoài (9.4.1). |
| **Q097** | ENTAILED | 9 | Khớp Fact cấu hình Redis/Memcached an toàn (1.2.1, 2.2.1). |
| **Q098** | NOT_SUPPORTED | 1 | **Retrieval Failure:** Không tìm thấy thông tin phát hiện Port scanning nội bộ. |
| **Q099** | ENTAILED | 10 | Khớp Fact tách biệt quyền DBA và khóa giải mã (3.7.6, 3.5.1). |
| **Q100** | ENTAILED | 9 | Khớp Fact thẩm định nhà cung cấp dự phòng (12.8.3) và ma trận trách nhiệm. |
| **Q101** | ENTAILED | 9 | Khớp Fact rà soát Firewall 6 tháng/lần (1.2.7) và Pen-test phân vùng (11.4.5). |
| **Q102** | ENTAILED | 8 | Khớp Fact cấm lưu credential trên BYOD (12.2.1) nhưng thiếu mã 8.3.2 về truyền tin. |
| **Q103** | ENTAILED | 10 | Khớp Fact dùng WAF chặn zero-day (6.4.1) và tin tình báo rủi ro (6.3.1). |
| **Q104** | ENTAILED | 10 | Khớp Fact cập nhật kiến trúc mật mã (3.6.1.1) và quy trình quản lý khóa (3.7.1). |
| **Q105** | ENTAILED | 10 | Khớp Fact phê duyệt script (6.4.3) và giám sát thay đổi hàng tuần (11.6.1). |
| **Q106** | ENTAILED | 10 | Khớp Fact kỹ thuật chặn chụp màn hình (3.4.2) và đào tạo cấm sao chép tại nhà. |
| **Q107** | ENTAILED | 9 | Khớp Fact tách biệt vai trò quản trị log (7.2.2) và giới hạn truy cập (10.3.1). |
| **Q108** | ENTAILED | 10 | Khớp Fact thu hồi khóa DEK khẩn cấp (3.7.5) và phân tích log truy cập. |
| **Q109** | CONTRADICTED | 2 | **Anchor Mismatch:** Gold yêu cầu quét có xác thực (11.3.1.2), Candidate dẫn mã 8.5.x không liên quan. |
| **Q110** | ENTAILED | 10 | Khớp Fact Pen-test giả lập tấn công từ POI vào mạng nội bộ (11.4.5, 11.4.1). |
| **Q111** | ENTAILED | 10 | Khớp Fact mã hóa backup (3.5.1) và thẩm định kho lưu trữ bên thứ ba (12.8.3). |
| **Q112** | ENTAILED | 8 | Khớp Fact thay đổi khẩn cấp vẫn phải phê duyệt (6.5.1) nhưng thiếu mã rà soát 12.4.2. |
| **Q113** | ENTAILED | 10 | Khớp Fact chính sách bảo mật thông tin (12.2.1) và giám sát rò rỉ (6.3.1). |
| **Q114** | ENTAILED | 7 | Khớp Fact Hardening container (2.2.1) nhưng Candidate thừa nhận quy trình chưa hoàn chỉnh. |
| **Q115** | NOT_SUPPORTED | 1 | **Retrieval Failure:** Thất bại trong việc chứng minh xử lý cảnh báo Anti-malware. |
| **Q116** | ENTAILED | 10 | Khớp Fact chặn hiển thị PAN khi share màn hình (3.4.1) và dùng MFA (8.4.2). |
| **Q117** | ENTAILED | 9 | Khớp Fact phân tích rủi ro động (8.3.9) và bắt buộc MFA (8.4.2). |
| **Q118** | ENTAILED | 10 | Khớp Fact giới hạn quyền thay đổi thời gian (10.6.3) và log cảnh báo (10.2.1.6). |
| **Q119** | ENTAILED | 10 | Khớp Fact rà soát lại Scope sau sáp nhập (12.5.3) và cập nhật sơ đồ (12.5.2). |
| **Q120** | NOT_SUPPORTED | 1 | **Retrieval Failure:** Không tìm thấy biện pháp chống Ransomware tống tiền. |
| **Q121** | ENTAILED | 10 | Khớp Fact đối chiếu lý do kinh doanh (1.2.7) và ghi nhật ký thay đổi (10.2.1.1). |
| **Q122** | ENTAILED | 10 | Khớp Fact dùng DLP ngăn nhập PAN vào CRM (12.3.1) và quét PAN lạc chỗ. |
| **Q123** | ENTAILED | 9 | Khớp Fact bảo mật API (6.4.1) và xác thực mạnh (8.2.1). |
| **Q124** | NOT_SUPPORTED | 1 | **Retrieval Failure:** Không tìm thấy quy trình Load testing dữ liệu thẻ. |
| **Q125** | ENTAILED | 8 | Khớp Fact cấm lưu mật khẩu không an toàn (12.2.1) nhưng thiếu mã rà soát 12.4.2. |
| **Q126** | ENTAILED | 10 | Khớp Fact đăng ký nhận Security advisories (12.3.4) và đánh giá rủi ro (6.3.1). |
| **Q127** | ENTAILED | 10 | Khớp Fact tách vùng Guest Wi-Fi bằng Firewall (1.2.1, 1.3.1). |
| **Q128** | ENTAILED | 10 | Khớp Fact thông báo cho Brand và khách hàng khi có vi phạm (12.10.1). |
| **Q129** | ENTAILED | 10 | Khớp Fact tiêu hủy vật lý media (9.4.6) và ghi nhật ký (10.2.1.1). |
| **Q130** | ENTAILED | 10 | Khớp Fact kiểm tra Misconfigurations qua Hardening (2.2.1) và Pen-test (11.4.1). |
| **Q131** | ENTAILED | 9 | Khớp Fact tài liệu hóa quy trình bàn giao (1.1.1, 1.1.2) và rà soát (12.4.2). |
| **Q132** | ENTAILED | 9 | Khớp Fact đào tạo Vishing (12.6.3.1) và xác thực danh tính người gọi (8.3.3). |
| **Q133** | ENTAILED | 10 | Khớp Fact cơ chế OTP một lần chống Replay attack (8.5.1). |
| **Q134** | ENTAILED | 10 | Khớp Fact AOC liệt kê đầy đủ cơ sở hạ tầng đã kiểm tra (12.5.2, 12.8.5). |
| **Q135** | ENTAILED | 10 | Khớp Fact truyền log Colocation về trung tâm (10.5.1) và xem xét hàng ngày. |
| **Q136** | ENTAILED | 10 | Khớp Fact cấu hình họp trực tuyến chặn share cửa sổ nhạy cảm (3.4.1, 12.6.1). |
| **Q137** | ENTAILED | 10 | Khớp Fact dùng HSM/KMS cô lập khóa khỏi các VM khác (3.7.3, 2.2.3.1). |
| **Q138** | ENTAILED | 10 | Khớp Fact cấu hình thiết bị mạng không chặn dải IP của ASV (11.3.2). |
| **Q139** | ENTAILED | 10 | Khớp Fact khóa chỉ dùng cho một mục đích duy nhất (3.7.2) và giám sát (10.2.1.1). |
| **Q140** | NOT_SUPPORTED | 1 | **Retrieval Failure:** Thất bại trong việc chứng minh quy trình Forensic điều tra. |
| **Q141** | ENTAILED | 10 | Khớp Fact chặn dịch vụ dịch thuật công cộng bằng lọc web (1.2.5, 12.2.1). |
| **Q142** | ENTAILED | 9 | Khớp Fact trách nhiệm giám sát TPSP (12.8.4) và phối hợp điều tra (12.10.1). |
| **Q143** | ENTAILED | 10 | Khớp Fact ưu tiên ghi log xuống đĩa và truyền thời gian thực (10.2.1, 10.5.1). |
| **Q144** | ENTAILED | 9 | Khớp Fact tài khoản tạm thời có ngày hết hạn tự động (8.2.1) và rà soát hàng tháng. |
| **Q145** | NOT_SUPPORTED | 1 | **Retrieval Failure:** Không tìm thấy biện pháp chống tấn công Bluetooth/Short-range. |
| **Q146** | NOT_SUPPORTED | 1 | **Retrieval Failure:** Không tìm thấy quy trình cập nhật luật GDPR/địa phương. |
| **Q147** | ENTAILED | 10 | Khớp Fact giám sát nỗ lực truy cập bị từ chối vào thư mục nhạy cảm (10.2.1.4, 10.4.1). |
| **Q148** | ENTAILED | 10 | Khớp Fact lập kế hoạch nâng cấp hạ tầng (6.5.1) và kiểm tra lại NSC (1.2.7). |
| **Q149** | ENTAILED | 10 | Khớp Fact dùng Privacy filters (12.2.1) và VPN/MFA tại nơi công cộng. |
| **Q150** | ENTAILED | 10 | Khớp Fact phối hợp gỡ bỏ web lừa đảo (12.10.1) và hỗ trợ cảnh báo (12.9.2). |

---

### TỔNG HỢP KẾT QUẢ (EVALUATION SUMMARY)

*   **Tổng số câu đánh giá:** 150
*   **Số câu Đúng (Score >= 6):** 128 câu (Đa số đạt độ chính xác kỹ thuật rất cao).
*   **Số câu Sai / Lệch mã (Score <= 4):** 9 câu (Lỗi chủ yếu do gán sai mã Requirement ID hoặc dùng mã tự chế 1.5.x).
*   **Số câu Lỗi truy xuất (Score = 1):** 13 câu (Candidate báo không tìm thấy dữ liệu dù Gold có đáp án).
*   **Điểm trung bình hệ thống:** **7.84 / 10**

**Nhận xét:** Hệ thống RAG phản hồi rất tốt về mặt nội dung diễn giải tiếng Việt, tuy nhiên cần cải thiện khả năng Mapping (ánh xạ) chính xác mã Requirement ID theo đúng bảng Gold để tránh các lỗi "Anchor Drift". Các lỗi "Retrieval Failure" tập trung vào các mảng như: Bluetooth, Ransomware, và cập nhật luật GDPR.


"answer": "Cách đảm bảo các thay đổi đáng kể không làm suy giảm hiệu quả phân vùng CDE và các lỗ hổng mới được phát hiện ngay lập tức\n\nXác nhận phạm vi (scope) định kỳ và sau mỗi thay đổi quan trọng\n\nThực hiện đánh giá lại phạm vi PCI DSS ít nhất một lần mỗi 12 tháng và ngay sau khi có thay đổi đáng kể đối với môi trường trong phạm vi (Requirement 12.5.2)【1】.\nĐối với service provider, việc xác nhận phạm vi phải được thực hiện ít nhất mỗi 6 tháng và sau mỗi thay đổi quan trọng (Requirement 12.5.2.1)【1】.\nĐánh giá này bao gồm:\nKiểm kê các điều khiển phân đoạn (segmentation controls) đang sử dụng.\nXác định tất cả các kết nối từ bên thứ ba có quyền truy cập vào CDE.\nĐảm bảo tất cả các luồng dữ liệu, thành phần hệ thống, và kết nối được đưa vào phạm vi.\n\nKiểm tra kỹ thuật (segmentation testing) sau mỗi thay đổi\n\nThực hiện kiểm tra kỹ thuật phân đoạn để xác nhận rằng các kiểm soát phân đoạn vẫn cách ly CDE khỏi các hệ thống ngoài phạm vi, cả trước và sau khi có thay đổi (sub‑requirement 11.4.6)【3】.\nKiểm tra này nên được thực hiện càng thường xuyên càng tốt (ít nhất mỗi 6 tháng) để phát hiện sớm bất kỳ lỗ hổng nào trong việc cách ly mạng.\n\nSử dụng công cụ và quy trình phát hiện lỗ hổng ngay lập tức\n\nÁp dụng công cụ phát hiện dữ liệu (data discovery) để tìm mọi vị trí chứa PAN (hoặc các thành phần CHD) trong hoặc ngoài CDE, bao gồm cả các file lỗi, dump bộ nhớ, v.v.\nKết hợp quy trình quản lý lỗ hổng (Requirement 6.3) để:\nThu thập thông tin lỗ hổng từ các nguồn tin cậy (NVD, CERT, RSS, vendor alerts).\nĐánh giá mức độ rủi ro (CVSS, FIRST, v.v.) và triển khai vá ngay khi có (Requirement 6.3.3).\nThực hiện quét lỗ hổng định kỳ (Requirements 11.3.1 & 11.3.2) và đánh giá sau mỗi thay đổi để phát hiện các lỗ hổng mới.\n\nQuy trình kiểm tra và chứng minh\n\nKiểm tra tài liệu (scope review reports, segmentation test results) và phỏng vấn nhân sự để xác nhận rằng các hoạt động trên đã được thực hiện đúng thời gian và đầy đủ nội dung (Testing Procedures 12.5.2.a/b, 12.5.2.1.a/b, 11.4.6)【1】【3】.\nLưu trữ bằng chứng (báo cáo kiểm tra, danh sách kiểm soát, kết quả quét) để có thể cung cấp cho assessor hoặc khách hàng khi cần.\n\nThực hành tốt (Good Practice)\n\nTài liệu hoá toàn bộ môi trường (bảng/đồ thị các thành phần, luồng dữ liệu, vị trí lưu trữ PAN, cách bảo vệ dữ liệu).\nThực hiện kiểm tra sau mỗi thay đổi (cấu hình, triển khai, cập nhật phần mềm) thay vì chỉ chờ đến kỳ đánh giá định kỳ.\nĐảm bảo các thay đổi được quản lý qua quy trình Change Management và đánh giá tác động bảo mật trước khi triển khai.\n\nBằng cách kết hợp đánh giá phạm vi định kỳ, kiểm tra kỹ thuật phân đoạn sau mỗi thay đổi, và quy trình quản lý lỗ hổng liên tục, tổ chức có thể đảm bảo rằng các thay đổi mạng không làm suy giảm hiệu quả phân vùng CDE và các lỗ hổng mới được phát hiện và khắc phục ngay lập tức.",
    "