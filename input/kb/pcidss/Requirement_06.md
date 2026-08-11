### A. Tài liệu gốc của Requirement 6

### B. Summary Overview của Control Objective 6.1
Tài liệu này mô tả chi tiết **Control Objective 6.1 **của **Requirement 6** trong **PCI-DSS v4.0.1**, tập trung vào việc thiết lập và duy trì chính sách, quy trình và phân công trách nhiệm liên quan đến phát triển và bảo trì hệ thống an toàn.
Mục tiêu chính là đảm bảo các chính sách, quy trình và vai trò trách nhiệm được tài liệu hóa, cập nhật, áp dụng thực tế và được hiểu rõ bởi các bên liên quan trong hoạt động phát triển và bảo trì hệ thống.
Gồm 2 sub-requirement chính:
- 6.1.1: Quản lý chính sách và quy trình
- 6.1.2: Phân công vai trò và trách nhiệm
Áp dụng cho toàn bộ tổ chức và nhân sự tham gia vào các hoạt động thuộc Requirement 6.

### C. Key Points của Control Objective 6.1
- **Phạm vi áp dụng:**Tất cả chính sách, quy trình và nhân sự liên quan Requirement 6
- **Trách nhiệm:**Phân rõ vai trò, đảm bảo nhân sự hiểu và thực hiện đúng
- **Quản lý tài liệu:**Chính sách và quy trình phải được tài liệu hóa, cập nhật và phổ biến
- **Áp dụng thực tế:**Quy trình phải được triển khai và sử dụng thực tế
- **Truyền thông:**Đảm bảo các bên liên quan được phổ biến và hiểu nội dung

### D. Deep Summary của Control Objective 6.1
**Bối cảnh:**
Nếu chính sách và trách nhiệm không rõ ràng, các hoạt động phát triển và bảo trì hệ thống có thể không được thực hiện an toàn, dẫn đến lỗ hổng bảo mật.
**Nội dung cốt lõi:**
- Tài liệu hóa chính sách và quy trình liên quan đến phát triển và bảo trì hệ thống
- Cập nhật kịp thời khi có thay đổi về công nghệ hoặc quy trình
- Đảm bảo quy trình được áp dụng thực tế trong vận hành
- Phổ biến đến tất cả nhân sự liên quan
- Phân rõ vai trò và trách nhiệm cho từng hoạt động
**Dữ liệu đáng chú ý:**
- Chính sách và quy trình phải "in use" và "known to all affected parties"
- Có thể sử dụng RACI matrix để quản lý trách nhiệm
**Rủi ro / Lưu ý:**
- Chính sách không cập nhật → không phản ánh thực tế hệ thống
- Quy trình không được thực thi → tạo lỗ hổng bảo mật
- Nhân sự không rõ trách nhiệm → bỏ sót kiểm soát
- Thiếu phân công rõ ràng → không có accountability

### E. Structured Output của Control Objective 6.1
**Control objectives:**6.1
**Sub-requirement:**6.1.1
**Defined Approach Requirements:**All security policies and operational procedures that are identified in Requirement 6 are:
• Documented.
• Kept up to date.
• In use.
• Known to all affected parties.
**Defined Approach Testing Procedures:**Examine documentation and interview personnel to verify that security policies and operational procedures identified in Requirement are managed in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Expectations, controls, and oversight for meeting activities within Requirement 6 are defined and adhered to by affected personnel. All supporting activities are repeatable, consistently applied, and conform to management's intent.
**Guidance - Purpose:**Requirement 6.1.1 is about effectively managing and maintaining the various policies and procedures specified throughout Requirement 6. While it is important to define the specific policies or procedures called out in Requirement 6, it is equally important to ensure they are properly documented, maintained, and disseminated.
**Guidance - Good Practice:**It is important to update policies and procedures as needed to address changes in processes, technologies, and business objectives. For this reason, consider updating these documents as soon as possible after a change occurs and not only on a periodic cycle.
**Guidance - Definitions:**Security policies define the entity's security objectives and principles. Operational procedures describe how to perform activities, and define the controls, methods, and processes that are followed to achieve the desired result in a consistent manner and in accordance with policy objectives.

