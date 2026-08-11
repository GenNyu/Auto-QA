### A. Tài liệu gốc của Requirement 1

### B. Summary Overview của Control Objective 1.1
Tài liệu này mô tả chi tiết **Control Objective 1.1 **của **Requirement 1 **trong **PCI-DSS v4.0.1, **tập trung vào việc **Quản lý chính sách, quy trình và trách nhiệm liên quan đến NSCs**
Mục tiêu là **Đảm bảo** các chính sách và quy trình bảo mật được tài liệu hóa, luôn được cập nhật, được áp dụng trong thực tế, được phổ biến đến các bên liên quan
Gồm 2 sub-requirement chính:
- 1.1.1: Quản lý chính sách và quy trình bảo mật
- 1.1.2: Phân công vai trò và trách nhiệm
Áp dụng cho nhân sự và hoạt động liên quan đến NSCs trong CDE

### C. Key Points của Control Objective 1.1
- **Phạm vi áp dụng:** Nhân sự chịu trách nhiệm về NSCs và các chính sách và quy trình bảo mật mạng
- **Trách nhiệm:** Xác định rõ vai trò và trách nhiệm (RACI) và đảm bảo hoạt động
- **Quản lý tài liệu:** Tài liệu hóa, Cập nhật và Phổ biến chính sách NSC đến các bên liên quan
- **Quản trị vận hành:**Các hoạt động phải được repeatable, consitent và phù hợp mục tiêu
- **Thời hạn:** Một số yêu cầu mới áp dụng từ 31/03/2025

### D. Deep Summary của Control Objective 1.1
**Bối cảnh:**
Control Objective 1.1 là nền tảng quản trị của Requirement 1, đảm bảo NSCs được quản trị rõ ràng. Thiếu chính sách và phân công trách nhiệm có thể dẫn đến: lỗ hổng vận hành. thực thi không nhất quán, mất kiểm soát bảo mật
**Nội dung cốt lõi:**
- **Quản lý quy trình:** **Tài liệu hóa, Cập nhật** và **Thực hiện** đầy đủ các chính sách, quy trình vận hành
- **Vai trò & trách nhiệm:**Phân rõ RACI (Responsible, Accountable, Consulted, Informed), đảm bảo không có hoạt động nào thiếu người chịu trách nhiệm
- **Vận hành hiệu quả: Các hoạt động phải **lặp lại được, nhất quán, có thể kiểm chứng
**Dữ liệu đáng chú ý:**
- Không có mốc thời gian cụ thể
- Mang tính **continuous compliance (tuân thủ liên tục)**
**Rủi ro / Lưu ý:**
- Không có chính sách rõ ràng → hoạt động không nhất quán
- Không phân công trách nhiệm → bỏ sót công việc
- Chính sách không được phổ biến → thực thi sai
- Quy trình không cập nhật → không phản ánh thực tế

### E. Structured Output của Control Objective 1.1
**Control objectives:**1.1
**Sub-requirement:** 1.1.1 *(Tag: security policy, network security policy, governance, documentation)*
**Defined Approach Requirements of 1.1.1:**All security policies and operational procedures that are identified in Requirement 1 are:
• Documented.
• Kept up to date.
• In use.
• Known to all affected parties.
**Defined Approach Testing Procedures of 1.1.1:**
- "1.1.1": Examine documentation and interview personnel to verify that security policies and operational procedures identified in Requirement 1 are managed in accordance with all elements specified in this requirement.
**Customized Approach Objective of 1.1.1:**Expectations, controls, and oversight for meeting activities within Requirement 1 are defined, understood, and adhered to by affected personnel. All supporting activities are repeatable, consistently applied, and conform to management's intent.
**Guidance - Purpose of 1.1.1:**Requirement 1.1.1 is about effectively managing and maintaining the various policies and procedures specified throughout Requirement 1. While it is important to define the specific policies or procedures called out in Requirement 1, it is equally important to ensure they are properly documented, maintained, and disseminated.
**Guidance - Good Practice of 1.1.1:**It is important to update policies and procedures as needed to address changes in processes, technologies, and business objectives. For these reasons, consider updating these documents as soon as possible after a change occurs and not only on a periodic cycle.
**Guidance - Definitions of 1.1.1:**Security policies define the entity's security objectives and principles. Operational procedures describe how to perform activities, and define the controls, methods, and processes that are followed to achieve the desired result in a consistent manner and in accordance with policy objectives.

