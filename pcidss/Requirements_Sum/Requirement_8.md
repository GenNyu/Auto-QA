### A. Tài liệu gốc của Requirement 8

### B. Summary Overview của Control Objective 8.1
Tài liệu này mô tả chi tiết **Control Objective 8.1** của **Requirement 8 **trong **PCI-DSS v4.0.1**, tập trung vào việc thiết lập và duy trì chính sách, quy trình và phân công trách nhiệm liên quan đến quản lý định danh và xác thực người dùng.
Mục tiêu chính là đảm bảo các chính sách, quy trình và vai trò trách nhiệm được tài liệu hóa, cập nhật, áp dụng thực tế và được hiểu rõ bởi các bên liên quan trong hoạt động quản lý tài khoản và xác thực.
Gồm 2 sub-requirement chính:
- 8.1.1: Quản lý chính sách và quy trình
- 8.1.2: Phân công vai trò và trách nhiệm
Áp dụng cho toàn bộ tổ chức và nhân sự tham gia vào các hoạt động quản lý định danh và xác thực theo Requirement 8.

### C. Key Points của Control Objective 8.1
- **Phạm vi áp dụng:**Tất cả chính sách, quy trình và nhân sự liên quan quản lý account và authentication
- **Trách nhiệm:**Phân rõ vai trò, đảm bảo nhân sự hiểu và thực hiện đúng
- **Quản lý tài liệu:** Chính sách và quy trình phải được tài liệu hóa, cập nhật và phổ biến
- **Áp dụng thực tế:** Quy trình phải được triển khai và sử dụng thực tế
- **Truyền thông:**Đảm bảo các bên liên quan được phổ biến và hiểu nội dung

### D. Deep Summary của Control Objective 8.1
**Bối cảnh:**
Nếu chính sách và trách nhiệm không rõ ràng, việc quản lý tài khoản và xác thực có thể bị sai lệch, dẫn đến truy cập trái phép.
**Nội dung cốt lõi:**
- Tài liệu hóa chính sách và quy trình quản lý định danh và xác thực
- Cập nhật khi có thay đổi về hệ thống hoặc phương thức xác thực
- Đảm bảo quy trình được áp dụng thực tế
- Phổ biến đến tất cả nhân sự liên quan
- Phân rõ vai trò và trách nhiệm cho từng hoạt động
**Dữ liệu đáng chú ý:**
- Chính sách và quy trình phải "in use" và "known to all affected parties"
- Có thể sử dụng RACI matrix để quản lý trách nhiệm
**Rủi ro / Lưu ý:**
- Chính sách không cập nhật → không phù hợp với cơ chế xác thực mới
- Quy trình không được thực thi → tạo lỗ hổng truy cập
- Nhân sự không rõ trách nhiệm → quản lý account sai
- Thiếu phân công rõ ràng → không có accountability

### E. Structured Output của Control Objective 8.1
**Control objectives:**8.1
**Sub-requirement:**8.1.1
**Defined Approach Requirements:**All security policies and operational procedures that are identified in Requirement 8 are:
• Documented.
• Kept up to date.
• In use.
• Known to all affected parties.
**Defined Approach Testing Procedures:**Examine documentation and interview personnel to verify that security policies and operational procedures that are identified in Requirement 8 are managed in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Expectations, controls, and oversight for meeting activities within Requirement 8 are defined and adhered to by affected personnel. All supporting activities are repeatable, consistently applied, and conform to management's intent.
**Guidance - Purpose:**Requirement 8.1.1 is about effectively managing and maintaining the various policies and procedures specified throughout Requirement 8. While it is important to define the specific policies or procedures called out in Requirement 8, it is equally important to ensure they are properly documented, maintained, and disseminated.
**Guidance - Good Practice:**It is important to update policies and procedures as needed to address changes in processes, technologies, and business objectives. For this reason, consider updating these documents as soon as possible after a change occurs and not only on a periodic cycle.
**Guidance - Definitions:**Security policies define the entity's security objectives and principles. Operational procedures describe how to perform activities, and define the controls, methods, and processes that are followed to achieve the desired result in a consistent manner and in accordance with policy objectives.

---
**Control objectives:**8.1
**Sub-requirement:**8.1.2
**Defined Approach Requirements:**Roles and responsibilities for performing activities in Requirement 8 are documented, assigned, and understood.
**Defined Approach Testing Procedures:**
- "8.1.2.a": Examine documentation to verify that descriptions of roles and responsibilities for performing activities in Requirement 8 are documented and assigned.
- "8.1.2.b": Interview personnel with responsibility performing activities in Requirement 8 to verify roles and responsibilities are assigned as documented and are understood. 8.2 User identification and related accounts for users and administrators are strictly managed throughout an account's lifecycle.
**Customized Approach Objective:**Day-to-day responsibilities for performing all the activities in Requirement 8 are allocated. Personnel are accountable for successful, continuous operation of these requirements.
**Guidance - Purpose:**If roles and responsibilities are not formally assigned, personnel may not be aware of their day-to-day responsibilities and critical activities may not occur.
**Guidance - Good Practice:**Roles and responsibilities may be documented within policies and procedures or maintained within separate documents. As part of communicating roles and responsibilities, entities can consider having personnel acknowledge their acceptance and understanding of their assigned roles and responsibilities.
**Guidance - Examples:**A method to document roles and responsibilities is a responsibility assignment matrix that includes who is responsible, accountable, consulted, and informed (also called a RACI matrix). 8.2 User identification and related accounts for users and administrators are strictly managed throughout an account's lifecycle. 8.2 User identification and related accounts for users and administrators are strictly managed throughout an account's lifecycle.

================

### A. Tài liệu gốc của Requirement 8

