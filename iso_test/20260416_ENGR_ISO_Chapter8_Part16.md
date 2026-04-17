### A. Tài liệu gốc của Chương 8 (Control 8.25, 8.26)

### B. Summary Overview của Chương 8 (Control 8.25, 8.26)
Tài liệu này mô tả chi tiết **mục 8.25 và 8.26** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào việc đưa an toàn thông tin vào vòng đời phát triển và xác định yêu cầu an ninh cho ứng dụng ngay từ đầu.
Mục tiêu là **đảm bảo phần mềm và hệ thống được thiết kế, xây dựng, kiểm thử và triển khai với các yêu cầu bảo mật rõ ràng, đầy đủ và có thể kiểm chứng**.
Gồm 2 mục chính:
- `8.25`: Secure development life cycle - vòng đời phát triển an toàn cho phần mềm và hệ thống
- `8.26`: Application security requirements - xác định và phê duyệt yêu cầu an ninh ứng dụng

Áp dụng cho hoạt động phát triển nội bộ hoặc thuê ngoài, thiết kế kiến trúc, mã nguồn, kiểm thử, môi trường dev/test/prod và các ứng dụng giao dịch hoặc xử lý dữ liệu nhạy cảm.

### C. Key Points của Chương 8 (Control 8.25, 8.26)
- **Mục tiêu quản trị:** `8.25` đưa security vào toàn bộ SDLC; `8.26` bảo đảm ứng dụng có yêu cầu an ninh rõ ràng trước khi phát triển hoặc mua sắm.
- **Yêu cầu chính của 8.25:** Phải có quy tắc phát triển an toàn, tách biệt môi trường dev/test/prod, secure coding, kiểm thử bảo mật, quản lý source code và giám sát outsourcing.
- **Yêu cầu chính của 8.26:** Yêu cầu an ninh ứng dụng phải được xác định, đặc tả, phê duyệt và gắn với risk assessment, bao gồm cả transactional services và electronic ordering/payment.
- **Điểm vận hành quan trọng:** `8.25` tập trung vào cách xây dựng hệ thống an toàn; `8.26` tập trung vào những gì hệ thống phải làm để đáp ứng bảo mật, privacy, non-repudiation và control giao dịch.
- **Lưu ý thực tế:** Nếu yêu cầu an ninh không được xác định rõ ngay từ đầu, các lỗ hổng sẽ bị “đóng băng” vào thiết kế và rất khó sửa về sau.

### D. Deep Summary của Chương 8 (Control 8.25, 8.26)
**Bối cảnh:**
Hai control này là lớp bảo vệ từ gốc cho phần mềm và ứng dụng. Nếu phát triển không có quy trình an toàn, tổ chức sẽ đưa lỗ hổng vào ngay từ đầu. Nếu yêu cầu an ninh ứng dụng không được xác định trước, hệ thống có thể hoạt động đúng về mặt chức năng nhưng sai về mặt bảo mật. Do đó, an toàn thông tin phải được xem như một phần của design và delivery, không phải lớp vá sau cùng.

**Nội dung cốt lõi:**
- `8.25` yêu cầu quy tắc phát triển an toàn được thiết lập và áp dụng xuyên suốt SDLC, bao gồm môi trường tách biệt, secure coding, test bảo mật, quản lý source code và version control.
- `8.25` cũng yêu cầu đảm bảo các supplier phát triển thuê ngoài tuân thủ quy tắc secure development của tổ chức.
- `8.26` yêu cầu xác định yêu cầu an ninh ứng dụng ngay từ giai đoạn phát triển hoặc mua sắm, dựa trên risk assessment và có sự hỗ trợ của chuyên gia an ninh.
- `8.26` mở rộng sang transactional services và electronic ordering/payment, nơi cần bảo vệ integrity, confidentiality, proof of dispatch/receipt và non-repudiation.
- `8.26` nhấn mạnh rằng nhiều yêu cầu an ninh ứng dụng có thể được đáp ứng bằng cryptography, nhưng phải xét đến ràng buộc pháp lý.

**Dữ liệu đáng chú ý:**
- `8.25` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Application_security#System_and_network_security` và miền `#Protection`.
- `8.26` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Application_security#System_and_network_security` và miền `#Protection#Defence`.
- `8.25` có liên hệ đến `8.28`, `8.29`, `8.30`, `8.31`, `8.4`, `8.9` và `8.32` trong các khâu coding, test và release.
- `8.26` có liên hệ đến `5.17`, `8.2`, `8.5`, `8.24`, `8.29`, `8.31` và `5.31` đến `5.36`.
- `8.26` đặc biệt coi trọng privacy, input controls, output controls, error handling và transaction logging.

**Rủi ro / Lưu ý:**
- Nếu SDLC không có security checkpoint, lỗi bảo mật sẽ đi thẳng vào production cùng với tính năng mới.
- Nếu yêu cầu an ninh ứng dụng mơ hồ, nhà phát triển hoặc nhà cung cấp có thể tối ưu chức năng nhưng bỏ sót kiểm soát quan trọng.
- Nếu dev/test/prod không tách biệt, dữ liệu và cấu hình production có thể bị lộ hoặc bị thay đổi trái phép.
- Nếu application security requirements không được kiểm thử và phê duyệt, hệ thống có thể không đáp ứng privacy, transaction integrity hoặc compliance.

