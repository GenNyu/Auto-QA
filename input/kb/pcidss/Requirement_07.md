### A. Tài liệu gốc của Requirement 7

### B. Summary Overview của Control Objective 7.1
Tài liệu này mô tả chi tiết **Control Objective 7.1** của **Requirement 7** trong **PCI-DSS v4.0.1**, tập trung vào việc thiết lập và duy trì chính sách, quy trình và phân công trách nhiệm liên quan đến kiểm soát truy cập.
Mục tiêu chính là đảm bảo các chính sách, quy trình và vai trò trách nhiệm được tài liệu hóa, cập nhật, áp dụng thực tế và được hiểu rõ bởi các bên liên quan trong hoạt động kiểm soát truy cập.
Gồm 2 sub-requirement chính:
- 7.1.1: Quản lý chính sách và quy trình
- 7.1.2: Phân công vai trò và trách nhiệm
Áp dụng cho toàn bộ tổ chức và nhân sự tham gia vào các hoạt động kiểm soát truy cập theo Requirement 7.

### C. Key Points của Control Objective 7.1
- **Phạm vi áp dụng:** Tất cả chính sách, quy trình và nhân sự liên quan kiểm soát truy cập
- **Trách nhiệm:**Phân rõ vai trò, đảm bảo nhân sự hiểu và thực hiện đúng
- **Quản lý tài liệu:** Chính sách và quy trình phải được tài liệu hóa, cập nhật và phổ biến
- **Áp dụng thực tế:**Quy trình phải được triển khai và sử dụng thực tế
- **Truyền thông:** Đảm bảo các bên liên quan được phổ biến và hiểu nội dung

### D. Deep Summary của Control Objective 7.1
**Bối cảnh:**
Nếu chính sách và trách nhiệm không rõ ràng, việc kiểm soát truy cập có thể không được thực thi đúng, dẫn đến truy cập trái phép vào hệ thống và dữ liệu.
**Nội dung cốt lõi:**
- Tài liệu hóa chính sách và quy trình kiểm soát truy cập
- Cập nhật khi có thay đổi về hệ thống hoặc yêu cầu truy cập
- Đảm bảo quy trình được áp dụng thực tế
- Phổ biến đến tất cả nhân sự liên quan
- Phân rõ vai trò và trách nhiệm cho từng hoạt động
**Dữ liệu đáng chú ý:**
- Chính sách và quy trình phải "in use" và "known to all affected parties"
- Có thể sử dụng RACI matrix để quản lý trách nhiệm
**Rủi ro / Lưu ý:**
- Chính sách không cập nhật → không kiểm soát được truy cập mới
- Quy trình không được thực thi → phát sinh truy cập trái phép
- Nhân sự không rõ trách nhiệm → cấp quyền sai
- Thiếu phân công rõ ràng → không có accountability

### E. Structured Output của Control Objective 7.1
**Control objectives:**7.1
**Sub-requirement:**7.1.1
**Defined Approach Requirements:**All security policies and operational procedures that are identified in Requirement 7 are:
• Documented.
• Kept up to date.
• In use.
• Known to all affected parties.
**Defined Approach Testing Procedures:**Examine documentation and interview personnel to verify that security policies and operational procedures identified in Requirement 7 are managed in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Expectations, controls, and oversight for meeting activities within Requirement 7 are defined and adhered to by affected personnel. All supporting activities are repeatable, consistently applied, and conform to management's intent.
**Guidance - Purpose:**Requirement 7.1.1 is about effectively managing and maintaining the various policies and procedures specified throughout Requirement 7. While it is important to define the specific policies or procedures called out in Requirement 7, it is equally important to ensure they are properly documented, maintained, and disseminated.
**Guidance - Good Practice:**It is important to update policies and procedures as needed to address changes in processes, technologies, and business objectives. For this reason, consider updating these documents as soon as possible after a change occurs and not only on a periodic cycle.
**Guidance - Definitions:**Security policies define the entity's security objectives and principles. Operational procedures describe how to perform activities, and define the controls, methods, and processes that are followed to achieve the desired result in a consistent manner and in accordance with policy objectives.