### B. Summary Overview của Control Objective 8.2
Tài liệu này mô tả chi tiết **Control Objective 8.2** của **Requirement 8** trong **PCI-DSS v4.0.1**, tập trung vào việc quản lý định danh người dùng và vòng đời tài khoản nhằm đảm bảo khả năng truy vết và kiểm soát truy cập.
Mục tiêu chính là đảm bảo mọi người dùng được định danh duy nhất, tài khoản được quản lý xuyên suốt vòng đời và các hoạt động truy cập đều có thể truy vết về cá nhân cụ thể.
Gồm 8 sub-requirement chính:
- 8.2.1: Định danh người dùng duy nhất
- 8.2.2: Kiểm soát shared/generic account
- 8.2.3: Xác thực riêng cho service provider
- 8.2.4: Quản lý lifecycle tài khoản
- 8.2.5: Thu hồi quyền user đã nghỉ việc
- 8.2.6: Xử lý account không hoạt động
- 8.2.7: Quản lý tài khoản third-party
- 8.2.8: Session timeout và re-authentication
Áp dụng cho tất cả user, account và cơ chế xác thực trong môi trường.

### C. Key Points của Control Objective 8.2
- **Phạm vi áp dụng:**Tất cả user account, authentication và session
- **Trách nhiệm:**Tài liệu hóa và quản lý lifecycle tài khoản
- **Định danh:**Mỗi user phải có ID duy nhất để truy vết
- **Quản lý account:** Bao gồm tạo, sửa, xóa và disable account
- **Kiểm soát truy cập:** Áp dụng least privilege và approval
- **Kiểm soát đặc biệt:**Hạn chế shared account và quản lý chặt khi sử dụng
- **Third-party:**Chỉ cho phép truy cập khi cần và phải kiểm soát
- **Session:** Timeout ≤ 15 phút và yêu cầu re-authentication

### D. Deep Summary của Control Objective 8.2
**Bối cảnh:**
Không kiểm soát định danh và vòng đời tài khoản sẽ dẫn đến mất khả năng truy vết và tăng nguy cơ truy cập trái phép.
**Nội dung cốt lõi:**
- Gán ID duy nhất cho từng user để đảm bảo accountability
- Hạn chế và kiểm soát chặt shared/generic account
- Quản lý lifecycle account: tạo, sửa, xóa, disable
- Thu hồi ngay quyền truy cập khi user nghỉ việc
- Disable account không hoạt động trong 90 ngày
- Kiểm soát tài khoản third-party và remote access
- Áp dụng session timeout và yêu cầu xác thực lại
**Dữ liệu đáng chú ý:**
- Inactive account phải disable trong ≤ 90 ngày
- Session idle timeout ≤ 15 phút
- Áp dụng cho cả employee và third-party
**Rủi ro / Lưu ý:**
- Không có unique ID → không truy vết được hành vi
- Shared account → mất accountability
- Không revoke account → user cũ vẫn truy cập được
- Account không hoạt động → mục tiêu tấn công
- Session không timeout → bị lợi dụng khi user rời máy

### E. Structured Output của Control Objective 8.2
**Control objectives:**8.2
**Sub-requirement:**8.2.1
**Defined Approach Requirements:**All users are assigned a unique ID before access to system components or cardholder data is allowed.
**Defined Approach Testing Procedures:**
- "8.2.1.a": Interview responsible personnel to verify that all users are assigned a unique ID for access to system components and cardholder data.
- "8.2.1.b": Examine audit logs and other evidence to verify that access to system components and cardholder data can be uniquely identified and associated with individuals.
**Customized Approach Objective:**All actions by all users are attributable to an individual.
**Applicability Notes:**This requirement is not intended to apply to user accounts within point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction
**Guidance - Purpose:**The ability to trace actions performed on a computer system to an individual establishes accountability and traceability and is fundamental to establishing effective access controls. By ensuring each user is uniquely identified, instead of using one ID for several employees, an organization can maintain individual responsibility for actions and an effective record in the audit log per employee. In addition, this will assist with issue resolution and containment when misuse or malicious intent occurs.

---
**Control objectives:**8.2
**Sub-requirement:**8.2.2
**Defined Approach Requirements:**Group, shared, or generic IDs, or other shared authentication credentials are only used when necessary on an exception basis, and are managed as follows:
• ID use is prevented unless needed for an exceptional circumstance.
• Use is limited to the time needed for the exceptional circumstance.
• Business justification for use is documented.
• Use is explicitly approved by management.
• Individual user identity is confirmed before access to an account is granted.
• Every action taken is attributable to an individual user.
**Defined Approach Testing Procedures:**
- "8.2.2.a": Examine user account lists on system components and applicable documentation to verify that shared authentication credentials are only used when necessary, on an exception basis, and are managed in accordance with all elements specified in this requirement.
- "8.2.2.b": Examine authentication policies and procedures to verify processes are defined for shared authentication credentials such that they are only used when necessary, on an exception basis, and are managed in accordance with all elements specified in this requirement.
- "8.2.2.c": Interview system administrators to verify that shared authentication credentials are only used when necessary, on an exception basis, and are managed in accordance with all elements specified in this requirement.
**Customized Approach Objective:**All actions performed by users with group, shared, or generic IDs are attributable to an individual person.
**Applicability Notes:**This requirement is not intended to apply to user accounts within point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction.
**Guidance - Purpose:**Group, shared, or generic (or default) IDs are typically delivered with software or operating systems-for example, root or with privileges associated with a specific function, such as an administrator. If multiple users share the same authentication credentials (for example, user ID and password), it becomes impossible to trace system access and activities to an individual. In turn, this prevents an entity from assigning accountability for, or having effective logging of, an individual's actions since a given action could have been performed by anyone in the group with knowledge of the user ID and associated authentication factors. The ability to associate individuals to the actions performed with an ID is essential to provide individual accountability and traceability regarding who performed an action, what action was performed, and when that action occurred.
**Guidance - Good Practice:**If shared IDs are used for any reason, strong management controls need to be established to maintain individual accountability and traceability.
**Guidance - Examples:**Tools and techniques can facilitate both management and security of these types of accounts and confirm individual user identity before access to an account is granted. Entities can consider password vaults or other system- managed controls such as the sudo command. An example of an exceptional circumstance is where all other authentication methods have failed, and a shared ID is needed for emergency use or 'break the glass' administrator access.

