### A. Tài liệu gốc của Requirement 5

### B. Summary Overview của Control Objective 5.1
Tài liệu này mô tả chi tiết **Control Objective 5.1** của **Requirement 5** trong **PCI-DSS v4.0.1**, tập trung vào việc thiết lập và duy trì chính sách, quy trình và phân công trách nhiệm liên quan đến phòng chống mã độc.
Mục tiêu chính là đảm bảo các chính sách, quy trình và vai trò trách nhiệm được tài liệu hóa, cập nhật, áp dụng thực tế và được hiểu rõ bởi các bên liên quan trong hoạt động phòng chống malware.
Gồm 2 sub-requirement chính:
- 5.1.1: Quản lý chính sách và quy trình
- 5.1.2: Phân công vai trò và trách nhiệm
Áp dụng cho toàn bộ tổ chức và nhân sự tham gia vào các hoạt động kiểm soát malware theo Requirement 5.

### C. Key Points của Control Objective 5.1
- **Phạm vi áp dụng:**Tất cả chính sách, quy trình và nhân sự liên quan kiểm soát malware
- **Trách nhiệm:**Phân rõ vai trò, đảm bảo nhân sự hiểu và thực hiện đúng
- **Quản lý tài liệu:** Chính sách và quy trình phải được tài liệu hóa, cập nhật và phổ biến
- **Áp dụng thực tế:**Quy trình phải được triển khai và sử dụng thực tế
- **Truyền thông:**Đảm bảo các bên liên quan được phổ biến và hiểu nội dung

### D. Deep Summary của Control Objective 5.1
**Bối cảnh:**
Nếu chính sách và trách nhiệm không rõ ràng, các biện pháp phòng chống malware có thể không được triển khai hoặc vận hành hiệu quả.
**Nội dung cốt lõi:**
- Tài liệu hóa chính sách và quy trình liên quan đến kiểm soát malware
- Cập nhật kịp thời khi có thay đổi về hệ thống hoặc mối đe dọa
- Đảm bảo quy trình được áp dụng thực tế trong vận hành
- Phổ biến đến tất cả nhân sự liên quan
- Phân rõ vai trò và trách nhiệm cho từng hoạt động
**Dữ liệu đáng chú ý:**
- Chính sách và quy trình phải "in use" và "known to all affected parties"
- Có thể sử dụng RACI matrix để quản lý trách nhiệm
**Rủi ro / Lưu ý:**
- Chính sách không cập nhật → không phản ánh rủi ro malware mới
- Quy trình không được thực thi → hệ thống dễ bị nhiễm mã độc
- Nhân sự không rõ trách nhiệm → bỏ sót kiểm soát
- Thiếu phân công rõ ràng → không có accountability

### E. Structured Output của Control Objective 5.1
**Control objectives:**5.1
**Sub-requirement:**5.1.1
**Defined Approach Requirements:**All security policies and operational procedures that are identified in Requirement 5 are:
• Documented.
• Kept up to date.
• In use.
• Known to all affected parties. Customized Approach Objective Expectations, controls, and oversight for meeting activities within Requirement 5 are defined and adhered to by affected personnel. All supporting
**Defined Approach Testing Procedures:**Examine documentation and interview personnel to verify that security policies and operational procedures identified in Requirement 5 are managed in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Expectations, controls, and oversight for meeting activities within Requirement 5 are defined and adhered to by affected personnel. All supporting
**Guidance - Purpose:**Requirement 5.1.1 is about effectively managing and maintaining the various policies and procedures specified throughout Requirement 5. While it is important to define the specific policies or procedures called out in Requirement 5, it is equally important to ensure they are properly documented, maintained, and disseminated.
**Guidance - Good Practice:**It is important to update policies and procedures as needed to address changes in processes, technologies, and business objectives. For this reason, consider updating these documents as soon as possible after a change occurs and not only on a periodic cycle.
**Guidance - Definitions:**Security policies define the entity's security objectives and principles. Operational procedures describe how to perform activities, and define the controls, methods, and processes that are followed to achieve the desired result in a consistent manner and in accordance with policy objectives.

