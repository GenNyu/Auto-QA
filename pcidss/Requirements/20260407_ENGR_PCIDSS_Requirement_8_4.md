### A. Tài liệu gốc của Requirement 8

### B. Summary Overview của Control Objective 8.4
Tài liệu này mô tả chi tiết** Control Objective 8.4 **của **Requirement 8** trong **PCI-DSS v4.0.1**, tập trung vào việc triển khai xác thực đa yếu tố (MFA) để bảo vệ truy cập vào hệ thống và dữ liệu.
Mục tiêu chính là đảm bảo truy cập vào CDE và các kết nối từ xa không thể được thực hiện chỉ với một yếu tố xác thực, nhằm giảm thiểu rủi ro bị compromise tài khoản.
Gồm 3 sub-requirement chính:
- 8.4.1: MFA cho admin non-console access
- 8.4.2: MFA cho tất cả truy cập vào CDE
- 8.4.3: MFA cho remote access
Áp dụng cho tất cả user, admin và third-party có truy cập vào CDE hoặc truy cập từ xa vào hệ thống.

### C. Key Points của Control Objective 8.4
- **Phạm vi áp dụng:**Truy cập vào CDE và remote access từ bên ngoài
- **Trách nhiệm:**Triển khai và đảm bảo MFA được áp dụng đúng phạm vi
- **Kiểm soát truy cập:** Bắt buộc MFA cho non-console access và remote access
- **Bảo mật xác thực:**MFA phải sử dụng ≥ 2 yếu tố (know/have/are)
- **Phạm vi hệ thống:**Áp dụng cho tất cả system components (cloud, on-prem, network, application)

### D. Deep Summary của Control Objective 8.4
**Bối cảnh:**
Xác thực một yếu tố (single-factor) dễ bị compromise, đặc biệt trong các cuộc tấn công đánh cắp thông tin đăng nhập hoặc phishing.
**Nội dung cốt lõi:**
- Áp dụng MFA cho admin khi truy cập non-console vào CDE
- Áp dụng MFA cho tất cả truy cập vào CDE
- Áp dụng MFA cho remote access từ bên ngoài mạng
- MFA phải sử dụng ít nhất 2 loại yếu tố xác thực khác nhau
- Có thể triển khai MFA ở network level hoặc system/application level
**Dữ liệu đáng chú ý:**
- MFA không hợp lệ nếu dùng cùng loại yếu tố 2 lần (ví dụ: 2 password)
- Có thể yêu cầu MFA nhiều lần (ví dụ: remote access + access vào CDE)
**Rủi ro / Lưu ý:**
- Không có MFA → dễ bị chiếm quyền tài khoản
- Áp dụng MFA không đầy đủ → tạo điểm yếu trong hệ thống
- Remote access không có MFA → entry point phổ biến cho attacker
- Hiểu sai MFA → triển khai không đúng (ví dụ dùng cùng loại factor)

### E. Structured Output của Control Objective 8.4
**Control objectives:**8.4
**Sub-requirement:**8.4.1
**Defined Approach Requirements:**MFA is implemented for all non-console access into the CDE for personnel with administrative access.
**Defined Approach Testing Procedures:**
- "8.4.1.a": Examine network and/or system configurations to verify MFA is required for all nonconsole into the CDE for personnel with administrative access.
- "8.4.1.b": Observe administrator personnel logging into the CDE and verify that MFA is required.
**Customized Approach Objective:** Administrative access to the CDE cannot be obtained by the use of a single authentication factor.
**Applicability Notes:**The requirement for MFA for non-console administrative access applies to all personnel with elevated or increased privileges accessing the CDE via a non-console connection—that is, via logical access occurring over a network interface rather than via a direct, physical connection.
**Guidance - Purpose:**Requiring more than one type of authentication factor reduces the probability that an attacker can gain access to a system by masquerading as a legitimate user, because the attacker would need to compromise multiple authentication factors. This is especially true in environments where traditionally the single authentication factor employed was something a user knows such as a password or passphrase.
**Guidance - Good Practice:** Implementing MFA for non-console administrative access to in-scope system components that are not part of the CDE will help prevent unauthorized users from using a single factor to gain access and compromise in-scope system components.
**Guidance - Definitions:** Using one factor twice (for example, using two separate passwords) is not considered multi-factor authentication.

