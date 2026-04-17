### A. Tài liệu gốc của Chương 8 (Control 8.2, 8.3)

### B. Summary Overview của Chương 8 (Control 8.2, 8.3)
Tài liệu này mô tả chi tiết **mục 8.2 và 8.3** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào việc kiểm soát quyền đặc quyền và giới hạn truy cập thông tin theo chính sách đã được thiết lập.
Mục tiêu là **ngăn lạm dụng quyền quản trị và bảo đảm chỉ đúng người, đúng thời điểm, đúng phạm vi mới được truy cập thông tin hoặc tài sản liên quan**.
Gồm 2 mục chính:
- `8.2`: Privileged access rights - quản lý quyền đặc quyền một cách chặt chẽ
- `8.3`: Information access restriction - hạn chế truy cập thông tin theo chính sách và cơ chế kỹ thuật phù hợp

Áp dụng cho tài khoản đặc quyền, hệ thống quản trị, ứng dụng, dữ liệu nhạy cảm và các cơ chế kiểm soát truy cập được dùng trong toàn bộ môi trường công nghệ của tổ chức.

### C. Key Points của Chương 8 (Control 8.2, 8.3)
- **Mục tiêu quản trị:** `8.2` giảm rủi ro lạm dụng quyền cao; `8.3` bảo đảm việc truy cập thông tin được giới hạn theo nhu cầu, phân quyền và mức độ nhạy cảm của dữ liệu.
- **Yêu cầu chính của 8.2:** Quyền đặc quyền phải được cấp có kiểm soát, chỉ cho người có năng lực phù hợp, có thời hạn, có log, không dùng chung danh tính và được rà soát lại sau thay đổi tổ chức.
- **Yêu cầu chính của 8.3:** Tổ chức phải áp dụng cơ chế hạn chế truy cập thông tin theo topic-specific policy, bao gồm kiểm soát truy cập theo vai trò, danh tính, nhóm, môi trường và mức độ dữ liệu.
- **Dynamic access management:** Với dữ liệu có giá trị cao hoặc cần chia sẻ ra ngoài, tổ chức nên xem xét cơ chế truy cập động để kiểm soát thời gian, bối cảnh, in ấn, ghi nhận sử dụng và rút quyền theo thời gian thực.
- **Lưu ý thực tế:** `8.2` và `8.3` hoạt động bổ trợ cho nhau: một bên kiểm soát người quản trị, bên kia kiểm soát phạm vi dữ liệu mà các tài khoản hoặc nhóm có thể tiếp cận.

### D. Deep Summary của Chương 8 (Control 8.2, 8.3)
**Bối cảnh:**
Nhóm control này xử lý lớp rủi ro logic quan trọng nhất trong môi trường công nghệ: quyền đặc quyền và quyền truy cập thông tin. Nếu quyền quản trị bị cấp quá rộng hoặc danh tính đặc quyền bị dùng sai, toàn bộ cấu hình bảo mật có thể bị vô hiệu. Nếu truy cập thông tin không được giới hạn đúng cách, dữ liệu nhạy cảm có thể bị xem, sao chép hoặc phân phối ngoài ý muốn.

**Nội dung cốt lõi:**
- `8.2` yêu cầu kiểm soát toàn bộ vòng đời quyền đặc quyền: xác định nhu cầu, cấp theo từng sự kiện, có phê duyệt, đặt thời hạn, log đầy đủ và rà soát lại định kỳ.
- `8.2` nhấn mạnh không dùng chung tài khoản quản trị, không dùng danh tính đặc quyền cho tác vụ thường ngày và nên có cơ chế nâng quyền tạm thời khi thật sự cần.
- `8.3` đặt ra nguyên tắc rằng truy cập vào thông tin và tài sản liên quan phải đi theo topic-specific policy, không dựa vào sự thuận tiện của người dùng hay cấu hình mặc định của hệ thống.
- `8.3` mở rộng từ kiểm soát truy cập truyền thống sang dynamic access management, nơi quyền có thể phụ thuộc vào danh tính, thiết bị, vị trí, thời gian, ứng dụng và mức độ nhạy cảm của thông tin.
- `8.3` còn yêu cầu ghi nhận ai đã truy cập, thông tin được dùng như thế nào, và cảnh báo khi có dấu hiệu lạm dụng, để hỗ trợ điều tra hoặc ứng phó sự cố sau này.

**Dữ liệu đáng chú ý:**
- `8.2` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Identity_and_access_management` và miền `#Protection`.
- `8.3` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Identity_and_access_management` và miền `#Protection`.
- `8.2` có tham chiếu đến ISO/IEC 29146 cho phần quản lý truy cập và bảo vệ nguồn lực ICT.
- `8.3` phân biệt rõ giữa access control truyền thống và dynamic access management, nhấn mạnh rằng hai lớp này bổ trợ chứ không thay thế nhau.
- `8.3` bao phủ cả việc chia sẻ thông tin ra ngoài tổ chức, nơi kiểm soát truy cập truyền thống có thể không còn đủ hiệu lực.

**Rủi ro / Lưu ý:**
- Nếu quyền đặc quyền không được kiểm soát chặt, một tài khoản quản trị bị lạm dụng có thể dẫn đến thay đổi cấu hình, vô hiệu hóa kiểm soát hoặc rò rỉ dữ liệu trên diện rộng.
- Nếu danh tính đặc quyền bị dùng cho việc thường ngày, nguy cơ nhấn nhầm thao tác, vô tình xóa/sửa dữ liệu hoặc bị tấn công qua phish sẽ tăng lên.
- Nếu truy cập thông tin không được giới hạn theo chính sách, người dùng có thể xem hoặc sao chép dữ liệu vượt quá nhu cầu công việc thực tế.
- Nếu không có log, theo dõi và khả năng rút quyền theo thời gian thực, tổ chức sẽ rất khó phát hiện và phản ứng khi dữ liệu bị lạm dụng.

