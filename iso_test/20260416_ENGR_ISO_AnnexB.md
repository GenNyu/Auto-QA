### A. Tài liệu gốc của Phụ lục B

### B. Summary Overview của Phụ lục B
Tài liệu này mô tả chi tiết **Phụ lục B. informative (Annex B)** của **ISO/IEC 27002:2022**, tập trung vào việc **cung cấp ma trận đối chiếu (mapping) giữa phiên bản 2022 và phiên bản 2013**.
Mục tiêu là **đảm bảo tính tương thích ngược, hỗ trợ các tổ chức thực hiện chuyển đổi hệ thống quản lý an toàn thông tin (ISMS) mà không làm gián đoạn các biện pháp kiểm soát hiện hữu**.
Gồm **02** bảng đối chiếu chính:
- **Bảng B.1 (Hướng thuận):** Ánh xạ từ các control mới (mục 5 đến 8) về các control tương ứng trong bản 2013.
- **Bảng B.2 (Hướng nghịch):** Ánh xạ từ các danh mục cũ của bản 2013 sang cấu trúc mới của bản 2022.

Áp dụng cho **các tổ chức đang thực hiện nâng cấp chứng chỉ ISO/IEC 27001, giúp Auditor và cán bộ tuân thủ thực hiện Gap Analysis (phân tích khoảng cách) một cách chính xác**.

### C. Key Points của Phụ lục B
- **Xác định lỗ hổng kiểm soát (Gap Identification):** Phải đặc biệt lưu ý các mục được đánh nhãn **"New"** trong bảng B.1 (như 5.7, 5.23, 5.30, 7.4, 8.9, 8.10, 8.11, 8.12, 8.16, 8.23, 8.28), vì đây là những yêu cầu hoàn toàn mới chưa có trong phiên bản 2013
- **Hợp nhất kiểm soát (Control Merging):** Auditor cần kiểm tra các control mới được tổng hợp từ nhiều control cũ (ví dụ: mục 5.1 thay thế cho 05.1.1 và 05.1.2) để đảm bảo bằng chứng tuân thủ bao quát được tất cả các khía cạnh cũ
- **Cập nhật Tuyên bố áp dụng (SoA):** Việc ánh xạ này là căn cứ bắt buộc để cập nhật tài liệu SoA sang cấu trúc 93 control mới mà vẫn duy trì được tính kế thừa từ các phân tích rủi ro trước đó.
- **Truy xuất nguồn gốc bằng chứng:** Cho phép tổ chức sử dụng lại các hồ sơ, kết quả đánh giá cũ bằng cách đối chiếu mã ID, giúp giảm thiểu khối lượng công việc khi tái đánh giá tuân thủ.
- **Tái cấu trúc danh mục:** Chuyển đổi tư duy quản lý từ 14 miền (domains) của bản 2013 sang 4 chủ đề (themes) của bản 2022 mà không bỏ sót bất kỳ yêu cầu kỹ thuật nào

### D. Deep Summary của Phụ lục B
**Bối cảnh:**
Sự thay đổi cấu trúc từ ISO/IEC 27002:2013 sang 2022 là một cuộc cải cách lớn về cách phân loại. Annex B đóng vai trò là "bản đồ chuyển đổi", giúp tổ chức định vị lại vị trí của các biện pháp kiểm soát trong sơ đồ quản trị mới, đảm bảo tính liên tục của ISMS

**Nội dung cốt lõi:**
- **Ma trận đối chiếu nhị phân:** Cung cấp cái nhìn hai chiều để đảm bảo không có control nào bị "bỏ rơi" trong quá trình chuyển đổi. Đặc biệt, cấu trúc mới chú trọng vào tính hội tụ, gom các biện pháp có mục tiêu tương đồng vào một đầu mối quản lý duy nhất
- **Hệ thống hóa các yêu cầu hiện đại:** Annex B làm nổi bật sự xuất hiện của các xu hướng công nghệ mới thông qua các control "New", phản ánh sự thay đổi trong bối cảnh rủi ro như Điện toán đám mây (5.23) hay Trí tuệ về mối đe dọa (5.7)

**Dữ liệu đáng chú ý:**
- **11 biện pháp kiểm soát mới hoàn toàn:** Tập trung vào kỹ thuật bảo mật dữ liệu (Data masking, Data leakage prevention) và vận hành hạ tầng hiện đại
- **Tỷ lệ hợp nhất:** Nhiều control cũ được gộp lại thành một control mới để tối ưu hóa việc quản lý (ví dụ: 8.15 Logging thay thế cho 3 control cũ liên quan đến log và bảo vệ log)

