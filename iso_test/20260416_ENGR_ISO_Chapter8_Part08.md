### A. Tài liệu gốc của Chương 8 (Control 8.12, 8.13)

### B. Summary Overview của Chương 8 (Control 8.12, 8.13)
Tài liệu này mô tả chi tiết **mục 8.12 và 8.13** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào việc ngăn rò rỉ dữ liệu và bảo đảm có bản sao dự phòng để khôi phục khi xảy ra sự cố.
Mục tiêu là **phát hiện và chặn dữ liệu nhạy cảm bị đưa ra ngoài trái phép, đồng thời bảo đảm dữ liệu, phần mềm và hệ thống có thể phục hồi sau mất mát hoặc gián đoạn**.
Gồm 2 mục chính:
- `8.12`: Data leakage prevention - ngăn rò rỉ dữ liệu qua kênh, thiết bị hoặc hành vi người dùng
- `8.13`: Information backup - sao lưu thông tin, phần mềm và hệ thống để khôi phục

Áp dụng cho hệ thống, mạng, thiết bị đầu cuối, lưu trữ dự phòng, cloud, người dùng và mọi luồng dữ liệu có khả năng rời khỏi phạm vi kiểm soát của tổ chức.

### C. Key Points của Chương 8 (Control 8.12, 8.13)
- **Mục tiêu quản trị:** `8.12` giảm rủi ro dữ liệu nhạy cảm bị lộ qua email, file transfer, USB, screenshot hoặc cloud ngoài kiểm soát; `8.13` giảm rủi ro mất dữ liệu bằng sao lưu và kiểm thử phục hồi định kỳ.
- **Yêu cầu chính của 8.12:** Tổ chức phải nhận diện dữ liệu nhạy cảm, theo dõi các kênh rò rỉ và chặn hành vi có thể làm lộ dữ liệu, bao gồm copy/paste, upload và chuyển dữ liệu ra ngoài.
- **Yêu cầu chính của 8.13:** Backup phải được thiết kế, lưu giữ, kiểm thử và giám sát theo policy, đủ để khôi phục sau sự cố, lỗi hệ thống hoặc mất media.
- **Điểm vận hành quan trọng:** `8.12` không chỉ là công cụ DLP mà còn liên quan đến training, auditing và các biện pháp đánh lừa đối thủ; `8.13` phải bao gồm cả cloud backup, offline backup và kiểm tra thời gian khôi phục.
- **Lưu ý thực tế:** DLP có thể tác động đến privacy và monitoring của nhân sự; backup chỉ có giá trị khi khôi phục được trong thực tế và khi dữ liệu dự phòng vẫn được bảo vệ đúng mức.

### D. Deep Summary của Chương 8 (Control 8.12, 8.13)
**Bối cảnh:**
Hai control này giải quyết hai mặt của cùng một vấn đề vận hành: làm sao tránh dữ liệu bị “đi ra ngoài” khi không được phép, và làm sao giữ dữ liệu đủ an toàn để quay trở lại khi có sự cố. Một control thiên về ngăn chặn và phát hiện, control còn lại thiên về phục hồi. Nếu thiếu một trong hai, tổ chức либо đối mặt với lộ lọt, либо đối mặt với mất mát không thể khôi phục.

**Nội dung cốt lõi:**
- `8.12` yêu cầu xác định dữ liệu cần bảo vệ, theo dõi các kênh rò rỉ và triển khai DLP để phát hiện hoặc chặn hành vi lộ dữ liệu qua email, transfer, mobile devices, portable storage hoặc cloud.
- `8.12` nhấn mạnh việc kiểm soát copy/paste, screenshot, upload và các hành vi chuyển dữ liệu ra ngoài, với quyền phê duyệt xuất dữ liệu thuộc về data owner khi cần.
- `8.12` cũng xét đến các biện pháp đánh lừa hoặc làm nhiễu hoạt động intelligence của đối thủ, như reverse social engineering hoặc honeypots, khi phù hợp với bối cảnh.
- `8.13` yêu cầu backup policy rõ ràng, sao lưu định kỳ, lưu trữ an toàn, kiểm thử khôi phục và bảo đảm backup phù hợp với mục tiêu business continuity.
- `8.13` mở rộng đến cloud và yêu cầu xác định trách nhiệm backup giữa cloud service provider và cloud service customer, cũng như quản lý thời hạn lưu giữ và xóa backup khi hết nhu cầu.

**Dữ liệu đáng chú ý:**
- `8.12` là kiểm soát `#Preventive #Detective`, gắn với `#Confidentiality`, thuộc `#Information_protection` và miền `#Protection#Defence`.
- `8.13` là kiểm soát `#Corrective`, gắn với `#Integrity`, `#Availability`, thuộc `#Continuity` và miền `#Protection`.
- `8.12` có thể đòi hỏi xem xét pháp lý liên quan đến privacy, monitoring nhân sự, interception và data processing.
- `8.13` yêu cầu test khôi phục backup chứ không chỉ kiểm tra file sao lưu tồn tại.
- `8.13` nhắc đến cloud backup và retention expiration, tức sao lưu cũng phải có vòng đời và chính sách xóa.

**Rủi ro / Lưu ý:**
- Nếu DLP được triển khai mà không cân bằng với quyền riêng tư hoặc nghiệp vụ, nó có thể tạo phản ứng ngược hoặc chặn nhầm công việc hợp lệ.
- Nếu không theo dõi đủ kênh rò rỉ, dữ liệu vẫn có thể thoát ra ngoài qua một con đường không được giám sát.
- Nếu backup không được kiểm thử phục hồi, tổ chức có thể phát hiện quá muộn rằng bản sao không dùng được khi có sự cố.
- Nếu backup cloud không có phân định trách nhiệm rõ, tổ chức có thể nghĩ dữ liệu đã được sao lưu trong khi thực tế chưa đủ để khôi phục.

