### A. Tài liệu gốc của Chapter 8

### B. Summary Overview của Chapter 8
Tài liệu này mô tả chi tiết **Chapter 8** trong **PCI-DSS v4.0.1**, tập trung vào **hai phương pháp tiếp cận để triển khai và xác nhận tuân thủ** tiêu chuẩn. 
Mục tiêu chính là mang lại sự linh hoạt cho các tổ chức trong việc lựa chọn phương pháp phù hợp nhất với trình độ bảo mật và khả năng triển khai thực tế của họ để đạt được các mục tiêu an ninh.

### C. Key Points của Chapter 8
- **Phương pháp Tiếp cận Xác định (Defined Approach):** Đây là phương pháp truyền thống, nơi các thực thể thực hiện chính xác theo các yêu cầu và quy trình kiểm tra đã được định nghĩa sẵn trong tiêu chuẩn.
- **Phương pháp Tiếp cận Tùy chỉnh (Customized Approach):** Tập trung vào việc đáp ứng "Mục tiêu Tiếp cận Tùy chỉnh" của từng yêu cầu, cho phép thực thể thiết kế các biện pháp kiểm soát riêng biệt không nhất thiết phải tuân theo các bước cụ thể của phương pháp truyền thống.
- **Kiểm soát Bù đắp (Compensating Controls):** Là một phần của Phương pháp Xác định, áp dụng khi thực thể có các ràng buộc kỹ thuật hoặc kinh doanh chính đáng không thể đáp ứng yêu cầu một cách trực tiếp.
- **Tính linh hoạt cao:** Thực thể có thể sử dụng đồng thời cả hai phương pháp (Xác định và Tùy chỉnh) cho các thành phần hệ thống hoặc môi trường khác nhau trong cùng một lần đánh giá.
- **Yêu cầu về năng lực:** Phương pháp Tùy chỉnh được thiết kế dành cho các thực thể đã "trưởng thành về rủi ro" (risk-mature) với quy trình quản lý rủi ro mạnh mẽ.

### D. Deep Summary của Chapter 8
**Bối cảnh:**
PCI DSS v4.0 giới thiệu sự thay đổi quan trọng trong cách xác nhận tuân thủ để hỗ trợ sự đổi mới trong các thực hành bảo mật, cho phép các tổ chức chứng minh cách thức các biện pháp kiểm soát hiện tại của họ đáp ứng được mục tiêu an ninh của tiêu chuẩn.

**Nội dung cốt lõi:**
- **Quy trình của Defined Approach:** Thực thể triển khai kiểm soát -> Kiểm toán viên sử dụng quy trình kiểm tra có sẵn trong tiêu chuẩn để xác minh.
- **Quy trình của Customized Approach:** Thực thể thiết kế kiểm soát đáp ứng Mục tiêu (Objective) -> Thực thể lập tài liệu giải trình -> Kiểm toán viên tự xây dựng (derive) quy trình kiểm tra riêng biệt để xác nhận hiệu quả của biện pháp kiểm soát đó.
- **Báo cáo hợp nhất:** Dù chọn con đường nào, bước cuối cùng vẫn là kiểm toán viên ghi nhận kết quả vào mẫu Báo cáo Tuân thủ (ROC) theo hướng dẫn chung.

**Dữ liệu đáng chú ý:**
- **Mức độ bảo mật:** Các biện pháp kiểm soát trong phương pháp Tùy chỉnh được kỳ vọng phải đáp ứng hoặc vượt quá mức độ an ninh so với phương pháp Xác định.
- **Hạn chế áp dụng:** Một số yêu cầu cụ thể không có "Mục tiêu Tiếp cận Tùy chỉnh", do đó không thể áp dụng phương pháp Tùy chỉnh cho những trường hợp này.
- **Tài liệu hóa:** Nỗ lực và khối lượng tài liệu cần thiết để xác nhận cho phương pháp Tùy chỉnh sẽ lớn hơn nhiều so với phương pháp Xác định.

**Rủi ro / Lưu ý:**
- **Trách nhiệm của kiểm toán viên:** Trong phương pháp Tùy chỉnh, kiểm toán viên phải tự xác định bằng chứng nào cần thu thập (quan sát, phỏng vấn, kiểm tra dữ liệu) vì không có quy trình kiểm tra sẵn có.
- **Điều kiện cho Compensating Controls:** Chỉ được sử dụng khi có ràng buộc thực tế và phải được thực thể lập hồ sơ, kiểm toán viên xem xét và xác nhận hàng năm.
- **Đối tượng phù hợp:** Phương pháp Xác định thường phù hợp hơn với các tổ chức mới tiếp cận PCI DSS hoặc muốn có sự hướng dẫn chi tiết về cách đạt được mục tiêu an ninh.

