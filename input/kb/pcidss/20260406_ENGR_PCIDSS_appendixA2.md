### A. Tài liệu gốc của Appendix A

### B. Summary Overview của Appendix A2
Tài liệu này mô tả chi tiết **Appendix A2** của **Appendix A** trong **PCI-DSS v4.0.1**, tập trung vào quy định các biện pháp kiểm soát rủi ro đối với các thiết bị đầu cuối điểm chấp nhận thanh toán (POS POI) vẫn còn sử dụng các giao thức mã hóa cũ là SSL hoặc TLS phiên bản sớm
Mục tiêu chính là đảm bảo các thiết bị POI không bị ảnh hưởng bởi lỗ hổng SSL/TLS đã biết, yêu cầu các thực thể phải chứng minh tính an toàn tạm thời và có lộ trình chuyển đổi sang các giao thức bảo mật hiện đại
### C. Key Points của Appendix A2
- Phạm vi áp dụng: Áp dụng cho các hệ thống POS POI vẫn đang sử dụng SSL hoặc các phiên bản TLS cũ (early TLS).
- Trách nhiệm: Nhà cung cấp dịch vụ phải đảm bảo giảm thiểu rủi ro bảo mật và có lộ trình chuyển đổi sang giao thức an toàn hơn.
- Kiểm soát lỗ hổng: Xác nhận hệ thống không bị ảnh hưởng bởi các lỗ hổng đã biết của SSL/early TLS.
- Kế hoạch di chuyển: Xây dựng và duy trì Risk Mitigation & Migration Plan rõ ràng.
- Cung cấp lựa chọn an toàn: Nhà cung cấp dịch vụ phải luôn có sẵn tùy chọn sử dụng giao thức bảo mật hiện đại cho khách hàng
### D. Deep Summary của Appendix A2
**Bối cảnh:**
SSL là công nghệ lỗi thời và dễ bị tấn công; tuy nhiên, PCI DSS vẫn cho phép sử dụng tạm thời trong môi trường thẻ hiện diện (card-present) nếu chứng minh được thiết bị POI không bị ảnh hưởng bởi các lỗ hổng hiện tại

**Nội dung cốt lõi:**
- Thực thể (như Merchant) phải lưu trữ tài liệu từ nhà cung cấp để xác minh tính an toàn của thiết bị
- Đối với nhà cung cấp dịch vụ, họ phải thực hiện đánh giá rủi ro, giám sát các lỗ hổng mới và đảm bảo không triển khai SSL/early TLS vào các môi trường mới

**Dữ liệu đáng chú ý:** Kế hoạch giảm thiểu rủi ro phải bao gồm: Mô tả cách sử dụng, kết quả đánh giá rủi ro, quy trình giám sát lỗ hổng và lộ trình dự án di chuyển cụ thể

**Rủi ro / Lưu ý:** Nếu xuất hiện các lỗ hổng mới mà thiết bị POI bị ảnh hưởng, thực thể phải thực hiện cập nhật ngay lập tức
### E. Structured Output của Appendix A2
**Sub-appendix:** `A2.1.1`
**Defined Approach Requirements:** Where POS POI terminals at the merchant or payment acceptance location use SSL and/or early TLS, the entity confirms the devices are not susceptible to any known exploits for those protocols
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Applicability Notes:** This requirement is intended to apply to the entity with the POS POI terminal, such as a merchant. This requirement is not intended for service providers who serve as the termination or connection point to those POS POI terminals. Requirements A2.1.2 and A2.1.3 apply to POS POI service providers. The allowance for POS POI terminals that are not currently susceptible to exploits is based on currently known risks. If new exploits are introduced to which POS POI terminals are susceptible, the POS POI terminals will need to be updated immediately
**Defined Approach Testing Procedures:**
- `A2.1.1`: For POS POI terminals using SSL and/or early TLS, confirm the entity has documentation (for example, vendor documentation, system/network configuration details) that verifies the devices are not susceptible to any known exploits for SSL/early TLS
**Guidance - Purpose:** POS POI terminals used in card-present environments can continue using SSL/early TLS when it can be shown that the POS POI terminal is not susceptible to the currently known exploits.
**Guidance - Good Practice:** However, SSL is outdated technology and could be susceptible to additional security vulnerabilities in the future; it is therefore strongly recommended that POS POI terminals be upgraded to a secure protocol as soon as possible. If SSL/early TLS is not needed in the environment, use of, and fallback to these versions should be disabled
**Guidance - Further Information:** Refer to the current PCI SSC Information Supplements on SSL/Early TLS for further guidance

---
**Sub-appendix:** `A2.1.2`
**Defined Approach Requirements:** Additional requirement for service providers only: All service providers with existing connection points to POS POI terminals that use SSL and/or early TLS as defined in A2.1 have a formal Risk Mitigation and Migration Plan in place that includes: 
• Description of usage, including what data is being transmitted, types and number of systems that use and/or support SSL/early TLS, and type of environment. 
• Risk-assessment results and risk-reduction controls in place. 
• Description of processes to monitor for new vulnerabilities associated with SSL/early TLS. 
• Description of change control processes that are implemented to ensure SSL/early TLS is not implemented into new environments. 
• Overview of migration project plan to replace SSL/early TLS at a future date
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Applicability Notes:** This requirement applies only when the entity being assessed is a service provider.
**Defined Approach Testing Procedures:**
- `A2.1.2` Additional testing procedure for service provider assessments only: Review the documented Risk Mitigation and Migration Plan to verify it includes all elements specified in this requirement.
**Guidance - Purpose:** POS POI termination points, including but not limited to service providers such as acquirers or acquirer processors, can continue using SSL/early TLS when it can be shown that the service provider has controls in place that mitigate the risk of supporting those connections for the service provider environment
**Guidance - Good Practice:** Service providers should communicate to all customers using SSL/early TLS about the risks associated with its use and the need to migrate to a secure protocol
**Guidance - Further Information:** Refer to the current PCI SSC Information Supplements on SSL/early TLS for further guidance on Risk Mitigation and Migration Plans
**Guidance - Definitions:** The Risk Mitigation and Migration Plan is a document prepared by the entity that details its plans for migrating to a secure protocol and describes controls the entity has in place to reduce the risk associated with SSL/early TLS until the migration is complete

---
**Sub-appendix:** `A2.1.3`
**Defined Approach Requirements:** Additional requirement for service providers only : All service providers provide a secure service offering
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Applicability Notes:** This requirement applies only when the entity being assessed is a service provider
**Defined Approach Testing Procedures:**
- `A2.1.3 Additional testing procedure for service provider assessments only: Examine system configurations and supporting documentation to verify the service provider offers a secure protocol option for its service.
**Guidance - Purpose:** Customers must be able to choose to upgrade their POIs to eliminate the vulnerability in using SSL and early TLS. In many cases, customers will need to take a phased or gradual approach to migrate their POS POI estate from the insecure protocol to a secure protocol and so will require the service provider to support a secure offering
**Guidance - Further Information:** Refer to the current PCI SSC Information Supplements on SSL/Early TLS for further guidance