---
**Control objectives:**7.1
**Sub-requirement:**7.1.2
**Defined Approach Requirements:**Roles and responsibilities for performing activities in Requirement 7 are documented, assigned, and understood.
**Defined Approach Testing Procedures:**
- "7.1.2.a": Examine documentation to verify that descriptions of roles and responsibilities for performing activities in Requirement 7 are documented and assigned.
- "7.1.2.b": Interview personnel with responsibility performing activities in Requirement 7 to verify roles and responsibilities are assigned as and understood. 7.2 Access to system components and data is appropriately defined and assigned.
**Customized Approach Objective:**Day-to-day responsibilities for performing all the activities in Requirement 7 are allocated. Personnel are accountable for successful, continuous operation of these requirements.
**Guidance - Purpose:**If roles and responsibilities are not formally assigned, personnel may not be aware of their day-to-day responsibilities, and critical activities may not occur.
**Guidance - Good Practice:**Roles and responsibilities may be documented within policies and procedures or maintained within separate documents. As part of communicating roles and responsibilities, entities can consider having personnel acknowledge their acceptance and understanding of their assigned roles and responsibilities.
**Guidance - Examples:**A method to document roles and responsibilities is a responsibility assignment matrix that includes who is responsible, accountable, consulted, and informed (also called a RACI matrix). 7.2 Access to system components and data is appropriately defined and assigned. 7.2 Access to system components and data is appropriately defined and assigned.

================

### A. Tài liệu gốc của Requirement 7

### B. Summary Overview của Control Objective 7.2
Tài liệu này mô tả chi tiết **Control Objective 7.2** của **Requirement 7 **trong **PCI-DSS v4.0.1**, tập trung vào việc định nghĩa, cấp phát và kiểm soát quyền truy cập vào hệ thống và dữ liệu theo nguyên tắc least privilege.
Mục tiêu chính là đảm bảo quyền truy cập được cấp đúng theo vai trò công việc, được phê duyệt, kiểm soát định kỳ và giới hạn ở mức tối thiểu cần thiết.
Gồm 5 sub-requirement chính:
- 7.2.1: Định nghĩa mô hình kiểm soát truy cập
- 7.2.2: Cấp quyền theo vai trò và least privilege
- 7.2.3: Phê duyệt quyền truy cập
- 7.2.4: Review quyền truy cập định kỳ
- 7.2.5: Quản lý account hệ thống và ứng dụng
- 7.2.6: Kiểm soát truy vấn dữ liệu thẻ
Áp dụng cho toàn bộ user, system account, application account và quyền truy cập vào dữ liệu trong môi trường.

### C. Key Points của Control Objective 7.2
- **Phạm vi áp dụng:**Tất cả user, account và quyền truy cập hệ thống/dữ liệu
- **Trách nhiệm:**Phân rõ vai trò và kiểm soát cấp quyền theo job function
- **Kiểm soát truy cập:**Áp dụng least privilege và need-to-know
- **Phê duyệt:**Quyền truy cập phải được phê duyệt bởi người có thẩm quyền
- **Review định kỳ:**Kiểm tra quyền truy cập ít nhất 6 tháng/lần
- **Quản lý account:** Bao gồm cả user, system và application account
- **Kiểm soát dữ liệu:**Hạn chế truy vấn trực tiếp vào repository chứa CHD

