### A. Tài liệu gốc của Chương 8 (Control 8.28)

### B. Summary Overview của Chương 8 (Control 8.28)
Tài liệu này mô tả chi tiết **mục 8.28** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào việc viết mã an toàn trong suốt vòng đời phát triển phần mềm.
Mục tiêu là **giảm số lượng lỗ hổng an ninh xuất hiện từ source code, từ giai đoạn thiết kế, lập trình, kiểm thử đến bảo trì và triển khai**.
Gồm 1 mục chính:
- `8.28`: Secure coding - áp dụng nguyên tắc lập trình an toàn để giảm lỗ hổng phần mềm

Áp dụng cho phát triển phần mềm nội bộ, phần mềm thuê ngoài, thư viện bên thứ ba, môi trường dev/test/prod và các ứng dụng web hoặc hệ thống có nguy cơ bị khai thác do lỗi mã nguồn.

### C. Key Points của Chương 8 (Control 8.28)
- **Mục tiêu quản trị:** `8.28` đưa an ninh vào từng bước coding, từ planning, secure design, coding practices, review, testing đến maintenance.
- **Yêu cầu chính:** Tổ chức phải có secure coding standards, baseline an toàn, kiểm soát công cụ phát triển, threat modelling và đào tạo developer.
- **Yêu cầu vận hành quan trọng:** Mã nguồn phải được review, test, package và triển khai an toàn; lỗ hổng được báo cáo phải được xử lý và log phải được theo dõi định kỳ.
- **Quản lý thành phần ngoài:** External libraries, open source, vendor components và compiled/interpreted code đều phải được kiểm soát, cập nhật và đánh giá rủi ro.
- **Lưu ý thực tế:** Secure coding không chỉ là viết code sạch; tổ chức phải loại bỏ insecure design patterns như hard-coded passwords, unapproved samples hoặc web services không xác thực.

### D. Deep Summary của Chương 8 (Control 8.28)
**Bối cảnh:**
Đây là control cốt lõi để ngăn lỗi an ninh ngay từ source code. Rất nhiều sự cố bảo mật không bắt nguồn từ hạ tầng mà từ quyết định lập trình sai hoặc thiếu kiểm soát trong quy trình phát triển. Secure coding nhằm biến an ninh thành một thuộc tính mặc định của phần mềm, không phải một bản vá về sau.

**Nội dung cốt lõi:**
- `8.28` yêu cầu tổ chức xây dựng governace cho secure coding trên toàn bộ SDLC và mở rộng sang third-party/open source components.
- `8.28` nhấn mạnh planning trước khi code: tiêu chuẩn coding, developer capability, secure design, threat modelling, công cụ phát triển và môi trường kiểm soát.
- `8.28` yêu cầu coding practices an toàn trong quá trình lập trình, bao gồm pair programming, peer review, refactoring, structured programming và test-driven development.
- `8.28` yêu cầu theo dõi sau khi code đi vào vận hành: update an toàn, xử lý vulnerability, log error/attack, và bảo vệ source code khỏi truy cập trái phép.
- `8.28` cũng xem xét rủi ro từ code nhúng, interpreted code, web apps, database injection và cross-site scripting trong bối cảnh triển khai thực tế.

**Dữ liệu đáng chú ý:**
- `8.28` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Application_security#System_and_network_security` và miền `#Protection`.
- `8.28` có liên hệ chặt với `8.25`, `8.29`, `8.4`, `8.9`, `8.32` và `5.8`.
- `8.28` khuyến khích secure repositories, secure coding standards và controlled environments cho development.
- `8.28` nhấn mạnh bảo vệ code khỏi tampering và bảo đảm security-relevant code được gọi khi cần.
- `8.28` có tham chiếu đến ISO/IEC 15408 cho ICT security evaluation.

**Rủi ro / Lưu ý:**
- Nếu developer không được đào tạo hoặc không có chuẩn coding an toàn, lỗ hổng sẽ được đưa vào phần mềm ngay từ đầu.
- Nếu review và testing lỏng lẻo, các lỗi như injection, XSS hoặc logic flaw có thể đi vào production.
- Nếu external libraries không được quản lý, tổ chức có thể vô tình mang lỗ hổng từ bên thứ ba vào sản phẩm của mình.
- Nếu source code hoặc scripts không được bảo vệ, attacker có thể sửa đổi hoặc khai thác trực tiếp logic ứng dụng.