### E. Structured Output của Chương 8 (Control 8.2, 8.3)
**Section:** 8.2
**Title:** Privileged access rights

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Identity_and_access_management |
| Security domains | #Protection |

**Control:**
The allocation and use of privileged access rights should be restricted and managed.

**Purpose:**
To ensure only authorized users, software components and services are provided with privileged access rights.

**Guidance:**
The allocation of privileged access rights should be controlled through an authorization process in accordance with the relevant topic-specific policy on access control (see 5.15). The following should be considered:
- identifying users who need privileged access rights for each system or process (e.g. operating systems, database management systems and applications);
- allocating privileged access rights to users as needed and on an event-by-event basis in line with the topic-specific policy on access control (see 5.15) (i.e. only to individuals with the necessary competence to carry out activities that require privileged access and based on the minimum requirement for their functional roles);
- maintaining an authorization process (i.e. determining who can approve privileged access rights, or not granting privileged access rights until the authorization process is complete) and a record of all privileges allocated;
- defining and implementing requirements for expiry of privileged access rights;
- taking measures to ensure that users are aware of their privileged access rights and when they are in privileged access mode. Possible measures include using specific user identities, user interface settings or even specific equipment;
- authentication requirements for privileged access rights can be higher than the requirements for normal access rights. Re-authentication or authentication step-up can be necessary before doing work with privileged access rights;
- regularly, and after any organizational change, reviewing users working with privileged access rights in order to verify if their duties, roles, responsibilities and competence still qualify them for working with privileged access rights (see 5.18);
- establishing specific rules in order to avoid the use of generic administration user IDs (such as “root”), depending on systems’ configuration capabilities. Managing and protecting authentication information of such identities (see 5.17);
- granting temporary privileged access just for the time window necessary to implement approved changes or activities (e.g. for maintenance activities or some critical changes), rather than permanently granting privileged access rights. This is often referred as break glass procedure, and often automated by privilege access management technologies;
- logging all privileged access to systems for audit purposes;
- not sharing or linking identities with privileged access rights to multiple persons, assigning each person a separate identity which allows assigning specific privileged access rights. Identities can be grouped (e.g. by defining an administrator group) in order to simplify the management of privileged access rights;
- only using identities with privileged access rights for undertaking administrative tasks and not for day-to-day general tasks [i.e. checking email, accessing the web (users should have a separate normal network identity for these activities)].

**Other information:**
Privileged access rights are access rights provided to an identity, a role or a process that allows the performance of activities that typical users or processes cannot perform. System administrator roles typically require privileged access rights.

Inappropriate use of system administrator privileges (any feature or facility of an information system that enables the user to override system or application controls) is a major contributory factor to failures or breaches of systems.

More information related to access management and the secure management of access to information and information and communications technologies resources can be found in ISO/IEC 29146.

---
**Section:** 8.3
**Title:** Information access restriction

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Identity_and_access_management |
| Security domains | #Protection |

**Control:**
Access to information and other associated assets should be restricted in accordance with the established topic-specific policy on access control.

**Purpose:**
To ensure only authorized access and to prevent unauthorized access to information and other associated assets.

**Guidance:**
Access to information and other associated assets should be restricted in accordance with the established topic-specific policies. The following should be considered in order to support access restriction requirements:
- not allowing access to sensitive information by unknown user identities or anonymously. Public or anonymous access should only be granted to storage locations that do not contain any sensitive information;
- providing configuration mechanisms to control access to information in systems, applications and services;
- controlling which data can be accessed by a particular user;
- controlling which identities or group of identities have which access, such as read, write, delete and execute;
- providing physical or logical access controls for the isolation of sensitive applications, application data, or systems.

Further, dynamic access management techniques and processes to protect sensitive information that has high value to the organization should be considered when the organization:
- needs granular control over who can access such information during what period and in what way;
- wants to share such information with people outside the organization and maintain control over who can access it;
- wants to dynamically manage, in real-time, the use and distribution of such information;
- wants to protect such information against unauthorized changes, copying and distribution (including printing);
- wants to monitor the use of the information;
- wants to record any changes to such information that take place in case a future investigation is required.

Dynamic access management techniques should protect information throughout its life cycle (i.e. creation, processing, storage, transmission and disposal), including:
- establishing rules on the management of dynamic access based on specific use cases considering:
  1. granting access permissions based on identity, device, location or application;
  2. leveraging the classification scheme in order to determine what information needs to be protected with dynamic access management techniques;
- establishing operational, monitoring and reporting processes and supporting technical infrastructure.

Dynamic access management systems should protect information by:
- requiring authentication, appropriate credentials or a certificate to access information;
- restricting access, for example to a specified time frame (e.g. after a given date or until a particular date);
- using encryption to protect information;
- defining the printing permissions for the information;
- recording who accesses the information and how the information is used;
- raising alerts if attempts to misuse the information are detected.

**Other information:**
Dynamic access management techniques and other dynamic information protection technologies can support the protection of information even when data is shared beyond the originating organization, where traditional access controls cannot be enforced. It can be applied to documents, emails or other files containing information to limit who can access the content and in what way. It can be at a granular level and be adapted over the life cycle of the information.

Dynamic access management techniques do not replace classical access management [e.g. using access control lists (ACLs)], but can add more factors for conditionality, real-time evaluation, just-in-time data reduction and other enhancements that can be useful for the most sensitive information. It offers a way to control access outside the organization’s environment. Incident response can be supported by dynamic access management techniques as permissions can be modified or revoked at any time.

Additional information on a framework for access management is provided in ISO/IEC 29146.