### A. Tài liệu gốc của Requirement 6

### B. Summary Overview của Control Objective 6.3
Tài liệu này mô tả chi tiết **Control Objective 6.3** của **Requirement 6** trong **PCI-DSS v4.0.1**, tập trung vào việc xác định, đánh giá và xử lý các lỗ hổng bảo mật trên hệ thống và phần mềm.
Mục tiêu chính là đảm bảo các lỗ hổng bảo mật được phát hiện kịp thời, đánh giá mức độ rủi ro và được khắc phục thông qua quản lý bản vá và kiểm soát liên quan.
Gồm 3 sub-requirement chính:
- 6.3.1: Xác định và đánh giá lỗ hổng
- 6.3.2: Quản lý inventory phần mềm
- 6.3.3: Cập nhật bản vá bảo mật
Áp dụng cho toàn bộ hệ thống, phần mềm nội bộ và phần mềm bên thứ ba trong môi trường.

### C. Key Points của Control Objective 6.3
- **Phạm vi áp dụng:**Tất cả system components và phần mềm (internal + third-party)
- **Trách nhiệm:**Tài liệu hóa quy trình quản lý lỗ hổng và đảm bảo thực thi
- **Quản lý lỗ hổng:**Theo dõi nguồn tin cậy (CERT, vendor, NVD…)
- **Đánh giá rủi ro:**Phân loại mức độ (critical, high…) để ưu tiên xử lý
- **Quản lý inventory:**Duy trì danh sách phần mềm và thành phần liên quan
- **Quản lý bản vá:**Cài patch cho lỗ hổng critical trong ≤ 1 tháng

### D. Deep Summary của Control Objective 6.3
**Bối cảnh:**
Các lỗ hổng bảo mật liên tục được phát hiện và công bố. Nếu không theo dõi và xử lý kịp thời, hệ thống có thể bị khai thác dễ dàng.
**Nội dung cốt lõi:**
- Theo dõi liên tục các nguồn thông tin về lỗ hổng bảo mật
- Đánh giá và phân loại rủi ro để ưu tiên xử lý
- Duy trì inventory phần mềm và các thành phần liên quan
- Cập nhật bản vá bảo mật theo mức độ rủi ro
- Tích hợp với các quy trình khác (risk, patch, incident…)
**Dữ liệu đáng chú ý:**
- Patch cho lỗ hổng critical phải triển khai trong vòng 1 tháng
- Có thể sử dụng CVSS, CERT, vendor advisory để đánh giá rủi ro
**Rủi ro / Lưu ý:**
- Không theo dõi vulnerability → bỏ sót lỗ hổng mới
- Không đánh giá đúng rủi ro → xử lý không ưu tiên đúng
- Không quản lý inventory → không biết hệ thống bị ảnh hưởng
- Chậm patch → dễ bị khai thác bởi attacker

### E. Structured Output của Control Objective 6.3
**Control objectives:**6.3
**Sub-requirement:**6.3.1
**Defined Approach Requirements:**Security vulnerabilities are identified and managed as follows:
• New security vulnerabilities are identified using industry-recognized sources for security vulnerability information, including alerts from international and national computer emergency response teams (CERTs).
• Vulnerabilities are assigned a risk ranking based on industry best practices and consideration of potential impact.
• Risk rankings identify, at a minimum, all vulnerabilities considered to be a high-risk or critical to the environment.
• Vulnerabilities for bespoke and custom, and third-party software (for example operating systems and databases) are covered.
**Defined Approach Testing Procedures:**
- "6.3.1.a": Examine policies and procedures for identifying and managing security vulnerabilities to verify that processes are defined in accordance with all elements specified in this requirement.
- "6.3.1.b": Interview responsible personnel, examine documentation, and observe processes to verify that security vulnerabilities are identified and managed in accordance with all elements specified in this requirement.
**Customized Approach Objective:**New system and software vulnerabilities that may impact the security of cardholder data and/or sensitive authentication data are monitored, cataloged, and risk assessed.
**Applicability Notes:**This requirement is not achieved by, and is in addition to, performing vulnerability scans according to Requirements 11.3.1 and 11.3.2. This requirement is for a process to actively monitor industry sources for vulnerability information and for the entity to determine the risk ranking to be associated with each vulnerability.
**Guidance - Purpose:**Classifying the risks (for example, as critical, high, medium, or low) allows organizations to identify, prioritize, and address the highest risk items more quickly and reduce the likelihood that vulnerabilities posing the greatest risk will be exploited.
**Guidance - Good Practice:**Methods for evaluating vulnerabilities and assigning risk ratings will vary based on an organization's environment and risk-assessment strategy. When an entity is assigning its risk rankings, it should consider using a formal, objective, justifiable methodology that accurately portrays the risks of the vulnerabilities pertinent to the organization and translates to an appropriate entity-assigned priority for resolution. Risk rankings should, at a minimum, identify all vulnerabilities considered to be a 'high risk' to the environment. In addition to the risk ranking, vulnerabilities may be considered 'critical' if they pose an imminent threat to the environment, impact critical systems, and/or would result in a potential compromise if not addressed. Examples of critical systems may include security systems, public-facing devices and systems, databases, and other systems that store, process, or transmit cardholder data.
An organization's processes for managing vulnerabilities should be integrated with other management processes-for example, risk management, change management, patch management, incident response, application security, as well as proper monitoring and logging of these processes. This process should include multiple sources of vulnerability information, including industry-recognized vulnerability databases (for example, the US National Vulnerability Database), CERTs, RSS feeds, information received from vendors and third parties, and vulnerabilities identified via internal and external vulnerability scans (Requirements 11.3.1 and 11.3.2). This will help to ensure all vulnerabilities are properly identified and addressed. Processes should support ongoing evaluation of vulnerabilities. For example, a vulnerability initially identified as low risk could become a higher risk later. Additionally, vulnerabilities individually considered to be low or medium risk, could collectively pose a high or critical risk if present on the same system, or if exploited on a low-risk system that could result in access to the CDE.
**Guidance - Examples:**Some organizations that issue alerts to advise entities about urgent vulnerabilities requiring immediate patches/updates are national Computer Emergency Readiness/Response Teams (CERTs) and vendors. Criteria for ranking vulnerabilities may include criticality of a vulnerability identified in an alert from Forum of Incident Response and Security Teams (FIRST) or a CERT, consideration of the CVSS score, the classification by the vendor, and/or type of systems affected.
**Guidance - Further Information:**Trustworthy sources for vulnerability information include vendor websites, industry newsgroups, mailing lists, etc. If software is developed in-house, the internal development team should also consider sources of information about new vulnerabilities that may affect internally developed applications. Other methods to ensure new vulnerabilities are identified include solutions that automatically recognize and alert upon detection of unusual behavior. Processes should account for widely published exploits as well as 'zero-day' attacks, which target previously unknown vulnerabilities. For bespoke and custom software, the organization may obtain information about libraries, frameworks, compilers, programming languages, etc. from public trusted sources (for example, special resources and resources from component developers). The organization may also independently analyze third- party components and identify vulnerabilities.
For control over in-house developed software, the organization may receive such information from external sources. The organization can consider using a "bug bounty" program where it posts information (for example, on its website) so third parties can contact the organization with vulnerability information. External sources may include independent investigators or companies that report to the organization about identified vulnerabilities and may include sources such as the Common Vulnerability Scoring System (CVSS) or the OWASP Risk Rating Methodology.

