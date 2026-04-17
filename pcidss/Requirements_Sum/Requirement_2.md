### A. Tài liệu gốc của Requirement 2

### B. Summary Overview của Control Objective 2.1
Tài liệu này mô tả chi tiết **Control Objective 2.1 **của **Requirement 2 **trong **PCI-DSS v4.0.1 **tập trung vào việc **Quản lý chính sách, quy trình và trách nhiệm liên quan đến cấu hình bảo mật hệ thống**
Mục tiêu chính là đảm bảo các chính sách và quy trình cấu hình được tài liệu hóa, cập nhật, áp dụng thực tế, được phổ biến
Gồm 2 sub-requirement chính:
- 2.1.1: Chính sách & quy trình
- 2.1.2: Vai trò & trách nhiệm
Áp dụng cho toàn bộ hoạt động cấu hình bảo mật trong phạm vi Requirement 2.

### C. Key Points của Control Objective 2.1
- **Phạm vi:**Chính sách và quy trình cấu hình hệ thống
- **Trách nhiệm:**Phân rõ vai trò (RACI)
- **Tài liệu:**Phải có, cập nhật và được sử dụng
- **Quản trị:**Đảm bảo nhận thức và tuân thủ của nhân sự
- **Vận hành:**Repeatable, consistent

### D. Deep Summary của Control Objective 2.1
**Bối cảnh:**
Việc thiếu chính sách và phân công trách nhiệm rõ ràng trong cấu hình hệ thống có thể dẫn đến cấu hình không nhất quán và lỗ hổng bảo mật. 2.1 đóng vai trò là nền tảng quản trị cho toàn bộ Requirement 2.
**Nội dung cốt lõi:**
- Quản lý quy trình: Tài liệu hóa, cập nhật và áp dụng các chính sách, quy trình cấu hình
- Vai trò & trách nhiệm: Phân rõ RACI, đảm bảo mọi hoạt động đều có người chịu trách nhiệm
- Vận hành hiệu quả: Các hoạt động phải lặp lại được, nhất quán, có thể kiểm chứng
**Dữ liệu đáng chú ý:**
- Không có mốc thời gian cụ thể
- Mang tính continuous compliance (tuân thủ liên tục)
**Rủi ro / Lưu ý:**
- Không có chính sách rõ ràng → cấu hình không nhất quán
- Không phân công trách nhiệm → bỏ sót công việc
- Chính sách không được phổ biến → thực thi sai
- Quy trình không cập nhật → không phản ánh thực tế

### E. Structured Output của của Control Objective 2.1
**Control objectives:**2.1
**Sub-requirement:**2.1.1 *(Tag: security policy, configuration policy, system hardening governance, documentation)*
**Defined Approach Requirements of 2.1.1:**All security policies and operational procedures that are identified in Requirement 2 are:
• Documented.
• Kept up to date.
• In use.
• Known to all affected parties.
**Defined Approach Testing Procedures of 2.1.1:**
- "2.1.1": Examine documentation and interview personnel to verify that security policies and operational procedures identified in Requirement 2 are managed in accordance with all elements specified in this requirement.
**Customized Approach Objective of 2.1.1:**Expectations, controls, and oversight for meeting activities within Requirement 2 are defined and adhered to by affected personnel. All supporting activities are repeatable, consistently applied, and conform to management's intent.
**Guidance - Purpose of 2.1.1:**Requirement 2.1.1 is about effectively managing and maintaining the various policies and procedures specified throughout Requirement 2. While it is important to define the specific policies or procedures called out in Requirement 2, it is equally important to ensure they are properly documented, maintained, and disseminated.
**Guidance - Good Practice of 2.1.1:**It is important to update policies and procedures as needed to address changes in processes, technologies, and business objectives. For this reason, consider updating these documents as soon as possible after a change occurs and not only on a periodic cycle.
**Guidance - Definitions of 2.1.1:**Security policies define the entity's security objectives and principles. Operational procedures describe how to perform activities, and define the controls, methods, and processes that are followed to achieve the desired result in a consistent manner and in accordance with policy objectives.

