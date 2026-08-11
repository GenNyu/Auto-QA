### A. Tài liệu gốc của Requirement 11

### B. Summary Overview của Control Objective 11.3
Tài liệu này mô tả chi tiết **Control Objective 11.3** của **Requirement 11** trong **PCI-DSS v4.0.1**, tập trung vào việc quét lỗ hổng (vulnerability scanning) để phát hiện và xử lý các điểm yếu bảo mật trong hệ thống.
Mục tiêu chính là đảm bảo các lỗ hổng được phát hiện định kỳ, đánh giá rủi ro và khắc phục kịp thời nhằm giảm thiểu khả năng bị khai thác.
Gồm 2 sub-requirement chính:
- 11.3.1: Quét lỗ hổng nội bộ
- 11.3.2: Quét lỗ hổng bên ngoài
Áp dụng cho tất cả các thành phần hệ thống (system components) trong môi trường (cả nội bộ và bên ngoài)

### C. Key Points của Control Objective 11.3
- **Phạm vi áp dụng:**Toàn bộ các thành phần hệ thống thuộc phạm vi PCI DSS
- **Trách nhiệm:** Tài liệu hóa và triển khai quy trình quét lỗ hổng; việc quét phải được thực hiện bởi nhân sự có năng lực và đảm bảo tính độc lập khách quan
- **Quản lý quét định kỳ:**Thực hiện quét ít nhất 3 tháng một lần và sau khi có các thay đổi lớn (significant changes)
- **Xử lý lỗ hổng:**Khắc phục các lỗ hổng được xếp hạng Cao (High) hoặc Nghiêm trọng (Critical) và thực hiện quét lại (rescan) để xác nhận kết quả
- **Kiểm soát quét bên ngoài:**Các lần quét bên ngoài phải do nhà cung cấp dịch vụ quét được ủy quyền (ASV) thực hiện

### D. Deep Summary của Control Objective 11.3
**Bối cảnh:**
Lỗ hổng bảo mật là điểm xâm nhập phổ biến mà kẻ tấn công thường lợi dụng để xâm nhập hệ thống; việc quét định kỳ giúp tổ chức nhận diện và vá các lỗ hổng trước khi chúng bị khai thác
**Nội dung cốt lõi:**
- Thực hiện đa dạng: Kết hợp quét lỗ hổng nội bộ và bên ngoài để có cái nhìn toàn diện về bề mặt tấn công
- Quét có xác thực (Authenticated Scanning): Sử dụng quyền truy cập phù hợp khi quét nội bộ để phát hiện các lỗ hổng local mà quét thông thường không thấy được
- Quản lý dựa trên rủi ro: Ưu tiên xử lý các lỗ hổng High/Critical và quản lý các lỗ hổng khác dựa trên phân tích rủi ro mục tiêu
- Xác nhận sau thay đổi: Thực hiện quét ngay sau các thay đổi lớn để đảm bảo không phát sinh lỗ hổng mới trong quá trình cập nhật hệ thống
**Dữ liệu đáng chú ý:**
- Tần suất tối thiểu: 3 tháng/lần
- Quét bên ngoài phải đạt trạng thái "passing scan" theo tiêu chuẩn của chương trình ASV
- Ngưỡng xử lý cho quét bên ngoài sau thay đổi: Lỗ hổng có điểm CVSS >= 4.0
**Rủi ro / Lưu ý:**
- Nếu không thực hiện quét lại (rescan), tổ chức không thể khẳng định các lỗ hổng đã được khắc phục hoàn toàn
- Quét không đủ quyền (không xác thực) dẫn đến rủi ro bỏ sót các lỗ hổng nghiêm trọng nằm sâu trong hệ điều hành hoặc ứng dụng
- Yêu cầu về quét có xác thực (11.3.1.2) và quản lý lỗ hổng rủi ro thấp (11.3.1.1) là best practice cho đến hết ngày 31/03/2025

