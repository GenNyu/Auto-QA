### A. Tài liệu gốc của Requirement 6

### B. Summary Overview của Control Objective 6.5
Tài liệu này mô tả chi tiết **Control Objective 6.5** của **Requirement 6** trong **PCI-DSS v4.0.1**, tập trung vào việc quản lý thay đổi hệ thống một cách an toàn nhằm đảm bảo không làm suy giảm kiểm soát bảo mật.
Mục tiêu chính là đảm bảo mọi thay đổi được kiểm soát, đánh giá tác động bảo mật, kiểm thử đầy đủ và triển khai một cách an toàn trong môi trường production.
Gồm 6 sub-requirement chính:
- 6.5.1: Quản lý thay đổi hệ thống
- 6.5.2: Xác nhận tuân thủ sau thay đổi
- 6.5.3: Tách biệt môi trường pre-production và production
- 6.5.4: Phân tách vai trò giữa các môi trường
- 6.5.5: Không sử dụng live PAN trong pre-production
- 6.5.6: Xóa test data và test account trước production
Áp dụng cho tất cả system components và các thay đổi trong môi trường production và pre-production.

### C. Key Points của Control Objective 6.5
- **Phạm vi áp dụng:**Tất cả thay đổi hệ thống và môi trường (production, pre-production)
- **Trách nhiệm:** Phân rõ vai trò, đảm bảo thay đổi được phê duyệt và kiểm soát
- **Quản lý thay đổi:**Phải có lý do, mô tả, đánh giá impact và phê duyệt
- **Kiểm thử:**Phải test đảm bảo không ảnh hưởng đến security trước khi deploy
- **Tách môi trường:**Pre-production phải tách biệt với production
- **Kiểm soát dữ liệu:**Không dùng live PAN và phải xóa test data trước production

### D. Deep Summary của Control Objective 6.5
**Bối cảnh:**
Thay đổi hệ thống là nguồn gây ra lỗi cấu hình và lỗ hổng bảo mật nếu không được kiểm soát chặt chẽ.
**Nội dung cốt lõi:**
- Thiết lập quy trình change management đầy đủ (mô tả, approval, test, rollback)
- Đánh giá tác động bảo mật trước khi triển khai thay đổi
- Xác nhận hệ thống vẫn tuân thủ PCI DSS sau thay đổi lớn
- Tách biệt môi trường production và pre-production
- Không sử dụng live PAN trong môi trường test
- Xóa test data và account trước khi đưa vào production
**Dữ liệu đáng chú ý:**
- Patch/test phải đảm bảo không làm suy giảm kiểm soát security
- Significant changes phải được re-validate toàn bộ control liên quan
**Rủi ro / Lưu ý:**
- Thay đổi không kiểm soát → gây lỗ hổng hoặc downtime
- Không test đầy đủ → ảnh hưởng security hoặc vận hành
- Không tách môi trường → rủi ro lan từ test sang production
- Dùng live PAN trong test → vi phạm PCI DSS nghiêm trọng
- Test data tồn tại trong production → bị khai thác dễ dàng

