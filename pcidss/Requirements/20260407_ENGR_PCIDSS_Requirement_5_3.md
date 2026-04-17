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