### A. Tài liệu gốc của Requirement 2

### B. Summary Overview của Control Objective 2.3
Tài liệu này mô tả chi tiết **Control Objective 2.3 **của **Requirement 2 **trong **PCI-DSS v4.0.1, **tập trung vào việc **Bảo mật môi trường mạng không dây (wireless) liên quan đến CDE**
Mục tiêu chính là ngăn truy cập trái phép qua wireless, loại bỏ cấu hình mặc định không an toàn, đảm bảo quản lý khóa mã hóa an toàn
Gồm 2 sub-requirement chính:
- 2.3.1: Thay đổi cấu hình mặc định wireless
- 2.3.2: Quản lý và thay đổi encryption keys
Áp dụng cho các mạng wireless kết nối vào CDE hoặc truyền dữ liệu thẻ

### C. Key Points của Control Objective 2.3

### Wireless security: Phải hardening thiết bị wireless

### Default config: Phải thay đổi hoặc đảm bảo an toàn

### SNMP / password / key: Không dùng mặc định

### Key management: Phải thay đổi khi cần

### Access control: Chỉ người có quyền mới biết key

### D. Deep Summary của Control Objective 2.3
**Bối cảnh:**
Mạng wireless dễ bị nghe lén và tấn công nếu cấu hình yếu hoặc dùng mặc định. 2.3 nhằm giảm rủi ro từ wireless khi kết nối vào CDE
**Nội dung cốt lõi:**
- Cấu hình an toàn: Thay đổi toàn bộ default settings (password, SNMP, key…)
- Bảo vệ truy cập: Ngăn truy cập bằng cấu hình mặc định
- Quản lý khóa: Thay đổi encryption key khi có nghi ngờ bị lộ hoặc nhân sự rời đi hoặc đổi role
- Kiểm soát truy cập: Chỉ người có business need được biết key
**Dữ liệu đáng chú ý:**
- Áp dụng cho mọi wireless kết nối CDE hoặc truyền account data
- Bao gồm access point, wireless network, encryption keys
**Rủi ro / Lưu ý:**
- Dùng default config → dễ bị truy cập trái phép
- Wireless sniffing → lộ dữ liệu và mật khẩu
- Key không thay đổi → bị reuse / compromise
- Không kiểm soát access → mở rộng attack surface

### E. Structured Output của Control Objective 2.3
**Control objectives:**2.3
**Sub-requirement:**2.3.1* (Tag: wireless security, default credentials, WiFi hardening, SNMP security)*
**Defined Approach Requirements of 2.3.1:**For wireless environments connected to the CDE or transmitting account data, all wireless vendor defaults are changed at installation or are confirmed to be secure, including but not limited to:
• Default wireless encryption keys.
• Passwords on wireless access points.
• SNMP defaults.
• Any other security-related wireless vendor defaults.
**Defined Approach Testing Procedures of 2.3.1:**
- "2.3.1.a": Examine policies and procedures and interview responsible personnel to verify that processes are defined for wireless vendor defaults to either change them upon installation or to confirm them to be secure in accordance with all elements of this requirement.
- "2.3.1.b": Examine vendor documentation and observe a system administrator logging into wireless devices to verify:
• SNMP defaults are not used.
• Default passwords/passphrases on wireless access points are not used.
- "2.3.1.c": Examine vendor documentation and configuration settings to verify other security-related wireless vendor defaults were changed, if applicable.
**Customized Approach Objective of 2.3.1:**Wireless networks cannot be accessed using vendor default passwords or default configurations.
**Applicability Notes of 2.3.1:**This includes, but is not limited to, default wireless encryption keys, passwords on wireless access points, SNMP defaults, and any other security-related wireless vendor defaults.
**Guidance - Purpose of 2.3.1:**If wireless networks are not implemented with sufficient security configurations (including changing default settings), wireless sniffers can eavesdrop on the traffic, easily capture data and passwords, and easily enter and attack the network.
**Guidance - Good Practice of 2.3.1:**Wireless passwords should be constructed so that they are resistant to offline brute force attacks.

---
**Control objectives:**2.3
**Sub-requirement:**2.3.2 *(Tag: key rotation, wireless encryption keys, key management, access revocation)*
**Defined Approach Requirements of 2.3.2:**For wireless environments connected to the CDE or transmitting account data, wireless encryption keys are changed as follows:
• Whenever personnel with knowledge of the key leave the company or the role for which the knowledge was necessary.
• Whenever a key is suspected of or known to be compromised. Customized Approach Objective Knowledge of wireless encryption keys cannot allow unauthorized access to wireless networks.
**Defined Approach Testing Procedures of 2.3.2:**Interview responsible personnel and examine key-management documentation to verify that wireless encryption keys are changed in accordance with all elements specified in this requirement.
**Customized Approach Objective of 2.3.2:**Knowledge of wireless encryption keys cannot allow unauthorized access to wireless networks.
**Guidance - Purpose of 2.3.2:**Changing wireless encryption keys whenever someone with knowledge of the key leaves the organization or moves to a role that no longer requires knowledge of the key, helps keep knowledge of keys limited to only those with a business need to know. Also, changing wireless encryption keys whenever a key is suspected or known to be comprised makes a wireless network more resistant to compromise.
**Guidance - Good Practice of 2.3.2:**This goal can be accomplished in multiple ways, including periodic changes of keys, changing keys via a defined 'joiners-movers-leavers' (JML) process, implementing additional technical controls, and not using fixed pre-shared keys. In addition, any keys that are known to be, or suspected of being, compromised should be managed in accordance with the entity's incident response plan at Requirement 12.10.1.