---
**Control objectives:**6.1
**Sub-requirement:**6.1.2
**Defined Approach Requirements:**Roles and responsibilities for performing activities in Requirement 6 are documented, assigned, and understood.
**Defined Approach Testing Procedures:**
- "6.1.2.a": Examine documentation to verify that descriptions of roles and responsibilities for performing activities in Requirement 6 are documented and assigned.
- "6.1.2.b": Interview personnel responsible for performing activities in Requirement 6 to verify that roles and responsibilities are assigned as documented and are understood.
**Customized Approach Objective:**Day-to-day responsibilities for performing all the activities in Requirement 6 are allocated. Personnel are accountable for successful, continuous operation of these requirements.
**Guidance - Purpose:**If roles and responsibilities are not formally assigned, systems will not be securely maintained, and their security level will be reduced.
**Guidance - Good Practice:**Roles and responsibilities may be documented within policies and procedures or maintained within separate documents. As part of communicating roles and responsibilities, entities can consider having personnel acknowledge their acceptance and understanding of their assigned roles and responsibilities.
**Guidance - Examples:**A method to document roles and responsibilities is a responsibility assignment matrix that includes who is responsible, accountable, consulted, and informed (also called a RACI matrix).

================

### A. Tài liệu gốc của Requirement 6

### B. Summary Overview của Control Objective 6.2
Tài liệu này mô tả chi tiết **Control Objective 6.2** của **Requirement 6** trong **PCI-DSS v4.0.1**, tập trung vào việc phát triển phần mềm nội bộ một cách an toàn nhằm giảm thiểu lỗ hổng bảo mật.
Mục tiêu chính là đảm bảo phần mềm custom/bespoke được phát triển theo secure SDLC, có kiểm soát về coding, review và đào tạo để ngăn ngừa các lỗ hổng bảo mật.
Gồm 4 sub-requirement chính:
- 6.2.1: Phát triển phần mềm an toàn
- 6.2.2: Đào tạo secure coding
- 6.2.3: Review code trước khi release
- 6.2.4: Phòng chống các tấn công phổ biến
Áp dụng cho toàn bộ phần mềm custom/bespoke được phát triển nội bộ (không áp dụng cho third-party software).

### C. Key Points của Control Objective 6.2
- **Phạm vi áp dụng:**Tất cả phần mềm custom/bespoke nội bộ
- **Trách nhiệm:**Tài liệu hóa quy trình phát triển và đảm bảo developer tuân thủ
- **Secure SDLC:**Tích hợp security trong toàn bộ vòng đời phát triển
- **Đào tạo:**Developer phải được đào tạo định kỳ về secure coding
- **Code review:**Phải review code trước khi đưa vào production
- **Kiểm soát kỹ thuật:**Áp dụng kỹ thuật để phòng chống các tấn công phổ biến (injection, XSS, auth bypass…)

### D. Deep Summary của Control Objective 6.2
**Bối cảnh:**
Lỗ hổng trong phần mềm là một trong những nguyên nhân chính dẫn đến compromise hệ thống. Nếu không kiểm soát từ giai đoạn phát triển, chi phí khắc phục sẽ rất cao.
**Nội dung cốt lõi:**
- Áp dụng secure SDLC xuyên suốt các giai đoạn phát triển
- Đào tạo developer về secure coding và security testing
- Thực hiện code review để phát hiện và sửa lỗi trước khi release
- Áp dụng kỹ thuật phòng chống các tấn công phổ biến
- Tích hợp security ngay từ đầu ("shift left")
**Dữ liệu đáng chú ý:**
- Áp dụng cho cả internal và public-facing application
- Có thể sử dụng framework như OWASP, NIST, PCI SSF
**Rủi ro / Lưu ý:**
- Không áp dụng secure SDLC → lỗ hổng đi vào production
- Thiếu đào tạo → developer viết code không an toàn
- Không review code → bỏ sót lỗi nghiêm trọng
- Không kiểm soát common attacks → dễ bị khai thác (SQLi, XSS, auth bypass…)

