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