---
**Control objectives:**2.1
**Sub-requirement:**2.1.2 *(Tag: roles & responsibilities, system ownership, configuration management responsibility, RACI)*
**Defined Approach Requirements of 2.1.2:**Roles and responsibilities for performing activities in Requirement 2 are documented, assigned, and understood.
**Defined Approach Testing Procedures of 2.1.2:**
- "2.1.2.a": Examine documentation to verify that descriptions of roles and responsibilities for performing activities in Requirement 2 are documented and assigned.
- "2.1.2.b": Interview personnel with responsibility for performing activities in Requirement 2 to verify that roles and responsibilities are assigned as documented and are understood.
**Customized Approach Objective of 2.1.2:**Day-to-day responsibilities for performing all the activities in Requirement 2 are allocated. Personnel are accountable for successful, continuous operation of these requirements.
**Guidance - Purpose of 2.1.2:**If roles and responsibilities are not formally assigned, personnel may not be aware of their day-to-day responsibilities and critical activities may not occur.
**Guidance - Good Practice of 2.1.2:**Roles and responsibilities may be documented within policies and procedures or maintained within separate documents. As part of communicating roles and responsibilities, entities can consider having personnel acknowledge their acceptance and understanding of their assigned roles and responsibilities.
**Guidance - Examples of 2.1.2:**A method to document roles and responsibilities is a responsibility assignment matrix that includes who is responsible, accountable, consulted, and informed (also called a RACI matrix).

================

### A. Tài liệu gốc của Requirement 2

### B. Summary Overview của Control Objective 2.2
Tài liệu này mô tả chi tiết **Control Objective 2.2 **của **Requirement 2 **trong **PCI-DSS v4.0.1 **tập trung vào việc **Áp dụng cấu hình bảo mật (system hardening) cho toàn bộ hệ thống**
Mục tiêu chính là giảm bề mặt tấn công, loại bỏ cấu hình yếu, mặc định, đảm bảo hệ thống được cấu hình an toàn và nhất quán
Gồm 7 sub-requirement chính:
- 2.2.1: Configuration standards (hardening baseline)
- 2.2.2: Quản lý tài khoản mặc địnH
- 2.2.3: Phân tách chức năng hệ thống
- 2.2.4: Loại bỏ dịch vụ không cần thiết
- 2.2.5: Kiểm soát protocol không an toàn
- 2.2.6: Thiết lập security parameters
- 2.2.7: Mã hóa truy cập quản trị
Áp dụng cho toàn bộ hệ thống (network, server, cloud, virtualization)

### C. Key Points của Control Objective 2.2
- **Hardening:** Áp dụng baseline theo CIS / NIST / vendor
- **Default accounts:** Phải đổi hoặc disable
- **Segmentation:** Tách chức năng hệ thống
- **Minimize services:** Chỉ bật cái cần thiết
- **Insecure protocols:** Phải có kiểm soát + justification
- **Security config:** Thiết lập đúng các tham số bảo mật
- **Admin access:** Phải mã hóa (SSH, TLS…)

### D. Deep Summary của Control Objective 2.2
**Bối cảnh:**
Cấu hình mặc định và sai cấu hình là nguyên nhân phổ biến dẫn đến compromise hệ thống. 2.2 nhằm đảm bảo hệ thống được hardening đúng cách để giảm thiểu rủi ro tấn công
**Nội dung cốt lõi:**
- Cấu hình chuẩn: Áp dụng hardening baseline theo chuẩn industry
- Quản lý tài khoản: Loại bỏ hoặc thay đổi default credentials
- Phân tách chức năng: Tách hoặc cô lập các chức năng có mức bảo mật khác nhau
- Giảm bề mặt tấn công: Disable dịch vụ, protocol, chức năng không cần thiết
- Kiểm soát rủi ro: Insecure protocols phải có kiểm soát bổ sung
- Thiết lập bảo mật: Cấu hình đúng các security parameters
- Bảo vệ truy cập: Mã hóa toàn bộ truy cập quản trị non-console
**Dữ liệu đáng chú ý:**
- Áp dụng cho toàn bộ system components
- Configuration standards phải cập nhật khi có lỗ hổng mới
**Rủi ro / Lưu ý:**
- Dùng cấu hình mặc định → dễ bị tấn công
- Không hardening → tăng attack surface
- Không tách chức năng → ảnh hưởng chéo bảo mật
- Dịch vụ dư thừa → điểm khai thác
- Protocol không an toàn → bị intercept
- Admin access không mã hóa → lộ credential

