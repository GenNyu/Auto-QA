### A. Tài liệu gốc của Requirement 10

### B. Summary Overview của Control Objective 10.2
Tài liệu này mô tả chi tiết **Control Objective 10.2** của **Requirement 10** trong **PCI-DSS v4.0.1**, tập trung vào việc ghi log đầy đủ các hoạt động liên quan đến hệ thống và dữ liệu thẻ.
Mục tiêu chính là đảm bảo tất cả các sự kiện quan trọng được ghi nhận đầy đủ để phục vụ giám sát, phát hiện bất thường và điều tra sự cố.
Gồm 2 sub-requirement chính:
- 10.2.1: Ghi log các sự kiện quan trọng
- 10.2.2: Nội dung chi tiết của log
Áp dụng cho tất cả system components và các hoạt động liên quan đến cardholder data.

### C. Key Points của Control Objective 10.2
- **Phạm vi áp dụng:**Tất cả system components và hoạt động liên quan CHD
- **Trách nhiệm:**Triển khai và đảm bảo logging được bật và hoạt động
- **Ghi log sự kiện:** Bao gồm truy cập dữ liệu, hành động admin, login thất bại, thay đổi account
- **Ghi log hệ thống:** Bao gồm start/stop log và thay đổi system object
- **Nội dung log:**Phải đầy đủ thông tin (user, thời gian, hành động, kết quả…)
- **Bảo mật log:**Log là dữ liệu nhạy cảm, cần được bảo vệ

### D. Deep Summary của Control Objective 10.2
**Bối cảnh:**
Nếu không có log đầy đủ, tổ chức sẽ không thể phát hiện hành vi bất thường hoặc điều tra sự cố bảo mật.
**Nội dung cốt lõi:**
- Bật logging trên tất cả system components
- Ghi log truy cập vào cardholder data
- Ghi log hành động của admin và account có quyền cao
- Ghi log login thất bại và thay đổi credential
- Ghi log hoạt động liên quan đến audit log (start/stop/change)
- Ghi log tạo/xóa system object
- Đảm bảo mỗi log chứa đủ thông tin (who, what, when, where, result)
**Dữ liệu đáng chú ý:**
- Log phải ghi nhận cả success và failure
- Bao gồm user ID, timestamp, event type, source và resource bị ảnh hưởng
**Rủi ro / Lưu ý:**
- Không bật logging → mất khả năng phát hiện sự cố
- Log không đầy đủ → không truy vết được hành vi
- Không log admin action → bỏ sót rủi ro lớn
- Log bị chỉnh sửa → che giấu hành vi tấn công

### E. Structured Output của Control Objective 10.2
**Control objectives:**10.2
**Sub-requirement:**10.2.1
**Defined Approach Requirements:**Audit logs are enabled and active for all system components and cardholder data.
**Defined Approach Testing Procedures:**Interview the system administrator and examine system configurations to verify that audit logs are enabled and active for all system components.
**Customized Approach Objective:**Records of all activities affecting system components and cardholder data are captured.
**Guidance - Purpose:**Audit logs must exist for all system components. Audit logs send alerts the system administrator, provides data to other monitoring mechanisms, such as intrusion-detection systems (IDS) and security information and event monitoring systems (SIEM) tools, and provide a history trail for post-incident investigation. Logging and analyzing security-relevant events enable an organization to identify and trace potentially malicious activities.
**Guidance - Good Practice:**When an entity considers which information to record in their logs, it is important to remember that information stored in audit logs is sensitive and should be protected per requirements in this standard. Care should be taken to only store essential information in the audit logs to minimize risk.

---
**Control objectives:**10.2
**Sub-requirement:**10.2.1.1
**Defined Approach Requirements:**Audit logs capture all individual user access to cardholder data.
**Defined Approach Testing Procedures:**Examine audit log configurations and log data to verify that all individual user access to cardholder data is logged.
**Customized Approach Objective:**Records of all individual user access to cardholder data are captured.
**Guidance - Purpose:**It is critical to have a process or system that links user access to system components accessed. Malicious individuals could obtain knowledge of a user account with access to systems in the CDE, or they could create a new, unauthorized account to access cardholder data.
**Guidance - Good Practice:**A record of all individual access to cardholder data can identify which accounts may have been compromised or misused.

