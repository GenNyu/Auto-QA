### A. Tài liệu gốc của Requirement 11

### B. Summary Overview của Control Objective 11.1
Tài liệu này mô tả chi tiết **Control Objective 11.1** của **Requirement 11** trong **PCI-DSS v4.0.1**, tập trung vào việc thiết lập và duy trì chính sách, quy trình và phân công trách nhiệm liên quan đến kiểm thử và giám sát bảo mật.
Mục tiêu chính là đảm bảo các chính sách, quy trình và vai trò trách nhiệm được tài liệu hóa, cập nhật, áp dụng thực tế và được hiểu rõ bởi các bên liên quan trong hoạt động kiểm thử bảo mật.
Gồm 2 sub-requirement chính:
- 11.1.1: Quản lý chính sách và quy trình
- 11.1.2: Phân công vai trò và trách nhiệm
Áp dụng cho toàn bộ tổ chức và nhân sự tham gia vào các hoạt động kiểm thử và giám sát bảo mật theo Requirement 11.

### C. Key Points của Control Objective 11.1
- **Phạm vi áp dụng:**Tất cả chính sách, quy trình và nhân sự liên quan kiểm thử và giám sát bảo mật
- **Trách nhiệm:**Phân rõ vai trò, đảm bảo nhân sự hiểu và thực hiện đúng
- **Quản lý tài liệu:**Chính sách và quy trình phải được tài liệu hóa, cập nhật và phổ biến
- **Áp dụng thực tế:** Quy trình phải được triển khai và sử dụng thực tế
- **Truyền thông:**Đảm bảo các bên liên quan được phổ biến và hiểu nội dung

### D. Deep Summary của Control Objective 11.1
**Bối cảnh:**
Nếu chính sách và trách nhiệm không rõ ràng, các hoạt động kiểm thử và giám sát bảo mật có thể không được thực hiện đầy đủ, dẫn đến không phát hiện được lỗ hổng hoặc tấn công.
**Nội dung cốt lõi:**
- Tài liệu hóa chính sách và quy trình liên quan kiểm thử và giám sát bảo mật
- Cập nhật khi có thay đổi về hệ thống hoặc phương pháp kiểm thử
- Đảm bảo quy trình được áp dụng thực tế
- Phổ biến đến tất cả nhân sự liên quan
- Phân rõ vai trò và trách nhiệm cho từng hoạt động
**Dữ liệu đáng chú ý:**
- Chính sách và quy trình phải "in use" và "known to all affected parties"
- Có thể sử dụng RACI matrix để quản lý trách nhiệm
**Rủi ro / Lưu ý:**
- Chính sách không cập nhật → không phù hợp với môi trường thực tế
- Quy trình không được thực thi → bỏ sót kiểm thử bảo mật
- Nhân sự không rõ trách nhiệm → không thực hiện kiểm soát
- Thiếu phân công rõ ràng → không có accountability

### E. Structured Output của Control Objective 11.1
**Control objectives:**11.1
**Sub-requirement:**11.1.1
**Defined Approach Requirements:**All security policies and operational procedures that are identified in Requirement 11 are:
• Documented.
• Kept up to date.
• In use.
• Known to all affected parties.
**Defined Approach Testing Procedures:**Examine documentation and interview personnel to verify that security policies and operational procedures are managed in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Expectations, controls, and oversight for meeting activities within Requirement 11 are defined and adhered to by affected personnel. All supporting activities are repeatable, consistently applied, and conform to management's intent.
**Guidance - Purpose:**Requirement 11.1.1 is about effectively managing and maintaining the various policies and procedures specified throughout Requirement 11. While it is important to define the specific policies or procedures called out in Requirement 11, it is equally important to ensure they are properly documented, maintained, and disseminated.
**Guidance - Good Practice:**It is important to update policies and procedures as needed to address changes in processes, technologies, and business objectives. For this reason, consider updating these documents as soon as possible after a change occurs and not only on a periodic cycle.
**Guidance - Definitions:**Security policies define the entity's security objectives and principles. Operational procedures describe how to perform activities, and define the controls, methods, and processes that are followed to achieve the desired result in a consistent manner and in accordance with policy objectives.

---
**Control objectives:**11.1
**Sub-requirement:**11.1.2
**Defined Approach Requirements:**Roles and responsibilities for performing activities in Requirement 11 are documented, assigned, and understood. continuous operation of these requirements. 11.2 Wireless access points are identified and monitored, and unauthorized wireless access points are addressed. 11.2 Wireless access points are identified and monitored, and unauthorized wireless access points are addressed.
**Defined Approach Testing Procedures:**
- "11.1.2.a": Examine documentation to verify that descriptions of roles and responsibilities for performing activities in Requirement 11 are documented and assigned.
- "11.1.2.b": Interview personnel with responsibility for performing activities in Requirement 11 to verify that roles and responsibilities are assigned as documented and are understood. 11.2 Wireless access points are identified and monitored, and unauthorized wireless access points are addressed.
**Customized Approach Objective:**Day-to-day responsibilities for performing all the activities in Requirement 11 are allocated. Personnel are accountable for successful, continuous operation of these requirements.
**Guidance - Purpose:**If roles and responsibilities are not formally assigned, personnel may not be aware of their day-to-day responsibilities and critical activities may not occur.
**Guidance - Good Practice:**Roles and responsibilities may be documented within policies and procedures or maintained within separate documents. As part of communicating roles and responsibilities, entities can consider having personnel acknowledge their acceptance and understanding of their assigned roles and responsibilities.
**Guidance - Examples:** A method to document roles and responsibilities is a responsibility assignment matrix that includes who is responsible, accountable, consulted, and informed (also called a RACI matrix).

