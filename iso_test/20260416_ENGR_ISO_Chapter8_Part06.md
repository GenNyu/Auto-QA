### A. Tài liệu gốc của Chương 8 (Control 8.9, 8.10)

### B. Summary Overview của Chương 8 (Control 8.9, 8.10)
Tài liệu này mô tả chi tiết **mục 8.9 và 8.10** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào việc chuẩn hóa cấu hình kỹ thuật và xóa dữ liệu an toàn khi không còn cần thiết.
Mục tiêu là **giữ hệ thống ở trạng thái cấu hình an toàn, nhất quán và có thể kiểm soát, đồng thời bảo đảm dữ liệu bị loại bỏ đúng cách để tránh lộ lọt hoặc tái khôi phục trái phép**.
Gồm 2 mục chính:
- `8.9`: Configuration management - thiết lập, ghi nhận, giám sát và rà soát cấu hình
- `8.10`: Information deletion - xóa thông tin an toàn khi không còn cần lưu giữ

Áp dụng cho phần cứng, phần mềm, dịch vụ, mạng, dữ liệu lưu trên hệ thống hoặc media, cũng như quy trình xóa dữ liệu nội bộ hoặc thông qua nhà cung cấp dịch vụ.

### C. Key Points của Chương 8 (Control 8.9, 8.10)
- **Mục tiêu quản trị:** `8.9` giảm rủi ro cấu hình sai hoặc thay đổi trái phép; `8.10` giảm rủi ro dữ liệu tồn lưu quá lâu hoặc bị khôi phục sau khi đã bị xóa.
- **Yêu cầu chính của 8.9:** Tổ chức phải có cấu hình chuẩn, template an toàn, theo dõi thay đổi, giám sát cấu hình thực tế và xử lý mọi sai lệch theo quy trình quản lý thay đổi.
- **Yêu cầu chính của 8.10:** Thông tin phải được xóa khi không còn cần thiết, bằng phương pháp phù hợp với mức độ nhạy cảm, yêu cầu pháp lý và môi trường lưu trữ.
- **Điểm vận hành quan trọng:** `8.9` cần đi kèm inventory và system management tools; `8.10` cần log, bằng chứng xóa và yêu cầu xóa áp dụng cho cả cloud, nhà cung cấp và thiết bị trả lại.
- **Lưu ý thực tế:** Việc xóa dữ liệu không chỉ là “delete”; tùy bối cảnh có thể cần overwrite, cryptographic erasure, destruction hoặc phối hợp với supplier để bảo đảm dữ liệu không còn phục hồi được.

### D. Deep Summary của Chương 8 (Control 8.9, 8.10)
**Bối cảnh:**
Hai control này xử lý hai vấn đề song hành trong quản trị công nghệ: cấu hình hệ thống phải được giữ ở trạng thái chuẩn và dữ liệu phải được loại bỏ đúng cách khi hết vòng đời. Nếu cấu hình không được kiểm soát, môi trường vận hành sẽ trôi dạt khỏi trạng thái an toàn ban đầu. Nếu dữ liệu không được xóa đúng, dữ liệu cũ có thể tồn tại trong hệ thống, backup, cloud hoặc media đã chuyển nhượng.

**Nội dung cốt lõi:**
- `8.9` yêu cầu xây dựng, ghi nhận, triển khai, giám sát và rà soát cấu hình cho hardware, software, services và networks trong suốt vòng đời vận hành.
- `8.9` nhấn mạnh standard templates, system hardening và việc chỉ cho phép thay đổi qua change management, đồng thời theo dõi các sai lệch giữa cấu hình thực tế và cấu hình mục tiêu.
- `8.10` yêu cầu tổ chức xóa dữ liệu khi không còn cần thiết, đồng thời phải chọn phương pháp xóa phù hợp với loại dữ liệu, phương tiện lưu trữ và bối cảnh pháp lý.
- `8.10` mở rộng sang bên thứ ba và cloud, nơi cần có nghĩa vụ hợp đồng và bằng chứng xóa để bảo đảm dữ liệu được xử lý đúng khi dịch vụ chấm dứt hoặc khi thiết bị trả về vendor.
- Cả hai control đều có tính nền tảng: `8.9` giữ hệ thống ổn định và an toàn, còn `8.10` giữ vòng đời dữ liệu có thể kiểm soát và có thể kiểm chứng.

**Dữ liệu đáng chú ý:**
- `8.9` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Secure_configuration` và miền `#Protection`.
- `8.10` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, thuộc `#Information_protection#Legal_and_compliance` và miền `#Protection`.
- `8.9` có thể tích hợp với asset management, vì cấu hình chuẩn phụ thuộc vào inventory chính xác.
- `8.10` có tham chiếu đến ISO/IEC 27017 và ISO/IEC 27555 cho cloud services và PII deletion.
- `8.10` nêu rõ một số thiết bị, như smartphone, có thể cần xóa bằng chức năng factory reset hoặc hủy vật lý tùy mức độ nhạy cảm của dữ liệu.

**Rủi ro / Lưu ý:**
- Nếu configuration management yếu, tổ chức dễ rơi vào cấu hình lệch chuẩn, mở cổng, tắt kiểm soát hoặc gây gián đoạn do thay đổi không được quản lý.
- Nếu cấu hình chuẩn không được cập nhật theo threat mới, template an toàn ban đầu sẽ nhanh chóng trở nên lỗi thời.
- Nếu dữ liệu không được xóa đúng cách, thông tin có thể bị khôi phục từ hệ thống, backup, cloud storage hoặc media đã trả lại nhà cung cấp.
- Nếu không có bằng chứng hoặc log xóa, tổ chức sẽ khó chứng minh việc tuân thủ khi điều tra sự cố hoặc đáp ứng yêu cầu pháp lý.

