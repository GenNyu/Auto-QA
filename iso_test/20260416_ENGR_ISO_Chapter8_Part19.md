### A. Tài liệu gốc của Chương 8 (Control 8.29, 8.30)

### B. Summary Overview của Chương 8 (Control 8.29, 8.30)
Tài liệu này mô tả chi tiết **mục 8.29 và 8.30** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào kiểm thử an ninh trong giai đoạn phát triển và kiểm soát hoạt động phát triển thuê ngoài.
Mục tiêu là **bảo đảm phần mềm được kiểm thử đúng cách trước khi đưa vào vận hành, đồng thời bảo đảm nhà cung cấp hoặc đơn vị phát triển thuê ngoài tuân thủ các yêu cầu an ninh đã cam kết**.
Gồm 2 mục chính:
- `8.29`: Security testing in development and acceptance - kiểm thử an ninh trong phát triển và nghiệm thu
- `8.30`: Outsourced development - kiểm soát phát triển hệ thống thuê ngoài

Áp dụng cho phát triển nội bộ, mua sắm phần mềm, kiểm thử bảo mật, môi trường test, quan hệ với nhà cung cấp và toàn bộ chuỗi cung ứng phát triển phần mềm.

### C. Key Points của Chương 8 (Control 8.29, 8.30)
- **Mục tiêu quản trị:** `8.29` bảo đảm security testing được tích hợp vào SDLC; `8.30` bảo đảm tổ chức vẫn kiểm soát được an ninh khi giao việc phát triển ra ngoài.
- **Yêu cầu chính của 8.29:** Cần có test process, test plan, môi trường kiểm thử phù hợp production, code review, vulnerability scanning, penetration testing và xác nhận đã khắc phục lỗi bảo mật.
- **Yêu cầu chính của 8.30:** Hợp đồng và cơ chế giám sát phải bao phủ secure design, coding, testing, threat model, acceptance testing, evidence về bảo mật và quyền audit nhà cung cấp.
- **Điểm vận hành quan trọng:** Kiểm thử không chỉ nhằm xác nhận chức năng mà còn phải phát hiện lỗi cấu hình, code yếu và lỗ hổng thiết kế trước khi release hoặc nghiệm thu.
- **Lưu ý thực tế:** Nếu môi trường test không giống production hoặc nhà cung cấp không bị ràng buộc bằng hợp đồng, kết quả kiểm thử và mức bảo đảm an ninh sẽ không đáng tin cậy.

### D. Deep Summary của Chương 8 (Control 8.29, 8.30)
**Bối cảnh:**
Hai control này nằm ở lớp kiểm soát trước khi hệ thống đi vào vận hành hoặc được chấp nhận chính thức. `8.29` xử lý rủi ro do lỗi chưa được phát hiện trong build mới, nâng cấp và phiên bản mới; `8.30` xử lý rủi ro khi năng lực phát triển nằm ngoài tổ chức nhưng vẫn ảnh hưởng trực tiếp đến mức an toàn của sản phẩm cuối cùng.

**Nội dung cốt lõi:**
- `8.29` yêu cầu kiểm thử an ninh được định nghĩa như một phần bắt buộc của vòng đời phát triển và nghiệm thu, thay vì làm theo kiểu phát sinh sau cùng.
- `8.29` nhấn mạnh kiểm thử phải bám theo yêu cầu đã xác định, bao gồm chức năng an ninh, secure coding và secure configuration.
- `8.29` cho phép dùng công cụ tự động nhưng vẫn cần đánh giá lại kết quả, xác nhận khắc phục và có kiểm thử độc lập khi chấp nhận hệ thống.
- `8.30` yêu cầu tổ chức chủ động dẫn dắt, giám sát và rà soát hoạt động phát triển thuê ngoài để bảo đảm yêu cầu an ninh được thực thi nhất quán.
- `8.30` mở rộng kiểm soát sang hợp đồng, sở hữu mã nguồn, threat model, bằng chứng kiểm thử, quyền audit và điều kiện pháp lý trong chuỗi cung ứng.

**Dữ liệu đáng chú ý:**
- `8.29` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Application_security#Information_securi-ty_assurance#System_and_net-work_security` và miền `#Protection`.
- `8.30` là kiểm soát `#Preventive#Detective`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#System_and_network_security#Application_security#Supplier_relationships_security` và miền `#Governance_and_Ecosystem#Protection`.
- `8.29` liên hệ trực tiếp với `8.25`, `8.28`, `8.31` và các hoạt động code review, scanning, penetration testing.
- `8.30` liên hệ trực tiếp với `5.20`, `5.32`, `8.25` đến `8.29`, `8.31` và yêu cầu về hợp đồng, quyền sở hữu, kiểm thử và lưu trữ mã nguồn.
- `8.29` coi môi trường test gần giống production là điều kiện quan trọng để kết quả kiểm thử có giá trị.