### E. Structured Output của Control Objective 6.2
**Control objectives:**6.2
**Sub-requirement:**6.2.1
**Defined Approach Requirements:**Bespoke and custom software are developed securely, as follows:
• Based on industry standards and/or best practices for secure development.
• In accordance with PCI DSS (for example, secure authentication and logging).
• Incorporating consideration of information security issues during each stage of the software development lifecycle.
**Defined Approach Testing Procedures:**Examine documented software development procedures to verify that processes are defined that include all elements specified in this requirement.
**Customized Approach Objective:**Bespoke and custom software is developed in accordance with PCI DSS and secure development processes throughout the software lifecycle.
**Applicability Notes:**This applies to all software developed for or by the entity for the entity's own use. This includes both bespoke and custom software. This does not apply to third-party software.
**Guidance - Purpose:**Without the inclusion of security during the requirements definition, design, analysis, and testing phases of software development, security vulnerabilities can be inadvertently or maliciously introduced into the production environment.
**Guidance - Good Practice:**Understanding how sensitive data is handled by the application-including when stored, transmitted, and in memory-can help identify where data needs to be protected. PCI DSS requirements must be considered when developing software to meet those requirements by design, rather than trying to retrofit the software later.
**Guidance - Examples:**Secure software lifecycle management methodologies and frameworks include PCI Software Security Framework, BSIMM, OPENSAMM, and works from NIST, ISO, and SAFECode.

---
**Control objectives:**6.2
**Sub-requirement:**6.2.2
**Defined Approach Requirements:**Software development personnel working on bespoke and custom software are trained at least once every 12 months as follows:
• On software security relevant to their job function and development languages.
• Including secure software design and secure coding techniques.
• Including, if security testing tools are used, how to use the tools for detecting vulnerabilities in software.
**Defined Approach Testing Procedures:**
- "6.2.2.a": Examine software development procedures to verify that processes are defined for training of software development personnel developing bespoke and custom software that includes all elements specified in this requirement.
- "6.2.2.b": Examine training records and interview personnel to verify that software development personnel working on bespoke and custom software received software security training that is relevant to their job function and development languages in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Software development personnel remain knowledgeable about secure development practices; software security; and attacks against the languages, frameworks, or applications they develop. Personnel are able to access assistance and guidance when required.
**Guidance - Purpose:**Having staff knowledgeable in secure coding methods, including techniques defined in Requirement 6.2.4, will help minimize the number of security vulnerabilities introduced through poor coding practices.
**Guidance - Good Practice:**Training for developers may be provided in-house or by third parties. Training should include, but is not limited to, development languages in use, secure software design, secure coding techniques, use of techniques/methods for finding vulnerabilities in code, processes to prevent reintroducing previously resolved vulnerabilities, and how to use any automated security testing tools for detecting vulnerabilities in software. As industry-accepted secure coding practices change, organizational coding practices and developer training may need to be updated to address new threats.

---
**Control objectives:**6.2
**Sub-requirement:**6.2.3
**Defined Approach Requirements:**Bespoke and custom software is reviewed prior to being released into production or to customers, to identify and correct potential coding vulnerabilities, as follows:
• Code reviews ensure code is developed according to secure coding guidelines.
• Code reviews look for both existing and emerging software vulnerabilities.
• Appropriate corrections are implemented prior to release.
**Defined Approach Testing Procedures:**
- "6.2.3.a": Examine documented software development procedures and interview responsible personnel to verify that processes are defined that require all bespoke and custom software to be reviewed in accordance with all elements specified in this requirement.
- "6.2.3.b": Examine evidence of changes to bespoke and custom software to verify that the code changes were reviewed in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Bespoke and custom software cannot be exploited via coding vulnerabilities.
**Applicability Notes:**This requirement for code reviews applies to all bespoke and custom software (both internal and public facing), as part of the system development lifecycle. Public-facing web applications are also subject to additional controls, to address ongoing threats and vulnerabilities after implementation, as defined at PCI DSS Requirement 6.4. Code reviews may be performed using either manual or automated processes, or a combination of both.
**Guidance - Purpose:**Security vulnerabilities in bespoke and custom software are commonly exploited by malicious individuals to gain access to a network and compromise account data. Vulnerable code is far more difficult and expensive to address after it has been deployed or released into production environments. Requiring a formal review and signoff by management prior to release helps to ensure that code is approved and has been developed in accordance with policies and procedures.
**Guidance - Good Practice:**The following items should be considered for inclusion in code reviews:
• Searching for undocumented features (implant tools, backdoors).
• Confirming that software securely uses external components' functions (libraries, frameworks, APIs, etc.). For example, if a third-party library providing cryptographic functions is used, verify that it was integrated securely.
• Checking for correct use of logging to prevent sensitive data from getting into logs.
• Analysis of insecure code structures that may contain potential vulnerabilities related to common software attacks identified in Requirement 6.2.4.
• Checking the application's behavior to detect logical vulnerabilities.

