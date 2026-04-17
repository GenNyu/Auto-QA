### A. Tài liệu gốc của Chương 8 (Control 8.1)

### B. Summary Overview của Chương 8 (Control 8.1)
Tài liệu này mô tả chi tiết **mục 8.1** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào việc bảo vệ thông tin trên thiết bị đầu cuối người dùng và kiểm soát cách thiết bị đó được cấu hình, sử dụng và bảo vệ.
Mục tiêu là **giảm rủi ro từ mất cắp, lộ lọt, hư hỏng, mã độc và cấu hình không an toàn trên user endpoint devices, đặc biệt khi thiết bị được dùng ngoài môi trường kiểm soát chặt của tổ chức**.
Gồm 1 mục chính:
- `8.1`: User endpoint devices - bảo vệ thiết bị đầu cuối người dùng bằng chính sách, cấu hình và kiểm soát sử dụng phù hợp

Áp dụng cho máy tính xách tay, thiết bị di động, máy tính bảng, thiết bị cá nhân dùng cho công việc và mọi user endpoint device có thể truy cập, lưu trữ hoặc xử lý thông tin của tổ chức.

### C. Key Points của Chương 8 (Control 8.1)
- **Mục tiêu quản trị:** `8.1` bảo vệ thông tin trên thiết bị đầu cuối bằng cách kết hợp chính sách cấu hình, kiểm soát kỹ thuật, trách nhiệm người dùng và quy trình xử lý thiết bị bị mất hoặc bị đánh cắp.
- **Yêu cầu chính:** Tổ chức phải quy định rõ loại thông tin được phép xử lý/lưu trữ, kiểm soát cài đặt phần mềm, cập nhật, mã hóa, sao lưu, truy cập mạng, chống malware và khả năng khóa hoặc xóa từ xa.
- **Trách nhiệm người dùng:** Người dùng phải khóa phiên, bảo vệ thiết bị khỏi truy cập trái phép, thận trọng khi sử dụng ở nơi công cộng và báo cáo ngay khi có mất mát hoặc trộm cắp.
- **BYOD và wireless:** Nếu cho phép thiết bị cá nhân hoặc kết nối không dây, tổ chức cần chính sách tách bạch công việc và cá nhân, quyền xóa dữ liệu từ xa, xử lý quyền sở hữu dữ liệu và bảo đảm băng thông phù hợp.
- **Lưu ý thực tế:** Một số biện pháp tốt nhất nên được tự động hóa qua configuration management; đồng thời cần cân nhắc tình huống ngoại lệ như USB-C hoặc các cổng vừa cấp nguồn vừa xuất hình.

### D. Deep Summary của Chương 8 (Control 8.1)
**Bối cảnh:**
Đây là control đặt nền cho việc bảo vệ endpoint, vì phần lớn rủi ro không còn nằm ở trung tâm dữ liệu mà nằm ngay trên thiết bị do người dùng mang theo. Khi thiết bị rời khỏi phạm vi kiểm soát vật lý và mạng của tổ chức, bề mặt tấn công tăng mạnh: mất cắp, nghe lén mạng, malware, sai cấu hình, và đồng thời cả vấn đề pháp lý nếu thiết bị là BYOD.

**Nội dung cốt lõi:**
- Tổ chức cần có topic-specific policy cho user endpoint devices, xác định rõ loại dữ liệu được phép xử lý, yêu cầu vật lý, kiểm soát phần mềm, kết nối mạng, mã hóa lưu trữ, sao lưu, remote wipe và các giới hạn sử dụng.
- Các kiểm soát nên được cưỡng chế càng nhiều càng tốt bằng cấu hình hoặc công cụ tự động để giảm phụ thuộc vào hành vi thủ công của người dùng.
- Người dùng phải được hướng dẫn bảo vệ thiết bị cả về logic lẫn vật lý: log off khi không dùng, khóa thiết bị, tránh để lộ màn hình ở nơi công cộng và bảo vệ khỏi mất cắp trong phương tiện di chuyển hoặc khách sạn.
- Nếu tổ chức cho phép BYOD, phải có cơ chế tách riêng dữ liệu cá nhân và công việc, quy định quyền xóa dữ liệu từ xa và xử lý tranh chấp về sở hữu dữ liệu hoặc tài sản trí tuệ.
- Với wireless connections, rủi ro không chỉ nằm ở bảo mật giao tiếp mà còn ở độ tin cậy của việc sao lưu và cập nhật, vì thiết bị có thể không kết nối vào thời điểm hệ thống định sẵn.

**Dữ liệu đáng chú ý:**
- `8.1` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Asset_management#Information_protection` và miền `#Protection`.
- Control này bao phủ cả thiết bị do tổ chức sở hữu lẫn thiết bị cá nhân dùng cho công việc.
- Nội dung nhấn mạnh hai lớp trách nhiệm: tổ chức phải quy định và cấu hình, còn người dùng phải thực thi và giữ kỷ luật sử dụng.
- Phần guidance tách rõ 4 cụm: `General`, `User responsibility`, `Use of personal devices`, `Wireless connections`.
- Phần other information lưu ý rằng backup trên endpoint có thể thất bại do băng thông hoặc do thiết bị không online vào thời điểm sao lưu.

