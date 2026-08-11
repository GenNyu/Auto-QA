### A. Tài liệu gốc của Requirement 12

### B. Summary Overview của Control Objective 12.4
Tài liệu này mô tả chi tiết** Control Objective 12.4 **của **Requirement 12 **trong **PCI-DSS v4.0.1**, tập trung vào việc thiết lập trách nhiệm quản trị và giám sát tuân thủ PCI DSS ở cấp quản lý.
Mục tiêu chính là đảm bảo trách nhiệm bảo vệ cardholder data và hoạt động tuân thủ PCI DSS được phân công rõ ràng ở cấp executive và được giám sát định kỳ.
Gồm 2 sub-requirement chính:
- 12.4.1: Trách nhiệm quản lý cấp cao
- 12.4.2: Review hoạt động tuân thủ định kỳ
Áp dụng cho service provider trong phạm vi PCI DSS.

### C. Key Points của Control Objective 12.4
- **Phạm vi áp dụng:**Service provider và chương trình tuân thủ PCI DSS
- **Trách nhiệm:** Executive management chịu trách nhiệm bảo mật và compliance
- **Quản trị:**Thiết lập chương trình PCI DSS compliance (charter, accountability)
- **Giám sát:**Review định kỳ việc thực hiện các kiểm soát bảo mật
- **Độc lập kiểm tra:**Review phải do người không trực tiếp thực hiện công việc
- **Tài liệu hóa:**Kết quả review và remediation phải được ghi nhận và phê duyệt

### D. Deep Summary của Control Objective 12.4
**Bối cảnh:**
Nếu không có sự tham gia của cấp quản lý cao và cơ chế giám sát độc lập, chương trình bảo mật có thể không được thực hiện hiệu quả hoặc thiếu tính nhất quán.
**Nội dung cốt lõi:**
- Giao trách nhiệm bảo mật và PCI DSS compliance cho executive management
- Thiết lập chương trình tuân thủ với accountability rõ ràng
- Thực hiện review định kỳ (ít nhất mỗi 3 tháng) để xác nhận các hoạt động bảo mật đang được thực hiện
- Review phải độc lập với người thực hiện công việc
- Ghi nhận kết quả review, remediation và phê duyệt bởi người có trách nhiệm
- Đảm bảo các hoạt động như log review, config review, incident response được thực hiện đúng
**Dữ liệu đáng chú ý:**
- Tần suất review tối thiểu: 3 tháng/lần
- Áp dụng cho các hoạt động như log review, change management, alert response
**Rủi ro / Lưu ý:**
- Không có accountability cấp cao → thiếu định hướng bảo mật
- Không review định kỳ → kiểm soát không được thực hiện
- Review không độc lập → thiếu khách quan
- Không tài liệu hóa → không có bằng chứng tuân thủ
- Không xử lý sai sót → lặp lại lỗi bảo mật

### E. Structured Output của Control Objective 12.4
**Control objectives:**12.4
**Sub-requirement:**12.4.1
**Defined Approach Requirements:**Additional requirement for service providers only: Responsibility is established by executive management for the protection of cardholder data and a PCI DSS compliance program to include:
• Overall accountability for maintaining PCI DSS compliance.
• Defining a charter for a PCI DSS compliance program and communication to executive management.
**Defined Approach Testing Procedures:**Additional testing procedure for service provider assessments only: Examine documentation to verify that executive management has established responsibility for the protection of cardholder data and a PCI DSS compliance program in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Executives are responsible and accountable for security of cardholder data.
**Applicability Notes:**This requirement applies only when the entity being assessed is a service provider. Executive management may include C-level positions, board of directors, or equivalent. The specific titles will depend on the particular organizational structure. Responsibility for the PCI DSS compliance program may be assigned to individual roles and/or to business units within the organization.
**Guidance - Purpose:**Executive management assignment of PCI DSS compliance responsibilities ensures executive- level visibility into the PCI DSS compliance program and allows for the opportunity to ask appropriate questions to determine the effectiveness of the program and influence strategic priorities.

---
**Control objectives:**12.4
**Sub-requirement:**12.4.2
**Defined Approach Requirements:**Additional requirement for service providers only: Reviews are performed at least once every three months to confirm that personnel are performing their tasks in accordance with all security policies and operational procedures. Reviews are performed by personnel other than those responsible for performing the given task and include, but are not limited to, the following tasks:
• Daily log reviews.
• Configuration reviews for network security controls.
• Applying configuration standards to new systems.
• Responding to security alerts.
• Change-management processes.
**Defined Approach Testing Procedures:**
- "12.4.2.a": Additional testing procedure for service provider assessments only: Examine policies and procedures to verify that processes are defined for conducting reviews to confirm that personnel are performing their tasks in accordance with all security policies and all operational procedures, including but not limited to the tasks specified in this requirement.
- "12.4.2.b": Additional testing procedure for service provider assessments only: Interview responsible personnel and examine records of reviews to verify that reviews are performed:
• At least once every three months.
• By personnel other than those responsible for performing the given task.
**Customized Approach Objective:**The operational effectiveness of critical PCI DSS controls is verified periodically by manual inspection of records.
**Applicability Notes:**This requirement applies only when the entity being assessed is a service provider.
**Guidance - Purpose:**Regularly confirming that security policies and procedures are being followed provides assurance that the expected controls are active and working as intended. This requirement is distinct from other requirements that specify a task to be performed. The objective of these reviews is not to reperform other PCI DSS requirements, but to confirm that security activities are being performed on an ongoing basis.
**Guidance - Good Practice:**These reviews can also be used to verify that appropriate evidence is being maintained-for example, audit logs, vulnerability scan reports, reviews of network security control rulesets-to assist in the entity's preparation for its next PCI DSS assessment.
**Guidance - Examples:**Looking at Requirement 1.2.7 as one example, Requirement 12.4.2 is met by confirming, at least once every three months, that reviews of configurations of network security controls have occurred at the required frequency. On the other hand, Requirement 1.2.7 is met by reviewing those configurations as specified in the requirement.

---
**Control objectives:**12.4
**Sub-requirement:**12.4.2.1
**Defined Approach Requirements:**Additional requirement for service providers only: Reviews conducted in accordance with Requirement 12.4.2 are documented to include:
• Results of the reviews.
• Documented remediation actions taken for any tasks that were found to not be performed at Requirement 12.4.2.
• Review and sign-off of results by personnel assigned responsibility for the PCI DSS compliance program.
**Defined Approach Testing Procedures:**Additional testing procedure for service provider assessments only: Examine documentation from the reviews conducted in accordance with PCI DSS Requirement 12.4.2 to verify the documentation includes all elements specified in this requirement.
**Customized Approach Objective:**Findings from operational effectiveness reviews are evaluated by management; appropriate remediation activities are implemented.
**Applicability Notes:**This requirement applies only when the entity being assessed is a service provider.
**Guidance - Purpose:**The intent of these independent checks is to confirm whether security activities are being performed on an ongoing basis. These reviews can also be used to verify that appropriate evidence is being maintained-for example, audit logs, vulnerability scan reports, reviews of network security control rulesets-to assist in the entity's preparation for its next PCI DSS assessment.