================

### A. Tài liệu gốc của Requirement 11

### B. Summary Overview của Control Objective 11.2
Tài liệu này mô tả chi tiết **Control Objective 11.2** của **Requirement 11 **trong **PCI-DSS v4.0.1**, tập trung vào việc phát hiện và quản lý các wireless access point nhằm ngăn chặn truy cập trái phép vào mạng.
Mục tiêu chính là đảm bảo các wireless access point (cả được ủy quyền và không được ủy quyền) được phát hiện, kiểm soát và xử lý kịp thời.
Gồm 2 sub-requirement chính:
- 11.2.1: Phát hiện và kiểm soát wireless access point
- 11.2.2: Quản lý inventory wireless access point
Áp dụng cho toàn bộ môi trường mạng, kể cả khi tổ chức có chính sách cấm sử dụng công nghệ không dây

### C. Key Points của Control Objective 11.2
- **Phạm vi áp dụng:**Tất cả môi trường mạng và các thiết bị có khả năng kết nối không dây
- **Trách nhiệm**: Tài liệu hóa và triển khai quy trình kiểm tra để phát hiện cả thiết bị được phép và không được phép
- **Quản lý tài liệu / cấu hình:**Duy trì inventory các access point hợp lệ kèm theo lý do nghiệp vụ (business justification) rõ ràng
- **Kiểm soát / bảo vệ:**Thực hiện kiểm tra định kỳ ít nhất 3 tháng một lần hoặc sử dụng các công cụ giám sát tự động như NAC, wireless IDS/IPS để tạo cảnh báo tức thì

### D. Deep Summary của Control Objective 11.2
**Bối cảnh:**
Wireless là một trong những điểm xâm nhập phổ biến của kẻ tấn công do dễ triển khai và khó kiểm soát; các thiết bị không dây trái phép có thể được ẩn giấu bên trong hệ thống để tạo lối vào "tàng hình"
**Nội dung cốt lõi:**
- Kiểm tra định kỳ: Thực hiện rà soát để phát hiện sự hiện diện của các điểm truy cập Wi-Fi trong môi trường mạng
- Phân loại thiết bị: Phải nhận diện và phân biệt chính xác giữa thiết bị được ủy quyền (authorized) và thiết bị lạ (unauthorized/rogue AP)
- Phương pháp linh hoạt: Sử dụng quét mạng không dây, kiểm tra vật lý/logic các thành phần hạ tầng hoặc các giải pháp tự động
- Tài liệu hóa inventory: Duy trì danh sách các thiết bị hợp lệ để hỗ trợ quản trị viên phản ứng nhanh khi phát hiện thiết bị lạ
**Dữ liệu đáng chú ý:**
- Tần suất kiểm tra tối thiểu 3 tháng/lần
- Áp dụng ngay cả khi có policy cấm wireless
**Rủi ro / Lưu ý:**
- Rogue AP → mở đường cho attacker truy cập mạng nội bộ
- Không phát hiện wireless → mất kiểm soát truy cập
- Không có inventory → không phân biệt được thiết bị hợp lệ
- Thiếu giám sát → attacker có thể tồn tại lâu trong hệ thống

### E. Structured Output của Control Objective 11.2
**Control objectives:**11.2
**Sub-requirement:**11.2.1
**Defined Approach Requirements:**Authorized and unauthorized wireless access points are managed as follows:
• The presence of wireless (Wi-Fi) access points is tested for,
• All authorized and unauthorized wireless access points are detected and identified,
• Testing, detection, and identification occurs at least once every three months.
• If automated monitoring is used, personnel are notified via generated alerts. 11.3 External and internal vulnerabilities are regularly identified, prioritized, and addressed.
**Defined Approach Testing Procedures:**
- "11.2.1.a": Examine policies and procedures to verify processes are defined for managing both authorized and unauthorized wireless access points with all elements specified in this requirement.
- "11.2.1.b": Examine the methodology(ies) in use and the resulting documentation, and interview personnel to verify processes are defined to detect and identify both authorized and unauthorized wireless access points in accordance with all elements specified in this requirement.
- "11.2.1.c": Examine wireless assessment results and interview personnel to verify that wireless assessments were conducted in accordance with all elements specified in this requirement.
- "11.2.1.d": If automated monitoring is used, examine configuration settings to verify the configuration will generate alerts to notify personnel.
**Customized Approach Objective:**Unauthorized wireless access points are identified and addressed periodically.
**Applicability Notes:**The requirement applies even when a policy exists that prohibits the use of wireless technology. Methods used to meet this requirement must be sufficient to detect and identify both authorized and unauthorized devices, including unauthorized devices attached to devices that themselves are authorized.
**Guidance - Purpose:**Implementation and/or exploitation of wireless technology within a network are common paths for malicious users to gain unauthorized access to the network and cardholder data. Unauthorized wireless devices could be hidden within or attached to a computer or other system component. These devices could also be attached directly to a network port, to a network device such as a switch or router, or inserted as a wireless interface card inside a system component. Even if a company has a policy prohibiting the use of wireless technologies, an unauthorized wireless device or network could be installed without the company's knowledge, allowing an attacker to enter the network easily and 'invisibly.' Detecting and removing such unauthorized access points reduces the duration and likelihood of such devices being leveraged for an attack.
**Guidance - Good Practice:**The size and complexity of an environment will dictate the appropriate tools and processes to be used to provide sufficient assurance that a rogue wireless access point has not been installed in the environment. For example, performing a detailed physical inspection of a single stand-alone retail kiosk in a shopping mall, where all communication components are contained within tamper-resistant and tamper-evident casings, may be sufficient to provide assurance that a rogue wireless access point has not been attached or installed. However, in an environment with multiple nodes (such as in a large retail store, call center, server room or data center), detailed physical inspection can be difficult. In this case, multiple methods may be combined, such as performing physical system inspections in conjunction with the results of a wireless analyzer.
**Guidance - Definitions:**This is also referred to as rogue access point detection.
**Guidance - Examples:**Methods that may be used include but are not limited to wireless network scans, physical/logical inspections of system components and infrastructure, network access control (NAC), or wireless IDS/IPS. NAC and wireless IDS/IPS are examples of automated monitoring tools.

