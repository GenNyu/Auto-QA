### A. Tài liệu gốc của Chương 8 (Control 8.18, 8.19)

### B. Summary Overview của Chương 8 (Control 8.18, 8.19)
Tài liệu này mô tả chi tiết **mục 8.18 và 8.19** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào việc kiểm soát các công cụ tiện ích có quyền cao và quản lý việc cài đặt phần mềm trên hệ thống vận hành.
Mục tiêu là **ngăn công cụ quản trị bị lạm dụng để vượt kiểm soát và bảo đảm mọi phần mềm cài trên hệ thống vận hành đều được phê duyệt, kiểm thử và quản lý đúng cách**.
Gồm 2 mục chính:
- `8.18`: Use of privileged utility programs - kiểm soát công cụ tiện ích đặc quyền
- `8.19`: Installation of software on operational systems - kiểm soát cài đặt phần mềm trên hệ thống vận hành

Áp dụng cho utility programs, phần mềm vận hành, quy trình update, môi trường production và các hoạt động cài đặt hoặc nâng cấp phần mềm có thể ảnh hưởng đến an toàn thông tin.

### C. Key Points của Chương 8 (Control 8.18, 8.19)
- **Mục tiêu quản trị:** `8.18` ngăn việc dùng utility để vượt kiểm soát hệ thống; `8.19` bảo đảm phần mềm vận hành được cài đặt an toàn và không đưa mã không được phép vào production.
- **Yêu cầu chính của 8.18:** Các utility programs có khả năng ghi đè system/application controls phải bị giới hạn cho số ít người tin cậy, có xác thực riêng, log đầy đủ và chỉ dùng trong phạm vi được phép.
- **Yêu cầu chính của 8.19:** Cài đặt và cập nhật phần mềm trên operational systems phải do người được ủy quyền thực hiện, qua quy trình test, approval, rollback và logging đầy đủ.
- **Điểm vận hành quan trọng:** `8.18` cần tách biệt utility khỏi ứng dụng và giới hạn thời gian sử dụng; `8.19` cần kiểm soát chặt vendor software, open source, source libraries và quyền cài đặt của người dùng.
- **Lưu ý thực tế:** Khi bên thứ ba tham gia cài đặt hoặc cập nhật, quyền truy cập vật lý hoặc logic phải có lý do chính đáng và được giám sát, vì đây là điểm dễ phát sinh rủi ro chuỗi cung ứng.

### D. Deep Summary của Chương 8 (Control 8.18, 8.19)
**Bối cảnh:**
Hai control này bảo vệ lớp vận hành thực tế của hệ thống trước những thay đổi có quyền cao. Utility programs thường là công cụ mạnh, có thể vượt qua bảo vệ thông thường; còn việc cài phần mềm lên hệ thống vận hành nếu không kiểm soát sẽ tạo ra backdoor, lỗi hoặc lỗ hổng mới. Cả hai đều là điểm chuyển đổi từ quản trị sang thao tác kỹ thuật, nên đòi hỏi quy trình, phân quyền và bằng chứng rõ ràng.

**Nội dung cốt lõi:**
- `8.18` yêu cầu giới hạn utility programs cho số ít người được tin cậy, xác thực và phân quyền rõ, đồng thời ghi log mọi lần sử dụng.
- `8.18` nhấn mạnh việc tách utility khỏi application software và hạn chế thời gian cấp quyền để tránh dùng sai mục đích.
- `8.19` yêu cầu quản lý cài đặt phần mềm trên operational systems bằng quy trình chặt chẽ, từ phê duyệt, test, update source libraries, rollback đến audit log.
- `8.19` cũng yêu cầu chỉ cài approved executable code, không mang development code hoặc compiler vào production.
- `8.19` xử lý cả rủi ro từ vendor software, open source software và phụ thuộc vào nguồn phần mềm chưa được duy trì.

**Dữ liệu đáng chú ý:**
- `8.18` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#System_and_network_security#Secure_configuration#Application_security` và miền `#Protection`.
- `8.19` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Secure_configuration#Application_security` và miền `#Protection`.
- `8.18` yêu cầu unique identification cho người dùng utility program và hạn chế availability của utility theo nhu cầu.
- `8.19` nhấn mạnh least privilege cho việc cài phần mềm trên operational systems.
- `8.19` xem rollback strategy và lưu trữ version cũ như một phần của contingency cho vận hành.

