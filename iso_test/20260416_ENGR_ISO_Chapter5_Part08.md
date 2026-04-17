### A. Tài liệu gốc của Chương 5 (Control 5.17, 5.18)

### B. Summary Overview của Chương 5 (Control 5.17, 5.18)
Tài liệu này mô tả chi tiết **mục 5.17 và 5.18** trong **Chương 5 (Organizational controls)** của **ISO/IEC 27002:2022**, tập trung vào việc kiểm soát thông tin xác thực và quyền truy cập để bảo đảm chỉ đối tượng phù hợp mới có thể xác thực và truy cập tài sản thông tin.
Mục tiêu chung của nhóm nội dung này là làm cho cơ chế xác thực đáng tin cậy hơn, đồng thời bảo đảm quyền truy cập được cấp, rà soát, điều chỉnh và thu hồi theo đúng yêu cầu nghiệp vụ và mức kiểm soát của tổ chức.
Gồm 2 mục chính:
- `5.17`: Authentication information - kiểm soát việc cấp phát và quản lý thông tin xác thực theo quy trình quản trị rõ ràng
- `5.18`: Access rights - cấp, rà soát, sửa đổi và thu hồi quyền truy cập theo chính sách và quy tắc access control của tổ chức
Áp dụng cho bộ phận quản trị danh tính, quản trị truy cập, vận hành hệ thống và các bên chịu trách nhiệm cấp phát hoặc sử dụng thông tin xác thực.

### C. Key Points của Chương 5 (Control 5.17, 5.18)
- **Mục tiêu quản trị:** nhóm control này làm cho xác thực và quyền truy cập đi cùng một quy trình, thay vì xử lý rời rạc ở từng hệ thống.
- **Yêu cầu chính của 5.17:** thông tin xác thực phải được cấp phát và quản lý bằng quy trình quản trị, có hướng dẫn rõ cho người dùng về cách bảo vệ và sử dụng.
- **Yêu cầu chính của 5.18:** quyền truy cập phải được cấp, xem xét, sửa đổi và thu hồi theo policy và rule access control, không để quyền tồn tại theo quán tính.
- **Điểm vận hành quan trọng:** mật khẩu, PIN, token hay các dạng thông tin xác thực tạm thời phải được tạo, truyền và thay đổi theo cách an toàn để tránh lộ lọt hoặc dùng lại sai mục đích.
- **Lưu ý thực tế:** nếu không đồng bộ giữa xác thực và cấp quyền, tổ chức sẽ dễ phát sinh tài khoản dùng chung, quyền thừa hoặc cơ chế xác thực hình thức.

### D. Deep Summary của Chương 5 (Control 5.17, 5.18)
**Bối cảnh:**
Đây là nhóm control cốt lõi để kiểm soát “ai đang xác thực bằng gì” và “ai đang có quyền gì”. Nếu hai lớp này không được gắn chặt với nhau, tổ chức rất dễ mất kiểm soát ở cả khâu xác thực lẫn khâu truy cập.

**Nội dung cốt lõi:**
- `5.17` yêu cầu tổ chức quản lý thông tin xác thực theo quy trình, bao gồm cả việc hướng dẫn nhân sự cách xử lý password, PIN, token và các cơ chế xác thực tương tự.
- `5.17` nhấn mạnh tính an toàn ở khâu cấp phát ban đầu, thay đổi, truyền tải, lưu trữ và thay thế thông tin xác thực.
- `5.18` yêu cầu vòng đời quyền truy cập phải được điều khiển chặt: cấp đúng, duy trì đúng, rà soát đúng và thu hồi đúng lúc.
- `5.18` cũng buộc tổ chức gắn quyền truy cập với business need, segregation of duties và các quyết định phê duyệt có thể truy vết.
- Hai control này thường được triển khai cùng nhau vì xác thực là đầu vào của cấp quyền, còn quyền truy cập là đầu ra của quá trình xác minh danh tính.

