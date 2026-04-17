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