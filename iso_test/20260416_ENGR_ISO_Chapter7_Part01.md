### A. Tài liệu gốc của Chương 7 (Control 7.1, 7.2, 7.3)

### B. Summary Overview của Chương 7 (Control 7.1, 7.2, 7.3)
Tài liệu này mô tả chi tiết **mục 7.1, 7.2 và 7.3** trong **chương 7. Physical controls** của **ISO/IEC 27002:2022**, tập trung vào việc thiết kế lớp bảo vệ vật lý cho khu vực chứa thông tin, kiểm soát ra vào, và bảo đảm văn phòng, phòng làm việc và cơ sở vật chất không bị truy cập trái phép hoặc can thiệp.
Mục tiêu là **ngăn truy cập vật lý trái phép, giảm nguy cơ phá hoại hoặc can thiệp, và bảo vệ thông tin cùng các tài sản liên quan ngay tại môi trường vật lý**.
Gồm 3 mục chính:
- `7.1`: Physical security perimeters - thiết lập và sử dụng chu vi an ninh vật lý
- `7.2`: Physical entry - kiểm soát lối vào và điểm ra vào vật lý
- `7.3`: Securing offices, rooms and facilities - bảo vệ văn phòng, phòng và cơ sở vật chất

Áp dụng cho các địa điểm, tòa nhà, khu vực, phòng và cơ sở chứa hệ thống xử lý thông tin, tài sản thông tin hoặc khu vực nhạy cảm cần kiểm soát truy cập vật lý.

### C. Key Points của Chương 7 (Control 7.1, 7.2, 7.3)
- **Mục tiêu quản trị:** Nhóm control này giảm rủi ro vật lý bằng cách tạo ranh giới bảo vệ rõ ràng, kiểm soát người ra vào và giảm khả năng nhìn thấy, nghe thấy hoặc chạm tới thông tin nhạy cảm.
- **Yêu cầu chính của 7.1:** Tổ chức phải xác định chu vi an ninh, xây dựng rào cản vật lý đủ chắc, bảo vệ cửa ra vào, cửa sổ, mái, thông gió và hệ thống cảnh báo theo mức độ rủi ro của tài sản bên trong.
- **Yêu cầu chính của 7.2:** Tổ chức phải kiểm soát điểm vào, đăng ký và giám sát khách, quản lý nhật ký truy cập, xử lý giao nhận hàng hóa và đảm bảo chỉ người được phép mới tiếp cận khu vực an toàn.
- **Yêu cầu chính của 7.3:** Văn phòng, phòng và cơ sở vật chất phải được bố trí, thiết kế và che chắn sao cho người bên ngoài không dễ dàng quan sát hoặc nghe lén hoạt động, tài liệu hay thông tin xử lý bên trong.
- **Lưu ý thực tế:** Kiểm soát vật lý hiệu quả không chỉ là khóa cửa; nó còn phụ thuộc vào phân luồng giao nhận, quản lý chìa khóa, giám sát khách và khả năng tăng cường kiểm soát khi mức đe dọa thay đổi.

### D. Deep Summary của Chương 7 (Control 7.1, 7.2, 7.3)
**Bối cảnh:**
Đây là nhóm control đặt nền tảng cho an ninh vật lý của môi trường làm việc. Nếu các lớp bảo vệ vật lý không được thiết kế đúng, các kiểm soát logic phía sau sẽ bị vô hiệu hóa rất nhanh vì kẻ tấn công hoặc người không được phép có thể tiếp cận trực tiếp tài sản, thiết bị, tài liệu hoặc khu vực xử lý thông tin.