### E. Structured Output của Chương 8 (Control 8.12, 8.13)
**Section:** 8.12
**Title:** Data leakage prevention

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive #Detective |
| Information security properties | #Confidentiality |
| Cybersecurity concepts | #Protect #Detect |
| Operational capabilities | #Information_protection |
| Security domains | #Protection #Defence |

**Control:**
Data leakage prevention measures should be applied to systems, networks and any other devices that process, store or transmit sensitive information.

**Purpose:**
To detect and prevent the unauthorized disclosure and extraction of information by individuals or systems.

**Guidance:**
The organization should consider the following to reduce the risk of data leakage:
- identifying and classifying information to protect against leakage (e.g. personal information, pricing models and product designs);
- monitoring channels of data leakage (e.g. email, file transfers, mobile devices and portable storage devices);
- acting to prevent information from leaking (e.g. quarantine emails containing sensitive information).

Data leakage prevention tools should be used to:
- identify and monitor sensitive information at risk of unauthorized disclosure (e.g. in unstructured data on a user’s system);
- detect the disclosure of sensitive information (e.g. when information is uploaded to untrusted third-party cloud services or sent via email);
- block user actions or network transmissions that expose sensitive information (e.g. preventing the copying of database entries into a spreadsheet).

The organization should determine if it is necessary to restrict a user’s ability to copy and paste or upload data to services, devices and storage media outside of the organization. If that is the case, the organization should implement technology such as data leakage prevention tools or the configuration of existing tools that allow users to view and manipulate data held remotely but prevent copy and paste outside of the organization’s control.

If data export is required, the data owner should be allowed to approve the export and hold users accountable for their actions.

Taking screenshots or photographs of the screen should be addressed through terms and conditions of use, training and auditing.

Where data is backed up, care should be taken to ensure sensitive information is protected using measures such as encryption, access control and physical protection of the storage media holding the backup.

Data leakage prevention should also be considered to protect against the intelligence actions of an adversary from obtaining confidential or secret information (geopolitical, human, financial, commercial, scientific or any other) which can be of interest for espionage or can be critical for the community. The data leakage prevention actions should be oriented to confuse the adversary’s decisions for example by replacing authentic information with false information, either as an independent action or as response to the adversary’s intelligence actions. Examples of these kinds of actions are reverse social engineering or the use of honeypots to attract attackers.

**Other information:**
Data leakage prevention tools are designed to identify data, monitor data usage and movement, and take actions to prevent data from leaking (e.g. alerting users to their risky behaviour and blocking the transfer of data to portable storage devices).

Data leakage prevention inherently involves monitoring personnel’s communications and online activities, and by extension external party messages, which raises legal concerns that should be considered prior to deploying data leakage prevention tools. There is a variety of legislation relating to privacy, data protection, employment, interception of data and telecommunications that is applicable to monitoring and data processing in the context of data leakage prevention.

Data leakage prevention can be supported by standard security controls, such as topic-specific policies on access control and secure document management (see 5.12 and 5.15).

---
**Section:** 8.13
**Title:** Information backup

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Corrective |
| Information security properties | #Integrity #Availability |
| Cybersecurity concepts | #Recover |
| Operational capabilities | #Continuity |
| Security domains | #Protection |

**Control:**
Backup copies of information, software and systems should be maintained and regularly tested in accordance with the agreed topic-specific policy on backup.

**Purpose:**
To enable recovery from loss of data or systems.

**Guidance:**
A topic-specific policy on backup should be established to address the organization’s data retention and information security requirements.

Adequate backup facilities should be provided to ensure that all essential information and software can be recovered following an incident or failure or loss of storage media.

Plans should be developed and implemented for how the organization will back up information, software and systems, to address the topic-specific policy on backup.

When designing a backup plan, the following items should be taken into consideration:
- producing accurate and complete records of the backup copies and documented restoration procedures;
- reflecting the business requirements of the organization (e.g. the recovery point objective, see 5.30), the security requirements of the information involved and the criticality of the information to the continued operation of the organization in the extent (e.g. full or differential backup) and frequency of backups;
- storing the backups in a safe and secure remote location, at a sufficient distance to escape any damage from a disaster at the main site;
- giving backup information an appropriate level of physical and environmental protection (see Clause 7 and 8.1) consistent with the standards applied at the main site;
- regularly testing backup media to ensure that they can be relied on for emergency use when necessary. Testing the ability to restore backed-up data onto a test system, not by overwriting the original storage media in case the backup or restoration process fails and causes irreparable data damage or loss;
- protecting backups by means of encryption according to the identified risks (e.g. in situations where confidentiality is of importance);
- taking care to ensure that inadvertent data loss is detected before backup is taken.

Operational procedures should monitor the execution of backups and address failures of scheduled backups to ensure completeness of backups according to the topic-specific policy on backups.

Backup measures for individual systems and services should be regularly tested to ensure that they meet the objectives of incident response and business continuity plans (see 5.30). This should be combined with a test of the restoration procedures and checked against the restoration time required by the business continuity plan. In the case of critical systems and services, backup measures should cover all systems information, applications and data necessary to recover the complete system in the event of a disaster.

When the organization uses a cloud service, backup copies of the organization’s information, applications and systems in the cloud service environment should be taken. The organization should determine if and how requirements for backup are fulfilled when using the information backup service provided as part of the cloud service.

The retention period for essential business information should be determined, taking into account any requirement for retention of archive copies. The organization should consider the deletion of information (see 8.10) in storage media used for backup once the information’s retention period expires and should take into consideration legislation and regulations.

**Other information:**
For further information on storage security including retention consideration, see ISO/IEC 27040.