**Rủi ro / Lưu ý:**
- **Rủi ro chuyển đổi bề nổi:** Doanh nghiệp có thể lầm tưởng rằng chỉ cần đổi mã số ID là xong. Auditor sẽ tập trung kiểm tra xem các control mới (nhất là các control được hợp nhất) có thực sự thực thi đầy đủ các hướng dẫn (guidance) chi tiết hơn trong bản 2022 hay không.
- **Lưu ý về "Necessary Controls":** Việc mapping chỉ mang tính tham chiếu. Tổ chức vẫn phải dựa trên kết quả đánh giá rủi ro thực tế để quyết định một control có áp dụng hay không, thay vì chỉ dựa vào việc nó đã từng tồn tại ở bản 2013.
- **Impact nếu fail:** Nếu mapping sai, tổ chức sẽ để lại "vùng mù" trong hệ thống kiểm soát, dẫn đến việc không đạt chứng chỉ khi đánh giá chuyển đổi do thiếu hụt bằng chứng cho các yêu cầu mới hoặc yêu cầu được mở rộng.

### E. Structured Output của Phụ lục B
**Correspondence of ISO/IEC 27002:2022 (this document) with ISO/IEC 27002:2013**
The purpose of this annex is to provide backwards compatibility with ISO/IEC 27002:2013 for organizations that are currently using that standard and now wish to transition to this edition.
Table B.1 provides the correspondence of the controls specified in Clauses 5 to 8 with those in ISO/IEC 27002:2013.

