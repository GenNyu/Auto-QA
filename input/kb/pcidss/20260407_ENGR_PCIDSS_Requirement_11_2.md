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