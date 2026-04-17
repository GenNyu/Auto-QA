### A. Tài liệu gốc của Chương 5 (Control 5.21, 5.22)

### B. Summary Overview của Chương 5 (Control 5.21, 5.22)
Tài liệu này mô tả chi tiết **mục 5.21 và 5.22** trong **Chương 5 (Organizational controls)** của **ISO/IEC 27002:2022**, tập trung vào việc quản lý rủi ro an toàn thông tin trong chuỗi cung ứng ICT và theo dõi cách nhà cung cấp duy trì dịch vụ sau khi đã ký kết.
Mục tiêu chung của phần này là duy trì mức bảo mật đã thỏa thuận trong quan hệ với supplier, đồng thời bảo đảm dịch vụ của supplier vẫn được kiểm soát khi có thay đổi về công nghệ, con người hoặc phương thức cung cấp.
Gồm 2 mục chính:
- `5.21`: Managing information security in the ICT supply chain - thiết lập quy trình để quản lý rủi ro an toàn thông tin trong chuỗi cung ứng ICT
- `5.22`: Monitoring, review and change management of supplier services - giám sát, rà soát và quản lý thay đổi trong thực hành bảo mật và dịch vụ của supplier

Áp dụng cho bộ phận quản trị supplier, mua sắm, an toàn thông tin, vận hành dịch vụ và các bên tham gia đánh giá chuỗi cung ứng ICT.

### C. Key Points của Chương 5 (Control 5.21, 5.22)
- **Mục tiêu quản trị:** nhóm control này giúp tổ chức kiểm soát rủi ro không chỉ ở supplier trực tiếp mà còn ở toàn bộ chuỗi cung ứng ICT phía sau họ.
- **Yêu cầu chính của 5.21:** tổ chức phải thiết lập và vận hành quy trình để quản lý rủi ro an toàn thông tin liên quan đến sản phẩm và dịch vụ ICT trong supply chain.
- **Yêu cầu chính của 5.22:** tổ chức phải theo dõi, rà soát, đánh giá và quản lý thay đổi trong thực hành bảo mật cũng như chất lượng cung cấp dịch vụ của supplier.
- **Điểm vận hành quan trọng:** control này đi sâu hơn supplier relationship thông thường, vì còn phải nhìn vào sub-supplier, component origin, assurance và tính liên tục của dịch vụ.
- **Lưu ý thực tế:** thực hành quản lý rủi ro chuỗi cung ứng ICT chỉ có tác dụng khi được xây trên nền quản trị an toàn thông tin, chất lượng, quản lý dự án và system engineering, không thay thế các nền tảng đó.

### D. Deep Summary của Chương 5 (Control 5.21, 5.22)
**Bối cảnh:**
Đây là nhóm control mở rộng từ quản trị supplier sang quản trị chuỗi cung ứng ICT và thay đổi dịch vụ sau triển khai. Tổ chức phải biết không chỉ supplier là ai, mà còn phải hiểu thành phần, nguồn gốc, thay đổi và mức độ tin cậy của dịch vụ hoặc sản phẩm ICT mà supplier cung cấp.

**Nội dung cốt lõi:**
- `5.21` yêu cầu tổ chức thiết lập cách kiểm soát rủi ro xuyên suốt chuỗi cung ứng ICT, bao gồm việc bảo đảm đầu vào, component origin, tính toàn vẹn và khả năng xác minh của sản phẩm hoặc dịch vụ.
- `5.21` đặc biệt quan trọng với các mô hình có nhiều lớp cung ứng như cloud, IoT, hosting hoặc phần mềm có nhiều thành phần từ bên thứ ba.
- `5.22` tập trung vào giám sát liên tục, rà soát báo cáo, đánh giá thay đổi và phản ứng với thay đổi ở phía supplier để tránh dịch vụ bị trượt khỏi điều kiện đã thỏa thuận.
- `5.22` giúp tổ chức phát hiện sớm thay đổi về công nghệ, nhà thầu phụ, địa điểm dịch vụ hoặc cách vận hành có thể ảnh hưởng đến mức bảo mật.
- Hai control này bổ trợ nhau: `5.21` nhìn vào chất lượng và rủi ro đầu vào của chuỗi cung ứng, còn `5.22` nhìn vào hành vi vận hành và thay đổi trong quá trình cung cấp dịch vụ.

