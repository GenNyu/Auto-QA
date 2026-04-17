### A. Tài liệu gốc của Chương 5 (Control 5.19)

### B. Summary Overview của Chương 5 (Control 5.19)
Tài liệu này mô tả chi tiết **mục 5.19** trong **Chương 5 (Organizational controls)** của **ISO/IEC 27002:2022**, tập trung vào việc quản lý rủi ro an toàn thông tin phát sinh từ nhà cung cấp, sản phẩm và dịch vụ do bên ngoài cung cấp.
Mục tiêu chung của phần này là duy trì một mức bảo mật thống nhất, có thể chấp nhận được trong quan hệ với nhà cung cấp, thay vì để rủi ro của bên thứ ba làm suy yếu kiểm soát nội bộ của tổ chức.
Gồm 1 mục chính:
- `5.19`: Information security in supplier relationships - thiết lập quy trình và thủ tục để quản lý rủi ro an toàn thông tin liên quan đến sản phẩm hoặc dịch vụ của nhà cung cấp

Áp dụng cho bộ phận mua sắm, pháp chế, an toàn thông tin, quản trị nhà cung cấp, vận hành hệ thống và các bên tham gia đánh giá hoặc giám sát dịch vụ bên thứ ba.

### C. Key Points của Chương 5 (Control 5.19)
- **Mục tiêu quản trị:** control này giúp tổ chức giữ được mức bảo mật mong muốn ngay cả khi một phần năng lực vận hành được giao cho supplier.
- **Yêu cầu chính:** tổ chức phải định nghĩa và thực thi các quy trình, thủ tục để quản lý rủi ro an toàn thông tin phát sinh từ sản phẩm hoặc dịch vụ của nhà cung cấp.
- **Yêu cầu vận hành:** cần có topic-specific policy về quan hệ nhà cung cấp, kèm theo cách đánh giá, giám sát, phản ứng và chấm dứt quan hệ nếu cần.
- **Điểm vận hành quan trọng:** rủi ro không chỉ nằm ở quyền truy cập của supplier mà còn ở chất lượng, độ tin cậy và khả năng phục hồi của sản phẩm hoặc dịch vụ họ cung cấp.
- **Lưu ý thực tế:** nếu không thể ép supplier tuân theo yêu cầu, tổ chức vẫn phải bù bằng lựa chọn supplier cẩn thận và các compensating controls phù hợp.

### D. Deep Summary của Chương 5 (Control 5.19)
**Bối cảnh:**
Đây là control quản trị rủi ro chuỗi cung ứng ở mức thực thi. Tổ chức không thể giả định rằng một supplier đã an toàn chỉ vì hợp đồng đã ký; thay vào đó, phải xác định rõ những gì supplier được phép chạm vào, cách họ được giám sát, và cách tổ chức vẫn giữ quyền kiểm soát nếu supplier gặp sự cố.

**Nội dung cốt lõi:**
- `5.19` yêu cầu tổ chức xây dựng quy trình và thủ tục để kiểm soát rủi ro do supplier tạo ra trong suốt vòng đời quan hệ.
- Phạm vi áp dụng không chỉ là dịch vụ truyền thống mà còn gồm cloud service, hạ tầng ICT, logistics, utilities và các dịch vụ có thể tác động đến C-I-A.
- Control này bao trùm các bước chọn supplier, đánh giá, giám sát, xử lý non-compliance, quản lý sự cố và chấm dứt quan hệ an toàn.
- Tổ chức vẫn giữ trách nhiệm cuối cùng đối với thông tin của mình, kể cả khi dữ liệu hoặc xử lý được giao cho bên thứ ba.
- Nếu supplier không thể đáp ứng trực tiếp yêu cầu, tổ chức phải dùng biện pháp bù trừ và đánh giá rủi ro thay thế.

**Dữ liệu đáng chú ý:**
- `5.19` là control `#Preventive`, gắn với `#Identify`, `#Supplier_relationships_security` và các miền governance/protection, cho thấy đây là control vừa quản trị vừa phòng ngừa.
- Phần guidance nhấn mạnh cả an toàn kỹ thuật lẫn khía cạnh hợp đồng, quy trình, đào tạo và kết thúc quan hệ.
- Control này liên kết với cloud, third-party review, incident handling, recovery, records management và secure disposal.
- Đây là control có tính xuyên suốt vòng đời supplier relationship, không phải một bước kiểm tra đơn lẻ.

**Rủi ro / Lưu ý:**
- Nếu supplier yếu về kiểm soát, tổ chức có thể bị kéo theo rủi ro về confidentiality, integrity, availability và cả pháp lý.
- Nếu không quy định rõ phạm vi truy cập, giám sát và trách nhiệm, supplier có thể trở thành điểm mở rộng bề mặt tấn công.
- Việc phụ thuộc quá sâu vào một supplier mà không có kế hoạch thay thế sẽ làm suy yếu khả năng phục hồi khi xảy ra sự cố hoặc ngừng dịch vụ.
- Nếu chỉ nhìn vào giá hoặc tính năng mà bỏ qua control an toàn thông tin, lựa chọn supplier sẽ tạo ra chi phí rủi ro cao hơn về sau.