---
**Control objectives:**1.1
**Sub-requirement:** 1.1.2 *(Tag: roles & responsibilities, RACI, security ownership, operational accountability)*
**Defined Approach Requirements of 1.1.2:**Roles and responsibilities for performing activities in Requirement 1 are documented, assigned, and understood.
**Defined Approach Testing Procedures of 1.1.2:**
- "1.1.2.a": Examine documentation to verify that descriptions of roles and responsibilities for performing activities in Requirement 1 are documented and assigned.
- "1.1.2.b": Interview personnel responsible for performing activities in Requirement 1 to verify roles and responsibilities are assigned as documented and are understood.
**Customized Approach Objective of 1.1.2:**Day-to-day responsibilities for performing all the activities in Requirement 1 are allocated. Personnel are accountable for successful, continuous operation of these requirements.
**Guidance - Purpose of 1.1.2:**If roles and responsibilities are not formally assigned, personnel may not be aware of their day-to-day responsibilities and critical activities may not occur.
**Guidance - Good Practice of 1.1.2:**Roles and responsibilities may be documented within policies and procedures or maintained within separate documents. As part of communicating roles and responsibilities, entities can consider having personnel acknowledge their acceptance and understanding of their assigned roles and responsibilities.
**Guidance - Examples of 1.1.2:**A method to document roles and responsibilities is a responsibility assignment matrix that includes who is responsible, accountable, consulted, and informed (also called a RACI matrix).

================

### A. Tài liệu gốc của Requirement 1

### B. Summary Overview của Control Objective 1.2
Tài liệu này mô tả chi tiết **Control Objective 1.2 **của **Requirement 1 **trong **PCI-DSS v4.0.1, **tập trung vào việc **Cấu hình, quản lý và duy trì Network Security Controls (NSCs)**
Mục tiêu là **Đảm bảo NSCs được** cấu hình đúng chuẩn, quản lý thay đổi chặt chẽ, duy trì chính xác và cập nhật
Gồm 6 nhóm sub-requirement chính:
- 1.2.1: Quy chuẩn cấu hình
- 1.2.2: Quản lý thay đổi
- 1.2.3–1.2.4: Sơ đồ mạng & luồng dữ liệu
- 1.2.5–1.2.6: Kiểm soát services/ports/protocols
- 1.2.7: Rà soát định kỳ
- 1.2.8: Bảo vệ cấu hình
Áp dụng cho toàn bộ NSCs trong phạm vi CDE

### C. Key Points của Control Objective 1.2
- **Cấu hình chuẩn:** NSCs phải có baseline rõ ràng
- **Change control:** Mọi thay đổi phải được phê duyệt
- **Sơ đồ:** Luôn duy trì network diagram & data-flow
- **Kiểm soát truy cập:**Chỉ cho phép services/ports có business justification
- **Rủi ro giao thức yếu:**Phải có biện pháp giảm thiểu
- **Rà soát:**Tối thiểu mỗi 6 tháng
- **Cấu hình:**Phải được bảo vệ và đồng nhất với hệ thống thực tế
- **Thời hạn:** Một số yêu cầu mới áp dụng từ 31/03/2025

