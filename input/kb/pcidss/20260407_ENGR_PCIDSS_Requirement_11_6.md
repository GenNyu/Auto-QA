### A. Tài liệu gốc của Requirement 11

### B. Summary Overview của Control Objective 11.6
Tài liệu này mô tả chi tiết **Control Objective 11.6 **của **Requirement 11 **trong **PCI-DSS v4.0.1**, tập trung vào việc phát hiện thay đổi và can thiệp trái phép trên payment page phía trình duyệt người dùng.
Mục tiêu chính là đảm bảo các thay đổi bất thường (đặc biệt liên quan đến script và HTTP header) trên payment page được phát hiện kịp thời để ngăn chặn tấn công skimming.
Gồm 1 sub-requirement chính:
- 11.6.1: Phát hiện thay đổi và tampering trên payment page
Áp dụng cho các hệ thống e-commerce xử lý payment page, bao gồm cả trường hợp sử dụng embedded payment form từ bên thứ ba.

### C. Key Points của Control Objective 11.6
- **Phạm vi áp dụng:**Payment page và nội dung được render trên trình duyệt người dùng
- **Trách nhiệm:**Triển khai cơ chế phát hiện thay đổi và tampering
- **Kiểm soát nội dung:**Giám sát HTTP header và script của payment page
- **Phát hiện thay đổi:**Alert khi có thay đổi trái phép hoặc indicator of compromise
- **Tần suất kiểm tra:**Ít nhất hàng tuần hoặc theo risk analysis
- **Phạm vi bên thứ ba: B**ao gồm cả embedded payment form (TPSP)

### D. Deep Summary của Control Objective 11.6
**Bối cảnh:**
Các cuộc tấn công e-skimming thường chèn mã độc vào payment page phía client, rất khó phát hiện nếu chỉ kiểm soát phía server.
**Nội dung cốt lõi:**
- Triển khai cơ chế phát hiện thay đổi và tampering trên payment page
- Giám sát HTTP header và nội dung script khi được load trên browser
- Phát hiện indicator of compromise hoặc hành vi bất thường
- Thực hiện kiểm tra định kỳ (≥ hàng tuần) hoặc theo risk-based
- Áp dụng cả với môi trường sử dụng third-party payment form
- Phát cảnh báo ngay khi phát hiện thay đổi trái phép
**Dữ liệu đáng chú ý:**
- Phát hiện dựa trên nội dung thực tế render trên browser
- Có thể sử dụng CSP, synthetic monitoring hoặc script detection
**Rủi ro / Lưu ý:**
- Không kiểm soát client-side → không phát hiện e-skimming
- Script bị chèn → đánh cắp dữ liệu thẻ
- Không monitor thay đổi → attacker tồn tại lâu
- Phụ thuộc third-party → cần đảm bảo họ cũng tuân thủ kiểm soát

### E. Structured Output của Control Objective 11.6
**Control objectives:**11.6
**Sub-requirement:**11.6.1
**Defined Approach Requirements:**A change- and tamper-detection mechanism is deployed as follows:
• To alert personnel to unauthorized modification (including indicators of compromise, changes, additions, and deletions) to the security- impacting HTTP headers and the script contents of payment pages as received by the consumer browser.
• The mechanism is configured to evaluate the received HTTP headers and payment pages.
• The mechanism functions are performed as follows: - At least weekly OR - Periodically (at the frequency defined in the entity's targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1).
**Defined Approach Testing Procedures:**
- "11.6.1.a": Examine system settings, monitored payment pages, and results from monitoring activities to verify the use of a change- and tamper- detection mechanism.
- "11.6.1.b": Examine configuration settings to verify the mechanism is configured in accordance with all elements specified in this requirement.
- "11.6.1.c": If the mechanism functions are performed at an entity-defined frequency, examine the entity's targeted risk analysis for determining the frequency to verify the risk analysis was performed in accordance with all elements specified at Requirement 12.3.1.
- "11.6.1.d": Examine configuration settings and interview personnel to verify the mechanism functions are performed either:
• At least weekly OR
• At the frequency defined in the entity's targeted risk analysis performed for this requirement.
**Customized Approach Objective:**E-commerce skimming code or techniques cannot be added to payment pages as received by the consumer browser without a timely alert being generated. Anti-skimming measures cannot be removed from payment pages without a prompt alert being generated.
**Applicability Notes:**This requirement also applies to entities with a webpage(s) that includes a TPSP's/payment processor's embedded payment page/form (for example, one or more inline frames or iframes.) This requirement does not apply to an entity for scripts in a TPSP's/payment processor's embedded payment page/form (for example, one or more iframes), where the entity includes a TPSP's/payment processor's payment page/form on its webpage. Scripts in the TPSP's/payment processor's embedded payment page/form are the responsibility of the TPSP/payment processor to manage in accordance with this requirement. The intention of this requirement is not that an entity installs software in the systems or browsers of its consumers, but rather that the entity uses techniques such as those described under Examples in the Guidance column to prevent and detect unexpected script activities. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Many web pages now rely on assembling objects, including active content (primarily JavaScript), from multiple internet locations. Additionally, the content of many web pages is defined using content management and tag management systems that may not be possible to monitor using traditional change detection mechanisms. Therefore, the only place to detect changes or indicators of malicious activity is in the consumer browser as the page is constructed and all JavaScript interpreted. By comparing the current version of the HTTP header and the active content of payment pages as received by the consumer browser with prior or known versions, it is possible to detect unauthorized changes that may indicate a skimming attack, or an attempt to disable a control designed to protect against, or to detect, skimming attacks. Additionally, by looking for known indicators of compromise and script elements or behavior typical of skimmers, suspicious alerts can be raised.
**Guidance - Good Practice:**Where an entity includes a TPSP's/payment processor's embedded payment page/form on its webpage, the entity should expect the TPSP/payment processor to provide evidence that the TPSP/payment processor is meeting this requirement, in accordance with the TPSP's/payment processor's PCI DSS assessment and Requirement 12.9.
**Guidance - Examples:**Mechanisms that detect and report on changes to the headers and content of the payment page could include, but are not limited to, a combination of the following techniques:
• Violations of the Content Security Policy (CSP) can be reported to the entity using the report-to or report-uri CSP directives.
• Changes to the CSP itself can indicate tampering.
• External monitoring by systems that request and analyze the received web pages (also known as synthetic user monitoring) can detect changes to JavaScript in payment pages and alert personnel.
• Embedding tamper-resistant, tamper-detection script in the payment page can alert and block when malicious script behavior is detected.
• Reverse proxies and Content Delivery Networks can detect changes in scripts and alert personnel.
The above list of mechanisms is not exhaustive, and the use of any one mechanism is not necessarily a full detection and reporting mechanism. Often, these mechanisms are subscription or cloud- based, but can also be based on custom and bespoke solutions.