---
**Control objectives:**11.2
**Sub-requirement:**11.2.2
**Defined Approach Requirements:**An inventory of authorized wireless access points is maintained, including a documented business justification.
**Defined Approach Testing Procedures:**Examine documentation to verify that an inventory of authorized wireless access points is maintained, and a business justification is documented for all authorized wireless access points.
**Customized Approach Objective:**Unauthorized wireless access points are not mistaken for authorized wireless access points.
**Guidance - Purpose:** An inventory of authorized wireless access points can help administrators quickly respond when unauthorized wireless access points are detected. This helps to proactively minimize the exposure of CDE to malicious individuals.
**Guidance - Good Practice:** If using a wireless scanner, it is equally important to have a defined list of known access points which, while not attached to the company's network, will usually be detected during a scan. These non-company devices are often found in multi-tenant buildings or businesses located near one another. However, it is important to verify that these devices are not connected to the entity's network port or through another network-connected device and given an SSID resembling a nearby business. Scan results should note such devices and how it was determined that these devices could be "ignored." In addition, detection of any unauthorized wireless access points that are determined to be a threat to the CDE should be managed following the entity's incident response plan per Requirement 12.10.1.

================

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

================

### A. Tài liệu gốc của Requirement 11

### B. Summary Overview của Control Objective 11.4
Tài liệu này mô tả chi tiết **Control Objective 11.4** của **Requirement 11** trong **PCI-DSS v4.0.1**, tập trung vào việc thực hiện penetration testing để đánh giá khả năng phòng thủ của hệ thống trước các tấn công thực tế.
Mục tiêu chính là đảm bảo các lỗ hổng có thể khai thác được được phát hiện thông qua kiểm thử mô phỏng tấn công và được khắc phục kịp thời.
Gồm 7 sub-requirement chính:
- 11.4.1: Xây dựng phương pháp pentest
- 11.4.2: Thực hiện internal pentest
- 11.4.3: Thực hiện external pentest
- 11.4.4: Khắc phục lỗ hổng
- 11.4.5: Kiểm thử segmentation
- 11.4.6: Segmentation cho Service Provider
- 11.4.7: Hỗ trợ Multi-tenant Service Provider
Áp dụng cho toàn bộ hệ thống, mạng và CDE trong môi trường.

### C. Key Points của Control Objective 11.4
- **Phạm vi áp dụng:**Toàn bộ hệ thống, ứng dụng và môi trường dữ liệu chủ thẻ (CDE)
- **Trách nhiệm:**Tài liệu hóa phương pháp và thực hiện kiểm thử bởi nhân sự có năng lực, đảm bảo tính độc lập về mặt tổ chức
- **Phương pháp:**Áp dụng các phương pháp kiểm thử theo chuẩn công nghiệp như OWASP hoặc OSSTMM
- **Kiểm thử định kỳ:**Thực hiện ít nhất mỗi 12 tháng và ngay sau khi có các thay đổi lớn về hạ tầng hoặc ứng dụng

### D. Deep Summary của Control Objective 11.4
**Bối cảnh:**
Penetration testing giúp mô phỏng hành vi của kẻ tấn công thực tế để phát hiện các điểm yếu và chuỗi khai thác mà các phương pháp quét tự động không thể nhận diện được
**Nội dung cốt lõi:**
- Phương pháp toàn diện: Phải xây dựng methodology bao quát cả lớp mạng (network layer) và lớp ứng dụng (application layer)
- Kiểm thử đa chiều: Thực hiện đánh giá từ cả bên trong và bên ngoài mạng, bao gồm cả các hệ thống quan trọng và điểm biên CDE
- Xác minh phân tách: Kiểm tra tính hiệu quả của các biện pháp chia phân vùng (segmentation) để đảm bảo các hệ thống ngoài phạm vi không thể truy cập vào CDE
- Khắc phục và tái kiểm tra: Các lỗ hổng phát hiện được phải được xử lý dựa trên đánh giá rủi ro và thực hiện kiểm thử lại để xác nhận kết quả khắc phục
**Dữ liệu đáng chú ý:**
- Kết quả kiểm thử và hoạt động khắc phục lỗ hổng phải được lưu giữ ít nhất 12 tháng
- Đối với Service Provider, việc kiểm thử segmentation phải thực hiện ít nhất 6 tháng một lần
**Rủi ro / Lưu ý:**
- Chỉ thực hiện quét (scan) mà không thực hiện khai thác thử nghiệm (exploit) sẽ dẫn đến việc đánh giá thiếu hiệu quả và bỏ sót lỗ hổng thực tế
- Nếu không kiểm tra tính hiệu quả của segmentation, tổ chức dễ bị tấn công leo thang hoặc di chuyển ngang (lateral movement) từ các vùng mạng kém an toàn
- Việc sử dụng tester không đủ năng lực hoặc không có tính độc lập sẽ khiến kết quả kiểm thử không khách quan và không đáng tin cậy