**Dữ liệu đáng chú ý:**
- `5.17` gắn với `#Preventive`, `#Protect`, `#Identity_and_access_management`, `#Protection`, cho thấy đây là control nhằm ngăn chặn thất bại trong xác thực.
- `5.18` cũng là `#Preventive` và thuộc cùng miền quản trị truy cập, nên nội dung nghiêng về vận hành quyền hơn là chỉ quản trị nhận dạng.
- `5.17` liên hệ chặt với cơ chế password management, secure transmission và kiểm soát thay đổi thông tin xác thực.
- `5.18` liên hệ chặt với authorization, review định kỳ, role assignment và xử lý thay đổi hoặc chấm dứt quan hệ lao động/dịch vụ.

**Rủi ro / Lưu ý:**
- Nếu thông tin xác thực được cấp phát hoặc truyền tải không an toàn, tổ chức sẽ đối mặt với rủi ro lộ mật khẩu, PIN hoặc token ngay từ bước đầu.
- Nếu quyền truy cập không được review và thu hồi kịp thời, tài khoản cũ hoặc tài khoản đặc quyền sẽ trở thành điểm yếu kéo dài.
- Việc gom quá nhiều quyền vào một profile mà không rà soát theo vai trò thực tế sẽ làm tăng xác suất cấp thừa quyền.
- Nếu tách rời 5.17 và 5.18 khỏi quy trình vận hành hàng ngày, policy sẽ có nhưng kiểm soát thực tế không còn hiệu lực.

### E. Structured Output của Chương 5 (Control 5.17, 5.18)
**Section:** 5.17
**Title:** Authentication information

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Informationsecurity properties | #Confidentiality#Integrity#Availability |
| Cybersecurityconcepts | #Protect |
| Operationalcapabilities | #Identity_and_access_management |
| Security domains | #Protection |

**Control:**
Allocation and management of authentication information should be controlled by a management process, including advising personnel on the appropriate handling of authentication information.

**Purpose:**
To ensure proper entity authentication and prevent failures of authentication processes.

**Guidance:**
***Allocation of authentication information:***
The allocation and management process should ensure that:
- personal passwords or personal identification numbers (PINs) generated automatically during enrolment processes as temporary secret authentication information are non-guessable and unique for each person, and that users are required to change them after the first use;
- procedures are established to verify the identity of a user prior to providing new, replacement or temporary authentication information;
- authentication information, including temporary authentication information, is transmitted to users in a secure manner (e.g. over an authenticated and protected channel) and the use of unprotected (clear text) electronic mail messages for this purpose is avoided;
- users acknowledge receipt of authentication information;
- default authentication information as predefined or provided by vendors is changed immediately following installation of systems or software;
- records of significant events concerning allocation and management of authentication information are kept and their confidentiality is granted, and that the record-keeping method is approved (e.g. by using an approved password vault tool).
***User responsibilities:***
Any person having access to or using authentication information should be advised to ensure that:
- secret authentication information such as passwords are kept confidential. Personal secret authentication information is not to be shared with anyone. Secret authentication information used in the context of identities linked to multiple users or linked to non-personal entities are solely shared with authorized persons;
- affected or compromised authentication information is changed immediately upon notification of or any other indication of a compromise;
- when passwords are used as authentication information, strong passwords according to best practice recommendations are selected, for example:
  - passwords are not based on anything somebody else can easily guess or obtain using person-related information (e.g. names, telephone numbers and dates of birth);
  - passwords are not based on dictionary words or combinations thereof;
  - use easy to remember passphrases and try to include alphanumerical and special characters;
  - passwords have a minimum length;
- the same passwords are not used across distinct services and systems;
- the obligation to follow these rules is also included in terms and conditions of employment (see 6.2).
***Password management system:***
When passwords are used as authentication information, the password management system should:
- allow users to select and change their own passwords and include a confirmation procedure to address input errors;
- enforce strong passwords according to good practice recommendations [see c) of "User responsibilities"];
- force users to change their passwords at first login;
- enforce password changes as necessary, for example after a security incident, or upon termination or change of employment when a user has known passwords for identities that remain active (e.g. shared identities);
- prevent re-use of previous passwords;
- prevent the use of commonly-used passwords and compromised usernames, password combinations from hacked systems;
- not display passwords on the screen when being entered;
- store and transmit passwords in protected form.
Password encryption and hashing should be performed according to approved cryptographic techniques for passwords (see 8.24).

