### A. Tài liệu gốc của Requirement 10

### B. Summary Overview của Control Objective 10.5
Tài liệu này mô tả chi tiết **Control Objective 10.5** của **Requirement 10** trong **PCI-DSS v4.0.1**, tập trung vào việc lưu trữ và duy trì lịch sử audit log.
Mục tiêu chính là đảm bảo audit log được lưu giữ đủ lâu và sẵn sàng phục vụ phân tích, điều tra sự cố khi cần thiết.
Gồm 1 sub-requirement chính:
- 10.5.1: Lưu trữ lịch sử audit log
Áp dụng cho tất cả audit log trong môi trường.

### C. Key Points của Control Objective 10.5
- Phạm vi áp dụng: Tất cả audit log và hệ thống lưu trữ log
- Trách nhiệm: Tài liệu hóa chính sách và quy trình lưu trữ log
- Lưu trữ dữ liệu: Log phải được lưu tối thiểu 12 tháng
- Khả dụng: Ít nhất 3 tháng log gần nhất phải sẵn sàng để phân tích
- Quản lý truy xuất: Phải đảm bảo truy cập nhanh khi cần điều tra

### D. Deep Summary của Control Objective 10.5
**Bối cảnh:**
Các sự cố bảo mật thường được phát hiện muộn, do đó cần có lịch sử log dài hạn để phục vụ điều tra và xác định phạm vi ảnh hưởng.
**Nội dung cốt lõi:**
- Lưu trữ audit log tối thiểu 12 tháng
- Đảm bảo ít nhất 3 tháng log gần nhất luôn sẵn sàng để phân tích ngay
- Thiết lập chính sách và quy trình lưu trữ log rõ ràng
- Có cơ chế lưu trữ (online, archive, backup) để đảm bảo khả dụng
**Dữ liệu đáng chú ý:**
- 12 tháng: thời gian lưu trữ tối thiểu
- 3 tháng: phải "immediately available" để phân tích
**Rủi ro / Lưu ý:**
- Không lưu đủ log → không điều tra được sự cố
- Log không sẵn sàng → chậm phản ứng khi có incident
- Lưu trữ không tập trung → khó truy xuất dữ liệu
- Mất log → mất bằng chứng forensic quan trọng

### E. Structured Output của Control Objective 10.5
**Control objectives:**10.5
**Sub-requirement:**10.5.1
**Defined Approach Requirements:**Retain audit log history for at least 12 months, with at least the most recent three months immediately available for analysis.
**Defined Approach Testing Procedures:**
- "10.5.1.a": Examine documentation to verify that the following is defined: • Audit log retention policies. • Procedures for retaining audit log history for at least 12 months, with at least the most recent three months immediately available online.
- "10.5.1.b": Examine configurations of audit log history, interview personnel and examine audit logs to verify that audit logs history is retained for at least 12 months.
- "10.5.1.c": Interview personnel and observe processes to verify that at least the most recent three months' audit log history is immediately available for analysis.
**Customized Approach Objective:**Historical records of activity are available immediately to support incident response and are retained for at least 12 months.
**Guidance - Purpose:**Retaining historical audit logs for at least 12 months is necessary because compromises often go unnoticed for significant lengths of time. Having centrally stored log history allows investigators to better determine the length of time a potential breach was occurring, and the possible system(s) impacted. By having three months of logs immediately available, an entity can quickly identify and minimize impact of a data breach.
**Guidance - Examples:**Methods that allow logs to be immediately available include storing logs online, archiving logs, or restoring logs quickly from backups.