### A. Tài liệu gốc của Chương 5 (Control 5.23)

### B. Summary Overview của Chương 5 (Control 5.23)
Tài liệu này mô tả chi tiết **mục 5.23** trong **Chương 5 (Organizational controls)** của **ISO/IEC 27002:2022**, tập trung vào việc xác định và quản lý yêu cầu an toàn thông tin khi tổ chức sử dụng dịch vụ đám mây.
Mục tiêu chung của phần này là bảo đảm tổ chức biết mình đang chịu trách nhiệm gì khi dùng cloud, cloud provider chịu trách nhiệm gì, và các yêu cầu bảo mật đó được phản ánh trong hợp đồng, vận hành và chiến lược thoát dịch vụ.
Gồm 1 mục chính:
- `5.23`: Information security for use of cloud services - thiết lập quy trình cho việc mua, dùng, quản lý và rời khỏi cloud services theo yêu cầu an toàn thông tin của tổ chức

Áp dụng cho bộ phận quản trị cloud, an toàn thông tin, pháp chế, mua sắm, vận hành dịch vụ và các bên tham gia đánh giá rủi ro cloud.

### C. Key Points của Chương 5 (Control 5.23)
- **Mục tiêu quản trị:** control này giúp tổ chức quản lý cloud theo góc nhìn của cloud service customer, thay vì mặc định nhà cung cấp sẽ giải quyết hết các vấn đề an toàn thông tin.
- **Yêu cầu chính:** tổ chức phải thiết lập các quy trình cho acquisition, use, management và exit khỏi cloud services theo đúng yêu cầu bảo mật của mình.
- **Yêu cầu vận hành:** cần có topic-specific policy về việc sử dụng cloud, đồng thời làm rõ cloud service objectives, residual risk và trách nhiệm chia sẻ giữa hai bên.
- **Điểm vận hành quan trọng:** cloud thường đi kèm shared responsibility, nên control này phải được gắn với hợp đồng, kỹ thuật, giám sát và kế hoạch thoát dịch vụ.
- **Lưu ý thực tế:** nếu không xác định rõ phạm vi trách nhiệm và nơi lưu trữ dữ liệu, tổ chức dễ gặp vấn đề về tuân thủ pháp lý, backup, portability và incident handling.

### D. Deep Summary của Chương 5 (Control 5.23)
**Bối cảnh:**
Đây là control đặt cloud dưới góc nhìn của khách hàng sử dụng dịch vụ. Tổ chức phải xác định không chỉ chức năng cloud mà còn mức bảo mật, vùng lưu trữ, quyền truy cập, khả năng thoát dịch vụ và các ràng buộc pháp lý đi kèm.

**Nội dung cốt lõi:**
- `5.23` yêu cầu tổ chức định nghĩa cách quản lý an toàn thông tin cho toàn bộ vòng đời sử dụng cloud: mua, dùng, quản trị và rời khỏi dịch vụ.
- Control này buộc tổ chức phải làm rõ shared responsibility giữa mình và cloud provider, thay vì để trách nhiệm bị mơ hồ trong vận hành thực tế.
- Tổ chức phải xem xét policy, hợp đồng, assurance, jurisdiction, backup, incident handling và exit strategy trước khi sử dụng cloud.
- `5.23` không chỉ là kiểm soát hợp đồng mà còn là kiểm soát kiến trúc, vận hành và khả năng di chuyển dữ liệu hoặc dịch vụ khi cần.
- Khi dùng nhiều cloud service hoặc nhiều provider, tổ chức cần quản lý cả interfaces, interdependencies và thay đổi chéo giữa các dịch vụ.

**Dữ liệu đáng chú ý:**
- `5.23` là control `#Preventive`, gắn với `#Protect` và miền supplier relationship security, nhưng phần dùng cloud còn kéo theo governance và assurance nhiều hơn các control supplier thông thường.
- Guidance nhấn mạnh cloud service agreement, cloud service level objectives, cloud service qualitative objectives và residual risk acceptance.
- Control này liên kết với các chuẩn chuyên biệt như ISO/IEC 17788, 17789, 22123-1, 19941, 27017, 27018, 27036-4 và ISO/IEC 19086.
- Các điểm như jurisdiction, portability, backup, digital evidence và sub-contracting là dấu hiệu cho thấy control này bao phủ cả pháp lý lẫn kỹ thuật.

**Rủi ro / Lưu ý:**
- Nếu tổ chức không xác định rõ shared responsibility, nhiều khoảng trống kiểm soát sẽ bị bỏ sót giữa cloud provider và khách hàng.
- Nếu không quản lý jurisdiction và data location, tổ chức có thể gặp rủi ro tuân thủ pháp lý hoặc hợp đồng.
- Nếu thiếu exit strategy và portability, tổ chức dễ bị khóa vào một cloud service mà không có phương án rút lui an toàn.
- Nếu chỉ nhìn cloud như một dịch vụ tiện ích, tổ chức sẽ đánh giá thấp tác động của change, incident và sub-contractor chain.

