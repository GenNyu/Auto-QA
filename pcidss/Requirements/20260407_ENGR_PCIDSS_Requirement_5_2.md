### A. Tài liệu gốc của Requirement 5

### B. Summary Overview của Control Objective 5.2
Tài liệu này mô tả chi tiết **Control Objective 5.2 **của **Requirement 5** trong **PCI-DSS v4.0.1**, tập trung vào việc phòng ngừa, phát hiện và xử lý mã độc trên hệ thống.
Mục tiêu chính là đảm bảo hệ thống được bảo vệ khỏi malware thông qua việc triển khai anti-malware, phát hiện và xử lý các mối đe dọa, đồng thời đánh giá liên tục các hệ thống không áp dụng bảo vệ.
Gồm 3 sub-requirement chính:
- 5.2.1: Triển khai anti-malware
- 5.2.2: Khả năng phát hiện và xử lý malware
- 5.2.3: Đánh giá hệ thống không có anti-malware
Áp dụng cho tất cả system components trong phạm vi, bao gồm cả các hệ thống được xác định không có nguy cơ malware.

### C. Key Points của Control Objective 5.2
- **Phạm vi áp dụng:**Tất cả system components trong môi trường
- **Trách nhiệm:** Tài liệu hóa, triển khai và duy trì anti-malware
- **Triển khai bảo vệ:**Phải cài đặt anti-malware trừ khi có đánh giá chứng minh không có rủi ro
- **Khả năng kiểm soát:**Anti-malware phải detect, block hoặc remove malware
- **Đánh giá định kỳ:**Các hệ thống không có anti-malware phải được đánh giá lại
- **Quản lý rủi ro:**Phải theo dõi evolving malware threats

### D. Deep Summary của Control Objective 5.2
**Bối cảnh:**
Malware liên tục phát triển và khai thác các lỗ hổng mới. Nếu không có cơ chế phòng chống phù hợp, hệ thống có thể bị compromise và trở thành điểm tấn công.
**Nội dung cốt lõi:**
- Triển khai anti-malware trên tất cả hệ thống có rủi ro
- Anti-malware phải có khả năng detect, block và remove malware
- Cho phép ngoại lệ nhưng phải có đánh giá chứng minh không có rủi ro
- Thực hiện đánh giá định kỳ cho các hệ thống không có anti-malware
- Theo dõi xu hướng malware và cập nhật kiểm soát phù hợp
**Dữ liệu đáng chú ý:**
- Malware bao gồm virus, worm, ransomware, spyware, keylogger…
- Có thể sử dụng nhiều lớp bảo vệ (endpoint, network, behavior-based)
**Rủi ro / Lưu ý:**
- Không triển khai anti-malware → hệ thống dễ bị tấn công
- Anti-malware không cập nhật → không phát hiện malware mới
- Đánh giá sai hệ thống "không có rủi ro" → tạo lỗ hổng lớn
- Không theo dõi threat landscape → kiểm soát lỗi thời

### E. Structured Output của Control Objective 5.2
**Control objectives:**5.2
**Sub-requirement:**5.2.1
**Defined Approach Requirements:**An anti-malware solution(s) is deployed on all system components, except for those system components identified in periodic evaluations per Requirement 5.2.3 that concludes the system components are not at risk from malware.
**Defined Approach Testing Procedures:**
- "5.2.1.a": Examine system components to verify that an anti-malware solution(s) is deployed on all system components, except for those determined to not be at risk from malware based on periodic evaluations per Requirement 5.2.3.
- "5.2.1.b": For any system components without an anti-malware solution, examine the periodic evaluations to verify the component was evaluated and the evaluation concludes that the component is not at risk from malware.
**Customized Approach Objective:**Automated mechanisms are implemented to prevent systems from becoming an attack vector for malware.
**Guidance - Purpose:**There is a constant stream of attacks targeting newly discovered vulnerabilities in systems previously regarded as secure. Without an anti- malware solution that is updated regularly, new forms of malware can be used to attack systems, disable a network, or compromise data.
**Guidance - Good Practice:**It is beneficial for entities to be aware of "zero-day" attacks (those that exploit a previously unknown vulnerability) and consider solutions that focus on behavioral characteristics and will alert and react to unexpected behavior.
**Guidance - Definitions:**System components known to be affected by malware have active malware exploits available in the real world (not only theoretical exploits).

