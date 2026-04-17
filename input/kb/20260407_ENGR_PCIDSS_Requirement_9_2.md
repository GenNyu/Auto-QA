### A. Tài liệu gốc của Requirement 9

### B. Summary Overview của Control Objective 9.2
Tài liệu này mô tả chi tiết **Control Objective 9.2** của **Requirement 9** trong **PCI-DSS v4.0.1**, tập trung vào việc triển khai các kiểm soát truy cập vật lý để hạn chế truy cập trái phép vào hệ thống và khu vực chứa dữ liệu thẻ.
Mục tiêu chính là đảm bảo chỉ những cá nhân được ủy quyền mới có thể truy cập vật lý vào CDE và các thành phần hệ thống liên quan.
Gồm 4 sub-requirement chính:
- 9.2.1: Kiểm soát truy cập vào facility/CDE
- 9.2.2: Kiểm soát network jack công cộng
- 9.2.3: Bảo vệ thiết bị mạng và hạ tầng
- 9.2.4: Khóa console tại khu vực nhạy cảm
Áp dụng cho tất cả khu vực vật lý, thiết bị và hạ tầng có liên quan đến CDE.

### C. Key Points của Control Objective 9.2
- Phạm vi áp dụng: Facility, CDE, thiết bị mạng và khu vực nhạy cảm
- Trách nhiệm: Triển khai và duy trì kiểm soát truy cập vật lý
- Kiểm soát truy cập: Chỉ cho phép personnel được ủy quyền vào CDE
- Giám sát: Theo dõi entry/exit tại khu vực nhạy cảm (camera/access control)
- Kiểm soát kết nối: Hạn chế sử dụng network jack tại khu vực công cộng
- Bảo vệ thiết bị: Giới hạn truy cập vật lý vào thiết bị mạng và telecom
- Kiểm soát console: Khóa console khi không sử dụng

### D. Deep Summary của Control Objective 9.2
**Bối cảnh:**
Truy cập vật lý trái phép có thể dẫn đến đánh cắp thiết bị, thay đổi cấu hình hoặc cài cắm thiết bị độc hại vào hệ thống.
**Nội dung cốt lõi:**
- Thiết lập cơ chế kiểm soát truy cập vào facility và khu vực CDE
- Giám sát entry/exit tại khu vực nhạy cảm và lưu trữ log
- Hạn chế truy cập vào network jack tại khu vực công cộng
- Bảo vệ thiết bị mạng, wireless và telecom khỏi truy cập trái phép
- Khóa console khi không sử dụng để ngăn truy cập trái phép
**Dữ liệu đáng chú ý:**
- Monitoring data phải được lưu ≥ 3 tháng
- Áp dụng cho tất cả entry/exit point tại khu vực nhạy cảm
**Rủi ro / Lưu ý:**
- Không kiểm soát vật lý → attacker có thể truy cập trực tiếp hệ thống
- Network jack công cộng → điểm vào dễ bị khai thác
- Thiết bị mạng không bảo vệ → bị gắn thiết bị nghe lén
- Console không khóa → bị truy cập trái phép ngay tại chỗ

### E. Structured Output của Control Objective 9.2
**Control objectives:**9.2
**Sub-requirement:**9.2.1
**Defined Approach Requirements:**Appropriate facility entry controls are in place to restrict physical access to systems in the CDE.
**Defined Approach Testing Procedures:**Observe entry controls and interview responsible personnel to verify that physical security controls are in place to restrict access to systems in the CDE.
**Customized Approach Objective:**System components in the CDE cannot be physically accessed by unauthorized personnel.
**Applicability Notes:**This requirement does not apply to locations that are publicly accessible by consumers (cardholders).
**Guidance - Purpose:**Without physical access controls, unauthorized persons could potentially gain access to the CDE and sensitive information, or could alter system configurations, introduce vulnerabilities into the network, or destroy or steal equipment. Therefore, the purpose of this requirement is that physical access to the CDE is controlled via physical security controls such as badge readers or other mechanisms such as lock and key.
**Guidance - Good Practice:**Whichever mechanism meets this requirement, it must be sufficient for the organization to verify that only authorized personnel are granted access.
**Guidance - Examples:**Facility entry controls include physical security controls at each computer room, data center, and other physical areas with systems in the CDE. It can also include badge readers or other devices that manage physical access controls, such as lock and key with a current list of all individuals holding the keys.