### E. Structured Output của Control Objective 11.4
**Control objectives:**11.4
**Sub-requirement:**11.4.1
**Defined Approach Requirements:**A penetration testing methodology is defined, documented, and implemented by the entity, and includes:
• Industry-accepted penetration testing approaches.
• Coverage for the entire CDE perimeter and critical systems.
• Testing from both inside and outside the network.
• Testing to validate any segmentation and scope- reduction controls.
• Application-layer penetration testing to identify, at a minimum, the vulnerabilities listed in Requirement 6.2.4.
• Network-layer penetration tests that encompass all components that support network functions as well as operating systems.
• Review and consideration of threats and vulnerabilities experienced in the last 12 months.
• Documented approach to assessing and addressing the risk posed by exploitable vulnerabilities and security weaknesses found during penetration testing. Retention of penetration testing results and remediation activities results for at least 12 months.
**Defined Approach Testing Procedures:**Examine documentation and interview personnel to verify that the penetration-testing methodology defined, documented, and implemented by the entity includes all elements specified in this requirement.
**Customized Approach Objective:**A formal methodology is defined for thorough technical testing that attempts to exploit vulnerabilities and security weaknesses via simulated attack methods by a competent manual attacker.
**Applicability Notes:** Testing from inside the network (or 'internal penetration testing') means testing from both inside the CDE and into the CDE from trusted and untrusted internal networks. Testing from outside the network (or 'external penetration testing') means testing the exposed external perimeter of trusted networks, and critical systems connected to or accessible to public network infrastructures.
**Guidance - Purpose:**Attackers spend a lot of time finding external and internal vulnerabilities to leverage to obtain access to cardholder data and then to exfiltrate that data. As such, entities need to test their networks thoroughly, just as an attacker would do. This testing allows the entity to identify and remediate weakness that might be leveraged to compromise the entity's network and data, and then to take appropriate actions to protect the network and system components from such attacks.
**Guidance - Good Practice:**Penetration testing techniques will differ based on an organization's needs and structure and should be suitable for the tested environment-for example, fuzzing, injection, and forgery tests might be appropriate. The type, depth, and complexity of the testing will depend on the specific environment and the needs of the organization.
**Guidance - Definitions:**Penetration tests simulate a real-world attack situation intending to identify how far an attacker could penetrate an environment, given differing amounts of information provided to the tester. This allows an entity to better understand its potential exposure and develop a strategy to defend against attacks. A penetration test differs from a vulnerability scan, as a penetration test is an active process that usually includes exploiting identified vulnerabilities.
Scanning for vulnerabilities alone is not a penetration test, nor is a penetration test adequate if the focus is solely on trying to exploit vulnerabilities found in a vulnerability scan. Conducting a vulnerability scan may be one of the first steps, but it is not the only step a penetration tester will perform to plan the testing strategy. Even if a vulnerability scan does not detect known vulnerabilities, the penetration tester will often gain enough knowledge about the system to identify possible security gaps. Penetration testing is a highly manual process. While some automated tools may be used, the tester uses their knowledge of systems to gain access into an environment. Often the tester will chain several types of exploits together with the goal of breaking through layers of defenses. For example, if the tester finds a way to gain access to an application server, the tester will then use the compromised server as a point to stage a new attack based on the resources to which the server has access. In this way, a tester can simulate the techniques used by an attacker to identify areas of potential weakness in the environment. The testing of security monitoring and detection methods-for example, to confirm the effectiveness of logging and file integrity monitoring mechanisms, should also be considered. Scanning for vulnerabilities alone is not a penetration test, nor is a penetration test adequate if the focus is solely on trying to exploit vulnerabilities found in a vulnerability scan. Conducting a vulnerability scan may be one of the first steps, but it is not the only step a penetration tester will perform to plan the testing strategy. Even if a vulnerability scan does not detect known vulnerabilities, the penetration tester will often gain enough knowledge about the system to identify possible security gaps. Penetration testing is a highly manual process. While some automated tools may be used, the tester uses their knowledge of systems to gain access into an environment. Often the tester will chain several types of exploits together with the goal of breaking through layers of defenses. For example, if the tester finds a way to gain access to an application server, the tester will then use the compromised server as a point to stage a new attack based on the resources to which the server has access. In this way, a tester can simulate the techniques used by an attacker to identify areas of potential weakness in the environment. The testing of security monitoring and detection methods-for example, to confirm the effectiveness of logging and file integrity monitoring mechanisms, should also be considered.
**Guidance - Further Information:**Refer to the Information Supplement: Penetration Testing Guidance for additional guidance. Industry-accepted penetration testing approaches include: The Open Source Security Testing Methodology and Manual (OSSTMM) Open Web Application Security Project (OWASP) penetration testing programs.

