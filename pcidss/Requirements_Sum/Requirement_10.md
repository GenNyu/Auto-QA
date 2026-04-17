### A. Tài liệu gốc của Requirement 10

### B. Summary Overview của Control Objective 10.1
Tài liệu này mô tả chi tiết **Control Objective 10.1** của **Requirement 10** trong **PCI-DSS v4.0.1**, tập trung vào việc thiết lập và duy trì chính sách, quy trình và phân công trách nhiệm liên quan đến logging và monitoring.
Mục tiêu chính là đảm bảo các chính sách, quy trình và vai trò trách nhiệm được tài liệu hóa, cập nhật, áp dụng thực tế và được hiểu rõ bởi các bên liên quan trong hoạt động ghi log và giám sát.
Gồm 2 sub-requirement chính:
- 10.1.1: Quản lý chính sách và quy trình
- 10.1.2: Phân công vai trò và trách nhiệm
Áp dụng cho toàn bộ tổ chức và nhân sự tham gia vào các hoạt động logging và monitoring theo Requirement 10.

### C. Key Points của Control Objective 10.1
- **Phạm vi áp dụng:**Tất cả chính sách, quy trình và nhân sự liên quan logging và monitoring
- **Trách nhiệm:**Phân rõ vai trò, đảm bảo nhân sự hiểu và thực hiện đúng
- **Quản lý tài liệu:**Chính sách và quy trình phải được tài liệu hóa, cập nhật và phổ biến
- **Áp dụng thực tế:**Quy trình phải được triển khai và sử dụng thực tế
- **Truyền thông:**Đảm bảo các bên liên quan được phổ biến và hiểu nội dung

### D. Deep Summary của Control Objective 10.1
**Bối cảnh:**
Nếu chính sách và trách nhiệm không rõ ràng, các hoạt động logging và monitoring có thể không được thực hiện đầy đủ, làm giảm khả năng phát hiện sự cố bảo mật.
**Nội dung cốt lõi:**
- Tài liệu hóa chính sách và quy trình liên quan logging và monitoring
- Cập nhật khi có thay đổi về hệ thống hoặc yêu cầu giám sát
- Đảm bảo quy trình được áp dụng thực tế
- Phổ biến đến tất cả nhân sự liên quan
- Phân rõ vai trò và trách nhiệm cho từng hoạt động
**Dữ liệu đáng chú ý:**
- Chính sách và quy trình phải "in use" và "known to all affected parties"
- Có thể sử dụng RACI matrix để quản lý trách nhiệm
**Rủi ro / Lưu ý:**
- Chính sách không cập nhật → không phù hợp hệ thống hiện tại
- Quy trình không được thực thi → mất khả năng giám sát
- Nhân sự không rõ trách nhiệm → bỏ sót log/alert
- Thiếu phân công rõ ràng → không có accountability

### E. Structured Output của Control Objective 10.1
**Control objectives:**10.1
**Sub-requirement:**10.1.1
**Defined Approach Requirements:**All security policies and operational procedures that are identified in Requirement 10 are:
• Documented.
• Kept up to date.
• In use.
• Known to all affected parties.
**Defined Approach Testing Procedures:**Examine documentation and interview personnel to verify that security policies and operational procedures identified in Requirement 10 are managed in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Expectations, controls, and oversight for meeting activities within Requirement 10 are defined and adhered to by affected personnel. All supporting activities are repeatable, consistently applied, and conform to management's intent.
**Guidance - Purpose:**Requirement 10.1.1 is about effectively managing and maintaining the various policies and procedures specified throughout Requirement 10. While it is important to define the specific policies or procedures called out in Requirement 10, it is equally important to ensure they are properly documented, maintained, and disseminated.
**Guidance - Good Practice:**It is important to update policies and procedures as needed to address changes in processes, technologies, and business objectives. For this reason, consider updating these documents as soon as possible after a change occurs and not only on a periodic cycle.
**Guidance - Definitions:**Security policies define the entity's security objectives and principles. Operational procedures describe how to perform activities, and define the controls, methods, and processes that are followed to achieve the desired result in a consistent manner and in accordance with policy objectives.

