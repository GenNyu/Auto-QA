### A. Tài liệu gốc của Chương 6 (Control 6.7, 6.8)

### B. Summary Overview của Chương 6 (Control 6.7, 6.8)
Tài liệu này mô tả chi tiết **mục 6.7 và 6.8** trong **chương 6. People controls** của **ISO/IEC 27002:2022**, tập trung vào việc kiểm soát rủi ro khi nhân sự làm việc từ xa và khi họ phải báo cáo các sự kiện an toàn thông tin.
Mục tiêu là **bảo vệ thông tin ngoài phạm vi văn phòng và bảo đảm tổ chức nhận được thông tin cảnh báo, sự cố và vi phạm kịp thời để phản ứng sớm**.
Gồm 2 mục chính:
- `6.7`: Remote working - kiểm soát an toàn thông tin khi làm việc từ xa
- `6.8`: Information security event reporting - cơ chế báo cáo sự kiện an toàn thông tin

Áp dụng cho mọi nhân sự và người dùng có làm việc từ xa, truy cập từ môi trường ngoài tổ chức, hoặc có trách nhiệm phát hiện và báo cáo sự kiện an toàn thông tin.

### C. Key Points của Chương 6 (Control 6.7, 6.8)
- **Mục tiêu quản trị:** `6.7` giảm rủi ro khi thông tin được xử lý ngoài trụ sở; `6.8` bảo đảm sự cố, vi phạm và dấu hiệu bất thường được báo cáo sớm qua kênh rõ ràng.
- **Yêu cầu chính của 6.7:** Tổ chức phải có chính sách và biện pháp cho làm việc từ xa, bao gồm an toàn vật lý, an toàn mạng, xác thực truy cập, thiết bị, lưu trữ, hỗ trợ và thu hồi quyền khi hoạt động kết thúc.
- **Yêu cầu chính của 6.8:** Tổ chức phải cung cấp cơ chế báo cáo sự kiện dễ dùng, dễ tiếp cận và được truyền thông rõ cho nhân sự, bao gồm cả chỉ dẫn về việc không tự ý thử khai thác lỗ hổng.
- **Điểm vận hành quan trọng:** Môi trường làm việc từ xa cần được xem xét theo loại thiết bị, vị trí làm việc, mạng sử dụng, mức độ nhạy cảm của thông tin và khả năng người khác truy cập trái phép tại chỗ.
- **Lưu ý thực tế:** Báo cáo sớm chỉ hiệu quả khi nhân sự hiểu điều gì cần báo cáo, biết báo cáo cho ai, và không sợ bị quy trách nhiệm chỉ vì đã nêu ra sự cố đúng lúc.

### D. Deep Summary của Chương 6 (Control 6.7, 6.8)
**Bối cảnh:**
Hai control này giải quyết các rủi ro vận hành ngày càng phổ biến khi nhân sự không còn làm việc trong môi trường kiểm soát truyền thống của tổ chức. Một control bảo vệ bề mặt tấn công mở rộng do làm việc từ xa, control còn lại tạo kênh cảnh báo để tổ chức phát hiện sớm sự cố, vi phạm và lỗ hổng.

**Nội dung cốt lõi:**
- `6.7` yêu cầu tổ chức thiết lập topic-specific policy cho remote working, thay vì để nhân sự tự quyết theo thói quen cá nhân.
- `6.7` nhấn mạnh nhiều lớp kiểm soát: an toàn vật lý tại điểm làm việc, bảo mật truyền thông, cấu hình mạng gia đình hoặc mạng công cộng, phòng chống malware, cấp phát và thu hồi quyền truy cập.
- `6.7` cũng đòi hỏi chuẩn bị cho vòng đời thiết bị và hỗ trợ vận hành, gồm cung cấp thiết bị, training, bảo trì, backup, monitoring và thu hồi tài sản khi kết thúc làm việc từ xa.
- `6.8` biến việc phát hiện dấu hiệu bất thường thành nghĩa vụ báo cáo rõ ràng, bao phủ từ sự cố, vi phạm, lỗi người dùng, thay đổi hệ thống không qua quy trình cho đến malware và vulnerability.
- `6.8` đặc biệt cảnh báo không nên tự ý kiểm thử lỗ hổng vì có thể gây hại cho hệ thống, làm hỏng chứng cứ số và kéo theo trách nhiệm pháp lý.

**Dữ liệu đáng chú ý:**
- `6.7` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Asset_management#Information_protection#Physical_security#System_and_network_security` và miền `#Protection`.
- `6.8` là kiểm soát `#Detective`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Information_security_event_management` và miền `#Defence`.
- `6.7` nêu rõ ảnh hưởng của luật và quy định địa phương có thể khiến một số khuyến nghị không áp dụng được nguyên vẹn.
- `6.8` khuyến nghị tham chiếu thêm bộ tiêu chuẩn ISO/IEC 27035 để mở rộng hướng dẫn về quản lý sự kiện và sự cố.
- Cả hai control đều phụ thuộc mạnh vào mức độ truyền thông và khả năng thực thi thực tế của tổ chức, không chỉ vào việc có văn bản chính sách.

