### A. Tài liệu gốc của Chương 8 (Control 8.15)

### B. Summary Overview của Chương 8 (Control 8.15)
Tài liệu này mô tả chi tiết **mục 8.15** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào việc ghi log các hoạt động, bảo vệ log và phân tích log để phát hiện sự kiện an toàn thông tin.
Mục tiêu là **tạo dấu vết đáng tin cậy để điều tra, giám sát và phát hiện sớm hành vi bất thường hoặc sự cố an toàn thông tin**.
Gồm 1 mục chính:
- `8.15`: Logging - ghi nhận, bảo vệ và phân tích log cho mục đích giám sát và điều tra

Áp dụng cho hệ thống, ứng dụng, thiết bị, hạ tầng mạng, môi trường vật lý và các luồng sự kiện cần được theo dõi để phục vụ phát hiện, điều tra và audit.

### C. Key Points của Chương 8 (Control 8.15)
- **Mục tiêu quản trị:** `8.15` tạo khả năng truy vết, phát hiện bất thường và cung cấp bằng chứng cho điều tra sự cố hoặc kiểm toán.
- **Yêu cầu chính:** Tổ chức phải xác định mục đích logging, dữ liệu nào cần ghi, cách bảo vệ log và cách phân tích log theo policy rõ ràng.
- **Yêu cầu bảo vệ log:** Log phải được bảo vệ khỏi sửa, xóa, vô hiệu hóa hoặc ghi đè trái phép, kể cả bởi người có quyền đặc quyền.
- **Yêu cầu phân tích:** Log cần được phân tích kết hợp với SIEM, UEBA, threat intelligence và các nguồn dữ liệu liên quan để tìm dấu hiệu compromise hoặc hành vi bất thường.
- **Lưu ý thực tế:** Log có thể chứa dữ liệu nhạy cảm và PII; do đó cần cân bằng giữa khả năng giám sát, yêu cầu pháp lý và việc de-identify trước khi chia sẻ cho vendor.

### D. Deep Summary của Chương 8 (Control 8.15)
**Bối cảnh:**
Logging là nền tảng của phát hiện và điều tra trong môi trường công nghệ. Nếu không có log, tổ chức gần như không thể chứng minh điều gì đã xảy ra, ai đã làm gì, khi nào và từ đâu. Tuy nhiên, log cũng có thể trở thành nguồn rò rỉ dữ liệu hoặc bị thao túng nếu không được bảo vệ đúng cách, nên logging vừa là công cụ phát hiện vừa là tài sản cần được bảo vệ.

**Nội dung cốt lõi:**
- `8.15` yêu cầu xác định trước mục đích logging, dữ liệu nào cần ghi, ai có trách nhiệm và cách lưu giữ, bảo vệ, phân tích log.
- `8.15` nhấn mạnh rằng log phải bao gồm định danh người dùng, hành động hệ thống, thời gian, thiết bị, địa chỉ mạng và các sự kiện quan trọng như đăng nhập, đổi cấu hình, dùng quyền, tạo/xóa danh tính hay transaction trong ứng dụng.
- `8.15` yêu cầu bảo vệ log khỏi chỉnh sửa, xóa, mất sự kiện hoặc ghi đè, kể cả khi log được lưu trên media có giới hạn dung lượng.
- `8.15` gắn chặt với phân tích log và giám sát liên tục để phát hiện bất thường, outbound kết nối độc hại, dấu hiệu malware hoặc probing vào hệ thống phòng thủ.
- `8.15` cũng phải được áp dụng trong bối cảnh cloud, nơi trách nhiệm quản lý log có thể chia giữa customer và provider.

**Dữ liệu đáng chú ý:**
- `8.15` là kiểm soát `#Detective`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Information_security_event_management` và miền `#Protection#Defence`.
- `8.15` phụ thuộc mạnh vào synchronized time sources để có thể correlating log giữa các hệ thống.
- `8.15` yêu cầu có thể de-identify log trước khi gửi cho vendor để debug hoặc troubleshooting.
- `8.15` có liên hệ với `8.16` về automated monitoring và với `5.25` về incident management.
- `8.15` có thể dùng SIEM, public transparency files hoặc append-only/read-only log files để tăng tính toàn vẹn.

**Rủi ro / Lưu ý:**
- Nếu log không đủ chi tiết hoặc không đồng bộ thời gian, điều tra sự cố sẽ thiếu bằng chứng và khó ghép chuỗi sự kiện.
- Nếu người có đặc quyền có thể xóa hoặc vô hiệu hóa log của chính họ, khả năng truy vết và accountability sẽ giảm mạnh.
- Nếu log chứa dữ liệu nhạy cảm mà không được bảo vệ, bản thân log có thể trở thành một nguồn rò rỉ.
- Nếu phân tích log không được gắn với cảnh báo và quy trình phản ứng, tổ chức sẽ chỉ lưu trữ dữ liệu mà không biến dữ liệu thành phát hiện hữu ích.

