### A. Tài liệu gốc của Chương 3 (Mục 3.2)

### B. Summary Overview của Chương 3 (Mục 3.2)
Tài liệu này mô tả chi tiết **mục 3.2 (Abbreviated terms)** trong **Chương 3 (Terms, definitions and abbreviated terms)** của **ISO/IEC 27002:2022**, tập trung vào việc **chuẩn hóa các ký hiệu rút gọn cho các khái niệm kỹ thuật, công nghệ và quản trị an toàn thông tin**.
Mục tiêu là **thiết lập một "ngôn ngữ chung" ngắn gọn nhưng chính xác, giúp tối ưu hóa việc soạn thảo chính sách, cấu hình hệ thống và trao đổi thông tin trong quá trình vận hành và đánh giá tuân thủ**.
Gồm **01** mục chính:
- **Danh mục 45+ thuật ngữ viết tắt tiêu chuẩn:** Bao quát các lĩnh vực từ quản lý định danh (IAM), hạ tầng mạng (VPN, SD-WAN), bảo mật ứng dụng (SAST) đến quản trị rủi ro và hồi phục (BIA, RPO, RTO),.

Áp dụng cho **các kiến trúc sư hệ thống, cán bộ soạn thảo chính sách và kiểm toán viên để đảm bảo tính đồng nhất giữa văn bản quản trị và bằng chứng kỹ thuật thực tế**.

### C. Key Points của Chương 3 (Mục 3.2)
- **Định danh năng lực công nghệ:** Việc sử dụng các thuật ngữ như SIEM, IDS, IPS, hoặc UEBA không chỉ là tên gọi công cụ mà còn định nghĩa năng lực **Phát hiện (#Detect)** và **Phản ứng (#Respond)** trong ma trận kiểm soát.
- **Cơ sở định lượng cho tính sẵn sàng:** Các thuật ngữ RPO và RTO là "thước đo" bắt buộc trong BIA (Phân tích tác động kinh doanh) để auditor đánh giá tính khả thi của các phương án dự phòng (8.13, 5.30).
- **Tiêu chuẩn hóa cơ chế truy cập:** Phải phân biệt rõ các mô hình kiểm soát truy cập (RBAC, ABAC, MAC, DAC) để làm căn cứ thiết kế và kiểm tra tính phù hợp của việc cấp phát quyền hạn (8.2, 8.3).
- **Quản trị thiết bị cá nhân (BYOD):** Thuật ngữ BYOD gắn liền với việc mở rộng phạm vi kiểm soát tài sản (8.1), yêu cầu các chính sách phải bao hàm cả thiết bị không thuộc sở hữu của tổ chức.
- **Tuân thủ quyền riêng tư:** Các thuật ngữ PII và PIA là căn cứ để định danh các biện pháp bảo vệ dữ liệu cá nhân và đánh giá tác động quyền riêng tư theo yêu cầu pháp lý (5.34).

### D. Deep Summary của Chương 3 (Mục 3.2)
**Bối cảnh:**
Trong môi trường an toàn thông tin hiện đại, sự phức tạp của công nghệ đòi hỏi một hệ thống ký hiệu rút gọn để tăng hiệu suất quản trị. Tuy nhiên, việc hiểu sai các từ viết tắt này thường dẫn đến các lỗi cấu hình kỹ thuật hoặc sai lệch trong báo cáo tuân thủ. Chương 3.2 cung cấp bảng tra cứu chính thức để làm sạch dữ liệu giao tiếp nội bộ.

**Nội dung cốt lõi:**
Trọng tâm là sự giao thoa giữa quản trị và kỹ thuật. Ví dụ, **IAM** (Identity and Access Management) không chỉ là một hệ thống phần mềm mà là một năng lực vận hành bao gồm nhiều tiến trình từ định danh đến xác thực. Tương tự, các thuật ngữ về mạng như **SD-WAN** hay **VPN** định hình phạm vi của kiểm soát an ninh mạng (8.20, 8.22).

**Dữ liệu đáng chú ý:**
- **Nhóm bảo mật hiện đại:** UEBA (Phân tích hành vi), SAST (Kiểm thử an ninh tĩnh), IoT (Internet vạn vật) và Cloud.
- **Nhóm hạ tầng cốt lõi:** DNS, IP, NTP, UPS, và các chuẩn kết nối vật lý (USB, SD).
- **Nhóm quản lý sự cố và hồi phục:** BIA, RPO, RTO là "bộ ba" quyết định sự thành bại của kế hoạch kinh doanh liên tục.

**Rủi ro / Lưu ý:**
- **Rủi ro mơ hồ trong Policy:** Nếu chính sách sử dụng thuật ngữ không nằm trong danh mục chuẩn (hoặc dùng sai ngữ cảnh, ví dụ nhầm lẫn giữa ACL và RBAC), tổ chức có thể bị auditor đánh giá là "thiếu năng lực kiểm soát hệ thống".
- **Lưu ý thực thi:** Khi cấu hình thiết bị (như Firewall hay Switch), việc sử dụng các khái niệm như **VLAN** (liên quan đến Segregation of networks - 8.22) phải nhất quán với các định nghĩa về phân vùng mạng trong tài liệu quản trị.
- **Impact nếu fail:** Hiểu sai các thuật ngữ viết tắt dẫn đến việc thiết lập sai các tham số kỹ thuật (ví dụ: đặt giá trị RPO/RTO không tương thích với năng lực của hệ thống Backup), gây tê liệt khả năng phục hồi khi có sự cố thực tế xảy ra.

### E. Structured Output của Chương 3 (Mục 3.2)
**Purpose:**
For the purposes of this document, the following abbreviated terms apply.

**Abbreviations:**

| Abbreviation | Meaning |
| --- | --- |
| ABAC | attribute-based access control |
| ACL | access control list |
| BIA | business impact analysis |
| BYOD | bring your own device |
| CAPTCHA | completely automated public Turing test to tell computers and humans apart |
| CPU | central processing unit |
| DAC | discretionary access control |
| DNS | domain name system |
| GPS | global positioning system |
| IAM | identity and access management |
| ICT | information and communication technology |
| ID | identifier |
| IDE | integrated development environment |
| IDS | intrusion detection system |
| IoT | internet of things |
| IP | internet protocol |
| IPS | intrusion prevention system |
| IT | information technology |
| ISMS | information security management system |
| MAC | mandatory access control |
| NTP | network time protocol |
| PIA | privacy impact assessment |
| PII | personally identifiable information |
| PIN | personal identification number |
| PKI | public key infrastructure |
| PTP | precision time protocol |
| RBAC | role-based access control |
| RPO | recovery point objective |
| RTO | recovery time objective |
| SAST | static application security testing |
| SD | secure digital |
| SDN | software-defined networking |
| SD-WAN | software-defined wide area networking |
| SIEM | security information and event management |
| SMS | short message service |
| SQL | structured query language |
| SSO | single sign on |
| SWID | software identification |
| UEBA | user and entity behaviour analytics |
| UPS | uninterruptible power supply |
| URL | uniform resource locator |
| USB | universal serial bus |
| VM | virtual machine |
| VPN | virtual private network |
| WiFi | wireless fidelity |