**Rủi ro / Lưu ý:**
- Nếu không có policy remote working rõ ràng, nhân sự dễ dùng thiết bị, mạng hoặc phương thức truy cập không được kiểm soát, làm tăng rủi ro rò rỉ thông tin.
- Nếu biện pháp vật lý và kỹ thuật cho làm việc từ xa quá lỏng, người khác tại nhà hoặc nơi công cộng có thể nhìn thấy, sao chép hoặc chiếm quyền truy cập thông tin.
- Nếu cơ chế báo cáo sự kiện khó dùng hoặc nhân sự không biết báo cáo ở đâu, tổ chức sẽ mất tín hiệu sớm và phản ứng chậm với sự cố.
- Nếu nhân sự tự ý thử khai thác lỗ hổng, họ có thể làm hỏng hệ thống hoặc chứng cứ, biến việc báo cáo thành một rủi ro mới.

### E. Structured Output của Chương 6 (Control 6.7, 6.8)
**Section:** 6.7
**Title:** Remote working

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Asset_management #Information_protection #Physical_security #System_and_network_security |
| Security domains | #Protection |

**Control:**
Security measures should be implemented when personnel are working remotely to protect information accessed, processed or stored outside the organization’s premises.

**Purpose:**
To ensure the security of information when personnel are working remotely.

**Guidance:**
Remote working occurs whenever personnel of the organization work from a location outside of the organization’s premises, accessing information whether in hardcopy or electronically via ICT equipment. Remote working environments include those referred to as “teleworking”, “telecommuting”, “flexible workplace”, “virtual work environments" and “remote maintenance”.

***NOTE:*** It is possible that not all the recommendations in this guidance can be applied due to local legislation and regulations in different jurisdictions.

Organizations allowing remote working activities should issue a topic-specific policy on remote working that defines the relevant conditions and restrictions. Where deemed applicable, the following matters should be considered:
- the existing or proposed physical security of the remote working site, taking into account the physical security of the location and the local environment, including the different jurisdictions where personnel are located;
- rules and security mechanisms for the remote physical environment such as lockable filing cabinets, secure transportation between locations and rules for remote access, clear desk, printing and disposal of information and other associated assets, and information security event reporting (see 6.8);
- the expected physical remote working environments;
- the communications security requirements, taking into account the need for remote access to the organization’s systems, the sensitivity of the information to be accessed and passed over the communication link and the sensitivity of the systems and applications;
- the use of remote access such as virtual desktop access that supports processing and storage of information on privately owned equipment;
- the threat of unauthorized access to information or resources from other persons at the remote working site (e.g. family and friends);
- the threat of unauthorized access to information or resources from other persons in public places;
- the use of home networks and public networks, and requirements or restrictions on the configuration of wireless network services;
- use of security measures, such as firewalls and protection against malware;
- secure mechanisms for deploying and initializing systems remotely;
- secure mechanisms for authentication and enablement of access privileges taking into consideration the vulnerability of single-factor authentication mechanisms where remote access to the organization’s network is allowed.

The guidelines and measures to be considered should include:
- the provision of suitable equipment and storage furniture for the remote working activities, where the use of privately-owned equipment that is not under the control of the organization is not allowed;
- a definition of the work permitted, the classification of information that can be held and the internal systems and services that the remote worker is authorized to access;
- the provision of training for those working remotely and those providing support. This should include how to conduct business in a secure manner while working remotely;
- the provision of suitable communication equipment, including methods for securing remote access, such as requirements on device screen locks and inactivity timers; the enabling of device location tracking; installation of remote wipe capabilities;
- physical security;
- rules and guidance on family and visitor access to equipment and information;
- the provision of hardware and software support and maintenance;
- the provision of insurance;
- the procedures for backup and business continuity;
- audit and security monitoring;
- revocation of authority and access rights and the return of equipment when the remote working activities are terminated.

**Other information:**
No other information.

---
**Section:** 6.8
**Title:** Information security event reporting

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Detective |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Detect |
| Operational capabilities | #Information_security_event_management |
| Security domains | #Defence |

**Control:**
The organization should provide a mechanism for personnel to report observed or suspected information security events through appropriate channels in a timely manner.

**Purpose:**
To support timely, consistent and effective reporting of information security events that can be identified by personnel.

**Guidance:**
All personnel and users should be made aware of their responsibility to report information security events as quickly as possible in order to prevent or minimize the effect of information security incidents.

They should also be aware of the procedure for reporting information security events and the point of contact to which the events should be reported. The reporting mechanism should be as easy, accessible and available as possible. Information security events include incidents, breaches and vulnerabilities.

Situations to be considered for information security event reporting include:
- ineffective information security controls;
- breach of information confidentiality, integrity or availability expectations;
- human errors;
- non-compliance with the information security policy, topic-specific policies or applicable standards;
- breaches of physical security measures;
- system changes that have not gone through the change management process;
- malfunctions or other anomalous system behaviour of software or hardware;
- access violations;
- vulnerabilities;
- suspected malware infection.

Personnel and users should be advised not to attempt to prove suspected information security vulnerabilities. Testing vulnerabilities can be interpreted as a potential misuse of the system and can also cause damage to the information system or service, and it can corrupt or obscure digital evidence. Ultimately, this can result in legal liability for the individual performing the testing.

**Other information:**
See the ISO/IEC 27035 series for additional information.