---
**Control objectives:**11.4
**Sub-requirement:**11.4.2
**Defined Approach Requirements:**Internal penetration testing is performed:
• Per the entity's defined methodology,
• At least once every 12 months
• After any significant infrastructure or application upgrade or change
• By a qualified internal resource or qualified external third-party
• Organizational independence of the tester exists (not required to be a QSA or ASV).
**Defined Approach Testing Procedures:**
- "11.4.2.a": Examine the scope of work and results from the most recent internal penetration test to verify that penetration testing is performed in accordance with all elements specified in this requirement.
- "11.4.2.b": Interview personnel to verify that the internal penetration test was performed by a qualified internal resource or qualified external third-party and that organizational independence the tester exists (not required to be a QSA or ASV).
**Customized Approach Objective:**Internal system defenses are verified by technical testing according to the entity's defined methodology as frequently as needed to address evolving and new attacks and threats and ensure that significant changes do not introduce unknown vulnerabilities.
**Guidance - Purpose:**Internal penetration testing serves two purposes. Firstly, just like an external penetration test, it discovers vulnerabilities and misconfigurations that could be used by an attacker that had managed to get some degree of access to the internal network, whether that is because the attacker is an authorized user conducting unauthorized activities, or an external attacker that had managed to penetrate the entity's perimeter. Secondly, internal penetration testing also helps entities to discover where their change control process failed by detecting previously unknown systems. Additionally, it verifies the status of many of the controls operating within the CDE. A penetration test is not truly a 'test' because the outcome of a penetration test is not something that can be classified as a 'pass' or a 'fail.' The best outcome of a test is a catalog of vulnerabilities and misconfigurations that an entity did not know about, and the penetration tester found them before an attacker could. A penetration test that found nothing is typically indicative of shortcomings of the penetration tester, rather than being a positive reflection of the security posture of the entity.
**Guidance - Good Practice:**Some considerations when choosing a qualified resource to perform penetration testing include:
• Specific penetration testing certifications, which may be an indication of the tester's skill level and competence.
• Prior experience conducting penetration testing—for example, the number of years of experience, and the type and scope of prior engagements can help confirm whether the tester's experience is appropriate for the needs of the engagement.
**Guidance - Further Information:** Refer to the Information Supplement: Penetration Testing Guidance on the PCI SSC website for additional guidance.

---
**Control objectives:**11.4
**Sub-requirement:**11.4.3
**Defined Approach Testing Procedures:**
- "11.4.3.a": Examine the scope of work and results from the most recent external penetration test to verify that penetration testing is performed according to all elements specified in this requirement.
- "11.4.3.b": Interview personnel to verify that the external penetration test was performed by a qualified internal resource or qualified external third party and that organizational independence of the tester exists (not required to be a QSA or ASV).
**Customized Approach Objective:** External system defenses are verified by technical testing according to the entity's defined methodology as frequently as needed to address evolving and new attacks and threats, and to ensure that significant changes do not introduce unknown vulnerabilities.
**Guidance - Purpose:**Internal penetration testing serves two purposes. Firstly, just like an external penetration test, it discovers vulnerabilities and misconfigurations that could be used by an attacker that had managed to get some degree of access to the internal network, whether that is because the attacker is an authorized user conducting unauthorized activities, or an external attacker that had managed to penetrate the entity's perimeter. Secondly, internal penetration testing also helps entities to discover where their change control process failed by detecting previously unknown systems. Additionally, it verifies the status of many of the controls operating within the CDE. A penetration test is not truly a 'test' because the outcome of a penetration test is not something that can be classified as a 'pass' or a 'fail.' The best outcome of a test is a catalog of vulnerabilities and misconfigurations that an entity did not know about, and the penetration tester found them before an attacker could. A penetration test that found nothing is typically indicative of shortcomings of the penetration tester, rather than being a positive reflection of the security posture of the entity.
**Guidance - Good Practice:**Some considerations when choosing a qualified resource to perform penetration testing include:
• Specific penetration testing certifications, which may be an indication of the tester's skill level and competence.
• Prior experience conducting penetration testing—for example, the number of years of experience, and the type and scope of prior engagements can help confirm whether the tester's experience is appropriate for the needs of the engagement.
**Guidance - Further Information:** Refer to the Information Supplement: Penetration Testing Guidance on the PCI SSC website for additional guidance.

---
**Control objectives:**11.4
**Sub-requirement:**11.4.4
**Defined Approach Requirements:**Exploitable vulnerabilities and security weaknesses found during penetration testing are corrected as follows:
• In accordance with the entity's assessment of the risk posed by the security issue as defined in Requirement 6.3.1.
• Penetration testing is repeated to verify the corrections. Customized Approach Objective Vulnerabilities and security weaknesses found while verifying system defenses are mitigated.
**Defined Approach Testing Procedures:**Examine penetration testing results to verify that noted exploitable vulnerabilities and security weaknesses were corrected in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Vulnerabilities and security weaknesses found while verifying system defenses are mitigated.
**Guidance - Purpose:**The results of a penetration test are usually a prioritized list of vulnerabilities discovered by the exercise. Often a tester will have chained a number of vulnerabilities together to compromise a system component. Remediating the vulnerabilities found by a penetration test significantly reduces the probability that the same vulnerabilities will be exploited by a malicious attacker. Using the entity's own vulnerability risk assessment process (see requirement 6.3.1) ensures that the vulnerabilities that pose the highest risk to the entity will be remediated more quickly.
**Guidance - Good Practice:**As part of the entity's assessment of risk, entities should consider how likely the vulnerability is to be exploited and whether there are other controls present in the environment to reduce the risk. Any weaknesses that point to PCI DSS requirements not being met should be addressed.

