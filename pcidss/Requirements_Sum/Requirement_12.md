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

================

### A. Tài liệu gốc của Requirement 12

### B. Summary Overview của Control Objective 12.2
Tài liệu này mô tả chi tiết **Control Objective 12.2** của **Requirement 12** trong **PCI-DSS v4.0.1**, tập trung vào việc thiết lập và quản lý chính sách sử dụng chấp nhận được đối với các công nghệ người dùng cuối.
Mục tiêu chính là đảm bảo việc sử dụng các thiết bị và công nghệ của người dùng được kiểm soát, chỉ sử dụng đúng mục đích và trong phạm vi được ủy quyền.
Gồm 1 sub-requirement chính:
- 12.2.1: Chính sách sử dụng chấp nhận được (acceptable use policy)
Áp dụng cho tất cả công nghệ người dùng cuối như laptop, mobile, email, Internet, wireless và remote access.

### C. Key Points của Control Objective 12.2
- **Phạm vi áp dụng:**Tất cả end-user technologies (device, software, network usage)
- **Trách nhiệm:**Tài liệu hóa và thực thi chính sách sử dụng
- **Kiểm soát sử dụng:**Quy định rõ các hành vi được phép và không được phép
- **Phê duyệt:** Việc sử dụng phải được phê duyệt bởi bên có thẩm quyền
- **Quản lý tài sản:**Danh sách thiết bị và phần mềm được phép sử dụng
- **Áp dụng thực tế:**Chính sách phải được triển khai và enforce

### D. Deep Summary của Control Objective 12.2
**Bối cảnh:**
Việc sử dụng công nghệ người dùng cuối không kiểm soát có thể dẫn đến rò rỉ dữ liệu, malware hoặc vi phạm chính sách bảo mật.
**Nội dung cốt lõi:**
- Xây dựng acceptable use policy cho các công nghệ người dùng
- Quy định rõ cách sử dụng đúng và sai đối với thiết bị và hệ thống
- Yêu cầu phê duyệt trước khi sử dụng công nghệ
- Duy trì danh sách thiết bị và phần mềm được phép
- Kết hợp policy với kiểm soát kỹ thuật để enforce
- Phổ biến cho người dùng để đảm bảo tuân thủ
**Dữ liệu đáng chú ý:**
- Bao gồm nhiều loại công nghệ: laptop, mobile, email, Internet, removable media
- Chính sách nên rõ ràng dạng "do / do not"
**Rủi ro / Lưu ý:**
- Sử dụng thiết bị không kiểm soát → rò rỉ dữ liệu
- Không có policy rõ ràng → người dùng sử dụng sai mục đích
- Không enforce → policy không có hiệu lực thực tế
- Thiếu phê duyệt → sử dụng công nghệ không được phép

### E. Structured Output của Control Objective 12.2
**Control objectives:**12.2
**Sub-requirement:**12.2.1
**Defined Approach Requirements:**Acceptable use policies for end-user technologies are documented and implemented, including:
• Explicit approval by authorized parties.
• Acceptable uses of the technology.
• List of products approved by the company for employee use, including hardware and software.
**Defined Approach Testing Procedures:**Examine the acceptable use policies for end-user technologies and interview responsible personnel to verify processes are documented and implemented in accordance with all elements specified in this requirement.
**Customized Approach Objective:**The use of end-user technologies is defined and managed to ensure authorized usage.
**Applicability Notes:**Examples of end-user technologies for which acceptable use policies are expected include, but are not limited to, remote access and wireless technologies, laptops, tablets, mobile phones, and removable electronic media, email usage, and Internet usage.
**Guidance - Purpose:**End-user technologies are a significant investment and may pose significant risk to an organization if not managed properly. Acceptable use policies outline the expected behavior from personnel when using the organization's information technology and reflect the organization's risk tolerance These policies instruct personnel on what they can and cannot do with company equipment and instruct personnel on correct and incorrect uses of company Internet and email resources. Such policies can legally protect an organization and allow it to act when the policies are violated.
**Guidance - Good Practice:**It is important that usage policies are supported by technical controls to manage the enforcement of the policies. Structuring polices as simple 'do' and 'do not' requirements that are linked to a purpose can help remove ambiguity and provide personnel with the context for the requirement.

================

### A. Tài liệu gốc của Requirement 12

### B. Summary Overview của Control Objective 12.3
Tài liệu này mô tả chi tiết **Control Objective 12.3** của **Requirement 12** trong **PCI-DSS v4.0.1**, tập trung vào việc thực hiện phân tích rủi ro có mục tiêu và quản lý vòng đời công nghệ.
Mục tiêu chính là đảm bảo các quyết định liên quan đến tần suất kiểm soát, công nghệ và bảo mật được dựa trên phân tích rủi ro có cơ sở và được cập nhật định kỳ.
Gồm 4 sub-requirement chính:
- 12.3.1: Thực hiện targeted risk analysis
- 12.3.2: Risk analysis cho customized approach
- 12.3.3: Quản lý cryptographic protocol
- 12.3.4: Quản lý vòng đời công nghệ
Áp dụng cho các yêu cầu PCI DSS có risk-based frequency, các hệ thống sử dụng cryptography và toàn bộ công nghệ trong môi trường.

### C. Key Points của Control Objective 12.3
- **Phạm vi áp dụng:**Risk analysis, cryptography và toàn bộ công nghệ hệ thống
- **Trách nhiệm:**Tài liệu hóa và thực hiện phân tích rủi ro
- **Phân tích rủi ro:**Xác định asset, threat, likelihood và impact
- **Review định kỳ:** Thực hiện ít nhất hàng năm và khi có thay đổi
- **Quản lý cryptography:**Inventory, theo dõi và có kế hoạch xử lý khi yếu
- **Quản lý công nghệ:**Review lifecycle, hỗ trợ vendor và kế hoạch thay thế
- **Phê duyệt:**Một số nội dung yêu cầu approval từ senior management

### D. Deep Summary của Control Objective 12.3
**Bối cảnh:**
Không có phân tích rủi ro phù hợp sẽ dẫn đến việc thiết lập kiểm soát không hiệu quả hoặc không phù hợp với môi trường và mối đe dọa thực tế.
**Nội dung cốt lõi:**
- Thực hiện targeted risk analysis cho các control có flexibility
- Xác định asset, threat, likelihood và impact để quyết định tần suất
- Review risk analysis ít nhất hàng năm và cập nhật khi cần
- Quản lý cryptographic protocol: inventory, theo dõi xu hướng và kế hoạch thay đổi
- Quản lý công nghệ: đánh giá tình trạng hỗ trợ, EOL và kế hoạch thay thế
- Áp dụng phê duyệt và quản trị ở cấp quản lý
**Dữ liệu đáng chú ý:**
- Risk analysis phải bao gồm asset, threat, likelihood, impact
- Review tối thiểu 12 tháng/lần
- Bao gồm cả cryptographic agility và technology lifecycle
**Rủi ro / Lưu ý:**
- Không có risk analysis → kiểm soát không phù hợp
- Cryptography lỗi thời → dễ bị khai thác
- Công nghệ EOL → không được vá lỗi
- Không cập nhật → không theo kịp threat mới
- Không có kế hoạch thay thế → gián đoạn bảo mật