**Other information:**
Passwords or passphrases are a commonly used type of authentication information and are a common means of verifying a user’s identity. Other types of authentication information are cryptographic keys, data stored on hardware tokens (e.g. smart cards) that produce authentication codes and biometric data such as iris scans or fingerprints. Additional information can be found in the ISO/IEC 24760 series.
Requiring frequent change of passwords can be problematic because users can get annoyed by the frequent changes, forget new passwords, note them down in unsafe places, or choose unsafe passwords. Provision of single sign on (SSO) or other authentication management tools (e.g. password vaults) reduces the amount of authentication information that users are required to protect and can thereby increase the effectiveness of this control. However, these tools can also increase the impact of disclosure of authentication information.
Some applications require user passwords to be assigned by an independent authority. In such cases, a), c) and d) of "Password management system" do not apply.

---
**Section:** 5.18
**Title:** Access rights

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Informationsecurity properties | #Confidentiality#Integrity#Availability |
| Cybersecurityconcepts | #Protect |
| Operationalcapabilities | #Identity_and_access_management |
| Security domains | #Protection |

**Control:**
Access rights to information and other associated assets should be provisioned, reviewed, modified and removed in accordance with the organization’s topic-specific policy on and rules for access control.

**Purpose:**
To ensure access to information and other associated assets is defined and authorized according to the business requirements.

**Guidance:**
***Provision and revocation of access rights:***
The provisioning process for assigning or revoking physical and logical access rights granted to an entity’s authenticated identity should include:
- obtaining authorization from the owner of the information and other associated assets for the use of the information and other associated assets (see 5.9). Separate approval for access rights by management can also be appropriate;
- considering the business requirements and the organization’s topic-specific policy and rules on access control;
- considering segregation of duties, including segregating the roles of approval and implementation of the access rights and separation of conflicting roles;
- ensuring access rights are removed when someone does not need to access the information and other associated assets, in particular ensuring access rights of users who have left the organization are removed in a timely fashion;
- considering giving temporary access rights for a limited time period and revoking them at the expiration date, in particular for temporary personnel or temporary access required by personnel;
- verifying that the level of access granted is in accordance with the topic-specific policies on access control (see 5.15) and is consistent with other information security requirements such as segregation of duties (see 5.3);
- ensuring that access rights are activated (e.g. by service providers) only after authorization procedures are successfully completed;
- maintaining a central record of access rights granted to a user identifier (ID, logical or physical) to access information and other associated assets;
- modifying access rights of users who have changed roles or jobs;
- removing or adjusting physical and logical access rights, which can be done by removal, revocation or replacement of keys, authentication information, identification cards or subscriptions;
- maintaining a record of changes to users’ logical and physical access rights.
***Review of access rights:***
Regular reviews of physical and logical access rights should consider the following:
- users’ access rights after any change within the same organization (e.g. job change, promotion, demotion) or termination of employment (see 6.1 to 6.5);
- authorizations for privileged access rights.
***Consideration before change or termination of employment:***
A user’s access rights to information and other associated assets should be reviewed and adjusted or removed before any change or termination of employment based on the evaluation of risk factors such as:
- whether the termination or change is initiated by the user or by management and the reason for termination;
- the current responsibilities of the user;
- the value of the assets currently accessible.

**Other information:**
Consideration should be given to establishing user access roles based on business requirements that summarize a number of access rights into typical user access profiles. Access requests and reviews of access rights are easier managed at the level of such roles than at the level of particular rights.
Consideration should be given to including clauses in personnel contracts and service contracts that specify sanctions if unauthorized access is attempted by personnel (see 5.20, 6.2, 6.4, 6.6).
In cases of management-initiated termination, disgruntled personnel or external party users can deliberately corrupt information or sabotage information processing facilities. In cases of persons resigning or being dismissed, they can be tempted to collect information for future use.
Cloning is an efficient way for organizations to assign access to users. However, it should be done with care based on distinct roles identified by the organization rather than just cloning an identity with all associated access rights. Cloning has an inherent risk of resulting in excessive access rights to information and other associated assets.