---
**Control objectives:**11.4
**Sub-requirement:**11.4.5
**Defined Approach Requirements:**If segmentation is used to isolate the CDE from other networks, penetration tests are performed on segmentation controls as follows:
• At least once every 12 months and after any changes to segmentation controls/methods
• Covering all segmentation controls/methods in use.
• According to the entity's defined penetration testing methodology.
• Confirming that the segmentation controls/methods are operational and effective, and isolate the CDE from all out-of-scope systems.
• Confirming effectiveness of any use of isolation to separate systems with differing security levels (see Requirement 2.2.3).
• Performed by a qualified internal resource or qualified external third party.
• Organizational independence of the tester exists (not required to be a QSA or ASV).
**Defined Approach Testing Procedures:**
- "11.4.5.a": Examine segmentation controls and review penetration-testing methodology to verify that penetration-testing procedures are defined to test all segmentation methods in accordance with all elements specified in this requirement.
- "11.4.5.b": Examine the results from the most recent penetration test to verify the penetration test covers and addresses all elements specified in this requirement.
- "11.4.5.c": Interview personnel to verify that the test was performed by a qualified internal resource or qualified external third party and that organizational independence of the tester exists (not required to be a QSA or ASV).
**Customized Approach Objective:**If segmentation is used, it is verified periodically by technical testing to be continually effective, including after any changes, in isolating the CDE from all out-of-scope systems.
**Guidance - Purpose:**When an entity uses segmentation controls to isolate the CDE from internal untrusted networks, the security of the CDE is dependent on that segmentation functioning. Many attacks have involved the attacker moving laterally from what an entity deemed an isolated network into the CDE. Using penetration testing tools and techniques to validate that an untrusted network is indeed isolated from the CDE can alert the entity to a failure or misconfiguration of the segmentation controls, which can then be rectified.
**Guidance - Good Practice:**Techniques such as host discovery and port scanning can be used to verify out-of-scope segments have no access to the CDE.

---
**Control objectives:**11.4
**Sub-requirement:**11.4.6
**Defined Approach Requirements:**Additional requirement for service providers only: If segmentation is used to isolate the CDE from other networks, penetration tests are performed on segmentation controls as follows:
• At least once every six months and after any changes to segmentation controls/methods.
• Covering all segmentation controls/methods in use.
• According to the entity's defined penetration testing methodology.
• Confirming that the segmentation controls/methods are operational and effective, and isolate the CDE from all out-of-scope systems.
• Confirming effectiveness of any use of isolation to separate systems with differing security levels (see Requirement 2.2.3).
• Performed by a qualified internal resource or qualified external third party.
• Organizational independence of the tester exists (not required to be a QSA or ASV).
**Defined Approach Testing Procedures:**
- "11.4.6.a": Additional testing procedure for service provider assessments only: Examine the results from the most recent penetration test to verify that the penetration covers and addressed all elements specified in this requirement.
- "11.4.6.b": Additional testing procedure for service provider assessments only: Interview personnel to verify that the test was performed by a qualified internal resource or qualified external third party and that organizational independence of the tester exists (not required to be a QSA or ASV).
**Customized Approach Objective:** If segmentation is used, it is verified by technical testing to be continually effective, including after any changes, in isolating the CDE from out-of-scope systems.
**Applicability Notes:** This requirement applies only when the entity being assessed is a service provider.
**Guidance - Purpose:**Service providers typically have access to greater volumes of cardholder data or can provide an entry point that can be exploited to then compromise multiple other entities. Service providers also typically have larger and more complex networks that are subject to more frequent change. The probability of segmentation controls failing in complex and dynamic networks is greater in service-provider environments. Validating segmentation controls more frequently is likely to discover such failings before they can be exploited by an attacker attempting to pivot laterally from an out-of-scope untrusted network to the CDE.
**Guidance - Good Practice:**Although the requirement specifies that this scope validation is carried out at least once every six months and after significant change, this exercise should be performed as frequently as possible to ensure it remains effective at isolating the CDE from other networks.