### E. Structured Output của Chương 8 (Control 8.28)
**Section:** 8.28
**Title:** Secure coding

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Application_security #System_and_network_security |
| Security domains | #Protection |

**Control:**
Secure coding principles should be applied to software development.

**Purpose:**
To ensure software is written securely thereby reducing the number of potential information security vulnerabilities in the software.

**Guidance:**
***General***
The organization should establish organization-wide processes to provide good governance for secure coding. A minimum secure baseline should be established and applied. Additionally, such processes and governance should be extended to cover software components from third parties and open source software.

The organization should monitor real world threats and up-to-date advice and information on software vulnerabilities to guide the organization’s secure coding principles through continual improvement and learning. This can help with ensuring effective secure coding practices are implemented to combat the fast-changing threat landscape.

***Planning and before coding***
Secure coding principles should be used both for new developments and in reuse scenarios. These principles should be applied to development activities both within the organization and for products and services supplied by the organization to others. Planning and prerequisites before coding should include:
- organization-specific expectations and approved principles for secure coding to be used for both in-house and outsourced code developments;
- common and historical coding practices and defects that lead to information security vulnerabilities;
- configuring development tools, such as integrated development environments (IDE), to help enforce the creation of secure code;
- following guidance issued by the providers of development tools and execution environments as applicable;
- maintenance and use of updated development tools (e.g. compilers);
- qualification of developers in writing secure code;
- secure design and architecture, including threat modelling;
- secure coding standards and where relevant mandating their use;
- use of controlled environments for development.

***During coding***
Considerations during coding should include:
- secure coding practices specific to the programming languages and techniques being used;
- using secure programming techniques, such as pair programming, refactoring, peer review, security iterations and test-driven development;
- using structured programming techniques;
- documenting code and removing programming defects, which can allow information security vulnerabilities to be exploited;
- prohibiting the use of insecure design techniques (e.g. the use of hard-coded passwords, unapproved code samples and unauthenticated web services).

Testing should be conducted during and after development (see 8.29). Static application security testing (SAST) processes can identify security vulnerabilities in software.

Before software is made operational, the following should be evaluated:
- attack surface and the principle of least privilege;
- conducting an analysis of the most common programming errors and documenting that these have been mitigated.

***Review and maintenance***
After code has been made operational:
- updates should be securely packaged and deployed;
- reported information security vulnerabilities should be handled (see 8.8);
- errors and suspected attacks should be logged and logs regularly reviewed to make adjustments to the code as necessary;
- source code should be protected against unauthorized access and tampering (e.g. by using configuration management tools, which typically provide features such as access control and version control).

If using external tools and libraries, the organization should consider:
- ensuring that external libraries are managed (e.g. by maintaining an inventory of libraries used and their versions) and regularly updated with release cycles;
- selection, authorization and reuse of well-vetted components, particularly authentication and cryptographic components;
- the licence, security and history of external components;
- ensuring that software is maintainable, tracked and originates from proven, reputable sources;
- sufficiently long-term availability of development resources and artefacts.

Where a software package needs to be modified the following points should be considered:
- the risk of built-in controls and integrity processes being compromised;
- whether to obtain the consent of the vendor;
- the possibility of obtaining the required changes from the vendor as standard program updates;
- the impact if the organization becomes responsible for the future maintenance of the software as a result of changes;
- compatibility with other software in use.

**Other information:**
A guiding principle is to ensure security-relevant code is invoked when necessary and is tamperresistant. Programs installed from compiled binary code also have these properties but only for data held within the application. For interpreted languages, the concept only works when the code is executed on a server that is otherwise inaccessible by the users and processes that use it, and that its data is held in a similarly protected database. For example, the interpreted code can be run on a cloud service where access to the code itself requires administrator privileges. Such administrator access should be protected by security mechanisms such as just-in-time administration principles and strong authentication. If the application owner can access scripts by direct remote access to the server, so in principle can an attacker. Webservers should be configured to prevent directory browsing in such cases.

Application code is best designed on the assumption that it is always subject to attack, through error or malicious action. In addition, critical applications can be designed to be tolerant of internal faults. For example, the output from a complex algorithm can be checked to ensure that it lies within safe bounds before the data is used in an application such as a safety or financial critical application. The code that performs the boundary checks is simple and therefore much easier to prove correctness.

Some web applications are susceptible to a variety of vulnerabilities that are introduced by poor design and coding, such as database injection and cross-site scripting attacks. In these attacks, requests can be manipulated to abuse the webserver functionality.

More information on ICT security evaluation can be found in the ISO/IEC 15408 series.