---
**Control objectives:**6.2
**Sub-requirement:**6.2.3.1
**Defined Approach Requirements:**If manual code reviews are performed for bespoke and custom software prior to release to production, code changes are:
• Reviewed by individuals other than the originating code author, and who are knowledgeable about code-review techniques and secure coding practices.
• Reviewed and approved by management prior to release.
**Defined Approach Testing Procedures:**
- "6.2.3.1.a": If manual code reviews are performed for bespoke and custom software prior to release to production, examine documented software development procedures and interview responsible personnel to verify that processes are defined for manual code reviews to be conducted in accordance with all elements specified in this requirement.
- "6.2.3.1.b": Examine evidence of changes to bespoke and custom software and interview personnel to verify that manual code reviews were conducted in accordance with all elements specified in this requirement.
**Customized Approach Objective:**The manual code review process cannot be bypassed and is effective at discovering security vulnerabilities.
**Applicability Notes:**Manual code reviews can be conducted by knowledgeable internal personnel or knowledgeable third-party personnel. An individual that has been formally granted accountability for release control and who is neither the original code author nor the code reviewer fulfills the criteria of being management.
**Guidance - Purpose:**Having code reviewed by someone other than the original author, who is both experienced in code reviews and knowledgeable about secure coding practices, minimizes the possibility that code containing security or logic errors that could affect the security of cardholder data is released into a production environment. Requiring management approval that the code was reviewed limits the ability for the process to be bypassed.
**Guidance - Good Practice:**Having a formal review methodology and review checklists has been found to improve the quality of the code review process. Code review is a tiring process, and for this reason, it is most effective when reviewers only review small amounts of code at a time. To maintain the effectiveness of code reviews, it is beneficial to monitor the general workload of reviewers and to have them review applications they are familiar with. Code reviews may be performed using either manual or automated processes, or a combination of both. Entitles that rely solely on manual code review should ensure that reviewers maintain their skills through regular training as new vulnerabilities are found, and new secure coding methods are recommended.
**Guidance - Further Information:**See the OWASP Code Review Guide .

---
**Control objectives:**6.2
**Sub-requirement:**6.2.4
**Defined Approach Requirements:**Software engineering techniques or other methods are defined and in use by software development personnel to prevent or mitigate common software attacks and related vulnerabilities in bespoke and custom software, including but not limited to the following:
• Injection attacks, including SQL, LDAP, XPath, or other command, parameter, object, fault, or injection-type flaws.
• Attacks on data and data structures, including attempts to manipulate buffers, pointers, input data, or shared data.
• Attacks on cryptography usage, including attempts to exploit weak, insecure, or inappropriate cryptographic implementations, algorithms, cipher suites, or modes of operation.
• Attacks on business logic, including attempts to abuse or bypass application features and functionalities through the manipulation of APIs, communication protocols and channels, client- side functionality, or other system/application functions and resources. This includes cross-site scripting (XSS) and cross-site request forgery (CSRF).
• Attacks on access control mechanisms, including attempts to bypass or abuse identification, authentication, or authorization mechanisms, or attempts to exploit weaknesses in the implementation of such mechanisms.
• Attacks via any 'high-risk' vulnerabilities identified in the vulnerability identification process, as defined in Requirement 6.3.1.
**Defined Approach Testing Procedures:**Examine documented procedures and interview responsible software development personnel to verify that software engineering techniques or other methods are defined and in use by developers of bespoke and custom software to prevent or mitigate all common software attacks as specified in this requirement. 6.3 Security vulnerabilities are identified and addressed.
**Customized Approach Objective:**Bespoke and custom software cannot be exploited via common attacks and related vulnerabilities.
**Applicability Notes:**This applies to all software developed for or by the entity for the entity's own use. This includes both bespoke and custom software. This does not apply to third-party software.
**Guidance - Purpose:**Detecting or preventing common errors that result in vulnerable code as early as possible in the software development process lowers the probability that such errors make it through to production and lead to a compromise. Having formal engineering techniques and tools embedded in the development process will catch these errors early. This philosophy is sometimes called 'shifting security left.' Good Practice For both bespoke and custom software, the entity must ensure that code is developed focusing on the prevention or mitigation of common software attacks, including:
• Attempts to exploit common coding vulnerabilities (bugs).
• Attempts to exploit software design flaws.
• Attempts to exploit implementation/configuration flaws.
• Enumeration attacks - automated attacks that are actively exploited in payments and abuse identification, authentication, or authorization mechanisms. See the PCI Perspectives blog article 'Beware of Account Testing Attacks .'
Researching and documenting software engineering techniques or other methods helps to define how software developers prevent or mitigate various software attacks by features or countermeasures they build into software. This might include identification/authentication mechanisms, access control, input validation routines, etc. Developers should be familiar with different types of vulnerabilities and potential attacks and use measures to avoid potential attack vectors when developing code.
**Guidance - Examples:**Techniques include automated processes and practices that scan code early in the development cycle when code is checked in to confirm the vulnerabilities are not present. 6.3 Security vulnerabilities are identified and addressed. 6.3 Security vulnerabilities are identified and addressed.

