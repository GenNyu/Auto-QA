### A. Tài liệu gốc của Requirement 12

### B. Summary Overview của Control Objective 12.8
Tài liệu này mô tả chi tiết **Control Objective 12.8** của **Requirement 12 **trong **PCI-DSS v4.0.1**, tập trung vào việc quản lý và kiểm soát rủi ro từ các bên thứ ba (TPSP) có liên quan đến cardholder data.
Mục tiêu chính là đảm bảo các bên thứ ba được quản lý, đánh giá và giám sát đầy đủ để không làm suy giảm mức độ bảo mật của môi trường.
Gồm 5 sub-requirement chính:
- 12.8.1: Quản lý danh sách TPSP
- 12.8.2: Thiết lập thỏa thuận với TPSP
- 12.8.3: Thực hiện due diligence trước khi hợp tác
- 12.8.4: Giám sát trạng thái tuân thủ của TPSP
- 12.8.5: Phân định trách nhiệm PCI DSS
Áp dụng cho tất cả TPSP có lưu trữ, xử lý, truyền dữ liệu thẻ hoặc ảnh hưởng đến bảo mật CDE.

### C. Key Points của Control Objective 12.8
- **Phạm vi áp dụng:**Tất cả TPSP liên quan đến cardholder data hoặc CDE
- **Trách nhiệm:** Tài liệu hóa và quản lý quan hệ với TPSP
- **Quản lý danh sách:**Duy trì inventory TPSP và dịch vụ cung cấp
- **Thỏa thuận:**Có hợp đồng ghi rõ trách nhiệm bảo mật của TPSP
- **Đánh giá trước:**Thực hiện due diligence trước khi hợp tác
- **Giám sát:**Theo dõi compliance của TPSP ít nhất hàng năm
- **Phân định trách nhiệm:**Xác định rõ trách nhiệm giữa entity và TPSP

### D. Deep Summary của Control Objective 12.8
**Bối cảnh:**
Bên thứ ba có thể mở rộng phạm vi tấn công (attack surface) và trở thành điểm yếu nếu không được kiểm soát chặt chẽ.
**Nội dung cốt lõi:**
- Duy trì danh sách đầy đủ TPSP và dịch vụ liên quan
- Thiết lập hợp đồng ghi rõ trách nhiệm bảo mật dữ liệu
- Thực hiện đánh giá (due diligence) trước khi lựa chọn TPSP
- Giám sát trạng thái tuân thủ PCI DSS của TPSP định kỳ
- Xác định rõ trách nhiệm PCI DSS giữa các bên (entity vs TPSP)
- Xem xét cả mối quan hệ TPSP lồng nhau (nested TPSP)
**Dữ liệu đáng chú ý:**
- Monitoring TPSP tối thiểu mỗi 12 tháng
- Có thể sử dụng responsibility matrix để phân định trách nhiệm
**Rủi ro / Lưu ý:**
- TPSP không kiểm soát → rò rỉ dữ liệu từ bên ngoài
- Không có hợp đồng rõ ràng → không xác định trách nhiệm
- Không đánh giá trước → chọn TPSP không an toàn
- Không giám sát → không phát hiện TPSP mất compliance
- Trách nhiệm không rõ → bỏ sót kiểm soát PCI DSS

### E. Structured Output của Control Objective 12.8
**Control objectives:**12.8
**Sub-requirement:**12.8.1
**Defined Approach Requirements:**A list of all third-party service providers (TPSPs) with which account data is shared or that could affect the security of account data is maintained, including a description for each of the services provided.
**Defined Approach Testing Procedures:**
- "12.8.1.a": Examine policies and procedures to verify that processes are defined to maintain a list of TPSPs, including a description for each of the services provided, for all TPSPs with whom account data is shared or that could affect the security of account data.
- "12.8.1.b": Examine documentation to verify that a list of all TPSPs is maintained that includes a description of the services provided.
**Customized Approach Objective:**Records are maintained of TPSPs and the services provided.
**Applicability Notes:**The use of a PCI DSS compliant TPSP does not make an entity PCI DSS compliant, nor does it remove the entity's responsibility for its own PCI DSS compliance.
**Guidance - Purpose:**Maintaining a list of all TPSPs identifies where potential risk extends outside the organization and defines the organization's extended attack surface.
**Guidance - Examples:**Different types of TPSPs include those that:
• Store, process, or transmit account data on the entity's behalf (such as payment gateways, payment processors, payment service providers (PSPs), and off-site storage providers).
• Manage system components included in the entity's PCI DSS assessment (such as providers of network security control services, anti-malware services, and security incident and event management (SIEM); contact and call centers; web-hosting companies; and IaaS, PaaS, SaaS, and FaaS cloud providers).
• Could impact the security of the entity's cardholder data and/or sensitive authentication data (such as vendors providing support via remote access, and bespoke software developers).