---
**Control objectives:**10.1
**Sub-requirement:**10.1.2
**Defined Approach Requirements:**Roles and responsibilities for performing activities in Requirement 10 are documented, assigned, and understood.
**Defined Approach Testing Procedures:**
- "10.1.2.a": Examine documentation to verify that descriptions of roles and responsibilities for performing activities in Requirement 10 are documented and assigned.
- "10.1.2.b": Interview personnel with responsibility for performing activities in Requirement 10 to verify that roles and responsibilities are assigned as defined and are understood.
**Customized Approach Objective:** Day-to-day responsibilities for performing all the activities in Requirement 10 are allocated. Personnel are accountable for successful, continuous operation of these requirements.
**Guidance - Purpose:**If roles and responsibilities are not formally assigned, personnel may not be aware of their day-to-day responsibilities and critical activities may not occur.
**Guidance - Good Practice:**Roles and responsibilities may be documented within policies and procedures or maintained within separate documents. As part of communicating roles and responsibilities, entities can consider having personnel acknowledge their acceptance and understanding of their assigned roles and responsibilities.
**Guidance - Examples:**A method to document roles and responsibilities is a responsibility assignment matrix that includes who is responsible, accountable, consulted, and informed (also called a RACI matrix).

================

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

================

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

================

### A. Tài liệu gốc của Requirement 10

### B. Summary Overview của Control Objective 10.4
Tài liệu này mô tả chi tiết **Control Objective 10.4** của **Requirement 10** trong **PCI-DSS v4.0.1**, tập trung vào việc review và phân tích audit log nhằm phát hiện sớm các hoạt động bất thường.
Mục tiêu chính là đảm bảo các log được xem xét định kỳ và kịp thời để phát hiện, xử lý các sự kiện bất thường hoặc dấu hiệu tấn công.
Gồm 3 sub-requirement chính:
- 10.4.1: Review log hàng ngày
- 10.4.2: Review log định kỳ cho hệ thống khác
- 10.4.3: Xử lý exception và anomaly
Áp dụng cho tất cả audit log trong môi trường, bao gồm hệ thống quan trọng và hệ thống khác trong scope.

### C. Key Points của Control Objective 10.4
- **Phạm vi áp dụng:**Tất cả audit log từ system components
- **Trách nhiệm:**Tài liệu hóa và thực hiện quy trình review log
- **Review định kỳ:**Log quan trọng phải review hàng ngày
- **Tự động hóa:**Sử dụng công cụ tự động (SIEM, log analyzer…)
- **Quản lý rủi ro:**Xác định tần suất review dựa trên risk analysis
- **Xử lý sự kiện:**Phải điều tra và xử lý anomaly/exception

### D. Deep Summary của Control Objective 10.4
**Bối cảnh:**
Nhiều sự cố bảo mật không được phát hiện kịp thời do thiếu review log, dẫn đến thời gian tồn tại của attacker trong hệ thống kéo dài.
**Nội dung cốt lõi:**
- Review log hàng ngày cho security event, hệ thống CDE và hệ thống quan trọng
- Review định kỳ cho các hệ thống còn lại dựa trên risk analysis
- Sử dụng công cụ tự động để phân tích và phát hiện bất thường
- Thiết lập baseline hoạt động bình thường để phát hiện anomaly
- Xử lý và điều tra tất cả exception và anomaly được phát hiện
**Dữ liệu đáng chú ý:**
- Daily review áp dụng 24/7, kể cả ngày lễ
- Tần suất review hệ thống khác phải dựa trên targeted risk analysis
**Rủi ro / Lưu ý:**
- Không review log → không phát hiện tấn công kịp thời
- Review thủ công → dễ bỏ sót sự kiện quan trọng
- Không xử lý anomaly → attacker tồn tại lâu trong hệ thống
- Không có baseline → khó phân biệt hành vi bất thường