**Nội dung cốt lõi:**
- `7.1` yêu cầu tổ chức xác định chu vi an ninh vật lý theo tài sản và mức độ nhạy cảm bên trong, rồi xây dựng rào chắn, cửa, tường, mái, cửa sổ và cơ chế báo động phù hợp.
- `7.1` nhấn mạnh rằng chu vi cần đủ chắc để tránh điểm yếu dễ xâm nhập, đồng thời có thể tăng cường khi bối cảnh đe dọa gia tăng.
- `7.2` đi từ kiểm soát điểm vào chung như lối giao nhận đến kiểm soát người ra vào chi tiết như log truy cập, xác thực, khách ra vào và quản lý chìa khóa hoặc thông tin xác thực vật lý.
- `7.2` đặc biệt quan tâm đến visitor management và delivery/loading areas vì đây là những điểm thường bị bỏ sót nhưng lại dễ trở thành cửa hậu cho xâm nhập trái phép.
- `7.3` chuyển trọng tâm sang việc thiết kế không gian làm việc sao cho thông tin mật không bị lộ qua tầm nhìn, âm thanh hoặc tài liệu dễ tiếp cận; với khu vực nhạy cảm, yếu tố che chắn điện từ cũng có thể cần xem xét.

**Dữ liệu đáng chú ý:**
- `7.1`, `7.2` và `7.3` đều là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc nhóm `#Physical_security` hoặc kết hợp với `#Identity_and_Access_Management` và `#Asset_management`.
- `7.1` thuộc miền `#Protection`; `7.2` cũng thuộc `#Protection`; `7.3` thuộc `#Protection`.
- `7.2` yêu cầu quản lý cả access rights vật lý và audit trail/logbook, tức là có phần kỹ thuật và phần bằng chứng vận hành.
- `7.2` và `7.3` đều gợi ý rằng các kiểm soát phải được thiết kế theo ngữ cảnh địa điểm, không áp dụng một mẫu chung cho mọi cơ sở.
- Một số biện pháp ở `7.2` liên quan đến luật địa phương, ví dụ khi kiểm tra đồ cá nhân của nhân sự hoặc khách.

**Rủi ro / Lưu ý:**
- Nếu chu vi vật lý không rõ ràng hoặc quá yếu, người không được phép có thể tiếp cận trực tiếp hệ thống, tài sản hoặc khu vực lưu giữ thông tin.
- Nếu khách, nhà cung cấp hoặc giao nhận hàng hóa không được kiểm soát chặt, khu vực nhạy cảm có thể bị lộ đường vào mà tổ chức không nhận ra kịp thời.
- Nếu quản lý chìa khóa, thẻ ra vào hoặc nhật ký truy cập lỏng lẻo, tổ chức sẽ khó truy vết sự cố và khó chứng minh ai đã vào khu vực nào, lúc nào.
- Nếu văn phòng hoặc phòng máy bị lộ thông tin qua tầm nhìn, âm thanh hoặc sơ đồ vị trí công khai, bí mật vận hành có thể bị rò rỉ mà không cần xâm nhập trực tiếp.

### E. Structured Output của Chương 7 (Control 7.1, 7.2, 7.3)
**Section:** 7.1
**Title:** Physical security perimeters

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Physical_security |
| Security domains | #Protection |

**Control:**
Security perimeters should be defined and used to protect areas that contain information and other associated assets.

**Purpose:**
To prevent unauthorized physical access, damage and interference to the organization’s information and other associated assets.

**Guidance:**
The following guidelines should be considered and implemented where appropriate for physical security perimeters:
- defining security perimeters and the siting and strength of each of the perimeters in accordance with the information security requirements related to the assets within the perimeter;
- having physically sound perimeters for a building or site containing information processing facilities (i.e. there should be no gaps in the perimeter or areas where a break-in can easily occur). The exterior roofs, walls, ceilings and flooring of the site should be of solid construction and all external doors should be suitably protected against unauthorized access with control mechanisms (e.g. bars, alarms, locks). Doors and windows should be locked when unattended and external protection should be considered for windows, particularly at ground level; ventilation points should also be considered;
- alarming, monitoring and testing all fire doors on a security perimeter in conjunction with the walls to establish the required level of resistance in accordance with suitable standards. They should operate in a failsafe manner.

**Other information:**
Physical protection can be achieved by creating one or more physical barriers around the organization’s premises and information processing facilities.

A secure area can be a lockable office or several rooms surrounded by a continuous internal physical security barrier. Additional barriers and perimeters to control physical access can be necessary between areas with different security requirements inside the security perimeter. The organization should consider having physical security measures that can be strengthened during increased threat situations.