### D. Deep Summary của Control Objective 7.2
**Bối cảnh:**
Cấp quyền truy cập không kiểm soát là nguyên nhân phổ biến dẫn đến truy cập trái phép và rò rỉ dữ liệu.
**Nội dung cốt lõi:**
- Xây dựng access control model dựa trên job function và least privilege
- Cấp quyền truy cập theo role và được phê duyệt
- Review định kỳ để đảm bảo quyền vẫn phù hợp
- Kiểm soát chặt chẽ account hệ thống và ứng dụng
- Hạn chế truy vấn trực tiếp dữ liệu thẻ, ưu tiên qua ứng dụng
**Dữ liệu đáng chú ý:**
- Review quyền truy cập tối thiểu 6 tháng/lần
- Áp dụng cho cả user account và system/application account
**Rủi ro / Lưu ý:**
- Cấp quyền quá mức → tăng nguy cơ lạm dụng hoặc compromise
- Không review định kỳ → quyền cũ vẫn tồn tại
- Account hệ thống có quyền cao → mục tiêu tấn công chính
- Truy vấn trực tiếp CHD → dễ bị lạm dụng và rò rỉ dữ liệu

### E. Structured Output của Control Objective 7.2
**Control objectives:**7.2
**Sub-requirement:**7.2.1
**Defined Approach Requirements:**An access control model is defined and includes granting access as follows:
• Appropriate access depending on the entity's business and access needs.
• Access to system components and data resources that is based on users' job classification and functions.
• The least privileges required (for example, user, administrator) to perform a job function.
**Defined Approach Testing Procedures:**
- "7.2.1.a": Examine documented policies and procedures and interview personnel to verify the access control model is defined in accordance with all elements specified in this requirement.
- "7.2.1.b": Examine access control model settings and verify that access needs are appropriately defined in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Access requirements are established according to job functions following least-privilege and need-to- know principles.
**Guidance - Purpose:**Defining an access control model that is appropriate for the entity's technology and access control philosophy supports a consistent and uniform way of allocating access and reduces the possibility of errors such as the granting of excessive rights.
**Guidance - Good Practice:**A factor to consider when defining access needs is the separation of duties principle. This principle is intended to prevent fraud and misuse or theft of resources. For example, 1) dividing mission- critical functions and information system support functions among different individuals and/or functions, 2) establishing roles such that information system support activities are performed by different functions/individuals (for example, system management, programming, configuration management, quality assurance and testing, and network security), and 3) ensuring security personnel administering access control functions do not also administer audit functions. In environments where one individual performs multiple functions, such as administration and security operations, duties may be assigned so that no single individual has end-to-end control of a process without an independent checkpoint. For example, responsibility for configuration and responsibility for approving changes could be assigned to separate individuals.
**Guidance - Definitions:**Key elements of an access control model include:
• Resources to be protected (the systems/devices/data to which access is needed),
• Job functions that need access to the resource (for example, system administrator, call-center personnel, store clerk), and
• Which activities each job function needs to perform (for example, read/write or query). Once job functions, resources, and activities per job functions are defined, individuals can be granted access accordingly.

---
**Control objectives:**7.2
**Sub-requirement:**7.2.2
**Defined Approach Requirements:**Access is assigned to users, including privileged users, based on:
• Job classification and function.
• Least privileges necessary to perform job responsibilities.
**Defined Approach Testing Procedures:**
- "7.2.2.a": Examine policies and procedures to verify they cover assigning access to users in accordance with all elements specified in this requirement.
- "7.2.2.b": Examine user access settings, including for privileged users, and interview responsible management personnel to verify that privileges assigned are in accordance with all elements specified in this requirement.
- "7.2.2.c": Interview personnel responsible for assigning access to verify that privileged user access is assigned in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Access to systems and data is limited to only the access needed to perform job functions, as defined in the related access roles.
**Guidance - Purpose:**Assigning least privileges helps prevent users without sufficient knowledge about the application from incorrectly or accidentally changing application configuration or altering its security settings. Enforcing least privilege also helps to minimize the scope of damage if an unauthorized person gains access to a user ID.
**Guidance - Good Practice:**Access rights are granted to a user by assignment to one or several functions. Access is assigned depending on the specific user functions and with the minimum scope required for the job. When assigning privileged access, it is important to assign individuals only the privileges they need to perform their job (the 'least privileges'). For example, the database administrator or backup administrator should not be assigned the same privileges as the overall systems administrator. Once needs are defined for user functions (per PCI DSS requirement 7.2.1), it is easy to grant individuals access according to their job classification and function by using the already- created roles. Entities may wish to consider use of Privileged Access Management (PAM), which is a method to grant access to privileged accounts only when those privileges are required, immediately revoking that access once they are no longer needed.