### D. Deep Summary của Control Objective 1.2
**Bối cảnh:**
Control Objective 1.2 tập trung vào cấu hình và vận hành NSCs để kiểm soát lưu lượng mạng vào/ra CDE. Cấu hình sai hoặc quản lý thay đổi không chặt chẽ có thể dẫn đến: truy cập trái phép, lỗ hổng bảo mật, mất kiểm soát hệ thống
**Nội dung cốt lõi:**
- **Cấu hình chuẩn:** NSCs có baseline và áp dụng nhất quán
- **Change control:** Mọi thay đổi phải được phê duyệt & kiểm tra
- **Minh bạch:** Duy trì network diagram & data-flow
- **Kiểm soát truy cập:** Chỉ allow khi có business justification (default deny)
- **Giảm rủi ro:** Kiểm soát protocol/port không an toàn
- **Rà soát:** Review cấu hình định kỳ
- **Bảo vệ config:** File cấu hình phải được bảo mật
**Dữ liệu đáng chú ý:**
- 6 tháng: chu kỳ review tối thiểu
- Scope: toàn bộ NSCs liên quan đến CDE
**Rủi ro / Lưu ý:**
- Misconfiguration → mở access trái phép
- Không kiểm soát change → tạo lỗ hổng
- Diagram không cập nhật → mất kiểm soát scope
- Protocol yếu → dễ bị khai thác
- Rule dư thừa → tăng risk
- Config không bảo vệ → bị sửa trái phép

### E. Structured Output của Control Objective 1.2
**Control objectives:**1.2
**Sub-requirement:** 1.2.1 *(Tag: firewall ruleset, network configuration standards, NSC baseline)*
**Defined Approach Requirements of 1.2.1:**Configuration standards for NSC rulesets are:
• Defined.
• Implemented.
• Maintained.
**Defined Approach Testing Procedures of 1.2.1:**
- "1.2.1.a": Examine the configuration standards for NSC rulesets to verify the standards are in accordance with all elements specified in this requirement.
- "1.2.1.b": Examine configuration settings for NSC rulesets to verify that rulesets are implemented according to the configuration standards.
**Customized Approach Objective of 1.2.1:**The way that NSCs are configured and operate are defined and consistently applied.
**Guidance - Purpose of 1.2.1:**The implementation of these configuration standards results in the NSC being configured and managed to properly perform their security function (often referred to as the ruleset).
**Guidance - Good Practice of 1.2.1:**These standards often define the requirements for acceptable protocols, ports that are permitted to be used, and specific configuration requirements that are acceptable. Configuration standards may also outline what the entity considers not acceptable or not permitted within its network.
**Guidance - Definitions of 1.2.1:**NSCs are key components of a network architecture. Most commonly, NSCs are used at the boundaries of the CDE to control network traffic flowing inbound and outbound from the CDE. Configuration standards outline an entity's minimum requirements for the configuration of its NSCs.
**Guidance - Examples of 1.2.1:**Examples of NSCs covered by these configuration standards include, but are not limited to, firewalls, routers configured with access control lists, and cloud virtual networks.

---
**Control objectives:**1.2
**Sub-requirement:** 1.2.2 *(Tag: change control, network change management, NSC configuration updates)*
**Defined Approach Requirements of 1.2.2:**All changes to network connections and to configurations of NSCs are approved and managed in accordance with the change control process defined at Requirement 6.5.1.
**Defined Approach Testing Procedures of 1.2.2:**
- "1.2.2.a": Examine documented procedures to verify that changes to network connections and configurations of NSCs are included in the formal change control process in accordance with Requirement 6.5.1.
- "1.2.2.b": Examine network configuration settings to identify changes made to network connections. Interview responsible personnel and examine change control records to verify that identified changes to network connections were approved and managed in accordance with Requirement 6.5.1.
- "1.2.2.c": Examine network configuration settings to identify changes made to configurations of NSCs. Interview responsible personnel and examine change control records to verify that identified changes to configurations of NSCs were approved and managed in accordance with Requirement 6.5.1.
**Customized Approach Objective of 1.2.2:**Changes to network connections and NSCs cannot result in misconfiguration, implementation of insecure services, or unauthorized network connections.
**Applicability Notes of 1.2.2:**Changes to network connections include the addition, removal, or modification of a connection. Changes to NSC configurations include those related to the component itself as well as those affecting how it performs its security function.
**Guidance - Purpose of 1.2.2:**Following a structured change control process for all changes to NSCs reduces the risk that a change could introduce a security vulnerability.
**Guidance - Good Practice of 1.2.2:**Changes should be approved by individuals with the appropriate authority and knowledge to understand the impact of the change. Verification should provide reasonable assurance that the change did not adversely impact the security of the network and that the change performs as expected.
To avoid having to address security issues introduced by a change, all changes should be approved prior to being implemented and verified after the change is implemented. Once approved and verified, network documentation should be updated to include the changes to prevent inconsistencies between network documentation and the actual configuration.