**Rủi ro / Lưu ý:**
- Nếu utility programs không bị kiểm soát chặt, người dùng có thể vượt qua các control hệ thống hoặc chỉnh sửa dữ liệu và cấu hình trái phép.
- Nếu cài phần mềm vào production mà không test hoặc không có rollback, tổ chức có thể gây gián đoạn hệ thống hoặc tạo lỗ hổng mới.
- Nếu vendor/open source software không được quản lý vòng đời, hệ thống vận hành có thể phụ thuộc vào phần mềm không còn được hỗ trợ.
- Nếu quyền cài đặt phần mềm không gắn với vai trò và giám sát, người dùng có thể đưa vào phần mềm không mong muốn hoặc có nguồn gốc đáng ngờ.

### E. Structured Output của Chương 8 (Control 8.18, 8.19)
**Section:** 8.18
**Title:** Use of privileged utility programs

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #System_and_network_security #Secure_configuration #Application_security |
| Security domains | #Protection |

**Control:**
The use of utility programs that can be capable of overriding system and application controls should be restricted and tightly controlled.

**Purpose:**
To ensure the use of utility programs does not harm system and application controls for information security.

**Guidance:**
The following guidelines for the use of utility programs that can be capable of overriding system and application controls should be considered:
- limitation of the use of utility programs to the minimum practical number of trusted, authorized users (see 8.2);
- use of identification, authentication and authorization procedures for utility programs, including unique identification of the person who uses the utility program;
- defining and documenting of authorization levels for utility programs;
- authorization for ad hoc use of utility programs;
- not making utility programs available to users who have access to applications on systems where segregation of duties is required;
- removing or disabling all unnecessary utility programs;
- at a minimum, logical segregation of utility programs from application software. Where practical, segregating network communications for such programs from application traffic;
- limitation of the availability of utility programs (e.g. for the duration of an authorized change);
- logging of all use of utility programs.

**Other information:**
Most information systems have one or more utility programs that can be capable of overriding system and application controls, for example diagnostics, patching, antivirus, disk defragmenters, debuggers, backup and network tools.

---
**Section:** 8.19
**Title:** Installation of software on operational systems

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Secure_configuration #Application_security |
| Security domains | #Protection |

**Control:**
Procedures and measures should be implemented to securely manage software installation on operational systems.

**Purpose:**
To ensure the integrity of operational systems and prevent exploitation of technical vulnerabilities.

**Guidance:**
The following guidelines should be considered to securely manage changes and installation of software on operational systems:
- performing updates of operational software only by trained administrators upon appropriate management authorization (see 8.5);
- ensuring that only approved executable code and no development code or compilers is installed on operational systems;
- only installing and updating software after extensive and successful testing (see 8.29 and 8.31);
- updating all corresponding program source libraries;
- using a configuration control system to keep control of all operational software as well as the system documentation;
- defining a rollback strategy before changes are implemented;
- maintaining an audit log of all updates to operational software;
- archiving old versions of software, together with all required information and parameters, procedures, configuration details and supporting software as a contingency measure, and for as long as the software is required to read or process archived data.

Any decision to upgrade to a new release should take into account the business requirements for the change and the security of the release (e.g. the introduction of new information security functionality or the number and severity of information security vulnerabilities affecting the current version). Software patches should be applied when they can help to remove or reduce information security vulnerabilities (see 8.8 and 8.19).

Computer software can rely on externally supplied software and packages (e.g. software programs using modules which are hosted on external sites), which should be monitored and controlled to avoid unauthorized changes, because they can introduce information security vulnerabilities.

Vendor supplied software used in operational systems should be maintained at a level supported by the supplier. Over time, software vendors will cease to support older versions of software. The organization should consider the risks of relying on unsupported software. Open source software used in operational systems should be maintained to the latest appropriate release of the software. Over time, open source code can cease to be maintained but is still available in an open source software repository. The organization should also consider the risks of relying on unmaintained open source software when used in operational systems.

When suppliers are involved in installing or updating software, physical or logical access should only be given when necessary and with appropriate authorization. The supplier’s activities should be monitored (see 5.22).

The organization should define and enforce strict rules on which types of software users can install.

The principle of least privilege should be applied to software installation on operational systems. The organization should identify what types of software installations are permitted (e.g. updates and security patches to existing software) and what types of installations are prohibited (e.g. software that is only for personal use and software whose pedigree with regard to being potentially malicious is unknown or suspect). These privileges should be granted based on the roles of the users concerned.

**Other information:**
No other information.
