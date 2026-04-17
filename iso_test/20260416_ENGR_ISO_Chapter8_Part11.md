### A. Tài liệu gốc của Chương 8 (Control 8.16, 8.17)

### B. Summary Overview của Chương 8 (Control 8.16, 8.17)
Tài liệu này mô tả chi tiết **mục 8.16 và 8.17** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào việc giám sát hoạt động bất thường trên hệ thống và đồng bộ thời gian giữa các hệ thống để phục vụ phân tích sự kiện.
Mục tiêu là **phát hiện sớm dấu hiệu tấn công hoặc lỗi vận hành, đồng thời bảo đảm dấu thời gian đủ chính xác để tương quan log và điều tra sự cố**.
Gồm 2 mục chính:
- `8.16`: Monitoring activities - giám sát hoạt động để phát hiện hành vi bất thường
- `8.17`: Clock synchronization - đồng bộ đồng hồ hệ thống với nguồn thời gian được chấp thuận

Áp dụng cho hệ thống, ứng dụng, mạng, công cụ giám sát, log, SIEM, và mọi môi trường cần phát hiện bất thường hoặc bảo đảm timestamp đáng tin cậy.

### C. Key Points của Chương 8 (Control 8.16, 8.17)
- **Mục tiêu quản trị:** `8.16` giúp phát hiện anomaly, compromise hoặc tấn công đang diễn ra; `8.17` giúp dữ liệu sự kiện có timestamp đáng tin cậy để phân tích và chứng minh.
- **Yêu cầu chính của 8.16:** Tổ chức phải xác định phạm vi giám sát, baseline bình thường, cảnh báo tự động và quy trình phản ứng với alert hoặc bất thường phát hiện được.
- **Yêu cầu chính của 8.17:** Các hệ thống xử lý thông tin phải được đồng bộ với nguồn thời gian đã phê duyệt để bảo đảm log và sự kiện có thể tương quan chính xác.
- **Điểm vận hành quan trọng:** `8.16` cần kết hợp log, network traffic, UEBA, threat intelligence và monitoring liên tục; `8.17` cần nguồn thời gian tin cậy, NTP/PTP hoặc nguồn clock tham chiếu.
- **Lưu ý thực tế:** Trong môi trường cloud hoặc kết hợp cloud/on-premises, chênh lệch thời gian giữa các hệ thống phải được theo dõi vì có thể làm sai lệch điều tra và phân tích.

### D. Deep Summary của Chương 8 (Control 8.16, 8.17)
**Bối cảnh:**
Hai control này là cặp đôi nền tảng cho năng lực phát hiện và điều tra trong môi trường số. Nếu không giám sát liên tục, tổ chức có thể bỏ lỡ dấu hiệu xâm nhập, malware hoặc hoạt động bất thường. Nếu đồng hồ không đồng bộ, các log dù có đầy đủ cũng khó ghép lại thành chuỗi sự kiện đáng tin cậy. Vì vậy, giám sát và đồng bộ thời gian là hai điều kiện cơ bản để biến dữ liệu vận hành thành bằng chứng và cảnh báo.

**Nội dung cốt lõi:**
- `8.16` yêu cầu theo dõi lưu lượng mạng, truy cập hệ thống, cấu hình, log từ security tools và resource usage để phát hiện hành vi bất thường.
- `8.16` đòi hỏi xây dựng baseline normal behavior, sau đó cấu hình hệ thống giám sát để phát hiện lệch chuẩn như malware activity, brute force, scanning, overload hoặc unauthorized access.
- `8.16` nhấn mạnh alerting, tuning để giảm false positives, phân công người phản ứng và có dự phòng để nhận và xử lý cảnh báo.
- `8.17` yêu cầu đồng bộ đồng hồ với nguồn thời gian được chấp thuận để bảo đảm mọi log và sự kiện có thể được correlation chính xác giữa các hệ thống.
- `8.17` đặc biệt quan trọng với môi trường cloud và các hệ thống đa miền, nơi chênh lệch clock có thể gây sai lệch điều tra hoặc làm giảm giá trị chứng cứ.

**Dữ liệu đáng chú ý:**
- `8.16` là kiểm soát `#Detective #Corrective`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Information_security_event_management` và miền `#Defence`.
- `8.17` là kiểm soát `#Detective`, gắn với `#Integrity`, thuộc `#Information_security_event_management` và miền `#Protection#Defence`.
- `8.16` có thể dùng SIEM, IDS, UEBA, threat intelligence và logging để xây dựng năng lực phát hiện.
- `8.17` cần standard reference time, NTP hoặc PTP và có thể dùng hai nguồn thời gian ngoài để tăng độ tin cậy.
- `8.16` và `8.17` cùng hỗ trợ điều tra sự cố, nhưng `8.17` chủ yếu bảo đảm chất lượng của bằng chứng thời gian.

**Rủi ro / Lưu ý:**
- Nếu baseline không đúng, hệ thống giám sát sẽ sinh quá nhiều false positives hoặc bỏ sót bất thường thực sự.
- Nếu alert không được xử lý bởi người có năng lực, giám sát sẽ không chuyển thành phản ứng kịp thời.
- Nếu đồng hồ không đồng bộ, log giữa các hệ thống sẽ lệch nhau và khó chứng minh thứ tự sự kiện.
- Nếu cloud service hoặc hệ thống lai không được theo dõi chênh lệch thời gian, sự cố có thể bị phân tích sai hoặc thiếu bằng chứng.

### E. Structured Output của Chương 8 (Control 8.16, 8.17)
**Section:** 8.16
**Title:** Monitoring activities

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Detective #Corrective |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Detect #Respond |
| Operational capabilities | #Information_security_event_management |
| Security domains | #Defence |

