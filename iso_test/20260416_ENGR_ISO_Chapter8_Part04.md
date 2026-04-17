### A. Tài liệu gốc của Chương 8 (Control 8.6, 8.7)

### B. Summary Overview của Chương 8 (Control 8.6, 8.7)
Tài liệu này mô tả chi tiết **mục 8.6 và 8.7** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào việc quản lý năng lực hạ tầng và bảo vệ hệ thống trước malware.
Mục tiêu là **bảo đảm hệ thống có đủ tài nguyên để vận hành ổn định, đồng thời phòng ngừa, phát hiện và xử lý mã độc trước khi gây gián đoạn hoặc lây lan**.
Gồm 2 mục chính:
- `8.6`: Capacity management - quản lý năng lực và tài nguyên hệ thống theo nhu cầu hiện tại và tương lai
- `8.7`: Protection against malware - bảo vệ hệ thống, dữ liệu và thiết bị trước malware

Áp dụng cho hạ tầng công nghệ, nhân sự vận hành, hệ thống, thiết bị đầu cuối, email, web, phương tiện lưu trữ và môi trường sản xuất hoặc hỗ trợ nghiệp vụ quan trọng.

### C. Key Points của Chương 8 (Control 8.6, 8.7)
- **Mục tiêu quản trị:** `8.6` giảm rủi ro thiếu tài nguyên hoặc nghẽn hệ thống; `8.7` giảm rủi ro mã độc xâm nhập, lan rộng và làm hỏng hoặc chiếm quyền hệ thống.
- **Yêu cầu chính của 8.6:** Tổ chức phải theo dõi, dự báo và điều chỉnh năng lực tài nguyên theo nhu cầu thực tế và nhu cầu tương lai, bao gồm con người, không gian, hệ thống xử lý và các dịch vụ hỗ trợ.
- **Yêu cầu chính của 8.7:** Cần có malware protection dựa trên công cụ phát hiện/sửa chữa, hardening hệ thống, cập nhật thường xuyên, scanning định kỳ và awareness cho người dùng.
- **Điểm vận hành quan trọng:** `8.6` không chỉ là capacity của máy chủ mà còn là năng lực tổng thể của tổ chức; `8.7` không thể dựa vào antivirus đơn lẻ mà phải kết hợp allowlisting, blocklisting, kiểm soát thay đổi và backup khôi phục.
- **Lưu ý thực tế:** Khi cần tắt tạm biện pháp chống malware vì ảnh hưởng vận hành, tổ chức phải có cơ chế phê duyệt ngoại lệ, justification và review date rõ ràng.

### D. Deep Summary của Chương 8 (Control 8.6, 8.7)
**Bối cảnh:**
Hai control này giải quyết hai dạng rủi ro nền trong vận hành công nghệ: thiếu công suất và nhiễm mã độc. Nếu không quản lý capacity, hệ thống sẽ chậm, gián đoạn hoặc đổ vỡ vào thời điểm tải cao. Nếu không có lớp phòng vệ malware phù hợp, tổ chức có thể mất dữ liệu, mất tính sẵn sàng hoặc bị chiếm quyền thông qua email, file, website hay thiết bị lưu trữ.

**Nội dung cốt lõi:**
- `8.6` yêu cầu xác định nhu cầu năng lực cho hệ thống, nhân sự, văn phòng và các cơ sở khác, rồi theo dõi sử dụng tài nguyên để phát hiện sớm giới hạn hoặc phụ thuộc rủi ro.
- `8.6` đòi hỏi stress-test, theo dõi xu hướng, và lập kế hoạch tăng hoặc giảm nhu cầu thông qua mở rộng tài nguyên, thuê thêm người, dùng cloud hoặc loại bỏ nhu cầu không còn cần thiết.
- `8.7` yêu cầu một tập hợp biện pháp phòng thủ nhiều lớp: công cụ chống malware, allowlisting/blocklisting, giảm lỗ hổng, kiểm tra tự động, scanning email/attachment/web và cảnh báo sự kiện.
- `8.7` cũng yêu cầu kiểm soát chặt việc vô hiệu hóa tạm thời các biện pháp bảo vệ, vì đây là điểm yếu dễ bị khai thác khi hoạt động bình thường gặp gián đoạn.
- `8.7` nhấn mạnh đào tạo người dùng, thu thập thông tin malware mới và dùng nguồn thông tin đáng tin cậy để cập nhật khả năng phòng vệ.

