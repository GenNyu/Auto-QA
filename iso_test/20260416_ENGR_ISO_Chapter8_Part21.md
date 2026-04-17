### A. Tài liệu gốc của Chương 8 (Control 8.33, 8.34)

### B. Summary Overview của Chương 8 (Control 8.33, 8.34)
Tài liệu này mô tả chi tiết **mục 8.33 và 8.34** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào quản lý dữ liệu dùng để kiểm thử và kiểm soát cách audit/test ảnh hưởng đến hệ thống vận hành.
Mục tiêu là bảo đảm dữ liệu kiểm thử đủ gần với thực tế nhưng không làm lộ thông tin nhạy cảm, đồng thời cho phép hoạt động kiểm toán và assurance diễn ra mà không gây gián đoạn hoặc mở rộng rủi ro lên production.
Gồm 2 control chính:
- `8.33`: Test information - lựa chọn, bảo vệ và quản lý dữ liệu dùng cho kiểm thử
- `8.34`: Protection of information systems during audit testing - bảo vệ hệ thống thông tin khi kiểm thử phục vụ audit/assurance

Áp dụng cho môi trường test, kiểm thử chấp nhận, kiểm toán kỹ thuật, hoạt động assurance và các hệ thống vận hành đang chạy.

### C. Key Points của Chương 8 (Control 8.33, 8.34)
- **Mục tiêu quản trị:** `8.33` giữ dữ liệu test có giá trị và an toàn; `8.34` cho phép audit test diễn ra với tác động tối thiểu lên hệ thống vận hành.
- **Yêu cầu chính của 8.33:** Dữ liệu test phải được chọn lọc, phân quyền, ghi log, che/mask khi cần và xóa ngay sau khi dùng xong.
- **Yêu cầu chính của 8.34:** Mọi truy cập phục vụ audit phải được thỏa thuận trước, giới hạn phạm vi, ưu tiên read-only và có giám sát, ghi log đầy đủ.
- **Điểm vận hành quan trọng:** Dữ liệu test cần đủ sát thực tế để kết quả đáng tin cậy, nhưng không được trở thành bản sao mở của dữ liệu production.
- **Lưu ý thực tế:** Nếu cho audit test quyền ghi trực tiếp hoặc để dữ liệu test tồn tại quá lâu, rủi ro rò rỉ, sai lệch kết quả và tác động vận hành sẽ tăng lên.

### D. Deep Summary của Chương 8 (Control 8.33, 8.34)
**Bối cảnh:**
Hai control này xử lý hai rủi ro thường bị xem nhẹ trong vận hành công nghệ. `8.33` tập trung vào dữ liệu được dùng để kiểm thử, còn `8.34` tập trung vào cách auditor hoặc bên assurance tiếp cận hệ thống thật mà không phá vỡ tính sẵn sàng hoặc bí mật của nó.

**Nội dung cốt lõi:**
- `8.33` coi test data là một tài sản cần quản lý, không phải dữ liệu phụ trợ vô danh; chất lượng test phụ thuộc trực tiếp vào chất lượng và tính bảo mật của dữ liệu đó.
- `8.33` yêu cầu kiểm soát tương tự production về truy cập, nhưng bổ sung các biện pháp riêng như masking, logging copy/use và xóa dữ liệu sau kiểm thử.
- `8.33` giải quyết mâu thuẫn giữa hai nhu cầu: cần dữ liệu gần thực tế để test có ý nghĩa, nhưng không được để dữ liệu nhạy cảm lan ra môi trường dev/test.
- `8.34` đặt kiểm toán kỹ thuật vào một khung quản trị có phê duyệt, giới hạn scope và ưu tiên read-only để giảm xác suất làm gián đoạn hệ thống đang chạy.
- `8.34` mở rộng sang cả thiết bị của người kiểm tra, vì thiết bị không được bảo vệ có thể trở thành điểm xâm nhập phụ trợ vào hệ thống vận hành.