---
**Control objectives:**8.4
**Sub-requirement:**8.4.2
**Defined Approach Requirements:**MFA is implemented for all non-console access into the CDE.
**Defined Approach Testing Procedures:**
- "8.4.2.a": Examine network and/or system configurations to verify MFA is implemented for all non-console access into the CDE.
- "8.4.2.b": Observe personnel logging in to the CDE and examine evidence to verify that MFA is required.
**Customized Approach Objective:**Access into the CDE cannot be obtained by the use of a single authentication factor.
**Applicability Notes:**This requirement does not apply to:
• Application or system accounts performing automated functions.
• User accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction.
• User accounts that are only authenticated with phishing-resistant authentication factors. MFA is required for both types of access specified in Requirements 8.4.2 and 8.4.3. Therefore, applying MFA to one type of access does not replace the need to apply another instance of MFA to the other type of access. If an individual first connects to the entity's network via remote access, and then later initiates a connection into the CDE from within the network, per this requirement the individual would authenticate using MFA twice, once when connecting via remote access to the entity's network and once when connecting from the entity's network into the CDE.
The MFA requirements apply for all types of system components, including cloud, hosted systems, and on-premises applications, network security devices, workstations, servers, and endpoints, and includes access directly to an entity's networks or systems as well as web-based access to an application or function. MFA for access into the CDE can be implemented at the network or system/application level; it does not have to be applied at both levels. For example, if MFA is used when a user connects to the CDE network, it does not have to be used when the user logs into each system or application within the CDE. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Requiring more than one type of authentication factor reduces the probability that an attacker can gain access to a system by masquerading as a legitimate user, because the attacker would need to compromise multiple authentication factors. This is especially true in environments where traditionally the single authentication factor employed was something a user knows such as a password or passphrase.
**Guidance - Definitions:**Using one factor twice (for example, using two separate passwords) is not considered multi- factor authentication. Refer to Appendix G for the definition of 'phishing resistant authentication.'

---
**Control objectives:**8.4
**Sub-requirement:**8.4.3
**Defined Approach Requirements:**MFA is implemented for all remote access originating from outside the entity's network that could access or impact the CDE.
**Defined Approach Testing Procedures:**
- "8.4.3.a": Examine network and/or system configurations for remote access servers and systems to verify MFA is required in accordance with all elements specified in this requirement.
- "8.4.3.b": Observe personnel (for example, users and administrators) and third parties connecting remotely to the network and verify that multi-factor authentication is required.
**Customized Approach Objective:**Remote access to the entity's network cannot be obtained by using a single authentication factor.
**Applicability Notes:** The requirement for MFA for originating from outside the to all user accounts that can remotely, where that remote could lead to access into the remote access by personnel administrators), and third parties limited to, vendors, suppliers, customers). If remote access is to a part that is properly segmented from remote users cannot access MFA for remote access to that not required. However, MFA remote access to networks with and is recommended for all entity's networks. The MFA requirements apply components, including cloud, on-premises applications, network workstations, servers, and endpoints, access directly to an entity's well as web-based access to function.
**Guidance - Purpose:**Requiring more than one type of authentication factor reduces the probability that an attacker can gain access to a system by masquerading as a legitimate user, because the attacker would need to compromise multiple authentication factors. This is especially true in environments where traditionally the single authentication factor employed was something a user knows, such as a password or passphrase.
**Guidance - Definitions:**Multi-factor authentication (MFA) requires an individual to present a minimum of two of the three authentication factors specified in Requirement 8.3.1 before access is granted. Using one factor twice (for example, using two separate passwords) is not considered multi- factor authentication.