**Rủi ro / Lưu ý:**
- Nếu không kiểm soát endpoint chặt, tổ chức dễ mất dữ liệu do trộm cắp, malware, hoặc người dùng lưu trữ thông tin nhạy cảm trên thiết bị cá nhân không được bảo vệ đúng mức.
- Nếu không có cơ chế remote wipe, một thiết bị thất lạc có thể biến thành sự cố rò rỉ dữ liệu kéo dài.
- Nếu BYOD không có chính sách rõ, tổ chức có thể gặp tranh chấp về quyền dữ liệu, quyền truy cập thiết bị hoặc nghĩa vụ pháp lý liên quan đến PII và licensing.
- Nếu chỉ dựa vào người dùng mà không tự động hóa cấu hình, mức độ tuân thủ sẽ không đồng đều và rất khó kiểm soát ở quy mô lớn.

### E. Structured Output của Chương 8 (Control 8.1)
**Section:** 8.1
**Title:** User endpoint devices

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Asset_management #Information_protection |
| Security domains | #Protection |

**Control:**
Information stored on, processed by or accessible via user endpoint devices should be protected.

**Purpose:**
To protect information against the risks introduced by using user endpoint devices.

**Guidance:**
***General***
The organization should establish a topic-specific policy on secure configuration and handling of user endpoint devices. The topic-specific policy should be communicated to all relevant personnel and consider the following:
- the type of information and the classification level that the user endpoint devices can handle, process, store or support;
- registration of user endpoint devices;
- requirements for physical protection;
- restriction of software installation (e.g. remotely controlled by system administrators);
- requirements for user endpoint device software (including software versions) and for applying updates (e.g. active automatic updating);
- rules for connection to information services, public networks or any other network off premises (e.g. requiring the use of personal firewall);
- access controls;
- storage device encryption;
- protection against malware;
- remote disabling, deletion or lockout;
- backups;
- usage of web services and web applications;
- end user behaviour analytics (see 8.16);
- the use of removable devices, including removable memory devices, and the possibility of disabling physical ports (e.g. USB ports);
- the use of partitioning capabilities, if supported by the user endpoint device, which can securely separate the organization's information and other associated assets (e.g. software) from other information and other associated assets on the device.

Consideration should be given as to whether certain information is so sensitive that it can only be accessed via user endpoint devices, but not stored on such devices. In such cases, additional technical safeguards can be required on the device. For example, ensuring that downloading files for offline working is disabled and that local storage such as SD card is disabled.

As far as possible, the recommendations on this control should be enforced through configuration management (see 8.9) or automated tools.

***User responsibility***
All users should be made aware of the security requirements and procedures for protecting user endpoint devices, as well as of their responsibilities for implementing such security measures. Users should be advised to:
- log-off active sessions and terminate services when no longer needed;
- protect user endpoint devices from unauthorized use with a physical control (e.g. key lock or special locks) and logical control (e.g. password access) when not in use; not leave devices carrying important, sensitive or critical business information unattended;
- use devices with special care in public places, open offices, meeting places and other unprotected areas (e.g. avoid reading confidential information if people can read from the back, use privacy screen filters);
- physically protect user endpoint devices against theft (e.g. in cars and other forms of transport, hotel rooms, conference centres and meeting places).

A specific procedure taking into account legal, statutory, regulatory, contractual (including insurance) and other security requirements of the organization should be established for cases of theft or loss of user endpoint devices.

***Use of personal devices***
Where the organization allows the use of personal devices (sometimes known as BYOD), in addition to the guidance given in this control, the following should be considered:
- separation of personal and business use of the devices, including using software to support such separation and protect business data on a private device;
- providing access to business information only after users have acknowledged their duties (physical protection, software updating, etc.), waiving ownership of business data, allowing remote wiping of data by the organization in case of theft or loss of the device or when no longer authorized to use the service. In such cases, PII protection legislation should be considered;
- topic-specific policies and procedures to prevent disputes concerning rights to intellectual property developed on privately owned equipment;
- access to privately owned equipment (to verify the security of the machine or during an investigation), which can be prevented by legislation;
- software licensing agreements that are such that organizations can become liable for licensing for client software on user endpoint devices owned privately by personnel or external party users.

***Wireless connections***
The organization should establish procedures for:
- the configuration of wireless connections on devices (e.g. disabling vulnerable protocols);
- using wireless or wired connections with appropriate bandwidth in accordance with relevant topic-specific policies (e.g. because backups or software updates are needed).

**Other information:**
Controls to protect information on user endpoint devices depend on whether the user endpoint device is used only inside of the organization's secured premises and network connections, or whether it is exposed to increased physical and network related threats outside of the organization.

The wireless connections for user endpoint devices are similar to other types of network connections but have important differences that should be considered when identifying controls. In particular, back-up of information stored on user endpoint devices can sometimes fail because of limited network bandwidth or because user endpoint devices are not connected at the times when backups are scheduled.

For some USB ports, such as USB-C, disabling the USB port is not possible because it is used for other purposes (e.g. power delivery and display output).