---
**Control objectives:**11.4
**Sub-requirement:**11.4.7
**Defined Approach Requirements:**Additional requirement for multi-tenant service providers only: Multi-tenant service providers support their customers for external penetration testing per Requirement 11.4.3 and 11.4.4.
**Defined Approach Testing Procedures:**Additional testing procedure for multi- tenant service providers only: Examine evidence to verify that multi-tenant service providers support their customers for external penetration testing Requirement 11.4.3 and 11.4.4.
**Customized Approach Objective:**Multi-tenant service providers support their customers' need for technical testing either by providing access or evidence that comparable technical testing has been undertaken.
**Applicability Notes:**This requirement applies only when the entity being assessed is a multi-tenant service provider. To meet this requirement, a multi-tenant service provider may either:
• Provide evidence to its customers to show that penetration testing has been performed according to Requirements 11.4.3 and 11.4.4 on the customers' subscribed infrastructure, or
• Provide prompt access to each of its customers, so customers can perform their own penetration testing.
Evidence provided to customers can include redacted penetration testing results but needs to include sufficient information to prove that all elements of Requirements 11.4.3 and 11.4.4 have been met on the customer's behalf. Refer also to Appendix A1: Additional PCI DSS Requirements for Multi-Tenant Service Providers . This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Entities need to conduct penetration tests in accordance with PCI DSS to simulate attacker behavior and discover vulnerabilities in their environment. In shared and cloud environments, the multi-tenant service provider may be concerned about the activities of a penetration tester affecting other customers' systems. Multi-tenant service providers cannot forbid penetration testing because this would leave their customers' systems open to exploitation. Therefore, multi-tenant service providers must support customer requests to conduct penetration testing or for penetration testing results.

================

### A. Tài liệu gốc của Requirement 11

### B. Summary Overview của Control Objective 11.5
Tài liệu này mô tả chi tiết** Control Objective 11.5 **của **Requirement 11 **trong** PCI-DSS v4.0.1**, tập trung vào việc phát hiện xâm nhập và thay đổi trái phép trong hệ thống.
Mục tiêu chính là đảm bảo các hoạt động bất thường, xâm nhập và thay đổi trái phép được phát hiện kịp thời và có cơ chế cảnh báo để xử lý.
Gồm 2 sub-requirement chính:
- 11.5.1: Phát hiện và ngăn chặn xâm nhập (IDS/IPS)
- 11.5.2: Phát hiện thay đổi file (FIM/change-detection)
Áp dụng cho toàn bộ hệ thống, đặc biệt tại các điểm quan trọng trong CDE.

### C. Key Points của Control Objective 11.5
- **Phạm vi áp dụng:**Network traffic và critical file trong hệ thống
- **Trách nhiệm:**Triển khai và duy trì cơ chế phát hiện xâm nhập và thay đổi
- **Giám sát mạng:**Monitor traffic tại perimeter và các điểm quan trọng
- **Cảnh báo:**Phải alert khi có dấu hiệu compromise
- **Cập nhật hệ thống:**IDS/IPS phải được cập nhật signature và baseline
- **Giám sát file:**Áp dụng FIM để phát hiện thay đổi file critical
- **Tần suất kiểm tra:**So sánh file ít nhất hàng tuần

### D. Deep Summary của Control Objective 11.5
**Bối cảnh:**
Các cuộc tấn công thường diễn ra âm thầm trong thời gian dài. Nếu không có cơ chế phát hiện, tổ chức sẽ không nhận biết được xâm nhập hoặc thay đổi trái phép.
**Nội dung cốt lõi:**
- Triển khai IDS/IPS để phát hiện và/hoặc ngăn chặn xâm nhập
- Giám sát toàn bộ traffic tại perimeter và các điểm quan trọng
- Cảnh báo cho nhân sự khi phát hiện dấu hiệu bất thường
- Cập nhật engine, signature và baseline liên tục
- Triển khai FIM để phát hiện thay đổi file critical
- So sánh file định kỳ và alert khi có thay đổi trái phép
**Dữ liệu đáng chú ý:**
- IDS/IPS có thể phát hiện theo signature hoặc behavior
- FIM phải kiểm tra file critical ít nhất hàng tuần
**Rủi ro / Lưu ý:**
- Không có IDS/IPS → không phát hiện xâm nhập
- Không cập nhật signature → không detect attack mới
- Không có FIM → không phát hiện thay đổi hệ thống
- Không monitor alert → bỏ lỡ sự cố bảo mật

### E. Structured Output của Control Objective 11.5
**Control objectives:**11.5
**Sub-requirement:**11.5.1
**Defined Approach Requirements:**Intrusion-detection and/or intrusion- prevention techniques are used to detect and/or prevent intrusions into the network as follows:
• All traffic is monitored at the perimeter of the CDE.
• All traffic is monitored at critical points in the CDE.
• Personnel are alerted to suspected compromises.
• All intrusion-detection and prevention engines, baselines, and signatures are kept up to date.
**Defined Approach Testing Procedures:**
- "11.5.1.a": Examine system configurations and network diagrams to verify that intrusion-detection and/or intrusion-prevention techniques are in place to monitor all traffic:
• At the perimeter of the CDE.
• At critical points in the CDE.
- "11.5.1.b": Examine system configurations and interview responsible personnel to verify intrusion- detection and/or intrusion-prevention techniques alert personnel of suspected compromises.
- "11.5.1.c": Examine system configurations and vendor documentation to verify intrusion-detection and/or intrusion-prevention techniques are configured to keep all engines, baselines, and signatures up to date.
**Customized Approach Objective:**Mechanisms to detect real-time suspicious or anomalous network traffic that may be indicative of threat actor activity are implemented. Alerts generated by these mechanisms are responded to by personnel, or by automated means that ensure that system components cannot be compromised as a result of the detected activity.
**Guidance - Purpose:**Intrusion-detection and/or intrusion-prevention techniques (such as IDS/IPS) compare the traffic coming into the network with known 'signatures' and/or behaviors of thousands of compromise types (hacker tools, Trojans, and other malware), and then send alerts and/or stop the attempt as it happens. Without a proactive approach to detect unauthorized activity, attacks on (or misuse of) computer resources could go unnoticed for long periods of time. The impact of an intrusion into the CDE is, in many ways, a factor of the time that an attacker has in the environment before being detected.
**Guidance - Good Practice:**Security alerts generated by these techniques should be continually monitored, so that the attempted or actual intrusions can be stopped, and potential damage limited.
**Guidance - Definitions:**Critical locations could include, but are not limited to, network security controls between network segments (for example, between a DMZ and an internal network or between an in-scope and out- of-scope network) and points protecting connections between a less trusted and a more trusted system component.