================

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

================

### A. Tài liệu gốc của Requirement 6

### B. Summary Overview của Control Objective 6.4
Tài liệu này mô tả chi tiết **Control Objective 6.4** của **Requirement 6** trong **PCI-DSS v4.0.1**, tập trung vào việc bảo vệ ứng dụng web public-facing và kiểm soát script trên trang thanh toán
Mục tiêu chính là đảm bảo các ứng dụng web public-facing được bảo vệ khỏi các tấn công phổ biến và ngăn chặn việc thực thi mã không được ủy quyền trên payment page
Gồm 2 sub-requirement chính:
- 6.4.1: Bảo vệ ứng dụng web public-facing (đánh giá hoặc giải pháp tự động)
- 6.4.2: Triển khai giải pháp kỹ thuật tự động liên tục (thay thế 6.4.1 sau 31/03/2025)
- 6.4.3: Quản lý script trên payment page
Áp dụng cho tất cả các ứng dụng web public-facing và các payment page xử lý dữ liệu thẻ

### C. Key Points của Control Objective 6.4
- **Phạm vi áp dụng:**Các ứng dụng web công khai và trang thanh toán tải/thực thi script trên trình duyệt người dùng
- **Trách nhiệm:** Tài liệu hóa quy trình, phân rõ vai trò trong việc đánh giá bảo mật và quản lý danh mục script
- **Quản lý tài liệu / cấu hình:** Duy trì inventory script kèm lý do nghiệp vụ; cấu hình các giải pháp tự động (WAF/RASP) để chặn hoặc cảnh báo tấn công
- **Kiểm soát / bảo vệ:**Sử dụng các phương pháp như SRI, CSP để đảm bảo tính toàn vẹn của script và ngăn chặn skimming dữ liệu

### D. Deep Summary của Control Objective 6.4
**Bối cảnh:**
Các ứng dụng web công khai là mục tiêu tấn công hàng đầu; việc thiếu kiểm soát script trên trang thanh toán tạo điều kiện cho mã độc đánh cắp dữ liệu thẻ ngay tại trình duyệt khách hàng (skimming)
**Nội dung cốt lõi:**
- Bảo vệ liên tục: Sử dụng các công cụ đánh giá lỗ hổng hoặc giải pháp tự động (WAF/RASP) để phát hiện và ngăn chặn các cuộc tấn công web phổ biến
- Quản lý lỗ hổng: Mọi lỗ hổng ứng dụng phải được xếp hạng, khắc phục và tái đánh giá sau khi sửa lỗi
- Kiểm soát script chặt chẽ: Chỉ cho phép các script đã được ủy quyền, đảm bảo tính toàn vẹn mã nguồn và duy trì danh sách quản lý đầy đủ
**Dữ liệu đáng chú ý:**
- Assessment phải thực hiện ít nhất 12 tháng/lần và sau thay đổi lớn
- Các yêu cầu 6.4.2 và 6.4.3 là best practice cho đến hết ngày 31/03/2025
- Có thể dùng WAF, RASP, CSP, SRI để bảo vệ
**Rủi ro / Lưu ý:**
- Script của bên thứ ba có thể bị thay đổi chức năng mà tổ chức không biết, dẫn đến rủi ro chuỗi cung ứng
- Nếu không duy trì inventory script, tổ chức sẽ mất kiểm soát đối với những mã đang thực thi trên trình duyệt người tiêu dùng
- Ứng dụng không được bảo vệ bởi giải pháp tự động hoặc đánh giá định kỳ sẽ dễ bị khai thác bởi các lỗi SQLi hoặc XSS