---
**Control objectives:**8.2
**Sub-requirement:**8.2.3
**Defined Approach Requirements:**Additional requirement for service providers only: Service providers with remote access to customer premises use unique authentication factors for each customer premises. Customized Approach Objective A service provider's credential used for one customer cannot be used for any other customer.
**Defined Approach Testing Procedures:**Additional testing procedure for service provider assessments only: Examine authentication policies and procedures and interview personnel to verify that service providers with remote access to customer premises use unique authentication factors for remote access to each customer premises.
**Customized Approach Objective:**A service provider's credential used for one customer cannot be used for any other customer.
**Applicability Notes:**This requirement applies only when the entity being assessed is a service provider. This requirement is not intended to apply to service providers accessing their own shared services environments, where multiple customer environments are hosted. If service provider employees use shared authentication factors to remotely access customer premises, these factors must be unique per customer and managed in accordance with Requirement 8.2.2.
**Guidance - Purpose:**Service providers with remote access to customer premises typically use this access to support POS POI systems or provide other remote services. If a service provider uses the same authentication factors to access multiple customers, all the service provider's customers can easily be compromised if an attacker compromises that one factor. Criminals know this and deliberately target service providers looking for a shared authentication factor that gives them remote access to many merchants via that single factor.
**Guidance - Examples:**Technologies such as multi-factor mechanisms that provide a unique credential for each connection (such as a single-use password) could also meet the intent of this requirement.

---
**Control objectives:**8.2
**Sub-requirement:**8.2.4
**Defined Approach Requirements:**Addition, deletion, and modification of user IDs, authentication factors, and other identifier objects are managed as follows:
• Authorized with the appropriate approval.
• Implemented with only the privileges specified on the documented approval.
**Defined Approach Testing Procedures:**Examine documented authorizations across various phases of the account lifecycle (additions, modifications, and deletions) and examine system settings to verify the activity has been managed in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Lifecycle events for user IDs and authentication factors cannot occur without appropriate authorization.
**Applicability Notes:**This requirement applies to all user accounts, including employees, contractors, consultants, temporary workers, and third-party vendors.
**Guidance - Purpose:**It is imperative that the lifecycle of a user ID (additions, deletions, and modifications) is controlled so that only authorized accounts can perform functions, actions are auditable, and privileges are limited to only what is required. Attackers often compromise an existing account and then escalate the privileges of that account to perform unauthorized acts, or they may create new IDs to continue their activity in the background. It is essential to detect and respond when user IDs are created or changed outside the normal change process or without corresponding authorization.

---
**Control objectives:**8.2
**Sub-requirement:**8.2.5
**Defined Approach Requirements:**Access for terminated users is immediately revoked.
**Defined Approach Testing Procedures:**
- "8.2.5.a": Examine information sources for terminated users and review current user access lists-for both local and remote access-to verify that terminated user IDs have been deactivated or removed from the access lists.
- "8.2.5.b": Interview responsible personnel to verify that all physical authentication factors-such as, smart cards, tokens, etc.-have been returned or deactivated for terminated users.
**Customized Approach Objective:**The accounts of terminated users cannot be used.
**Guidance - Purpose:**If an employee or third party/vendor has left the company and still has access to the network via their user account, unnecessary or malicious access to cardholder data could occur-either by the former employee or by a malicious user who exploits the old and/or unused account.

---
**Control objectives:**8.2
**Sub-requirement:**8.2.6
**Defined Approach Requirements:**Inactive user accounts are removed or disabled within 90 days of inactivity.
**Defined Approach Testing Procedures:**Examine user accounts and last logon information, and interview personnel to verify that any inactive user accounts are removed or disabled within 90 days of inactivity.
**Customized Approach Objective:**Inactive user accounts cannot be used.
**Guidance - Purpose:**Accounts that are not used regularly are often targets of attack since it is less likely that any changes, such as a changed password, will be noticed. As such, these accounts may be more easily exploited and used to access cardholder data.
**Guidance - Good Practice:**Where it may be reasonably anticipated that an account will not be used for an extended period of time, such as an extended leave of absence, the account should be disabled as soon as the leave

---
**Control objectives:**8.2
**Sub-requirement:**8.2.7
**Defined Approach Requirements:**Accounts used by third parties to access, support, or maintain system components via remote access are managed as follows:
• Enabled only during the time period needed and disabled when not in use.
• Use is monitored for unexpected activity.
**Defined Approach Testing Procedures:**Interview personnel, examine documentation for managing accounts, and examine evidence to verify that accounts used by third parties for remote access are managed according to all elements specified in this requirement.
**Customized Approach Objective:**Third-party remote access cannot be used except where specifically authorized and use is overseen by management.
**Guidance - Purpose:**Allowing third parties to have 24/7 access into an entity's systems and networks in case they need to provide support increases the chances of unauthorized access. This access could result in an unauthorized user in the third party's environment or a malicious individual using the always-available external entry point into an entity's network. Where third parties do need access 24/7, it should be documented, justified, monitored, and tied to specific service reasons.
**Guidance - Good Practice:**Enabling access only for the time periods needed and disabling it as soon as it is no longer required helps prevent misuse of these connections. Additionally, consider assigning third parties a start and stop date for their access in accordance with their service contract. Monitoring third-party access helps ensure that third parties are accessing only the systems necessary and only during approved time frames. Any unusual activity using third-party accounts should be followed up and resolved.