---
**Control objectives:**5.2
**Sub-requirement:**5.2.2
**Defined Approach Requirements:**The deployed anti-malware solution(s):
• Detects all known types of malware.
• Removes, blocks, or contains all known types of malware. Customized Approach Objective
**Defined Approach Testing Procedures:**Examine vendor documentation and configurations of the anti-malware solution(s) to verify that the solution:
• Detects all known types of malware.
• Removes, blocks, or contains all known types of malware.
**Guidance - Purpose:**It is important to protect against all types and forms of malware to prevent unauthorized access.
**Guidance - Good Practice:**Anti-malware solutions may include a combination of network-based controls, host-based controls, and endpoint security solutions. In addition to signature- based tools, capabilities used by modern anti- malware solutions include sandboxing, privilege escalation controls, and machine learning. Solution techniques include preventing malware from getting into the network and removing or containing malware that does get into the network.
**Guidance - Examples:**Types of malware include, but are not limited to, viruses, Trojans, worms, spyware, ransomware, keyloggers, rootkits, malicious code, scripts, and links.

---
**Control objectives:**5.2
**Sub-requirement:**5.2.3
**Defined Approach Requirements:**Any system components that are not at risk for malware are evaluated periodically to include the following:
• A documented list of all system components not at risk for malware.
• Identification and evaluation of evolving malware threats for those system components.
• Confirmation whether such system components continue to not require anti-malware protection.
**Defined Approach Testing Procedures:**
- "5.2.3.a": Examine documented policies and procedures to verify that a process is defined for periodic evaluations of any system components that are not at risk for malware that includes all elements specified in this requirement.
- "5.2.3.b": Interview personnel to verify that the evaluations include all elements specified in this requirement.
- "5.2.3.c": Examine the list of system components identified as not at risk of malware and compare to the system components without an anti-malware solution deployed per Requirement 5.2.1 to verify that the system components match for both requirements.
**Customized Approach Objective:**The entity maintains awareness of evolving malware threats to ensure that any systems not protected from malware are not at risk of infection.
**Applicability Notes:**System components covered by this requirement are those for which there is no anti-malware solution deployed per Requirement 5.2.1.
**Guidance - Purpose:**Certain systems, at a given point in time, may not currently be commonly targeted or affected by malware. However, industry trends for malware can change quickly, so it is important for organizations to be aware of new malware that might affect their systems-for example, by monitoring vendor security notices and anti-malware forums to determine whether its systems might be coming under threat from new and evolving malware.
**Guidance - Good Practice:**If an entity determines that a particular system is not susceptible to any malware, the determination should be supported by industry evidence, vendor resources, and best practices. The following steps can help entities during their periodic evaluations:
• Identification of all system types previously determined to not require malware protection.
• Review of industry vulnerability alerts and notices to determine if new threats exist for any identified system.
• A documented conclusion about whether the system types remain not susceptible to malware.
• A strategy to add malware protection for any system types for which malware protection has become necessary.
Trends in malware should be included in the identification of new security vulnerabilities at Requirement 6.3.1, and methods to address new trends should be incorporated into the entity's configuration standards and protection mechanisms as needed.

---
**Control objectives:**5.2
**Sub-requirement:**5.2.3.1
**Defined Approach Requirements:**The frequency of periodic evaluations of system components identified as not at risk for malware is defined in the entity's targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1.
**Defined Approach Testing Procedures:**
- "5.2.3.1.a": Examine the entity's targeted risk analysis for the frequency of periodic evaluations of system components identified as not at risk for malware to verify the risk analysis was performed in accordance with all elements specified in Requirement 12.3.1.
- "5.2.3.1.b": Examine documented results of periodic evaluations of system components identified as not at risk for malware and interview personnel to verify that evaluations are performed at the frequency defined in the entity's targeted risk analysis performed for this requirement.
**Customized Approach Objective:**Systems not known to be at risk from malware are re-evaluated at a frequency that addresses the entity's risk.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Entities determine the optimum period to undertake the evaluation based on criteria such as the complexity of each entity's environment and the number of types of systems that are required to be evaluated.