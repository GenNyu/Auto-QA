### A. Tài liệu gốc của Requirement 12

### B. Summary Overview của Control Objective 12.6
Tài liệu này mô tả chi tiết **Control Objective 12.6** của **Requirement 12 **trong **PCI-DSS v4.0.1**, tập trung vào việc xây dựng và duy trì chương trình đào tạo nhận thức an toàn thông tin cho nhân sự.
Mục tiêu chính là đảm bảo tất cả nhân sự hiểu rõ rủi ro bảo mật, trách nhiệm của mình và cách bảo vệ cardholder data trong quá trình làm việc.
Gồm 3 sub-requirement chính:
- 12.6.1: Thiết lập security awareness program
- 12.6.2: Review và cập nhật chương trình
- 12.6.3: Đào tạo và xác nhận nhận thức của nhân sự
Áp dụng cho toàn bộ nhân sự trong tổ chức.

### C. Key Points của Control Objective 12.6
- **Phạm vi áp dụng:**Tất cả nhân sự trong tổ chức
- **Trách nhiệm:**Tài liệu hóa và triển khai chương trình đào tạo nhận thức
- **Đào tạo:**Thực hiện khi onboard và ít nhất hàng năm
- **Nội dung:**Bao gồm threat, phishing, social engineering và acceptable use
- **Truyền thông:**Sử dụng nhiều hình thức (training, email, poster…)
- **Xác nhận:**Nhân sự phải xác nhận đã hiểu policy
- **Cập nhật:**Chương trình phải review và cập nhật định kỳ

### D. Deep Summary của Control Objective 12.6
**Bối cảnh:**
Nhân sự là một trong những điểm yếu lớn nhất trong bảo mật, đặc biệt với các tấn công như phishing và social engineering.
**Nội dung cốt lõi:**
- Thiết lập chương trình security awareness cho toàn bộ nhân sự
- Đào tạo khi tuyển dụng và định kỳ hàng năm
- Cập nhật nội dung theo threat landscape mới
- Bao gồm nhận diện phishing, social engineering và sử dụng công nghệ đúng cách
- Sử dụng nhiều phương thức truyền thông để tăng hiệu quả
- Yêu cầu nhân sự xác nhận đã đọc và hiểu policy
- Có cơ chế hỗ trợ và hướng dẫn khi cần
**Dữ liệu đáng chú ý:**
- Training tối thiểu: khi onboarding + mỗi 12 tháng
- Bao gồm nội dung phishing, social engineering và acceptable use
**Rủi ro / Lưu ý:**
- Nhân sự không được đào tạo → dễ bị tấn công
- Không cập nhật nội dung → không theo kịp threat mới
- Không xác nhận → không đảm bảo hiểu policy
- Đào tạo không hiệu quả → không thay đổi hành vi bảo mật

### E. Structured Output của Control Objective 12.6
**Control objectives:**12.6
**Sub-requirement:**12.6.1
**Defined Approach Requirements:**A formal security awareness program is implemented to make all personnel aware of the entity's information security policy and procedures, and their role in protecting the cardholder data.
**Defined Approach Testing Procedures:**Examine the security awareness program to verify it provides awareness to all personnel about the entity's information security policy and procedures, and personnel's role in protecting the cardholder data.
**Customized Approach Objective:**Personnel are knowledgeable about the threat landscape, their responsibility for the operation of relevant security controls, and are able to access assistance and guidance when required.
**Guidance - Purpose:**If personnel are not educated about their company's information security policies and procedures and their own security responsibilities, security safeguards and processes that have been implemented may become ineffective through unintentional errors or intentional actions.

---
**Control objectives:**12.6
**Sub-requirement:**12.6.2
**Defined Approach Requirements:**The security awareness program is:
• Reviewed at least once every 12 months, and
• Updated as needed to address any new threats and vulnerabilities that may impact the security of the entity's cardholder data and/or sensitive authentication data, or the information provided to personnel about their role in protecting cardholder data.
**Defined Approach Testing Procedures:**Examine security awareness program content, evidence of reviews, and interview personnel to verify that the security awareness program is in accordance with all elements specified in this requirement.
**Customized Approach Objective:**The content of security awareness material is reviewed and updated periodically.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**The threat environment and an entity's defenses are not static. As such, the security awareness program materials must be updated as frequently as needed to ensure that the education received by personnel is up to date and represents the current threat environment.

