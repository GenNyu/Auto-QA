### A. Tài liệu gốc của Chương 7 (Control 7.4, 7.5, 7.6)

### B. Summary Overview của Chương 7 (Control 7.4, 7.5, 7.6)
Tài liệu này mô tả chi tiết **mục 7.4, 7.5 và 7.6** trong **chương 7. Physical controls** của **ISO/IEC 27002:2022**, tập trung vào giám sát an ninh vật lý, bảo vệ trước các mối đe dọa vật lý và môi trường, và thiết lập quy tắc làm việc trong khu vực an toàn.
Mục tiêu là **phát hiện sớm xâm nhập vật lý trái phép, giảm thiểu tác động của thiên tai hoặc sự cố môi trường, và kiểm soát hành vi của nhân sự trong khu vực nhạy cảm**.
Gồm 3 mục chính:
- `7.4`: Physical security monitoring - giám sát an ninh vật lý liên tục
- `7.5`: Protecting against physical and environmental threats - bảo vệ trước các mối đe dọa vật lý và môi trường
- `7.6`: Working in secure areas - quy tắc làm việc trong khu vực an toàn

Áp dụng cho các cơ sở, phòng, khu vực xử lý thông tin và bất kỳ không gian an toàn nào cần được giám sát, bảo vệ và vận hành theo quy tắc riêng.

### C. Key Points của Chương 7 (Control 7.4, 7.5, 7.6)
- **Mục tiêu quản trị:** Nhóm control này kết hợp phòng ngừa và phát hiện để bảo vệ tài sản vật lý, đồng thời giảm rủi ro từ môi trường tự nhiên, hạ tầng và hành vi người dùng trong khu vực an toàn.
- **Yêu cầu chính của 7.4:** Tổ chức phải giám sát liên tục các khu vực nhạy cảm bằng camera, báo động, cảm biến và cơ chế chống can thiệp, đồng thời bảo vệ dữ liệu giám sát khỏi bị truy cập trái phép.
- **Yêu cầu chính của 7.5:** Trước khi vận hành địa điểm quan trọng, tổ chức phải đánh giá rủi ro vật lý và môi trường, rồi triển khai biện pháp cho các mối đe dọa như cháy, ngập, tăng áp điện, nổ, vũ khí hoặc bất ổn xã hội.
- **Yêu cầu chính của 7.6:** Nhân sự làm việc trong khu vực an toàn phải tuân thủ quy định riêng về thông báo, giám sát, khóa khu vực trống, cấm ghi hình/ghi âm trái phép, kiểm soát thiết bị cá nhân và treo sẵn quy trình khẩn cấp.
- **Lưu ý thực tế:** Các control này phụ thuộc mạnh vào thiết kế địa điểm, sự liên kết giữa bảo vệ vật lý và vận hành, cũng như việc đánh giá định kỳ để điều chỉnh theo mức đe dọa thực tế.

### D. Deep Summary của Chương 7 (Control 7.4, 7.5, 7.6)
**Bối cảnh:**
Nhóm control này bổ sung cho lớp rào chắn và kiểm soát ra vào của phần trước bằng cách tăng khả năng phát hiện, chuẩn bị cho tình huống khẩn cấp và chuẩn hóa hành vi trong khu vực an toàn. Đây là lớp kiểm soát giúp tổ chức không chỉ ngăn truy cập mà còn nhận diện sớm dấu hiệu bất thường và giảm thiệt hại nếu sự cố xảy ra.

**Nội dung cốt lõi:**
- `7.4` yêu cầu hệ thống giám sát liên tục cho các khu vực và tòa nhà chứa hệ thống quan trọng, với camera, cảm biến và báo động được thiết kế theo chuẩn, kiểm tra định kỳ và bảo vệ khỏi bị vô hiệu hóa.
- `7.4` đồng thời nhấn mạnh tính bí mật của thiết kế giám sát, vì nếu kẻ xấu biết hệ thống hoạt động như thế nào thì khả năng đột nhập không bị phát hiện sẽ tăng lên.
- `7.5` yêu cầu đánh giá rủi ro trước khi bắt đầu vận hành và trong các khoảng thời gian phù hợp, vì các mối đe dọa vật lý và môi trường thay đổi theo địa điểm, khí hậu và bối cảnh xã hội.
- `7.5` mở rộng kiểm soát từ phòng cháy chữa cháy, chống ngập, chống tăng áp đến kiểm tra ngẫu nhiên đối với chất nổ hoặc vũ khí ở các khu vực nhạy cảm.
- `7.6` tập trung vào hành vi và kỷ luật vận hành trong khu vực an toàn: cần giới hạn thông tin theo nhu cầu biết, tránh làm việc một mình khi không cần thiết, khóa khu vực trống và cấm thiết bị ghi hình nếu chưa được phép.

**Dữ liệu đáng chú ý:**
- `7.4` là kiểm soát `#Preventive #Detective`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Physical_security` và miền `#Protection#Defence`.
- `7.5` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Physical_security` và miền `#Protection`.
- `7.6` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Physical_security` và miền `#Protection`.
- `7.4` nhấn mạnh rằng thông tin về thiết kế giám sát phải được giữ kín vì có thể hỗ trợ đột nhập không bị phát hiện.
- `7.5` yêu cầu cân nhắc luật, tiêu chuẩn và biện pháp phù hợp khi áp dụng giám sát, cảm biến hoặc kiểm tra an ninh vật lý.