### E. Structured Output của Control Objective 12.3
**Control objectives:**12.3
**Sub-requirement:**12.3.1
**Defined Approach Requirements:**For each PCI DSS requirement that specifies completion of a targeted risk analysis, the analysis is documented and includes:
• Identification of the assets being protected.
• Identification of the threat(s) that the requirement is protecting against.
• Identification of factors that contribute to the likelihood and/or impact of a threat being realized.
• Resulting analysis that determines, and includes justification for, how the frequency or processes defined by the entity to meet the requirement minimize the likelihood and/or impact of the threat being realized.
• Review of each targeted risk analysis at least once every 12 months to determine whether the results are still valid or if an updated risk analysis is needed.
• Performance of updated risk analyses when needed, as determined by the annual review.
**Defined Approach Testing Procedures:**Examine documented policies and procedures to verify a process is defined for performing targeted risk analyses for each PCI DSS requirement that specifies completion of a targeted risk analysis, and that the process includes all elements specified in this requirement.
**Customized Approach Objective:**Up to date knowledge and assessment of risks to the CDE are maintained.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Some PCI DSS requirements allow an entity to define how frequently an activity is performed based on the risk to the entity's environment. Performing this risk analysis according to a methodology ensures validity and consistency with policies and procedures. This targeted risk analysis (as opposed to a traditional enterprise-wide risk assessment) focuses on those PCI DSS requirements that allow an entity flexibility about how frequently an entity performs a given control. For this risk analysis, the entity carefully evaluates each PCI DSS requirement that provides this flexibility and determines the frequency that supports adequate security for the entity, and the level of risk the entity is willing to accept. The risk analysis identifies the specific assets, such as the system components and data-for example, log files, or credentials-that the requirement is intended to protect, as well as the threat(s) or outcomes that the requirement is protecting the assets from-for example, malware, an undetected intruder, or misuse of credentials. Examples of factors that could contribute to likelihood or impact include any that could increase the vulnerability of an asset to a threat—for example, exposure to untrusted networks, complexity of environment, or high staff turnover—as well as the criticality of the system components, or volume and sensitivity of the data, being protected. Reviewing the results of these targeted risk analyses at least once every 12 months and upon changes that could impact the risk to the environment allows the organization to ensure the risk analysis results remain current with organizational changes and evolving threats, trends, and technologies, and that the selected frequencies still adequately address the entity's risk.
**Guidance - Good Practice:**An enterprise-wide risk assessment, which is a point-in-time activity that enables entities to identify threats and associated vulnerabilities, is recommended, but is not required, for entities to determine and understand broader and emerging threats with the potential to negatively impact its business. This enterprise-wide risk assessment could be established as part of an overarching risk management program that is used as an input to the annual review of an organization's overall information security policy (see Requirement 12.1.1).
**Guidance - Further Information:**Refer to the following documents on the PCI SSC website:
• Information Supplement: TRA Guidance
• Sample Template: TRA for Activity Frequency .

---
**Control objectives:**12.3
**Sub-requirement:**12.3.2
**Defined Approach Requirements:**A targeted risk analysis is performed for each PCI DSS requirement that the entity meets with the customized approach, to include:
• Documented evidence detailing each element specified in Appendix D: Customized Approach (including, at a minimum, a controls matrix and risk analysis).
• Approval of documented evidence by senior management.
• Performance of the targeted analysis of risk at least once every 12 months.
**Defined Approach Testing Procedures:**Examine the documented targeted risk- analysis for each PCI DSS requirement that the entity meets with the customized approach to verify that documentation for each requirement exists and is in accordance with all elements specified in this requirement.
**Customized Approach Objective:**This requirement is part of the customized approach and must be met for those using the customized approach.
**Applicability Notes:**This requirement only applies to entities using a Customized Approach.
**Guidance - Purpose:**A risk analysis following a repeatable and robust methodology enables an entity to meet the customized approach objective.
**Guidance - Definitions:**The customized approach to meeting a PCI DSS requirement allows entities to define the controls used to meet a given requirement's stated Customized Approach Objective in a way that does not strictly follow the defined requirement. These controls are expected to at least meet or exceed the security provided by the defined requirement and require extensive documentation by the entity using the customized approach.
**Guidance - Further Information:**See Appendix D: Customized Approach for instructions on how to document the required evidence for the customized approach. See PCI DSS v4.x: Sample Templates to Support Customized Approach on the PCI SSC website for templates that entities may use to document their customized controls. Note that while use of the templates is optional, the information specified within each template must be documented and provided to each entity's assessor.

---
**Control objectives:**12.3
**Sub-requirement:**12.3.3
**Defined Approach Requirements:**Cryptographic cipher suites and protocols in use are documented and reviewed at least once every 12 months, including at least the following:
• An up-to-date inventory of all cryptographic cipher suites and protocols in use, including purpose and where used.
• Active monitoring of industry trends regarding continued viability of all cryptographic cipher suites and protocols in use.
• Documentation of a plan, to respond to anticipated changes in cryptographic vulnerabilities.
**Defined Approach Testing Procedures:**Examine documentation for cryptographic suites and protocols in use and interview personnel to verify the documentation and review is in accordance with all elements specified in this requirement.
**Customized Approach Objective:**The entity is able to respond quickly to any vulnerabilities in cryptographic protocols or algorithms, where those vulnerabilities affect protection of cardholder data.
**Applicability Notes:**The requirement applies to all cryptographic cipher suites and protocols used to meet PCI DSS requirements, including, but not limited to, those used to render PAN unreadable in storage and transmission, to protect passwords, and as part of authenticating access. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Protocols and encryption strengths may quickly change or be deprecated due to identification of vulnerabilities or design flaws. In order to support current and future data security needs, entities need to know where cryptography is used and understand how they would be able to respond rapidly to changes impacting the strength of their cryptographic implementations.
**Guidance - Good Practice:**Cryptographic agility is important to ensure an alternative to the original encryption method or cryptographic primitive is available, with plans to upgrade to the alternative without significant change to system infrastructure. For example, if the entity is aware of when protocols or algorithms will be deprecated by standards bodies, proactive plans will help the entity to upgrade before the deprecation is impactful to operations.
**Guidance - Definitions:**'Cryptographic agility' refers to the ability to monitor and manage the encryption and related verification technologies deployed across an organization.
**Guidance - Further Information:**Refer to NIST SP 800-131a, Transitioning the Use of Cryptographic Algorithms and Key Lengths .

---
**Control objectives:**12.3
**Sub-requirement:**12.3.4
**Defined Approach Requirements:**Hardware and software technologies in use are reviewed at least once every 12 months, including at least the following:
• Analysis that the technologies continue to receive security fixes from vendors promptly.
• Analysis that the technologies continue to support (and do not preclude) the entity's PCI DSS compliance.
• Documentation of any industry announcements or trends related to a technology, such as when a vendor has announced 'end of life' plans for a technology.
• Documentation of a plan, approved by senior management, to remediate outdated technologies, including those for which vendors have announced 'end of life' plans.
**Defined Approach Testing Procedures:**Examine documentation for the review of hardware and software technologies in use and interview personnel to verify that the review is in accordance with all elements specified in this requirement.
**Customized Approach Objective:**The entity's hardware and software technologies are up to date and supported by the vendor. Plans to remove or replace all unsupported system components are reviewed periodically.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Hardware and software technologies are constantly evolving, and organizations need to be aware of changes to the technologies they use, as well as the evolving threats to those technologies to ensure that they can prepare for, and manage, vulnerabilities in hardware and software that will not be remediated by the vendor or developer.
**Guidance - Good Practice:**Organizations should review firmware versions to ensure they remain current and supported by the vendors. Organizations also need to be aware of changes made by technology vendors to their products or processes to understand how such changes may impact the organization's use of the technology. Regular reviews of technologies that impact or influence PCI DSS controls can assist with purchasing, usage, and deployment strategies, and ensure controls that rely on those technologies remain effective. These reviews include, but are not limited to, reviewing technologies that are no longer supported by the vendor and/or no longer meet the security needs of the organization.

================

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

================

### A. Tài liệu gốc của Requirement 12

### B. Summary Overview của Control Objective 12.5
Tài liệu này mô tả chi tiết **Control Objective 12.5** của** Requirement 12** trong **PCI-DSS v4.0.1**, tập trung vào việc xác định, duy trì và xác nhận phạm vi (scope) PCI DSS và các hệ thống liên quan.
Mục tiêu chính là đảm bảo toàn bộ system components, data flow và kết nối liên quan đến cardholder data được xác định đầy đủ và luôn nằm trong phạm vi kiểm soát.
Gồm 3 sub-requirement chính:
- 12.5.1: Quản lý inventory system components
- 12.5.2: Xác nhận và duy trì PCI DSS scope
- 12.5.3: Đánh giá thay đổi cấu trúc tổ chức
Áp dụng cho toàn bộ hệ thống, dữ liệu và môi trường liên quan đến CDE.

### C. Key Points của Control Objective 12.5
- **Phạm vi áp dụng**: Tất cả system components, data flow và kết nối liên quan CDE.
- **Trách nhiệm**: **Tài liệu hóa** và duy trì inventory cũng như xác nhận phạm vi bảo mật.
- **Quản lý tài liệu / cấu hình**: Duy trì danh sách system components kèm mô tả chức năng và cách sử dụng.
- **Xác định scope**: Bao gồm xác định luồng dữ liệu (data flow), vị trí lưu trữ CHD, các hệ thống trong CDE và các kết nối liên quan.
- **Kiểm soát / bảo vệ**: Xác định các biện pháp chia phân vùng (segmentation control) và quản lý các kết nối từ bên thứ ba