---
**Control objectives:**9.2
**Sub-requirement:**9.2.1.1
**Defined Approach Requirements:**Individual physical access to sensitive areas within the CDE is monitored with either video cameras or physical access control mechanisms (or both) as follows:
• Entry and exit points to/from sensitive areas within the CDE are monitored.
• Monitoring devices or mechanisms are protected from tampering or disabling.
• Collected data is reviewed and correlated with other entries.
• Collected data is stored for at least three months, unless otherwise restricted by law.
**Defined Approach Testing Procedures:**
- "9.2.1.1.a": Observe locations where individual physical access to sensitive areas within the CDE occurs to verify that either video cameras or physical access control mechanisms (or both) are in place to monitor the entry and exit points.
- "9.2.1.1.b": Observe locations where individual physical access to sensitive areas within the CDE occurs to verify that either video cameras or physical access control mechanisms (or both) are protected from tampering or disabling.
- "9.2.1.1.c": Observe the physical access control mechanisms and/or examine video cameras and interview responsible personnel to verify that:
• Collected data from video cameras and/or physical access control mechanisms is reviewed and correlated with other entries.
• Collected data is stored for at least three months.
**Customized Approach Objective:**Trusted, verifiable records are maintained of individual physical entry to, and exit from, sensitive areas.
**Guidance - Purpose:**Maintaining details of individuals entering and exiting the sensitive areas can help with investigations of physical breaches by identifying individuals that physically accessed the sensitive areas, as well as when they entered and exited.
**Guidance - Good Practice:**Whichever mechanism meets this requirement, it should effectively monitor all entry and exit points to sensitive areas. Criminals attempting to gain physical access to sensitive areas will often try to disable or bypass the monitoring controls. To protect these controls from tampering, video cameras could be positioned so they are out of reach and/or be monitored to detect tampering. Similarly, physical access control mechanisms could be monitored or have physical protections installed to prevent them from being damaged or disabled by malicious individuals

---
**Control objectives:**9.2
**Sub-requirement:**9.2.2
**Defined Approach Requirements:**Physical and/or logical controls are implemented to restrict use of publicly accessible network jacks within the facility.
**Defined Approach Testing Procedures:**Interview responsible personnel and observe locations of publicly accessible network jacks to verify that physical and/or logical controls are in place to restrict access to publicly accessible network jacks within the facility.
**Customized Approach Objective:**Unauthorized devices cannot connect to the entity's network from public areas within the facility.
**Guidance - Purpose:**Restricting access to network jacks (or network ports) will prevent malicious individuals from plugging into readily available network jacks and gaining access to the CDE or systems connected to the CDE.
**Guidance - Good Practice:**Whether logical or physical controls, or a combination of both, are used, they should prevent an individual or device that is not explicitly authorized from being able to connect to the network.
**Guidance - Examples:**Methods to meet this requirement include network jacks located in public areas and areas accessible to visitors could be disabled and only enabled when network access is explicitly authorized. Alternatively, processes could be implemented to ensure that visitors are escorted at all times in areas with active network jacks.

---
**Control objectives:**9.2
**Sub-requirement:**9.2.3
**Defined Approach Requirements:**Physical access to wireless access points, gateways, networking/communications hardware, and telecommunication lines within the facility is restricted
**Defined Approach Testing Procedures:**Interview responsible personnel and observe locations of hardware and lines to verify that physical access to wireless access points, gateways, networking/communications hardware, and telecommunication lines within the facility is restricted.
**Customized Approach Objective:** Physical networking equipment cannot be accessed by unauthorized personnel.
**Guidance - Purpose:**Without appropriate physical security over access to wireless components and devices, and computer networking and telecommunications equipment and lines, malicious users could gain access to the entity's network resources. Additionally, they could connect their own devices to the network to gain unauthorized access to the CDE or systems connected to the CDE. Additionally, securing networking and communications hardware prevents malicious users from intercepting network traffic or physically connecting their own devices to wired network resources.

---
**Control objectives:**9.2
**Sub-requirement:**9.2.4
**Defined Approach Requirements:**Access to consoles in sensitive areas is restricted via locking when not in use.
**Defined Approach Testing Procedures:**Observe a system administrator's attempt to log into consoles in sensitive areas and verify that they are 'locked' to prevent unauthorized use. 9.3 Physical access for personnel and visitors is authorized and managed.
**Customized Approach Objective:**Physical consoles within sensitive areas cannot be used by unauthorized personnel.
**Guidance - Purpose:**Locking console login screens prevents unauthorized persons from gaining access to sensitive information, altering system configurations, introducing vulnerabilities into the network, or destroying records.