---
**Control objectives:**8.2
**Sub-requirement:**8.2.8
**Defined Approach Requirements:**If a user session has been idle for more than 15 minutes, the user is required to re-authenticate to re-activate the terminal or session.
**Defined Approach Testing Procedures:**Examine system configuration settings to verify that system/session idle timeout features for user sessions have been set to 15 minutes or less.
**Customized Approach Objective:**A user session cannot be used except by the authorized user.
**Applicability Notes:**This requirement is not intended to apply to user accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction. This requirement is not meant to prevent legitimate activities from being performed while the console/PC is unattended.
**Guidance - Purpose:**When users walk away from an open machine with access to system components or cardholder data, there is a risk that the machine may be used by others in the user's absence, resulting in unauthorized account access and/or misuse.
**Guidance - Good Practice:**The re-authentication can be applied either at the system level to protect all sessions running on that machine or at the application level. Entities may also want to consider staging controls in succession to further restrict the access of an unattended session as time passes. For example, the screensaver may activate after 15 minutes and log off the user after an hour. However, timeout controls must balance the risk of access and exposure with the impact to the user and purpose of the access. If a user needs to run a program from an unattended computer, the user can log in to the computer to initiate the program, and then 'lock' the computer so that no one else can use the user's login while the computer is unattended.
**Guidance - Examples:**One way to meet this requirement is to configure an automated screensaver to launch whenever the console is idle for 15 minutes and requiring the logged-in user to enter their password to unlock the screen.

================

### A. Tài liệu gốc của Requirement 8

### B. Summary Overview của Control Objective 8.3
Tài liệu này mô tả chi tiết** Control Objective 8.3** của **Requirement 8 **trong **PCI-DSS v4.0.1**, tập trung vào việc xác thực người dùng và bảo vệ các yếu tố xác thực.
Mục tiêu chính là đảm bảo việc xác thực được thực hiện an toàn, các yếu tố xác thực được bảo vệ, quản lý chặt chẽ và không bị lạm dụng hoặc khai thác.
Gồm 11 sub-requirement chính:
- 8.3.1: Yếu tố xác thực
- 8.3.2: Mã hóa yếu tố xác thực
- 8.3.3: Xác minh khi thay đổi
- 8.3.4: Khóa tài khoản
- 8.3.5: Thiết lập và reset mật khẩu
- 8.3.6: Độ phức tạp mật khẩu
- 8.3.7: Lịch sử mật khẩu
- 8.3.8: Tài liệu hóa chính sách
- 8.3.9: Thay đổi định kỳ/Phân tích động
- 8.3.10: Hướng dẫn cho khách hàng (Service Provider)
- 8.3.11: Quản lý Token và Chứng chỉ
Áp dụng cho tất cả user, cơ chế xác thực và các yếu tố xác thực trong môi trường, ngoại trừ các tài khoản trên thiết bị POS chỉ truy cập một số thẻ tại một thời điểm

### C. Key Points của Control Objective 8.3
- **Phạm vi áp dụng:**Tất cả user, authentication factor và cơ chế xác thực
- **Trách nhiệm:** Tài liệu hóa và quản lý xác thực người dùng
- **Xác thực:** Sử dụng ít nhất một authentication factor (know/have/are)
- **Bảo vệ dữ liệu:**Authentication factor phải được mã hóa khi lưu trữ và truyền
- **Kiểm soát truy cập:**Giới hạn login sai và yêu cầu re-authentication
- **Quản lý password:** Áp dụng độ dài, complexity và lịch sử password
- **Chính sách người dùng:**Phổ biến hướng dẫn sử dụng và bảo vệ password

### D. Deep Summary của Control Objective 8.3
**Bối cảnh:**
Việc sử dụng các yếu tố xác thực yếu hoặc không được bảo vệ là kẽ hở lớn để kẻ tấn công xâm nhập hệ thống và chiếm đoạt quyền truy cập hợp lệ. Kiểm soát này giúp giảm thiểu rủi ro từ các cuộc tấn công dò mật khẩu (brute-force) hoặc kỹ thuật xã hội (social engineering)
**Nội dung cốt lõi:**
- Sử dụng authentication factor phù hợp (password, token, biometric)
- Bảo vệ authentication factor bằng strong cryptography
- Xác minh danh tính trước khi thay đổi authentication factor
- Giới hạn số lần login sai và lock account
- Áp dụng chính sách password mạnh (độ dài, complexity, history)
- Quản lý vòng đời password và cập nhật định kỳ
- Phổ biến hướng dẫn cho người dùng về bảo vệ thông tin xác thực
**Dữ liệu đáng chú ý:**
- Lock account sau ≤ 10 lần đăng nhập sai
- Lock tối thiểu 30 phút hoặc đến khi xác minh
- Password ≥ 12 ký tự (hoặc ≥ 8 nếu hệ thống hạn chế)
- Thay đổi mật khẩu ít nhất mỗi 90 ngày nếu chỉ dùng xác thực đơn yếu tố
**Rủi ro / Lưu ý:**
- Password yếu → dễ bị brute force
- Không mã hóa → lộ authentication factor
- Không lock account → attacker thử nhiều lần
- Không verify identity → bị social engineering
- Reuse password → tăng nguy cơ compromise

### E. Structured Output của Control Objective 8.3
**Control objectives:**8.3
**Sub-requirement:**8.3.1
**Defined Approach Requirements:**All user access to system components for users and administrators is authenticated via at least one of the following authentication factors:
• Something you know, such as a password or passphrase.
• Something you have, such as a token device or smart card.
• Something you are, such as a biometric element.
**Defined Approach Testing Procedures:**
- "8.3.1.a": Examine documentation describing the authentication factor(s) used to verify that user access to system components is authenticated via at least one authentication factor specified in this requirement.
- "8.3.1.b": For each type of authentication factor used with each type of system component, observe an authentication to verify that authentication is functioning consistently with documented authentication factor(s).
**Customized Approach Objective:**An account cannot be accessed except with a combination of user identity and an authentication factor.
**Applicability Notes:**This requirement is not intended to apply to user accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction. This requirement does not supersede multi-factor authentication (MFA) requirements but applies to those in-scope systems not otherwise subject to MFA requirements. A digital certificate is a valid option for 'something you have' if it is unique for a particular user.
**Guidance - Purpose:**When used in addition to unique IDs, an authentication factor helps protect user IDs from being compromised, since the attacker needs to have the unique ID and compromise the associated authentication factor(s).
**Guidance - Good Practice:**A common approach for a malicious individual to compromise a system is to exploit weak or nonexistent authentication factors (for example, passwords/passphrases). Requiring strong authentication factors helps protect against this attack.
**Guidance - Further Information:**See fidoalliance.org for more information about using tokens, smart cards, or biometrics as authentication factors.