---
**Control objectives:**5.1
**Sub-requirement:**5.1.2
**Defined Approach Requirements:**Roles and responsibilities for performing activities in Requirement 5 are documented, assigned, and understood.
**Defined Approach Testing Procedures:**
- "5.1.2.a": Examine documentation to verify that descriptions of roles and responsibilities for performing activities in Requirement 5 are documented and assigned.
- "5.1.2.b": Interview personnel with responsibility for performing activities in Requirement 5 to verify that roles and responsibilities are assigned as documented and are understood.
**Customized Approach Objective:**Day-to-day responsibilities for performing all the activities in Requirement 5 are allocated. Personnel are accountable for successful, continuous operation of these requirements. 5.2 Malicious software (malware) is prevented, or detected and addressed. 5.2 Malicious software (malware) is prevented, or detected and addressed.
**Guidance - Purpose:**If roles and responsibilities are not formally assigned, networks and systems may not be properly protected from malware.
**Guidance - Good Practice:**Roles and responsibilities may be documented within policies and procedures or maintained within separate documents. As part of communicating roles and responsibilities, entities can consider having personnel acknowledge their acceptance and understanding of their assigned roles and responsibilities.
**Guidance - Examples:**A method to document roles and responsibilities is a responsibility assignment matrix that includes who is responsible, accountable, consulted, and informed (also called a RACI matrix).

================

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

================

### A. Tài liệu gốc của Requirement 5

### B. Summary Overview của Control Objective 5.3
Tài liệu này mô tả chi tiết **Control Objective 5.3 **của **Requirement 5 **trong **PCI-DSS v4.0.1**, tập trung vào việc vận hành, duy trì và kiểm soát hiệu quả các cơ chế anti-malware.
Mục tiêu chính là đảm bảo các giải pháp anti-malware luôn được cập nhật, hoạt động liên tục, có khả năng phát hiện kịp thời và không bị vô hiệu hóa trái phép.
Gồm 4 sub-requirement chính:
- 5.3.1: Cập nhật anti-malware tự động
- 5.3.2: Quét và phát hiện malware
- 5.3.3: Kiểm soát malware qua removable media
- 5.3.4: Ghi log anti-malware
- 5.3.5: Ngăn vô hiệu hóa anti-malware
Áp dụng cho tất cả hệ thống có triển khai anti-malware trong môi trường.

### C. Key Points của Control Objective 5.3
- **Phạm vi áp dụng:**Tất cả hệ thống có anti-malware
- **Trách nhiệm:**Đảm bảo anti-malware được cập nhật, vận hành và kiểm soát
- **Cập nhật:**Anti-malware phải được cập nhật tự động từ nguồn tin cậy
- **Phát hiện:**Phải có cơ chế scan định kỳ hoặc real-time/behavior-based
- **Kiểm soát media:**Phải kiểm soát malware từ thiết bị lưu trữ rời
- **Logging:**Phải bật và lưu log hoạt động anti-malware
- **Kiểm soát thay đổi:**Không cho phép user tự ý disable hoặc chỉnh sửa

### D. Deep Summary của Control Objective 5.3
**Bối cảnh:**
Malware liên tục thay đổi và có thể vượt qua các cơ chế bảo vệ nếu anti-malware không được cập nhật hoặc vận hành đúng cách.
**Nội dung cốt lõi:**
- Cập nhật anti-malware tự động để nhận signature và engine mới nhất
- Thực hiện quét định kỳ, real-time hoặc phân tích hành vi
- Kiểm soát malware từ removable media (USB, external devices)
- Ghi log đầy đủ hoạt động để theo dõi và điều tra
- Ngăn việc vô hiệu hóa anti-malware trái phép
**Dữ liệu đáng chú ý:**
- Có thể kết hợp periodic scan + real-time scan để tăng hiệu quả
- Log phải được lưu trữ theo Requirement 10.5.1
**Rủi ro / Lưu ý:**
- Không cập nhật → không phát hiện malware mới
- Không scan hoặc chỉ scan định kỳ → bỏ sót malware runtime
- USB/removable media → nguồn lây nhiễm phổ biến
- Anti-malware bị disable → mất lớp bảo vệ quan trọng
- Thiếu log → không điều tra được sự cố malware

