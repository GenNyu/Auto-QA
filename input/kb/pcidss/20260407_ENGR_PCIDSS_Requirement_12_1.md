### A. Tài liệu gốc của Requirement 12

### B. Summary Overview của Control Objective 12.1
Tài liệu này mô tả chi tiết **Control Objective 12.1** của **Requirement 12** trong **PCI-DSS v4.0.1**, tập trung vào việc thiết lập, duy trì và quản lý chính sách an toàn thông tin ở cấp tổ chức.
Mục tiêu chính là đảm bảo chính sách an toàn thông tin được tài liệu hóa, cập nhật, phổ biến và có phân công trách nhiệm rõ ràng nhằm định hướng toàn bộ hoạt động bảo mật.
Gồm 4 sub-requirement chính:
- 12.1.1: Thiết lập và phổ biến security policy
- 12.1.2: Review và cập nhật policy
- 12.1.3: Phân định vai trò và trách nhiệm
- 12.1.4: Chỉ định trách nhiệm ở cấp quản lý
Áp dụng cho toàn bộ tổ chức, bao gồm nhân sự, vendor và đối tác liên quan.

### C. Key Points của Control Objective 12.1
- **Phạm vi áp dụng:**Toàn bộ tổ chức, nhân sự và bên thứ ba liên quan
- **Trách nhiệm:**Phân rõ vai trò và trách nhiệm về an toàn thông tin
- **Quản lý tài liệu:** Chính sách phải được tài liệu hóa, duy trì và phổ biến
- **Cập nhật:**Review ít nhất hàng năm và cập nhật theo thay đổi rủi ro
- **Truyền thông:**Nhân sự phải hiểu và xác nhận trách nhiệm bảo mật
- **Quản trị:**Phải có người chịu trách nhiệm ở cấp executive (CISO hoặc tương đương)

### D. Deep Summary của Control Objective 12.1
**Bối cảnh:**
Thiếu chính sách an toàn thông tin rõ ràng sẽ dẫn đến việc kiểm soát bảo mật không nhất quán và không đáp ứng yêu cầu pháp lý, bảo mật.
**Nội dung cốt lõi:**
- Thiết lập chính sách an toàn thông tin tổng thể cho tổ chức
- Phổ biến đến tất cả nhân sự và bên liên quan
- Review định kỳ (≥ 12 tháng) và cập nhật khi có thay đổi
- Phân rõ vai trò và trách nhiệm bảo mật cho từng cá nhân
- Yêu cầu nhân sự hiểu và xác nhận trách nhiệm
- Chỉ định người chịu trách nhiệm bảo mật ở cấp quản lý cao
**Dữ liệu đáng chú ý:**
- Chính sách phải được "disseminated" đến cả vendor và partner
- Phải có executive chịu trách nhiệm (CISO hoặc tương đương)
**Rủi ro / Lưu ý:**
- Không có policy → kiểm soát bảo mật rời rạc
- Policy không cập nhật → không phù hợp với rủi ro mới
- Nhân sự không hiểu trách nhiệm → dễ gây sai sót bảo mật
- Không có owner rõ ràng → thiếu accountability trong bảo mật

### E. Structured Output của Control Objective 12.1
**Control objectives:**12.1
**Sub-requirement:**12.1.1
**Defined Approach Requirements:**An overall information security policy is:
• Established.
• Published.
• Maintained.
• Disseminated to all relevant personnel, as well as to relevant vendors and business partners.
**Defined Approach Testing Procedures:**Examine the information security policy and interview personnel to verify that the overall information security policy is managed in accordance with all elements specified in this requirement.
**Customized Approach Objective:**The strategic objectives and principles of information security are defined, adopted, and known to all personnel.
**Guidance - Purpose:**An organization's overall information security policy ties to and governs all other policies and procedures that define protection of cardholder data. The information security policy communicates management's intent and objectives regarding the protection of its most valuable assets, including cardholder data. Without an information security policy, individuals will make their own value decisions on the controls that are required within the organization which may result in the organization neither meeting its legal, regulatory, and contractual obligations, nor being able to adequately protect its assets in a consistent manner. To ensure the policy is implemented, it is important that all relevant personnel within the organization, as well as relevant third parties, vendors, and business partners are aware of the organization's information security policy and their responsibilities for protecting information assets.
**Guidance - Good Practice:**The security policy for the organization identifies the purpose, scope, accountability, and information that clearly defines the organization's position regarding information security. The overall information security policy differs from individual security policies that address specific technology or security disciplines. This policy sets forth the directives for the entire organization whereas individual security policies align and support the overall security policy and communicate specific objectives for technology or security disciplines. It is important that all relevant personnel within the organization, as well as relevant third parties, vendors, and business partners are aware of the organization's information security policy and their responsibilities for protecting information assets.
**Guidance - Definitions:**'Relevant' for this requirement means that the information security policy is disseminated to those with roles applicable to some or all the topics in the policy, either within the company or because of services/functions performed by a vendor or third party.

---
**Control objectives:**12.1
**Sub-requirement:**12.1.2
**Defined Approach Requirements:**The information security policy is:
• Reviewed at least once every 12 months.
• Updated as needed to reflect changes to business objectives or risks to the environment.
**Defined Approach Testing Procedures:**Examine the information security policy and interview responsible personnel to verify the policy is managed in accordance with all elements specified in this requirement.
**Customized Approach Objective:**The information security policy continues to reflect the organization's strategic objectives and principles.
**Guidance - Purpose:**Security threats and associated protection methods evolve rapidly. Without updating the information security policy to reflect relevant changes, new measures to defend against these threats may not be addressed.

---
**Control objectives:**12.1
**Sub-requirement:**12.1.3
**Defined Approach Requirements:**The security policy clearly defines information security roles and responsibilities for all personnel, and all personnel are aware of and acknowledge their information security responsibilities.
**Defined Approach Testing Procedures:**
- "12.1.3.a": Examine the information security policy to verify that they clearly define information security roles and responsibilities for all personnel.
- "12.1.3.b": Interview personnel in various roles to verify they understand their information security responsibilities.
- "12.1.3.c": Examine documented evidence to verify personnel acknowledge their information security responsibilities.
**Customized Approach Objective:**Personnel understand their role in protecting the entity's cardholder data.
**Guidance - Purpose:**Without clearly defined security roles and responsibilities assigned, there could be misuse of the organization's information assets or inconsistent interaction with information security personnel, leading to insecure implementation of technologies or use of outdated or insecure technologies.

---
**Control objectives:**12.1
**Sub-requirement:**12.1.4
**Defined Approach Requirements:**Responsibility for information security is formally assigned to a Chief Information Security Officer or other information security knowledgeable member of executive management. .
**Defined Approach Testing Procedures:**Examine the information security policy to verify that information security is formally assigned to a Chief Information Security Officer or other information security-knowledgeable member of executive management.
**Customized Approach Objective:**A designated member of executive management is responsible for information security.
**Guidance - Purpose:**To ensure someone with sufficient authority and responsibility is actively managing and championing the organization's information security program, accountability and responsibility for information security needs to be assigned at the executive level within an organization.
**Guidance - Good Practice:**These executive management positions are often at the most senior level of management and are part of the chief executive level or C-level, typically reporting to the Chief Executive Officer or the Board of Directors. Information security knowledge for this executive management role can be indicated by work experience, education, and/or relevant professional certifications. The expectation is that this individual can provide assurance about the implementation of an effective security program and ensure the right technical experts are employed. Entities should also consider transition and/or succession plans for these key personnel to avoid potential gaps in critical security activities.