### E. Structured Output của Chương 8 (Control 8.25, 8.26)
**Section:** 8.25
**Title:** Secure development life cycle

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Application_security #System_and_network_security |
| Security domains | #Protection |

**Control:**
Rules for the secure development of software and systems should be established and applied.

**Purpose:**
To ensure information security is designed and implemented within the secure development life cycle of software and systems.

**Guidance:**
Secure development is a requirement to build up a secure service, architecture, software and system. To achieve this, the following aspects should be considered:
- separation of development, test and production environments (see 8.31);
- guidance on the security in the software development life cycle:
  1. security in the software development methodology (see 8.28 and 8.27);
  2. secure coding guidelines for each programming language used (see 8.28);
- security requirements in the specification and design phase (see 5.8);
- security checkpoints in projects (see 5.8);
- system and security testing, such as regression testing, code scan and penetration tests (see 8.29);
- secure repositories for source code and configuration (see 8.4 and 8.9);
- security in the version control (see 8.32);
- required application security knowledge and training (see 8.28);
- developers’ capability for preventing, finding and fixing vulnerabilities (see 8.28);
- licensing requirements and alternatives to ensure cost-effective solutions while avoiding future licensing issues (See 5.32).

If development is outsourced, the organization should obtain assurance that the supplier complies with the organization’s rules for secure development (see 8.30).

**Other information:**
Development can also take place inside applications, such as office applications, scripting, browsers and databases.

---
**Section:** 8.26
**Title:** Application security requirements

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Application_security #System_and_network_security |
| Security domains | #Protection #Defence |

**Control:**
Information security requirements should be identified, specified and approved when developing or acquiring applications.

**Purpose:**
To ensure all information security requirements are identified and addressed when developing or acquiring applications.

**Guidance:**
***General***
Application security requirements should be identified and specified. These requirements are usually determined through a risk assessment. The requirements should be developed with the support of information security specialists.

Application security requirements can cover a wide range of topics, depending on the purpose of the application.

Application security requirements should include, as applicable:
- level of trust in identity of entities [e.g. through authentication (see 5.17, 8.2 and 8.5)];
- identifying the type of information and classification level to be processed by the application;
- need for segregation of access and level of access to data and functions in the application;
- resilience against malicious attacks or unintentional disruptions [e.g. protection against buffer overflow or structured query language (SQL) injections];
- legal, statutory and regulatory requirements in the jurisdiction where the transaction is generated, processed, completed or stored;
- need for privacy associated with all parties involved;
- the protection requirements of any confidential information;
- protection of data while being processed, in transit and at rest;
- need to securely encrypt communications between all involved parties;
- input controls, including integrity checks and input validation;
- automated controls (e.g. approval limits or dual approvals);
- output controls, also considering who can access outputs and its authorization;
- restrictions around content of "free-text" fields, as these can lead to uncontrolled storage of confidential data (e.g. personal data);
- requirements derived from the business process, such as transaction logging and monitoring, nonrepudiation requirements;
- requirements mandated by other security controls (e.g. interfaces to logging and monitoring or data leakage detection systems);
- error message handling.

***Transactional services***
Additionally, for applications offering transactional services between the organization and a partner, the following should be considered when identifying information security requirements:
- the level of trust each party requires in each other’s claimed identity;
- the level of trust required in the integrity of information exchanged or processed and the mechanisms for identification of lack of integrity (e.g. cyclic redundancy check, hashing, digital signatures);
- authorization processes associated with who can approve contents of, issue or sign key transactional documents;
- confidentiality, integrity, proof of dispatch and receipt of key documents and the non-repudiation (e.g. contracts associated with tendering and contract processes);
- the confidentiality and integrity of any transactions (e.g. orders, delivery address details and confirmation of receipts);
- requirements on how long to maintain a transaction confidential;
- insurance and other contractual requirements.

***Electronic ordering and payment applications***
Additionally, for applications involving electronic ordering and payment, the following should be considered:
- requirements for maintaining the confidentiality and integrity of order information;
- the degree of verification appropriate to verify payment information supplied by a customer;
- avoidance of loss or duplication of transaction information;
- storing transaction details outside of any publicly accessible environment (e.g. on a storage platform existing on the organizational intranet, and not retained and exposed on electronic storage media directly accessible from the internet);
- where a trusted authority is used (e.g. for the purposes of issuing and maintaining digital signatures or digital certificates) security is integrated and embedded throughout the entire endto-end certificate or signature management process.

Several of the above considerations can be addressed by the application of cryptography (see 8.24), taking into consideration legal requirements (see 5.31 to 5.36, especially see 5.31 for cryptography legislation).

**Other information:**
Applications accessible via networks are subject to a range of network related threats, such as fraudulent activities, contract disputes or disclosure of information to the public; incomplete transmission, misrouting, unauthorized message alteration, duplication or replay. Therefore, detailed risk assessments and careful determination of controls are indispensable. Controls required often include cryptographic methods for authentication and securing data transfer.

Further information on application security can be found in the ISO/IEC 27034 series.