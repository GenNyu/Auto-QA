### A. Tài liệu gốc của Chương 8 (Control 8.31, 8.32)

### B. Summary Overview của Chương 8 (Control 8.31, 8.32)
Tài liệu này mô tả chi tiết **mục 8.31 và 8.32** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào tách biệt môi trường phát triển/kiểm thử/sản xuất, và quản lý thay đổi có kiểm soát đối với hệ thống và hạ tầng.
Mục tiêu là giảm rủi ro lỗi phát sinh từ dev/test, ngăn thay đổi trái phép vào production, đồng thời bảo đảm mọi thay đổi đều được đánh giá, phê duyệt, kiểm thử và triển khai có kiểm soát.
Gồm 2 control chính:
- `8.31`: Separation of development, test and production environments - tách biệt môi trường phát triển, kiểm thử và sản xuất để tránh ảnh hưởng chéo
- `8.32`: Change management - quản lý thay đổi để mọi cập nhật hệ thống đều đi qua quy trình kiểm soát

Áp dụng cho toàn bộ vòng đời hệ thống, từ phát triển, kiểm thử, phát hành đến vận hành và bảo trì.

### C. Key Points của Chương 8 (Control 8.31, 8.32)
- **Mục tiêu quản trị:** `8.31` bảo vệ production khỏi tác động từ dev/test; `8.32` bảo đảm mọi thay đổi được xem xét, thử nghiệm và phê duyệt trước khi áp dụng.
- **Yêu cầu chính của 8.31:** Phải có mức tách biệt phù hợp giữa các môi trường, không để công cụ phát triển lẫn vào production, và không đưa dữ liệu nhạy cảm sang dev/test nếu không có kiểm soát tương đương.
- **Yêu cầu chính của 8.32:** Mỗi thay đổi cần có đánh giá tác động, thẩm quyền phê duyệt, kiểm thử, kế hoạch triển khai, phương án dự phòng và hồ sơ đầy đủ.
- **Điểm vận hành quan trọng:** Cần ngăn một cá nhân tự ý sửa cả dev lẫn production; việc thay đổi hạ tầng, phần mềm và tài liệu vận hành phải được đồng bộ.
- **Lưu ý thực tế:** Nếu môi trường không tách bạch hoặc change management làm hình thức, lỗi cấu hình, thay đổi chưa kiểm thử và sự cố production sẽ tăng nhanh.

### D. Deep Summary của Chương 8 (Control 8.31, 8.32)
**Bối cảnh:**
Hai control này nằm ở lớp kiểm soát nền tảng của vận hành công nghệ. `8.31` xử lý nguy cơ do môi trường dev/test “rò” sang production, còn `8.32` xử lý nguy cơ thay đổi thiếu kiểm soát làm hệ thống mất ổn định hoặc mất an toàn.

**Nội dung cốt lõi:**
- `8.31` yêu cầu tổ chức xác định mức tách biệt cần thiết rồi triển khai bằng biện pháp kỹ thuật và quy trình, không chỉ dừng ở mô tả chính sách.
- `8.31` nhấn mạnh segregation of duties: người phát triển hoặc kiểm thử không nên đồng thời có khả năng sửa production mà không qua review/approval.
- `8.31` coi việc bảo vệ dev/test environment là bắt buộc, gồm vá lỗi, cấu hình an toàn, kiểm soát truy cập, giám sát thay đổi và sao lưu.
- `8.32` biến thay đổi thành một quy trình quản trị đầy đủ: phân tích tác động, phê duyệt, thông tin cho các bên liên quan, kiểm thử, triển khai và lưu vết.
- `8.32` mở rộng phạm vi sang cả tài liệu vận hành, kế hoạch continuity, response và recovery, nên đây là kiểm soát có tính hệ thống chứ không chỉ là kiểm soát kỹ thuật.

**Dữ liệu đáng chú ý:**
- `8.31` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Application_security#System_and_net-work_security` và miền `#Protection`.
- `8.32` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Application_security#System_and_net-work_security` và miền `#Protection`.
- `8.31` cho phép một số mô hình triển khai linh hoạt như pilot users, controlled rollout hoặc hai production environment song song, nhưng vẫn phải kiểm soát được trạng thái live.
- `8.32` áp dụng cho cả ứng dụng lẫn hạ tầng, bao gồm operating systems, databases và middleware platforms.
- `8.32` liên hệ trực tiếp với `8.29` vì change management phải bao gồm kiểm thử và chấp nhận kiểm thử.

**Rủi ro / Lưu ý:**
- Nếu dev/test và production dùng chung công cụ, dữ liệu hoặc quyền truy cập, một lỗi nhỏ có thể trở thành sự cố vận hành hoặc rò rỉ dữ liệu.
- Nếu thay đổi được triển khai mà không có rollback plan hoặc hồ sơ đầy đủ, việc phục hồi sau sự cố sẽ chậm và khó truy nguyên nguyên nhân.
- Nếu không cập nhật tài liệu vận hành và continuity plan sau khi thay đổi, đội vận hành có thể xử lý sai khi có sự cố thật.
- Nếu cho phép một người tự thay đổi cả dev và production mà không có review độc lập, rủi ro thao túng và lỗi không được phát hiện sẽ tăng đáng kể.