---
**Control objectives:**8.3
**Sub-requirement:**8.3.2
**Defined Approach Requirements:**Strong cryptography is used to render all authentication factors unreadable during transmission and storage on all system components.
**Defined Approach Testing Procedures:**
- "8.3.2.a": Examine vendor documentation and system configuration settings to verify that authentication factors are rendered unreadable with strong cryptography during transmission and storage.
- "8.3.2.b": Examine repositories of authentication factors to verify that they are unreadable during storage.
- "8.3.2.c": Examine data transmissions to verify that authentication factors are unreadable during transmission.
**Customized Approach Objective:**Cleartext authentication factors cannot be obtained, derived, or reused from the interception of communications or from stored data.
**Guidance - Purpose:**Network devices and applications have been known to transmit unencrypted, readable authentication factors (such as passwords and passphrases) across the network and/or store these values without encryption. As a result, a malicious individual can easily intercept this information during transmission using a 'sniffer,' or directly access unencrypted authentication factors in files where they are stored, and then use this data to gain unauthorized access.

---
**Control objectives:**8.3
**Sub-requirement:**8.3.3
**Defined Approach Requirements:**User identity is verified before modifying any authentication factor.
**Defined Approach Testing Procedures:**Examine procedures for modifying authentication factors and observe security personnel to verify that when a user requests a modification of an authentication factor, the user's identity is verified before the authentication factor is modified.
**Customized Approach Objective:**Unauthorized individuals cannot gain system access by impersonating the identity of an authorized user.
**Guidance - Purpose:**Malicious individuals use "social engineering' techniques to impersonate a user of a system- for example, calling a help desk and acting as a legitimate user-to have an authentication factor changed so they can use a valid user ID. Requiring positive identification of a user reduces the probability of this type of attack succeeding.
**Guidance - Good Practice:**Modifications to authentication factors for which user identity should be verified include but are not limited to performing password resets, provisioning new hardware or software tokens, and generating new keys.
**Guidance - Examples:**Methods to verify a user's identity include a secret question/answer, knowledge-based information, and calling the user back at a known and previously established phone number.

---
**Control objectives:**8.3
**Sub-requirement:**8.3.4
**Defined Approach Requirements:**Invalid authentication attempts are limited by:
• Locking out the user ID after not more than 10 attempts.
• Setting the lockout duration to a minimum of 30 minutes or until the user's identity is confirmed.
**Defined Approach Testing Procedures:**
- "8.3.4.a": Examine system configuration settings to verify that authentication parameters are set to require that user accounts be locked out after not more than 10 invalid logon attempts.
- "8.3.4.b": Examine system configuration settings to verify that password parameters are set to require that once a user account is locked out, it remains locked for a minimum of 30 minutes or until the user's identity is confirmed.
**Customized Approach Objective:**An authentication factor cannot be guessed in a brute force, online attack.
**Applicability Notes:**This requirement is not intended to apply to user accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction.
**Guidance - Purpose:**Without account-lockout mechanisms in place, an attacker can continually try to guess a password through manual or automated tools (for example, password cracking) until the attacker succeeds and gains access to a user's account. If an account is locked out due to someone continually trying to guess a password, controls to delay reactivation of the locked account stop the malicious individual from guessing the password, as they will have to stop for a minimum of 30 minutes until the account is reactivated.
**Guidance - Good Practice:**Before reactivating a locked account, the user's identity should be confirmed. For example, the administrator or help desk personnel can validate that the actual account owner is requesting reactivation, or there may be password reset self- service mechanisms that the account owner uses to verify their identity.

---
**Control objectives:**8.3
**Sub-requirement:**8.3.5
**Defined Approach Requirements:**If passwords/passphrases are used as authentication factors to meet Requirement 8.3.1, they are set and reset for each user as follows:
• Set to a unique value for first-time use and upon reset.
• Forced to be changed immediately after the first use.
**Defined Approach Testing Procedures:**Examine procedures for setting and resetting passwords/passphrases (if used as authentication factors to meet Requirement 8.3.1) and observe security personnel to verify that passwords/passphrases are set and reset in accordance with all elements specified in this requirement.
**Customized Approach Objective:**An initial or reset password/passphrase assigned to a user cannot be used by an unauthorized user.
**Guidance - Purpose:**If the same password/passphrase is used for every new user, an internal user, former employee, or malicious individual may know or easily discover the value and use it to gain access to accounts before the authorized user attempts to use the password.

---
**Control objectives:**8.3
**Sub-requirement:**8.3.6
**Defined Approach Requirements:**If passwords/passphrases are used as authentication factors to meet Requirement 8.3.1, they meet the following minimum level of complexity:
• A minimum length of 12 characters (or IF the system does not support 12 characters, a minimum length of eight characters).
• Contain both numeric and alphabetic characters.
**Defined Approach Testing Procedures:**Examine system configuration settings to verify that user password/passphrase complexity parameters are set in accordance with all elements specified in this requirement.
**Customized Approach Objective:**A guessed password/passphrase cannot be verified by either an online or offline brute force attack.
**Applicability Notes:**This requirement is not intended to apply to:
• User accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction.
• Application or system accounts, which are governed by requirements in section 8.6. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. Until 31 March 2025, passwords must be a minimum length of seven characters in accordance with PCI DSS v3.2.1 Requirement 8.2.3.
**Guidance - Purpose:**Strong passwords/passphrases may be the first line of defense into a network since a malicious individual will often first try to find accounts with weak, static, or non-existent passwords. If passwords are short or easily guessable, it is relatively easy for a malicious individual to find these weak accounts and compromise a network under the guise of a valid user ID.
**Guidance - Good Practice:**Password/passphrase strength is dependent on password/passphrase complexity, length, and randomness. Passwords/passphrases should be sufficiently complex, so they are impractical for an attacker to guess or otherwise discover its value. Entities can consider adding increased complexity by requiring the use of special characters and upper- and lower-case characters, in addition to the minimum standards outlined by this requirement. Additional complexity increases the time required for offline brute force attacks of hashed passwords/passphrases. Another option for increasing the resistance of passwords to guessing attacks is by comparing proposed password/passphrases to a bad password list and having users provide new passwords for any passwords found on the list.

