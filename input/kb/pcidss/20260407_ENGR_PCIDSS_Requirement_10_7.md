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