Table B.1 — Correspondence between controls in this document and controls in ISO/IEC 27002:2013
| ISO/IEC 27002:2022 control identifier | ISO/IEC 27002:2013 control identifier | Control name |
| --- | --- | --- |
| 5.1 | 05.1.1, 05.1.2 | Policies for information security |
| 5.2 | 06.1.1 | Information security roles and responsibilities |
| 5.3 | 06.1.2 | Segregation of duties |
| 5.4 | 07.2.1 | Management responsibilities |
| 5.5 | 06.1.3 | Contact with authorities |
| 5.6 | 06.1.4 | Contact with special interest groups |
| 5.7 | New | Threat intelligence |
| 5.8 | 06.1.5, 14.1.1 | Information security in project management |
| 5.9 | 08.1.1, 08.1.2 | Inventory of information and other associated assets |
| 5.10 | 08.1.3, 08.2.3 | Acceptable use of information and other associated assets |
| 5.11 | 08.1.4 | Return of assets |
| 5.12 | 08.2.1 | Classification of information |
| 5.13 | 08.2.2 | Labelling of information |
| 5.14 | 13.2.1, 13.2.2, 13.2.3 | Information transfer |
| 5.15 | 09.1.1, 09.1.2 | Access control |
| 5.16 | 09.2.1 | Identity management |
| 5.17 | 09.2.4, 09.3.1,09.4.3 | Authentication information |
| 5.18 | 09.2.2, 09.2.5,09.2.6 | Access rights |
| 5.19 | 15.1.1 | Information security in supplier relationships |
| 5.20 | 15.1.2 | Addressing information security within supplier agreements |
| 5.21 | 15.1.3 | Managing information security in the ICT supply chain |
| 5.22 | 15.2.1, 15.2.2 | Monitoring, review and change management of supplier services |
| 5.23 | New | Information security for use of cloud services |
| 5.24 | 16.1.1 | Information security incident management planning and preparation |
| 5.25 | 16.1.4 | Assessment and decision on information security events |
| 5.26 | 16.1.5 | Response to information security incidents |
| 5.27 | 16.1.6 | Learning from information security incidents |
| 5.28 | 16.1.7 | Collection of evidence |
| 5.29 | 17.1.1, 17.1.2, 17.1.3 | Information security during disruption |
| 5.30 | New | ICT readiness for business continuity |
| 5.31 | 18.1.1, 18.1.5 | Legal, statutory, regulatory and contractual requirements |
| 5.32 | 18.1.2 | Intellectual property rights |
| 5.33 | 18.1.3 | Protection of records |
| 5.34 | 18.1.4 | Privacy and protection of PII |
| 5.35 | 18.2.1 | Independent review of information security |
| 5.36 | 18.2.2, 18.2.3 | Compliance with policies, rules and standards for information security |
| 5.37 | 12.1.1 | Documented operating procedures |
| 6.1 | 07.1.1 | Screening |
| 6.2 | 07.1.2 | Terms and conditions of employment |
| 6.3 | 07.2.2 | Information security awareness, education and training |
| 6.4 | 07.2.3 | Disciplinary process |
| 6.5 | 07.3.1 | Responsibilities after termination or change of employment |
| 6.6 | 13.2.4 | Confidentiality or non-disclosure agreements |
| 6.7 | 06.2.2 | Remote working |
| 6.8 | 16.1.2, 16.1.3 | Information security event reporting |
| 7.1 | 11.1.1 | Physical security perimeters |
| 7.2 | 11.1.2, 11.1.6 | Physical entry |
| 7.3 | 11.1.3 | Securing offices, rooms and facilities |
| 7.4 | New | Physical security monitoring |
| 7.5 | 11.1.4 | Protecting against physical and environmental threats |
| 7.6 | 11.1.5 | Working in secure areas |
| 7.7 | 11.2.9 | Clear desk and clear screen |
| 7.8 | 11.2.1 | Equipment siting and protection |
| 7.9 | 11.2.6 | Security of assets off-premises |
| 7.10 | 08.3.1, 08.3.2,08.3.3,11.2.5 | Storage media |
| 7.11 | 11.2.2 | Supporting utilities |
| 7.12 | 11.2.3 | Cabling security |
| 7.13 | 11.2.4 | Equipment maintenance |
| 7.14 | 11.2.7 | Secure disposal or re-use of equipment |
| 8.1 | 06.2.1, 11.2.8 | User endpoint devices |
| 8.2 | 09.2.3 | Privileged access rights |
| 8.3 | 09.4.1 | Information access restriction |
| 8.4 | 09.4.5 | Access to source code |
| 8.5 | 09.4.2 | Secure authentication |
| 8.6 | 12.1.3 | Capacity management |
| 8.7 | 12.2.1 | Protection against malware |
| 8.8 | 12.6.1, 18.2.3 | Management of technical vulnerabilities |
| 8.9 | New | Configuration management |
| 8.10 | New | Information deletion |
| 8.11 | New | Data masking |
| 8.12 | New | Data leakage prevention |
| 8.13 | 12.3.1 | Information backup |
| 8.14 | 17.2.1 | Redundancy of information processing facilities |
| 8.15 | 12.4.1, 12.4.2,12.4.3 | Logging |
| 8.16 | New | Monitoring activities |
| 8.17 | 12.4.4 | Clock synchronization |
| 8.18 | 09.4.4 | Use of privileged utility programs |
| 8.19 | 12.5.1, 12.6.2 | Installation of software on operational systems |
| 8.20 | 13.1.1 | Networks security |
| 8.21 | 13.1.2 | Security of network services |
| 8.22 | 13.1.3 | Segregation of networks |
| 8.23 | New | Web filtering |
| 8.24 | 10.1.1, 10.1.2 | Use of cryptography |
| 8.25 | 14.2.1 | Secure development lifecycle |
| 8.26 | 14.1.2, 14.1.3 | Application security requirements |
| 8.27 | 14.2.5 | Secure system architecture and engineering principles |
| 8.28 | New | Secure coding |
| 8.29 | 14.2.8, 14.2.9 | Security testing in development and acceptance |
| 8.30 | 14.2.7 | Outsourced development |
| 8.31 | 12.1.4, 14.2.6 | Separation of development, test and production environments |
| 8.32 | 12.1.2, 14.2.2,14.2.3, 14.2.4 | Change management |
| 8.33 | 14.3.1 | Test information |
| 8.34 | 12.7.1 | Protection of information systems during audit testing |