### E. Structured Output của Control Objective 2.2
**Control objectives:**2.2
**Sub-requirement:**2.2.1 *(Tag: system hardening, baseline configuration, CIS benchmark, secure build standard)*
**Defined Approach Requirements of 2.2.1:**Configuration standards are developed, implemented, and maintained to:
• Cover all system components.
• Address all known security vulnerabilities.
• Be consistent with industry-accepted system hardening standards or vendor hardening recommendations.
• Be updated as new vulnerability issues are identified, as defined in Requirement 6.3.1.
• Be applied when new systems are configured and verified as in place before or immediately after a system component is connected to a production environment.
**Defined Approach Testing Procedures of 2.2.1:**
- "2.2.1.a": Examine system configuration standards to verify they define processes that include all elements specified in this requirement.
- "2.2.1.b": Examine policies and procedures and interview personnel to verify that system configuration standards are updated as new vulnerability issues are identified, as defined in Requirement 6.3.1.
- "2.2.1.c": Examine configuration settings and interview personnel to verify that system configuration standards are applied when new systems are configured and verified as being in place before or immediately after a system component is connected to a production environment.
**Customized Approach Objective of 2.2.1:**All system components are configured securely and consistently and in accordance with industry- accepted hardening standards or vendor recommendations.
**Guidance - Purpose of 2.2.1:**There are known weaknesses with many operating systems, databases, network devices, software, applications, container images, and other devices used by an entity or within an entity's environment. There are also known ways to configure these system components to fix security vulnerabilities. Fixing security vulnerabilities reduces the opportunities available to an attacker. By developing standards, entities ensure their system components will be configured consistently and securely and will address the protection of devices for which full hardening may be more difficult.
**Guidance - Good Practice of 2.2.1:**Keeping up to date with current industry guidance will help the entity maintain secure configurations. The specific controls to be applied to a system will vary and should be appropriate for the type and function of the system. Numerous security organizations have established system-hardening guidelines and recommendations, which advise how to correct common, known weaknesses.
**Guidance - Further Information of 2.2.1:**Sources for guidance on configuration standards include but are not limited to: Center for Internet Security (CIS), International Organization for Standardization (ISO), National Institute of Standards and Technology (NIST), Cloud Security Alliance, and product vendors.

---
**Control objectives:**2.2
**Sub-requirement:**2.2.2 *(Tag: default credentials, vendor defaults, password hardening, account security)*
**Defined Approach Requirements of 2.2.2:**Vendor default accounts are managed as follows:
• If the vendor default account(s) will be used, the default password is changed per Requirement 8.3.6.
• If the vendor default account(s) will not be used, the account is removed or disabled.
**Defined Approach Testing Procedures of 2.2.2:**
- "2.2.2.a": Examine system configuration standards to verify they include managing vendor default accounts in accordance with all elements specified in this requirement.
- "2.2.2.b": Examine vendor documentation and observe a system administrator logging on using vendor default accounts to verify accounts are implemented in accordance with all elements specified in this requirement.
- "2.2.2.c": Examine configuration files and interview personnel to verify that all vendor default accounts that will not be used are removed or disabled.
**Customized Approach Objective of 2.2.2:**System components cannot be accessed using default passwords.
**Applicability Notes of 2.2.2:**This applies to ALL vendor default accounts and passwords, including, but not limited to, those used by operating systems, software that provides security services, application and system accounts, point-of-sale (POS) terminals, payment applications, and Simple Network Management Protocol (SNMP) defaults. This requirement also applies where a system component is not installed within an entity's environment, for example, software and applications that are part of the CDE and are accessed via a cloud subscription service.
**Guidance - Purpose of 2.2.2:**Malicious individuals often use vendor default account names and passwords to compromise operating systems, applications, and the systems on which they are installed. Because these default settings are often published and are well known, changing these settings will make systems less vulnerable to attack.
**Guidance - Good Practice of 2.2.2:**All vendor default accounts should be identified, and their purpose and use understood. It is important to establish controls for application and system accounts, including those used to deploy and maintain cloud services so that they do not use default passwords and are not usable by unauthorized individuals. Where a default account is not intended to be used, changing the default password to a unique password that meets PCI DSS Requirement 8.3.6, removing any access to the default account, and then disabling the account, will prevent a malicious individual from re-enabling the account and gaining access with the default password. Using an isolated staging network to install and configure new systems is recommended and can also be used to confirm that default credentials have not been introduced into production environments.
**Guidance - Examples of 2.2.2:**Defaults to be considered include user IDs, passwords, and other authentication credentials commonly used by vendors in their products.