### E. Structured Output của Chapter 8
To support flexibility in how security objectives are met, there are two approaches for implementing and validating to PCI DSS. Entities should identify the approach best suited to their security implementation and use that approach to validate the controls.

#### Defined Approach
Follows the traditional method for implementing and validating PCI DSS and uses the Requirements and Testing Procedures defined within the standard. In the defined approach, the entity implements security controls to meet the stated requirements, and the assessor follows the defined testing procedures to verify that requirements have been met.

The defined approach supports entities with controls in place that meet PCI DSS requirements as stated. This approach may also suit entities that want more direction about how to meet security objectives, as well as entities new to information security or PCI DSS.

**Compensating Controls**
As part of the defined approach, entities that cannot meet a PCI DSS requirement explicitly as stated due to a legitimate and documented technical or business constraint may implement other, or compensating, controls, that sufficiently mitigate the risk associated with not meeting the requirement. On an annual basis, any compensating controls must be documented by the entity and reviewed and validated by the assessor and included with the Report on Compliance submission.

**Note:** For more details, see Appendix B: Compensating Controls and Appendix C: Compensating Controls Worksheet.

#### Customized Approach
Focuses on the Objective of each PCI DSS requirement (if applicable), allowing entities to implement controls to meet the requirement’s stated Customized Approach Objective in a way that does not strictly follow the defined requirement. Because each customized implementation will be different, there are no defined testing procedures; the assessor is required to derive testing procedures that are appropriate to the specific implementation to validate that the implemented controls meet the stated Objective.

The customized approach supports innovation in security practices, allowing entities greater flexibility to show how their current security controls meet PCI DSS objectives. This approach is intended for risk-mature entities that demonstrate a robust risk-management approach to security, including, but not limited to, a dedicated risk-management department or an organization-wide risk management approach.

The controls implemented and validated using the customized approach are expected to meet or exceed the security provided by the requirement in the defined approach. The level of documentation and effort required to validate customized implementations will also be greater than for the defined approach.

**Note:** For more details, see Appendix D: Customized Approach and PCI DSS v4.x: Sample Templates to Support Customized Approach on the PCI SSC website.

---
Most PCI DSS requirements can be met using either the defined or customized approach. However, several requirements do not have a stated Customized Approach Objective; the customized approach is not an option for these requirements.

Entities can use both the defined and customized approaches within their environment. This means an entity could use the defined approach to meet some requirements and use the customized approach to meet other requirements. This also means that an entity could use the defined approach to meet a given PCI DSS requirement for one system component or within one environment and use the customized approach to meet that same PCI DSS requirement for a different system component or within a different environment. In this way, a PCI DSS assessment could include both defined and customized testing procedures.

Figure 4 shows the two validation options for PCI DSS v4.x.

#### Figure 4. PCI DSS Validation Approaches
**PCI DSS Validation Approaches: How Entities Prove Compliance**
The process begins with the **Entity identifying their validation path**. Depending on how they have implemented their security controls, they must choose one of two main paths:

**Path 1: Defined Validation (The Traditional Approach)**
This path is used when an entity follows the specific requirements and testing procedures as written in the PCI DSS standard.

1.  **Implementation:** The Entity implements control(s) exactly per the PCI DSS requirement.
2.  **Special Case (Compensating Controls):** If the entity has a legitimate and documented technical or business constraint that prevents it from meeting a requirement as written, it must implement and document a **compensating control** for the assessor to review.
3.  **Assessment:** The Assessor performs the assessment using the predefined **PCI DSS Testing Procedure(s)**.

**Path 2: Customized Validation (The Flexible Approach)**
This path is intended for risk-mature entities that design their own security controls to meet a requirement's goal rather than following the standard steps.

1.  **Design:** The Entity designs and implements control(s) that meet the **Objective** of the PCI DSS requirement.
2.  **Documentation:** The Entity documents their customized control(s) and provides a clear explanation of how these controls meet the requirement's **Objective**.
3.  **Test Creation:** Since there are no standard tests for custom designs, the **Assessor derives testing procedure(s)**. This includes defining what to review, which evidence to examine/observe, and who to interview.
4.  **Assessment:** The Assessor performs the assessment based on those **assessor-derived testing procedure(s)**.

**Final Step: Consolidated Reporting**
Regardless of which path was chosen (Defined or Customized), the final step is the same:

- **Documentation:** The Assessor documents the results of the assessment according to the instructions found in the **ROC (Report on Compliance) Template**.
