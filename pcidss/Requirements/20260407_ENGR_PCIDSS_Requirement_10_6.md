### A. Tài liệu gốc của Requirement 10

### B. Summary Overview của Control Objective 10.6
Tài liệu này mô tả chi tiết **Control Objective 10.6** của **Requirement 10** trong **PCI-DSS v4.0.1**, tập trung vào việc đồng bộ thời gian hệ thống để đảm bảo tính nhất quán và chính xác của audit log.
Mục tiêu chính là đảm bảo tất cả hệ thống sử dụng thời gian đồng bộ, chính xác và được bảo vệ nhằm phục vụ logging, monitoring và điều tra sự cố.
Gồm 3 sub-requirement chính:
- 10.6.1: Triển khai time synchronization
- 10.6.2: Cấu hình hệ thống thời gian chuẩn
- 10.6.3: Bảo vệ cấu hình thời gian
Áp dụng cho tất cả system components trong môi trường.

### C. Key Points của Control Objective 10.6
- **Phạm vi áp dụng:** Tất cả system components
- **Trách nhiệm:**Triển khai và duy trì cơ chế đồng bộ thời gian
- **Đồng bộ thời gian:** Sử dụng time synchronization (ví dụ NTP)
- **Cấu hình hệ thống:**Sử dụng time server trung tâm và nguồn thời gian chuẩn (UTC)
- **Kiểm soát truy cập:**Giới hạn quyền thay đổi cấu hình thời gian
- **Giám sát:**Ghi log và theo dõi các thay đổi về thời gian

### D. Deep Summary của Control Objective 10.6
**Bối cảnh:**
Nếu thời gian giữa các hệ thống không đồng bộ, việc phân tích log và xác định chuỗi sự kiện khi xảy ra sự cố sẽ rất khó khăn.
**Nội dung cốt lõi:**
- Triển khai cơ chế đồng bộ thời gian trên toàn bộ hệ thống (NTP hoặc tương đương)
- Sử dụng time server trung tâm và nguồn thời gian chuẩn (UTC)
- Chỉ cho phép time server nhận thời gian từ nguồn tin cậy
- Đảm bảo hệ thống nội bộ chỉ nhận thời gian từ time server trung tâm
- Giới hạn quyền truy cập và thay đổi cấu hình thời gian
- Ghi log, giám sát và review các thay đổi về thời gian
**Dữ liệu đáng chú ý:**
- Time synchronization giúp correlation log giữa các hệ thống
- Có thể sử dụng NTP với nguồn thời gian chuẩn quốc tế
**Rủi ro / Lưu ý:**
- Không đồng bộ thời gian → không xác định được thứ tự sự kiện
- Time server không kiểm soát → bị thay đổi thời gian trái phép
- Không log thay đổi thời gian → attacker có thể che giấu hành vi
- Cấu hình sai → sai lệch log và ảnh hưởng điều tra forensic

### E. Structured Output của Control Objective 10.6
**Control objectives:**10.6
**Sub-requirement:**10.6.1
**Defined Approach Requirements:**System clocks and time are synchronized using time-synchronization technology.
**Defined Approach Testing Procedures:**Examine system configuration settings to verify that time-synchronization technology is implemented and kept current.
**Customized Approach Objective:**Common time is established across all systems.
**Applicability Notes:**Keeping time-synchronization includes managing vulnerabilities technology according to PCI DSS 6.3.1 and 6.3.3.
**Guidance - Purpose:**Time synchronization technology is used to synchronize clocks on multiple systems. When clocks are not properly synchronized, it can be difficult, if not impossible, to compare log files from different systems and establish an exact sequence of events, which is crucial for forensic analysis following a breach. For post-incident forensics teams, the accuracy and consistency of time across all systems and the time of each activity are critical in determining how the systems were compromised.
**Guidance - Examples:**Network Time Protocol (NTP) is one example of time-synchronization technology.

---
**Control objectives:**10.6
**Sub-requirement:**10.6.2
**Defined Approach Requirements:**Systems are configured to the correct and consistent time as follows:
• One or more designated time servers are in use.
• Only the designated central time server(s) receives time from external sources.
• Time received from external sources is based on International Atomic Time or Coordinated Universal Time (UTC).
• The designated time server(s) accept time updates only from specific industry-accepted external sources.
• Where there is more than one designated time server, the time servers peer with one another to keep accurate time.
• Internal systems receive time information only from designated central time server(s).
**Defined Approach Testing Procedures:**Examine system configuration settings for acquiring, distributing, and storing the correct time to verify the settings are configured in accordance with all elements specified in this requirement.
**Customized Approach Objective:**The time on all systems is accurate and consistent.
**Guidance - Purpose:**component of the time synchronization process. Accepting time updates from specific, industry- accepted external sources helps prevent a malicious individual from changing time settings on systems.
**Guidance - Good Practice:**Another option to prevent unauthorized use of internal time servers is to encrypt updates with a symmetric key and create access control lists that specify the IP addresses of client machines that will be provided with the time updates.

---
**Control objectives:**10.6
**Sub-requirement:**10.6.3
**Defined Approach Requirements:**Time synchronization settings and data are protected as follows:
• Access to time data is restricted to only personnel with a business need.
• Any changes to time settings on critical systems are logged, monitored, and reviewed.
**Defined Approach Testing Procedures:**
- "10.6.3.a": Examine system configurations and time- synchronization settings to verify that access to time data is restricted to only personnel with a business need.
- "10.6.3.b": Examine system configurations and time synchronization settings and logs and observe processes to verify that any changes to time settings on critical systems are logged, monitored, and reviewed.
**Guidance - Purpose:**Attackers will try to change time configurations to hide their activity. Therefore, restricting the ability to change or modify time synchronization configurations or the system time to administrators will lessen the probability of an attacker successfully changing time configurations.