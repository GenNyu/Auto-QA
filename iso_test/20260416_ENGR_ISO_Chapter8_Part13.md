### A. Tài liệu gốc của Chương 8 (Control 8.20, 8.21)

### B. Summary Overview của Chương 8 (Control 8.20, 8.21)
Tài liệu này mô tả chi tiết **mục 8.20 và 8.21** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào việc bảo vệ an ninh mạng lưới và kiểm soát chất lượng an toàn của các dịch vụ mạng.
Mục tiêu là **bảo vệ thông tin đi qua mạng, ngăn truy cập trái phép, và bảo đảm các dịch vụ mạng được cung cấp với mức bảo mật phù hợp**.
Gồm 2 mục chính:
- `8.20`: Networks security - bảo mật mạng, thiết bị mạng và kết nối mạng
- `8.21`: Security of network services - bảo đảm an toàn của dịch vụ mạng do nội bộ hoặc bên thứ ba cung cấp

Áp dụng cho network devices, network traffic, public network, wireless network, VPN, managed network services, và các dịch vụ mạng được dùng để kết nối hoặc bảo vệ hệ thống thông tin.

### C. Key Points của Chương 8 (Control 8.20, 8.21)
- **Mục tiêu quản trị:** `8.20` bảo vệ luồng dữ liệu và thiết bị mạng trước truy cập trái phép, cấu hình sai và tấn công; `8.21` bảo đảm các dịch vụ mạng có security feature, service level và monitoring phù hợp.
- **Yêu cầu chính của 8.20:** Tổ chức phải quản lý network devices, phân tách khu vực quản trị, hardening thiết bị, logging/monitoring và hạn chế kết nối mạng vào các hệ thống, thiết bị hoặc subnet quan trọng.
- **Yêu cầu chính của 8.21:** Các nhà cung cấp dịch vụ mạng phải đáp ứng security requirements đã thỏa thuận, có thể audit được, và có cơ chế giám sát liên tục về mức độ an toàn của dịch vụ.
- **Điểm vận hành quan trọng:** `8.20` bao gồm cả virtualized networks và SDN/SD-WAN; `8.21` cần quy định rõ quyền truy cập, cơ chế xác thực, kỹ thuật kết nối và monitoring cho từng loại dịch vụ mạng.
- **Lưu ý thực tế:** Mạng là môi trường động, nên các control này phải được duy trì như cấu phần vận hành thường xuyên chứ không chỉ là cấu hình ban đầu.

### D. Deep Summary của Chương 8 (Control 8.20, 8.21)
**Bối cảnh:**
Hai control này bao phủ lớp truyền dẫn và lớp dịch vụ của hạ tầng mạng. Nếu network security yếu, mọi system và application bên trên đều bị phơi bày. Nếu network service provider không đáp ứng security requirement, tổ chức có thể đang sử dụng một kết nối có sẵn nhưng không an toàn theo đúng nghĩa quản trị. Vì vậy, mạng không chỉ là kênh truyền mà là một bề mặt kiểm soát độc lập.

**Nội dung cốt lõi:**
- `8.20` yêu cầu bảo vệ mạng và network devices bằng cách xác định loại thông tin được hỗ trợ, phân công trách nhiệm quản trị và duy trì tài liệu, sơ đồ mạng và cấu hình thiết bị.
- `8.20` nhấn mạnh bảo vệ confidentiality, integrity và availability của dữ liệu qua public network, third-party network và wireless network.
- `8.20` cũng yêu cầu logging, monitoring, authentication hệ thống, filtering kết nối, hardening thiết bị, tách kênh admin và cô lập subnet quan trọng khi bị tấn công.
- `8.21` yêu cầu xác định security mechanism, service level và service requirements cho các network services, rồi giám sát khả năng cung cấp dịch vụ an toàn của provider.
- `8.21` làm rõ các yếu tố như loại network được phép, authentication, authorization, VPN/wireless access, location/time-based attributes và monitoring việc sử dụng dịch vụ.

**Dữ liệu đáng chú ý:**
- `8.20` là kiểm soát `#Preventive #Detective`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#System_and_network_security` và miền `#Protection`.
- `8.21` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#System_and_network_security` và miền `#Protection`.
- `8.20` bao gồm virtualized networks, SDN và SD-WAN, nghĩa là network security phải bao phủ cả lớp logic lẫn lớp vật lý.
- `8.21` nhấn mạnh quyền audit và third-party attestations để xác minh nhà cung cấp dịch vụ mạng.
- `8.20` và `8.21` đều có liên hệ đến ISO/IEC 27033 và ISO/IEC 29146 cho framework và access management.