### E. Structured Output của Control Objective 5.3
**Control objectives:**5.3
**Sub-requirement:**5.3.1
**Defined Approach Requirements:**The anti-malware solution(s) is kept current via automatic updates.
**Defined Approach Testing Procedures:**
- "5.3.1.a": Examine anti-malware solution(s) configurations, including any master installation of the software, to verify the solution is configured to perform automatic updates.
- "5.3.1.b": Examine system components and logs, to verify that the anti-malware solution(s) and
**Customized Approach Objective:**Anti-malware mechanisms can detect and address
**Guidance - Purpose:**For an anti-malware solution to remain effective, it needs to have the latest security updates, signatures, threat analysis engines, and any other malware protections on which the solution relies. Having an automated update process avoids burdening end users with responsibility for manually installing updates and provides greater assurance that anti-malware protection mechanisms are updated as quickly as possible after an update is released.
**Guidance - Good Practice:**Anti-malware mechanisms should be updated via a trusted source as soon as possible after an update is available. Using a trusted common source to distribute updates to end-user systems helps ensure the integrity and consistency of the solution architecture. Updates may be automatically downloaded to a central location-for example, to allow for testing- prior to being deployed to individual system components.

---
**Control objectives:**5.3
**Sub-requirement:**5.3.2
**Defined Approach Requirements:**The anti-malware solution(s):
• Performs periodic scans and active or real-time scans. OR
• Performs continuous behavioral analysis of systems or processes.
**Defined Approach Testing Procedures:**
- "5.3.2.a": Examine anti-malware solution(s) configurations, including any master installation of the software, to verify the solution(s) is configured to perform at least one of the elements specified in this requirement.
- "5.3.2.b": Examine system components, including all operating system types identified as at risk for malware, to verify the solution(s) is enabled in accordance with at least one of the elements specified in this requirement.
- "5.3.2.c": Examine logs and scan results to verify that the solution(s) is enabled in accordance with at least one of the elements specified in this requirement.
**Customized Approach Objective:**Malware cannot complete execution.
**Guidance - Purpose:**Periodic scans can identify malware that is present, but currently inactive, within the environment. Some malware, such as zero-day malware, can enter an environment before the scan solution is capable of detecting it. Performing regular periodic scans or continuous behavioral analysis of systems or processes helps ensure that previously undetectable malware can be identified, removed, and investigated to determine how it gained access to the environment.
**Guidance - Good Practice:**Using a combination of periodic scans (scheduled and on-demand) and active, real-time (on-access) scanning helps ensure that malware residing in both static and dynamic elements of the CDE is addressed. Users should also be able to run on- demand scans on their systems if suspicious activity is detected - this can be useful in the early detection of malware. Scans should include the entire file system, including all disks, memory, and start-up files and boot records (at system restart) to detect all malware upon file execution, including any software that may be resident on a system but not currently active. Scan scope should include all systems and software in the CDE, including those that are often overlooked such as email servers, web browsers, and instant messaging software.
**Guidance - Definitions:**Active, or real-time, scanning checks files for malware upon any attempt to open, close, rename, or otherwise interact with a file, preventing the malware from being activated.

---
**Control objectives:**5.3
**Sub-requirement:**5.3.2.1
**Defined Approach Requirements:**If periodic malware scans are performed to meet Requirement 5.3.2, the frequency of scans is defined in the entity's targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1.
**Defined Approach Testing Procedures:**
- "5.3.2.1.a": Examine the entity's targeted risk analysis for the frequency of periodic malware scans to verify the risk analysis was performed in accordance with all elements specified in Requirement 12.3.1.
- "5.3.2.1.b": Examine documented results of periodic malware scans and interview personnel to verify scans are performed at the frequency defined in the entity's targeted risk analysis performed for this requirement.
**Customized Approach Objective:**Scans by the malware solution are performed at a frequency that addresses the entity's risk.
**Applicability Notes:**This requirement applies to entities conducting periodic malware scans to meet Requirement 5.3.2. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Entities can determine the optimum period to undertake periodic scans based on their own assessment of the risks posed to their environments.