---
**Control objectives:**8.3
**Sub-requirement:**8.3.7
**Defined Approach Requirements:**Individuals are not allowed to submit a new password/passphrase that is the same as any of the last four passwords/passphrases used.
**Defined Approach Testing Procedures:**Examine system configuration settings to verify that password parameters are set to require that new passwords/passphrases cannot be the same as the four previously used passwords/passphrases.
**Customized Approach Objective:**A previously used password cannot be used to gain access to an account for at least 12 months.
**Applicability Notes:**This requirement is not intended to apply to user accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction.
**Guidance - Purpose:**If password history is not maintained, the effectiveness of changing passwords is reduced, as previous passwords can be reused over and over. Requiring that passwords cannot be reused for a period reduces the likelihood that passwords that have been guessed or brute-forced will be re- used in the future. Passwords or passphrases may have previously been changed due to suspicion of compromise or because the password or passphrase exceeded its effective use period, both of which are reasons why previously used passwords should not be reused.

---
**Control objectives:**8.3
**Sub-requirement:**8.3.8
**Defined Approach Requirements:**Authentication policies and procedures are documented and communicated to all users including:
• Guidance on selecting strong authentication factors.
• Guidance for how users should protect their authentication factors.
• Instructions not to reuse previously used passwords/passphrases.
• Instructions to change passwords/passphrases there is any suspicion or knowledge that the password/passphrases have been and how to report the incident.
**Defined Approach Testing Procedures:**
- "8.3.8.a": Examine procedures and interview personnel to verify that authentication policies and procedures are distributed to all users.
- "8.3.8.b": Review authentication policies and procedures that are distributed to users and verify they include the elements specified in this requirement.
- "8.3.8.c": Interview users to verify that they are familiar with authentication policies and procedures.
**Customized Approach Objective:**Users are knowledgeable about the correct use of authentication factors and can access assistance and guidance when required.
**Guidance - Purpose:**Communicating authentication policies and procedures to all users helps them to understand and abide by the policies.
**Guidance - Good Practice:**Guidance on selecting strong passwords may include suggestions to help personnel select hard-to-guess passwords that do not contain dictionary words or information about the user, such as the user ID, names of family members, date of birth, etc. Guidance for protecting authentication factors may include not writing down passwords or not saving them in insecure files, and being alert to malicious individuals who may try to exploit their passwords (for example, by calling an employee and asking for their password so the caller can 'troubleshoot a problem'). Alternatively, entities can implement processes to confirm passwords meet password policy, for example, by comparing password choices to a list of unacceptable passwords and having users choose a new password for any that match with one on the list. Instructing users to change passwords if there is a chance the password is no longer secure can prevent malicious users from using a legitimate password to gain unauthorized access.

---
**Control objectives:**8.3
**Sub-requirement:**8.3.9
**Defined Approach Requirements:**If passwords/passphrases are used as the only authentication factor for user access (i.e., in any single-factor authentication implementation) then either:
• Passwords/passphrases are changed at least once every 90 days, OR
• The security posture of accounts is dynamically analyzed, and real-time access to resources is automatically determined accordingly.
**Defined Approach Testing Procedures:**If passwords/passphrases are used as the only authentication factor for user access, inspect system configuration settings to verify that passwords/passphrases are managed in accordance with ONE of the elements specified in this requirement.
**Customized Approach Objective:**An undetected compromised password/passphrase cannot be used indefinitely.
**Applicability Notes:**This requirement does not apply to in-scope system components where MFA is used. This requirement is not intended to apply to user accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction. This requirement does not apply to service providers' customer accounts but does apply to facilitate a single transaction. This requirement does not apply to service providers' customer accounts but does apply to accounts for service provider personnel.
**Guidance - Purpose:**Access to in-scope system components that are not in the CDE may be provided using a single authentication factor, such as a password/passphrase, token device or smart card, or biometric attribute. Where passwords/passphrases are employed as the only authentication factor for such access, additional controls are required to protect the integrity of the password/passphrase.
**Guidance - Good Practice:**Passwords/passphrases that are valid for a long time without a change provide malicious individuals with more time to break the password/phrase. Periodically changing passwords offers less time for a malicious individual to crack a password/passphrase and less time to use a compromised password. Using a password/passphrase as the only authentication factor provides a single point of failure if compromised. Therefore, in these implementations, controls are needed to minimize how long malicious activity could occur via a compromised password/passphrase. Dynamically analyzing an account's security posture is another option that allows for more rapid detection and response to address potentially compromised credentials. Such analysis takes a number of data points, which may include device integrity, location, access times, and the resources accessed to determine in real time whether an account can be granted access to a requested resource. In this way, access can be denied and accounts blocked if it is suspected that authentication credentials have been compromised.
**Guidance - Further Information:**For information about using dynamic analysis to manage user access to resources, see NIST SP 800-207 Zero Trust Architecture .

---
**Control objectives:**8.3
**Sub-requirement:**8.3.10
**Defined Approach Requirements:**Additional requirement for service providers only: If passwords/passphrases are used as the only authentication factor for customer user access to cardholder data (i.e., in any single- factor authentication implementation), then guidance is provided to customer users including:
• Guidance for customers to change their user passwords/passphrases periodically.
• Guidance as to when, and under what circumstances, passwords/passphrases are to be changed.
**Defined Approach Testing Procedures:**Additional testing procedure for service provider assessments only: If passwords/passphrases are used as the only authentication factor for customer user access to cardholder data, examine guidance provided to customer users to verify that the guidance includes all elements specified in this requirement.
**Customized Approach Objective:**Passwords/passphrases for service providers' customers cannot be used indefinitely.
**Applicability Notes:**This requirement applies only when the entity being assessed is a service provider. This requirement does not apply to accounts of consumer users accessing their own payment card information.
This requirement for service providers will be superseded by Requirement 8.3.10.1 once 8.3.10.1 becomes effective.
**Guidance - Purpose:**Using a password/passphrase as the only authentication factor provides a single point of failure if compromised. Therefore, in these implementations, controls are needed to minimize how long malicious activity could occur via a compromised password/passphrase.
**Guidance - Good Practice:**Passwords/passphrases that are valid for a long time without a change provide malicious individuals with more time to break the password/phrase. Periodically changing passwords offers less time for a malicious individual to crack a password/passphrase and less time to use a compromised password.