### E. Structured Output của Control Objective 11.3
**Control objectives:**11.3
**Sub-requirement:**11.3.1
**Defined Approach Requirements:**Internal vulnerability scans are performed as follows:
• At least once every three months.
• Vulnerabilities that are either high-risk or critical (according to the entity's vulnerability risk rankings defined at Requirement 6.3.1) are resolved.
• Rescans are performed that confirm all high-risk and all critical vulnerabilities (as noted above) have been resolved.
• Scan tool is kept up to date with latest vulnerability information.
• Scans are performed by qualified personnel and organizational independence of the tester exists.
**Defined Approach Testing Procedures:**
- "11.3.1.a": Examine internal scan report results from the last 12 months to verify that internal scans occurred at least once every three months in the most recent 12-month period.
- "11.3.1.b": Examine internal scan report results from each scan and rescan run in the last 12 months to verify that all high-risk vulnerabilities and all critical vulnerabilities (defined in PCI DSS Requirement 6.3.1) are resolved.
- "11.3.1.c": Examine scan tool configurations and interview personnel to verify that the scan tool is kept up to date with the latest vulnerability information.
- "11.3.1.d": Interview responsible personnel to verify that the scan was performed by a qualified internal resource(s) or qualified external third party and that organizational independence of the tester exists.
**Customized Approach Objective:**The security posture of all system components is verified periodically using automated tools designed to detect vulnerabilities operating inside the network. Detected vulnerabilities are assessed and rectified based on a formal risk assessment framework.
**Applicability Notes:**It is not required to use a QSA or ASV to conduct internal vulnerability scans. Internal vulnerability scans can be performed by qualified, internal staff that are reasonably independent of the system component(s) being scanned (for example, a network administrator should not be responsible for scanning the network), or an entity may choose to have internal vulnerability scans performed by a firm specializing in vulnerability scanning.
**Guidance - Purpose:**Identifying and addressing vulnerabilities promptly reduces the likelihood of a vulnerability being exploited and the potential compromise of a system component or cardholder data. Vulnerability scans conducted at least every three months provide this detection and identification.
**Guidance - Good Practice:**Vulnerabilities posing the greatest risk to the environment (for example, ranked high or critical per Requirement 6.3.1) should be resolved with the highest priority. Vulnerabilities identified during internal vulnerability scans should be part of a vulnerability management process that includes multiple vulnerability sources, as specified in Requirement 6.3.1. Multiple scan reports can be combined for the quarterly scan process to show that all systems were scanned and all applicable vulnerabilities were resolved as part of the three-month vulnerability scan cycle. However, additional documentation may be required to verify non- remediated vulnerabilities are in the process of being resolved. While scans are required at least once every three months, more frequent scans are recommended depending on the network complexity, frequency of change, and types of devices, software, and operating systems used.
**Guidance - Definitions:**A vulnerability scan is a combination of automated tools, techniques, and/or methods run against external and internal devices and servers, designed to expose potential vulnerabilities in applications, operating systems, and network devices that could be found and exploited by malicious individuals.

---
**Control objectives:**11.3
**Sub-requirement:**11.3.1.1
**Defined Approach Requirements:**All other applicable vulnerabilities (those not ranked as high-risk vulnerabilities or critical vulnerabilities according to the entity's vulnerability risk rankings defined at Requirement 6.3.1) are managed as follows:
• Addressed based on the risk defined in the entity's targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1.
• Rescans are conducted as needed.
**Defined Approach Testing Procedures:**
- "11.3.1.1.a": Examine the entity's targeted risk analysis that defines the risk for addressing all other applicable vulnerabilities (those not ranked as high-risk vulnerabilities or critical vulnerabilities according to the entity's vulnerability risk rankings at Requirement 6.3.1) to verify the risk analysis was performed in accordance with all elements specified at Requirement 12.3.1.
- "11.3.1.1.b": Interview responsible personnel and examine internal scan report results or other documentation to verify that all other applicable
**Customized Approach Objective:** Lower ranked vulnerabilities (lower than high-risk or critical) are addressed at a frequency in accordance with the entity's risk.
**Applicability Notes:**The timeframe for addressing lower-risk vulnerabilities is subject to the results of a risk analysis per Requirement 12.3.1 that includes (minimally) identification of assets being protected, threats, and likelihood and/or impact of a threat being realized. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**All vulnerabilities, regardless of criticality, provide a potential avenue of attack and must therefore be addressed periodically, with the vulnerabilities that expose the most risk addressed more quickly to limit the potential window of attack.

---
**Control objectives:**11.3
**Sub-requirement:**11.3.1.2
**Defined Approach Requirements:**Internal vulnerability scans are performed via authenticated scanning as follows:
• Systems that are unable to accept credentials for authenticated scanning are documented.
• Sufficient privileges are used for those systems that accept credentials for scanning.
• If accounts used for authenticated scanning can be used for interactive login, they are managed in accordance with Requirement 8.2.2.
**Defined Approach Testing Procedures:**
- "11.3.1.2.a": Examine scan tool configurations to verify that authenticated scanning is used for internal scans, with sufficient privileges, for those systems that accept credentials for scanning.
- "11.3.1.2.b": Examine scan report results and interview personnel to verify that authenticated scans are performed.
- "11.3.1.2.c": If accounts used for authenticated scanning can be used for interactive login, examine the accounts and interview personnel to verify the accounts are managed following all elements specified in Requirement 8.2.2.
- "11.3.1.2.d": Examine documentation to verify that systems that are unable to accept credentials for authenticated scanning are defined.
**Customized Approach Objective:**Automated tools used to detect vulnerabilities can detect vulnerabilities local to each system, which are not visible remotely.
**Applicability Notes:**The authenticated scanning tools can be either host-based or network-based. 'Sufficient' privileges are those needed to access system resources such that a thorough scan can be conducted that detects known vulnerabilities. This requirement does not apply to system components that cannot accept credentials for scanning. Examples of systems that may not accept credentials for scanning include some network and security appliances, mainframes, and containers. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Authenticated scanning provides greater insight into an entity's vulnerability landscape since it can detect vulnerabilities that unauthenticated scans cannot detect. Attackers may leverage vulnerabilities that an entity is unaware of because certain vulnerabilities will only be detected with authenticated scanning. Authenticated scanning can yield significant additional information about an organization's vulnerabilities.
**Guidance - Good Practice:**The credentials used for these scans should be considered highly privileged. They should be protected and controlled as such, following PCI DSS Requirements 7 and 8 (except for those requirements for multi-factor authentication and application and system accounts).

---
**Control objectives:**11.3
**Sub-requirement:**11.3.1.3
**Defined Approach Requirements:**Internal vulnerability scans are performed after any significant change as follows:
• Vulnerabilities that are either high-risk or critical (according to the entity's vulnerability risk rankings defined at Requirement 6.3.1) are resolved.
• Rescans are conducted as needed.
• Scans are performed by qualified personnel and organizational independence of the tester exists (not required to be a QSA or ASV).
**Defined Approach Testing Procedures:**
- "11.3.1.3.a": Examine change control documentation and internal scan reports to verify that system components were scanned after any significant changes.
- "11.3.1.3.b": Interview personnel and examine internal scan and rescan reports to verify that internal scans were performed after significant changes and that all high-risk vulnerabilities and all critical vulnerabilities (defined in PCI DSS Requirement 6.3.1) were resolved.
- "11.3.1.3.c": Interview personnel to verify that internal scans are performed by a qualified internal resource(s) or qualified external third party and that organizational independence of the tester exists.
**Customized Approach Objective:**The security posture of all system components is verified following significant changes to the network or systems, by using automated tools designed to detect vulnerabilities operating inside the network. Detected vulnerabilities are assessed and rectified based on a formal risk assessment framework.
**Applicability Notes:**Authenticated internal vulnerability scanning per Requirement 11.3.1.2 is not required for scans performed after significant changes.
**Guidance - Purpose:**Scanning an environment after any significant changes ensures that changes were completed appropriately such that the security of the environment was not compromised because of the change.
**Guidance - Good Practice:**Entities should perform scans after significant changes as part of the change process per Requirement 6.5.2 and before considering the change complete. All system components affected by the change will need to be scanned.

---
**Control objectives:**11.3
**Sub-requirement:**11.3.2
**Defined Approach Requirements:**External vulnerability scans are performed as follows:
• At least once every three months.
• By a PCI SSC Approved Scanning Vendor (ASV).
• Vulnerabilities are resolved and ASV Program Guide requirements for a passing scan are met.
• Rescans are performed as needed to confirm that vulnerabilities are resolved per the ASV Program Guide requirements for a passing scan.
**Defined Approach Testing Procedures:**
- "11.3.2.a": Examine ASV scan reports from the last 12 months to verify that external vulnerability scans occurred at least once every three months in the most recent 12-month period.
- "11.3.2.b": Examine the ASV scan report from each scan and rescan run in the last 12 months to verify that vulnerabilities are resolved and the ASV Program Guide requirements for a passing scan are met.
- "11.3.2.c": Examine the ASV scan reports to verify that the scans were completed by a PCI SSC Approved Scanning Vendor (ASV).
**Customized Approach Objective:**This requirement is not eligible for the customized approach.
**Applicability Notes:**For the initial PCI DSS assessment against this requirement, it is not required that four passing scans be completed within 12 months if the assessor verifies: 1) the most recent scan result was a passing scan, 2) the entity has documented policies and procedures requiring scanning at least once every three months, and 3) vulnerabilities noted in the scan results have been corrected as shown in a re-scan(s).
However, for subsequent years after the initial PCI DSS assessment, passing scans at least every three months must have occurred. ASV scanning tools can scan a vast array of network types and topologies. Any specifics about the target environment (for example, load balancers, third-party providers, ISPs, specific configurations, protocols in use, scan interference) should be worked out between the ASV and scan customer. Refer to the ASV Program Guide published on the PCI SSC website for scan customer responsibilities, scan preparation, etc.
**Guidance - Purpose:**Attackers routinely look for unpatched or vulnerable externally facing servers, which can be leveraged to launch a directed attack. Organizations must ensure these externally facing devices are regularly scanned for weaknesses and that vulnerabilities are patched or remediated to protect the entity. Because external networks are at greater risk of compromise, external vulnerability scanning must be performed at least once every three months by a PCI SSC Approved Scanning Vendor (ASV).
**Guidance - Good Practice:**While scans are required at least once every three months, more frequent scans are recommended depending on the network complexity, frequency of change, and types of devices, software, and operating systems used. Vulnerabilities identified during external vulnerability scans should be part of a vulnerability management process that includes multiple vulnerability sources, as specified in Requirement 6.3.1. Multiple scan reports can be combined to show that all systems were scanned and that all applicable vulnerabilities were resolved as part of the three-month vulnerability scan cycle. However, additional documentation may be required to verify non-remediated vulnerabilities are in the process of being resolved.
**Guidance - Further Information:**See the ASV Program Guide on the PCI SSC website.

