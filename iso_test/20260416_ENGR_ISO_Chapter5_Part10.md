### A. Tài liệu gốc của Chương 5 (Control 5.20)

### B. Summary Overview của Chương 5 (Control 5.20)
Tài liệu này mô tả chi tiết **mục 5.20** trong **Chương 5 (Organizational controls)** của **ISO/IEC 27002:2022**, tập trung vào việc đưa các yêu cầu an toàn thông tin vào trong hợp đồng và thỏa thuận với nhà cung cấp.
Mục tiêu chung của phần này là bảo đảm hai bên hiểu rõ nghĩa vụ bảo mật của mình ngay từ lúc ký kết, để mức bảo mật thỏa thuận được duy trì xuyên suốt quan hệ với supplier.
Gồm 1 mục chính:
- `5.20`: Addressing information security within supplier agreements - xác lập và thống nhất các yêu cầu an toàn thông tin trong thỏa thuận với từng supplier theo loại quan hệ cung ứng

Áp dụng cho bộ phận pháp chế, mua sắm, an toàn thông tin, quản trị supplier và các bên tham gia đàm phán hoặc giám sát hợp đồng dịch vụ.

### C. Key Points của Chương 5 (Control 5.20)
- **Mục tiêu quản trị:** control này biến yêu cầu an toàn thông tin thành điều khoản cụ thể trong hợp đồng, thay vì chỉ dừng ở policy nội bộ.
- **Yêu cầu chính:** tổ chức phải xác định và thống nhất với từng supplier các yêu cầu bảo mật phù hợp với loại quan hệ và mức độ rủi ro.
- **Yêu cầu vận hành:** thỏa thuận với supplier phải được lập thành văn bản, thể hiện rõ nghĩa vụ của cả hai bên và cách đáp ứng các yêu cầu liên quan.
- **Điểm vận hành quan trọng:** nội dung hợp đồng cần bao trùm phạm vi truy cập, xử lý, giám sát, báo cáo, kiểm toán, sub-contracting, chuyển giao và chấm dứt quan hệ.
- **Lưu ý thực tế:** điều khoản với supplier có thể rất khác nhau giữa từng tổ chức và từng loại supplier, nên không thể dùng một mẫu hợp đồng cứng cho mọi trường hợp.

### D. Deep Summary của Chương 5 (Control 5.20)
**Bối cảnh:**
Đây là control biến yêu cầu an toàn thông tin thành ràng buộc pháp lý hoặc hợp đồng. Nếu chỉ đánh giá supplier ở mức kỹ thuật mà không gắn vào thỏa thuận, tổ chức sẽ khó thực thi trách nhiệm, kiểm tra tuân thủ hoặc xử lý vi phạm.

**Nội dung cốt lõi:**
- `5.20` yêu cầu tổ chức chốt các yêu cầu bảo mật cụ thể với supplier trong hợp đồng hoặc thỏa thuận tương đương.
- Nội dung thỏa thuận phải phản ánh loại supplier, loại dịch vụ, mức độ nhạy cảm của thông tin và phạm vi truy cập của supplier.
- Control này bao trùm vòng đời hợp đồng, từ khởi tạo, vận hành, review, tới chấm dứt và bàn giao.
- Nó cũng là nền để kiểm tra, audit, xử lý non-compliance và xác định trách nhiệm khi có sự cố.

**Dữ liệu đáng chú ý:**
- `5.20` là control `#Preventive`, gắn với `#Identify`, `#Supplier_relationships_security` và các miền governance/protection, cho thấy đây là control quản trị ở lớp hợp đồng.
- Phần guidance liệt kê rất nhiều điều khoản có thể đưa vào hợp đồng, từ phân loại thông tin đến audit, incident response, backup, sub-contracting và termination.
- Đây là control có tính “đầu vào pháp lý” cho các control supplier khác như giám sát, đánh giá và chấm dứt quan hệ.
- Sự khác nhau giữa supplier types làm cho cấu trúc hợp đồng và mức độ kiểm soát phải được điều chỉnh theo rủi ro thực tế.

**Rủi ro / Lưu ý:**
- Nếu hợp đồng không ghi rõ yêu cầu an toàn thông tin, supplier có thể cung cấp dịch vụ đúng chức năng nhưng sai mức bảo mật.
- Nếu điều khoản quá chung chung, tổ chức sẽ khó yêu cầu audit, notification, recovery hoặc termination theo đúng kỳ vọng.
- Việc không phân loại supplier theo rủi ro sẽ làm hợp đồng hoặc quá nặng, hoặc quá nhẹ so với thực tế sử dụng.
- Nếu chỉ dựa vào mẫu hợp đồng chuẩn mà không điều chỉnh theo dịch vụ, nguy cơ bỏ sót điều khoản quan trọng là rất cao.

