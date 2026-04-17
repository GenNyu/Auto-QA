### A. Tài liệu gốc của Phụ lục A1

### B. Summary Overview của Phụ lục A1
Tài liệu này mô tả chi tiết **Phụ lục A.1. General (Annex A.1)** của **ISO/IEC 27002:2022**, tập trung vào việc **thiết lập hệ thống phân loại đa chiều cho các biện pháp kiểm soát thông qua cấu trúc thuộc tính (attributes)**.
Mục tiêu là **cung cấp khả năng tùy biến góc nhìn (view) quản trị, giúp tổ chức dễ dàng lọc, sắp xếp và báo cáo tình trạng kiểm soát theo các nhu cầu nghiệp vụ khác nhau thay vì chỉ phụ thuộc vào danh mục phẳng truyền thống**.
Gồm **02** mục chính:
- **Hệ thống 05 nhóm thuộc tính tiêu chuẩn:** Phân loại control theo loại hình, đặc tính bảo mật, khái niệm an ninh mạng, năng lực vận hành và miền bảo mật
- **Ma trận ánh xạ (Table A.1):** Bảng đối chiếu chi tiết giá trị thuộc tính cho toàn bộ 93 biện pháp kiểm soát từ mục 5 đến mục 8

Áp dụng cho **các chuyên gia đánh giá (Auditors), cán bộ quản trị rủi ro và đội ngũ vận hành an ninh thông tin trong việc xây dựng SoA (Statement of Applicability) và báo cáo tuân thủ đa chiều**.