**Dữ liệu đáng chú ý:**
- `8.6` là kiểm soát `#Preventive #Detective`, gắn với `#Integrity`, `#Availability`, thuộc `#Continuity` và miền `#Governance_and_Ecosystem #Protection`.
- `8.7` là kiểm soát `#Preventive #Detective #Corrective`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#System_and_network_security#Information_protection` và miền `#Protection#Defence`.
- `8.6` nhấn mạnh cả capacity của hạ tầng lẫn phụ thuộc vào key personnel, nên là vấn đề kỹ thuật và tổ chức cùng lúc.
- `8.7` có thể cần các backup online/offline và kế hoạch khôi phục khi malware làm hỏng hệ thống hoặc firmware.
- `8.7` nêu rõ không phải hệ thống nào cũng cài được phần mềm chống malware, ví dụ một số industrial control systems.

**Rủi ro / Lưu ý:**
- Nếu capacity management yếu, hệ thống có thể bị quá tải vào lúc cao điểm, gây gián đoạn dịch vụ hoặc làm sụp các quy trình nghiệp vụ quan trọng.
- Nếu không theo dõi xu hướng sử dụng tài nguyên, tổ chức sẽ chỉ phản ứng khi đã có sự cố thay vì chủ động mở rộng hoặc giảm nhu cầu.
- Nếu phòng vệ malware chỉ dừng ở một công cụ duy nhất, tổ chức dễ bị qua mặt bởi biến thể mới, file nén, kênh truyền bất thường hoặc tấn công vào firmware.
- Nếu ngoại lệ tắt chống malware không được phê duyệt và theo dõi, tổ chức có thể tự tạo cửa hậu cho tấn công trong lúc vận hành.

### E. Structured Output của Chương 8 (Control 8.6, 8.7)
**Section:** 8.6
**Title:** Capacity management

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive #Detective |
| Information security properties | #Integrity #Availability |
| Cybersecurity concepts | #Identify #Protect #Detect |
| Operational capabilities | #Continuity |
| Security domains | #Governance_and_Ecosystem #Protection |

**Control:**
The use of resources should be monitored and adjusted in line with current and expected capacity requirements.

**Purpose:**
To ensure the required capacity of information processing facilities, human resources, offices and other facilities.

**Guidance:**
Capacity requirements for information processing facilities, human resources, offices and other facilities should be identified, taking into account the business criticality of the concerned systems and processes.

System tuning and monitoring should be applied to ensure and, where necessary, improve the availability and efficiency of systems.

The organization should perform stress-tests of systems and services to confirm that sufficient system capacity is available to meet peak performance requirements.

Detective controls should be put in place to indicate problems in due time.

Projections of future capacity requirements should take account of new business and system requirements and current and projected trends in the organization’s information processing capabilities.

Particular attention should be paid to any resources with long procurement lead times or high costs.   
Therefore, managers, service or product owners should monitor the utilization of key system resources.

Managers should use capacity information to identify and avoid potential resource limitations and dependency on key personnel which can present a threat to system security or services and plan appropriate action.

Providing sufficient capacity can be achieved by increasing capacity or by reducing demand. The following should be considered to increase capacity:
- hiring new personnel;
- obtaining new facilities or space;
- acquiring more powerful processing systems, memory and storage;
- making use of cloud computing, which has inherent characteristics that directly address issues of capacity. Cloud computing has elasticity and scalability which enable on-demand rapid expansion and reduction in resources available to particular applications and services.