**Dữ liệu đáng chú ý:**
- `5.21` là control `#Preventive`, gắn với `#Identify` và miền quản trị supplier relationship security, phản ánh trọng tâm nhận diện và kiểm soát rủi ro đầu vào.
- `5.22` cũng là `#Preventive`, nhưng nhấn mạnh theo dõi, review và change management để giữ dịch vụ đi đúng điều kiện đã thỏa thuận.
- `5.21` liên hệ mạnh với provenance, certification, SWID, assurance và traceability.
- `5.22` liên hệ mạnh với monitoring, audit trail, service reports, incident handling, sub-supplier change và continuity.

**Rủi ro / Lưu ý:**
- Nếu tổ chức chỉ kiểm soát supplier bề mặt mà bỏ qua supply chain phía sau, nguy cơ component giả, thành phần yếu hoặc nhà thầu phụ không đạt chuẩn sẽ lọt vào hệ thống.
- Nếu không giám sát thay đổi ở phía supplier, các thay đổi về công nghệ, địa điểm dịch vụ hoặc nhà thầu phụ có thể làm lệch mức kiểm soát ban đầu.
- Nếu rủi ro chuỗi cung ứng ICT không được gắn với procurement và lifecycle management, các điều khoản hợp đồng sẽ không đủ lực để ngăn sự cố.
- Nếu bỏ qua nền tảng quản lý chất lượng và engineering, control này sẽ bị biến thành danh sách kiểm tra hình thức thay vì cơ chế kiểm soát thực.

### E. Structured Output của Chương 5 (Control 5.21, 5.22)
**Section:** 5.21
**Title:** Managing information security in the ICT supply chain

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Informationsecurity properties | #Confidentiality#Integrity#Availability |
| Cybersecurityconcepts | #Identify |
| Operationalcapabilities | #Supplier_relation-ships_security |
| Security domains | #Governance_and_Ecosystem #Protec-tion |

**Control:**
Processes and procedures should be defined and implemented to manage the information security risks associated with the ICT products and services supply chain.

**Purpose:**
To maintain an agreed level of information security in supplier relationships.

**Guidance:**
The following topics should be considered to address information security within ICT supply chain security in addition to the general information security requirements for supplier relationships:
- defining information security requirements to apply to ICT product or service acquisition;
- requiring that ICT services suppliers propagate the organization’s security requirements throughout the supply chain if they sub-contract for parts of the ICT service provided to the organization;
- requiring that ICT products suppliers propagate appropriate security practices throughout the supply chain if these products include components purchased or acquired from other suppliers or other entities (e.g. sub-contracted software developers and hardware component providers);
- requesting that ICT products suppliers provide information describing the software components used in products;
- requesting that ICT products suppliers provide information describing the implemented security functions of their product and the configuration required for its secure operation;
- implementing a monitoring process and acceptable methods for validating that delivered ICT products and services comply with stated security requirements. Examples of such supplier review methods can include penetration testing and proof or validation of third-party attestations for the supplier’s information security operations;
- implementing a process for identifying and documenting product or service components that are critical for maintaining functionality and therefore require increased attention, scrutiny and further follow up required when built outside of the organization especially if the supplier outsources aspects of product or service components to other suppliers;
- obtaining assurance that critical components and their origin can be traced throughout the supply chain;
- obtaining assurance that the delivered ICT products are functioning as expected without any unexpected or unwanted features;
- implementing processes to ensure that components from suppliers are genuine and unaltered from their specification. Example measures include anti-tamper labels, cryptographic hash verifications or digital signatures. Monitoring for out of specification performance can be an indicator of tampering or counterfeits. Prevention and detection of tampering should be implemented during multiple stages in the system development life cycle, including design, development, integration, operations and maintenance;
- obtaining assurance that ICT products achieve required security levels, for example, through formal certification or an evaluation scheme such as the Common Criteria Recognition Arrangement;
- defining rules for sharing of information regarding the supply chain and any potential issues and compromises among the organization and suppliers;
- implementing specific processes for managing ICT component life cycle and availability and associated security risks. This includes managing the risks of components no longer being available due to suppliers no longer being in business or suppliers no longer providing these components due to technology advancements. Identification of an alternative supplier and the process to transfer software and competence to the alternative supplier should be considered.

