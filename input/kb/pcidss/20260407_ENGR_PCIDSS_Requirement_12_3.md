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