**Dữ liệu đáng chú ý:**
- `8.33` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, thuộc `#Information_protection` và miền `#Protection`.
- `8.34` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#System_and_network_security#Information_protection` và miền `#Governance_and_Ecosystem#Protection`.
- `8.33` áp dụng cho cả test environment nội bộ và cloud service, nên phạm vi kiểm soát không phụ thuộc nơi triển khai.
- `8.34` nhấn mạnh read-only access, nhưng vẫn cho phép ngoại lệ khi cần thông qua người quản trị có quyền phù hợp thay mặt auditor.
- `8.34` cho phép các test gây ảnh hưởng khả dụng thực hiện ngoài giờ làm việc, phản ánh yêu cầu cân bằng giữa kiểm tra và vận hành.

**Rủi ro / Lưu ý:**
- Nếu test data không được mask hoặc xóa đúng cách, dữ liệu nhạy cảm có thể bị lộ hoặc bị dùng ngoài mục đích.
- Nếu không tách quyền và không ghi log khi sao chép dữ liệu vào test environment, tổ chức sẽ khó truy vết trách nhiệm khi có sự cố.
- Nếu audit test vượt phạm vi đã thống nhất, dùng quyền ghi hoặc chạy tool tùy tiện, hệ thống production có thể bị ảnh hưởng trực tiếp.
- Nếu thiết bị dùng để audit không được kiểm tra an ninh trước khi truy cập, audit itself có thể trở thành đường xâm nhập.

### E. Structured Output của Chương 8 (Control 8.33, 8.34)
**Section:** 8.33
**Title:** Test information

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Information_protection |
| Security domains | #Protection |

**Control:**
Test information should be appropriately selected, protected and managed.

**Purpose:**
To ensure relevance of testing and protection of operational information used for testing.

**Guidance:**
Test information should be selected to ensure the reliability of tests results and the confidentiality of the relevant operational information. Sensitive information (including personally identifiable information) should not be copied into the development and testing environments (see 8.31).

The following guidelines should be applied to protect the copies of operational information, when used for testing purposes, whether the test environment is built in-house or on a cloud service:

- applying the same access control procedures to test environments as those applied to operational environments;
- having a separate authorization each time operational information is copied to a test environment;
- logging the copying and use of operational information to provide an audit trail;
- protecting sensitive information by removal or masking (see 8.11) if used for testing;
- properly deleting (see 8.10) operational information from a test environment immediately after the testing is complete to prevent unauthorized use of test information.

Test information should be securely stored (to prevent tampering, which can otherwise lead to invalid results) and only used for testing purposes.

**Other information:**
System and acceptance testing can require substantial volumes of test information that are as close as possible to operational information.

---
**Section:** 8.34
**Title:** Protection of information systems during audit testing

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #System_and_network_security #Information_protection |
| Security domains | #Governance_and_Ecosystem #Protection |

**Control:**
Audit tests and other assurance activities involving assessment of operational systems should be planned and agreed between the tester and appropriate management.

**Purpose:**
To minimize the impact of audit and other assurance activities on operational systems and business processes.

**Guidance:**
The following guidelines should be observed:

- agreeing audit requests for access to systems and data with appropriate management;
- agreeing and controlling the scope of technical audit tests;
- limiting audit tests to read-only access to software and data. If read-only access is not available to obtain the necessary information, executing the test by an experienced administrator who has the necessary access rights on behalf of the auditor;
- if access is granted, establishing and verifying the security requirements (e.g. antivirus and patching) of the devices used for accessing the systems (e.g. laptops or tablets) before allowing the access;
- only allowing access other than read-only for isolated copies of system files, deleting them when the audit is completed, or giving them appropriate protection if there is an obligation to keep such files under audit documentation requirements;
- identifying and agreeing on requests for special or additional processing, such as running audit tools;
- running audit tests that can affect system availability outside business hours;
- monitoring and logging all access for audit and test purposes.

**Other information:**
Audit tests and other assurance activities can also happen on development and test systems, where such tests can impact for example the integrity of code or lead to disclosure of any sensitive information held in such environments.