**Rủi ro / Lưu ý:**
- Nếu security testing chỉ làm cho có, lỗ hổng cấu hình hoặc logic sẽ lọt qua trước khi vào production.
- Nếu test environment khác xa production, các kết quả test có thể sai lệch và không phản ánh rủi ro thực.
- Nếu nhà cung cấp không bị ràng buộc bằng yêu cầu hợp đồng và quyền audit, tổ chức khó chứng minh được mức bảo đảm an ninh của phần mềm thuê ngoài.
- Nếu không yêu cầu bằng chứng kiểm thử hoặc không kiểm tra chất lượng deliverable, mã độc, lỗi bảo mật hoặc phần mềm thiếu kiểm soát có thể được bàn giao mà không bị phát hiện.

### E. Structured Output của Chương 8 (Control 8.29, 8.30)
**Section:** 8.29
**Title:** Security testing in development and acceptance

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Identify |
| Operational capabilities | #Application_security #Information_securi-ty_assurance #System_and_net-work_security |
| Security domains | #Protection |

**Control:**
Security testing processes should be defined and implemented in the development life cycle.

**Purpose:**
To validate if information security requirements are met when applications or code are deployed to the production environment.

**Guidance:**
Security testing should be an integral part of the testing for systems or components. New information systems, upgrades and new versions should be thoroughly tested and verified during the development processes.

Security testing should be conducted against a set of requirements, which can be expressed as functional or non-functional. Security testing should include testing of:

- security functions [e.g. user authentication (see 8.5), access restriction (see 8.3) and use of cryptography (see 8.24)]
- secure coding (see 8.28)
- secure configurations (see 8.9, 8.20 and 8.22) including that of operating systems, firewalls and other security components

Test plans should be determined using a set of criteria. The extent of testing should be in proportion to the importance, nature of the system and the potential impact of the change being introduced. The test plan should include:

- detailed schedule of activities and tests
- inputs and expected outputs under a range of conditions
- criteria to evaluate the results
- decision for further actions as necessary

The organization can leverage automated tools, such as code analysis tools or vulnerability scanners, and should verify the remediation of security related defects.

For in-house developments, such tests should initially be performed by the development team. Independent acceptance testing should then be undertaken to ensure that the system works as expected and only as expected (see 5.8). The following should be considered:

- performing code review activities as a relevant element for testing for security flaws, including unanticipated inputs and conditions
- performing vulnerability scanning to identify insecure configurations and system vulnerabilities
- performing penetration testing to identify insecure code and design

For outsourced development and purchasing components, an acquisition process should be followed. Contracts with the supplier should address the identified security requirements (see 5.20). Products and services should be evaluated against these criteria before acquisition.

Testing should be performed in a test environment that matches the target production environment as closely as possible to ensure that the system does not introduce vulnerabilities to the organization’s environment and that the tests are reliable (see 8.31).

**Other information:**
Multiple test environments can be established, which can be used for different kinds of testing (e.g. functional and performance testing). These different environments can be virtual, with individual configurations to simulate a variety of operating environments.

Testing and monitoring of test environments, tools and technologies also needs to be considered to ensure effective testing. The same considerations apply to monitoring of the monitoring systems deployed in development, test and production settings. Judgement is needed, guided by the sensitivity of the systems and data, to determine how many layers of meta-testing are useful.

---
**Section:** 8.30
**Title:** Outsourced development

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive #Detective |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Identify #Protect #Detect |
| Operational capabilities | #System_and_network_security #Application_security #Supplier_relationships_security |
| Security domains | #Governance_and_Ecosystem #Protection |

**Control:**
The organization should direct, monitor and review the activities related to outsourced system development.

**Purpose:**
To ensure information security measures required by the organization are implemented in outsourced system development.

**Guidance:**
Where system development is outsourced, the organization should communicate and agree requirements and expectations, and continually monitor and review whether the delivery of outsourced work meets these expectations. The following points should be considered across the organization’s entire external supply chain:

- licensing agreements, code ownership and intellectual property rights related to the outsourced content (see 5.32)
- contractual requirements for secure design, coding and testing practices (see 8.25 to 8.29)
- provision of the threat model to consider by external developers
- acceptance testing for the quality and accuracy of the deliverables (see 8.29)
- provision of evidence that minimum acceptable levels of security and privacy capabilities are established (e.g. assurance reports)
- provision of evidence that sufficient testing has been applied to guard against the presence of malicious content (both intentional and unintentional) upon delivery
- provision of evidence that sufficient testing has been applied to guard against the presence of known vulnerabilities
- escrow agreements for the software source code (e.g. if the supplier goes out of business)
- contractual right to audit development processes and controls
- security requirements for the development environment (see 8.31)
- taking consideration of applicable legislation (e.g. on protection of personal data)

**Other information:**
Further information on supplier relationships can be found in the ISO/IEC 27036 series.