**Control:**
Networks, systems and applications should be monitored for anomalous behaviour and appropriate actions taken to evaluate potential information security incidents.

**Purpose:**
To detect anomalous behaviour and potential information security incidents.

**Guidance:**
The monitoring scope and level should be determined in accordance with business and information security requirements and taking into consideration relevant laws and regulations. Monitoring records should be maintained for defined retention periods.

The following should be considered for inclusion within the monitoring system:
- outbound and inbound network, system and application traffic;
- access to systems, servers, networking equipment, monitoring system, critical applications, etc.;
- critical or admin level system and network configuration files;
- logs from security tools [e.g. antivirus, IDS, intrusion prevention system (IPS), web filters, firewalls, data leakage prevention];
- event logs relating to system and network activity;
- checking that the code being executed is authorized to run in the system and that it has not been tampered with (e.g. by recompilation to add additional unwanted code);
- use of the resources (e.g. CPU, hard disks, memory, bandwidth) and their performance.

The organization should establish a baseline of normal behaviour and monitor against this baseline for anomalies. When establishing a baseline, the following should be considered:
- reviewing utilization of systems at normal and peak periods;
- usual time of access, location of access, frequency of access for each user or group of users.

The monitoring system should be configured against the established baseline to identify anomalous behaviour, such as:
- unplanned termination of processes or applications;
- activity typically associated with malware or traffic originating from known malicious IP addresses or network domains (e.g. those associated with botnet command and control servers);
- known attack characteristics (e.g. denial of service and buffer overflows);
- unusual system behaviour (e.g. keystroke logging, process injection and deviations in use of standard protocols);
- bottlenecks and overloads (e.g. network queuing, latency levels and network jitter);
- unauthorized access (actual or attempted) to systems or information;
- unauthorized scanning of business applications, systems and networks;
- successful and unsuccessful attempts to access protected resources (e.g. DNS servers, web portals and file systems);
- unusual user and system behaviour in relation to expected behaviour.

Continuous monitoring via a monitoring tool should be used. Monitoring should be done in real time or in periodic intervals, subject to organizational need and capabilities. Monitoring tools should include the ability to handle large amounts of data, adapt to a constantly changing threat landscape, and allow for real-time notification. The tools should also be able to recognize specific signatures and data or network or application behaviour patterns.

Automated monitoring software should be configured to generate alerts (e.g. via management consoles, email messages or instant messaging systems) based on predefined thresholds. The alerting system should be tuned and trained on the organization’s baseline to minimize false positives. Personnel should be dedicated to respond to alerts and should be properly trained to accurately interpret potential incidents. There should be redundant systems and processes in place to receive and respond to alert notifications.

Abnormal events should be communicated to relevant parties in order to improve the following activities: auditing, security evaluation, vulnerability scanning and monitoring (see 5.25). Procedures should be in place to respond to positive indicators from the monitoring system in a timely manner, in order to minimize the effect of adverse events (see 5.26) on information security. Procedures should also be established to identify and address false positives including tuning the monitoring software to reduce the number of future false positives.

**Other information:**
Security monitoring can be enhanced by:
- leveraging threat intelligence systems (see 5.7);
- leveraging machine learning and artificial intelligence capabilities;
- using blocklists or allowlists;
- undertaking a range of technical security assessments (e.g. vulnerability assessments, penetration testing, cyber-attack simulations and cyber response exercises), and using the results of these assessments to help determine baselines or acceptable behaviour;
- using performance monitoring systems to help establish and detect anomalous behaviour;
- leveraging logs in combination with monitoring systems.

Monitoring activities are often conducted using specialist software, such as intrusion detection systems. These can be configured to a baseline of normal, acceptable and expected system and network activities.

Monitoring for anomalous communications helps in the identification of botnets (i.e. set of devices under the malicious control of the botnet owner, usually used for mounting distributed denial of service attacks on other computers of other organizations). If the computer is being controlled by an external device, there is a communication between the infected device and the controller. The organization should therefore employ technologies to monitor for anomalous communications and take such action as necessary.

---
**Section:** 8.17
**Title:** Clock synchronization

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Detective |
| Information security properties | #Integrity |
| Cybersecurity concepts | #Protect #Detect |
| Operational capabilities | #Information_security_event_management |
| Security domains | #Protection #Defence |

**Control:**
The clocks of information processing systems used by the organization should be synchronized to approved time sources.

**Purpose:**
To enable the correlation and analysis of security-related events and other recorded data, and to support investigations into information security incidents.

**Guidance:**
External and internal requirements for time representation, reliable synchronization and accuracy should be documented and implemented. Such requirements can be from legal, statutory, regulatory, contractual, standards and internal monitoring needs. A standard reference time for use within the organization should be defined and considered for all systems, including building management systems, entry and exit systems and others that can be used to aid investigations.

A clock linked to a radio time broadcast from a national atomic clock or global positioning system (GPS) should be used as the reference clock for logging systems; a consistent, trusted date and time source to ensure accurate time-stamps. Protocols such as network time protocol (NTP) or precision time protocol (PTP) should be used to keep all networked systems in synchronization with a reference clock.

The organization can use two external time sources at the same time in order to improve the reliability of external clocks, and appropriately manage any variance.

Clock synchronization can be difficult when using multiple cloud services or when using both cloud and on-premises services. In this case, the clock of each service should be monitored and the difference recorded in order to mitigate risks arising from discrepancies.

**Other information:**
The correct setting of computer clocks is important to ensure the accuracy of event logs, which can be required for investigations or as evidence in legal and disciplinary cases. Inaccurate audit logs can hinder such investigations and damage the credibility of such evidence.