### A. Tài liệu gốc của Appendix A

### B. Summary Overview của Appendix A1
Tài liệu này mô tả chi tiết **Appendix A1** của **Appendix A** trong **PCI-DSS v4.0.1**, tập trung vào việc đảm bảo an toàn cho dữ liệu trong môi trường chia sẻ (multi-tenant) - nơi nhiều khách hàng cùng sử dụng hạ tầng của một nhà cung cấp.
Mục tiêu chính là thiết lập tách biệt logic giữa các môi trường khách hàng, quản lý quyền truy cập tài nguyên đúng phạm vi, và duy trì hệ thống ghi nhật ký cùng quy trình ứng phó sự cố riêng biệt cho từng thực thể.
### C. Key Points của Appendix A1
- Phạm vi áp dụng: Áp dụng cho các nhà cung cấp dịch vụ quản lý nhiều khách hàng trên cùng một hạ tầng (multi-tenant), đặc biệt có liên quan đến môi trường dữ liệu chủ thẻ (CDE).
- Trách nhiệm: Nhà cung cấp dịch vụ chịu trách nhiệm đảm bảo cách ly, bảo mật dữ liệu, kiểm soát truy cập và hỗ trợ khách hàng trong các vấn đề bảo mật.
- Tách biệt logic nghiêm ngặt: Đảm bảo cô lập hoàn toàn giữa các tenant và giữa khách hàng với hệ thống nhà cung cấp.
- Xác nhận định kỳ: Thực hiện penetration testing tối thiểu 6 tháng/lần để kiểm tra hiệu quả cách ly.
- Kiểm soát quyền truy cập: Mỗi khách hàng chỉ truy cập được tài nguyên và dữ liệu được phân bổ riêng.
- Quản lý nhật ký: Log phải tách biệt theo từng tenant, đảm bảo chỉ chủ sở hữu có quyền truy cập.
- Ứng phó sự cố: Có quy trình hỗ trợ điều tra (forensics) và cơ chế báo cáo sự cố/lỗ hổng an toàn
### D. Deep Summary của Appendix A1
**Bối cảnh:**
Trong môi trường đa thuê bao, một tác nhân độc hại trong môi trường của nhà cung cấp hoặc của một khách hàng có thể gây nguy hiểm cho toàn bộ hệ thống nếu thiếu các biện pháp kiểm soát phân đoạn

**Nội dung cốt lõi:** 
- Tập trung vào việc triển khai tách biệt logic thông qua cấu hình hệ thống và mạng
- Nhà cung cấp chịu trách nhiệm quản lý phân đoạn và phải đảm bảo các thay đổi công nghệ không vô tình tạo ra lỗ hổng xuyên suốt các khách hàng
- Việc thiết lập các phương thức báo cáo sự cố an toàn giúp phát hiện sớm các cấu hình sai sót

**Dữ liệu đáng chú ý:**
- Kiểm thử xâm nhập xác nhận tách biệt logic: Ít nhất 6 tháng/lần
- Thời hạn bắt buộc: Các yêu cầu này là phương pháp thực hành tốt (best practice) cho đến 31/03/2025, sau đó sẽ trở thành yêu cầu bắt buộc

**Rủi ro / Lưu ý:** Nếu không có sự phản hồi nhanh chóng đối với các yêu cầu điều tra pháp y, thời gian để kẻ tấn công chiếm hữu môi trường khách hàng sẽ kéo dài, gây thiệt hại nghiêm trọng hơn
### E. Structured Output của Appendix A1
**Sub-appendix:** `A1.1.1`
**Defined Approach Requirements:** Logical separation is implemented as follows: 
• The provider cannot access its customers' environments without authorization. 
• Customers cannot access the provider's environment without authorization
**Customized Approach Objective:** Customers cannot access the provider's environment. The provider cannot access its customers' environments without authorization
**Applicability Notes:** This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment
**Defined Approach Testing Procedures:**
- `A1.1.1`: Examine documentation and system and network configurations and interview personnel to verify that logical separation is implemented in accordance with all elements specified in this requirement.
**Guidance - Purpose:** Without controls between the provider's environment and the customer's environment, a malicious actor within the provider's environment could compromise the customer's environment, and similarly, a malicious actor in a customer environment could compromise the provider and potentially other of the provider's customers. Multi-tenant environments should be isolated from each other and from the provider's infrastructure such that they can be separately managed entities with no connectivity between them
**Guidance - Good Practice:** Providers should ensure strong separation between the environments that are designed for customer access, for example, configuration and billing portals, and the provider's private environment that should only be accessed by authorized provider personnel. Service provider access to customer environments is performed in accordance with requirement 8.2.3
**Guidance - Further Information:** Refer to the Information Supplement: PCI SSC Cloud Computing Guidelines for further guidance on cloud environments

