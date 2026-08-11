### A. Tài liệu gốc của Requirement 1

### B. Summary Overview của Control Objective 1.4
Tài liệu này mô tả chi tiết **Control Objective 1.4 **của **Requirement 1 **trong **PCI-DSS v4.0.1, **tập trung vào việc **Kiểm soát kết nối giữa mạng tin cậy (trusted) và không tin cậy (untrusted)**
Mục tiêu là ngăn truy cập trái phép từ mạng không tin cậy, kiểm soát chặt lưu lượng vào mạng nội bộ, bảo vệ CDE thông qua phân tách mạng
Gồm 5 sub-requirement chính:
- 1.4.1: Triển khai NSCs giữa trusted và untrusted
- 1.4.2: Kiểm soát inbound từ untrusted
- 1.4.3: Anti-spoofing
- 1.4.4: Không cho truy cập trực tiếp dữ liệu thẻ
- 1.4.5: Ẩn thông tin mạng nội bộ
Áp dụng cho tất cả kết nối giữa mạng nội bộ và bên ngoài (Internet, wireless, external networks)

### C. Key Points của Control Objective 1.4
- **Boundary control:**NSCs phải đặt giữa trusted & untrusted
- **Inbound control:**Chỉ allow traffic hợp lệ và stateful response
- **Segmentation:**Sử dụng DMZ để tách hệ thống public
- **Anti-spoofing:**Chặn IP giả mạo
- **Data protection:**Không cho truy cập trực tiếp vào nơi lưu cardholder data
- **Information hiding:**Ẩn IP nội bộ (NAT, proxy, filtering)

### D. Deep Summary của Control Objective 1.4
**Bối cảnh:**
Mạng không tin cậy (Internet, external, wireless) là nguồn tấn công chính vào hệ thống nội bộ. Nếu không kiểm soát ranh giới mạng, attacker có thể xâm nhập trực tiếp vào CDE.
**Nội dung cốt lõi:**
- **Kiểm soát ranh giới:**Triển khai NSCs giữa trusted và untrusted networks
- **Kiểm soát inbound:**Chỉ cho phép traffic được authorize hoặc stateful response
- **Phân tách hệ thống:**Sử dụng DMZ để cô lập hệ thống public-facing
- **Chống giả mạo:**Áp dụng anti-spoofing để chặn IP giả
- **Bảo vệ dữ liệu:**Không cho truy cập trực tiếp vào nơi lưu cardholder data
- **Ẩn thông tin mạng:**Hạn chế lộ IP nội bộ và routing
**Dữ liệu đáng chú ý:**
- Áp dụng cho mọi kết nối giữa trusted và untrusted networks
- Bao gồm Internet, wireless, external networks
**Rủi ro / Lưu ý:**
- Không có NSC tại boundary → truy cập trái phép
- Inbound không kiểm soát → mở cửa vào hệ thống
- Không có DMZ → tăng nguy cơ compromise toàn bộ mạng
- Không anti-spoofing → bị giả mạo nguồn
- Lộ IP nội bộ → hỗ trợ attacker phân tích hệ thống
- Truy cập trực tiếp DB → rủi ro lộ dữ liệu thẻ

### E. Structured Output của Control Objective 1.4
**Control objectives:**1.4
**Sub-requirement:** 1.4.1 *(Tag: DMZ, network segmentation, trusted-untrusted boundary)*
**Defined Approach Requirements of 1.4.1:**NSCs are implemented between trusted and untrusted networks.
**Defined Approach Testing Procedures of 1.4.1:**
- "1.4.1.a": Examine configuration standards and network diagrams to verify that NSCs are defined between trusted and untrusted networks.
- "1.4.1.b": Examine network configurations to verify that NSCs are in place between trusted and untrusted networks, in accordance with the documented configuration standards and network diagrams.
**Customized Approach Objective of 1.4.1:**Unauthorized traffic cannot traverse network boundaries between trusted and untrusted networks.
**Guidance - Purpose of 1.4.1:**Implementing NSCs at every connection coming into and out of trusted networks allows the entity to monitor and control access and minimizes the chances of a malicious individual obtaining access to the internal network via an unprotected connection.
**Guidance - Examples of 1.4.1:**An entity could implement a DMZ, which is a part of the network that manages connections between an untrusted network (for examples of
untrusted networks refer to the Requirement 1 Overview) and services that an organization needs to have available to the public, such as a web server. Please note that if an entity's DMZ processes or transmits account data (for example, e-commerce website), it is also considered a CDE.

