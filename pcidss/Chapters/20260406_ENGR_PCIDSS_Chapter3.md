### A. Tài liệu gốc của Chapter 3

### B. Summary Overview của Chapter 3
Tài liệu này mô tả chi tiết **Chapter 3** trong **PCI-DSS v4.0.1**, tập trung vào **mối quan hệ giữa tiêu chuẩn PCI DSS và các Tiêu chuẩn Phần mềm của PCI SSC** (bao gồm Khung Bảo mật Phần mềm - SSF)
Mục tiêu chính là hỗ trợ việc sử dụng phần mềm thanh toán an toàn trong môi trường dữ liệu chủ thẻ (CDE) và đảm bảo các thực thể hiểu rõ rằng việc sử dụng phần mềm đã được xác thực là cần thiết nhưng không thay thế hoàn toàn cho việc đánh giá tuân thủ định kỳ

### C. Key Points của Chapter 3
- **Khung Bảo mật Phần mềm (SSF):** Bao gồm hai tiêu chuẩn cốt lõi là Tiêu chuẩn Phần mềm An toàn (Secure Software Standard) và Tiêu chuẩn Vòng đời Phần mềm An toàn (Secure SLC Standard)
- **Phạm vi đánh giá:** Tất cả phần mềm lưu trữ, xử lý, truyền tải dữ liệu tài khoản hoặc có khả năng ảnh hưởng đến an ninh của CDE đều nằm trong phạm vi đánh giá PCI DSS
- **Trách nhiệm triển khai:** Việc sử dụng phần mềm đã được xác thực không mặc nhiên giúp thực thể đạt tuân thủ; thực thể phải đảm bảo phần mềm được cấu hình và triển khai đúng cách để hỗ trợ các yêu cầu của PCI DSS
- **Phần mềm tự phát triển:** Khuyến khích các thực thể tự phát triển phần mềm áp dụng các tiêu chuẩn bảo mật của PCI SSC như những phương pháp thực thi tốt nhất (best practices)

### D. Deep Summary của Chapter 3
**Bối cảnh:**
PCI SSC duy trì các chương trình phần mềm an toàn để cung cấp sự đảm bảo rằng phần mềm thanh toán được phát triển theo các quy trình bảo mật nghiêm ngặt, giúp bảo vệ tính toàn vẹn của giao dịch và dữ liệu tài khoản,

**Nội dung cốt lõi:**
- **Phần mềm được xác thực (Validated Software):** Là các ứng dụng đã được kiểm định bởi chuyên gia để đáp ứng các yêu cầu về bảo mật giao dịch. Danh sách này được duy trì công khai trên website của PCI SSC
- **Nhà cung cấp đủ điều kiện (Qualified Vendors):** Các đơn vị tích hợp quy trình phát triển an toàn vào toàn bộ vòng đời phần mềm theo tiêu chuẩn Secure SLC
- **Phần mềm tùy chỉnh và Bespoke:** Các phần mềm được viết riêng cho một thực thể phải tuân thủ đầy đủ **Yêu cầu 6** của PCI DSS. Nếu những phần mềm này được phát triển bởi bên thứ ba, thực thể vẫn chịu trách nhiệm đảm bảo nhà cung cấp tuân thủ đúng các yêu cầu này,,

**Dữ liệu đáng chú ý:**
- **Sự thay thế tiêu chuẩn:** Tiêu chuẩn PA-DSS và chương trình liên quan đã chính thức nghỉ hưu vào **tháng 10 năm 2022**
- **Trạng thái phần mềm:** Sau ngày hết hạn, các ứng dụng PA-DSS chỉ được liệt kê là "Chỉ chấp nhận cho các triển khai đã tồn tại trước đó" (Acceptable only for Pre-Existing Deployments)

**Rủi ro / Lưu ý:**
- **Phần mềm hết vòng đời (End of Life):** Các phần mềm không còn được nhà cung cấp hỗ trợ sẽ không đảm bảo mức độ an ninh trước các mối đe dọa mới; thực thể cần lập kế hoạch cập nhật hoặc thay thế
- **Ảnh hưởng của việc tùy chỉnh:** Nếu phần mềm đã xác thực bị tùy chỉnh (customized), nó có thể không còn giữ nguyên các thuộc tính an toàn như phiên bản gốc, đòi hỏi việc đánh giá phải thực hiện chuyên sâu và kỹ lưỡng hơn
- **Nhà cung cấp là Service Provider:** Một nhà cung cấp phần mềm cũng có thể thuộc phạm vi áp dụng PCI DSS nếu họ có quyền truy cập từ xa vào dữ liệu tài khoản của khách hàng hoặc cung cấp các dịch vụ thanh toán đám mây