---
**Section:** 7.2
**Title:** Physical entry

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Physical_security #Identity_and_Access_Management |
| Security domains | #Protection |

**Control:**
Secure areas should be protected by appropriate entry controls and access points.

**Purpose:**
To ensure only authorized physical access to the organization’s information and other associated assets occurs.

**Guidance:**
***General:***
Access points such as delivery and loading areas and other points where unauthorized persons can enter the premises should be controlled and, if possible, isolated from information processing facilities to avoid unauthorized access.

The following guidelines should be considered:
- restricting access to sites and buildings to authorized personnel only. The process for the management of access rights to physical areas should include the provision, periodical review, update and revocation of authorizations (see 5.18);
- securely maintaining and monitoring a physical logbook or electronic audit trail of all access and protecting all logs (see 5.33) and sensitive authentication information;
- establishing and implementing a process and technical mechanisms for the management of access to areas where information is processed or stored. Authentication mechanisms include the use of access cards, biometrics or two-factor authentication such as an access card and secret PIN. Double security doors should be considered for access to sensitive areas;
- setting up a reception area monitored by personnel, or other means to control physical access to the site or building;
- inspecting and examining personal belongings of personnel and interested parties upon entry and exit;
- requiring all personnel and interested parties to wear some form of visible identification and to immediately notify security personnel if they encounter unescorted visitors and anyone not wearing visible identification. Easily distinguishable badges should be considered to better identify permanent employees, suppliers and visitors;
- granting supplier personnel restricted access to secure areas or information processing facilities only when required. This access should be authorized and monitored;
- giving special attention to physical access security in the case of buildings holding assets for multiple organizations;
- designing physical security measures so that they can be strengthened when the likelihood of physical incidents increases;
- securing other entry points such as emergency exits from unauthorized access;
- setting up a key management process to ensure the management of the physical keys or authentication information (e.g. lock codes, combination locks to offices, rooms and facilities such as key cabinets) and to ensure a log book or annual key audit and that access to physical keys or authentication information is controlled (see 5.17 for further guidance on authentication information).

***Visitors:***
The following guidelines should be considered:
- authenticating the identity of visitors by an appropriate means;
- recording the date and time of entry and departure of visitors;
- only granting access for visitors for specific, authorized purposes and with instructions on the security requirements of the area and on emergency procedures;
- supervising all visitors, unless an explicit exception is granted.

***Delivery and loading areas and incoming material:***
The following guidelines should be considered:
- restricting access to delivery and loading areas from outside of the building to identified and authorized personnel;
- designing the delivery and loading areas so that deliveries can be loaded and unloaded without delivery personnel gaining unauthorized access to other parts of the building;
- securing the external doors of delivery and loading areas when doors to restricted areas are opened;
- inspecting and examining incoming deliveries for explosives, chemicals or other hazardous materials before they are moved from delivery and loading areas;
- registering incoming deliveries in accordance with asset management procedures (see 5.9 and 7.10) on entry to the site;
- physically segregating incoming and outgoing shipments, where possible;
- inspecting incoming deliveries for evidence of tampering on the way. If tampering is discovered, it should be immediately reported to security personnel.

**Other information:**
No other information.

---
**Section:** 7.3
**Title:** Securing offices, rooms and facilities

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Physical_security #Asset_management |
| Security domains | #Protection |

**Control:**
Physical security for offices, rooms and facilities should be designed and implemented.

**Purpose:**
To prevent unauthorized physical access, damage and interference to the organization’s information and other associated assets in offices, rooms and facilities.

**Guidance:**
The following guidelines should be considered to secure offices, rooms and facilities:
- siting critical facilities to avoid access by the public;
- where applicable, ensuring buildings are unobtrusive and give minimum indication of their purpose, with no obvious signs, outside or inside the building, identifying the presence of information processing activities;
- configuring facilities to prevent confidential information or activities from being visible and audible from the outside. Electromagnetic shielding should also be considered as appropriate;
- not making directories, internal telephone books and online accessible maps identifying locations of confidential information processing facilities readily available to any unauthorized person.

**Other information:**
No other information.