### E. Structured Output của Control Objective 6.5
**Control objectives:**6.5
**Sub-requirement:**6.5.1
**Defined Approach Requirements:**Changes to all system components in the production environment are made according to established procedures that include:
• Reason for, and description of, the change.
• Documentation of security impact.
• Documented change approval by authorized parties.
• Testing to verify that the change does not adversely impact system security.
• For bespoke and custom software changes, all updates are tested for compliance with Requirement 6.2.4 before being deployed into production.
• Procedures to address failures and return to a secure state.
**Defined Approach Testing Procedures:**
- "6.5.1.a": Examine documented change control procedures to verify procedures are defined for changes to all system components in the production environment to include all elements specified in this requirement.
- "6.5.1.b": Examine recent changes to system components and trace those changes back to related change control documentation. For each change examined, verify the change is implemented in accordance with all elements specified in this requirement.
**Customized Approach Objective:**All changes are tracked, authorized, and evaluated for impact and security, and changes are managed to avoid unintended effects to the security of system components.
**Guidance - Purpose:**Change management procedures must be applied to all changes-including the addition, removal, or modification of any system component-in the production environment. It is important to document the reason for a change and the change description so that relevant parties understand and agree the change is needed. Likewise, documenting the impacts of the change allows all affected parties to plan appropriately for any processing changes.
**Guidance - Good Practice:**Approval by authorized parties confirms that the change is legitimate and that the change is sanctioned by the organization. Changes should be approved by individuals with the appropriate authority and knowledge to understand the impact of the change. Thorough testing by the entity confirms that the security of the environment is not reduced by implementing a change and that all existing security controls either remain in place or are replaced with equal or stronger security controls after the change. The specific testing to be performed will vary according to the type of change and system component(s) affected. For each change, it is important to have documented procedures that address any failures and provide instructions on how to return to a secure state in case the change fails or adversely affects the security of an application or system. These procedures will allow the application or system to be restored to its previous secure state.

---
**Control objectives:**6.5
**Sub-requirement:**6.5.2
**Defined Approach Requirements:**Upon completion of a significant change, all applicable PCI DSS requirements are confirmed to be in place on all new or changed systems and networks, and documentation is updated as applicable.
**Defined Approach Testing Procedures:**Examine documentation for significant changes, interview personnel, and observe the affected systems/networks to verify that the entity confirmed applicable PCI DSS requirements were in place on all new or changed systems and networks and that documentation was updated as applicable.
**Customized Approach Objective:**All system components are verified after a significant change to be compliant with the applicable PCI DSS requirements.
**Applicability Notes:**These significant changes should also be captured and reflected in the entity's annual PCI DSS scope confirmation activity per Requirement 12.5.2.
**Guidance - Purpose:**Having processes to analyze significant changes helps ensure that all appropriate PCI DSS controls are applied to any systems or networks added or changed within the in-scope environment, and that PCI DSS requirements continue to be met to secure the environment.
**Guidance - Good Practice:**Building this validation into change management processes helps ensure that device inventories and configuration standards are kept up to date and security controls are applied where needed.
**Guidance - Examples:**Applicable PCI DSS requirements that could be impacted include, but are not limited to:
• Network and data-flow diagrams are updated to reflect changes.
• Systems are configured per configuration standards, with all default passwords changed and unnecessary services disabled.
• Systems are protected with required controls-for example, file integrity monitoring (FIM), anti- malware, patches, and audit logging.
• Sensitive authentication data is not stored, and all account data storage is documented and incorporated into data retention policy and procedures.
• New systems are included in the quarterly vulnerability scanning process.
• Systems are scanned for internal and external vulnerabilities after significant changes per Requirements 11.3.1.3 and 11.3.2.1.

---
**Control objectives:**6.5
**Sub-requirement:**6.5.3
**Defined Approach Requirements:**Pre-production environments are separated from production environments and the separation is enforced with access controls.
**Defined Approach Testing Procedures:**
- "6.5.3.a": Examine policies and procedures to verify that processes are defined for separating the pre- production environment from the production environment via access controls that enforce the separation.
- "6.5.3.b": Examine network documentation and configurations of network security controls to verify that the pre-production environment is separate from the production environment(s).
- "6.5.3.c": Examine access control settings to verify that access controls are in place to enforce separation between the pre-production and production environment(s).
**Customized Approach Objective:** Pre-production environments cannot introduce risks and vulnerabilities into production environments
**Guidance - Purpose:**Due to the constantly changing state of pre- production environments, they are often less secure than the production environment.
**Guidance - Good Practice:**Organizations must clearly understand which environments are test environments or development environments and how these environments interact on the level of networks and applications.
**Guidance - Definitions:**Pre-production environments include development, testing, user acceptance testing (UAT), etc. Even where production infrastructure is used to facilitate testing or development, production environments still need to be separated (logically or physically) from pre-production functionality such that vulnerabilities introduced as a result of pre-production activities do not adversely affect production systems.