---
**Control objectives:**8.3
**Sub-requirement:**8.3.10.1
**Defined Approach Requirements:**Additional requirement for service providers only: If passwords/passphrases are used as the only authentication factor for customer user access (i.e., in any single-factor authentication implementation) then either:
• Passwords/passphrases are changed at least once every 90 days, OR
• The security posture of accounts is dynamically analyzed, and real-time access to resources is automatically determined accordingly.
**Defined Approach Testing Procedures:**Additional testing procedure for service provider assessments only: If passwords/passphrases are used as the only authentication factor for customer user access, inspect system configuration settings to verify that passwords/passphrases are managed in accordance with ONE of the elements specified in this requirement.
**Customized Approach Objective:**Passwords/passphrases for service providers' customers cannot be used indefinitely.
**Applicability Notes:**This requirement applies only when the entity being assessed is a service provider. This requirement does not apply to accounts of consumer users accessing their own payment card information. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. Until this requirement is effective on 31 March 2025, service providers may meet either Requirement 8.3.10 or 8.3.10.1.
**Guidance - Purpose:**Using a password/passphrase as the only authentication factor provides a single point of failure if compromised. Therefore, in these implementations, controls are needed to minimize how long malicious activity could occur via a compromised password/passphrase.
**Guidance - Good Practice:**Passwords/passphrases that are valid for a long time without a change provide malicious individuals with more time to break the password/phrase. Periodically changing passwords offers less time for a malicious individual to crack a password/passphrase and less time to use a compromised password. Dynamically analyzing an account's security posture is another option that allows for more rapid detection and response to address potentially compromised credentials. Such analysis takes a number of data points which may include device integrity, location, access times, and the resources accessed to determine in real time whether an account can be granted access to a requested resource. In this way, access can be denied and accounts blocked if it is suspected that account credentials have been compromised.
**Guidance - Further Information:**For information about using dynamic analysis to manage user access to resources, refer to NIST SP 800-207 Zero Trust Architecture .

---
**Control objectives:**8.3
**Sub-requirement:**8.3.11
**Defined Approach Requirements:**Where authentication factors such as physical or logical security tokens, smart cards, or certificates are used:
• Factors are assigned to an individual user and not shared among multiple users.
• Physical and/or logical controls ensure only the intended user can use that factor to gain access.
**Defined Approach Testing Procedures:**
- "8.3.11.a": Examine authentication policies and procedures to verify that procedures for using authentication factors such as physical security tokens, smart cards, and certificates are defined and include all elements specified in this requirement.
- "8.3.11.b": Interview security personnel to verify authentication factors are assigned to an individual user and not shared among multiple users.
- "8.3.11.c": Examine system configuration settings and/or observe physical controls, as applicable, to verify that controls are implemented to ensure only the intended user can use that factor to gain access.
**Customized Approach Objective:**An authentication factor cannot be used by anyone other than the user to which it is assigned.
**Guidance - Purpose:**If multiple users can use authentication factors such as tokens, smart cards, and certificates, it may be impossible to identify the individual using the authentication mechanism.
**Guidance - Good Practice:**Having physical and/or logical controls (for example, a PIN, biometric data, or a password) to uniquely authenticate the user of the account will prevent unauthorized users from gaining access to the user account through use of a shared authentication factor.

================

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

================

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

================

### A. Tài liệu gốc của Requirement 8

### B. Summary Overview của Control Objective 8.6
Tài liệu này mô tả chi tiết **Control Objective 8.6** của **Requirement 8** trong **PCI-DSS v4.0.1**, tập trung vào việc quản lý và bảo vệ tài khoản hệ thống và ứng dụng.
Mục tiêu chính là đảm bảo các account hệ thống và ứng dụng được kiểm soát chặt chẽ, không bị lạm dụng và các yếu tố xác thực liên quan được bảo vệ an toàn.
Gồm 3 sub-requirement chính:
- 8.6.1: Kiểm soát interactive login cho system/application account
- 8.6.2: Không hardcode password
- 8.6.3: Bảo vệ password system/application account
Áp dụng cho tất cả system account và application account trong môi trường.

### C. Key Points của Control Objective 8.6
- **Phạm vi áp dụng:**Tất cả system account và application account
- **Trách nhiệm:** Tài liệu hóa và kiểm soát việc sử dụng account đặc quyền
- **Kiểm soát truy cập:**Hạn chế interactive login, chỉ cho phép khi có exception
- **Quản lý password:**Không được hardcode password trong code/config
- **Bảo vệ xác thực:**Password phải được thay đổi định kỳ và có độ phức tạp phù hợp
- **Truy vết:**Mọi hành động phải truy vết được về cá nhân

### D. Deep Summary của Control Objective 8.6
**Bối cảnh:**
System và application account thường có quyền cao, nếu bị compromise sẽ gây ảnh hưởng nghiêm trọng đến hệ thống và dữ liệu.
**Nội dung cốt lõi:**
- Không cho phép interactive login với system/application account trừ khi có exception được phê duyệt
- Nếu sử dụng interactive login, phải đảm bảo truy vết được về cá nhân
- Không hardcode password trong source code, script hoặc config
- Bảo vệ password bằng cách thay đổi định kỳ và tăng độ phức tạp
- Áp dụng kiểm soát bổ sung (vault, managed solution) để bảo vệ credential
**Dữ liệu đáng chú ý:**
- Password change frequency dựa trên risk analysis (Requirement 12.3.1)
- Có thể sử dụng password vault để quản lý credential
**Rủi ro / Lưu ý:**
- Hardcoded password → dễ bị lộ qua source code
- System account bị lạm dụng → khó truy vết
- Không rotate password → tăng nguy cơ bị brute force
- Interactive login không kiểm soát → mất accountability

