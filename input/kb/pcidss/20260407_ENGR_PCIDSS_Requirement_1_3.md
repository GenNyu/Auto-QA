### A. Tài liệu gốc của Requirement 1

### B. Summary Overview của Control Objective 1.3
Tài liệu này mô tả chi tiết **Control Objective 1.3 **của **Requirement 1 **trong **PCI-DSS v4.0.1, **tập trung vào việc **Hạn chế lưu lượng mạng vào/ra CDE bằng NSCs**
Mục tiêu là chỉ cho phép lưu lượng cần thiết, từ chối toàn bộ lưu lượng không được phép (default deny), ngăn truy cập trái phép vào và ra khỏi CDE
Gồm 3 sub-requirement chính:
- 1.3.1: Kiểm soát inbound traffic
- 1.3.2: Kiểm soát outbound traffic
- 1.3.3: Phân tách wireless với CDE
Áp dụng cho toàn bộ lưu lượng mạng liên quan đến CDE

### C. Key Points của Control Objective 1.3
- **Inbound/Outbound:** Chỉ allow traffic cần thiết
- **Nguyên tắc:** Default deny
- **Wireless:** Phải tách biệt với CDE bằng NSCs
- **Kiểm soát:** Dựa trên ruleset (IP, port, protocol…)
- **Mục tiêu:** Ngăn truy cập trái phép và data exfiltration

### D. Deep Summary của Control Objective 1.3
**Bối cảnh:**
CDE thường bị tấn công từ mạng không tin cậy (Internet, wireless). Nếu không kiểm soát chặt lưu lượng mạng, attacker có thể truy cập trái phép hoặc đánh cắp dữ liệu.
**Nội dung cốt lõi:**
- **Kiểm soát inbound:**Chỉ cho phép lưu lượng cần thiết vào CDE, còn lại bị từ chối
- **Kiểm soát outbound:**Hạn chế lưu lượng ra ngoài để ngăn data exfiltration
- **Nguyên tắc mặc định:**Deny all, chỉ allow khi có business justification
- **Phân tách wireless:**Wireless network phải được cách ly và kiểm soát trước khi vào CDE
- **Thực thi kỹ thuật:**Áp dụng ruleset rõ ràng (IP, port, protocol, direction)
**Dữ liệu đáng chú ý:**
- Áp dụng cho toàn bộ traffic vào/ra CDE
- Bao gồm cả mạng wireless và mạng nội bộ
**Rủi ro / Lưu ý:**
- Không kiểm soát inbound → truy cập trái phép vào CDE
- Không kiểm soát outbound → rò rỉ dữ liệu
- Không tách wireless → attacker dễ xâm nhập
- Rule lỏng lẻo → tạo lỗ hổng bảo mật

### E. Structured Output của Control Objective 1.3
**Control objectives:**1.3
**Sub-requirement:** 1.3.1 *(Tag: inbound traffic filtering, firewall inbound rules, deny-by-default)*
**Defined Approach Requirements of 1.3.1:**Inbound traffic to the CDE is restricted as follows:
• To only traffic that is necessary.
• All other traffic is specifically denied.
**Defined Approach Testing Procedures of 1.3.1:**
- "1.3.1.a": Examine configuration standards for NSCs to verify that they define restricting inbound traffic to the CDE is in accordance with all elements specified in this requirement.
- "1.3.1.b": Examine configurations of NSCs to verify that inbound traffic to the CDE is restricted in accordance with all elements specified in this requirement.
**Customized Approach Objective of 1.3.1:**Unauthorized traffic cannot enter the CDE.
**Guidance - Purpose of 1.3.1:**This requirement aims to prevent malicious individuals from accessing the entity's network via unauthorized IP addresses or from using services, protocols, or ports in an unauthorized manner.
**Guidance - Good Practice of 1.3.1:**All traffic inbound to the CDE, regardless of where it originates, should be evaluated to ensure it follows established, authorized rules. Connections should be inspected to ensure traffic is restricted to only authorized communications-for example, by restricting source/destination addresses and ports, and blocking of content.
**Guidance - Examples of 1.3.1:**Implementing a rule that denies all inbound and outbound traffic that is not specifically needed- for example, by using an explicit 'deny all' or implicit deny after allow statement-helps to prevent inadvertent holes that would allow unintended and potentially harmful traffic.

---
**Control objectives:**1.3
**Sub-requirement:** 1.3.2 *(Tag: outbound traffic control, data exfiltration prevention, egress filtering)*
**Defined Approach Requirements of 1.3.2:**Outbound traffic from the CDE is restricted as follows:
• To only traffic that is necessary.
• All other traffic is specifically denied.
**Defined Approach Testing Procedures of 1.3.2:**
- "1.3.2.a": Examine configuration standards for NSCs to verify that they define restricting outbound traffic from the CDE in accordance with all elements specified in this requirement.
- "1.3.2.b": Examine configurations of NSCs to verify that outbound traffic from the CDE is restricted in accordance with all elements specified in this requirement.
**Customized Approach Objective of 1.3.2:**Unauthorized traffic cannot leave the CDE.
**Guidance - Purpose of 1.3.2:**This requirement aims to prevent malicious individuals and compromised system components within the entity's network from communicating with an untrusted external host.
**Guidance - Good Practice of 1.3.2:**All traffic outbound from the CDE, regardless of the destination, should be evaluated to ensure it follows established, authorized rules. Connections should be inspected to restrict traffic to only authorized communications-for example, by restricting source/destination addresses and ports, and blocking of content.
**Guidance - Examples of 1.3.2:**Implementing a rule that denies all inbound and outbound traffic that is not specifically needed- for example, by using an explicit 'deny all' or implicit deny after allow statement-helps to prevent inadvertent holes that would allow unintended and potentially harmful traffic.

---
**Control objectives:**1.3
**Sub-requirement:** 1.3.3 *(Tag: wireless network segmentation, WiFi isolation, CDE protection)*
**Defined Approach Requirements of 1.3.3:**NSCs are installed between all wireless networks and the CDE, regardless of whether the wireless network is a CDE, such that:
• All wireless traffic from wireless networks into the CDE is denied by default.
• Only wireless traffic with an authorized business is allowed into the CDE.
**Defined Approach Testing Procedures of 1.3.3:**
- "1.3.3": Examine configuration settings and network diagrams to verify that NSCs are implemented between all wireless networks and the CDE, in accordance with all elements specified in this requirement.
**Customized Approach Objective of 1.3.3:**Unauthorized traffic cannot traverse network boundaries between any wireless networks and wired environments in the CDE.
**Guidance - Purpose of 1.3.3:**The known (or unknown) implementation and exploitation of wireless technology within a network is a common path for malicious individuals to gain access to the network and account data. If a wireless device or network is installed without the entity's knowledge, a malicious individual could easily and "invisibly" enter the network. If NSCs do not restrict access from wireless networks into the CDE, malicious individuals that gain unauthorized access to the wireless network can easily connect to the CDE and compromise account information.