### D. Deep Summary của Control Objective 12.5
**Bối cảnh:**
Nếu không xác định đúng phạm vi PCI DSS, các hệ thống chứa hoặc liên quan đến dữ liệu thẻ có thể bị bỏ sót và không được bảo vệ đầy đủ. Việc duy trì danh sách thành phần hệ thống hiện tại cho phép tổ chức thực hiện các yêu cầu bảo mật một cách chính xác và hiệu quả
**Nội dung cốt lõi:**
- Duy trì Inventory: Luôn cập nhật danh sách đầy đủ các system components trong phạm vi để tránh việc vô tình loại bỏ các hệ thống khỏi tiêu chuẩn cấu hình
- Phân tích luồng dữ liệu: Xác định rõ ràng cách thức dữ liệu thẻ di chuyển qua các giai đoạn thanh toán và các kênh chấp nhận khác nhau
- Xác định vị trí dữ liệu: Tìm kiếm và liệt kê tất cả các điểm lưu trữ, xử lý và truyền CHD, bao gồm cả các bản sao lưu và dữ liệu ngoài vùng CDE hiện tại
- Xác nhận phân vùng: Kiểm tra tính hiệu quả của segmentation và các kết nối từ bên thứ ba để đảm bảo ranh giới bảo mật
- Đánh giá thay đổi: Thực hiện rà soát lại phạm vi khi có sự thay đổi lớn về hạ tầng hoặc cấu trúc tổ chức để đảm bảo các kiểm soát vẫn được duy trì
**Dữ liệu đáng chú ý:**
- Phải có sơ đồ luồng dữ liệu (data flow diagram) và danh sách vị trí CHD
- Thực hiện xác nhận scope tối thiểu 12 tháng/lần hoặc sau khi có thay đổi lớn
- Service Provider phải thực hiện xác nhận scope ít nhất 6 tháng/lần
**Rủi ro / Lưu ý:**
- Scope không đầy đủ dẫn đến việc bỏ sót các hệ thống quan trọng cần được bảo vệ
- Thiếu inventory cập nhật khiến tổ chức không biết rõ các hệ thống nào đang nằm trong phạm vi kiểm soát
- Các kết nối từ bên thứ ba không được kiểm soát có thể trở thành điểm xâm nhập rủi ro vào CDE
- Hiểu sai về segmentation dẫn đến việc áp dụng sai phạm vi bảo mật cho môi trường

### E. Structured Output của Control Objective 12.5
**Control objectives:**12.5
**Sub-requirement:**12.5.1
**Defined Approach Requirements:**An inventory of system components that are in scope for PCI DSS, including a description of function/use, is maintained and kept current.
**Defined Approach Testing Procedures:**
- "12.5.1.a": Examine the inventory to verify it includes all in-scope system components and a description of function/use for each.
- "12.5.1.b": Interview personnel to verify the inventory is kept current.
**Customized Approach Objective:**All system components in scope for PCI DSS are identified and known.
**Guidance - Purpose:**Maintaining a current list of all system components will enable an organization to define the scope of its environment and implement PCI DSS requirements accurately and efficiently. Without an inventory, some system components could be overlooked and be inadvertently excluded from the organization's configuration standards.
**Guidance - Good Practice:**If an entity keeps an inventory of all assets, those system components in scope for PCI DSS should be clearly identifiable among the other assets. Inventories should include containers or images that may be instantiated. Assigning an owner to the inventory helps to ensure the inventory stays current.
**Guidance - Examples:**Methods to maintain an inventory include as a database, as a series of files, or in an inventory- management tool.

---
**Control objectives:**12.5
**Sub-requirement:**12.5.2
**Defined Approach Requirements:**PCI DSS scope is documented and confirmed by the entity at least once every 12 months and upon significant change to the in-scope environment. At a minimum, the scoping validation includes:
• Identifying all data flows for the various payment stages (for example, authorization, capture settlement, chargebacks, and refunds) and acceptance channels (for example, card- present, card-not-present, and e-commerce).
• Updating all data-flow diagrams per Requirement 1.2.4.
• Identifying all locations where account data is stored, processed, and transmitted, including but not limited to: 1) any locations outside of the currently defined CDE, 2) applications that process CHD, 3) transmissions between systems and networks, and 4) file backups.
• Identifying all system components in the CDE, connected to the CDE, or that could impact security of the CDE.
• Identifying all segmentation controls in use and the environment(s) from which the CDE is segmented, including justification for environments being out of scope.
• Identifying all connections from third-party entities with access to the CDE.
• Confirming that all identified data flows, account data, system components, segmentation controls, and connections from third parties with access to the CDE are included in scope.
**Defined Approach Testing Procedures:**
- "12.5.2.a": Examine documented results of scope reviews and interview personnel to verify that the reviews are performed: • At least once every 12 months. • After significant changes to the in-scope environment.
- "12.5.2.b": Examine documented results of scope reviews performed by the entity to verify that PCI DSS scoping confirmation activity includes all elements specified in this requirement.
**Customized Approach Objective:**PCI DSS scope is verified periodically, and after significant changes, by comprehensive analysis and appropriate technical measures.
**Applicability Notes:**This annual confirmation of PCI DSS scope is an activity expected to be performed by the entity under assessment, and is not the same, nor is it intended to be replaced by, the scoping confirmation performed by the entity's assessor during the annual assessment.
**Guidance - Purpose:**Frequent validation of PCI DSS scope helps to ensure PCI DSS scope remains up to date and aligned with changing business objectives, and therefore that security controls are protecting all appropriate system components.
**Guidance - Good Practice:**Accurate scoping involves critically evaluating the CDE and all connected system components to determine the necessary coverage for PCI DSS requirements. Scoping activities, including careful analysis and ongoing monitoring, help to ensure that in-scope systems are appropriately secured. When documenting account data locations, the entity can consider creating a table or spreadsheet that includes the following information:
• Data stores (databases, files, cloud, etc.), including the purpose of data storage and the retention period,
• Which CHD elements are stored (PAN, expiry date, cardholder name, and/or any elements of SAD prior to completion of authorization),
• How data is secured (type of encryption and strength, hashing algorithm and strength, truncation, tokenization),
• How access to data stores is logged, including a description of logging mechanism(s) in use (enterprise solution, application level, operating system level, etc.).
In addition to internal systems and networks, all connections from third-party entities—for example, business partners, entities providing remote support services, and other service providers—need to be identified to determine inclusion for PCI DSS scope. Once the in-scope connections have been identified, the applicable PCI DSS controls can be implemented to reduce the risk of a third-party connection being used to compromise an entity's CDE. A data discovery tool or methodology can be used to facilitate identifying all sources and locations of PAN, and to look for PAN that resides on systems and networks outside the currently defined CDE or in unexpected places within the defined CDE—for example, in an error log or memory dump file. This approach can help ensure that previously unknown locations of PAN are detected and that the PAN is either eliminated or properly secured.
**Guidance - Further Information:**For additional guidance, refer to Information Supplement: Guidance for PCI DSS Scoping and Network Segmentation .

---
**Control objectives:**12.5
**Sub-requirement:**12.5.2.1
**Defined Approach Requirements:**Additional requirement for service providers only: PCI DSS scope is documented and confirmed by the entity at least once every six months and upon significant change to the in-scope environment. At a minimum, the scoping validation includes all the elements specified in Requirement 12.5.2.
**Defined Approach Testing Procedures:**
- "12.5.2.1.a": Additional testing procedure for service provider assessments only: Examine documented results of scope reviews and interview personnel to verify that reviews per Requirement 12.5.2 are performed: • At least once every six months, and • After significant changes
- "12.5.2.1.b": Additional testing procedure for service provider assessments only: Examine documented results of scope reviews to verify that scoping validation includes all elements specified
**Customized Approach Objective:** The accuracy of PCI DSS scope is verified to be continuously accurate by comprehensive analysis and appropriate technical measures.
**Applicability Notes:** This requirement applies only when the entity being assessed is a service provider. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Service providers typically have access to greater volumes of cardholder data than do merchants, or can provide an entry point that can be exploited to then compromise multiple other entities. Service providers also typically have larger and more complex networks that are subject to more frequent change. The probability of overlooked changes to scope in complex and dynamic networks is greater in service-providers environments. Validating PCI DSS scope more frequently is likely to discover such overlooked changes before they can be exploited by an attacker.