Table B.2 — Correspondence between controls in ISO/IEC 27002:2013 and controls in this document
| ISO/IEC 27002:2013 control identifier | ISO/IEC 27002:2022 control identifier | Control name according to ISO/IEC 27002:2013 |
| --- | --- | --- |
| 5 |  | Information security policies |
| 5.1 |  | Management direction for information security |
| 5.1.1 | 5.1 | Policies for information security |
| 5.1.2 | 5.1 | Review of the policies for information security |
| 6 |  | Organization of information security |
| 6.1 |  | Internal organization |
| 6.1.1 | 5.2 | Information security roles and responsibilities |
| 6.1.2 | 5.3 | Segregation of duties |
| 6.1.3 | 5.5 | Contact with authorities |
| 6.1.4 | 5.6 | Contact with special interest groups |
| 6.1.5 | 5.8 | Information security in project management |
| 6.2 |  | Mobile devices and teleworking |
| 6.2.1 | 8.1 | Mobile device policy |
| 6.2.2 | 6.7 | Teleworking |
| 7 |  | Human resource security |
| 7.1 |  | Prior to employment |
| 7.1.1 | 6.1 | Screening |
| 7.1.2 | 6.2 | Terms and conditions of employment |
| 7.2 |  | During employment |
| 7.2.1 | 5.4 | Management responsibilities |
| 7.2.2 | 6.3 | Information security awareness, education and training |
| 7.2.3 | 6.4 | Disciplinary process |
| 7.3 |  | Termination and change of employment |
| 7.3.1 | 6.5 | Termination or change of employment responsibilities |
| 8 |  | Asset management |
| 8.1 |  | Responsibility for assets |
| 8.1.1 | 5.9 | Inventory of assets |
| 8.1.2 | 5.9 | Ownership of assets |
| 8.1.3 | 5.10 | Acceptable use of assets |
| 8.1.4 | 5.11 | Return of assets |
| 8.2 |  | Information classification |
| 8.2.1 | 5.12 | Classification of information |
| 8.2.2 | 5.13 | Labelling of information |
| 8.2.3 | 5.10 | Handling of assets |
| 8.3 |  | Media handling |
| 8.3.1 | 7.10 | Management of removable media |
| 8.3.2 | 7.10 | Disposal of media |
| 8.3.3 | 7.10 | Physical media transfer |
| 9 |  | Access control |
| 9.1 |  | Business requirements of access control |
| 9.1.1 | 5.15 | Access control policy |
| 9.1.2 | 5.15 | Access to networks and network services |
| 9.2 |  | User access management |
| 9.2.1 | 5.16 | User registration and de-registration |
| 9.2.2 | 5.18 | User access provisioning |
| 9.2.3 | 8.2 | Management of privileged access rights |
| 9.2.4 | 5.17 | Management of secret authentication information of users |
| 9.2.5 | 5.18 | Review of user access rights |
| 9.2.6 | 5.18 | Removal or adjustment of access rights |
| 9.3 |  | User responsibilities |
| 9.3.1 | 5.17 | Use of secret authentication information |
| 9.4 |  | System and application access control |
| 9.4.1 | 8.3 | Information access restriction |
| 9.4.2 | 8.5 | Secure log-on procedures |
| 9.4.3 | 5.17 | Password management system |
| 9.4.4 | 8.18 | Use of privileged utility programs |
| 9.4.5 | 8.4 | Access control to program source code |
| 10 |  | Cryptography |
| 10.1 |  | Cryptographic controls |
| 10.1.1 | 8.24 | Policy on the use of cryptographic controls |
| 10.1.2 | 8.24 | Key management |
| 11 |  | Physical and environmental security |
| 11.1 |  | Secure areas |
| 11.1.1 | 7.1 | Physical security perimeter |
| 11.1.2 | 7.2 | Physical entry controls |
| 11.1.3 | 7.3 | Securing offices, rooms and facilities |
| 11.1.4 | 7.5 | Protecting against external and environmental threats |
| 11.1.5 | 7.6 | Working in secure areas |
| 11.1.6 | 7.2 | Delivery and loading areas |
| 11.2 |  | Equipment |
| 11.2.1 | 7.8 | Equipment siting and protection |
| 11.2.2 | 7.11 | Supporting utilities |
| 11.2.3 | 7.12 | Cabling security |
| 11.2.4 | 7.13 | Equipment maintenance |
| 11.2.5 | 7.10 | Removal of assets |
| 11.2.6 | 7.9 | Security of equipment and assets off-premises |
| 11.2.7 | 7.14 | Secure disposal or reuse of equipment |
| 11.2.8 | 8.1 | Unattended user equipment |
| 11.2.9 | 7.7 | Clear desk and clear screen policy |
| 12 |  | Operations security |
| 12.1 |  | Operational procedures and responsibilities |
| 12.1.1 | 5.37 | Documented operating procedures |
| 12.1.2 | 8.32 | Change management |
| 12.1.3 | 8.6 | Capacity management |
| 12.1.4 | 8.31 | Separation of development, testing and operational environments |
| 12.2 |  | Protection from malware |
| 12.2.1 | 8.7 | Controls against malware |
| 12.3 |  | Backup |
| 12.3.1 | 8.13 | Information backup |
| 12.4 |  | Logging and monitoring |
| 12.4.1 | 8.15 | Event logging |
| 12.4.2 | 8.15 | Protection of log information |
| 12.4.3 | 8.15 | Administrator and operator logs |
| 12.4.4 | 8.17 | Clock synchronization |
| 12.5 |  | Control of operational software |
| 12.5.1 | 8.19 | Installation of software on operational systems |
| 12.6 |  | Technical vulnerability management |
| 12.6.1 | 8.8 | Management of technical vulnerabilities |
| 12.6.2 | 8.19 | Restrictions on software installation |
| 12.7 |  | Information systems audit considerations |
| 12.7.1 | 8.34 | Information systems audit controls |
| 13 |  | Communications security |
| 13.1 |  | Network security management facilities. |
| 13.1.1 | 8.20 | Network controls |
| 13.1.2 | 8.21 | Security of network services |
| 13.1.3 | 8.22 | Segregation of networks |
| 13.2 |  | Information transfer |
| 13.2.1 | 5.14 | Information transfer policies and procedures |
| 13.2.2 | 5.14 | Agreements on information transfer |
| 13.2.3 | 5.14 | Electronic messaging |
| 13.2.4 | 6.6 | Confidentiality or non-disclosure agreements |
| 14 |  | System acquisition,development and maintenance |
| 14.1 |  | Security requirements of information systems |
| 14.1.1 | 5.8 | Information security requirements analysis and specification |
| 14.1.2 | 8.26 | Securing application services on public networks |
| 14.1.3 | 8.26 | Protecting application services transactions |
| 14.2 |  | Security in development and support processes |
| 14.2.1 | 8.25 | Secure development policy |
| 14.2.2 | 8.32 | System change control procedures |
| 14.2.3 | 8.32 | Technical review of applications after operating platform changes |
| 14.2.4 | 8.32 | Restrictions on changes to software packages |
| 14.2.5 | 8.27 | Secure system engineering principles |
| 14.2.6 | 8.31 | Secure development environment |
| 14.2.7 | 8.30 | Outsourced development |
| 14.2.8 | 8.29 | System security testing |
| 14.2.9 | 8.29 | System acceptance testing |
| 14.3 |  | Test data |
| 14.3.1 | 8.33 | Protection of test data |
| 15 |  | Supplier relationships |
| 15.1 |  | Information security in supplier relationships |
| 15.1.1 | 5.19 | Information security policy for supplier relationships |
| 15.1.2 | 5.20 | Addressing security within supplier agreements |
| 15.1.3 | 5.21 | Information and communication technology supply chain |
| 15.2 |  | Supplier service delivery management |
| 15.2.1 | 5.22 | Monitoring and review of supplier services |
| 15.2.2 | 5.22 | Managing changes to supplier services |
| 16 |  | Information security incident management |
| 16.1 |  | Management of information security incidents and improvements |
| 16.1.1 | 5.24 | Responsibilities and procedures |
| 16.1.2 | 6.8 | Reporting information security events |
| 16.1.3 | 6.8 | Reporting information security weaknesses |
| 16.1.4 | 5.25 | Assessment of and decision on information security events |
| 16.1.5 | 5.26 | Response to information security incidents |
| 16.1.6 | 5.27 | Learning from information security incidents |
| 16.1.7 | 5.28 | Collection of evidence |
| 17 |  | Information security aspects of business continuity management |
| 17.1 |  | Information security continuity |
| 17.1.1 | 5.29 | Planning information security continuity |
| 17.1.2 | 5.29 | Implementing information security continuity |
| 17.1.3 | 5.29 | Verify, review and evaluate information security continuity |
| 17.2 |  | Redundancies |
| 17.2.1 | 8.14 | Availability of information processing facilities |
| 18 |  | Compliance |
| 18.1 |  | Compliance with legal and contractual requirements |
| 18.1.1 | 5.31 | Identification of applicable legislation and contractual requirements |
| 18.1.2 | 5.32 | Intellectual property rights |
| 18.1.3 | 5.33 | Protection of records |
| 18.1.4 | 5.34 | Privacy and protection of personally identifiable information |
| 18.1.5 | 5.31 | Regulation of cryptographic controls |
| 18.2 |  | Information security reviews |
| 18.2.1 | 5.35 | Independent review of information security |
| 18.2.2 | 5.36 | Compliance with security policies and standards |
| 18.2.3 | 5.36, 8.8 | Technical compliance review |