---
**Control objectives:**7.2
**Sub-requirement:**7.2.3
**Defined Approach Requirements:**Required privileges are approved by authorized personnel.
**Defined Approach Testing Procedures:**
- "7.2.3.a": Examine policies and procedures to verify they define processes for approval of all privileges by authorized personnel.
- "7.2.3.b": Examine user IDs and assigned privileges, and compare with documented approvals to verify that:
• Documented approval exists for the assigned privileges.
• The approval was by authorized personnel.
• Specified privileges match the roles assigned to the individual.
**Customized Approach Objective:**Access privileges cannot be granted to users without appropriate, documented authorization.
**Guidance - Purpose:**Documented approval (for example, in writing or electronically) assures that those with access and privileges are known and authorized by management, and that their access is necessary for their job function.

---
**Control objectives:**7.2
**Sub-requirement:**7.2.4
**Defined Approach Requirements:**All user accounts and related access privileges, including third-party/vendor accounts, are reviewed as follows:
• At least once every six months.
• To ensure user accounts and access remain appropriate based on job function.
• Any inappropriate access is addressed.
• Management acknowledges that access remains appropriate.
**Defined Approach Testing Procedures:**
- "7.2.4.a": Examine policies and procedures to verify they define processes to review all user accounts and related access privileges, including third- party/vendor accounts, in accordance with all elements specified in this requirement.
- "7.2.4.b": Interview responsible personnel and examine documented results of periodic reviews of user accounts to verify that all the results are in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Account privilege assignments are verified periodically by management as correct, and nonconformities are remediated.
**Applicability Notes:**This requirement applies to all user accounts and related access privileges, including those used by personnel and third parties/vendors, and accounts used to access third-party cloud services. See Requirements 7.2.5 and 7.2.5.1 and 8.6.1 through 8.6.3 for controls for application and system accounts. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Regular review of access rights helps to detect excessive access rights remaining after user job responsibilities change, system functions change, or other modifications. If excessive user rights are not revoked in due time, they may be used by malicious users for unauthorized access. This review provides another opportunity to ensure that accounts for all terminated users have been removed (if any were missed at the time of termination), as well as to ensure that any third parties that no longer need access have had their access terminated.
**Guidance - Good Practice:**When a user transfers into a new role or a new department, typically the privileges and access associated with their former role are no longer required. Continued access to privileges or functions that are no longer required may introduce the risk of misuse or errors. Therefore, when responsibilities change, processes that revalidate access help to ensure user access is appropriate for the user's new responsibilities. Entities can consider implementing a regular, repeatable process for conducting reviews of access rights, and assigning 'data owners' that are responsible for managing and monitoring access to data related to their job function and that also ensure user access remains current and appropriate. As an example, a direct manager could review team access monthly, while the senior manager reviews their groups' access quarterly, both making updates to access as needed. The intent of these best practices is to support and facilitate conducting the reviews at least once every 6 months.

---
**Control objectives:**7.2
**Sub-requirement:**7.2.5
**Defined Approach Requirements:**All application and system accounts and related access privileges are assigned and managed as follows:
• Based on the least privileges necessary for the operability of the system or application.
• Access is limited to the systems, applications, or processes that specifically require their use.
**Defined Approach Testing Procedures:**
- "7.2.5.a": Examine policies and procedures to verify they define processes to manage and assign application and system accounts and related access privileges in accordance with all elements specified in this requirement.
- "7.2.5.b": Examine privileges associated with system and application accounts and interview responsible personnel to verify that application and system accounts and related access privileges are assigned and managed in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Access rights granted to application and system accounts are limited to only the access needed for the operability of that application or system.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**It is important to establish the appropriate access level for application or system accounts. If such accounts are compromised, malicious users will receive the same access level as that granted to the application or system. Therefore, it is important to ensure limited access is granted to system and application accounts on the same basis as to user accounts.
**Guidance - Good Practice:**Entities may want to consider establishing a baseline when setting up these application and system accounts including the following as applicable to the organization:
• Making sure that the account is not a member of a privileged group such as domain administrators, local administrators, or root.
• Restricting which computers the account can be used on.
• Restricting hours of use.
• Removing any additional settings like VPN access and remote access.