---
**Control objectives:**10.2
**Sub-requirement:**10.2.1.2
**Defined Approach Requirements:**Audit logs capture all actions taken by any individual with administrative access, including any interactive use of application or system accounts.
**Defined Approach Testing Procedures:**Examine audit log configurations and log data to verify that all actions taken by any individual with administrative access, including any interactive use of application or system accounts, are logged.
**Customized Approach Objective:**Records of all actions performed by individuals with elevated privileges are captured.
**Guidance - Purpose:**Accounts with increased access privileges, such as the 'administrator' or 'root' account, have the potential to significantly impact the security or operational functionality of a system. Without a log of the activities performed, an organization is cannot trace any issues resulting from an administrative mistake or misuse of privilege back to the specific action and account.
**Guidance - Definitions:**The functions or activities considered to be administrative are beyond those performed by regular users as part of routine business functions. Refer to Appendix G for the definition of

---
**Control objectives:**10.2
**Sub-requirement:**10.2.1.3
**Defined Approach Requirements:**Audit logs capture all access to audit logs.
**Defined Approach Testing Procedures:**Examine audit log configurations and log data to verify that access to all audit logs is captured.
**Customized Approach Objective:**Records of all access to audit logs are captured.
**Guidance - Purpose:**Malicious users often attempt to alter audit logs to hide their actions. A record of access allows an organization to trace any inconsistencies or potential tampering of the logs to an individual account. Having logs identify changes, additions, and deletions to the audit logs can help retrace steps made by unauthorized personnel.

---
**Control objectives:**10.2
**Sub-requirement:**10.2.1.4
**Defined Approach Requirements:**Audit logs capture all invalid logical access attempts.
**Defined Approach Testing Procedures:**Examine audit log configurations and log data to verify that invalid logical access attempts are captured.
**Customized Approach Objective:**Records of all invalid access attempts are captured.
**Guidance - Purpose:**Malicious individuals will often perform multiple access attempts on targeted systems. Multiple invalid login attempts may be an indication of an unauthorized user's attempts to 'brute force' or guess a password.

---
**Control objectives:**10.2
**Sub-requirement:**10.2.1.5
**Defined Approach Requirements:**Audit logs capture all changes to identification and authentication credentials including, but not limited to:
• Creation of new accounts.
• Elevation of privileges.
• All changes, additions, or deletions to accounts with administrative access.
**Defined Approach Testing Procedures:**Examine audit log configurations and log data to verify that changes to identification and authentication credentials are captured in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Records of all changes to identification and authentication credentials are captured.
**Guidance - Purpose:**Logging changes to authentication credentials (including elevation of privileges, additions, and deletions of accounts with administrative access) provides residual evidence of activities. Malicious users may attempt to manipulate authentication credentials to bypass them or impersonate a valid account.

---
**Control objectives:**10.2
**Sub-requirement:**10.2.1.6
**Defined Approach Requirements:**Audit logs capture the following:
• All initialization of new audit logs, and
• All starting, stopping, or pausing of the existing audit logs.
**Defined Approach Testing Procedures:**Examine audit log configurations and log data to verify that all elements specified in this requirement are captured.
**Customized Approach Objective:**Records of all changes to audit log activity status
**Guidance - Purpose:**Turning off or pausing audit logs before performing illicit activities is common practice for malicious users who want to avoid detection. Initialization of audit logs could indicate that that a user disabled the log function to hide their actions.

---
**Control objectives:**10.2
**Sub-requirement:**10.2.1.7
**Defined Approach Requirements:**Audit logs capture all creation and deletion of system-level objects.
**Defined Approach Testing Procedures:**Examine audit log configurations and log data to verify that creation and deletion of system level objects is captured.
**Customized Approach Objective:**Records of alterations that indicate a system has been modified from its intended functionality are captured.
**Guidance - Purpose:**Malicious software, such as malware, often creates or replaces system-level objects on the target system to control a particular function or operation on that system. By logging when system-level objects are created or deleted, it will be easier to determine whether such modifications were authorized.

---
**Control objectives:**10.2
**Sub-requirement:**10.2.2
**Defined Approach Requirements:**Audit logs record the following details for each auditable event:
• User identification.
• Type of event.
• Date and time.
• Success and failure indication.
• Origination of event.
• Identity or name of affected data, system component, resource, or service (for example, name and protocol).
**Defined Approach Testing Procedures:**Interview personnel and examine audit log configurations and log data to verify that all elements specified in this requirement are included in log entries for each auditable event (from 10.2.1.1 through 10.2.1.7).
**Customized Approach Objective:**Sufficient data to be able to identify successful and failed attempts and who, what, when, where, and how for each event listed in requirement 10.2.1 are captured.
**Guidance - Purpose:**By recording these details for the auditable events at 10.2.1.1 through 10.2.1.7, a potential compromise can be quickly identified, with sufficient detail to facilitate following up on suspicious activities.