### E. Structured Output của Chương 8 (Control 8.31, 8.32)
---
**Section:** 8.31
**Title:** Separation of development, test and production environments

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Application_security #System_and_net-work_security |
| Security domains | #Protection |

**Control:**
Development, testing and production environments should be separated and secured.

**Purpose:**
To protect the production environment and data from compromise by development and test activities.

**Guidance:**
The level of separation between production, testing and development environments that is necessary to prevent production problems should be identified and implemented.

The following items should be considered:

- adequately separating development and production systems and operating them in different domains (e.g. in separate virtual or physical environments);
- defining, documenting and implementing rules and authorization for the deployment of software from development to production status;
- testing changes to production systems and applications in a testing or staging environment prior to being applied to production systems (see 8.29);
- not testing in production environments except in circumstances that have been defined and approved;
- compilers, editors and other development tools or utility programs not being accessible from production systems when not required;
- displaying appropriate environment identification labels in menus to reduce the risk of error;
- not copying sensitive information into the development and testing system environments unless equivalent controls are provided for the development and testing systems.

In all cases, development and testing environments should be protected considering:

- patching and updating of all the development, integration and testing tools (including builders, integrators, compilers, configuration systems and libraries);
- secure configuration of systems and software;
- control of access to the environments;
- monitoring of change to the environment and code stored therein;
- secure monitoring of the environments;
- taking backups of the environments.

A single person should not have the ability to make changes to both development and production without prior review and approval. This can be achieved for example through segregation of access rights or through rules that are monitored. In exceptional situations, additional measures such as detailed logging and real-time monitoring should be implemented in order to detect and act on unauthorized changes.

**Other information:**
Without adequate measures and procedures, developers and testers having access to production systems can introduce significant risks (e.g. unwanted modification of files or system environment, system failure, running unauthorized and untested code in production systems, disclosure of confidential data, data integrity and availability issues). There is a need to maintain a known and stable environment in which to perform meaningful testing and to prevent inappropriate developer access to the production environment.

Measures and procedures include carefully designed roles in conjunction with implementing segregation of duty requirements and having adequate monitoring processes in place.

Development and testing personnel also pose a threat to the confidentiality of production information. Development and testing activities can cause unintended changes to software or information if they share the same computing environment. Separating development, testing and production environments is therefore desirable to reduce the risk of accidental change or unauthorized access to production software and business data (see 8.33 for the protection of test information).

In some cases, the distinction between development, test and production environments can be deliberately blurred and testing can be carried out in a development environment or through controlled rollouts to live users or servers (e.g. small population of pilot users). In some cases, product testing can occur through live use of the product inside the organization. Furthermore, to reduce downtime of live deployments, two identical production environments can be supported where only one is live at any one time.

Supporting processes for the use of production data in development and testing environments (8.33) are necessary.

Organizations can also consider the guidance provided in this section for training environments when conducting end user training.

---
**Section:** 8.32
**Title:** Change management

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Application_security #System_and_net-work_security |
| Security domains | #Protection |

**Control:**
Changes to information processing facilities and information systems should be subject to change management procedures.

**Purpose:**
To preserve information security when executing changes.

**Guidance:**
Introduction of new systems and major changes to existing systems should follow agreed rules and a formal process of documentation, specification, testing, quality control and managed implementation. Management responsibilities and procedures should be in place to ensure satisfactory control of all changes.

Change control procedures should be documented and enforced to ensure the confidentiality, integrity and availability of information in information processing facilities and information systems, for the entire system development life cycle from the early design stages through all subsequent maintenance efforts.

Wherever practicable, change control procedures for ICT infrastructure and software should be integrated.

The change control procedures should include:

- planning and assessing the potential impact of changes considering all dependencies;
- authorization of changes;
- communicating changes to relevant interested parties;
- tests and acceptance of tests for the changes (see 8.29);
- implementation of changes including deployment plans;
- emergency and contingency considerations including fall-back procedures;
- maintaining records of changes that include all of the above;
- ensuring that operating documentation (see 5.37) and user procedures are changed as necessary to remain appropriate;
- ensuring that ICT continuity plans and response and recovery procedures (see 5.30) are changed as necessary to remain appropriate.

**Other information:**
Inadequate control of changes to information processing facilities and information systems is a common cause of system or security failures. Changes to the production environment, especially when transferring software from development to operational environment, can impact on the integrity and availability of applications.

Changing software can impact the production environment and vice versa.

Good practice includes the testing of ICT components in an environment segregated from both the production and development environments (see 8.31). This provides a means of having control over new software and allowing additional protection of operational information that is used for testing purposes. This should include patches, service packs and other updates.

Production environment includes operating systems, databases and middleware platforms. The control should be applied for changes of applications and infrastructures.