The following should be considered to reduce demand on the organization’s resources:
- deletion of obsolete data (disk space);
- disposal of hardcopy records that have met their retention period (free up shelving space);
- decommissioning of applications, systems, databases or environments;
- optimizing batch processes and schedules;
- optimizing application code or database queries;
- denying or restricting bandwidth for resource-consuming services if these are not critical (e.g. video streaming).

A documented capacity management plan should be considered for mission critical systems.

**Other information:**
For more detail on the elasticity and scalability of cloud computing, see ISO/IEC TS 23167.

---
**Section:** 8.7
**Title:** Protection against malware

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive #Detective #Corrective |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect #Detect |
| Operational capabilities | #System_and_network_security #Information_protection |
| Security domains | #Protection #Defence |

**Control:**
Protection against malware should be implemented and supported by appropriate user awareness.

**Purpose:**
To ensure information and other associated assets are protected against malware.

**Guidance:**
Protection against malware should be based on malware detection and repair software, information security awareness, appropriate system access and change management controls. Use of malware detection and repair software alone is not usually adequate. The following guidance should be considered:
- implementing rules and controls that prevent or detect the use of unauthorized software [e.g. application allowlisting (i.e. using a list providing allowed applications)] (see 8.19 and 8.32);
- implementing controls that prevent or detect the use of known or suspected malicious websites (e.g. blocklisting);
- reducing vulnerabilities that can be exploited by malware [e.g. through technical vulnerability management (see 8.8 and 8.19)];
- conducting regular automated validation of the software and data content of systems, especially for systems supporting critical business processes; investigating the presence of any unapproved files or unauthorized amendments;
- establishing protective measures against risks associated with obtaining files and software either from or via external networks or on any other medium;
- installing and regularly updating malware detection and repair software to scan computers and electronic storage media. Carrying out regular scans that include:
  1. scanning any data received over networks or via any form of electronic storage media, for malware before use;
  2. scanning email and instant messaging attachments and downloads for malware before use. Carrying out this scan at different places (e.g. at email servers, desktop computers) and when entering the network of the organization;
  3. scanning webpages for malware when accessed;
- determining the placement and configuration of malware detection and repair tools based on risk assessment outcomes and considering:
  1. defence in depth principles where they would be most effective. For example, this can lead to malware detection in a network gateway (in various application protocols such as email, file transfer and web) as well as user endpoint devices and servers;
  2. the evasive techniques of attackers (e.g. the use of encrypted files) to deliver malware or the use of encryption protocols to transmit malware;
- taking care to protect against the introduction of malware during maintenance and emergency procedures, which can bypass normal controls against malware;
- implementing a process to authorize temporarily or permanently disable some or all measures against malware, including exception approval authorities, documented justification and review date. This can be necessary when the protection against malware causes disruption to normal operations;
- preparing appropriate business continuity plans for recovering from malware attacks, including all necessary data and software backup (including both online and offline backup) and recovery measures (see 8.13);
- isolating environments where catastrophic consequences can occur;
- defining procedures and responsibilities to deal with protection against malware on systems, including training in their use, reporting and recovering from malware attacks;
- providing awareness or training (see 6.3) to all users on how to identify and potentially mitigate the receipt, sending or installation of malware infected emails, files or programs [the information collected in n) and o) can be used to ensure awareness and training are kept up-to-date];
- implementing procedures to regularly collect information about new malware, such as subscribing to mailing lists or reviewing relevant websites;
- verifying that information relating to malware, such as warning bulletins, comes from qualified and reputable sources (e.g. reliable internet sites or suppliers of malware detection software) and is accurate and informative.

**Other information:**
It is not always possible to install software that protects against malware on some systems (e.g. some industrial control systems). Some forms of malware infect computer operating systems and computer firmware such that common malware controls cannot clean the system and a full reimaging of the operating system software and sometimes the computer firmware is necessary to return to a secure state.