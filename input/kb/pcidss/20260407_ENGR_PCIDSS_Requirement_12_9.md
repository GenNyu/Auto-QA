### A. Tài liệu gốc của Requirement 12

### B. Summary Overview của Control Objective 12.9
Tài liệu này mô tả chi tiết **Control Objective 12.9 **của **Requirement 12** trong **PCI-DSS v4.0.1**, tập trung vào việc trách nhiệm và hỗ trợ của TPSP đối với khách hàng trong tuân thủ PCI DSS.
Mục tiêu chính là đảm bảo TPSP cam kết rõ ràng về trách nhiệm bảo mật và cung cấp đầy đủ thông tin để hỗ trợ khách hàng đáp ứng yêu cầu PCI DSS.
Gồm 2 sub-requirement chính:
- 12.9.1: Cam kết trách nhiệm bảo mật từ TPSP
- 12.9.2: Hỗ trợ khách hàng về thông tin tuân thủ
Áp dụng cho service provider (TPSP).

### C. Key Points của Control Objective 12.9
- **Phạm vi áp dụng:**TPSP cung cấp dịch vụ liên quan đến cardholder data
- **Trách nhiệm:**TPSP phải xác nhận trách nhiệm bảo mật bằng văn bản
- **Thỏa thuận:** Cung cấp cam kết về bảo vệ dữ liệu thẻ trong hợp đồng
- **Hỗ trợ thông tin:**Cung cấp thông tin compliance khi khách hàng yêu cầu
- **Phân định trách nhiệm:**Làm rõ trách nhiệm PCI DSS giữa TPSP và khách hàng
- **Minh bạch:**Cung cấp AOC hoặc bằng chứng tương đương

### D. Deep Summary của Control Objective 12.9
**Bối cảnh:**
Nếu TPSP không minh bạch trách nhiệm và không hỗ trợ thông tin, khách hàng sẽ không thể đảm bảo tuân thủ PCI DSS hoặc bảo vệ dữ liệu hiệu quả.
**Nội dung cốt lõi:**
- TPSP cung cấp văn bản xác nhận trách nhiệm bảo mật dữ liệu
- Cam kết bao gồm dữ liệu lưu trữ, xử lý, truyền hoặc ảnh hưởng đến CDE
- Hỗ trợ khách hàng bằng cách cung cấp thông tin compliance (AOC, scope, trách nhiệm)
- Xác định rõ trách nhiệm giữa TPSP và khách hàng
- Đảm bảo thông tin cung cấp phù hợp với dịch vụ thực tế
**Dữ liệu đáng chú ý:**
- TPSP phải cung cấp thông tin phục vụ Requirement 12.8.4 và 12.8.5
- AOC là một dạng bằng chứng phổ biến nhưng không thay thế thỏa thuận
**Rủi ro / Lưu ý:**
- Không có cam kết → không rõ trách nhiệm bảo mật
- Không cung cấp thông tin → khách hàng không thể tuân thủ PCI DSS
- Trách nhiệm không rõ → bỏ sót kiểm soát bảo mật
- TPSP không minh bạch → tăng rủi ro từ bên thứ ba

