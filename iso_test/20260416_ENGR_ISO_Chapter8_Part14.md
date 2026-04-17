### A. Tài liệu gốc của Chương 8 (Control 8.22, 8.23)

### B. Summary Overview của Chương 8 (Control 8.22, 8.23)
Tài liệu này mô tả chi tiết **mục 8.22 và 8.23** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào việc phân tách mạng theo vùng an ninh và kiểm soát truy cập web để giảm phơi nhiễm với nội dung độc hại.
Mục tiêu là **tạo ranh giới mạng rõ ràng giữa các nhóm dịch vụ/người dùng/hệ thống và hạn chế truy cập vào website có nội dung độc hại, bất hợp pháp hoặc không phù hợp**.
Gồm 2 mục chính:
- `8.22`: Segregation of networks - phân tách mạng thành các vùng an ninh riêng
- `8.23`: Web filtering - lọc truy cập web để giảm rủi ro nội dung độc hại

Áp dụng cho mạng nội bộ, guest WiFi, public network, gateway, firewall, router, trình duyệt và các truy cập web của nhân sự trong môi trường tổ chức.

### C. Key Points của Chương 8 (Control 8.22, 8.23)
- **Mục tiêu quản trị:** `8.22` giảm lan truyền rủi ro giữa các vùng mạng; `8.23` giảm phơi nhiễm với malware, phishing, illegal content và các website không được phép.
- **Yêu cầu chính của 8.22:** Mạng phải được chia thành các domain hoặc vùng logic/vật lý theo độ tin cậy, criticality, sensitivity và phải kiểm soát traffic qua gateway như firewall hoặc filtering router.
- **Yêu cầu chính của 8.23:** Truy cập website bên ngoài phải được quản lý bằng blocklist, rules, training và exception process phù hợp với nhu cầu công việc.
- **Điểm vận hành quan trọng:** `8.22` đặc biệt phải xử lý wireless/guest WiFi vì perimeter không rõ ràng; `8.23` cần cập nhật thường xuyên theo threat intelligence và hành vi web mới.
- **Lưu ý thực tế:** Phân tách mạng và lọc web chỉ hiệu quả khi đi kèm policy, cấu hình phù hợp và training để người dùng không tự ý vượt qua các cảnh báo bảo mật.

### D. Deep Summary của Chương 8 (Control 8.22, 8.23)
**Bối cảnh:**
Hai control này kiểm soát hai điểm tiếp xúc rủi ro phổ biến nhất của hạ tầng số: ranh giới mạng và truy cập web. Nếu mạng không được phân vùng, một sự cố ở một khu vực có thể lan sang cả hệ thống. Nếu web access không được lọc, người dùng có thể mở cửa cho malware, phishing hoặc nội dung độc hại đi thẳng vào endpoint và mạng nội bộ.

**Nội dung cốt lõi:**
- `8.22` yêu cầu tổ chức chia mạng thành các vùng an ninh phù hợp với trust, criticality, sensitivity hoặc đơn vị tổ chức, đồng thời kiểm soát kết nối giữa các vùng qua gateway.
- `8.22` lưu ý đặc biệt với wireless networks và guest WiFi, vì perimeter không rõ như mạng dây và có thể phải coi toàn bộ wireless access như external connection.
- `8.22` cũng yêu cầu định nghĩa rõ tiêu chí phân tách, quyền truy cập qua gateway và tác động lên cost/performance để thiết kế cân bằng giữa bảo mật và vận hành.
- `8.23` yêu cầu giới hạn truy cập vào các website có nội dung độc hại, illegal, phishing, command-and-control, hoặc các site có chức năng upload nếu không cần thiết cho công việc.
- `8.23` đi kèm training, rules for use, và quy trình xử lý ngoại lệ để người dùng không tự ý vượt qua cảnh báo trình duyệt hoặc sử dụng web không an toàn.

**Dữ liệu đáng chú ý:**
- `8.22` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#System_and_network_security` và miền `#Protection`.
- `8.23` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#System_and_network_security` và miền `#Protection`.
- `8.22` có thể triển khai bằng physical network hoặc logical network, nhưng gateway control là bắt buộc khi traffic đi giữa các vùng.
- `8.23` có thể dùng signatures, heuristics, allowlist, blocklist hoặc bespoke configuration để lọc web.
- `8.22` và `8.23` đều cần cập nhật theo threat landscape mới và được tích hợp vào quy trình vận hành thường xuyên.