### E. Structured Output của Chương 8 (Control 8.15)
**Section:** 8.15
**Title:** Logging

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Detective |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Detect |
| Operational capabilities | #Information_security_event_management |
| Security domains | #Protection #Defence |

**Control:**
Logs that record activities, exceptions, faults and other relevant events should be produced, stored, protected and analysed.

**Purpose:**
To record events, generate evidence, ensure the integrity of log information, prevent against unauthorized access, identify information security events that can lead to an information security incident and to support investigations.

**Guidance:**
***General***
The organization should determine the purpose for which logs are created, what data is collected and logged, and any log-specific requirements for protecting and handling the log data. This should be documented in a topic-specific policy on logging.

Event logs should include for each event, as applicable:
- user IDs;
- system activities;
- dates, times and details of relevant events (e.g. log-on and log-off);
- device identity, system identifier and location;
- network addresses and protocols.

The following events should be considered for logging:
- successful and rejected system access attempts;
- successful and rejected data and other resource access attempts;
- changes to system configuration;
- use of privileges;
- use of utility programs and applications;
- files accessed and the type of access, including deletion of important data files;
- alarms raised by the access control system;
- activation and de-activation of security systems, such as anti-virus systems and intrusion detection systems;
- creation, modification or deletion of identities;
- transactions executed by users in applications. In some cases, the applications are a service or product provided or run by a third party.

It is important for all systems to have synchronized time sources (see 8.17) as this allows for correlation of logs between systems for analysis, alerting and investigation of an incident.

***Protection of logs***
Users, including those with privileged access rights, should not have permission to delete or de-activate logs of their own activities. They can potentially manipulate the logs on information processing facilities under their direct control. Therefore, it is necessary to protect and review the logs to maintain accountability for the privileged users.

Controls should aim to protect against unauthorized changes to log information and operational problems with the logging facility including:
- alterations to the message types that are recorded;
- log files being edited or deleted;
- failure to record events or over-writing of past recorded events if the storage media holding a log file is exceeded.

For protection of logs, the use of the following techniques should be considered: cryptographic hashing, recording in an append-only and read-only file, recording in a public transparency file.

Some audit logs can be required to be archived because of requirements on data retention or requirements to collect and retain evidence (see 5.28).

Where the organization needs to send system or application logs to a vendor to assist with debugging or troubleshooting errors, logs should be de-identified where possible using data masking techniques (see 8.11) for information such as usernames, internet protocol (IP) addresses, hostnames or organization name, before sending to the vendor.

Event logs can contain sensitive data and personally identifiable information. Appropriate privacy protection measures should be taken (see 5.34).

***Log analysis***
Log analysis should cover the analysis and interpretation of information security events, to help identify unusual activity or anomalous behaviour, which can represent indicators of compromise.

Analysis of events should be performed by taking into account:
- the necessary skills for the experts performing the analysis;
- determining the procedure of log analysis;
- the required attributes of each security-related event;
- exceptions identified through the use of predetermined rules [e.g. security information and event management (SIEM) or firewall rules, and intrusion detection systems (IDSs) or malware signatures];
- known behaviour patterns and standard network traffic compared to anomalous activity and behaviour [user and entity behaviour analytics (UEBA)];
- results of trend or pattern analysis (e.g. as a result of using data analytics, big data techniques and specialized analysis tools);
- available threat intelligence.

Log analysis should be supported by specific monitoring activities to help identify and analyse anomalous behaviour, which includes:
- reviewing successful and unsuccessful attempts to access protected resources [e.g. domain name system (DNS) servers, web portals and file shares];
- checking DNS logs to identify outbound network connections to malicious servers, such as those associated with botnet command and control servers;
- examining usage reports from service providers (e.g. invoices or service reports) for unusual activity within systems and networks (e.g. by reviewing patterns of activity);
- including event logs of physical monitoring such as entrance and exit to ensure more accurate detection and incident analysis;
- correlating logs to enable efficient and highly accurate analysis.

Suspected and actual information security incidents should be identified (e.g. malware infection or probing of firewalls) and be subject to further investigation (e.g. as part of an information security incident management process, see 5.25).

**Other information:**
System logs often contain a large volume of information, much of which is extraneous to information security monitoring. To help identify significant events for information security monitoring purposes, the use of suitable utility programs or audit tools to perform file interrogation can be considered.

Event logging sets the foundation for automated monitoring systems (see 8.16) which are capable of generating consolidated reports and alerts on system security.

A SIEM tool or equivalent service can be used to store, correlate, normalize and analyse log information, and to generate alerts. SIEMs tend to require careful configuration to optimize their benefits. Configurations to consider include identification and selection of appropriate log sources, tuning and testing of rules and development of use cases.

Public transparency files for the recording of logs are used, for example, in certificate transparency systems. Such files can provide an additional detection mechanism useful for guarding against log tampering.

In cloud environments, log management responsibilities can be shared between the cloud service customer and the cloud service provider. Responsibilities vary depending on the type of cloud service being used. Further guidance can be found in ISO/IEC 27017.