### E. Structured Output của Control Objective 8.6
**Control objectives:**8.6
**Sub-requirement:**8.6.1
**Defined Approach Requirements:**If accounts used by systems or applications can be used for interactive login, they are managed as follows:
• Interactive use is prevented unless needed for an exceptional circumstance.
• Interactive use is limited to the time needed for the exceptional circumstance.
• Business justification for interactive use is documented.
• Interactive use is explicitly approved by management.
• Individual user identity is confirmed before access to account is granted.
• Every action taken is attributable to an individual user.
**Defined Approach Testing Procedures:**Examine application and system accounts that can be used interactively and interview administrative personnel to verify that application and system accounts are managed in accordance with all elements specified in this requirement.
**Customized Approach Objective:**When used interactively, all actions with accounts designated as system or application accounts are authorized and attributable to an individual person.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Like individual user accounts, system and application accounts require accountability and strict management to ensure they are used only for the intended purpose and are not misused. Attackers often compromise system or application accounts to gain access to cardholder data.
**Guidance - Good Practice:**Where possible, configure system and application accounts to disallow interactive login to prevent unauthorized individuals from logging in and using the account with its associated system privileges, and to limit the machines and devices on which the account can be used.
**Guidance - Definitions:**Interactive login is the ability for a person to log into a system or application account in the same manner as a normal user account. Using system and application accounts this way means there is no accountability and traceability of actions taken by the user. Refer to Appendix G for the definition of 'application and system accounts.'

---
**Control objectives:**8.6
**Sub-requirement:**8.6.2
**Defined Approach Requirements:**Passwords/passphrases for any application and system accounts that can be used for interactive login are not hard coded in scripts, configuration/property files, or bespoke and custom source code.
**Defined Approach Testing Procedures:**
- "8.6.2.a": Interview personnel and examine system development procedures to verify that processes are defined for application and system accounts that can be used for interactive login, specifying that passwords/passphrases are not hard coded in scripts, configuration/property files, or bespoke and custom source code.
- "8.6.2.b": Examine scripts, configuration/property files, and bespoke and custom source code for application and system accounts that can be used for interactive login, to verify passwords/passphrases for those accounts are not present.
**Customized Approach Objective:**Passwords/passphrases used by application and system accounts cannot be used by unauthorized personnel.
**Applicability Notes:**Stored passwords/passphrases are required to be encrypted in accordance with PCI DSS Requirement 8.3.2. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Not properly protecting passwords/passphrases used by application and system accounts, especially if those accounts can be used for interactive login, increases the risk and success of unauthorized use of those privileged accounts.
**Guidance - Good Practice:**Changing these values due to suspected or confirmed disclosure can be particularly difficult to implement. Tools can facilitate both management and security of authentication factors for application and system accounts. For example, consider password vaults or other system-managed controls.

---
**Control objectives:**8.6
**Sub-requirement:**8.6.3
**Defined Approach Requirements:**Passwords/passphrases for any application and system accounts are protected against misuse as follows:
• Passwords/passphrases are changed periodically (at the frequency defined in the entity's targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1) and upon suspicion or confirmation of compromise.
• Passwords/passphrases are constructed with sufficient complexity appropriate for how frequently the entity changes the passwords/passphrases.
**Defined Approach Testing Procedures:**
- "8.6.3.a": Examine policies and procedures to verify that procedures are defined to protect passwords/passphrases for application or system accounts against misuse in accordance with all elements specified in this requirement.
- "8.6.3.b": Examine the entity's targeted risk analysis for the change frequency and complexity for passwords/passphrases for application and system accounts to verify the risk analysis was performed in accordance with all elements specified in Requirement 12.3.1 and addresses:
• The frequency defined for periodic changes to application and system passwords/passphrases.
• The complexity defined for passwords/passphrases and appropriateness of the complexity relative to the frequency of changes.
- "8.6.3.c": Interview responsible personnel and examine system configuration settings to verify that passwords/passphrases for any application and system accounts are protected against misuse in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Passwords/passphrases used by application and system accounts cannot be used indefinitely and are structured to resist brute-force and guessing attacks.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Systems and application accounts pose more inherent security risk than user accounts because they often run in an elevated security context, with access to systems that may not be typically granted to user accounts, such as programmatic access to databases, etc. As a result, special consideration must be made to protect passwords/passphrases used for application and system accounts.
**Guidance - Good Practice:**Entities should consider the following risk factors when determining how to protect application and system passwords/passphrases against misuse:
• How securely the passwords/passphrases are stored (for example, whether they are stored in a password vault).
• Staff turnover.
• The number of people with access to the authentication factor.
• Whether the account can be used for interactive login.
• Whether the security posture of accounts is dynamically analyzed, and real-time access to resources is automatically determined accordingly (see Requirement 8.3.9). All these elements affect the level of risk for application and system accounts and might impact the security of systems accessed by the system and application accounts.
Entities should correlate their selected change frequency for application and system passwords/passwords with their selected complexity for those passwords/passphrases - i.e., the complexity should be more rigorous when passwords/passphrases are changed infrequently and can be less rigorous when changed more frequently. For example, a longer change frequency is more justifiable when passwords/passphrases complexity is set to 36 alphanumeric characters with upper- and lower- case letters, numbers, and special characters. Best practices are to consider password changes at least once a year, a password/passphrase length of at least 15 characters, and complexity for the passwords/passphrase of alphanumeric characters, with upper- and lower-case letters, and special characters.
**Guidance - Further Information:**For information about variability and equivalency of password strength for passwords/passphrases of different formats, see the industry standards (for example, the current version of NIST SP 800- 63 Digital Identity Guidelines).