### E. Structured Output của Control Objective 10.4
**Control objectives:**10.4
**Sub-requirement:**10.4.1
**Defined Approach Requirements:**The following audit logs are reviewed at least once daily:
• All security events.
• Logs of all system components that store, process, or transmit CHD and/or SAD.
• Logs of all critical system components.
• Logs of all servers and system components that perform security functions (for example, network security controls, intrusion-detection systems/intrusion-prevention systems (IDS/IPS), authentication servers).
**Defined Approach Testing Procedures:**
- "10.4.1.a": Examine security policies and procedures to verify that processes are defined for reviewing all elements specified in this requirement at least once daily.
- "10.4.1.b": Observe processes and interview personnel to verify that all elements specified in this requirement are reviewed at least once daily
**Customized Approach Objective:**Potentially suspicious or anomalous activities are quickly identified to minimize impact.
**Guidance - Purpose:**Many breaches occur months before being detected. Regular log reviews mean incidents can be quickly identified and proactively addressed.
**Guidance - Good Practice:**Checking logs daily (7 days a week, 365 days a year, including holidays) minimizes the amount of time and exposure of a potential breach. Log harvesting, parsing, and alerting tools, centralized log management systems, event log analyzers, and security information and event management (SIEM) solutions are examples of automated tools that can be used to meet this requirement. Daily review of security events-for example, notifications or alerts that identify suspicious or anomalous activities-as well as logs from critical system components, and logs from systems that perform security functions, such as firewalls, IDS/IPS, file integrity monitoring (FIM) systems, etc., is necessary to identify potential issues. The determination of 'security event' will vary for each organization and may include consideration for the type of technology, location, and function of the device. Organizations may also wish to maintain a baseline of 'normal' traffic to help identify anomalous behavior. An entity that uses third-party service providers to perform log review services is responsible to provide context about the entity's environment to the service providers, so it understands the entity's environment, has a baseline of 'normal' traffic for the entity, and can detect potential security issues and provide accurate exceptions and anomaly notifications.

---
**Control objectives:**10.4
**Sub-requirement:**10.4.1.1
**Defined Approach Requirements:**Automated mechanisms are used to perform audit log reviews.
**Defined Approach Testing Procedures:**Examine log review mechanisms and interview personnel to verify that automated mechanisms are used to perform log reviews.
**Customized Approach Objective:**Potentially suspicious or anomalous activities are identified via a repeatable and consistent mechanism.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Manual log reviews are difficult to perform, even for one or two systems, due to the amount of log data that is generated. However, using log harvesting, parsing, and alerting tools, centralized log management systems, event log analyzers, and security information and event management (SIEM) solutions can help facilitate the process by identifying log events that need to be reviewed.
**Guidance - Good Practice:**Establishing a baseline of normal audit activity patterns is critical to the effectiveness of an automated log review mechanism. The analysis of new audit activity against the established baseline can significantly improve the identification of suspicious or anomalous activities. The entity should keep logging tools aligned with any changes in their environment by periodically reviewing tool settings and updating settings to reflect any changes.
**Guidance - Further Information:**Refer to the Information Supplement: Effective Daily Log Monitoring for additional guidance.

---
**Control objectives:**10.4
**Sub-requirement:**10.4.2
**Defined Approach Requirements:**Logs of all other system components (those not specified in Requirement 10.4.1) are reviewed periodically.
**Defined Approach Testing Procedures:**
- "10.4.2.a": Examine security policies and procedures to verify that processes are defined for reviewing logs of all other system components periodically.
- "10.4.2.b": Examine documented results of log reviews and interview personnel to verify that reviews are performed periodically.
**Customized Approach Objective:**Potentially suspicious or anomalous activities for other system components (not included in 10.4.1)
**Applicability Notes:** This requirement is applicable to all other in-scope system components not included in Requirement 10.4.1.
**Guidance - Purpose:**Periodic review of logs for all other system components (not specified in Requirement 10.4.1) helps to identify indications of potential issues or attempts to access critical systems via less-critical systems.

---
**Control objectives:**10.4
**Sub-requirement:**10.4.2.1
**Defined Approach Requirements:**The frequency of periodic log reviews for all other system components (not defined in Requirement 10.4.1) is defined in the entity's targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1
**Defined Approach Testing Procedures:**
- "10.4.2.1.a": Examine the entity's targeted risk analysis for the frequency of periodic log reviews for all other system components (not defined in Requirement 10.4.1) to verify the risk analysis was performed in accordance with all elements specified at Requirement 12.3.1.
- "10.4.2.1.b": Examine documented results of periodic log reviews of all other system components (not defined in Requirement 10.4.1) and interview personnel to verify log reviews are performed at the frequency specified in the entity's targeted risk analysis performed for this requirement.
**Customized Approach Objective:**Log reviews for lower-risk system components are performed at a frequency that addresses the entity's risk.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Entities can determine the optimum period to review these logs based on criteria such as the complexity of each entity's environment, the number of types of systems that are required to be evaluated, and the functions of such systems.