**Rủi ro / Lưu ý:**
- Nếu mạng không được harden hoặc phân đoạn đúng, một điểm xâm nhập có thể lan sang toàn bộ hạ tầng.
- Nếu dịch vụ mạng của nhà cung cấp không được giám sát, tổ chức có thể sử dụng một dịch vụ “có vẻ an toàn” nhưng thực chất không đáp ứng yêu cầu bảo mật.
- Nếu logging và monitoring mạng yếu, tổ chức sẽ khó phát hiện botnet, scanning, traffic bất thường hoặc kết nối độc hại.
- Nếu mạng ảo, SDN hoặc SD-WAN không được đưa vào phạm vi control, phần kiểm soát quan trọng có thể bị bỏ sót.

### E. Structured Output của Chương 8 (Control 8.20, 8.21)
**Section:** 8.20
**Title:** Networks security

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive #Detective |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect #Detect |
| Operational capabilities | #System_and_network_security |
| Security domains | #Protection |

**Control:**
Networks and network devices should be secured, managed and controlled to protect information in systems and applications.

**Purpose:**
To protect information in networks and its supporting information processing facilities from compromise via the network.

**Guidance:**
Controls should be implemented to ensure the security of information in networks and to protect connected services from unauthorized access. In particular, the following items should be considered:
- the type and classification level of information that the network can support;
- establishing responsibilities and procedures for the management of networking equipment and devices;
- maintaining up to date documentation including network diagrams and configuration files of devices (e.g. routers, switches);
- separating operational responsibility for networks from ICT system operations where appropriate (see 5.3);
- establishing controls to safeguard the confidentiality and integrity of data passing over public networks, third-party networks or over wireless networks and to protect the connected systems and applications (see 5.22, 8.24, 5.14 and 6.6). Additional controls can also be required to maintain the availability of the network services and computers connected to the network;
- appropriately logging and monitoring to enable recording and detection of actions that can affect, or are relevant to, information security (see 8.16 and 8.15);
- closely coordinating network management activities both to optimize the service to the organization and to ensure that controls are consistently applied across the information processing infrastructure;
- authenticating systems on the network;
- restricting and filtering systems connection to the network (e.g. using firewalls);
- detecting, restricting and authenticating the connection of equipment and devices to the network;
- hardening of network devices;
- segregating network administration channels from other network traffic;
- temporarily isolating critical subnetworks (e.g. with drawbridges) if the network is under attack;
- disabling vulnerable network protocols.

The organization should ensure that appropriate security controls are applied to the use of virtualized networks. Virtualized networks also cover software-defined networking (SDN, SD-WAN). Virtualized networks can be desirable from a security viewpoint, since they can permit logical separation of communication taking place over physical networks, particularly for systems and applications that are implemented using distributed computing.

**Other information:**
Additional information on network security can be found in the ISO/IEC 27033 series.

More information concerning virtualized networks can be found in ISO/IEC TS 23167.

---
**Section:** 8.21
**Title:** Security of network services

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #System_and_network_security |
| Security domains | #Protection |

**Control:**
Security mechanisms, service levels and service requirements of network services should be identified, implemented and monitored.

**Purpose:**
To ensure security in the use of network services.

**Guidance:**
The security measures necessary for particular services, such as security features, service levels and service requirements, should be identified and implemented (by internal or external network service providers). The organization should ensure that network service providers implement these measures.

The ability of the network service provider to manage agreed services in a secure way should be determined and regularly monitored. The right to audit should be agreed between the organization and the provider. The organization should also consider third-party attestations provided by service providers to demonstrate they maintain appropriate security measures.

Rules on the use of networks and network services should be formulated and implemented to cover:
- the networks and network services which are allowed to be accessed;
- authentication requirements for accessing various network services;
- authorization procedures for determining who is allowed to access which networks and networked services;
- network management and technological controls and procedures to protect access to network connections and network services;
- the means used to access networks and network services [e.g. use of virtual private network (VPN) or wireless network];
- time, location and other attributes of the user at the time of the access;
- monitoring of the use of network services.

The following security features of network services should be considered:
- technology applied for security of network services, such as authentication, encryption and network connection controls;
- technical parameters required for secured connection with the network services in accordance with the security and network connection rules;
- caching (e.g. in a content delivery network) and its parameters that allow users to choose the use of caching in accordance with performance, availability and confidentiality requirements;
- procedures for the network service usage to restrict access to network services or applications, where necessary.

**Other information:**
Network services include the provision of connections, private network services and managed network security solutions such as firewalls and intrusion detection systems. These services can range from simple unmanaged bandwidth to complex value-added offerings.

More guidance on a framework for access management is given in ISO/IEC 29146.