### C. Key Points của Phụ lục A1
- **Chuẩn hóa Metadata kiểm soát:** Mọi biện pháp kiểm soát từ chính sách (5.1) đến kiểm tra thử nghiệm (8.34) đều phải được gán nhãn bằng 5 lớp thuộc tính để đảm bảo tính sẵn sàng cho việc truy vấn và phân tích hệ thống.
- **Cân bằng loại hình phòng thủ (Control Types):** Tổ chức phải xác định rõ tỷ trọng giữa các nhóm **Ngăn chặn (#Preventive)**, **Phát hiện (#Detective)** và **Khắc phục (#Corrective)** để đảm bảo hệ thống không bị lệch về một phía (ví dụ: chỉ lo ngăn chặn mà thiếu khả năng hồi phục).
- **Ánh xạ mục tiêu bảo vệ (CIA):** Mỗi control phải được định danh rõ ràng việc bảo vệ tính **Bảo mật (#Confidentiality)**, **Toàn vẹn (#Integrity)** hay **Sẵn sàng (#Availability)** để làm căn cứ đánh giá hiệu quả xử lý rủi ro dựa trên tác động kinh doanh.
- **Tương thích khung quản trị quốc tế:** Việc sử dụng thuộc tính "Cybersecurity concepts" (Identify, Protect, Detect, Respond, Recover) là yêu cầu bắt buộc để đồng bộ hóa báo cáo với các khung tiêu chuẩn khác như NIST CSF.
- **Phân định năng lực vận hành (Operational Capabilities):** Control phải được phân nhóm vào 15 năng lực cụ thể (như Governance, Asset Management, IAM,...) để xác định rõ trách nhiệm thực thi và nguồn lực cần thiết.

### D. Deep Summary của Phụ lục A1
**Bối cảnh:**
Trong phiên bản 2022, ISO 27002 không còn trình bày các control theo một danh sách cố định đơn điệu. Thay vào đó, nó chuyển sang mô hình dữ liệu có cấu trúc. Annex A.1 đóng vai trò là "bộ từ điển nhãn" giúp kỹ thuật hóa các khái niệm quản trị thành các thẻ (tags) có thể tìm kiếm và phân tích được trên các công cụ số như Spreadsheet hoặc Database.

**Nội dung cốt lõi:**
- **Ma trận kiểm soát tổng thể (Matrix of Controls):** Đây là "xương sống" của tri thức tuân thủ, nơi mỗi control được phân tích qua 5 lăng kính khác nhau. Ví dụ: Biện pháp "Threat Intelligence" (5.7) được định danh đồng thời là control ngăn chặn, phát hiện và khắc phục; tác động đến cả 3 thuộc tính CIA; và thuộc về khả năng vận hành "Quản lý mối đe dọa & lỗ hổng".
- **Cơ chế tạo Góc nhìn (Views):** Bằng cách lọc theo thuộc tính, tổ chức có thể tạo ra các báo cáo chuyên biệt. Ví dụ, một view về "Corrective controls" (Bảng A.2) sẽ tập trung vào các biện pháp như Quản lý sự cố (5.26) hay Sao lưu dữ liệu (8.13) để phục vụ kiểm tra khả năng phục hồi sau thảm họa.

**Dữ liệu đáng chú ý:**
- **5 nhóm thuộc tính chuẩn:** Control types, Information security properties, Cybersecurity concepts, Operational capabilities, và Security domains.
- **15 năng lực vận hành:** Phân tách rõ ràng các mảng từ Quản trị (Governance), Quản lý tài sản (Asset Management) đến Bảo mật ứng dụng (Application security) và Quan hệ nhà cung cấp (Supplier relationships security).
- **4 miền bảo mật (Security domains):** Governance and Ecosystem, Protection, Defence, và Resilience.

**Rủi ro / Lưu ý:**
- **Rủi ro thiếu sót kiểm soát:** Nếu tổ chức chỉ tập trung vào các control thuộc nhóm "Protection", họ sẽ fail trong việc chứng minh khả năng "Defence" và "Resilience" khi bị Auditor truy vấn dựa trên thuộc tính Security Domains.
- **Lưu ý về Audit:** Khi đánh giá tuân thủ, việc chỉ kiểm tra sự hiện diện của control là chưa đủ. Auditor sẽ sử dụng thuộc tính để kiểm tra xem control đó có đạt được **mục đích (Intent)** đã định danh hay không (ví dụ: một control được dán nhãn #Corrective nhưng thực tế không có quy trình khôi phục dữ liệu).
- **Quản lý linh hoạt:** Mặc dù ISO cung cấp bộ thuộc tính mặc định, nhưng rủi ro lớn nhất là tổ chức áp dụng một cách máy móc mà không tùy chỉnh thêm các thuộc tính nội bộ (như mức độ ưu tiên, trạng thái triển khai) để phù hợp với bối cảnh riêng.

### E. Structured Output của Phụ lục A1
This annex provides a table to demonstrate the use of attributes as a way of creating different views of the controls. The five examples of attributes are (see 4.2):
a) Control types (#Preventive, #Detective, #Corrective)
b) Information security properties (#Confidentiality, #Integrity, #Availability)
c) Cybersecurity concepts (#Identify, #Protect, #Detect, #Respond, #Recover)
d) Operational capabilities (#Governance, #Asset_management, #Information_protection, #Human_ resource_security, #Physical_security, #System_and_network_security, #Application_security, #Secure_configuration, #Identity_and_access_management, #Threat_and_vulnerability_ management, #Continuity, #Supplier_relationships_security, #Legal_and_compliance, #Information_security_event_management, #Information_security_assurance)
e) Security domains (#Governance_and_Ecosystem, #Protection, #Defence, #Resilience)

Table A.1 contains a matrix of all controls in this document with their given attribute values.
The filtering or sorting of the matrix can be achieved by using a tool such as a simple spreadsheet or a database, which can include more information like control text, guidance, organization-specific guidance or attributes (see A.2).

Table A.1 — Matrix of controls and attribute values
| ISO/IEC 27002 control identifier | Control name | Control type | Information security properties | Cybersecurity concepts | Operational capabilities | Security domains |
| --- | --- | --- | --- | --- | --- | --- |
| 5.1 | Policies for information security | #Preventive | #Confidentiality #Integrity #Availability | #Identify | #Governance | #Governance_and_Ecosystem #Resilience |
| 5.2 | Information security roles and responsibilities | #Preventive | #Confidentiality #Integrity #Availability | #Identify | #Governance | #Governance_and_Ecosystem #Protection #Resilience |
| 5.3 | Segregation of duties | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Governance #Identity_and_access_management | #Governance_and_Ecosystem |
| 5.4 | Management responsibilities | #Preventive | #Confidentiality #Integrity #Availability | #Identify | #Governance | #Governance_and_Ecosystem |
| 5.5 | Contact with authorities | #Preventive #Corrective | #Confidentiality #Integrity #Availability | #Identify #Protect #Respond #Recover | #Governance | #Defence #Resilience |
| 5.6 | Contact with special interest groups | #Preventive #Corrective | #Confidentiality #Integrity #Availability | #Protect #Respond #Recover | #Governance | #Defence |
| 5.7 | Threat intelligence | #Preventive #Detective #Corrective | #Confidentiality #Integrity #Availability | #Identify #Detect #Respond | #Threat_and_vulnerability_management | #Defence #Resilience |
| 5.8 | Information security in project management | #Preventive | #Confidentiality #Integrity #Availability | #Identify #Protect | #Governance | #Governance_and_Ecosystem #Protection |
| 5.9 | Inventory of information and other associated assets | #Preventive | #Confidentiality #Integrity #Availability | #Identify | #Asset_management | #Governance_and_Ecosystem #Protection |
| 5.10 | Acceptable use of information and other associated assets | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Asset_management #Information_protection | #Governance_and_Ecosystem #Protection |
| 5.11 | Return of assets | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Asset_management | #Protection |
| 5.12 | Classification of information | #Preventive | #Confidentiality #Integrity #Availability | #Identify | #Information_protection | #Protection #Defence |
| 5.13 | Labelling of information | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Information_protection | #Defence #Protection |
| 5.14 | Information transfer | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Asset_management #Information_protection | #Protection |
| 5.15 | Access control | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Identity_and_access_management | #Protection |
| 5.16 | Identity management | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Identity_and_access_management | #Protection |
| 5.17 | Authentication information | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Identity_and_access_management | #Protection |
| 5.18 | Access rights | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Identity_and_access_management | #Protection |
| 5.19 | Information security in supplier relationships | #Preventive | #Confidentiality #Integrity #Availability | #Identify | #Supplier_relationships_security | #Governance_and_Ecosystem #Protection |
| 5.20 | Addressing information security within supplier agreements | #Preventive | #Confidentiality #Integrity #Availability | #Identify | #Supplier_relationships_security | #Governance_and_Ecosystem #Protection |
| 5.21 | Managing information security in the ICT supply chain | #Preventive | #Confidentiality #Integrity #Availability | #Identify | #Supplier_relationships_security | #Governance_and_Ecosystem #Protection |
| 5.22 | Monitoring, review and change management of supplier services | #Preventive | #Confidentiality #Integrity #Availability | #Identify | #Supplier_relationships_security | #Governance_and_Ecosystem #Protection #Defence #Information_security_assurance |
| 5.23 | Information security for use of cloud services | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Supplier_relationships_security | #Governance_and_Ecosystem #Protection |
| 5.24 | Information security incident management planning and preparation | #Corrective | #Confidentiality #Integrity #Availability | #Respond #Recover | #Governance #Information_security_event_management | #Defence |
| 5.25 | Assessment and decision on information security events | #Detective | #Confidentiality #Integrity #Availability | #Detect #Respond | #Information_security_event_management | #Defence |
| 5.26 | Response to information security incidents | #Corrective | #Confidentiality #Integrity #Availability | #Respond #Recover | #Information_security_event_management | #Defence |
| 5.27 | Learning from information security incidents | #Preventive | #Confidentiality #Integrity #Availability | #Identify #Protect | #Information_security_event_management | #Defence |
| 5.28 | Collection of evidence | #Corrective | #Confidentiality #Integrity #Availability | #Detect #Respond | #Information_security_event_management | #Defence |
| 5.29 | Information security during disruption | #Preventive #Corrective | #Confidentiality #Integrity #Availability | #Protect #Respond | #Continuity | #Protection #Resilience |
| 5.30 | ICT readiness for business continuity | #Corrective | #Availability | #Respond | #Continuity | #Resilience |
| 5.31 | Legal, statutory, regulatory and contractual requirements | #Preventive | #Confidentiality #Integrity #Availability | #Identify | #Legal_and_compliance | #Governance_and_Ecosystem #Protection |
| 5.32 | Intellectual property rights | #Preventive | #Confidentiality #Integrity #Availability | #Identify | #Legal_and_compliance | #Governance_and_Ecosystem |
| 5.33 | Protection of records | #Preventive | #Confidentiality #Integrity #Availability | #Identify #Protect | #Legal_and_compliance #Asset_management #Information_protection | #Defence |
| 5.34 | Privacy and protection of PII | #Preventive | #Confidentiality #Integrity #Availability | #Identify #Protect | #Information_protection #Legal_and_compliance | #Protection |
| 5.35 | Independent review of information security | #Preventive #Corrective | #Confidentiality #Integrity #Availability | #Identify #Protect | #Information_security_assurance | #Governance_and_Ecosystem |
| 5.36 | Compliance with policies, rules and standards for information security | #Preventive | #Confidentiality #Integrity #Availability | #Identify #Protect | #Legal_and_compliance #Information_security_assurance | #Governance_and_Ecosystem |
| 5.37 | Documented operating procedures | #Preventive #Corrective | #Confidentiality #Integrity #Availability | #Protect #Recover | #Asset_management #Physical_security #System_and_network_security #Application_security #Secure_configuration #Identity_and_access_management #Threat_and_vulnerability_management #Continuity #Information_security_event_management | #Governance_and_Ecosystem #Protection #Defence |
| 6.1 | Screening | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Human_resource_security | #Governance_and_Ecosystem |
| 6.2 | Terms and conditions of employment | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Human_resource_security | #Governance_and_Ecosystem |
| 6.3 | Information security awareness, education and training | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Human_resource_security | #Governance_and_Ecosystem |
| 6.4 | Disciplinary process | #Preventive #Corrective | #Confidentiality #Integrity #Availability | #Protect #Respond | #Human_resource_security | #Governance_and_Ecosystem |
| 6.5 | Responsibilities after termination or change of employment | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Human_resource_security #Asset_management | #Governance_and_Ecosystem |
| 6.6 | Confidentiality or non-disclosure agreements | #Preventive | #Confidentiality | #Protect | #Human_resource_security #Information_protection #Supplier_relationships | #Governance_and_Ecosystem |
| 6.7 | Remote working | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Asset_management #Information_protection#Physical_security #System_and_network_security | #Protection |
| 6.8 | Information security event reporting | #Detective | #Confidentiality #Integrity #Availability | #Detect | #Information_security_event_management | #Defence |
| 7.1 | Physical security perimeters | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Physical_security | #Protection |
| 7.2 | Physical entry | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Physical_security #Iden-tity_and_Ac-cess_Manage-ment | #Protection |
| 7.3 | Securing offices, rooms and facilities | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Physical_security #Asset_management | #Protection |
| 7.4 | Physical security monitoring | #Preventive #Detective | #Confidentiality #Integrity #Availability | #Protect #Detect | #Physical_security | #Protection #Defence |
| 7.5 | Protecting against physical and environmental threats | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Physical_security | #Protection |
| 7.6 | Working in secure areas | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Physical_security | #Protection |
| 7.7 | Clear desk and clear screen | #Preventive | #Confidentiality | #Protect | #Physical_security | #Protection |
| 7.8 | Equipment siting and protection | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Physical_security #Asset_management | #Protection |
| 7.9 | Security of assets off-premises | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Physical_security #Asset_management | #Protection |
| 7.10 | Storage media | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Physical_security #Asset_management | #Protection |
| 7.11 | Supporting utilities | #Preventive #Detective | #Integrity #Availability | #Protect #Detect | #Physical_security | #Protection |
| 7.12 | Cabling security | #Preventive | #Confidentiality #Availability | #Protect | #Physical_security | #Protection |
| 7.13 | Equipment maintenance | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Physical_security #Asset_management | #Protection #Resilience |
| 7.14 | Secure disposal or re-use of equipment | #Preventive | #Confidentiality | #Protect | #Physical_security #Asset_management | #Protection |
| 8.1 | User endpoint devices | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Asset_management #Information_protection | #Protection |
| 8.2 | Privileged access rights | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Identity_and_access_management | #Protection |
| 8.3 | Information access restriction | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Identity_and_access_management | #Protection |
| 8.4 | Access to source code | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Identity_and_access_management #Application_security #Secure_configuration | #Protection |
| 8.5 | Secure authentication | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Identity_and_access_management | #Protection |
| 8.6 | Capacity management | #Preventive #Detective | #Integrity #Availability | #Identify #Protect #Detect | #Continuity | #Governance_and_Ecosystem #Protection |
| 8.7 | Protection against malware | #Preventive #Detective #Corrective | #Confidentiality #Integrity #Availability | #Protect #Detect | #System_and_network_security #Information_protection | #Protection #Defence |
| 8.8 | Management of technical vulnerabilities | #Preventive | #Confidentiality #Integrity #Availability | #Identify #Protect | #Threat_and_vulnerability_management | #Governance_and_Ecosystem #Protection #Defence |
| 8.9 | Configuration management | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Secure_configuration | #Protection |
| 8.10 | Information deletion | #Preventive | #Confidentiality | #Protect | #Information_protection #Legal_and_compliance | #Protection |
| 8.11 | Data masking | #Preventive | #Confidentiality | #Protect | #Information_protection | #Protection |
| 8.12 | Data leakage prevention | #Preventive #Detective | #Confidentiality | #Protect #Detect | #Information_protection | #Protection #Defence |
| 8.13 | Information backup | #Corrective | #Integrity #Availability | #Recover | #Continuity | #Protection |
| 8.14 | Redundancy of information processing facilities | #Preventive | #Availability | #Protect | #Continuity#Asset_management | #Protection #Resilience |
| 8.15 | Logging | #Detective | #Confidentiality #Integrity #Availability | #Detect | #Information_security_event_management | #Protection #Defence |
| 8.16 | Monitoring activities | #Detective #Corrective | #Confidentiality #Integrity #Availability | #Detect #Respond | #Information_security_event_management | #Defence |
| 8.17 | Clock synchronization | #Detective | #Integrity | #Protect #Detect | #Information_security_event_management | #Protection #Defence |
| 8.18 | Use of privileged utility programs | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #System_and_network_security #Secure_configuration #Application_security | #Protection |
| 8.19 | Installation of software on operational systems | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Secure_configuration#Application_security | #Protection |
| 8.20 | Networks security | #Preventive #Detective | #Confidentiality #Integrity #Availability | #Protect #Detect | #System_and_network_security | #Protection |
| 8.21 | Security of network services | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #System_and_network_security | #Protection |
| 8.22 | Segregation of networks | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #System_and_network_security | #Protection |
| 8.23 | Web filtering | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #System_and_network_security | #Protection |
| 8.24 | Use of cryptography | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Secure_configuration | #Protection |
| 8.25 | Secure development lifecycle | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Application_security #System_and_network_security | #Protection |
| 8.26 | Application security requirements | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Application_security #System_and_network_security | #Protection #Defence |
| 8.27 | Secure system architecture and engineering principles | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Application_security #System_and_network_security | #Protection |
| 8.28 | Secure coding | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Application_security #System_and_network_security | #Protection |
| 8.29 | Security testing in development and acceptance | #Preventive | #Confidentiality #Integrity #Availability | #Identify | #Application_security #Information_security_assurance #System_and_network_security | #Protection |
| 8.30 | Outsourced development | #Preventive #Detective | #Confidentiality #Integrity #Availability | #Identify #Protect #Detect | #System_and_network_security #Application_security #Supplier_relationships_security | #Governance_and_Ecosystem #Protection |
| 8.31 | Separation of development, test and production environments | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Application_security #System_and_network_security | #Protection |
| 8.32 | Change management | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #Application_security #System_and_network_security | #Protection |
| 8.33 | Test information | #Preventive | #Confidentiality #Integrity | #Protect | #Information_protection | #Protection |
| 8.34 | Protection of information systems during audit testing | #Preventive | #Confidentiality #Integrity #Availability | #Protect | #System_and_network_security #Information_protection | #Governance_and_Ecosystem #Protection |

Table A.2 shows an example of how to create a view by filtering by a particular attribute value, in this case #Corrective. 

Table A.2 — View of #Corrective controls
| ISO/IEC 27002 control identifier | Control name | Control type | Information security properties | Cybersecurity concepts | Operational capabilities | Security domains |
| --- | --- | --- | --- | --- | --- | --- |
| 5.5 | Contact with authorities | #Preventive #Corrective | #Confidentiality #Integrity #Availability | #Identify #Protect #Respond #Recover | #Governance | #Defence #Resilience |
| 5.6 | Contact with special interest groups | #Preventive #Corrective | #Confidentiality #Integrity #Availability | #Protect #Respond #Recover | #Governance | #Defence |
| 5.7 | Threat intelligence | #Preventive #Detective #Corrective | #Confidentiality #Integrity #Availability | #Identify #Detect #Respond | #Threat_and_vulnerability_management | #Defence #Resilience |
| 5.24 | Information security incident management planning and preparation | #Corrective | #Confidentiality #Integrity #Availability | #Respond #Recover | #Governance #Information_security_event_management | #Defence |
| 5.26 | Response to information security incidents | #Corrective | #Confidentiality #Integrity #Availability | #Respond #Recover | #Information_security_event_management | #Defence |
| 5.28 | Collection of evidence | #Corrective | #Confidentiality #Integrity #Availability | #Detect #Respond | #Information_security_event_management | #Defence |
| 5.29 | Information security during disruption | #Preventive #Corrective | #Confidentiality #Integrity #Availability | #Protect #Respond | #Continuity | #Protection #Resilience |
| 5.30 | ICT readiness for business continuity | #Corrective | #Availability | #Respond | #Continuity | #Resilience |
| 5.35 | Independent review of information security | #Preventive #Corrective | #Confidentiality #Integrity #Availability | #Identify #Protect | #Information_security_assurance | #Governance_and_Ecosystem |
| 5.37 | Documented operating procedures | #Preventive #Corrective | #Confidentiality #Integrity #Availability | #Protect #Recover | #Asset_management #Physical_security #System_and_network_security #Application_security #Secure_configuration #Identity_and_access_management #Threat_and_vulnerability_management #Continuity #Information_security_event_management | #Governance_and_Ecosystem #Protection #Defence |
| 6.4 | Disciplinary process | #Preventive #Corrective | #Confidentiality #Integrity #Availability | #Protect #Respond | #Human_resource_security | #Governance_and_Ecosystem |
| 8.7 | Protection against malware | #Preventive #Detective #Corrective | #Confidentiality #Integrity #Availability | #Protect #Detect | #System_and_network_security #Information_protection | #Protection #Defence |
| 8.13 | Information backup | #Corrective | #Integrity #Availability | #Recover | #Continuity | #Protection |
| 8.16 | Monitoring activities | #Detective #Corrective | #Confidentiality #Integrity #Availability | #Detect #Respond | #Information_security_event_management | #Defence | 