### E. Structured Output của Control Objective 6.4
**Control objectives:**6.4
**Sub-requirement:**6.4.1
**Defined Approach Requirements:**For public-facing web applications, new threats and vulnerabilities are addressed on an ongoing basis and these applications are protected against known attacks as follows:
• Reviewing public-facing web applications via manual or automated application vulnerability security assessment tools or methods as follows: - At least once every 12 months and after significant changes. - By an entity that specializes in application security. - Including, at a minimum, all common software attacks in Requirement 6.2.4. - All vulnerabilities are ranked in accordance with requirement 6.3.1. - All vulnerabilities are corrected. - The application is re-evaluated after the corrections. OR
• Installing an automated technical solution(s) that continually detects and prevents web-based attacks as follows: - Installed in front of public-facing web applications to detect and prevent web- based attacks. - Actively running and up to date as applicable. - Generating audit logs. - Configured to either block web-based attacks or generate an alert that is immediately investigated.
**Defined Approach Testing Procedures:**For public-facing web applications, ensure that either one of the required methods is in place as follows:
• If manual or automated vulnerability security assessment tools or methods are in use, examine documented processes, interview personnel, and examine records of application security assessments to verify that public- facing web applications are reviewed in accordance with all elements of this requirement specific to the tool/method. OR
• If an automated technical solution(s) is installed that continually detects and prevents web- based attacks, examine the system configuration settings and audit logs, and interview responsible personnel to verify that the automated technical solution(s) is installed in accordance with all elements of this requirement specific to the solution(s).
**Customized Approach Objective:**Public-facing web applications are protected against malicious attacks.
**Applicability Notes:**This assessment is not the same as the vulnerability scans performed for Requirement 11.3.1 and 11.3.2. This requirement will be superseded by Requirement 6.4.2 after 31 March 2025 when Requirement 6.4.2 becomes effective.
**Guidance - Purpose:**Public-facing web applications are those that are available to the public (not only for internal use). These applications are primary targets for attackers, and poorly coded web applications provide an easy path for attackers to gain access to sensitive data and systems.
**Guidance - Good Practice:**Manual or automated vulnerability security assessment tools or methods review and/or test the application for vulnerabilities. Common assessment tools include specialized web scanners that perform automatic analysis of web application protection. When using automated technical solutions, it is important to include processes that facilitate timely responses to alerts generated by the solutions so that any detected attacks can be mitigated.
**Guidance - Examples:**A web application firewall (WAF) installed in front of public-facing web applications to check all traffic is an example of an automated technical solution that detects and prevents web-based attacks (for example, the attacks included in Requirement 6.2.4). WAFs filter and block non-essential traffic at the application layer. A properly configured WAF helps to prevent application-layer attacks on applications that are improperly coded or configured. Another example of an automated technical solution is Runtime Application Self-Protection (RASP) technologies. When implemented correctly, RASP solutions can detect and block anomalous behavior by the software during execution. While WAFs typically monitor the application perimeter, RASP solutions monitor and block behavior within the application.