---
**Control objectives:**1.2
**Sub-requirement:** 1.2.3 *(Tag: network diagram, CDE connectivity, infrastructure mapping)*
**Defined Approach Requirements of 1.2.3:**An accurate network diagram(s) is maintained that shows all connections between the CDE and other networks, including any wireless networks.
**Defined Approach Testing Procedures of 1.2.3:**
- "1.2.3.a": Examine diagram(s) and network configurations to verify that an accurate network diagram(s) exists in accordance with all elements specified in this requirement.
- "1.2.3.b": Examine documentation and interview responsible personnel to verify that the network diagram(s) is accurate and updated when there are changes to the environment.
**Customized Approach Objective of 1.2.3:**A representation of the boundaries between the CDE, all trusted networks, and all untrusted networks, is maintained and available.
**Applicability Notes of 1.2.3:**A current network diagram(s) or other technical or topological solution that identifies network connections and devices can be used to meet this requirement.
**Guidance - Purpose of 1.2.3:**Maintaining an accurate and up-to-date network diagram(s) prevents network connections and devices from being overlooked and unknowingly left unsecured and vulnerable to compromise. A properly maintained network diagram(s) helps an organization verify its PCI DSS scope by identifying systems connecting to and from the CDE.
**Guidance - Good Practice of 1.2.3:**All connections to and from the CDE should be identified, including systems providing security, management, or maintenance services to CDE system components. Entities should consider including the following in their network diagrams:
• All locations, including retail locations, data centers, corporate locations, cloud providers, etc.
• Clear labeling of all network segments.
• All security controls providing segmentation, including unique identifiers for each control (for example, name of control, make, model, and version).
• All in-scope system components, including NSCs, web app firewalls, anti-malware solutions, change management solutions, IDS/IPS, log aggregation systems, payment terminals, payment applications, HSMs, etc. (continued on next page)
• Clear labeling of any out-of-scope areas on the diagram via a shaded box or other
mechanism.
• Date of last update, and names of people that made and approved the updates.
• A legend or key to explain the diagram. Diagrams should be updated by authorized personnel to ensure diagrams continue to provide an accurate description of the network.

---
**Control objectives:**1.2
**Sub-requirement:** 1.2.4 *(Tag: data flow diagram, cardholder data flow, payment data lifecycle)*
**Defined Approach Requirements of 1.2.4:**An accurate data-flow diagram(s) is maintained that meets the following:
• Shows all account data flows across systems and networks.
• Updated as needed upon changes to the environment.
**Defined Approach Testing Procedures of 1.2.4:**
- "1.2.4.a": Examine data-flow diagram(s) and interview personnel to verify the diagram(s) show all account data flows in accordance with all elements specified in this requirement.
- "1.2.4.b": Examine documentation and interview responsible personnel to verify that the data-flow diagram(s) is accurate and updated when there are changes to the environment.
**Customized Approach Objective of 1.2.4:**A representation of all transmissions of account data between system components and across network segments is maintained and available.
**Applicability Notes of 1.2.4:**A data-flow diagram(s) or other technical or topological solution that identifies flows of account data across systems and networks can be used to meet this requirement.
**Guidance - Purpose of 1.2.4:**An up-to-date, readily available data-flow diagram helps an organization understand and keep track of the scope of its environment by showing how account data flows across networks and between individual systems and devices. Maintaining an up-to-date data-flow diagram(s) prevents account data from being overlooked and unknowingly left unsecured.
**Guidance - Good Practice of 1.2.4:**The data-flow diagram should include all connection points where account data is received into and sent out of the network, including connections to open, public networks, application processing flows, storage, transmissions between systems and networks, and file backups.
The data-flow diagram is meant to be in addition to the network diagram and should reconcile with and augment the network diagram. As a best practice, entities can consider including the following in their data-flow diagrams:
• All processing flows of account data, including authorization, capture, settlement, chargeback, and refunds.
• All distinct acceptance channels, including card-present, card-not-present, and e-commerce.
• All types of data receipt or transmission, including any involving hard copy/paper media.
• The flow of account data from the point where it enters the environment, to its final disposition.
• Where account data is transmitted and processed, where it is stored, and whether storage is short term or long term.
• The source of all account data received (for example, customers, third party, etc.), and any entities with which account data is shared.
• Date of last update, and names of people that made and approved the updates.