### E. Structured Output của Chương 5 (Control 5.23)
**Section:** 5.23
**Title:** Information security for use of cloud services

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Informationsecurity properties | #Confidentiality#Integrity#Availability |
| Cybersecurityconcepts | #Protect |
| Operationalcapabilities | #Supplier_relation-ships_security |
| Security domains | #Governance_and_Ecosystem #Protec-tion |

**Control:**
Processes for acquisition, use, management and exit from cloud services should be established in accordance with the organization’s information security requirements.

**Purpose:**
To specify and manage information security for the use of cloud services.

**Guidance:**
The organization should establish and communicate topic-specific policy on the use of cloud services to all relevant interested parties.
The organization should define and communicate how it intends to manage information security risks associated with the use of cloud services. It can be an extension or part of the existing approach for how an organization manages services provided by external parties (see 5.21 and 5.22).
The use of cloud services can involve shared responsibility for information security and collaborative effort between the cloud service provider and the organization acting as the cloud service customer. It is essential that the responsibilities for both the cloud service provider and the organization, acting as the cloud service customer, are defined and implemented appropriately.
The organization should define:
- all relevant information security requirements associated with the use of the cloud services;
- cloud service selection criteria and scope of cloud service usage;
- roles and responsibilities related to the use and management of cloud services;
- which information security controls are managed by the cloud service provider and which are managed by the organization as the cloud service customer;
- how to obtain and utilize information security capabilities provided by the cloud service provider;
- how to obtain assurance on information security controls implemented by cloud service providers;
- how to manage controls, interfaces and changes in services when an organization uses multiple cloud services, particularly from different cloud service providers;
- procedures for handling information security incidents that occur in relation to the use of cloud services;
- its approach for monitoring, reviewing and evaluating the ongoing use of cloud services to manage information security risks;
- how to change or stop the use of cloud services including exit strategies for cloud services.

Cloud service agreements are often pre-defined and not open to negotiation. For all cloud services, the organization should review cloud service agreements with the cloud service provider(s). A cloud service agreement should address the confidentiality, integrity, availability and information handling requirements of the organization, with appropriate cloud service level objectives and cloud service qualitative objectives. The organization should also undertake relevant risk assessments to identify the risks associated with using the cloud service. Any residual risks connected to the use of the cloud service should be clearly identified and accepted by the appropriate management of the organization.
An agreement between the cloud service provider and the organization, acting as the cloud service customer, should include the following provisions for the protection of the organization’s data and availability of services:
- providing solutions based on industry accepted standards for architecture and infrastructure;
- managing access controls of the cloud service to meet the requirements of the organization;
- implementing malware monitoring and protection solutions;
- processing and storing the organization’s sensitive information in approved locations (e.g. particular country or region) or within or subject to a particular jurisdiction;
- providing dedicated support in the event of an information security incident in the cloud service environment;
- ensuring that the organization’s information security requirements are met in the event of cloud services being further sub-contracted to an external supplier (or prohibiting cloud services from being sub-contracted);
- supporting the organization in gathering digital evidence, taking into consideration laws and regulations for digital evidence across different jurisdictions;
- providing appropriate support and availability of services for an appropriate time frame when the organization wants to exit from the cloud service;
- providing required backup of data and configuration information and securely managing backups as applicable, based on the capabilities of the cloud service provider used by the organization, acting as the cloud service customer;
- providing and returning information such as configuration files, source code and data that are owned by the organization, acting as the cloud service customer, when requested during the service provision or at termination of service.
The organization, acting as the cloud service customer, should consider whether the agreement should require cloud service providers to provide advance notification prior to any substantive customer impacting changes being made to the way the service is delivered to the organization, including:
- changes to the technical infrastructure (e.g. relocation, reconfiguration, or changes in hardware or software) that affect or change the cloud service offering;
- processing or storing information in a new geographical or legal jurisdiction;
- use of peer cloud service providers or other sub-contractors (including changing existing or using new parties).

The organization using cloud services should maintain close contact with its cloud service providers. These contacts enable mutual exchange of information about information security for the use of the cloud services including a mechanism for both cloud service provider and the organization, acting as the cloud service customer, to monitor each service characteristic and report failures to the commitments contained in the agreements.

**Other information:**
This control considers cloud security from the perspective of the cloud service customer.
Additional information relating to cloud services can be found in ISO/IEC 17788, ISO/IEC 17789 and ISO/IEC 22123-1. Specifics related to cloud portability in support of exit strategies can be found in ISO/IEC 19941. Specifics related to information security and public cloud services are described in ISO/IEC 27017. Specifics related to PII protection in public clouds acting as PII processor are described in ISO/IEC 27018. Supplier relationships for cloud services are covered by ISO/IEC 27036-4 and cloud service agreements and their contents are dealt with in the ISO/IEC 19086 series, with security and privacy specifically covered by ISO/IEC 19086-4.