### A. Tài liệu gốc của Requirement 10

### B. Summary Overview của Control Objective 10.1
Tài liệu này mô tả chi tiết **Control Objective 10.1** của **Requirement 10** trong **PCI-DSS v4.0.1**, tập trung vào việc thiết lập và duy trì chính sách, quy trình và phân công trách nhiệm liên quan đến logging và monitoring.
Mục tiêu chính là đảm bảo các chính sách, quy trình và vai trò trách nhiệm được tài liệu hóa, cập nhật, áp dụng thực tế và được hiểu rõ bởi các bên liên quan trong hoạt động ghi log và giám sát.
Gồm 2 sub-requirement chính:
- 10.1.1: Quản lý chính sách và quy trình
- 10.1.2: Phân công vai trò và trách nhiệm
Áp dụng cho toàn bộ tổ chức và nhân sự tham gia vào các hoạt động logging và monitoring theo Requirement 10.

### C. Key Points của Control Objective 10.1
- **Phạm vi áp dụng:**Tất cả chính sách, quy trình và nhân sự liên quan logging và monitoring
- **Trách nhiệm:**Phân rõ vai trò, đảm bảo nhân sự hiểu và thực hiện đúng
- **Quản lý tài liệu:**Chính sách và quy trình phải được tài liệu hóa, cập nhật và phổ biến
- **Áp dụng thực tế:**Quy trình phải được triển khai và sử dụng thực tế
- **Truyền thông:**Đảm bảo các bên liên quan được phổ biến và hiểu nội dung

### D. Deep Summary của Control Objective 10.1
**Bối cảnh:**
Nếu chính sách và trách nhiệm không rõ ràng, các hoạt động logging và monitoring có thể không được thực hiện đầy đủ, làm giảm khả năng phát hiện sự cố bảo mật.
**Nội dung cốt lõi:**
- Tài liệu hóa chính sách và quy trình liên quan logging và monitoring
- Cập nhật khi có thay đổi về hệ thống hoặc yêu cầu giám sát
- Đảm bảo quy trình được áp dụng thực tế
- Phổ biến đến tất cả nhân sự liên quan
- Phân rõ vai trò và trách nhiệm cho từng hoạt động
**Dữ liệu đáng chú ý:**
- Chính sách và quy trình phải "in use" và "known to all affected parties"
- Có thể sử dụng RACI matrix để quản lý trách nhiệm
**Rủi ro / Lưu ý:**
- Chính sách không cập nhật → không phù hợp hệ thống hiện tại
- Quy trình không được thực thi → mất khả năng giám sát
- Nhân sự không rõ trách nhiệm → bỏ sót log/alert
- Thiếu phân công rõ ràng → không có accountability

### E. Structured Output của Control Objective 10.1
**Control objectives:**10.1
**Sub-requirement:**10.1.1
**Defined Approach Requirements:**All security policies and operational procedures that are identified in Requirement 10 are:
• Documented.
• Kept up to date.
• In use.
• Known to all affected parties.
**Defined Approach Testing Procedures:**Examine documentation and interview personnel to verify that security policies and operational procedures identified in Requirement 10 are managed in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Expectations, controls, and oversight for meeting activities within Requirement 10 are defined and adhered to by affected personnel. All supporting activities are repeatable, consistently applied, and conform to management's intent.
**Guidance - Purpose:**Requirement 10.1.1 is about effectively managing and maintaining the various policies and procedures specified throughout Requirement 10. While it is important to define the specific policies or procedures called out in Requirement 10, it is equally important to ensure they are properly documented, maintained, and disseminated.
**Guidance - Good Practice:**It is important to update policies and procedures as needed to address changes in processes, technologies, and business objectives. For this reason, consider updating these documents as soon as possible after a change occurs and not only on a periodic cycle.
**Guidance - Definitions:**Security policies define the entity's security objectives and principles. Operational procedures describe how to perform activities, and define the controls, methods, and processes that are followed to achieve the desired result in a consistent manner and in accordance with policy objectives.

---
**Control objectives:**10.1
**Sub-requirement:**10.1.2
**Defined Approach Requirements:**Roles and responsibilities for performing activities in Requirement 10 are documented, assigned, and understood.
**Defined Approach Testing Procedures:**
- "10.1.2.a": Examine documentation to verify that descriptions of roles and responsibilities for performing activities in Requirement 10 are documented and assigned.
- "10.1.2.b": Interview personnel with responsibility for performing activities in Requirement 10 to verify that roles and responsibilities are assigned as defined and are understood.
**Customized Approach Objective:** Day-to-day responsibilities for performing all the activities in Requirement 10 are allocated. Personnel are accountable for successful, continuous operation of these requirements.
**Guidance - Purpose:**If roles and responsibilities are not formally assigned, personnel may not be aware of their day-to-day responsibilities and critical activities may not occur.
**Guidance - Good Practice:**Roles and responsibilities may be documented within policies and procedures or maintained within separate documents. As part of communicating roles and responsibilities, entities can consider having personnel acknowledge their acceptance and understanding of their assigned roles and responsibilities.
**Guidance - Examples:**A method to document roles and responsibilities is a responsibility assignment matrix that includes who is responsible, accountable, consulted, and informed (also called a RACI matrix).