---
**Control objectives:**2.2
**Sub-requirement:**2.2.3 *(Tag: system segregation, tier architecture, application-database separation, isolation)*
**Defined Approach Requirements of 2.2.3:**Primary functions requiring different security levels are managed as follows:
• Only one primary function exists on a system component, OR
• Primary functions with differing security levels that exist on the same system component are isolated from each other, OR
• Primary functions with differing security levels on the same system component are all secured to the level required by the function with the highest security need.
**Defined Approach Testing Procedures of 2.2.3:**
- "2.2.3.a": Examine system configuration standards to verify they include managing primary functions requiring different security levels as specified in this requirement.
- "2.2.3.b": Examine system configurations to verify that primary functions requiring different security levels are managed per one of the ways specified in this requirement.
- "2.2.3.c": Where virtualization technologies are used, examine the system configurations to verify that system functions requiring different security levels are managed in one of the following ways:
• Functions with differing security needs do not co-exist on the same system component.
• Functions with differing security needs that exist on the same system component are isolated from each other.
• Functions with differing security needs on the same system component are all secured to the level required by the function with the highest security need.
**Customized Approach Objective of 2.2.3:**Primary functions with lower security needs cannot affect the security of primary functions with higher security needs on the same system component.
**Guidance - Purpose of 2.2.3:**Systems containing a combination of services, protocols, and daemons for their primary function will have a security profile appropriate to allow that function to operate effectively. For example, systems that need to be directly connected to the Internet would have a particular profile, like a DNS server, web server, or an e-commerce server. Conversely, other system components may operate a primary function comprising a different set of services, protocols, and daemons that perform functions that an entity does not want exposed to the Internet. This requirement aims to ensure that different functions do not impact the security profiles of other services in a way which may cause them to operate at a higher or lower security level.
**Guidance - Good Practice of 2.2.3:**Ideally, each function should be placed on different system components. This can be achieved by implementing only one primary function on each system component. Another option is to isolate primary functions on the same system component that have different security levels, for example, isolating web servers (which need to be directly connected to the Internet) from application and database servers. If a system component contains primary functions that need different security levels, a third option is to implement additional controls to ensure that the resultant security level of the primary function(s) with higher security needs is not reduced by the presence of the lower security primary functions. Additionally, the functions with a lower security level should be isolated and/or secured to ensure they cannot access or affect the resources of another system function, and do not introduce security weaknesses to other functions on the same server. Functions of differing security levels may be isolated by either physical or logical controls. For example, a database system should not also be hosting web services unless using controls like virtualization technologies to isolate and contain the functions into separate sub-systems. Another example is using virtual instances or providing dedicated memory access by system function. Where virtualization technologies are used, the security levels should be identified and managed for each virtual component. Examples of considerations for virtualized environments include:
• The function of each application, container, or virtual server instance.
• How virtual machines (VMs) or containers are stored and secured.

---
**Control objectives:**2.2
**Sub-requirement:**2.2.4 *(Tag: attack surface reduction, service minimization, disable unused services, hardening)*
**Defined Approach Requirements of 2.2.4:**Only necessary services, protocols, daemons, and functions are enabled, and all unnecessary functionality is removed or disabled.
**Defined Approach Testing Procedures of 2.2.4:**
- "2.2.4.a": Examine system configuration standards to verify necessary services, protocols, daemons, and functions are identified and documented.
- "2.2.4.b": Examine system configurations to verify the following:
• All unnecessary functionality is removed or disabled.
• Only required functionality, as documented in the configuration standards, is enabled.
**Customized Approach Objective of 2.2.4:**System components cannot be compromised by exploiting unnecessary functionality present in the system component.
**Guidance - Purpose of 2.2.4:**Unnecessary services and functions can provide additional opportunities for malicious individuals to gain access to a system. By removing or disabling all unnecessary services, protocols, daemons, and functions, organizations can focus on securing the functions that are required and reduce the risk that unknown or unnecessary functions will be exploited.
**Guidance - Good Practice of 2.2.4:**There are many protocols that could be enabled by default that are commonly used by malicious individuals to compromise a network. Disabling or removing all services, functions, and protocols that are not used minimizes the potential attack surface-for example, by removing or disabling an unused FTP or web server.
**Guidance - Examples of 2.2.4:**Unnecessary functionality may include, but is not limited to scripts, drivers, features, subsystems, file systems, interfaces (USB and Bluetooth), and unnecessary web servers.