---
**Control objectives:**6.4
**Sub-requirement:**6.4.2
**Defined Approach Requirements:**For public-facing web applications, an automated technical solution is deployed that continually detects and prevents web-based attacks, with at least the following:
• Is installed in front of public-facing web applications and is configured to detect and prevent web-based attacks.
• Actively running and up to date as applicable.
• Generating audit logs.
• Configured to either block web-based attacks or generate an alert that is immediately investigated.
**Defined Approach Testing Procedures:**For public-facing web applications, examine the system configuration settings and audit logs, and interview responsible personnel to verify that an automated technical solution that detects and prevents web-based attacks is in place in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Public-facing web applications are protected in real time against malicious attacks.
**Applicability Notes:**This new requirement will replace Requirement 6.4.1 once its effective date is reached. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Public-facing web applications are primary targets for attackers, and poorly coded web applications provide an easy path for attackers to gain access to sensitive data and systems.
**Guidance - Good Practice:**When using automated technical solutions, it is important to include processes that facilitate timely responses to alerts generated by the solutions so that any detected attacks can be mitigated. Such solutions may also be used to automate mitigation, for example rate-limiting controls, which can be implemented to mitigate against brute-force attacks and enumeration attacks.
**Guidance - Examples:**A web application firewall (WAF), which can be either on-premise or cloud-based, installed in front of public-facing web applications to check all traffic, is an example of an automated technical solution that detects and prevents web-based attacks (for example, the attacks included in Requirement 6.2.4). WAFs filter and block non-essential traffic at the application layer. A properly configured WAF helps to prevent application-layer attacks on applications that are improperly coded or configured.

---
**Control objectives:**6.4
**Sub-requirement:**6.4.3
**Defined Approach Requirements:**All payment page scripts that are loaded and executed in the consumer's browser are managed as follows:
• A method is implemented to confirm that each script is authorized.
• A method is implemented to assure the integrity of each script.
• An inventory of all scripts is maintained with written business or technical justification as to why each is necessary.
**Defined Approach Testing Procedures:**
- "6.4.3.a": Examine policies and procedures to verify that processes are defined for managing all payment page scripts that are loaded and executed in the consumer's browser, in accordance with all elements specified in this requirement.
- "6.4.3.b": Interview responsible personnel and examine inventory records and system configurations to verify that all payment page scripts that are loaded and executed in the consumer's browser are managed in accordance with all elements specified in this requirement.
**Customized Approach Objective:** Unauthorized code cannot be executed in the payment page as it is rendered in the consumer's browser.
**Applicability Notes:**This requirement applies to all scripts loaded from the entity's environment and scripts loaded from third and fourth parties. This requirement also applies to scripts in the entity's webpage(s) that includes a TPSP's/ payment processor's embedded payment page/form (for example, one or more inline frames or iframes). This requirement does not apply to an entity for scripts in a TPSP's/payment processor's embedded payment page/form (for example, one or more iframes), where the entity includes a TPSP's/payment processor's payment page/form on its webpage. Scripts in the TPSP's/payment processor's embedded payment page/form are the responsibility of the TPSP/payment processor to manage in accordance with this requirement. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Scripts loaded and executed in the payment page can have their functionality altered without the entity's knowledge and can also have the functionality to load additional external scripts (for example, advertising and tracking, tag management systems). Such seemingly harmless scripts can be used by potential attackers to upload malicious scripts that can read and exfiltrate cardholder data from the consumer browser. Ensuring that the functionality of all such scripts is understood to be necessary for the operation of the payment page minimizes the number of scripts that could be tampered with. Ensuring that scripts have been explicitly authorized reduces the probability of unnecessary scripts being added to the payment page without appropriate management approval. Where it is impractical for such authorization to occur before a script is changed or a new script is added to the page, the authorization should be confirmed as soon as possible after a change is made. Using techniques to prevent tampering with the script will minimize the probability of the script being modified to carry out unauthorized behavior, such as skimming the cardholder data from the payment page.
**Guidance - Good Practice:**Scripts may be authorized by manual or automated (e.g., workflow) processes. Where the payment page will be loaded into an inline frame (iframe), restricting the location that the payment page can be loaded from, using the parent page's Content Security Policy (CSP) can help prevent unauthorized content being substituted for the payment page. Where an entity includes a TPSP's/payment processor's embedded payment page/form on its webpage, the entity should expect the TPSP/payment processor to provide evidence that the TPSP/payment processor is meeting this requirement, in accordance with the TPSP's/payment processor's PCI DSS assessment and Requirement 12.9.
**Guidance - Examples:**The integrity of scripts can be enforced by several different mechanisms including, but not limited to:
• Sub-resource integrity (SRI), which allows the consumer browser to validate that a script has not been tampered with.
• A CSP, which limits the locations the consumer browser can load a script from and transmit account data to.
• Proprietary script or tag-management systems, which can prevent malicious script execution. 6.5 Changes to all system components are managed securely. 6.5 Changes to all system components are managed securely.

================

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