---
**Control objectives:**6.3
**Sub-requirement:**6.3.2
**Defined Approach Requirements:**An inventory of bespoke and custom software, and third-party software components incorporated into bespoke and custom software is maintained to facilitate vulnerability and patch management.
**Defined Approach Testing Procedures:**
- "6.3.2.a": Examine documentation and interview personnel to verify that an inventory of bespoke and custom software and third-party software components incorporated into bespoke and custom software is maintained, and that the inventory is used to identify and address vulnerabilities.
- "6.3.2.b": Examine software documentation, including for bespoke and custom software that integrates third-party software components, and compare it the inventory to verify that the inventory includes the bespoke and custom software and third-party software components.
**Customized Approach Objective:**Known vulnerabilities in third-party software components cannot be exploited in bespoke and custom software.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Identifying and listing all the entity's bespoke and custom software, and any third-party software that is incorporated into the entity's bespoke and custom software enables the entity to manage vulnerabilities and patches. Vulnerabilities in third-party components (including libraries, APIs, etc.) embedded in an entity's software also renders those applications vulnerable to attacks. Knowing which third-party components are used in the entity's software and monitoring the availability of security patches to address known vulnerabilities is critical to ensuring the security of the software.
**Guidance - Good Practice:**An entity's inventory should cover all payment software components and dependencies, including supported execution platforms or environments, third- party libraries, services, and other required functionalities. There are many different types of solutions that can help with managing software inventories, such as software composition analysis tools, application discovery tools, and mobile device management.

---
**Control objectives:**6.3
**Sub-requirement:**6.3.3
**Defined Approach Requirements:**All system components are protected from known vulnerabilities by installing applicable security patches/updates as follows:
• Patches/updates for critical vulnerabilities (identified according to the risk ranking process at Requirement 6.3.1) are installed within one month of release.
• All other applicable security patches/updates are installed within an appropriate time frame as determined by the entity's assessment of the criticality of the risk to the environment as identified according to the risk ranking process at Requirement 6.3.1.
**Defined Approach Testing Procedures:**
- "6.3.3.a": Examine policies and procedures to verify processes are defined for addressing vulnerabilities by installing applicable security patches/updates in accordance with all elements specified in this requirement.
- "6.3.3.b": Examine system components and related software and compare the list of installed security patches/updates to the most recent security patch/update information to verify vulnerabilities are addressed in accordance with all elements specified in this requirement. 6.4 Public-facing web applications are protected against attacks.
**Customized Approach Objective:**System components cannot be compromised via the exploitation of a known vulnerability.
**Guidance - Purpose:**New exploits are constantly being discovered, and these can permit attacks against systems that have previously been considered secure. If the most recent security patches/updates are not implemented on critical systems as soon as possible, a malicious actor can use these exploits to attack or disable a system or gain access to sensitive data.
**Guidance - Good Practice:**Prioritizing security patches/updates for critical infrastructure ensures that high-priority systems and devices are protected from vulnerabilities as soon as possible after a patch is released. An entity's patching cadence should factor in any re- evaluation of vulnerabilities and subsequent changes in the criticality of a vulnerability per Requirement 6.3.1. For example, a vulnerability initially identified as low risk could become a higher risk later. Additionally, vulnerabilities individually considered to be low or medium risk could collectively pose a high or critical risk if present on the same system, or if exploited on a low-risk system that could result in access to the CDE.
It is recommended that the entity complete a targeted risk analysis (TRA) according to PCI DSS Requirement 12.3.1 to document the frequency of installing all other applicable security patches/updates. This TRA would include consideration of the entity's assessment of the criticality of the risk to their environment as identified in the risk ranking process at Requirement 6.3.1.
**Guidance - Examples:**An example time frame for installation of patches/updates could be 60 days for high-risk vulnerabilities and 90 days for others, as determined by the entity's assessment of risk. 6.4 Public-facing web applications are protected against attacks.