---
**Control objectives:**10.4
**Sub-requirement:**10.4.3
**Defined Approach Requirements:**Exceptions and anomalies identified during the review process are addressed.
**Defined Approach Testing Procedures:**
- "10.4.3.a": Examine security policies and procedures to verify that processes are defined for addressing exceptions and anomalies identified during the review process.
- "10.4.3.b": Observe processes and interview personnel to verify that, when exceptions and anomalies are identified, they are addressed. 10.5 Audit log history is retained and available for analysis.
**Customized Approach Objective:**Suspicious or anomalous activities are addressed.
**Guidance - Purpose:**If exceptions and anomalies identified during the log-review process are not investigated, the entity may be unaware of unauthorized and potentially malicious activities occurring within their network.
**Guidance - Good Practice:**Entities should consider how to address the following when developing their processes for defining and managing exceptions and anomalies:
• How log review activities are recorded,
• How to rank and prioritize exceptions and anomalies,
• What procedures should be in place to report and escalate exceptions and anomalies, and
• Who is responsible for investigating and for any remediation tasks.

================

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

================

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

================

### A. Tài liệu gốc của Requirement 10

### B. Summary Overview của Control Objective 10.7
Tài liệu này mô tả chi tiết **Control Objective 10.7** của **Requirement 10** trong **PCI-DSS v4.0.1**, tập trung vào việc phát hiện và xử lý sự cố liên quan đến các kiểm soát bảo mật quan trọng.
Mục tiêu chính là đảm bảo các failure của critical security control systems được phát hiện, cảnh báo và xử lý kịp thời nhằm giảm thiểu rủi ro bảo mật.
Gồm 3 sub-requirement chính:
- 10.7.1: Phát hiện failure (service provider)
- 10.7.2: Phát hiện failure (áp dụng chung)
- 10.7.3: Xử lý failure
Áp dụng cho tất cả critical security control systems trong môi trường (tùy theo phạm vi entity/service provider).

### C. Key Points của Control Objective 10.7
- **Phạm vi áp dụng:**Tất cả critical security control systems (firewall, IDS/IPS, FIM, logging…)
- **Trách nhiệm:** Tài liệu hóa và triển khai quy trình phát hiện và xử lý failure
- **Phát hiện sự cố:** Phải detect và alert khi control không hoạt động
- **Phạm vi kiểm soát:** Bao gồm network security, access control, logging, anti-malware…
- **Xử lý sự cố:**Phải restore, phân tích nguyên nhân và khắc phục
- **Phòng ngừa:** Triển khai biện pháp để tránh lặp lại

### D. Deep Summary của Control Objective 10.7
**Bối cảnh:**
Nếu các kiểm soát bảo mật quan trọng bị lỗi mà không được phát hiện, attacker có thể lợi dụng khoảng thời gian này để tấn công và xâm nhập hệ thống.
**Nội dung cốt lõi:**
- Phát hiện và cảnh báo ngay khi critical security control bị failure
- Bao phủ nhiều control: firewall, IDS/IPS, FIM, logging, segmentation…
- Phản ứng nhanh: khôi phục chức năng bảo mật
- Ghi nhận thời gian và nguyên nhân failure
- Xử lý các rủi ro phát sinh trong thời gian failure
- Triển khai biện pháp phòng ngừa tái diễn
- Khôi phục và tiếp tục giám sát hệ thống
**Dữ liệu đáng chú ý:**
- Failure có thể là hệ thống dừng hoạt động hoặc hoạt động sai chức năng
- Bao gồm cả automated security tools và log review mechanism
**Rủi ro / Lưu ý:**
- Không detect failure → mất hoàn toàn lớp bảo vệ
- Không alert → chậm phản ứng với sự cố
- Không xử lý triệt để → lặp lại sự cố
- Không ghi nhận nguyên nhân → không cải thiện được hệ thống