---
**Control objectives:**2.2
**Sub-requirement:**2.2.5 *(Tag: insecure protocols, TLS enforcement, legacy protocol mitigation, risk acceptance)*
**Defined Approach Requirements of 2.2.5:**If any insecure services, protocols, or daemons are present:
• Business justification is documented.
• Additional security features are documented and implemented that reduce the risk of using insecure services, protocols, or daemons.
**Defined Approach Testing Procedures of 2.2.5:**
- "2.2.5.a": If any insecure services, protocols, or daemons are present, examine system configuration standards and interview personnel to verify they are managed and implemented in accordance with all elements specified in this requirement.
- "2.2.5.b": If any insecure services, protocols, or daemons, are present, examine configuration settings to verify that additional security features are implemented to reduce the risk of using insecure services, daemons, and protocols.
**Customized Approach Objective of 2.2.5:**System components cannot be compromised by exploiting insecure services, protocols, or daemons.
**Guidance - Purpose of 2.2.5:**Ensuring that all insecure services, protocols, and daemons are adequately secured with appropriate security features makes it more difficult for malicious individuals to exploit common points of compromise within a network.
**Guidance - Good Practice of 2.2.5:**Enabling security features before new system components are deployed will prevent insecure configurations from being introduced into the environment. Some vendor solutions may provide additional security functions to assist with securing an insecure process.
**Guidance - Further Information of 2.2.5:**For guidance on services, protocols, or daemons considered to be insecure, refer to industry standards and guidance (for example, as published by NIST, ENISA, and OWASP).

---
**Control objectives:**2.2
**Sub-requirement:**2.2.6 *(Tag: security parameters, system configuration, secure settings, misconfiguration prevention)*
**Defined Approach Requirements of 2.2.6:**System security parameters are configured to prevent misuse.
**Defined Approach Testing Procedures of 2.2.6:**
- "2.2.6.a": Examine system configuration standards to verify they include configuring system security parameters to prevent misuse.
- "2.2.6.b": Interview system administrators and/or security managers to verify they have knowledge of common security parameter settings for system components.
- "2.2.6.c": Examine system configurations to verify that common security parameters are set appropriately and in accordance with the system configuration standards.
**Customized Approach Objective of 2.2.6:**System components cannot be compromised because of incorrect security parameter configuration.
**Guidance - Purpose of 2.2.6:**Correctly configuring security parameters provided in system components takes advantage of the capabilities of the system component to defeat malicious attacks.
**Guidance - Good Practice of 2.2.6:**System configuration standards and related processes should specifically address security settings and parameters that have known security implications for each type of system in use. For systems to be configured securely, personnel responsible for configuration and/or administering systems should be knowledgeable in the specific security parameters and settings that apply to the system. Considerations should also include secure settings for parameters used to access cloud portals.
**Guidance - Further Information of 2.2.6:**Refer to vendor documentation and industry references noted in Requirement 2.2.1 for information about applicable security parameters for each type of system.

---
**Control objectives:**2.2
**Sub-requirement:**2.2.7 *(Tag: encrypted admin access, SSH, TLS, secure remote access, API security)*
**Defined Approach Requirements of 2.2.7:**All non-console administrative access is encrypted using strong cryptography.
**Defined Approach Testing Procedures of 2.2.7:**
- "2.2.7.a": Examine system configuration standards to verify they include encrypting all non-console administrative access using strong cryptography.
- "2.2.7.b": Observe an administrator log on to system components and examine system configurations to verify that non-console administrative access is managed in accordance with this requirement.
- "2.2.7.c": Examine settings for system components and authentication services to verify that insecure remote login services are not available for non- console administrative access.
- "2.2.7.d": Examine vendor documentation and interview personnel to verify that strong cryptography for the technology in use is implemented according to industry best practices and/or vendor recommendations.
**Customized Approach Objective of 2.2.7:**Cleartext administrative authorization factors cannot be read or intercepted from any network transmissions.
**Applicability Notes of 2.2.7:**This includes administrative access via browser- based interfaces and application programming interfaces (APIs).
**Guidance - Purpose of 2.2.7:**If non-console (including remote) administration does not use encrypted communications, administrative authorization factors (such as IDs and passwords) can be revealed to an eavesdropper. A malicious individual could use this information to access the network, become administrator, and steal data.
**Guidance - Good Practice of 2.2.7:**Whichever security protocol is used, it should be configured to use only secure versions and configurations to prevent use of an insecure connection-for example, by using only trusted certificates, supporting only strong encryption, and not supporting fallback to weaker, insecure protocols or methods.
**Guidance - Examples of 2.2.7:**Cleartext protocols (such as HTTP, telnet, etc.) do not encrypt traffic or logon details, making it easy for an eavesdropper to intercept this information. Non-console access may be facilitated by technologies that provide alternative access to systems, including but not limited to, out-of-band (OOB), lights-out management (LOM), Intelligent Platform Management Interface (IPMI), and keyboard, video, mouse (KVM) switches with remote capabilities. These and other non-console access technologies and methods must be secured with strong cryptography.
**Guidance - Further Information of 2.2.7:**Refer to industry standards and best practices such as NIST SP 800-52 and SP 800-57.

================

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