---
**Control objectives:**12.5
**Sub-requirement:**12.5.3
**Defined Approach Requirements:**Additional requirement for service providers only: Significant changes to organizational structure result in a documented (internal) review of the impact to PCI DSS scope and applicability of controls, with results communicated to executive management.
**Defined Approach Testing Procedures:**
- "12.5.3.a": Additional testing procedure for service provider assessments only: Examine policies and procedures to verify that processes are defined such that a significant change to organizational structure results in documented review of the impact to PCI DSS scope and applicability of controls.
- "12.5.3.b": Additional testing procedure for service provider assessments only: Examine documentation (for example, meeting minutes) and interview responsible personnel to verify that significant changes to organizational structure resulted in documented reviews that included all elements specified in this requirement, with results communicated to executive management.
**Customized Approach Objective:**PCI DSS scope is confirmed after significant organizational change.
**Applicability Notes:**This requirement applies only when the entity being assessed is a service provider. This requirement is a best practice until 31 March 2025, after which it will be required and must be
**Guidance - Purpose:**An organization's structure and management define the requirements and protocol for effective and secure operations. Changes to this structure could have negative effects to existing controls and frameworks by reallocating or removing resources that once supported PCI DSS controls or inheriting new responsibilities that may not have established controls in place. Therefore, it is important to revisit PCI DSS scope and controls when there are changes to an organization's structure and management to ensure controls are in place and active.
**Guidance - Examples:**Changes to organizational structure include, but are not limited to, company mergers or acquisitions, and significant changes or reassignments of personnel with responsibility for security controls.

================

### A. Tài liệu gốc của Requirement 12

### B. Summary Overview của Control Objective 12.6
Tài liệu này mô tả chi tiết **Control Objective 12.6** của **Requirement 12 **trong **PCI-DSS v4.0.1**, tập trung vào việc xây dựng và duy trì chương trình đào tạo nhận thức an toàn thông tin cho nhân sự.
Mục tiêu chính là đảm bảo tất cả nhân sự hiểu rõ rủi ro bảo mật, trách nhiệm của mình và cách bảo vệ cardholder data trong quá trình làm việc.
Gồm 3 sub-requirement chính:
- 12.6.1: Thiết lập security awareness program
- 12.6.2: Review và cập nhật chương trình
- 12.6.3: Đào tạo và xác nhận nhận thức của nhân sự
Áp dụng cho toàn bộ nhân sự trong tổ chức.

### C. Key Points của Control Objective 12.6
- **Phạm vi áp dụng:**Tất cả nhân sự trong tổ chức
- **Trách nhiệm:**Tài liệu hóa và triển khai chương trình đào tạo nhận thức
- **Đào tạo:**Thực hiện khi onboard và ít nhất hàng năm
- **Nội dung:**Bao gồm threat, phishing, social engineering và acceptable use
- **Truyền thông:**Sử dụng nhiều hình thức (training, email, poster…)
- **Xác nhận:**Nhân sự phải xác nhận đã hiểu policy
- **Cập nhật:**Chương trình phải review và cập nhật định kỳ

### D. Deep Summary của Control Objective 12.6
**Bối cảnh:**
Nhân sự là một trong những điểm yếu lớn nhất trong bảo mật, đặc biệt với các tấn công như phishing và social engineering.
**Nội dung cốt lõi:**
- Thiết lập chương trình security awareness cho toàn bộ nhân sự
- Đào tạo khi tuyển dụng và định kỳ hàng năm
- Cập nhật nội dung theo threat landscape mới
- Bao gồm nhận diện phishing, social engineering và sử dụng công nghệ đúng cách
- Sử dụng nhiều phương thức truyền thông để tăng hiệu quả
- Yêu cầu nhân sự xác nhận đã đọc và hiểu policy
- Có cơ chế hỗ trợ và hướng dẫn khi cần
**Dữ liệu đáng chú ý:**
- Training tối thiểu: khi onboarding + mỗi 12 tháng
- Bao gồm nội dung phishing, social engineering và acceptable use
**Rủi ro / Lưu ý:**
- Nhân sự không được đào tạo → dễ bị tấn công
- Không cập nhật nội dung → không theo kịp threat mới
- Không xác nhận → không đảm bảo hiểu policy
- Đào tạo không hiệu quả → không thay đổi hành vi bảo mật

### E. Structured Output của Control Objective 12.6
**Control objectives:**12.6
**Sub-requirement:**12.6.1
**Defined Approach Requirements:**A formal security awareness program is implemented to make all personnel aware of the entity's information security policy and procedures, and their role in protecting the cardholder data.
**Defined Approach Testing Procedures:**Examine the security awareness program to verify it provides awareness to all personnel about the entity's information security policy and procedures, and personnel's role in protecting the cardholder data.
**Customized Approach Objective:**Personnel are knowledgeable about the threat landscape, their responsibility for the operation of relevant security controls, and are able to access assistance and guidance when required.
**Guidance - Purpose:**If personnel are not educated about their company's information security policies and procedures and their own security responsibilities, security safeguards and processes that have been implemented may become ineffective through unintentional errors or intentional actions.

---
**Control objectives:**12.6
**Sub-requirement:**12.6.2
**Defined Approach Requirements:**The security awareness program is:
• Reviewed at least once every 12 months, and
• Updated as needed to address any new threats and vulnerabilities that may impact the security of the entity's cardholder data and/or sensitive authentication data, or the information provided to personnel about their role in protecting cardholder data.
**Defined Approach Testing Procedures:**Examine security awareness program content, evidence of reviews, and interview personnel to verify that the security awareness program is in accordance with all elements specified in this requirement.
**Customized Approach Objective:**The content of security awareness material is reviewed and updated periodically.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**The threat environment and an entity's defenses are not static. As such, the security awareness program materials must be updated as frequently as needed to ensure that the education received by personnel is up to date and represents the current threat environment.

---
**Control objectives:**12.6
**Sub-requirement:**12.6.3
**Defined Approach Requirements:**Personnel receive security awareness training as follows:
• Upon hire and at least once every 12 months.
• Multiple methods of communication are used.
• Personnel acknowledge at least once every 12 months that they have read and understood the information security policy and procedures.
**Defined Approach Testing Procedures:**
- "12.6.3.a": Examine security awareness program records to verify that personnel attend security awareness training upon hire and at least once every 12 months.
- "12.6.3.b": Examine security awareness program materials to verify the program includes methods of communicating awareness and multiple educating personnel.
- "12.6.3.c": Interview personnel to verify they have completed awareness training and are aware of their role in protecting cardholder data.
- "12.6.3.d": Examine security awareness program materials and personnel acknowledgments to verify that personnel acknowledge at least once every 12 months that they have read and understand the information security policy and procedures.
**Customized Approach Objective:**Personnel remain knowledgeable about the threat landscape, their responsibility for the operation of relevant security controls, and are able to access assistance and guidance when required.
**Guidance - Purpose:**Training of personnel ensures they receive the information about the importance of information security and that they understand their role in protecting the organization. Requiring an acknowledgment by personnel helps ensure that they have read and understood the security policies and procedures, and that they have made and will continue to make a commitment to comply with these policies.
**Guidance - Good Practice:**Entities may incorporate new-hire training as part of the Human Resources onboarding process. Training should outline the security-related 'dos' and 'don'ts.' Periodic refresher training reinforces key security processes and procedures that may be forgotten or bypassed. Entities should consider requiring security awareness training anytime personnel transfer into roles where they can impact the security of cardholder data and/or sensitive authentication data from roles where they did not have this impact. Methods and training content can vary, depending on personnel roles.
**Guidance - Examples:**Different methods that can be used to provide security awareness and education include posters, letters, web-based training, in-person training, team meetings, and incentives. Personnel acknowledgments may be recorded in writing or electronically.