---
**Control objectives:**11.3
**Sub-requirement:**11.3.2.1
**Defined Approach Requirements:**External vulnerability scans are performed after any significant change as follows:
• Vulnerabilities that are scored 4.0 or higher by the CVSS are resolved.
• Rescans are conducted as needed.
• Scans are performed by qualified personnel and organizational independence of the tester exists (not required to be a QSA or ASV). 11.4 External and internal penetration testing is regularly performed, and exploitable vulnerabilities and security weaknesses are corrected.
**Defined Approach Testing Procedures:**
- "11.3.2.1.a": Examine change control documentation and external scan reports to verify that system components were scanned after any significant changes.
- "11.3.2.1.b": Interview personnel and examine external scan and rescan reports to verify that external scans were performed after significant changes and that vulnerabilities scored 4.0 or higher by the CVSS were resolved.
- "11.3.2.1.c": Interview personnel to verify that external scans are performed by a qualified internal resource(s) or qualified external third party and that organizational independence of the tester exists. 11.4 External and internal penetration testing is regularly performed, and exploitable vulnerabilities and security weaknesses are corrected.
**Customized Approach Objective:**The security posture of all system components is verified following significant changes to the network or systems, by using tools designed to detect vulnerabilities operating from outside the network. Detected vulnerabilities are assessed and rectified based on a formal risk assessment framework.
**Guidance - Purpose:**Scanning an environment after any significant changes ensures that changes were completed appropriately such that the security of the environment was not compromised because of the change.
**Guidance - Good Practice:**Entities should include the need to perform scans after significant changes as part of the change process and before the change is considered complete. All system components affected by the change will need to be scanned.