---
**Control objectives:**1.2
**Sub-requirement:** 1.2.5* (Tag: ports & protocols, service whitelist, firewall allow rules)*
**Defined Approach Requirements of 1.2.5:**All services, protocols, and ports allowed are identified, approved, and have a defined business need.
**Defined Approach Testing Procedures of 1.2.5:**
- "1.2.5.a": Examine documentation to verify that a list exists of all allowed services, protocols, and ports, including business justification and approval for each.
- "1.2.5.b": Examine configuration settings for NSCs to verify that only approved services, protocols, and ports are in use.
**Customized Approach Objective of 1.2.5:**Unauthorized network traffic (services, protocols, or packets destined for specific ports) cannot enter or leave the network.
**Guidance - Purpose of 1.2.5:**Compromises often happen due to unused or insecure services (for example, telnet and FTP), protocols, and ports, since these can lead to unnecessary points of access being opened into the CDE. Additionally, services, protocols, and ports that are enabled but not in use are often overlooked and left unsecured and unpatched. By identifying the services, protocols, and ports necessary for business, entities can ensure that all other services, protocols, and ports are disabled or removed.
**Guidance - Good Practice of 1.2.5:**The security risk associated with each service, protocol, and port allowed should be understood. Approvals should be granted by personnel independent of those managing the configuration. Approving personnel should possess knowledge and accountability appropriate for making approval decisions.
--- **Control objectives:**1.2
**Sub-requirement:** 1.2.6 *(Tag: insecure protocols, TLS enforcement, legacy protocol mitigation)*
**Defined Approach Requirements of 1.2.6:**Security features are defined and implemented for all services, protocols, and ports that are in use and considered to be insecure, such that the risk is mitigated.
**Defined Approach Testing Procedures of 1.2.6:**
- "1.2.6.a": Examine documentation that identifies all insecure services, protocols, and ports in use to verify that for each, security features are defined to mitigate the risk.
- "1.2.6.b": Examine configuration settings for NSCs to verify that the defined security features are implemented for each identified insecure service, protocol, and port.
**Customized Approach Objective of 1.2.6:**The specific risks associated with the use of insecure services, protocols, and ports are understood, assessed, and appropriately mitigated.
**Guidance - Purpose of 1.2.6:**Compromises take advantage of insecure network configurations.
**Guidance - Good Practice of 1.2.6:**If insecure services, protocols, or ports are necessary for business, the risk posed by these services, protocols, and ports should be clearly understood and accepted by the organization, the use of the service, protocol, or port should be justified, and the security features that mitigate the risk of using these services, protocols, and ports should be defined and implemented by the entity.
**Guidance - Further Information of 1.2.6:**For guidance on services, protocols, or ports considered to be insecure, refer to industry standards and guidance (for example, from NIST, ENISA, OWASP).