### E. Structured Output của Chương 5 (Control 5.19)
**Section:** 5.19
**Title:** Information security in supplier relationships

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Informationsecurity properties | #Confidentiality#Integrity#Availability |
| Cybersecurityconcepts | #Identify |
| Operationalcapabilities | #Supplier_relationships_security |
| Security domains | #Governance_and_Ecosystem #Protection |
**Control:**
Processes and procedures should be defined and implemented to manage the information security risks associated with the use of supplier’s products or services.

**Purpose:**
To maintain an agreed level of information security in supplier relationships.

**Guidance:**
The organization should establish and communicate a topic-specific policy on supplier relationships to all relevant interested parties.
The organization should identify and implement processes and procedures to address security risks associated with the use of products and services provided by suppliers. This should also apply to the organization’s use of resources of cloud service providers. These processes and procedures should include those to be implemented by the organization, as well as those the organization requires the supplier to implement for the commencement of use of a supplier’s products or services or for the termination of use of a supplier’s products and services, such as:
- identifying and documenting the types of suppliers (e.g. ICT services, logistics, utilities, financial services, ICT infrastructure components) which can affect the confidentiality, integrity and availability of the organization's information;
- establishing how to evaluate and select suppliers according to the sensitivity of information, products and services (e.g. with market analysis, customer references, review of documents, onsite assessments, certifications);
- evaluating and selecting supplier’s products or services that have adequate information security controls and reviewing them; in particular, accuracy and completeness of controls implemented by the supplier that ensure integrity of the supplier’s information and information processing and hence the organization’s information security;
- defining the organization’s information, ICT services and the physical infrastructure that suppliers can access, monitor, control or use;
- defining the types of ICT infrastructure components and services provided by suppliers which can affect the confidentiality, integrity and availability of the organization's information;
- assessing and managing the information security risks associated with:
  - the suppliers’ use of the organization’s information and other associated assets, including risks originating from potential malicious supplier personnel;
  - malfunctioning or vulnerabilities of the products (including software components and subcomponents used in these products) or services provided by the suppliers;
- monitoring compliance with established information security requirements for each type of supplier and type of access, including third-party review and product validation;
- mitigating non-compliance of a supplier, whether this was detected through monitoring or by other means;
- handling incidents and contingencies associated with supplier products and services including responsibilities of both the organization and suppliers;
- resilience and, if necessary, recovery and contingency measures to ensure the availability of the supplier’s information and information processing and hence the availability of the organization’s information;
- awareness and training for the organization’s personnel interacting with supplier personnel regarding appropriate rules of engagement, topic-specific policies, processes and procedures and behaviour based on the type of supplier and the level of supplier access to the organization’s systems and information;
- managing the necessary transfer of information, other associated assets and anything else that needs to be changed and ensuring that information security is maintained throughout the transfer period;
- requirements to ensure a secure termination of the supplier relationship, including:
  - de-provisioning of access rights;
  - information handling;
  - determining ownership of intellectual property developed during the engagement;
  - information portability in case of change of supplier or insourcing;
  - records management;
  - return of assets;
  - secure disposal of information and other associated assets;
  - ongoing confidentiality requirements;
- level of personnel security and physical security expected from supplier's personnel and facilities.

The procedures for continuing information processing in the event that the supplier becomes unable to supply its products or services (e.g. because of an incident, because the supplier is no longer in business, or no longer provides some components due to technology advancements) should be considered to avoid any delay in arranging replacement products or services (e.g. identifying an alternative supplier in advance or always using alternative suppliers).

**Other information:**
In cases where it is not possible for an organization to place requirements on a supplier, the organization should:
- consider the guidance given in this control in making decisions about choosing a supplier and its product or service;
- implement compensating controls as necessary based on a risk assessment.

Information can be put at risk by suppliers with inadequate information security management. Controls should be determined and applied to manage the supplier's access to information and other associated assets. For example, if there is a special need for confidentiality of the information, non-disclosure agreements or cryptographic techniques can be used. Another example is personal data protection risks when the supplier agreement involves transfer of, or access to, information across borders. The organization needs to be aware that the legal or contractual responsibility for protecting information remains with the organization.
Risks can also be caused by inadequate controls of ICT infrastructure components or services provided by suppliers. Malfunctioning or vulnerable components or services can cause information security breaches in the organization or to another entity (e.g. they can cause malware infection, attacks or other harm on entities other than the organization).
See ISO/IEC 27036-2 for more detail.