---
**Control objectives:**12.6
**Sub-requirement:**12.6.3.1
**Defined Approach Requirements:**Security awareness training includes awareness of threats and vulnerabilities that could impact the security of cardholder data and/or sensitive authentication data, including but not limited to:
• Phishing and related attacks.
• Social engineering.
**Defined Approach Testing Procedures:**Examine security awareness training content to verify it includes all elements specified in this requirement.
**Customized Approach Objective:**Personnel are knowledgeable about their own human vulnerabilities and how threat actors will attempt to exploit such vulnerabilities. Personnel are able to access assistance and guidance when required.
**Applicability Notes:**See Requirement 5.4.1 for guidance on the difference between technical and automated controls to detect and protect users from phishing attacks, and this requirement for providing users security awareness training about phishing and social engineering. These are two separate and distinct requirements, and one is not met by implementing controls required by the other one. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Educating personnel on how to detect, react to, and report potential phishing and related attacks and social engineering attempts is essential to minimizing the probability of successful attacks.
**Guidance - Good Practice:**An effective security awareness program should include examples of phishing emails and periodic testing to determine the prevalence of personnel reporting such attacks. Training material an entity can consider for this topic include:
• How to identify phishing and other social engineering attacks.
• How to react to suspected phishing and social engineering.
• Where and how to report suspected phishing and social engineering activity.
An emphasis on reporting allows the organization to reward positive behavior, to optimize technical defenses (see Requirement 5.4.1), and to take immediate action to remove similar phishing emails that evaded technical defenses from recipient inboxes.

---
**Control objectives:**12.6
**Sub-requirement:**12.6.3.2
**Defined Approach Requirements:**Security awareness training includes awareness about the acceptable use of end-user technologies in accordance with Requirement 12.2.1.
**Defined Approach Testing Procedures:**Examine security awareness training content to verify it includes awareness about acceptable use of end-user technologies in accordance with Requirement 12.2.1.
**Customized Approach Objective:**Personnel are knowledgeable about their responsibility for the security and operation of end-user technologies and are able to access assistance and guidance when required.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**By including the key points of the acceptable use policy in regular training and the related context, personnel will understand their responsibilities and how these impact the security of an organization's systems.

================

### A. Tài liệu gốc của Requirement 12

### B. Summary Overview của Control Objective 12.7
Tài liệu này mô tả chi tiết **Control Objective 12.7 **của **Requirement 12 **trong **PCI-DSS v4.0.1**, tập trung vào việc sàng lọc nhân sự trước khi cấp quyền truy cập vào CDE.
Mục tiêu chính là giảm thiểu rủi ro từ nội bộ bằng cách đảm bảo nhân sự có quyền truy cập vào hệ thống và dữ liệu thẻ đã được đánh giá phù hợp trước khi tuyển dụng.
Gồm 1 sub-requirement chính:
- 12.7.1: Sàng lọc nhân sự trước khi cấp quyền truy cập CDE
Áp dụng cho các vị trí có quyền truy cập vào CDE.

### C. Key Points của Control Objective 12.7
- **Phạm vi áp dụng:** Nhân sự có quyền truy cập vào CDE
- **Trách nhiệm:** Tài liệu hóa và thực hiện quy trình screening
- **Sàng lọc:**Thực hiện trước khi tuyển dụng (pre-employment screening)
- **Tuân thủ pháp lý:**Thực hiện trong phạm vi luật địa phương
- **Đánh giá rủi ro:**Mức độ screening phù hợp với vai trò và quyền truy cập
- **Áp dụng thực tế:** Có thể áp dụng khi chuyển vai trò nội bộ

### D. Deep Summary của Control Objective 12.7
**Bối cảnh:**
Nhân sự nội bộ có quyền truy cập vào hệ thống là một trong những nguồn rủi ro lớn nếu không được kiểm soát và đánh giá trước.
**Nội dung cốt lõi:**
- Thực hiện screening nhân sự trước khi tuyển dụng cho các vị trí có truy cập CDE
- Đánh giá thông tin như lịch sử làm việc, tham chiếu, hồ sơ công khai
- Áp dụng mức độ screening phù hợp với vai trò và quyền hạn
- Tuân thủ quy định pháp luật địa phương khi thực hiện
- Có thể áp dụng lại screening khi nhân sự chuyển sang vị trí nhạy cảm hơn
**Dữ liệu đáng chú ý:**
- Áp dụng cho vị trí có truy cập CDE (không bắt buộc với vai trò rất hạn chế)
- Screening có thể bao gồm background check, reference check
**Rủi ro / Lưu ý:**
- Không screening → tăng nguy cơ insider threat
- Screening không phù hợp → bỏ sót rủi ro nhân sự
- Không tuân thủ pháp lý → vi phạm luật địa phương
- Không đánh giá theo role → áp dụng kiểm soát không hiệu quả

### E. Structured Output của Control Objective 12.7
**Control objectives:**12.7
**Sub-requirement:**12.7.1
**Defined Approach Requirements:**Potential personnel who will have access to the CDE are screened, within the constraints of local laws, prior to hire to minimize the risk of attacks from internal sources.
**Defined Approach Testing Procedures:**Interview responsible Human Resource department management to verify that screening is conducted, within the constraints of local laws, prior to hiring potential personnel who will have access to the CDE.
**Customized Approach Objective:**The risk related to allowing new members of staff access to the CDE is understood and managed.
**Applicability Notes:**For those potential personnel to be hired for positions such as store cashiers, who only have access to one card number at a time when facilitating a transaction, this requirement is a recommendation only.
**Guidance - Purpose:**Performing thorough screening prior to hiring potential personnel who are expected to be given access to the CDE provides entities with the information necessary to make informed risk decisions regarding personnel they hire that will have access to the CDE. Other benefits of screening potential personnel include helping to ensure workplace safety and confirming information provided by prospective employees on their resumes.
**Guidance - Good Practice:**Entities should consider screening for existing personnel anytime they transfer into roles where they have access to the CDE from roles where they did not have this access. To be effective, the level of screening should be appropriate for the position. For example, positions requiring greater responsibility or that have administrative access to critical data or systems may warrant more detailed or more frequent screening than positions with less responsibility and access.
**Guidance - Examples:**Screening options can include, as appropriate for the entity's region, previous employment history, review of public information/social media resources, criminal record, credit history, and reference checks.

================

### A. Tài liệu gốc của Requirement 12

### B. Summary Overview của Control Objective 12.8
Tài liệu này mô tả chi tiết **Control Objective 12.8** của **Requirement 12 **trong **PCI-DSS v4.0.1**, tập trung vào việc quản lý và kiểm soát rủi ro từ các bên thứ ba (TPSP) có liên quan đến cardholder data.
Mục tiêu chính là đảm bảo các bên thứ ba được quản lý, đánh giá và giám sát đầy đủ để không làm suy giảm mức độ bảo mật của môi trường.
Gồm 5 sub-requirement chính:
- 12.8.1: Quản lý danh sách TPSP
- 12.8.2: Thiết lập thỏa thuận với TPSP
- 12.8.3: Thực hiện due diligence trước khi hợp tác
- 12.8.4: Giám sát trạng thái tuân thủ của TPSP
- 12.8.5: Phân định trách nhiệm PCI DSS
Áp dụng cho tất cả TPSP có lưu trữ, xử lý, truyền dữ liệu thẻ hoặc ảnh hưởng đến bảo mật CDE.

### C. Key Points của Control Objective 12.8
- **Phạm vi áp dụng:**Tất cả TPSP liên quan đến cardholder data hoặc CDE
- **Trách nhiệm:** Tài liệu hóa và quản lý quan hệ với TPSP
- **Quản lý danh sách:**Duy trì inventory TPSP và dịch vụ cung cấp
- **Thỏa thuận:**Có hợp đồng ghi rõ trách nhiệm bảo mật của TPSP
- **Đánh giá trước:**Thực hiện due diligence trước khi hợp tác
- **Giám sát:**Theo dõi compliance của TPSP ít nhất hàng năm
- **Phân định trách nhiệm:**Xác định rõ trách nhiệm giữa entity và TPSP