### E. Structured Output của Chương 8 (Control 8.9, 8.10)
**Section:** 8.9
**Title:** Configuration management

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Secure_configuration |
| Security domains | #Protection |

**Control:**
Configurations, including security configurations, of hardware, software, services and networks should be established, documented, implemented, monitored and reviewed.

**Purpose:**
To ensure hardware, software, services and networks function correctly with required security settings, and configuration is not altered by unauthorized or incorrect changes.

**Guidance:**
***General***
The organization should define and implement processes and tools to enforce the defined configurations (including security configurations) for hardware, software, services (e.g. cloud services) and networks, for newly installed systems as well as for operational systems over their lifetime.

Roles, responsibilities and procedures should be in place to ensure satisfactory control of all configuration changes.

***Standard templates***
Standard templates for the secure configuration of hardware, software, services and networks should be defined:
- using publicly available guidance (e.g. pre-defined templates from vendors and from independent security organizations);
- considering the level of protection needed in order to determine a sufficient level of security;
- supporting the organization’s information security policy, topic-specific policies, standards and other security requirements;
- considering the feasibility and applicability of security configurations in the organization’s context.

The templates should be reviewed periodically and updated when new threats or vulnerabilities need to be addressed, or when new software or hardware versions are introduced.

The following should be considered for establishing standard templates for the secure configuration of hardware, software, services and networks:
- minimizing the number of identities with privileged or administrator level access rights;
- disabling unnecessary, unused or insecure identities;
- disabling or restricting unnecessary functions and services;
- restricting access to powerful utility programs and host parameter settings;
- synchronizing clocks;
- changing vendor default authentication information such as default passwords immediately after installation and reviewing other important default security-related parameters;
- invoking time-out facilities that automatically log off computing devices after a predetermined period of inactivity;
- verifying that licence requirements have been met (see 5.32).

***Managing configurations***
Established configurations of hardware, software, services and networks should be recorded and a log should be maintained of all configuration changes. These records should be securely stored. This can be achieved in various ways, such as configuration databases or configuration templates.

Changes to configurations should follow the change management process (see 8.32).

Configuration records can contain as relevant:
- up-to-date owner or point of contact information for the asset;
- date of the last change of configuration;
- version of configuration template;
- relation to configurations of other assets.

***Monitoring configurations***
Configurations should be monitored with a comprehensive set of system management tools (e.g. maintenance utilities, remote support, enterprise management tools, backup and restore software) and should be reviewed on a regular basis to verify configuration settings, evaluate password strengths and assess activities performed. Actual configurations can be compared with the defined target templates. Any deviations should be addressed, either by automatic enforcement of the defined target configuration or by manual analysis of the deviation followed by corrective actions.

**Other information:**
Documentation for systems often records details about the configuration of both hardware and software.

System hardening is a typical part of configuration management.

Configuration management can be integrated with asset management processes and associated tooling.

Automation is usually more effective to manage security configuration (e.g. using infrastructure as code).

Configuration templates and targets can be confidential information and should be protected from unauthorized access accordingly.

---
**Section:** 8.10
**Title:** Information deletion

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Information_protection #Legal_and_compliance |
| Security domains | #Protection |

**Control:**
Information stored in information systems, devices or in any other storage media should be deleted when no longer required.

**Purpose:**
To prevent unnecessary exposure of sensitive information and to comply with legal, statutory, regulatory and contractual requirements for information deletion.

**Guidance:**
***General***
Sensitive information should not be kept for longer than it is required to reduce the risk of undesirable disclosure.

When deleting information on systems, applications and services, the following should be considered:
- selecting a deletion method (e.g. electronic overwriting or cryptographic erasure) in accordance with business requirements and taking into consideration relevant laws and regulations;
- recording the results of deletion as evidence;
- when using service suppliers of information deletion, obtaining evidence of information deletion from them.

Where third parties store the organization’s information on its behalf, the organization should consider the inclusion of requirements on information deletion into the third-party agreements to enforce it during and upon termination of such services.

***Deletion methods***
In accordance with the organization’s topic-specific policy on data retention and taking into consideration relevant legislation and regulations, sensitive information should be deleted when no longer required, by:
- configuring systems to securely destroy information when no longer required (e.g. after a defined period subject to the topic-specific policy on data retention or by subject access request);
- deleting obsolete versions, copies and temporary files wherever they are located;
- using approved, secure deletion software to permanently delete information to help ensure information cannot be recovered by using specialist recovery or forensic tools;
- using approved, certified providers of secure disposal services;
- using disposal mechanisms appropriate for the type of storage media being disposed of (e.g. degaussing hard disk drives and other magnetic storage media).

Where cloud services are used, the organization should verify if the deletion method provided by the cloud service provider is acceptable, and if it is the case, the organization should use it, or request that the cloud service provider delete the information. These deletion processes should be automated in accordance with topic-specific policies, when available and applicable. Depending on the sensitivity of information deleted, logs can track or verify that these deletion processes have happened.

To avoid the unintentional exposure of sensitive information when equipment is being sent back to vendors, sensitive information should be protected by removing auxiliary storages (e.g. hard disk drives) and memory before equipment leaves the organization’s premises.

Considering that the secure deletion of some devices (e.g. smartphones) can only be achieved through destruction or using the functions embedded in these devices (e.g. “restore factory settings”), the organization should choose the appropriate method according to the classification of information handled by such devices.

Control measures described in 7.14 should be applied to physically destroy the storage device and simultaneously delete the information it contains.

An official record of information deletion is useful when analysing the cause of a possible information leakage event.

**Other information:**
Information on user data deletion in cloud services can be found in ISO/IEC 27017.

Information on deletion of PII can be found in ISO/IEC 27555.