### E. Structured Output của Chapter 3
PCI SSC supports the use of secure payment software within cardholder data environments (CDE) via the Software Security Framework (SSF), which consists of the Secure Software Standard and the Secure Software Lifecycle (Secure SLC) Standard. Software that is PCI SSC validated and listed provides assurance that the software has been developed using secure practices and has met a defined set of software security requirements.

The PCI SSC secure software programs include listings of payment software and software vendors that have been validated as meeting the applicable PCI SSC Software Standards.

- **Validated Software:** Payment software listed on the PCI SSC website as a Validated Payment Application (PA-DSS) or Validated Payment Software (the Secure Software Standard) has been evaluated by a qualified assessor to confirm the software meets the security requirements within that standard. The security requirements in these standards are focused on protecting the integrity and confidentiality of payment transactions and account data.

- **Qualified Software Vendors:** The Secure SLC Standard defines security requirements for software vendors to integrate secure software development practices throughout the entire software lifecycle. Software vendors that have been validated as meeting the Secure SLC Standard are listed on the PCI SSC website as a Secure SLC Qualified Vendor.

For more information about the SSF or PA-DSS, refer to the respective Program Guides at www.pcisecuritystandards.org.

All software that stores, processes, or transmits account data, or that could impact the security of cardholder data and/or sensitive authentication data, is in scope for an entity’s PCI DSS assessment. While the use of validated payment software supports the security of an entity’s CDE, the use of such software does not by itself make an entity PCI DSS compliant. The entity’s PCI DSS assessment should include verification that the software is properly configured and securely implemented to support applicable PCI DSS requirements. Additionally, if PCI-listed payment software has been customized, a more in-depth review will be required during the PCI DSS assessment because the software may no longer be representative of the version that was originally validated.

Because security threats are constantly evolving, software that is no longer supported by the vendor (for example, identified by the vendor as “end of life”) may not offer the same level of security as supported versions. Entities are strongly encouraged to keep their software current and updated to the latest software versions available.

Entities that develop their own software are encouraged to refer to PCI SSC’s software security standards and consider the requirements therein as best practices to use in their development environments. Secure payment software implemented in a PCI DSS compliant environment will help minimize the potential for security breaches leading to compromises of account data and fraud. See Bespoke and Custom Software.

**Note:** PA-DSS and the related program were retired in October 2022. Refer to the PCI SSC List of Validated Payment Applications for expiry dates for PA-DSS validated applications. Since the expiry date, applications are listed as “Acceptable only for Pre-Existing Deployments”. Whether an entity can continue to use a PA-DSS application with an expired listing is at the discretion of organizations that manage compliance programs (such as payment brands and acquirers); entities should contact these organizations for more details.

#### Applicability of PCI DSS to Payment Software Vendors
PCI DSS may apply to a payment software vendor if the vendor is also a service provider that stores, processes, or transmits account data, or has access to their customers’ account data—for example, in the role of a payment service provider or via remote access to a customer environment. Software vendors to which PCI DSS may be applicable include those offering payment services, as well as cloud service providers offering payment terminals in the cloud, software as a service (SaaS), e-commerce in the cloud, and other cloud payment services.

#### Bespoke and Custom Software
All bespoke and custom software that stores, processes, or transmits account data, or that could impact the security of cardholder data and/or sensitive authentication data, is in scope for an entity’s PCI DSS assessment.

Bespoke and custom software that has been developed and maintained in accordance with one of PCI SSC’s Software Security Framework standards (the Secure Software Standard or the Secure SLC standard) will support an entity in meeting PCI DSS Requirement 6.

See Appendix F for more details.

**Note:** PCI DSS Requirement 6 fully applies to bespoke and custom software that has not been developed and maintained in accordance with one of PCI SSC’s Software Security Framework standards. Entities that use software vendors to develop bespoke or custom software that could impact the security of their cardholder data and/or sensitive authentication data are responsible for ensuring those software vendors develop the software according to PCI DSS Requirement 6.