### E. Structured Output của Control Objective 10.7
**Control objectives:**10.7
**Sub-requirement:**10.7.1
**Defined Approach Requirements:**Additional requirement for service providers only: Failures of critical security control systems are detected, alerted, and addressed promptly, including but not limited to failure of the following critical security control systems:
• Network security controls.
• IDS/IPS.
• FIM.
• Anti-malware solutions.
• Physical access controls.
• Logical access controls.
• Audit logging mechanisms.
• Segmentation controls (if used).
**Defined Approach Testing Procedures:**
- "10.7.1.a": Additional testing procedure for service provider assessments only: Examine documentation to verify that processes are defined for the prompt detection and addressing of failures of critical security control systems, including but not limited to failure of all elements specified in this requirement.
- "10.7.1.b": Additional testing procedure for service provider assessments only: Observe detection and alerting processes and interview personnel to verify that failures of critical security control systems are detected and reported, and that failure of a critical security control results in the generation of an alert.
**Customized Approach Objective:** Failures in critical security control systems are promptly identified and addressed.
**Applicability Notes:**This requirement applies only when the entity being assessed is a service provider. This requirement will be superseded by Requirement 10.7.2 as of 31 March 2025.
**Guidance - Purpose:**Without formal processes to detect and alert when critical security controls fail, failures may go undetected for extended periods and provide attackers ample time to compromise system components and steal account data from the CDE.
**Guidance - Good Practice:**The specific types of failures may vary, depending on the function of the device system component and technology in use. Typical failures include a system ceasing to perform its security function or not functioning in its intended manner, such as a firewall erasing all its rules or going offline.

---
**Control objectives:**10.7
**Sub-requirement:**10.7.2
**Defined Approach Requirements:**Failures of critical security control systems are detected, alerted, and addressed promptly, including but not limited to failure of the following critical security control systems:
• Network security controls.
• IDS/IPS.
• Change-detection mechanisms.
• Anti-malware solutions.
• Physical access controls.
• Logical access controls.
• Audit logging mechanisms.
• Segmentation controls (if used).
• Audit log review mechanisms.
• Automated security testing tools (if used).
**Defined Approach Testing Procedures:**
- "10.7.2.a": Examine documentation to verify that processes are defined for the prompt detection and addressing of failures of critical security control systems, including but not limited to failure of all elements specified in this requirement.
- "10.7.2.b": Observe detection and alerting processes and interview personnel to verify that failures of critical security control systems are detected and reported, and that failure of a critical security control results in the generation of an alert.
**Customized Approach Objective:**Failures in critical security control systems are promptly identified and addressed.
**Applicability Notes:**This requirement applies to all entities, including service providers, and will supersede Requirement 10.7.1 as of 31 March 2025. It includes two additional critical security control systems not in Requirement 10.7.1. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Without formal processes to detect and alert when critical security controls fail, failures may go undetected for extended periods and provide attackers ample time to compromise system components and steal account data from the CDE.
**Guidance - Good Practice:**The specific types of failures may vary, depending on the function of the device system component and technology in use. However, typical failures include a system no longer performing its security function or not functioning in its intended manner-for example, a firewall erasing its rules or going offline.

---
**Control objectives:**10.7
**Sub-requirement:**10.7.3
**Defined Approach Requirements:**Failures of any critical security control systems are responded to promptly, including but not limited to:
• Restoring security functions.
• Identifying and documenting the duration (date and time from start to end) of the security failure.
• Identifying and documenting the cause(s) of failure and documenting required remediation.
• Identifying and addressing any security issues that arose during the failure.
• Determining whether further actions are required as a result of the security failure.
• Implementing controls to prevent the cause of failure from reoccurring.
• Resuming monitoring of security controls.
**Defined Approach Testing Procedures:**
- "10.7.3.a": Examine documentation and interview personnel to verify that processes are defined and implemented to respond to a failure of any critical security control system and include at least all elements specified in this requirement.
- "10.7.3.b": Examine records to verify that failures of critical security control systems are documented to include:
• Identification of cause(s) of the failure.
• Duration (date and time start and end) of the security failure.
• Details of the remediation required to address the root cause.
**Customized Approach Objective:**Failures of critical security control systems are analyzed, contained, and resolved, and security controls restored to minimize impact. Resulting security issues are addressed, and measures taken to prevent reoccurrence.
**Applicability Notes:** This requirement applies only when the entity being assessed is a service provider until 31 March 2025, after which this requirement will apply to all entities. This is a current v3.2.1 requirement that applies to service providers only. However, this requirement is a best practice for all other entities until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**If alerts from failures of critical security control systems are not responded to quickly and effectively, attackers may use this time to insert malicious software, gain control of a system, or steal data from the entity's environment.
**Guidance - Good Practice:**Documented evidence (for example, records within a problem management system) should provide support that processes and procedures are in place to respond to security failures. In addition, personnel should be aware of their responsibilities in the event of a failure. Actions and responses to the failure should be captured in the documented evidence.