**Other information:**
The specific ICT supply chain risk management practices are built on top of general information security, quality, project management and system engineering practices but do not replace them.
Organizations are advised to work with suppliers to understand the ICT supply chain and any matters that have an important effect on the products and services being provided. The organization can influence ICT supply chain information security practices by making clear in agreements with their suppliers the matters that should be addressed by other suppliers in the ICT supply chain.
ICT should be acquired from reputable sources. The reliability of software and hardware is a matter of quality control. While it is generally not possible for an organization to inspect the quality control systems of its vendors, it can make reliable judgments based on the reputation of the vendor.
ICT supply chain as addressed here includes cloud services.
Examples of ICT supply chains are:
- cloud services provisioning, where the cloud service provider relies on the software developers, telecommunication service providers, hardware providers;
- IoT, where the service involves the device manufacturers, the cloud service providers (e.g. the IoT platform operators), the developers for mobile and web applications, the vendor of software libraries;
- hosting services, where the provider relies on external service desks including first, second and third support levels.

See ISO/IEC 27036-3 for more details including risk assessment guidance.
Software identification (SWID) tags can also help to achieve better information security in the supply chain, by providing information about software provenance. See ISO/IEC 19770-2 for more details.

---
**Section:** 5.22
**Title:** Monitoring, review and change management of supplier services

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Informationsecurity properties | #Confidentiality#Integrity#Availability |
| Cybersecurityconcepts | #Identify |
| Operationalcapabilities | #Supplier_relation-ships_security |
| Security domains | #Governance_and_Ecosystem #Protec-tion#Defence#Information_secu-rity_assurance |

**Control:**
The organization should regularly monitor, review, evaluate and manage change in supplier information security practices and service delivery.

**Purpose:**
To maintain an agreed level of information security and service delivery in line with supplier agreements.

**Guidance:**
Monitoring, review and change management of supplier services should ensure the information security terms and conditions of the agreements are complied with, information security incidents and problems are managed properly and changes in supplier services or business status do not affect service delivery.
This should involve a process to manage the relationship between the organization and the supplier to:
- monitor service performance levels to verify compliance with the agreements;
- monitor changes made by suppliers including:
    1) enhancements to the current services offered;
    2) development of any new applications and systems;
    3) modifications or updates of the supplier’s policies and procedures;
    4) new or changed controls to resolve information security incidents and to improve information security;
- monitor changes in supplier services including:
    1) changes and enhancement to networks;
    2) use of new technologies;
    3) adoption of new products or newer versions or releases;
    4) new development tools and environments;
    5) changes to physical location of service facilities;
    6) change of sub-suppliers;
    7) sub-contracting to another supplier;
- review service reports produced by the supplier and arrange regular progress meetings as required by the agreements;
- conduct audits of suppliers and sub-suppliers, in conjunction with review of independent auditor’s reports, if available and follow-up on issues identified;
- provide information about information security incidents and review this information as required by the agreements and any supporting guidelines and procedures;
- review supplier audit trails and records of information security events, operational problems, failures, tracing of faults and disruptions related to the service delivered;
- respond to and manage any identified information security events or incidents;
- identify information security vulnerabilities and manage them;
- review information security aspects of the supplier’s relationships with its own suppliers;
- ensure that the supplier maintains sufficient service capability together with workable plans designed to ensure that agreed service continuity levels are maintained following major service failures or disaster (see 5.29, 5.30, 5.35, 5.36, 8.14);
- ensure that suppliers assign responsibilities for reviewing compliance and enforcing the requirements of the agreements;
- evaluate regularly that the suppliers maintain adequate information security levels.

The responsibility for managing supplier relationships should be assigned to a designated individual or team. Sufficient technical skills and resources should be made available to monitor that the requirements of the agreement, in particular the information security requirements, are being met. Appropriate actions should be taken when deficiencies in the service delivery are observed.

**Other information:**
See ISO/IEC 27036-3 for more detail.