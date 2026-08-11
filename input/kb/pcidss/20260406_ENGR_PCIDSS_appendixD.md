### A. Tài liệu gốc của Appendix D

### B. Summary Overview của Appendix D
Tài liệu này mô tả chi tiết **Appendix D** trong **PCI-DSS v4.0.1**, tập trung vào **Phương pháp tiếp cận tùy chỉnh (Customized Approach)**. 
Mục tiêu chính là cho phép các thực thể đáp ứng mục tiêu của một yêu cầu PCI DSS theo cách không tuân thủ nghiêm ngặt các yêu cầu đã được định nghĩa sẵn, giúp tổ chức chủ động thiết kế các biện pháp kiểm soát bảo mật độc đáo và mang tính chiến lược phù hợp với môi trường riêng của mình.
### C. Key Points của Appendix D
Các tiêu chí quan trọng để thực hiện phương pháp này bao gồm:
- **Trách nhiệm của thực thể:** Phải lập hồ sơ ma trận kiểm soát, thực hiện phân tích rủi ro mục tiêu (Targeted Risk Analysis), kiểm tra tính hiệu quả và duy trì bằng chứng liên tục.
- **Trách nhiệm của đánh giá viên:** Phải xem xét tài liệu, tự xây dựng quy trình kiểm tra riêng và xác nhận xem việc triển khai của thực thể có đạt được mục tiêu của yêu cầu hay không.
- **Tính độc lập:** Đánh giá viên (QSA) không được tham gia vào việc thiết kế hoặc triển khai biện pháp kiểm soát mà họ sẽ trực tiếp đánh giá.
- **Sự phối hợp:** Thực thể và đánh giá viên phải thống nhất về việc các kiểm soát tùy chỉnh đáp ứng đầy đủ mục tiêu đề ra.
### D. Deep Summary của Appendix D
**Bối cảnh:**
Phương pháp tiếp cận tùy chỉnh được thiết kế cho các thực thể muốn áp dụng các công nghệ hoặc quy trình bảo mật sáng tạo mà vẫn đảm bảo đạt được các mục tiêu an ninh cốt lõi của PCI DSS thay vì chỉ tuân theo các bước thực hiện cứng nhắc.

**Nội dung cốt lõi:**
Trọng tâm của phương pháp này là việc chứng minh tính hiệu quả thông qua dữ liệu. Thực thể phải sử dụng các mẫu (template) cụ thể cho ma trận kiểm soát và phân tích rủi ro mục tiêu theo yêu cầu 12.3.2. Việc sử dụng phương pháp này phải được ghi chép lại bởi QSA hoặc ISA trong Báo cáo Tuân thủ (ROC).

**Dữ liệu đáng chú ý:**
- **Đối tượng hạn chế:** Các thực thể hoàn thành Bản tự đánh giá (SAQ) **không đủ điều kiện** sử dụng phương pháp tiếp cận tùy chỉnh.
- **Quy định bổ sung:** Việc sử dụng phương pháp này có thể bị quản lý và yêu cầu hướng dẫn thêm từ các tổ chức quản lý chương trình tuân thủ như các thương hiệu thanh toán hoặc ngân hàng thanh toán.

**Rủi ro / Lưu ý:**
- **Không có biện pháp bù đắp:** Biện pháp kiểm soát bù đắp (Compensating controls) **không phải là một lựa chọn** khi sử dụng phương pháp tùy chỉnh, vì thực thể đã được tự thiết kế kiểm soát để đáp ứng mục tiêu ban đầu.
- **Gánh nặng bằng chứng:** Thực thể phải liên tục giám sát và duy trì bằng chứng về tính hiệu quả của kiểm soát để cung cấp cho đánh giá viên trong mỗi kỳ kiểm tra.
### E. Structured Output của Appendix D
This approach is intended for entities that decide to meet a PCI DSS requirement’s stated Customized Approach Objective in a way that does not strictly follow the defined requirement. The customized approach allows an entity to take a strategic approach to meeting a requirement’s Customized Approach Objective, so it can determine and design the security controls needed to meet the objective in a manner unique for that organization.

**The entity implementing a customized approach must satisfy the following criteria:**
- Document and maintain evidence about each customized control, including all information specified in the Controls Matrix Template in *PCI DSS v4.x: Sample Templates to Support Customized Approach on the PCI SSC website*.
- Perform and document a targeted risk analysis (PCI DSS Requirement 12.3.2) for each customized control, including all information specified in the Targeted Risk Analysis Template in PCI DSS v4.x: Sample Templates to Support Customized Approach on the PCI SSC website.
- Perform testing of each customized control to prove effectiveness, and document testing performed, methods used, what was tested, when testing was performed, and results of testing in the controls matrix.
- Monitor and maintain evidence about the effectiveness of each customized control.
- Provide completed controls matrix(es), targeted risk analysis, testing evidence, and evidence of customized control effectiveness to its assessor.

**The assessor performing an assessment of customized controls must satisfy the following criteria:**
- Review the entity’s controls matrix(es), targeted risk analysis, and evidence of control effectiveness to fully understand the customized control(s) and to verify the entity meets all Customized Approach documentation and evidence requirements.
- Derive and document the appropriate testing procedures needed to conduct thorough testing of each customized control.
- Test each customized control to determine whether the entity’s implementation 1) meets the requirement’s Customized Approach Objective and 2) results in an “in place” finding for the requirement.
- At all times, QSAs maintain independence requirements defined in the QSA Qualification Requirements. This means if a QSA is involved in designing or implementing a customized control, that QSA does not also derive testing procedures for, assess, or assist with the assessment of that customized control.

The entity and its assessor are expected to work together to ensure 1) they agree that the customized control(s) fully meets the customized approach objective, 2) the assessor fully understands the customized control, and 3) the entity understands the derived testing the assessor will perform.

Use of the customized approach must be documented by a QSA or ISA in accordance with instructions in the Report on Compliance (ROC) Template and following the instructions in the FAQs for use with PCI DSS v4.x ROC Template available on the PCI SSC website.

Entities that complete a Self-Assessment Questionnaire are not eligible to use a customized approach; however, these entities may elect to have a QSA or ISA perform their assessment and document it in a ROC Template.

The use of the customized approach may be regulated by organizations that manage compliance programs (for example, payment brands and acquirers). Therefore, questions about use of a customized approach must be referred to those organizations, including, for example, whether an entity is required to use a QSA, or may use an ISA to complete an assessment using the customized approach.

**Note:** Compensating controls are not an option with the customized approach. Because the customized approach allows an entity to determine and design the controls needed to meet a requirement’s Customized Approach Objective, the entity is expected to effectively implement the controls it designed for that requirement without needing to also implement alternate, compensating controls.