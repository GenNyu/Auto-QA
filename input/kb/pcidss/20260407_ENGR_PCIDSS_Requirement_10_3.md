### A. Tài liệu gốc của Requirement 10

### B. Summary Overview của Control Objective 10.3
Tài liệu này mô tả chi tiết **Control Objective 10.3** của **Requirement 10 **trong **PCI-DSS v4.0.1**, tập trung vào việc bảo vệ tính toàn vẹn và bảo mật của audit log.
Mục tiêu chính là đảm bảo audit log không bị truy cập trái phép, không bị chỉnh sửa và được lưu trữ an toàn để phục vụ điều tra.
Gồm 4 sub-requirement chính:
- 10.3.1: Giới hạn truy cập đọc log
- 10.3.2: Bảo vệ log khỏi chỉnh sửa
- 10.3.3: Backup log tập trung
- 10.3.4: Giám sát thay đổi log
Áp dụng cho tất cả audit log trên system components và hệ thống lưu trữ log.

### C. Key Points của Control Objective 10.3
- **Phạm vi áp dụng:**Tất cả audit log và hệ thống lưu trữ log
- **Trách nhiệm:**Tài liệu hóa và triển khai kiểm soát bảo vệ log
- **Kiểm soát truy cập:**Chỉ cho phép truy cập log theo need-to-know
- **Bảo vệ dữ liệu:**Ngăn chỉnh sửa log thông qua access control và segregation
- **Lưu trữ:**Backup log về hệ thống tập trung an toàn
- **Giám sát:**Áp dụng file integrity monitoring để phát hiện thay đổi

### D. Deep Summary của Control Objective 10.3
**Bối cảnh:**
Audit log là bằng chứng quan trọng để phát hiện và điều tra sự cố. Nếu log bị chỉnh sửa hoặc truy cập trái phép, toàn bộ quá trình điều tra sẽ bị vô hiệu hóa.
**Nội dung cốt lõi:**
- Giới hạn quyền truy cập đọc log chỉ cho người có nhu cầu công việc
- Bảo vệ log khỏi bị chỉnh sửa bằng access control và segregation
- Backup log về hệ thống tập trung khó bị thay đổi
- Áp dụng file integrity monitoring để phát hiện thay đổi trái phép
- Bảo vệ log cả tại nguồn và tại nơi lưu trữ
**Dữ liệu đáng chú ý:**
- Log nên được lưu trên hệ thống tập trung (log server/SIEM)
- File integrity monitoring phải alert khi log bị thay đổi
**Rủi ro / Lưu ý:**
- Log bị truy cập trái phép → lộ thông tin nhạy cảm
- Log bị chỉnh sửa → mất bằng chứng điều tra
- Không backup log → mất dữ liệu khi hệ thống bị compromise
- Không giám sát thay đổi → attacker có thể xóa dấu vết

### E. Structured Output của Control Objective 10.3
**Control objectives:**10.3
**Sub-requirement:**10.3.1
**Defined Approach Requirements:**Read access to audit logs files is limited to those with a job-related need.
**Defined Approach Testing Procedures:**Interview system administrators and examine system configurations and privileges verify that only individuals with a job-related have read access to audit log files.
**Customized Approach Objective:**Stored activity records cannot be accessed by unauthorized personnel.
**Guidance - Purpose:**Audit log files contain sensitive information, and read access to the log files must be limited only to those with a valid business need. This access includes audit log files on the originating systems as well as anywhere else they are stored.
**Guidance - Good Practice:**Adequate protection of the audit logs includes strong access control that limits access to logs based on 'need to know' only and the use of physical or network segregation to make the logs harder to find and modify.

---
**Control objectives:**10.3
**Sub-requirement:**10.3.2
**Defined Approach Requirements:**Audit log files are protected to prevent modifications by individuals.
**Defined Approach Testing Procedures:**Examine system configurations and privileges and interview system administrators to verify that current audit log files are protected from modifications by individuals via access control mechanisms, physical segregation, and/or network segregation.
**Customized Approach Objective:**Stored activity records cannot be modified by personnel.
**Guidance - Purpose:**Often a malicious individual who has entered the network will try to edit the audit logs to hide their activity. Without adequate protection of audit logs, their completeness, accuracy, and integrity cannot be guaranteed, and the audit logs can be rendered useless as an investigation tool after a compromise. Therefore, audit logs should be protected on the originating systems as well as anywhere else they are stored.
**Guidance - Good Practice:**Entities should attempt to prevent logs from being exposed in public-accessible locations.

---
**Control objectives:**10.3
**Sub-requirement:**10.3.3
**Defined Approach Requirements:**Audit log files, including those for external- facing technologies, are promptly backed up to a secure, central, internal log server(s) or other media that is difficult to modify.
**Defined Approach Testing Procedures:** Examine backup configurations or log files to verify that current audit log files, including those for external-facing technologies, are promptly backed up to a secure, central, internal log server(s) or other media that is difficult to modify.
**Customized Approach Objective:**Stored activity records are secured and preserved in a central location to prevent unauthorized modification.
**Guidance - Purpose:**Promptly backing up the logs to a centralized log server or media that is difficult to alter keeps the logs protected, even if the system generating the logs becomes compromised. Writing logs from external-facing technologies such as wireless, network security controls, DNS, and mail servers, reduces the risk of those logs being lost or altered.
**Guidance - Good Practice:**Each entity determines the best way to back up log files, whether via one or more centralized log servers or other secure media. Logs may be written directly, offloaded, or copied from external systems to the secure internal system or media.

---
**Control objectives:**10.3
**Sub-requirement:**10.3.4
**Defined Approach Requirements:**File integrity monitoring or change-detection mechanisms is used on audit logs to ensure that existing log data cannot be changed without generating alerts.
**Defined Approach Testing Procedures:**Examine system settings, monitored files, and results from monitoring activities to verify the use of file integrity monitoring or change-detection software on audit logs.
**Customized Approach Objective:**Stored activity records cannot be modified without an alert being generated.
**Guidance - Purpose:**File integrity monitoring or change-detection systems check for changes to critical files and notify when such changes are identified. For file integrity monitoring purposes, an entity usually monitors files that do not regularly change, but when changed, indicate a possible compromise.
**Guidance - Good Practice:**Software used to monitor changes to audit logs should be configured to provide alerts when existing log data or files are changed or deleted. However, new log data being added to an audit log should not generate an alert.