### D. Deep Summary của Control Objective 12.8
**Bối cảnh:**
Bên thứ ba có thể mở rộng phạm vi tấn công (attack surface) và trở thành điểm yếu nếu không được kiểm soát chặt chẽ.
**Nội dung cốt lõi:**
- Duy trì danh sách đầy đủ TPSP và dịch vụ liên quan
- Thiết lập hợp đồng ghi rõ trách nhiệm bảo mật dữ liệu
- Thực hiện đánh giá (due diligence) trước khi lựa chọn TPSP
- Giám sát trạng thái tuân thủ PCI DSS của TPSP định kỳ
- Xác định rõ trách nhiệm PCI DSS giữa các bên (entity vs TPSP)
- Xem xét cả mối quan hệ TPSP lồng nhau (nested TPSP)
**Dữ liệu đáng chú ý:**
- Monitoring TPSP tối thiểu mỗi 12 tháng
- Có thể sử dụng responsibility matrix để phân định trách nhiệm
**Rủi ro / Lưu ý:**
- TPSP không kiểm soát → rò rỉ dữ liệu từ bên ngoài
- Không có hợp đồng rõ ràng → không xác định trách nhiệm
- Không đánh giá trước → chọn TPSP không an toàn
- Không giám sát → không phát hiện TPSP mất compliance
- Trách nhiệm không rõ → bỏ sót kiểm soát PCI DSS

### E. Structured Output của Control Objective 12.8
**Control objectives:**12.8
**Sub-requirement:**12.8.1
**Defined Approach Requirements:**A list of all third-party service providers (TPSPs) with which account data is shared or that could affect the security of account data is maintained, including a description for each of the services provided.
**Defined Approach Testing Procedures:**
- "12.8.1.a": Examine policies and procedures to verify that processes are defined to maintain a list of TPSPs, including a description for each of the services provided, for all TPSPs with whom account data is shared or that could affect the security of account data.
- "12.8.1.b": Examine documentation to verify that a list of all TPSPs is maintained that includes a description of the services provided.
**Customized Approach Objective:**Records are maintained of TPSPs and the services provided.
**Applicability Notes:**The use of a PCI DSS compliant TPSP does not make an entity PCI DSS compliant, nor does it remove the entity's responsibility for its own PCI DSS compliance.
**Guidance - Purpose:**Maintaining a list of all TPSPs identifies where potential risk extends outside the organization and defines the organization's extended attack surface.
**Guidance - Examples:**Different types of TPSPs include those that:
• Store, process, or transmit account data on the entity's behalf (such as payment gateways, payment processors, payment service providers (PSPs), and off-site storage providers).
• Manage system components included in the entity's PCI DSS assessment (such as providers of network security control services, anti-malware services, and security incident and event management (SIEM); contact and call centers; web-hosting companies; and IaaS, PaaS, SaaS, and FaaS cloud providers).
• Could impact the security of the entity's cardholder data and/or sensitive authentication data (such as vendors providing support via remote access, and bespoke software developers).