**Rủi ro / Lưu ý:**
- Nếu không có giám sát liên tục, tổ chức có thể phát hiện xâm nhập quá muộn để ngăn thiệt hại hoặc mất chứng cứ.
- Nếu thiết kế hệ thống giám sát bị lộ, kẻ tấn công có thể tìm cách tránh né hoặc vô hiệu hóa các điểm kiểm soát chính.
- Nếu đánh giá rủi ro môi trường không được cập nhật, tổ chức có thể đặt cơ sở quan trọng ở vị trí không phù hợp và chịu thiệt hại lớn khi có thiên tai hoặc sự cố hạ tầng.
- Nếu quy định làm việc trong khu vực an toàn lỏng lẻo, người trong nội bộ có thể vô tình hoặc cố ý ghi nhận, sao chép hoặc làm lộ thông tin nhạy cảm.

### E. Structured Output của Chương 7 (Control 7.4, 7.5, 7.6)
**Section:** 7.4
**Title:** Physical security monitoring

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive #Detective |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect #Detect |
| Operational capabilities | #Physical_security |
| Security domains | #Protection #Defence |

**Control:**
Premises should be continuously monitored for unauthorized physical access.

**Purpose:**
To detect and deter unauthorized physical access.

**Guidance:**
Physical premises should be monitored by surveillance systems, which can include guards, intruder alarms, video monitoring systems such as closed-circuit television and physical security information management software either managed internally or by a monitoring service provider.

Access to buildings that house critical systems should be continuously monitored to detect unauthorized access or suspicious behaviour by:
- installing video monitoring systems such as closed-circuit television to view and record access to sensitive areas within and outside an organization’s premises;
- installing, according to relevant applicable standards, and periodically testing contact, sound or motion detectors to trigger an intruder alarm such as:
  1. installing contact detectors that trigger an alarm when a contact is made or broken in any place where a contact can be made or broken (such as windows and doors and underneath objects) to be used as a panic alarm;
  2. motion detectors based on infra-red technology which trigger an alarm when an object passes through their field of view;
  3. installing sensors sensitive to the sound of breaking glass which can be used to trigger an alarm to alert security personnel;
- using those alarms to cover all external doors and accessible windows. Unoccupied areas should be alarmed at all times; cover should also be provided for other areas (e.g. computer or communications rooms).

The design of monitoring systems should be kept confidential because disclosure can facilitate undetected break-ins.

Monitoring systems should be protected from unauthorized access in order to prevent surveillance information, such as video feeds, from being accessed by unauthorized persons or systems being disabled remotely.

The alarm system control panel should be placed in an alarmed zone and, for safety alarms, in a place that allows an easy exit route for the person who sets the alarm. The control panel and the detectors should have tamperproof mechanisms. The system should regularly be tested to ensure that it is working as intended, particularly if its components are battery powered.

Any monitoring and recording mechanism should be used taking into consideration local laws and regulations including data protection and PII protection legislation, especially regarding the monitoring of personnel and recorded video retention periods.

**Other information:**
No other information.

---
**Section:** 7.5
**Title:** Protecting against physical and environmental threats

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Physical_security |
| Security domains | #Protection |

**Control:**
Protection against physical and environmental threats, such as natural disasters and other intentional or unintentional physical threats to infrastructure should be designed and implemented.

**Purpose:**
To prevent or reduce the consequences of events originating from physical and environmental threats.

**Guidance:**
Risk assessments to identify the potential consequences of physical and environmental threats should be performed prior to beginning critical operations at a physical site, and at regular intervals. Necessary safeguards should be implemented and changes to threats should be monitored. Specialist advice should be obtained on how to manage risks arising from physical and environmental threats such as fire, flood, earthquake, explosion, civil unrest, toxic waste, environmental emissions and other forms of natural disaster or disaster caused by human beings.

Physical premises location and construction should take account of:
- local topography, such as appropriate elevation, bodies of water and tectonic fault lines;
- urban threats, such as locations with a high profile for attracting political unrest, criminal activity or terrorist attacks.

Based on risk assessment results, relevant physical and environmental threats should be identified and appropriate controls considered in the following contexts as examples:
- fire: installing and configuring systems able to detect fires at an early stage to send alarms or trigger fire suppression systems in order to prevent fire damage to storage media and to related information processing systems. Fire suppression should be performed using the most appropriate substance with regard to the surrounding environment (e.g. gas in confined spaces);
- flooding: installing systems able to detect flooding at an early stage under the floors of areas containing storage media or information processing systems. Water pumps or equivalent means should be readily made available in case flooding occurs;
- electrical surges: adopting systems able to protect both server and client information systems against electrical surges or similar events to minimize the consequences of such events;
- explosives and weapons: performing random inspections for the presence of explosives or weapons on personnel, vehicles or goods entering sensitive information processing facilities.

**Other information:**
Safes or other forms of secure storage facilities can protect information stored therein against disasters such as a fire, earthquake, flood or explosion.

Organizations can consider the concepts of crime prevention through environmental design when designing the controls to secure their environment and reduce urban threats. For example, instead of using bollards, statues or water features can serve as both a feature and a physical barrier.

---
**Section:** 7.6
**Title:** Working in secure areas

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Physical_security |
| Security domains | #Protection |

**Control:**
Security measures for working in secure areas should be designed and implemented.

**Purpose:**
To protect information and other associated assets in secure areas from damage and unauthorized interference by personnel working in these areas.

**Guidance:**
The security measures for working in secure areas should apply to all personnel and cover all activities taking place in the secure area.

The following guidelines should be considered:
- making personnel aware only of the existence of, or activities within, a secure area on a need-to-know basis;
- avoiding unsupervised work in secure areas both for safety reasons and to reduce chances for malicious activities;
- physically locking and periodically inspecting vacant secure areas;
- not allowing photographic, video, audio or other recording equipment, such as cameras in user endpoint devices, unless authorized;
- appropriately controlling the carrying and use of user endpoint devices in secure areas;
- posting emergency procedures in a readily visible or accessible manner.

**Other information:**
No other information.