---
**Control objectives:**1.2
**Sub-requirement:** 1.2.7* (Tag: firewall rule review, periodic audit, access validation)*
**Defined Approach Requirements of 1.2.7:**Configurations of NSCs are reviewed at least once every six months to confirm they are relevant and effective.
**Defined Approach Testing Procedures of 1.2.7:**
- "1.2.7.a": Examine documentation to verify procedures are defined for reviewing configurations of NSCs at least once every six months.
- "1.2.7.b": Examine documentation of reviews of configurations for NSCs and interview responsible personnel to verify that reviews occur at least once every six months.
- "1.2.7.c": Examine configurations for NSCs to verify that configurations identified as no longer being supported by a business justification are removed or updated.
**Customized Approach Objective of 1.2.7:**NSC configurations that allow or restrict access to trusted networks are verified periodically to ensure that only authorized connections with a current business justification are permitted.
**Guidance - Purpose of 1.2.7:**Such a review gives the organization an opportunity to clean up any unneeded, outdated, or incorrect rules and configurations which could be utilized by an unauthorized person. Furthermore, it ensures that all rules and configurations allow only authorized services, protocols, and ports that match the documented business justifications.
**Guidance - Good Practice of 1.2.7:**This review, which can be implemented using manual, automated, or system-based methods, is intended to confirm that the settings that manage traffic rules, what is allowed in and out of the network, match the approved configurations. The review should provide confirmation that all permitted access has a justified business reason. Any discrepancies or uncertainties about a rule or configuration should be escalated for resolution. While this requirement specifies that this review occur at least once every six months, organizations with a high volume of changes to their network configurations may wish to consider performing reviews more frequently to ensure that the configurations continue to meet the needs of the business.

---
**Control objectives:**1.2
**Sub-requirement:** 1.2.8 *(Tag: configuration files, infrastructure as code, secure config storage)*
**Defined Approach Requirements of 1.2.8:**Configuration files for NSCs are:
• Secured from unauthorized access.
• Kept consistent with active network configurations.
**Defined Approach Testing Procedures of 1.2.8:**
- "1.2.8": Examine configuration files for NSCs to verify they are in accordance with all elements specified in this requirement.
**Customized Approach Objective of 1.2.8:**NSCs cannot be defined or modified using untrusted configuration objects (including files).
**Applicability Notes of 1.2.8:**Any file or setting used to configure or synchronize NSCs is considered to be a 'configuration file.' This includes files, automated and system-based controls, scripts, settings, infrastructure as code, or other parameters that are backed up, archived, or stored remotely.
**Guidance - Purpose of 1.2.8:**To prevent unauthorized configurations from being applied to the network, stored files with configurations for network controls need to be kept up to date and secured against unauthorized changes. Keeping configuration information current and secure ensures that the correct settings for NSCs are applied whenever the configuration is run.
**Guidance - Examples of 1.2.8:**If the secure configuration for a router is stored in non-volatile memory, when that router is restarted or rebooted, these controls should ensure that its secure configuration is reinstated.

================

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

================

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

================

### A. Tài liệu gốc của Requirement 1

### B. Summary Overview của Control Objective 1.5
Tài liệu này mô tả chi tiết **Control Objective 1.5 **của **Requirement 1 **trong **PCI-DSS v4.0.1, **tập trung vào việc **Giảm thiểu rủi ro từ các thiết bị kết nối đồng thời vào mạng không tin cậy và CDE**
Mục tiêu là ngăn thiết bị (laptop, mobile, BYOD…) mang mối đe dọa vào CDE và đảm bảo thiết bị có security controls phù hợp trước khi kết nối
Gồm 1 sub-requirement chính:
- 1.5.1: Áp dụng security controls trên endpoint (company & BYOD)
Áp dụng cho tất cả thiết bị kết nối đồng thời Internet / mạng không tin cậy và CDE

### C. Key Points của Control Objective 1.5
- **Endpoint security:** Phải có security controls (EDR, firewall…)
- **Configuration:** Có cấu hình bảo mật rõ ràng
- **Enforcement:** Controls phải luôn hoạt động
- **User restriction:** Người dùng không được tự ý tắt
- **BYOD:** Áp dụng cả thiết bị cá nhân
- **VPN:** Hạn chế split-tunneling