### E. Structured Output của Chương 5 (Control 5.20)
**Section:** 5.20
**Title:** Addressing information security within supplier agreements

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Informationsecurity properties | #Confidentiality#Integrity#Availability |
| Cybersecurityconcepts | #Identify |
| Operationalcapabilities | #Supplier_relationships_security |
| Security domains | #Governance_and_Ecosystem #Protection |

**Control:**
Relevant information security requirements should be established and agreed with each supplier based on the type of supplier relationship.

**Purpose:**
To maintain an agreed level of information security in supplier relationships.

**Guidance:**
Supplier agreements should be established and documented to ensure that there is clear understanding between the organization and the supplier regarding both parties’ obligations to fulfil relevant information security requirements.
The following terms can be considered for inclusion in the agreements in order to satisfy the identified information security requirements:
- description of the information to be provided or accessed and methods of providing or accessing the information;
- classification of information according to the organization’s classification scheme (see 5.10, 5.12, 5.13);
- mapping between the organization’s own classification scheme and the classification scheme of the supplier;
- legal, statutory, regulatory and contractual requirements, including data protection, handling of personally identifiable information (PII), intellectual property rights and copyright and a description of how it will be ensured that they are met;
- obligation of each contractual party to implement an agreed set of controls, including access control, performance review, monitoring, reporting and auditing, and the supplier’s obligations to comply with the organization’s information security requirements;
- rules of acceptable use of information and other associated assets, including unacceptable use if necessary;
- procedures or conditions for authorization and removal of the authorization for the use of the organization’s information and other associated assets by supplier personnel (e.g. through an explicit list of supplier personnel authorized to use the organization’s information and other associated assets);
- information security requirements regarding the supplier’s ICT infrastructure; in particular, minimum information security requirements for each type of information and type of access to serve as the basis for individual supplier agreements based on the organization’s business needs and risk criteria;
- indemnities and remediation for failure of contractor to meet requirements;
- incident management requirements and procedures (especially notification and collaboration during incident remediation);
- training and awareness requirements for specific procedures and information security requirements (e.g. for incident response, authorization procedures);
- relevant provisions for sub-contracting, including the controls that need to be implemented, such as agreement on the use of sub-suppliers (e.g. requiring to have them under the same obligations of the supplier, requiring to have a list of sub-suppliers and notification before any change);
- relevant contacts, including a contact person for information security issues;
- any screening requirements, where legally permissible, for the supplier’s personnel, including responsibilities for conducting the screening and notification procedures if screening has not been completed or if the results give cause for doubt or concern;
- the evidence and assurance mechanisms of third-party attestations for relevant information security requirements related to the supplier processes and an independent report on effectiveness of controls;
- right to audit the supplier processes and controls related to the agreement;
- supplier’s obligation to periodically deliver a report on the effectiveness of controls and agreement on timely correction of relevant issues raised in the report;
- defect resolution and conflict resolution processes;
- providing backup aligned with the organization’s needs (in terms of frequency and type and storage location);
- ensuring the availability of an alternate facility (i.e. disaster recovery site) not subject to the same threats as the primary facility and considerations for fall back controls (alternate controls) in the event primary controls fail);
- having a change management process that ensures advance notification to the organization and the possibility for the organization of not accepting changes;
- physical security controls commensurate with the information classification;
- information transfer controls to protect the information during physical transfer or logical transmission;
- termination clauses upon conclusion of the agreement including records management, return of assets, secure disposal of information and other associated assets, and any ongoing confidentiality obligations;
- provision of a method of securely destroying the organization’s information stored by the supplier as soon as it is no longer required;
- ensuring, at the end of the contract, handover support to another supplier or to the organization itself.

The organization should establish and maintain a register of agreements with external parties (e.g. contracts, memorandum of understanding, information-sharing agreements) to keep track of where their information is going. The organization should also regularly review, validate and update their agreements with external parties to ensure they are still required and fit for purpose with relevant information security clauses.

**Other information:**
The agreements can vary considerably for different organizations and among the different types of suppliers. Therefore, care should be taken to include all relevant requirements for addressing information security risks.
For details on supplier agreements, see ISO/IEC 27036 series. For cloud service agreements, see ISO/IEC 19086 series.