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