### D. Deep Summary của Control Objective 1.5
**Bối cảnh:**
Thiết bị người dùng (laptop, mobile, BYOD) thường xuyên kết nối Internet nên dễ bị nhiễm malware. Khi các thiết bị này kết nối vào CDE, chúng có thể trở thành điểm xâm nhập cho attacker.
**Nội dung cốt lõi:**
- **Bảo vệ endpoint:**Thiết bị phải có security controls (endpoint protection, firewall…)
- **Cấu hình bảo mật:**Có thiết lập để ngăn threat từ mạng không tin cậy
- **Thực thi kiểm soát:**Controls phải luôn chạy và không bị user tự ý thay đổi
- **Kiểm soát truy cập:**Thiết bị chỉ được kết nối khi đáp ứng yêu cầu bảo mật
- **Quản lý ngoại lệ:**Chỉ được tắt controls khi có phê duyệt và trong thời gian giới hạn
**Dữ liệu đáng chú ý:**
- Áp dụng cho cả thiết bị công ty và BYOD
- Bao gồm laptop, mobile, tablet và thiết bị di động khác
**Rủi ro / Lưu ý:**
- Thiết bị nhiễm malware → lây vào CDE
- User tắt security controls → mất lớp bảo vệ
- Split-tunneling → bypass kiểm soát mạng
- Thiết bị không kiểm soát → trở thành điểm tấn công
- Không quản lý BYOD → mở rộng attack surface

### E. Structured Output của Control Objective 1.5
**Control objectives:**1.5
**Sub-requirement:** 1.5.1 *(Tag: endpoint security, VPN, split tunneling, device hardening)*
**Defined Approach Requirements of 1.5.1:**Security controls are implemented on any computing devices, including company- and employee-owned devices, that connect to both untrusted networks (including the Internet) and the CDE as follows:
• Specific configuration settings are defined to prevent threats being introduced into the entity's network.
• Security controls are actively running.
• Security controls are not alterable by users of the computing devices unless specifically documented and authorized by management on a case-by-case basis for a limited period.
**Defined Approach Testing Procedures of 1.5.1:**
- "1.5.1.a": Examine policies and configuration standards and interview personnel to verify security controls for computing devices that connect to both untrusted networks, and the are implemented in accordance with all elements specified in this requirement.
- "1.5.1.b": Examine configuration settings on computing devices that connect to both untrusted networks and the CDE to verify settings are implemented in accordance with all elements specified in this requirement.
**Customized Approach Objective of 1.5.1:**Devices that connect to untrusted environments and also connect to the CDE cannot introduce threats to the entity's CDE.
**Applicability Notes of 1.5.1:**These security controls may be temporarily disabled only if there is legitimate technical need, as authorized by management on a case-by-case basis. If these security controls need to be disabled for a specific
**Guidance - Purpose of 1.5.1:**Computing devices that are allowed to connect to the Internet from outside the corporate environment-for example, desktops, laptops, tablets, smartphones, and other mobile computing devices used by employees-are more vulnerable to Internet-based threats. Use of security controls such as host-based controls (for example, personal firewall software or end-point protection solutions), network-based security controls (for example, firewalls, network- based heuristics inspection, and malware simulation), or hardware, helps to protect devices from Internet-based attacks, which could use the device to gain access to the organization's systems and data when the device reconnects to the network.
**Guidance - Good Practice of 1.5.1:**The specific configuration settings are determined by the entity and should be consistent with its network security policies and procedures. Where there is a legitimate need to temporarily disable security controls on a company-owned or employee-owned device that connects to both an untrusted network and the CDE-for example, to support a specific maintenance activity or investigation of a technical problem-the reason for taking such action is understood and approved by an appropriate management representative. Any disabling or altering of these security controls, including on administrators' own devices, is performed by authorized personnel. It is recognized that administrators have privileges that may allow them to disable security controls on their own computers, but there should be alerting mechanisms in place when such controls are disabled and follow up that occurs to ensure processes were followed.
**Guidance - Examples of 1.5.1:**Practices include forbidding split-tunneling of VPNs for employee-owned or corporate-owned mobile devices and requiring that such devices boot up into a VPN.