---
**Control objectives:**12.8
**Sub-requirement:**12.8.2
**Defined Approach Requirements:**Written agreements with TPSPs are maintained as follows:
• Written agreements are maintained with all TPSPs with which account data is shared or that could affect the security of the CDE.
• Written agreements include acknowledgments from TPSPs that TPSPs are responsible for the security of account data the TPSPs possess or otherwise store, process, or transmit on behalf of the entity, or to the extent that the TPSP could impact the security of the entity's cardholder data and/or sensitive authentication data.
**Defined Approach Testing Procedures:**
- "12.8.2.a": Examine policies and procedures to verify that processes are defined to maintain written agreements with all TPSPs in accordance with all elements specified in this requirement.
- "12.8.2.b": Examine written agreements with TPSPs to verify they are maintained in accordance with all elements as specified in this requirement.
**Customized Approach Objective:**Records are maintained of each TPSP's acknowledgment of its responsibility to protect account data.
**Applicability Notes:**The exact wording of an agreement will depend on the details of the service being provided, and the responsibilities assigned to each party. The agreement does not have to include the exact wording provided in this requirement. The TPSP's written acknowledgment is a confirmation that states the TPSP is responsible for the security of the account data it may store, process, or transmit on behalf of the customer or to the extent the TPSP may impact the security of a customer's cardholder data and/or sensitive authentication data. Evidence that a TPSP is meeting PCI DSS requirements (is not the same as a written acknowledgment specified in this requirement. For example, a PCI DSS Attestation of Compliance (AOC), a declaration on a company's website, a policy statement, a responsibility matrix, or other evidence not included in a written agreement is not a written acknowledgment.
**Guidance - Purpose:**The written acknowledgment from a TPSP demonstrates its commitment to maintaining proper security of account data that it obtains from its customers and that the TPSP is fully aware of the assets that could be affected during the provisioning of the TPSP's service. The extent to which a specific TPSP is responsible for the security of account data will depend on the service provided and the responsibilities agreed between the provider and assessed entity (the customer). In conjunction with Requirement 12.9.1, this requirement is intended to promote a consistent level of understanding between parties about their applicable PCI DSS responsibilities. For example, the agreement may include the applicable PCI DSS requirements to be maintained as part of the provided service.
**Guidance - Good Practice:**The entity may also want to consider including in their written agreement with a TPSP that the TPSP will support the entity's request for information per Requirement 12.9.2. Entities will also want to understand whether any TPSPs have 'nested' relationships with other TPSPs, meaning the primary TPSP contracts with another TPSP(s) for the purposes of providing a service. It is important to understand whether the primary TPSP is relying on the secondary TPSP(s) to achieve overall compliance of a service, and what types of written agreements the primary TPSP has in place with the secondary TPSPs. Entities can consider including coverage in their written agreement for any 'nested' TPSPs a primary TPSP may use.
**Guidance - Further Information:**Refer to the Information Supplement: Third-Party Security Assurance for further guidance.

---
**Control objectives:**12.8
**Sub-requirement:**12.8.3
**Defined Approach Requirements:**An established process is implemented for engaging TPSPs, including proper due diligence prior to engagement.
**Defined Approach Testing Procedures:**
- "12.8.3.a": Examine policies and procedures to verify that processes are defined for engaging TPSPs, including proper due diligence prior to engagement.
- "12.8.3.b": Examine evidence and interview responsible personnel to verify the process for engaging TPSPs includes proper due diligence prior to engagement.
**Customized Approach Objective:**The capability, intent, and resources of a prospective TPSP to adequately protect account data are assessed before the TPSP is engaged.
**Guidance - Purpose:**A thorough process for engaging TPSPs, including details for selection and vetting prior to engagement, helps ensure that a TPSP is thoroughly vetted internally by an entity prior to establishing a formal relationship and that the risk to cardholder data associated with the engagement of the TPSP is understood.
**Guidance - Good Practice:**Specific due-diligence processes and goals will vary for each organization. Elements that should be considered include the provider's reporting practices, breach-notification and incident response procedures, details of how PCI DSS responsibilities are assigned between each party, how the TPSP validates their PCI DSS compliance and what evidence they provide.

---
**Control objectives:**12.8
**Sub-requirement:**12.8.4
**Defined Approach Requirements:**A program is implemented to monitor TPSPs' PCI DSS compliance status at least once every 12 months.
**Defined Approach Testing Procedures:**
- "12.8.4.a": Examine policies and procedures to verify that processes are defined to monitor TPSPs' PCI DSS compliance status at least once every 12 months.
- "12.8.4.b": Examine documentation and interview responsible personnel to verify that the PCI DSS compliance status of each TPSP is monitored at least once every 12 months.
**Customized Approach Objective:**The PCI DSS compliance status of TPSPs is verified periodically.
**Applicability Notes:**Where an entity has an agreement with a TPSP for meeting PCI DSS requirements on behalf of the entity (for example, via a firewall service), the entity must work with the TPSP to make sure the applicable PCI DSS requirements are met. If the TPSP does not meet those applicable PCI DSS requirements, then those requirements are also 'not in place' for the entity.
**Guidance - Purpose:**Knowing the PCI DSS compliance status of all engaged TPSPs provides assurance and awareness about whether they comply with the requirements applicable to the services they offer to the organization.
**Guidance - Good Practice:**If the TPSP offers a variety of services, the compliance status the entity monitors should be specific to those services delivered to the entity and those services in scope for the entity's PCI DSS assessment. If a TPSP has a PCI DSS Attestation of Compliance (AOC), the expectation is that the TPSP should provide that to customers upon request to demonstrate their PCI DSS compliance status. If the TPSP did not undergo a PCI DSS assessment, it may be able to provide other sufficient evidence to demonstrate that it has met the applicable requirements without undergoing a formal compliance validation. For example, the TPSP can provide specific evidence to the entity's assessor so the assessor can confirm applicable requirements are met. Alternatively, the TPSP can elect to undergo multiple on-demand assessments by each of its customers' assessors, with each assessment targeted to confirm that applicable requirements are met.
**Guidance - Further Information:**For more information about third-party service providers, refer to:
• PCI DSS section: Use of Third-Party Service Providers.
• Information Supplement: Third-Party Security Assurance .

---
**Control objectives:**12.8
**Sub-requirement:**12.8.5
**Defined Approach Requirements:**Information is maintained about which PCI DSS requirements are managed by each TPSP, which are managed by the entity, and any that are shared between the TPSP and the entity. 12.9 Third-party service providers (TPSPs) support their customers' PCI DSS compliance.
**Defined Approach Testing Procedures:**
- "12.8.5.a": Examine policies and procedures to verify that processes are defined to maintain information about which PCI DSS requirements are managed by each TPSP, which are managed by the entity, and any that are shared between both the TPSP and the entity.
- "12.8.5.b": Examine documentation and interview personnel to verify the entity maintains information about which PCI DSS requirements are managed by each TPSP, which are managed by the entity, and any that are shared between both entities. 12.9 Third-party service providers (TPSPs) support their customers' PCI DSS compliance.
**Customized Approach Objective:**Records detailing the PCI DSS requirements and related system components for which each TPSP is solely or jointly responsible, are maintained and reviewed periodically.
**Guidance - Purpose:**It is important that the entity understands which PCI DSS requirements and sub-requirements its TPSPs have agreed to meet, which requirements are shared between the TPSP and the entity, and for those that are shared, specifics about how the requirements are shared and which entity is responsible for meeting each sub-requirement. Without this shared understanding, it is inevitable that the entity and the TPSP will assume a given PCI DSS sub-requirement is the responsibility of the other party, and therefore that sub- requirement may not be addressed at all. The specific information an entity maintains will depend on the particular agreement with their providers, the type of service, etc. TPSPs may define their PCI DSS responsibilities to be the same for all their customers; otherwise, this responsibility should be agreed upon by both the entity and TPSP.
**Guidance - Good Practice:**Entities can document these responsibilities via a matrix that identifies all applicable PCI DSS requirements and indicates for each requirement whether the entity or TPSP is responsible for meeting that requirement or whether it is a shared responsibility. This type of document is often referred to as a responsibility matrix. It is also important for entities to understand whether any TPSPs have "nested" relationships with other TPSPs, meaning the primary TPSP contracts with another TPSP(s) for the purposes of providing a service. It is important to understand whether the primary TPSP is relying on the secondary TPSP(s) to achieve overall compliance of a service, and how the primary TPSP is monitoring performance of the service and the PCI DSS compliance status of the secondary TPSP(s). Note that it is the responsibility of the primary TPSP to manage and monitor any secondary TPSPs.
**Guidance - Further Information:**Refer to Information Supplement: Third-Party Security Assurance for a sample responsibility matrix template.