### A. Tài liệu gốc của Requirement 8

### B. Summary Overview của Control Objective 8.5
Tài liệu này mô tả chi tiết **Control Objective 8.5 **của **Requirement 8 **trong** PCI-DSS v4.0.1**, tập trung vào việc cấu hình và đảm bảo tính bảo mật của hệ thống xác thực đa yếu tố (MFA).
Mục tiêu chính là đảm bảo hệ thống MFA được triển khai đúng cách, không thể bị bypass và có khả năng chống lại các hình thức tấn công như replay attack.
Gồm 1 sub-requirement chính:
- 8.5.1: Cấu hình và bảo mật hệ thống MFA
Áp dụng cho tất cả hệ thống MFA sử dụng để kiểm soát truy cập vào hệ thống và CDE.

### C. Key Points của Control Objective 8.5
- **Phạm vi áp dụng:**Tất cả hệ thống MFA trong môi trường
- **Trách nhiệm:**Tài liệu hóa và cấu hình MFA đúng chuẩn bảo mật
- **Kiểm soát MFA:**Phải sử dụng ít nhất 2 loại authentication factor khác nhau
- **Bảo mật hệ thống:**MFA phải chống replay attack
- **Kiểm soát bypass:**Không được bypass MFA trừ khi có phê duyệt đặc biệt
- **Thực thi xác thực:**Chỉ cấp quyền khi tất cả authentication factor hợp lệ

### D. Deep Summary của Control Objective 8.5
**Bối cảnh:**
MFA nếu cấu hình sai hoặc bị bypass sẽ làm mất hiệu quả bảo vệ, cho phép attacker truy cập hệ thống dù đã có nhiều lớp xác thực.
**Nội dung cốt lõi:**
- Đảm bảo MFA không bị replay attack (timestamp, OTP, session control…)
- Không cho phép bypass MFA, kể cả admin, trừ trường hợp exception có kiểm soát
- MFA phải sử dụng ≥ 2 loại yếu tố xác thực khác nhau
- Chỉ cấp quyền khi tất cả yếu tố xác thực đều thành công
**Dữ liệu đáng chú ý:**
- Replay attack là việc tái sử dụng dữ liệu xác thực hợp lệ để truy cập trái phép
- MFA không hợp lệ nếu dùng cùng loại yếu tố nhiều lần
**Rủi ro / Lưu ý:**
- MFA bị bypass → mất hoàn toàn lớp bảo vệ
- Không chống replay attack → attacker tái sử dụng session/token
- Cấu hình sai MFA → không đảm bảo security thực tế
- Không kiểm soát exception → mở lỗ hổng truy cập trái phép

### E. Structured Output của Control Objective 8.5
**Control objectives:**8.5
**Sub-requirement:**8.5.1
**Defined Approach Requirements:**MFA systems are implemented as follows:
• The MFA system is not susceptible to replay attacks.
• MFA systems cannot be bypassed by any users, including administrative users unless specifically documented, and authorized by management on an exception basis, for a limited time period.
• At least two different types of authentication factors are used.
• Success of all authentication factors is required before access is granted.
**Defined Approach Testing Procedures:**
- "8.5.1.a": Examine vendor system documentation to verify that the MFA system is not susceptible to replay attacks.
- "8.5.1.b": Examine system configurations for the MFA implementation to verify it is configured in accordance with all elements specified in this requirement.
- "8.5.1.c": Interview responsible personnel and observe processes to verify that any requests to bypass MFA are specifically documented and authorized by management on an exception basis, for a limited time period.
- "8.5.1.d": Observe personnel logging into system components in the CDE to verify that access is granted only after all authentication factors are successful.
- "8.5.1.e": Observe personnel connecting remotely from outside the entity's network to verify that access is granted only after all authentication factors are successful.
**Customized Approach Objective:**MFA systems are resistant to attack and strictly control any administrative overrides.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Poorly configured MFA systems can be bypassed by attackers. This requirement therefore addresses configuration of MFA system(s) that provide MFA for users accessing system components in the CDE.
**Guidance - Definitions:**Using one type of factor twice (for example, using two separate passwords) is not considered multi- factor authentication. A replay attack is when an attacker intercepts a valid transmission of data and then resends or redirects this communication for malicious purposes. In MFA implementations, replay attacks are typically used to gain unauthorized access by leveraging legitimate credentials.
**Guidance - Examples:**Examples of methods to help protect against replay attacks include, but are not limited to:
• Unique session identifiers and session keys
• Timestamps
• Time-based, one-time passwords or passcodes
• Anti-replay mechanisms that detect and reject duplicated authentication attempts.
**Guidance - Further Information:**For more information about MFA systems and features, refer to the following: PCI SSC's Information Supplement: Multi-Factor Authentication PCI SSC's Frequently Asked Questions (FAQs) on this topic.