---
**Control objectives:**1.4
**Sub-requirement:** 1.4.2 *(Tag: stateful firewall, public services exposure, inbound filtering)*
**Defined Approach Requirements of 1.4.2:**Inbound traffic from untrusted networks to trusted networks is restricted to:
• Communications with system components that are authorized to provide publicly accessible services, protocols, and ports.
• Stateful responses to communications initiated by system components in a trusted network.
• All other traffic is denied.
**Defined Approach Testing Procedures of 1.4.2:**
- "1.4.2": Examine vendor documentation and configurations of NSCs to verify that inbound traffic from untrusted networks to trusted networks is restricted in accordance with all elements specified in this requirement.
**Customized Approach Objective of 1.4.2:**Only traffic that is authorized or that is a response to a system component in the trusted network can enter a trusted network from an untrusted network.
**Applicability Notes of 1.4.2:**The intent of this requirement is to address communication sessions between trusted and untrusted networks, rather than the specifics of protocols. This requirement does not limit the use of UDP or other connectionless network protocols if state is maintained by the NSC.
**Guidance - Purpose of 1.4.2:**Ensuring that public access to a system component is specifically authorized reduces the risk of system components being unnecessarily exposed to untrusted networks.
**Guidance - Good Practice of 1.4.2:**System components that provide publicly accessible services, such as email, web, and DNS servers, are the most vulnerable to threats originating from untrusted networks. Ideally, such systems are placed within a dedicated trusted network that is public facing (for example, a DMZ) but that is separated via NSCs from more sensitive internal systems, which helps protect the rest of the network in the event these externally accessible systems are compromised. This functionality is intended to prevent malicious actors from accessing the organization's internal network from the Internet, or from using services, protocols, or ports in an unauthorized manner. Where this functionality is provided as a built-in feature of an NSC, the entity should ensure that its configurations do not result in the functionality being disabled or bypassed.
**Guidance - Definitions of 1.4.2:**Maintaining the "state" (or status) for each connection into a network means the NSC 'knows' whether an apparent response to a previous connection is a valid, authorized response (since the NSC retains each connection's status) or whether it is malicious traffic trying to fool the NSC into allowing the connection.

---
**Control objectives:**1.4
**Sub-requirement:** 1.4.3 *(Tag: anti-spoofing, IP filtering, packet validation)*
**Defined Approach Requirements of 1.4.3:**Anti-spoofing measures are implemented to detect and block forged source IP addresses from entering the trusted network.
**Defined Approach Testing Procedures of 1.4.3:**
- "1.4.3": Examine vendor documentation and configurations for NSCs to verify that anti-spoofing measures are implemented to detect and block forged source IP addresses from entering the trusted network.
**Customized Approach Objective of 1.4.3:**Packets with forged IP source addresses cannot enter a trusted network.
**Guidance - Purpose of 1.4.3:**Filtering packets coming into the trusted network helps to, among other things, ensure packets are not 'spoofed' to appear as if they are coming from an organization's own internal network. For example, anti-spoofing measures prevent internal addresses originating from the Internet from passing into the DMZ.
**Guidance - Good Practice of 1.4.3:**Products usually come with anti-spoofing set as a default and may not be configurable. Entities should consult the vendor's documentation for more information.
**Guidance - Examples of 1.4.3:**Normally, a packet contains the IP address of the computer that originally sent it so other computers in the network know where the packet originated. Malicious individuals will often try to spoof (or imitate) the sending IP address to fool the target system into believing the packet is from a trusted source

---
**Control objectives:**1.4
**Sub-requirement:** 1.4.4 *(Tag: database isolation, CDE protection, no direct public access)*
**Defined Approach Requirements of 1.4.4:**System components that store cardholder data are not directly accessible from untrusted networks.
**Defined Approach Testing Procedures of 1.4.4:**
- "1.4.4.a": Examine the data-flow diagram and network diagram to verify that it is documented that system components storing cardholder data are not directly accessible from the untrusted networks.
- "1.4.4.b": Examine configurations of NSCs to verify that controls are implemented such that system components storing cardholder data are not directly accessible from untrusted networks.
**Customized Approach Objective of 1.4.4:**Stored cardholder data cannot be accessed from untrusted networks.
**Applicability Notes of 1.4.4:**This requirement is not intended to apply to storage of account data in volatile memory but does apply where memory is being treated as persistent storage (for example, RAM disk). Account data can only be stored in volatile memory during the time necessary to support the associated business process (for example, until completion of the related payment card transaction). 1.4.4.b Examine configurations of NSCs to verify that controls are implemented such that system components storing cardholder data are not directly accessible from untrusted networks.
**Guidance - Purpose of 1.4.4:**Cardholder data that is directly accessible from an untrusted network, for example, because it is stored on a system within the DMZ or in a cloud database service, is easier for an external attacker to access because there are fewer defensive layers to penetrate. Using NSCs to ensure that system components that store cardholder data (such as a database or a file) can only be directly accessed from trusted networks can prevent unauthorized network traffic from reaching the system component.

---
**Control objectives:**1.4
**Sub-requirement:** 1.4.5 *(Tag: NAT, IP masking, network information disclosure)*
**Defined Approach Requirements of 1.4.5:**The disclosure of internal IP addresses and routing information is limited to only authorized parties.
**Defined Approach Testing Procedures of 1.4.5:**
- "1.4.5.a": Examine configurations of NSCs to verify that the disclosure of internal IP addresses and routing information is limited to only authorized parties.
- "1.4.5.b": Interview personnel and examine documentation to verify that controls are implemented such that any disclosure of internal addresses and routing information is limited to only authorized parties.
**Customized Approach Objective of 1.4.5:**Internal network information is protected from unauthorized disclosure.
**Guidance - Purpose of 1.4.5:**Restricting the disclosure of internal, private, and local IP addresses is useful to prevent a hacker from obtaining knowledge of these IP addresses and using that information to access the network.
**Guidance - Good Practice of 1.4.5:**Methods used to meet the intent of this requirement may vary, depending on the specific networking technology being used. For example, the controls used to meet this requirement may be different for IPv4 networks than for IPv6 networks.
**Guidance - Examples of 1.4.5:**Methods to obscure IP addressing may include, but are not limited to:
• IPv4 Network Address Translation (NAT).
• Placing system components behind proxy servers/NSCs.
• Removal or filtering of route advertisements for internal networks that use registered addressing.
• Internal use of RFC 1918 (IPv4) or use IPv6 privacy extension (RFC 4941) when initiating outgoing sessions to the internet.