---
**Control objectives:**5.3
**Sub-requirement:**5.3.3
**Defined Approach Requirements:**For removable electronic media, the anti- malware solution(s):
**Defined Approach Testing Procedures:**
- "5.3.3.a": Examine anti-malware solution( s) configurations to verify that, for removable electronic media, the solution is configured to perform at least one of the elements specified in this requirement.
- "5.3.3.b": Examine system components with removable electronic media connected to verify that the solution(s) is enabled in accordance with at least one of the elements as specified in this requirement.
- "5.3.3.c": Examine logs and scan results to verify that the solution(s) is enabled in accordance with at least one of the elements specified in this requirement.
**Customized Approach Objective:**Malware cannot be introduced to system components via external removable media.
**Applicability Notes:**This requirement is a best practice 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Portable media devices are often overlooked as an entry method for malware. Attackers will often pre- load malware onto portable devices such as USB and flash drives; connecting an infected device to a computer then triggers the malware, introducing new threats within the environment.

---
**Control objectives:**5.3
**Sub-requirement:**5.3.4
**Defined Approach Requirements:**Audit logs for the anti-malware solution(s) are enabled and retained in accordance with Requirement 10.5.1.
**Defined Approach Testing Procedures:**Examine anti-malware solution(s) configurations to verify logs are enabled and retained in accordance with Requirement 10.5.1.
**Customized Approach Objective:**Historical records of anti-malware actions are immediately available and retained for at least 12 months.
**Guidance - Purpose:**It is important to track the effectiveness of the anti- malware mechanisms-for example, by confirming that updates and scans are being performed as expected, and that malware is identified and addressed. Audit logs also allow an entity to determine how malware entered the environment and track its activity when inside the entity's network.

---
**Control objectives:**5.3
**Sub-requirement:**5.3.5
**Defined Approach Requirements:**Anti-malware mechanisms cannot be disabled or altered by users, unless specifically documented, and authorized by management on a case-by-case basis for a limited time period.
**Defined Approach Testing Procedures:**
- "5.3.5.a": Examine anti-malware configurations, to verify that the anti-malware mechanisms cannot be disabled or altered by users.
- "5.3.5.b": Interview responsible personnel and observe processes to verify that any requests to disable or alter anti-malware mechanisms are specifically documented and authorized by management on a case-by-case basis for a limited time period.
**Customized Approach Objective:**Anti-malware mechanisms cannot be modified by
unauthorized personnel.
**Applicability Notes:**Anti-malware solutions may be temporarily disabled only if there is a legitimate technical need, as authorized by management on a case-by-case basis. If anti-malware protection needs to be disabled for a specific purpose, it must be formally authorized. Additional security measures may also need to be implemented for the period during which anti-malware protection is not active. 5.4 Anti-phishing mechanisms protect users against phishing attacks. 5.4 Anti-phishing mechanisms protect users against phishing attacks.
**Guidance - Purpose:**It is important that defensive mechanisms are always running so that malware is detected in real time. Ad-hoc starting and stopping of anti-malware solutions could allow malware to propagate unchecked and undetected.
**Guidance - Good Practice:**Where there is a legitimate need to temporarily disable a system's anti-malware protection-for example, to support a specific maintenance activity or investigation of a technical problem-the reason for taking such action should be understood and approved by an appropriate management representative. Any disabling or altering of anti- malware mechanisms, including on administrators' own devices, should be performed by authorized personnel. It is recognized that administrators have privileges that may allow them to disable anti- malware on their own computers, but there should be alerting mechanisms in place when such software is disabled and then follow up that occurs to ensure correct processes were followed.
**Guidance - Examples:**Additional security measures that may need to be implemented for the period during which anti- malware protection is not active include disconnecting the unprotected system from the Internet while the anti-malware protection is disabled and running a full scan once it is re- enabled.

================

### A. Tài liệu gốc của Requirement 5

### B. Summary Overview của Control Objective 5.4
Tài liệu này mô tả chi tiết **Control Objective 5.4** của **Requirement 5** trong **PCI-DSS v4.0.1**, tập trung vào việc phát hiện và bảo vệ nhân sự khỏi các cuộc tấn công phishing.
Mục tiêu chính là đảm bảo có các quy trình và cơ chế kỹ thuật để giảm thiểu rủi ro phishing thông qua việc phát hiện, ngăn chặn và bảo vệ người dùng.
Gồm 1 sub-requirement chính:
- 5.4.1: Phát hiện và bảo vệ khỏi phishing
Áp dụng cho toàn bộ nhân sự có quyền truy cập vào hệ thống trong phạm vi PCI DSS.