---
**Control objectives:**11.5
**Sub-requirement:**11.5.1.1
**Defined Approach Requirements:**Additional requirement for service providers only: Intrusion-detection and/or intrusion-prevention techniques detect, alert on/prevent, and address covert malware communication channels.
**Defined Approach Testing Procedures:**
- "11.5.1.1.a": Additional testing procedure for service provider assessments only: Examine documentation and configuration settings to verify that methods to detect and alert on/prevent covert malware communication channels are in place and operating.
- "11.5.1.1.b": Additional testing procedure for service provider assessments only: Examine the entity's incident-response plan (Requirement 12.10.1) to verify it requires and defines a response in the event that covert malware communication channels are detected.
- "11.5.1.1.c": Additional testing procedure for service provider assessments only: Interview responsible personnel and observe processes to verify that personnel maintain knowledge of covert malware communication and control techniques and are knowledgeable about how to respond when malware is suspected.
**Customized Approach Objective:**Mechanisms are in place to detect and alert/prevent covert communications with command-and-control systems. Alerts generated by these mechanisms are responded to by personnel, or by automated means that ensure that such communications are blocked.
**Applicability Notes:**This requirement applies only when the entity being assessed is a service provider. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Detecting covert malware communication attempts (for example, DNS tunneling) can help block the spread of malware laterally inside a network and the exfiltration of data. When deciding where to place this control, entities should consider critical locations in the network, and likely routes for covert channels. When malware establishes a foothold in an infected environment, it often tries to establish a communication channel to a command-and- control (C&C) server. Through the C&C server, the attacker communicates with and controls malware on compromised systems to deliver malicious payloads or instructions, or to initiate data exfiltration. In many cases, the malware will communicate with the C&C server indirectly via botnets, bypassing monitoring, blocking controls, and rendering these methods ineffective to detect the covert channels.
**Guidance - Good Practice:**Methods that can help detect and address malware communications channels include real- time endpoint scanning, egress traffic filtering, an 'allow' listing, data loss prevention tools, and network security monitoring tools such as IDS/IPS. Additionally, DNS queries and responses are a key data source used by network defenders in support of incident response as well as intrusion discovery. When these transactions are collected for processing and analytics, they can enable a number of valuable security analytic scenarios. It is important that organizations maintain up-to- date knowledge of malware modes of operation, as mitigating these can help detect and limit the impact of malware in the environment.

---
**Control objectives:**11.5
**Sub-requirement:**11.5.2
**Defined Approach Requirements:**A change-detection mechanism (for example, file integrity monitoring tools) is deployed as follows:
• To alert personnel to unauthorized modification (including changes, additions, and deletions) of critical files.
• To perform critical file comparisons at least once weekly.
**Defined Approach Testing Procedures:**
- "11.5.2.a": Examine system settings, monitored files, and results from monitoring activities to verify the use of a change-detection mechanism.
- "11.5.2.b": Examine settings for the change-detection mechanism to verify it is configured in accordance with all elements specified in this requirement. 11.6 Unauthorized changes on payment pages are detected and responded to.
**Customized Approach Objective:**Critical files cannot be modified by unauthorized personnel without an alert being generated.
**Applicability Notes:**For change-detection purposes, critical files are usually those that do not regularly change, but the modification of which could indicate a system compromise or risk of compromise. Change- detection mechanisms such as file integrity monitoring products usually come pre-configured with critical files for the related operating system. Other critical files, such as those for custom applications, must be evaluated and defined by the entity (that is, the merchant or service provider).
**Guidance - Purpose:**Changes to critical system, configuration, or content files can be an indicator an attacker has accessed an organization's system. Such changes can allow an attacker to take additional malicious actions, access cardholder data, and/or conduct activities without detection or record. A change detection mechanism will detect and evaluate such changes to critical files and generate alerts that can be responded to following defined processes so that personnel can take appropriate actions.
If not implemented properly and the output of the change-detection solution monitored, a malicious individual could add, remove, or alter configuration file contents, operating system programs, or application executables. Unauthorized changes, if undetected, could render existing security controls ineffective and/or result in cardholder data being stolen with no perceptible impact to normal processing.
**Guidance - Good Practice:**Examples of the types of files that should be monitored include, but are not limited to:
• System executables.
• Application executables.
• Configuration and parameter files.
• Centrally stored, historical, or archived audit logs.
• Additional critical files determined by entity (for example, through risk assessment or other means).
**Guidance - Examples:**Change-detection solutions such as file integrity monitoring (FIM) tools check for changes, additions, and deletions to critical files, and notify when such changes are detected.

================

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