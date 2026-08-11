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