---
**Control objectives:**6.5
**Sub-requirement:**6.5.4
**Defined Approach Requirements:**Roles and functions are separated between production and pre-production environments to provide accountability such that only reviewed and approved changes are deployed.
**Defined Approach Testing Procedures:**
- "6.5.4.a": Examine policies and procedures to verify that processes are defined for separating roles and functions to provide accountability such that only reviewed and approved changes are deployed.
- "6.5.4.b": Observe processes and interview personnel to verify implemented controls separate roles and functions and provide accountability such that only reviewed and approved changes are deployed.
**Customized Approach Objective:**Job roles and accountability that differentiate between pre-production and production activities are defined and managed to minimize the risk of unauthorized, unintentional, or inappropriate actions.
**Applicability Notes:**In environments with limited personnel where individuals perform multiple roles or functions, this same goal can be achieved with additional procedural controls that provide accountability. For example, a developer may also be an administrator that uses an administrator-level account with elevated privileges in the development environment and, for their developer role, they use a separate account with user-level access to the production environment.
**Guidance - Purpose:**The goal of separating roles and functions between production and pre-production environments is to reduce the number of personnel with access to the production environment and account data and thereby minimize risk of unauthorized, unintentional, or inappropriate access to data and system components and help ensure that access is limited to those individuals with a business need for such access. The intent of this control is to separate critical activities to provide oversight and review to catch errors and minimize the chances of fraud or theft (since two people would need to collude in order to hide an activity). Separating roles and functions, also referred to as separation or segregation of duties, is a key internal control concept to protect an entity's assets.

---
**Control objectives:**6.5
**Sub-requirement:**6.5.5
**Defined Approach Requirements:**Live PANs are not used in pre-production environments, except where those environments are included in the CDE and protected in accordance with all applicable PCI DSS requirements.
**Defined Approach Testing Procedures:**
- "6.5.5.a": Examine policies and procedures to verify that processes are defined for not using live PANs in pre-production environments, except where those environments are in a CDE and protected in accordance with all applicable PCI DSS requirements.
- "6.5.5.b": Observe testing processes and interview personnel to verify procedures are in place to ensure live PANs are not used in pre-production environments, except where those environments are in a CDE and protected in accordance with all applicable PCI DSS requirements.
- "6.5.5.c": Examine pre-production test data to verify live PANs are not used in pre-production environments, except where those environments are in a CDE and protected in accordance with all applicable PCI DSS requirements.
**Customized Approach Objective:**Live PANs cannot be present in pre-production environments outside the CDE.
**Guidance - Purpose:**Use of live PANs outside of protected CDEs provides malicious individuals with the opportunity to gain unauthorized access to cardholder data.
**Guidance - Definitions:**Live PANs refer to valid PANs (not test PANs) issued by, or on behalf of, a payment brand. Additionally, when payment cards expire, the same PAN is often reused with a different expiry date. All PANs must be verified as being unable to conduct payment transactions or pose fraud risk to the payment system before they are excluded from PCI DSS scope. It is the responsibility of the entity to confirm that PANs are not live.

---
**Control objectives:**6.5
**Sub-requirement:**6.5.6
**Defined Approach Requirements:**Test data and test accounts are removed from system components before the system goes into production.
**Defined Approach Testing Procedures:**
- "6.5.6.a": Examine policies and procedures to verify that processes are defined for removal of test data and test accounts from system components before the system goes into production.
- "6.5.6.b": Observe testing processes for both off-the- shelf software and in-house applications, and interview personnel to verify test data and test accounts are removed before a system goes into production.
- "6.5.6.c": Examine data and accounts for recently installed or updated off-the-shelf software and in- house applications to verify there is no test data or test accounts on systems in production.
**Customized Approach Objective:**Test data and test accounts cannot exist in production environments.
**Guidance - Purpose:**This data may give away information about the functioning of an application or system and is an easy target for unauthorized individuals to exploit to gain access to systems. Possession of such information could facilitate compromise of the system and related account data.