### E. Structured Output của Control Objective 12.9
**Control objectives:**12.9
**Sub-requirement:**12.9.1
**Defined Approach Requirements:**Additional requirement for service providers only: TPSPs provide written agreements to customers that include acknowledgments that TPSPs are responsible for the security of account data the TPSP possesses or otherwise stores, processes, or transmits on behalf of the customer, or to the extent that the TPSP could impact the security of the customer's cardholder data and/or sensitive authentication data.
**Defined Approach Testing Procedures:**Additional testing procedure for service provider assessments only: Examine TPSP policies, procedures, and templates used for written agreements to verify processes are defined for the TPSP to provide written acknowledgments to customers in accordance with all elements specified in this requirement.
**Customized Approach Objective:**TPSPs formally acknowledge their security responsibilities to their customers.
**Applicability Notes:**This requirement applies only when the entity being assessed is a service provider. The exact wording of an agreement will depend on the details of the service being provided, and the responsibilities assigned to each party. The agreement does not have to include the exact wording provided in this requirement. The TPSP's written acknowledgment is a confirmation that states the TPSP is responsible for the security of the account data it may store, process, or transmit on behalf of the customer or to the extent the TPSP may impact the security of a customer's cardholder data and/or sensitive authentication data. Evidence that a TPSP is meeting PCI DSS requirements is not the same as a written agreement specified in this requirement. For example, a PCI DSS Attestation of Compliance (AOC), a declaration on a company's website, a policy statement, a responsibility matrix, or other evidence not included in a written agreement is not a written acknowledgment.
**Guidance - Purpose:**In conjunction with Requirement 12.8.2, this requirement is intended to promote a consistent level of understanding between TPSPs and their customers about their applicable PCI DSS responsibilities. The acknowledgment from the TPSP evidences the TPSP's commitment to maintaining proper security of the account data that it obtains from its customers. The TPSP's internal policies and procedures related to their customer engagement process and any templates used for written agreements should include provision of an applicable PCI DSS acknowledgement to its customers. The method by which the TPSP provides written acknowledgment should be agreed between the provider and its customers.

---
**Control objectives:**12.9
**Sub-requirement:**12.9.2
**Defined Approach Requirements:**Additional requirement for service providers only: TPSPs support their customers' requests for information to meet Requirements 12.8.4 and 12.8.5 by providing the following upon customer request:
• PCI DSS compliance status information (Requirement 12.8.4).
• Information about which PCI DSS requirements are the responsibility of the TPSP and which are the responsibility of the customer, including any shared responsibilities (Requirement 12.8.5), for any service the TPSP provides that meets a PCI DSS requirement(s) on behalf of customers or that can impact security of customers' cardholder data or sensitive authentication data. 12.10 Suspected and confirmed security incidents that could impact the CDE are responded to immediately.
**Defined Approach Testing Procedures:**Additional testing procedure for service provider assessments only: Examine policies and procedures to verify processes are defined for the TPSPs to support customers' request for information to meet Requirements 12.8.4 and 12.8.5 in accordance with all elements specified in this requirement.
**Customized Approach Objective:**TPSPs provide information as needed to support their customers' PCI DSS compliance efforts.
**Applicability Notes:**This requirement applies only when the entity being assessed is a service provider.
**Guidance - Purpose:**If a TPSP does not provide the necessary information to enable its customers to meet their security and compliance requirements, the customers will not be able to protect cardholder data nor meet their own contractual obligations.
**Guidance - Good Practice:**If a TPSP has a PCI DSS Attestation of Compliance (AOC), the expectation is that the TPSP should provide that to customers upon request to demonstrate their PCI DSS compliance status. If the TPSP did not undergo a PCI DSS assessment, they may be able to provide other sufficient evidence to demonstrate that it has met the applicable requirements without undergoing a formal compliance validation. For example, the TPSP can provide specific evidence to the entity's assessor so the assessor can confirm applicable requirements are met. Alternatively, the TPSP can elect to undergo multiple on-demand assessments by each of its customers' assessors, with each assessment targeted to confirm that applicable requirements are met. TPSPs should provide sufficient evidence to their customers to verify that the scope of the TPSP's PCI DSS assessment covered the services applicable to the customer and that the relevant PCI DSS requirements were examined and determined to be in place. TPSPs may define their PCI DSS responsibilities to be the same for all their customers; otherwise, this responsibility should be agreed upon by both the customer and TPSP. It is important that the customer understands which PCI DSS requirements and sub-requirements its TPSPs have agreed to meet, which requirements are shared between the TPSP and the customer, and for those that are shared, specifics about how the requirements are shared and which entity is responsible for meeting each sub-requirement. An example of a way to document these responsibilities is via a matrix that identifies all applicable PCI DSS requirements and indicates whether the customer or TPSP is responsible for meeting that requirement or whether it is a shared responsibility.
**Guidance - Further Information:**For further guidance, refer to:
• PCI DSS section: Use of Third-Party Service Providers .
• Information Supplement: Third-Party Security Assurance (includes a sample responsibility matrix template).