---
**Control objectives:**12.8
**Sub-requirement:**12.8.2
**Defined Approach Requirements:**Written agreements with TPSPs are maintained as follows:
• Written agreements are maintained with all TPSPs with which account data is shared or that could affect the security of the CDE.
• Written agreements include acknowledgments from TPSPs that TPSPs are responsible for the security of account data the TPSPs possess or otherwise store, process, or transmit on behalf of the entity, or to the extent that the TPSP could impact the security of the entity's cardholder data and/or sensitive authentication data.
**Defined Approach Testing Procedures:**
- "12.8.2.a": Examine policies and procedures to verify that processes are defined to maintain written agreements with all TPSPs in accordance with all elements specified in this requirement.
- "12.8.2.b": Examine written agreements with TPSPs to verify they are maintained in accordance with all elements as specified in this requirement.
**Customized Approach Objective:**Records are maintained of each TPSP's acknowledgment of its responsibility to protect account data.
**Applicability Notes:**The exact wording of an agreement will depend on the details of the service being provided, and the responsibilities assigned to each party. The agreement does not have to include the exact wording provided in this requirement. The TPSP's written acknowledgment is a confirmation that states the TPSP is responsible for the security of the account data it may store, process, or transmit on behalf of the customer or to the extent the TPSP may impact the security of a customer's cardholder data and/or sensitive authentication data. Evidence that a TPSP is meeting PCI DSS requirements (is not the same as a written acknowledgment specified in this requirement. For example, a PCI DSS Attestation of Compliance (AOC), a declaration on a company's website, a policy statement, a responsibility matrix, or other evidence not included in a written agreement is not a written acknowledgment.
**Guidance - Purpose:**The written acknowledgment from a TPSP demonstrates its commitment to maintaining proper security of account data that it obtains from its customers and that the TPSP is fully aware of the assets that could be affected during the provisioning of the TPSP's service. The extent to which a specific TPSP is responsible for the security of account data will depend on the service provided and the responsibilities agreed between the provider and assessed entity (the customer). In conjunction with Requirement 12.9.1, this requirement is intended to promote a consistent level of understanding between parties about their applicable PCI DSS responsibilities. For example, the agreement may include the applicable PCI DSS requirements to be maintained as part of the provided service.
**Guidance - Good Practice:**The entity may also want to consider including in their written agreement with a TPSP that the TPSP will support the entity's request for information per Requirement 12.9.2. Entities will also want to understand whether any TPSPs have 'nested' relationships with other TPSPs, meaning the primary TPSP contracts with another TPSP(s) for the purposes of providing a service. It is important to understand whether the primary TPSP is relying on the secondary TPSP(s) to achieve overall compliance of a service, and what types of written agreements the primary TPSP has in place with the secondary TPSPs. Entities can consider including coverage in their written agreement for any 'nested' TPSPs a primary TPSP may use.
**Guidance - Further Information:**Refer to the Information Supplement: Third-Party Security Assurance for further guidance.

---
**Control objectives:**12.8
**Sub-requirement:**12.8.3
**Defined Approach Requirements:**An established process is implemented for engaging TPSPs, including proper due diligence prior to engagement.
**Defined Approach Testing Procedures:**
- "12.8.3.a": Examine policies and procedures to verify that processes are defined for engaging TPSPs, including proper due diligence prior to engagement.
- "12.8.3.b": Examine evidence and interview responsible personnel to verify the process for engaging TPSPs includes proper due diligence prior to engagement.
**Customized Approach Objective:**The capability, intent, and resources of a prospective TPSP to adequately protect account data are assessed before the TPSP is engaged.
**Guidance - Purpose:**A thorough process for engaging TPSPs, including details for selection and vetting prior to engagement, helps ensure that a TPSP is thoroughly vetted internally by an entity prior to establishing a formal relationship and that the risk to cardholder data associated with the engagement of the TPSP is understood.
**Guidance - Good Practice:**Specific due-diligence processes and goals will vary for each organization. Elements that should be considered include the provider's reporting practices, breach-notification and incident response procedures, details of how PCI DSS responsibilities are assigned between each party, how the TPSP validates their PCI DSS compliance and what evidence they provide.

---
**Control objectives:**12.8
**Sub-requirement:**12.8.4
**Defined Approach Requirements:**A program is implemented to monitor TPSPs' PCI DSS compliance status at least once every 12 months.
**Defined Approach Testing Procedures:**
- "12.8.4.a": Examine policies and procedures to verify that processes are defined to monitor TPSPs' PCI DSS compliance status at least once every 12 months.
- "12.8.4.b": Examine documentation and interview responsible personnel to verify that the PCI DSS compliance status of each TPSP is monitored at least once every 12 months.
**Customized Approach Objective:**The PCI DSS compliance status of TPSPs is verified periodically.
**Applicability Notes:**Where an entity has an agreement with a TPSP for meeting PCI DSS requirements on behalf of the entity (for example, via a firewall service), the entity must work with the TPSP to make sure the applicable PCI DSS requirements are met. If the TPSP does not meet those applicable PCI DSS requirements, then those requirements are also 'not in place' for the entity.
**Guidance - Purpose:**Knowing the PCI DSS compliance status of all engaged TPSPs provides assurance and awareness about whether they comply with the requirements applicable to the services they offer to the organization.
**Guidance - Good Practice:**If the TPSP offers a variety of services, the compliance status the entity monitors should be specific to those services delivered to the entity and those services in scope for the entity's PCI DSS assessment. If a TPSP has a PCI DSS Attestation of Compliance (AOC), the expectation is that the TPSP should provide that to customers upon request to demonstrate their PCI DSS compliance status. If the TPSP did not undergo a PCI DSS assessment, it may be able to provide other sufficient evidence to demonstrate that it has met the applicable requirements without undergoing a formal compliance validation. For example, the TPSP can provide specific evidence to the entity's assessor so the assessor can confirm applicable requirements are met. Alternatively, the TPSP can elect to undergo multiple on-demand assessments by each of its customers' assessors, with each assessment targeted to confirm that applicable requirements are met.
**Guidance - Further Information:**For more information about third-party service providers, refer to:
• PCI DSS section: Use of Third-Party Service Providers.
• Information Supplement: Third-Party Security Assurance .

---
**Control objectives:**12.8
**Sub-requirement:**12.8.5
**Defined Approach Requirements:**Information is maintained about which PCI DSS requirements are managed by each TPSP, which are managed by the entity, and any that are shared between the TPSP and the entity. 12.9 Third-party service providers (TPSPs) support their customers' PCI DSS compliance.
**Defined Approach Testing Procedures:**
- "12.8.5.a": Examine policies and procedures to verify that processes are defined to maintain information about which PCI DSS requirements are managed by each TPSP, which are managed by the entity, and any that are shared between both the TPSP and the entity.
- "12.8.5.b": Examine documentation and interview personnel to verify the entity maintains information about which PCI DSS requirements are managed by each TPSP, which are managed by the entity, and any that are shared between both entities. 12.9 Third-party service providers (TPSPs) support their customers' PCI DSS compliance.
**Customized Approach Objective:**Records detailing the PCI DSS requirements and related system components for which each TPSP is solely or jointly responsible, are maintained and reviewed periodically.
**Guidance - Purpose:**It is important that the entity understands which PCI DSS requirements and sub-requirements its TPSPs have agreed to meet, which requirements are shared between the TPSP and the entity, and for those that are shared, specifics about how the requirements are shared and which entity is responsible for meeting each sub-requirement. Without this shared understanding, it is inevitable that the entity and the TPSP will assume a given PCI DSS sub-requirement is the responsibility of the other party, and therefore that sub- requirement may not be addressed at all. The specific information an entity maintains will depend on the particular agreement with their providers, the type of service, etc. TPSPs may define their PCI DSS responsibilities to be the same for all their customers; otherwise, this responsibility should be agreed upon by both the entity and TPSP.
**Guidance - Good Practice:**Entities can document these responsibilities via a matrix that identifies all applicable PCI DSS requirements and indicates for each requirement whether the entity or TPSP is responsible for meeting that requirement or whether it is a shared responsibility. This type of document is often referred to as a responsibility matrix. It is also important for entities to understand whether any TPSPs have "nested" relationships with other TPSPs, meaning the primary TPSP contracts with another TPSP(s) for the purposes of providing a service. It is important to understand whether the primary TPSP is relying on the secondary TPSP(s) to achieve overall compliance of a service, and how the primary TPSP is monitoring performance of the service and the PCI DSS compliance status of the secondary TPSP(s). Note that it is the responsibility of the primary TPSP to manage and monitor any secondary TPSPs.
**Guidance - Further Information:**Refer to Information Supplement: Third-Party Security Assurance for a sample responsibility matrix template.

================

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

================

### A. Tài liệu gốc của Requirement 12

### B. Summary Overview của Control Objective 12.10
Tài liệu này mô tả chi tiết **Control Objective 12.10** của **Requirement 12** trong **PCI-DSS v4.0.1**, tập trung vào việc thiết lập, duy trì và vận hành quy trình ứng phó sự cố bảo mật.
Mục tiêu chính là đảm bảo các sự cố bảo mật được phát hiện, xử lý kịp thời và có quy trình rõ ràng nhằm giảm thiểu tác động đến hệ thống và cardholder data.
Gồm 6 sub-requirement chính:
- 12.10.1: Thiết lập incident response plan
- 12.10.2: Review và test kế hoạch
- 12.10.3: Đảm bảo nhân sự 24/7
- 12.10.4: Đào tạo nhân sự ứng phó sự cố
- 12.10.5: Xử lý alert từ hệ thống giám sát
- 12.10.6: Cập nhật kế hoạch theo bài học
- 12.10.7: Xử lý PAN ngoài phạm vi
Áp dụng cho toàn bộ hệ thống, nhân sự và quy trình liên quan đến ứng phó sự cố trong môi trường.

### C. Key Points của Control Objective 12.10
- **Phạm vi áp dụng:**Toàn bộ hệ thống, CDE và hoạt động security monitoring
- **Trách nhiệm:** Tài liệu hóa và vận hành incident response plan
- **Ứng phó sự cố:**Có quy trình rõ ràng (containment, mitigation, recovery)
- **Sẵn sàng:**Có nhân sự trực 24/7 để xử lý sự cố
- **Đào tạo:**Nhân sự phải được đào tạo định kỳ
- **Giám sát:**Xử lý alert từ IDS/IPS, FIM, network control…
- **Cập nhật:** Kế hoạch phải được review, test và cải tiến liên tục

### D. Deep Summary của Control Objective 12.10
**Bối cảnh:**
Không có quy trình ứng phó sự cố rõ ràng sẽ dẫn đến xử lý chậm, gây thiệt hại lớn về tài chính, uy tín và pháp lý.
**Nội dung cốt lõi:**
- Xây dựng incident response plan đầy đủ (role, communication, recovery…)
- Review và test kế hoạch ít nhất hàng năm
- Đảm bảo nhân sự sẵn sàng 24/7
- Đào tạo nhân sự về quy trình và kỹ năng xử lý sự cố
- Xử lý alert từ các hệ thống giám sát bảo mật
- Cập nhật kế hoạch dựa trên bài học và threat mới
- Có quy trình riêng khi phát hiện PAN ngoài phạm vi
**Dữ liệu đáng chú ý:**
- Incident response plan phải bao gồm cả legal, communication và backup
- Training và test phải thực hiện định kỳ
- Bao phủ alert từ nhiều nguồn (IDS/IPS, FIM, wireless…)
**Rủi ro / Lưu ý:**
- Không có plan → xử lý sự cố rối loạn
- Không test → plan không khả thi
- Không có 24/7 response → chậm phản ứng
- Không xử lý alert → bỏ lỡ tấn công
- Không cập nhật → không đáp ứng threat mới
- Không xử lý PAN ngoài scope → rò rỉ dữ liệu không kiểm soát

### E. Structured Output của Control Objective 12.10
**Control objectives:**12.10
**Sub-requirement:**12.10.1
**Defined Approach Requirements:**An incident response plan exists and is ready to be activated in the event of a suspected or confirmed security incident. The plan includes, but is not limited to:
• Roles, responsibilities, and communication and contact strategies in the event of a suspected or confirmed security incident, including notification of payment brands and acquirers, at a minimum.
• Incident response procedures with specific containment and mitigation activities for different types of incidents.
• Business recovery and continuity procedures.
• Data backup processes.
• Analysis of legal requirements for reporting compromises.
• Coverage and responses of all critical system components.
• Reference or inclusion of incident response procedures from the payment brands.
**Defined Approach Testing Procedures:**
- "12.10.1.a": Examine the incident response plan to verify that the plan exists and includes at least the elements specified in this requirement.
- "12.10.1.b": Interview personnel and examine documentation from previously reported incidents or alerts to verify that the documented incident response plan and procedures were followed.
**Customized Approach Objective:**A comprehensive incident response plan that meets card brand expectations is maintained.
**Guidance - Purpose:**Without a comprehensive incident response plan that is properly disseminated, read, and understood by the parties responsible, confusion and lack of a unified response could create further downtime for the business, unnecessary public media exposure, as well as risk of financial and/or reputational loss and legal liabilities.
**Guidance - Good Practice:**The incident response plan should be thorough and contain all the key elements for stakeholders (for example, legal, communications) to allow the entity to respond effectively in the event of a breach that could impact account data. It is important to keep the plan up to date with current contact information of all individuals designated as having a role in incident response. Other relevant parties for notifications may include customers, financial institutions (acquirers and issuers), and business partners. Entities should consider how to address all compromises of data within the CDE in their incident response plans, including compromises to account data, wireless encryption keys, encryption keys used for transmission and storage or account data or cardholder data, etc.
**Guidance - Examples:**Legal requirements for reporting compromises include those in most US states, the EU General Data Protection Regulation (GDPR), and the Personal Data Protection Act (Singapore).
**Guidance - Further Information:**For more information, refer to the NIST SP 800- 61 Rev. 2, Computer Security Incident Handling Guide .

---
**Control objectives:**12.10
**Sub-requirement:**12.10.2
**Defined Approach Requirements:**At least once every 12 months, the security incident response plan is:
• Reviewed and the content is updated as needed.
• Tested, including all elements listed in Requirement 12.10.1.
**Defined Approach Testing Procedures:**Interview personnel and review documentation to verify that, at least once every 12 months, the security incident response plan is:
• Reviewed and updated as needed.
• Tested, including all elements listed in Requirement 12.10.1.
**Customized Approach Objective:**The incident response plan is kept current and tested periodically.
**Guidance - Purpose:**Proper testing of the security incident response plan can identify broken business processes and ensure key steps are not missed, which could result in increased exposure during an incident. Periodic testing of the plan ensures that the processes remain viable, as well as ensuring that all relevant personnel in the organization are familiar with the plan.
**Guidance - Good Practice:**The test of the incident response plan can include simulated incidents and the corresponding responses in the form of a 'table-top exercise' that includes participation by relevant personnel. A review of the incident and the quality of the response can provide entities with the assurance that all required elements are included in the plan.

---
**Control objectives:**12.10
**Sub-requirement:**12.10.3
**Defined Approach Requirements:**Specific personnel are designated to be available on a 24/7 basis to respond to suspected or confirmed security incidents.
**Defined Approach Testing Procedures:**Examine documentation and interview responsible personnel occupying designated roles to verify that specific personnel are designated to be available on a 24/7 basis to respond to security incidents.
**Customized Approach Objective:**Incidents are responded to immediately where appropriate.
**Guidance - Purpose:**An incident could occur at any time, therefore if a person who is trained in incident response and familiar with the entity's plan is available when an incident is detected, the entity's ability to correctly respond to the incident is increased.
**Guidance - Good Practice:**Often, specific personnel are designated to be part of a security incident response team, with the team having overall responsibility for responding to incidents (perhaps on a rotating schedule basis) and managing those incidents in accordance with the plan. The incident response team can consist of core members who are permanently assigned or 'on-demand' personnel who may be called up as necessary, depending on their expertise and the specifics of the incident. Having available resources to respond quickly to incidents minimizes disruption to the organization. Examples** **of types of activity the team or individuals should respond to include any evidence of unauthorized activity, detection of unauthorized wireless access points, critical IDS alerts, and reports of unauthorized critical system or content file changes.

---
**Control objectives:**12.10
**Sub-requirement:**12.10.4
**Defined Approach Requirements:**Personnel responsible for responding to suspected and confirmed security incidents are appropriately and periodically trained on their incident response responsibilities.
**Defined Approach Testing Procedures:** Examine training documentation and interview incident response personnel to verify that personnel are appropriately and periodically trained on their incident response responsibilities.
**Customized Approach Objective:**Personnel are knowledgeable about their role and responsibilities in incident response and are able to access assistance and guidance when required.
**Guidance - Purpose:**Without a trained and readily available incident response team, extended damage to the network could occur, and critical data and systems may become 'polluted' by inappropriate handling of the targeted systems. This can hinder the success of a post-incident investigation.
**Guidance - Good Practice:**It is important that all personnel involved in incident response are trained and knowledgeable about managing evidence for forensics and investigations.

---
**Control objectives:**12.10
**Sub-requirement:**12.10.4.1
**Defined Approach Requirements:**The frequency of periodic training for incident response personnel is defined in the entity's targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1.
**Defined Approach Testing Procedures:**
- "12.10.4.1.a": Examine the entity's targeted risk analysis for the frequency of training for incident response personnel to verify the risk analysis was performed in accordance with all elements specified in Requirement 12.3.1.
- "12.10.4.1.b": Examine documented results of periodic training of incident response personnel and interview personnel to verify training is performed at the frequency defined in the entity's targeted risk analysis performed for this requirement.
**Customized Approach Objective:**Incident response personnel are trained at a frequency that addresses the entity's risk.
**Applicability Notes:** This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Each entity's environment and incident response plan are different, and the approach will depend on a number of factors, including the size and complexity of the entity, the degree of change in the environment, the size of the incident response team, and the turnover in personnel. Performing a risk analysis will allow the entity to determine the optimum frequency for training personnel with incident response responsibilities.

---
**Control objectives:**12.10
**Sub-requirement:**12.10.5
**Defined Approach Requirements:**The security incident response plan includes monitoring and responding to alerts from security monitoring systems, including but not limited to:
• Intrusion-detection and intrusion-prevention systems.
• Network security controls.
• Change-detection mechanisms for critical files.
• The change-and tamper-detection mechanism for payment pages. This bullet is a best practice until its effective date; refer to Applicability Notes below for details.
• Detection of unauthorized wireless access points.
**Defined Approach Testing Procedures:**Examine documentation and observe incident response processes to verify that monitoring and responding to alerts from security monitoring systems are covered in the security incident response plan, including but not limited to the systems specified in this requirement.
**Customized Approach Objective:**Alerts generated by monitoring and detection technologies are responded to in a structured, repeatable manner.
**Applicability Notes:**The bullet above (for monitoring and responding to alerts from a change- and tamper-detection mechanism for payment pages) is a best practice until 31 March 2025, after which it will be required as part of Requirement 12.10.5 and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Responding to alerts generated by security monitoring systems that are explicitly designed to focus on potential risk to data is critical to prevent a breach and therefore, this must be included in the incident-response processes.

---
**Control objectives:**12.10
**Sub-requirement:**12.10.6
**Defined Approach Requirements:**The security incident response plan is modified and evolved according to lessons learned and to incorporate industry developments.
**Defined Approach Testing Procedures:**
- "12.10.6.a": Examine policies and procedures to verify that processes are defined to modify and evolve the security incident response plan according to lessons learned and to incorporate industry developments.
- "12.10.6.b": Examine the security incident response plan and interview responsible personnel to verify that the incident response plan is modified and evolved according to lessons learned and to incorporate industry developments.
**Customized Approach Objective:**The effectiveness and accuracy of the incident response plan is reviewed and updated after each invocation.
**Guidance - Purpose:**Incorporating lessons learned into the incident response plan after an incident occurs and in-step with industry developments, helps keep the plan current and able to react to emerging threats and security trends.
**Guidance - Good Practice:**The lessons-learned exercise should include all levels of personnel. Although it is often included as part of the review of the entire incident, it should focus on how the entity's response to the incident could be improved. It is important to not just consider elements of the response that did not have the planned outcomes but also to understand what worked well and whether lessons from those elements that worked well can be applied to areas of the plan that did not. Another way to optimize an entity's incident response plan is to understand the attacks made against other organizations and use that information to fine-tune the entity's detection, containment, mitigation, or recovery procedures.

---
**Control objectives:**12.10
**Sub-requirement:**12.10.7
**Defined Approach Requirements:**Incident response procedures are in place, to be initiated upon the detection of stored PAN anywhere it is not expected, and include:
• Determining what to do if PAN is discovered outside the CDE, including its retrieval, secure deletion, and/or migration into the currently defined CDE, as applicable.
• Identifying whether sensitive authentication data is stored with PAN.
• Determining where the account data came from and how it ended up where it was not expected.
• Remediating data leaks or process gaps that resulted in the account data being where it was not expected.
**Defined Approach Testing Procedures:**
- "12.10.7.a": Examine documented incident response procedures to verify that procedures for responding to the detection of stored PAN anywhere it is not expected to exist, ready to be initiated, and include all elements specified in this requirement.
- "12.10.7.b": Interview personnel and examine records of response actions to verify that incident response procedures are performed upon detection of stored PAN anywhere it is not expected.
**Customized Approach Objective:**Processes are in place to quickly respond, analyze, and address situations in the event that cleartext PAN is detected where it is not expected.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Having documented incident response procedures that are followed in the event that stored PAN is found anywhere it is not expected to be, helps to identify the necessary remediation actions and prevent future leaks.
**Guidance - Good Practice:**If PAN was found outside the CDE, analysis should be performed to 1) determine whether it was saved independently of other data or with sensitive authentication data, 2) identify the source of the data, and 3) identify the control gaps that resulted in the data being outside the CDE. Entities should consider whether there are contributory factors, such as business processes, user behavior, improper system configurations, etc. that caused the PAN to be stored in an unexpected location. If such contributory factors are present, they should be addressed per this Requirement to prevent recurrence.