---
**Control objectives:**7.2
**Sub-requirement:**7.2.5.1
**Defined Approach Requirements:**All access by application and system accounts and related access privileges are reviewed as follows:
• Periodically (at the frequency defined in the entity's targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1).
• The application/system access remains appropriate for the function being performed.
• Any inappropriate access is addressed.
• Management acknowledges that access remains appropriate.
**Defined Approach Testing Procedures:**
- "7.2.5.1.a": Examine policies and procedures to verify they define processes to review all application and system accounts and related access privileges in accordance with all elements specified in this requirement.
- "7.2.5.1.b": Examine the entity's targeted risk analysis for the frequency of periodic reviews of application and system accounts and related access privileges to verify the risk analysis was performed in accordance with all elements specified in Requirement 12.3.1.
- "7.2.5.1.c": Interview responsible personnel and examine documented results of periodic reviews of system and application accounts and related privileges to verify that the reviews occur in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Application and system account privilege assignments are verified periodically by management as correct, and nonconformities are remediated.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Regular review of access rights helps to detect excessive access rights remaining after system functions change, or other application or system modifications occur. If excessive rights are not removed when no longer needed, they may be used by malicious users for unauthorized access.

---
**Control objectives:**7.2
**Sub-requirement:**7.2.6
**Defined Approach Requirements:**All user access to query repositories of stored cardholder data is restricted as follows:
• Via applications or other programmatic methods, with access and allowed actions based on user roles and least privileges.
• Only the responsible administrator(s) can directly access or query repositories of stored CHD.
**Defined Approach Testing Procedures:**
- "7.2.6.a": Examine policies and procedures and interview personnel to verify processes are defined for granting user access to query repositories of stored cardholder data, in accordance with all elements specified in this requirement.
- "7.2.6.b": Examine configuration settings for querying repositories of stored cardholder data to verify they are in accordance with all elements specified in this requirement. 7.3 Access to system components and data is managed via an access control system(s).
**Customized Approach Objective:**Direct unfiltered (ad hoc) query access to cardholder data repositories is prohibited, unless performed by an authorized administrator.
**Applicability Notes:**This requirement applies to controls for user access to query repositories of stored cardholder data. See Requirements 7.2.5 and 7.2.5.1 and 8.6.1 through 8.6.3 for controls for application and system accounts.
**Guidance - Purpose:**The misuse of query access to repositories of cardholder data has been a regular cause of data breaches. Limiting such access to administrators reduces the risk of such access being abused by unauthorized users.
**Guidance - Good Practice:**Typical user actions include moving, copying, and deleting data. Also consider the scope of privilege needed when granting access. For example, access can be granted to specific objects such as data elements, files, tables, indexes, views, and stored routines. Granting access to repositories of cardholder data should follow the same process as all other granted access, meaning that it is based on roles, with only the privileges assigned to each user that are needed to perform their job functions.
**Guidance - Definitions:**'Programmatic methods' means granting access through means such as database stored procedures that allow users to perform controlled actions to data in a table, rather than via direct, unfiltered access to the data repository by end users (except for the responsible administrator(s), who need direct access to the database for their administrative duties).

================

### A. Tài liệu gốc của Requirement 7

### B. Summary Overview của Control Objective 7.3
Tài liệu này mô tả chi tiết **Control Objective 7.3 **của **Requirement 7** trong **PCI-DSS v4.0.1**, tập trung vào việc triển khai và cấu hình hệ thống kiểm soát truy cập để thực thi các quyền đã được định nghĩa.
Mục tiêu chính là đảm bảo quyền truy cập được thực thi tự động thông qua access control system, dựa trên nguyên tắc need-to-know và least privilege.
Gồm 3 sub-requirement chính:
- 7.3.1: Triển khai access control system
- 7.3.2: Thực thi quyền truy cập theo role
- 7.3.3: Cấu hình mặc định deny all
Áp dụng cho tất cả system components, user, application và hệ thống truy cập.

### C. Key Points của Control Objective 7.3
- **Phạm vi áp dụng:**Tất cả system components và cơ chế kiểm soát truy cập
- **Trách nhiệm:** Triển khai và cấu hình access control system đúng nguyên tắc
- **Kiểm soát truy cập:** Áp dụng need-to-know và least privilege
- **Thực thi quyền:** Quyền được enforce tự động qua system
- **Cấu hình mặc định:** Phải thiết lập deny all

### D. Deep Summary của Control Objective 7.3
**Bối cảnh:**
Nếu không có cơ chế tự động thực thi quyền truy cập, việc cấp quyền có thể bị sai sót hoặc bị lạm dụng, dẫn đến truy cập trái phép.
**Nội dung cốt lõi:**
- Triển khai access control system bao phủ toàn bộ system components
- Thực thi quyền truy cập dựa trên role và job function
- Đảm bảo quyền chỉ được cấp theo need-to-know
- Cấu hình mặc định deny all, chỉ cho phép khi có rule rõ ràng
**Dữ liệu đáng chú ý:**
- Access control system phải quản lý cả user, application và system account
- Quyền truy cập được kế thừa từ group/role
**Rủi ro / Lưu ý:**
- Không có access control system → khó kiểm soát truy cập
- Cấu hình allow by default → mở rộng quyền ngoài kiểm soát
- Không enforce role-based → dễ cấp sai quyền
- Không áp dụng deny all → tăng nguy cơ truy cập trái phép

### E. Structured Output của Control Objective 7.3
**Control objectives:**7.3
**Sub-requirement:**7.3.1
**Defined Approach Requirements:**An access control system(s) is in place that restricts access based on a user's need to know and covers all system components.
**Defined Approach Testing Procedures:**Examine vendor documentation and system settings to verify that access is managed for each system component via an access control system(s) that restricts access based on a user's need to know and covers all system components.
**Customized Approach Objective:**Access rights and privileges are managed via mechanisms intended for that purpose.
**Guidance - Purpose:**Without a mechanism to restrict access based on user's need to know, a user may unknowingly be granted access to cardholder data. Access control systems automate the process of restricting access and assigning privileges.

---
**Control objectives:**7.3
**Sub-requirement:**7.3.2
**Defined Approach Requirements:**The access control system(s) is configured to enforce permissions assigned to individuals, applications, and systems based on job classification and function.
**Defined Approach Testing Procedures:**Examine vendor documentation and system settings to verify that the access control system(s) is configured to enforce permissions assigned to individuals, applications, and systems based on job classification and function.
**Customized Approach Objective:**Individual account access rights and privileges to systems, applications, and data are only inherited from group membership.
**Guidance - Purpose:**Restricting privileged access with an access control system reduces the opportunity for errors in the assignment of permissions to individuals, applications, and systems.

---
**Control objectives:**7.3
**Sub-requirement:**7.3.3
**Defined Approach Requirements:**The access control system(s) is set to 'deny all' by default.
**Defined Approach Testing Procedures:**Examine vendor documentation and system settings to verify that the access control system(s) is set to 'deny all' by default.
**Customized Approach Objective:**Access rights and privileges are prohibited unless expressly permitted.
**Guidance - Purpose:**A default setting of 'deny all' ensures no one is granted access unless a rule is established specifically granting such access.
**Guidance - Good Practice:**It is important to check the default configuration of access control systems because some are set by default to 'allow all,' thereby permitting access unless/until a rule is written to specifically deny it.