---
**Sub-appendix:** `A1.1.2`
**Defined Approach Requirements:** Controls are implemented such that each customer only has permission to access its own cardholder data and CDE
**Customized Approach Objective:** Customers cannot access other customers' environments.
**Defined Approach Testing Procedures:**
- `A1.1.2.a`: Examine documentation to verify controls are defined such that each customer only has permission to access its own cardholder data and CDE.
- `A1.1.2.b`: Examine system configurations to verify that customers have privileges established to only access their own account data and CDE.
**Guidance - Purpose:** It is important that a multi-tenant service provider define controls so that each customer can only access their own environment and CDE to prevent unauthorized access from one customer's environment to another
**Guidance - Examples:** In a cloud-based infrastructure, such as an infrastructure as a service (IaaS) offering, the customers' CDE may include virtual network devices and virtual servers that are configured and managed by the customers, including operating systems, files, memory, etc.

---
**Sub-appendix:** `A1.1.3`
**Defined Approach Requirements:** Controls are implemented such that each customer can only access resources allocated to them
**Customized Approach Objective:** Customers cannot impact resources allocated to other customers
**Defined Approach Testing Procedures:**
- `A1.1.3`: Examine customer privileges to verify each customer can only access resources allocated to them.
**Guidance - Purpose:** To prevent any inadvertent or intentional impact to other customers' environments or account data, it is important that each customer can access only resources allocated to that customer

---
**Sub-appendix:** `A1.1.4`
**Defined Approach Requirements:** The effectiveness of logical separation controls used to separate customer environments is confirmed at least once every six months via penetration testing
**Customized Approach Objective:** Segmentation of customer environments from other environments is periodically validated to be effective
**Applicability Notes:** The testing of adequate separation between customers in a multi-tenant service provider environment is in addition to the penetration tests specified in Requirement 11.4.6. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment
**Defined Approach Testing Procedures:**
- `A1.1.4`: Examine the results from the most recent penetration test to verify that testing confirmed the effectiveness of logical separation controls used to separate customer environments.
**Guidance - Purpose:** Multi-tenant services providers are responsible for managing the segmentation between their customers. Without technical assurance that segmentation controls are effective, it is possible that changes to the service provider's technology would inadvertently create a vulnerability that could be exploited across all the service provider's customers
**Guidance - Good Practice:** Effectiveness of separation techniques can be confirmed by using service-provider-created temporary (mock-up) environments that represent customer environments and attempting to 1) access one temporary environment from another environment, and 2) access a temporary environment from the Internet

---
**Sub-appendix:** `A1.2.1`
**Defined Approach Requirements:** Audit log capability is enabled for each customer's environment that is consistent with PCI DSS Requirement 10, including: 
• Logs are enabled for common third-party applications.
• Logs are active by default.
• Logs are available for review only by the owning customer.
• Log locations are clearly communicated to the owning customer.
• Log data and availability is consistent with PCI DSS Requirement 10
**Customized Approach Objective:** Log capability is available to all customers without affecting the confidentiality of other customers.
**Defined Approach Testing Procedures:**
- `A1.2.1`: Examine documentation and system configuration settings to verify the provider has enabled audit log capability for each customer environment in accordance with all elements specified in this requirement.
**Guidance - Purpose:** Log information is useful for detecting and troubleshooting security incidents and is invaluable for forensic investigations. Customers therefore need to have access to these logs. However, log information can also be used by an attacker for reconnaissance, and so a customer's log information must only be accessible by the customer that the log relates to

---
**Sub-appendix:** `A1.2.2`
**Defined Approach Requirements:** Processes or mechanisms are implemented to support and/or facilitate prompt forensic investigations in the event of a suspected or confirmed security incident for any customer
**Customized Approach Objective:** Forensic investigation is readily available to all customers in the event of a suspected or confirmed security incident
**Defined Approach Testing Procedures:**
- `A1.2.2`: Examine documented procedures to verify that the provider has processes or mechanisms to support and/or facilitate a prompt forensic investigation of related servers in the event of a suspected or confirmed security incident for any customer.
**Guidance - Purpose:** In the event of a suspected or confirmed breach of confidentiality of cardholder data, a customer's forensic investigator aims to find the cause of the breach, exclude the attacker from the environment, and ensure all unauthorized access is removed. Prompt and efficient responses to forensic investigators' requests can significantly reduce the time taken for the investigator to secure the customer's environment

---
**Sub-appendix:** `A1.2.3`
**Defined Approach Requirements:** Processes or mechanisms are implemented for reporting and addressing suspected or confirmed security incidents and vulnerabilities, including: 
• Customers can securely report security incidents and vulnerabilities to the provider. 
• The provider addresses and remediates suspected or confirmed security incidents and vulnerabilities according to Requirement 6.3.1
**Customized Approach Objective:** Suspected or confirmed security incidents or vulnerabilities are discovered and addressed. Customers are informed where appropriate
**Applicability Notes:** This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Defined Approach Testing Procedures:**
- `A1.2.3`: Examine documented procedures and interview personnel to verify that the provider has a mechanism for reporting and addressing suspected or confirmed security incidents and vulnerabilities, in accordance with all elements specified in this requirement.
**Guidance - Purpose:** Security vulnerabilities in the provided services can impact the security of all the service provider's customers and therefore must be managed in accordance with the service provider's established processes, with priority given to resolving vulnerabilities that have the highest probability of compromise. Customers are likely to notice vulnerabilities and security misconfigurations while using the service. Implementing secure methods for customers to report security incidents and vulnerabilities encourages customers to report potential issues and enable the provider to quickly learn about and address potential issues within their environment