---
**Control objectives:**12.6
**Sub-requirement:**12.6.3
**Defined Approach Requirements:**Personnel receive security awareness training as follows:
• Upon hire and at least once every 12 months.
• Multiple methods of communication are used.
• Personnel acknowledge at least once every 12 months that they have read and understood the information security policy and procedures.
**Defined Approach Testing Procedures:**
- "12.6.3.a": Examine security awareness program records to verify that personnel attend security awareness training upon hire and at least once every 12 months.
- "12.6.3.b": Examine security awareness program materials to verify the program includes methods of communicating awareness and multiple educating personnel.
- "12.6.3.c": Interview personnel to verify they have completed awareness training and are aware of their role in protecting cardholder data.
- "12.6.3.d": Examine security awareness program materials and personnel acknowledgments to verify that personnel acknowledge at least once every 12 months that they have read and understand the information security policy and procedures.
**Customized Approach Objective:**Personnel remain knowledgeable about the threat landscape, their responsibility for the operation of relevant security controls, and are able to access assistance and guidance when required.
**Guidance - Purpose:**Training of personnel ensures they receive the information about the importance of information security and that they understand their role in protecting the organization. Requiring an acknowledgment by personnel helps ensure that they have read and understood the security policies and procedures, and that they have made and will continue to make a commitment to comply with these policies.
**Guidance - Good Practice:**Entities may incorporate new-hire training as part of the Human Resources onboarding process. Training should outline the security-related 'dos' and 'don'ts.' Periodic refresher training reinforces key security processes and procedures that may be forgotten or bypassed. Entities should consider requiring security awareness training anytime personnel transfer into roles where they can impact the security of cardholder data and/or sensitive authentication data from roles where they did not have this impact. Methods and training content can vary, depending on personnel roles.
**Guidance - Examples:**Different methods that can be used to provide security awareness and education include posters, letters, web-based training, in-person training, team meetings, and incentives. Personnel acknowledgments may be recorded in writing or electronically.

---
**Control objectives:**12.6
**Sub-requirement:**12.6.3.1
**Defined Approach Requirements:**Security awareness training includes awareness of threats and vulnerabilities that could impact the security of cardholder data and/or sensitive authentication data, including but not limited to:
• Phishing and related attacks.
• Social engineering.
**Defined Approach Testing Procedures:**Examine security awareness training content to verify it includes all elements specified in this requirement.
**Customized Approach Objective:**Personnel are knowledgeable about their own human vulnerabilities and how threat actors will attempt to exploit such vulnerabilities. Personnel are able to access assistance and guidance when required.
**Applicability Notes:**See Requirement 5.4.1 for guidance on the difference between technical and automated controls to detect and protect users from phishing attacks, and this requirement for providing users security awareness training about phishing and social engineering. These are two separate and distinct requirements, and one is not met by implementing controls required by the other one. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Educating personnel on how to detect, react to, and report potential phishing and related attacks and social engineering attempts is essential to minimizing the probability of successful attacks.
**Guidance - Good Practice:**An effective security awareness program should include examples of phishing emails and periodic testing to determine the prevalence of personnel reporting such attacks. Training material an entity can consider for this topic include:
• How to identify phishing and other social engineering attacks.
• How to react to suspected phishing and social engineering.
• Where and how to report suspected phishing and social engineering activity.
An emphasis on reporting allows the organization to reward positive behavior, to optimize technical defenses (see Requirement 5.4.1), and to take immediate action to remove similar phishing emails that evaded technical defenses from recipient inboxes.

---
**Control objectives:**12.6
**Sub-requirement:**12.6.3.2
**Defined Approach Requirements:**Security awareness training includes awareness about the acceptable use of end-user technologies in accordance with Requirement 12.2.1.
**Defined Approach Testing Procedures:**Examine security awareness training content to verify it includes awareness about acceptable use of end-user technologies in accordance with Requirement 12.2.1.
**Customized Approach Objective:**Personnel are knowledgeable about their responsibility for the security and operation of end-user technologies and are able to access assistance and guidance when required.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**By including the key points of the acceptable use policy in regular training and the related context, personnel will understand their responsibilities and how these impact the security of an organization's systems.