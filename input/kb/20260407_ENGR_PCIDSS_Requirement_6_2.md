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