### C. Key Points của Control Objective 5.4
- **Phạm vi áp dụng:**Nhân sự có truy cập vào hệ thống trong scope
- **Trách nhiệm:**Tài liệu hóa và triển khai cơ chế chống phishing
- **Kiểm soát kỹ thuật:** Áp dụng cơ chế tự động để detect và block phishing
- **Bảo vệ người dùng:** Giảm phụ thuộc vào đánh giá thủ công của nhân sự
- **Cơ chế bổ trợ:**Có thể sử dụng DMARC, SPF, DKIM, email filtering, link protection

### D. Deep Summary của Control Objective 5.4
**Bối cảnh:**
Phishing là một trong những phương thức tấn công phổ biến nhằm đánh cắp thông tin đăng nhập và dữ liệu nhạy cảm thông qua yếu tố con người.
**Nội dung cốt lõi:**
- Triển khai cơ chế phát hiện phishing (email filtering, anti-spoofing)
- Áp dụng kiểm soát kỹ thuật để ngăn phishing trước khi đến người dùng
- Giảm phụ thuộc vào việc người dùng tự nhận diện phishing
- Có thể kết hợp nhiều cơ chế: DMARC, SPF, DKIM, anti-malware, link scanning
**Dữ liệu đáng chú ý:**
- Phishing là hình thức social engineering giả mạo nguồn tin cậy
- Anti-phishing không thay thế cho security awareness training
**Rủi ro / Lưu ý:**
- Không có cơ chế kỹ thuật → phụ thuộc hoàn toàn vào người dùng
- Email spoofing → dễ đánh lừa người dùng nếu không kiểm soát domain
- Click link độc hại → dẫn đến malware hoặc lộ thông tin
- Nhầm lẫn với training → không đáp ứng đầy đủ yêu cầu PCI DSS

### E. Structured Output của Control Objective 5.4
**Control objectives:**5.4
**Sub-requirement:**5.4.1
**Defined Approach Requirements:**Processes and automated mechanisms are in place to detect and protect personnel against phishing attacks.
**Defined Approach Testing Procedures:**Observe implemented processes and examine mechanisms to verify controls are in place to detect and protect personnel against phishing attacks.
**Customized Approach Objective:**Mechanisms are in place to protect against and mitigate risk posed by phishing attacks.
**Applicability Notes:**The focus of this requirement is on protecting personnel with access to system components in- scope for PCI DSS. Meeting this requirement for technical and automated controls to detect and protect personnel against phishing is not the same as Requirement 12.6.3.1 for security awareness training. Meeting this requirement does not also meet the requirement for providing personnel with security awareness training, and vice versa. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Technical controls can limit the number of occasions personnel have to evaluate the veracity of a communication and can also limit the effects of individual responses to phishing.
**Guidance - Good Practice:**When developing anti-phishing controls, entities are encouraged to consider a combination of approaches. For example, using anti-spoofing controls such as Domain-based Message Authentication, Reporting & Conformance (DMARC), Sender Policy Framework (SPF), and Domain Keys Identified Mail (DKIM) will help stop phishers from spoofing the entity's domain and impersonating personnel. The deployment of technologies for blocking phishing emails and malware before they reach personnel, such as link scrubbers and server-side anti-malware, can reduce incidents and decrease the time required by personnel to check and report phishing attacks. Additionally, training personnel to recognize and report phishing emails can allow similar emails to be identified and permit them to be removed before being opened. It is recommended (but not required) that anti- phishing controls are applied across an entity's entire organization.
**Guidance - Definitions:**Phishing is a form of social engineering and describes the different methods used by attackers to trick personnel into disclosing sensitive information, such as user account names and passwords, and account data. Attackers will typically disguise themselves and attempt to appear as a genuine or trusted source, directing personnel to send an email response, click on a web link, or enter data into a compromised website. Mechanisms that can detect and prevent phishing attempts are often included in anti-malware solutions.
**Guidance - Further Information:**See the following for more information about phishing: National Cyber Security Centre - Phishing Attacks: Defending your Organization . US Cybersecurity & Infrastructure Security Agency - Report Phishing Sites.