**Rủi ro / Lưu ý:**
- Nếu mạng không được segregate đúng, một vùng bị xâm nhập có thể trở thành bàn đạp sang vùng khác.
- Nếu guest WiFi không tách khỏi mạng nội bộ, người dùng ngoài tổ chức có thể mở rộng phạm vi tấn công vào tài sản nội bộ.
- Nếu web filtering quá lỏng, người dùng có thể truy cập malware, phishing hoặc command-and-control infrastructure mà không bị chặn.
- Nếu filtering quá chặt nhưng không có exception process, tổ chức có thể tạo ra trở ngại vận hành và người dùng sẽ có xu hướng tìm cách обход kiểm soát.

### E. Structured Output của Chương 8 (Control 8.22, 8.23)
**Section:** 8.22
**Title:** Segregation of networks

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #System_and_network_security |
| Security domains | #Protection |

**Control:**
Groups of information services, users and information systems should be segregated in the organization’s networks.

**Purpose:**
To split the network in security boundaries and to control traffic between them based on business needs.

**Guidance:**
The organization should consider managing the security of large networks by dividing them into separate network domains and separating them from the public network (i.e. internet). The domains can be chosen based on levels of trust, criticality and sensitivity (e.g. public access domain, desktop domain, server domain, low- and high-risk systems), along organizational units (e.g. human resources, finance, marketing) or some combination (e.g. server domain connecting to multiple organizational units). The segregation can be done using either physically different networks or by using different logical networks.

The perimeter of each domain should be well-defined. If access between network domains is allowed, it should be controlled at the perimeter using a gateway (e.g. firewall, filtering router). The criteria for segregation of networks into domains, and the access allowed through the gateways, should be based on an assessment of the security requirements of each domain. The assessment should be in accordance with the topic-specific policy on access control (see 5.15), access requirements, value and classification of information processed and take account of the relative cost and performance impact of incorporating suitable gateway technology.

Wireless networks require special treatment due to the poorly-defined network perimeter. Radio coverage adjustment should be considered for segregation of wireless networks. For sensitive environments, consideration should be made to treat all wireless access as external connections and to segregate this access from internal networks until the access has passed through a gateway in accordance with network controls (see 8.20) before granting access to internal systems. Wireless access network for guests should be segregated from those for personnel if personnel only use controlled user endpoint devices compliant to the organization’s topic-specific policies. WiFi for guests should have at least the same restrictions as WiFi for personnel, in order to discourage the use of guest WiFi by personnel.

**Other information:**
Networks often extend beyond organizational boundaries, as business partnerships are formed that require the interconnection or sharing of information processing and networking facilities. Such extensions can increase the risk of unauthorized access to the organization’s information systems that use the network, some of which require protection from other network users because of their sensitivity or criticality.

---
**Section:** 8.23
**Title:** Web filtering

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #System_and_network_security |
| Security domains | #Protection |

**Control:**
Access to external websites should be managed to reduce exposure to malicious content.

**Purpose:**
To protect systems from being compromised by malware and to prevent access to unauthorized web resources.

**Guidance:**
The organization should reduce the risks of its personnel accessing websites that contain illegal information or are known to contain viruses or phishing material. A technique for achieving this works by blocking the IP address or domain of the website(s) concerned. Some browsers and anti-malware technologies do this automatically or can be configured to do so.

The organization should identify the types of websites to which personnel should or should not have access. The organization should consider blocking access to the following types of websites:
- websites that have an information upload function unless permitted for valid business reasons;
- known or suspected malicious websites (e.g. those distributing malware or phishing contents);
- command and control servers;
- malicious website acquired from threat intelligence (see 5.7);
- websites sharing illegal content.

Prior to deploying this control, the organization should establish rules for safe and appropriate use of online resources, including any restriction to undesirable or inappropriate websites and web-based applications. The rules should be kept up-to-date.

Training should be given to personnel on the secure and appropriate use of online resources including access to the web. The training should include the organization’s rules, contact point for raising security concerns, and exception process when restricted web resources need to be accessed for legitimate business reasons. Training should also be given to personnel to ensure that they do not overrule any browser advisory that reports that a website is not secure but allows the user to proceed.

**Other information:**
Web filtering can include a range of techniques including signatures, heuristics, list of acceptable websites or domains, list of prohibited websites or domains and bespoke configuration to help prevent malicious software and other malicious activity from attacking the organization’s network and systems.