### A. Tài liệu gốc của Chương 8 (Control 8.14)

### B. Summary Overview của Chương 8 (Control 8.14)
Tài liệu này mô tả chi tiết **mục 8.14** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào việc thiết kế dư thừa cho các cơ sở xử lý thông tin để duy trì tính sẵn sàng của dịch vụ.
Mục tiêu là **bảo đảm hệ thống và hạ tầng xử lý thông tin vẫn tiếp tục hoạt động khi một thành phần, một tuyến hoặc một địa điểm gặp sự cố**.
Gồm 1 mục chính:
- `8.14`: Redundancy of information processing facilities - xây dựng cơ sở xử lý thông tin dự phòng hoặc song song để duy trì availability

Áp dụng cho kiến trúc hệ thống, trung tâm dữ liệu, nguồn điện, mạng, thành phần phần mềm/hardware và các dịch vụ công nghệ cần failover hoặc load balancing.

### C. Key Points của Chương 8 (Control 8.14)
- **Mục tiêu quản trị:** `8.14` giảm rủi ro gián đoạn dịch vụ bằng cách tạo năng lực dự phòng đủ để tiếp tục vận hành khi thành phần chính hỏng.
- **Yêu cầu chính:** Tổ chức phải xác định yêu cầu availability, thiết kế kiến trúc dư thừa phù hợp và có quy trình kích hoạt failover tự động hoặc thủ công.
- **Yêu cầu kiểm thử:** Các cấu phần dự phòng phải được kiểm thử để xác minh việc chuyển đổi hoạt động từ thành phần chính sang dự phòng diễn ra đúng như thiết kế.
- **Điểm vận hành quan trọng:** Dư thừa không chỉ là “có thêm một cái dự phòng”; tổ chức phải bảo đảm các bản sao hoặc thành phần dự phòng có mức bảo mật tương đương và được giám sát khi hỏng.
- **Lưu ý thực tế:** Dư thừa có thể làm tăng rủi ro integrity hoặc confidentiality nếu dữ liệu sao chép, thành phần dự phòng hoặc đồng bộ hóa không được kiểm soát chặt.

### D. Deep Summary của Chương 8 (Control 8.14)
**Bối cảnh:**
Đây là control cốt lõi cho continuity, đặc biệt với các dịch vụ cần uptime cao hoặc recovery time ngắn. Nếu chỉ có một điểm lỗi duy nhất, bất kỳ sự cố phần cứng, mạng, nguồn điện hoặc trung tâm dữ liệu nào cũng có thể làm dừng dịch vụ. Redundancy nhằm loại bỏ single point of failure và tạo khả năng chuyển đổi sang thành phần thay thế mà người dùng không bị gián đoạn đáng kể.

**Nội dung cốt lõi:**
- `8.14` yêu cầu tổ chức thiết kế kiến trúc với mức dư thừa phù hợp với nhu cầu availability của dịch vụ và hệ thống.
- `8.14` có thể được triển khai bằng cách nhân đôi thành phần, dùng nhiều nhà cung cấp, nhiều tuyến mạng, nhiều data center hoặc nhiều instance song song với load balancing.
- `8.14` yêu cầu quy trình kích hoạt dự phòng rõ ràng, xác định khi nào tự động chuyển sang dự phòng và khi nào cần can thiệp thủ công.
- `8.14` đòi hỏi hệ thống dự phòng phải được kiểm thử trong thực tế, tốt nhất ở môi trường sản xuất hoặc tương đương, để bảo đảm failover hoạt động như mong muốn.
- `8.14` cũng phải được cân bằng với rủi ro mới phát sinh từ việc sao chép dữ liệu hoặc mở rộng bề mặt tấn công trên các thành phần nhân bản.

**Dữ liệu đáng chú ý:**
- `8.14` là kiểm soát `#Preventive`, gắn với `#Availability`, thuộc `#Continuity#Asset_management` và miền `#Protection#Resilience`.
- Redundancy có mối liên hệ chặt với business continuity và ICT readiness, đặc biệt khi thời gian khôi phục yêu cầu rất ngắn.
- `8.14` không phải lúc nào cũng giải quyết được application unavailability do lỗi bên trong ứng dụng.
- Với cloud, có thể tồn tại nhiều bản live ở nhiều địa điểm vật lý khác nhau với automatic failover và load balancing.
- Một số kỹ thuật redundant failover trong cloud được bàn thêm trong ISO/IEC TS 23167.

**Rủi ro / Lưu ý:**
- Nếu redundancy được thiết kế mà không test failover, tổ chức có thể phát hiện quá muộn rằng cơ chế dự phòng không hoạt động.
- Nếu bản sao dự phòng không có mức bảo mật tương đương, tính sẵn sàng tăng lên nhưng confidentiality hoặc integrity có thể xấu đi.
- Nếu dự phòng tạo ra đồng bộ dữ liệu lỗi, hệ thống chính và hệ thống dự phòng có thể cùng mang cùng một sai sót.
- Nếu tổ chức nhầm redundancy với business continuity đầy đủ, có thể bỏ sót các yếu tố như quy trình vận hành, con người và phục hồi ứng dụng.

### E. Structured Output của Chương 8 (Control 8.14)
**Section:** 8.14
**Title:** Redundancy of information processing facilities

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Continuity #Asset_management |
| Security domains | #Protection #Resilience |

**Control:**
Information processing facilities should be implemented with redundancy sufficient to meet availability requirements.

**Purpose:**
To ensure the continuous operation of information processing facilities.

**Guidance:**
The organization should identify requirements for the availability of business services and information systems. The organization should design and implement systems architecture with appropriate redundancy to meet these requirements.

Redundancy can be introduced by duplicating information processing facilities in part or in their entirety (i.e. spare components or having two of everything). The organization should plan and implement procedures for the activation of the redundant components and processing facilities. The procedures should establish if the redundant components and processing activities are always activated, or in case of emergency, automatically or manually activated. The redundant components and information processing facilities should ensure the same security level as the primary ones.

Mechanisms should be in place to alert the organization to any failure in the information processing facilities, enable executing the planned procedure and allow continued availability while the information processing facilities are repaired or replaced.

The organization should consider the following when implementing redundant systems:
- contracting with two or more suppliers of network and critical information processing facilities such as internet service providers;
- using redundant networks;
- using two geographically separate data centres with mirrored systems;
- using physically redundant power supplies or sources;
- using multiple parallel instances of software components, with automatic load balancing between them (between instances in the same data centre or in different data centres);
- having duplicated components in systems (e.g. CPU, hard disks, memories) or in networks (e.g. firewalls, routers, switches).

Where applicable, preferably in production mode, redundant information systems should be tested to ensure the failover from one component to another component works as intended.

**Other information:**
There is a strong relationship between redundancy and ICT readiness for business continuity (see 5.30) especially if short recovery times are required. Many of the redundancy measures can be part of the ICT continuity strategies and solutions.

The implementation of redundancies can introduce risks to the integrity (e.g. processes of copying data to duplicated components can introduce errors) or confidentiality (e.g. weak security control of duplicated components can lead to compromise) of information and information systems, which need to be considered when designing information systems.

Redundancy in information processing facilities does not usually address application unavailability due to faults within an application.

With the use of public cloud computing, it is possible to have multiple live versions of information processing facilities, existing in multiple separate physical locations with automatic failover and load balancing between them.

Some of the technologies and techniques for providing redundancy and automatic fail-over in the context of cloud services are discussed in ISO/IEC TS 23167.
