### A. Tài liệu gốc của Chương 7 (Control 7.12, 7.13, 7.14)

### B. Summary Overview của Chương 7 (Control 7.12, 7.13, 7.14)
Tài liệu này mô tả chi tiết **mục 7.12, 7.13 và 7.14** trong **chương 7. Physical controls** của **ISO/IEC 27002:2022**, tập trung vào an toàn cáp, bảo trì thiết bị và tiêu hủy hoặc tái sử dụng thiết bị một cách an toàn.
Mục tiêu là **ngăn nghe lén, can thiệp hoặc hư hỏng hạ tầng truyền dẫn; duy trì thiết bị ở trạng thái vận hành an toàn; và bảo đảm dữ liệu không bị lộ khi thiết bị được loại bỏ hoặc tái sử dụng**.
Gồm 3 mục chính:
- `7.12`: Cabling security - bảo vệ cáp điện, cáp dữ liệu và cáp dịch vụ
- `7.13`: Equipment maintenance - bảo trì thiết bị đúng cách
- `7.14`: Secure disposal or re-use of equipment - tiêu hủy hoặc tái sử dụng thiết bị an toàn

Áp dụng cho hạ tầng cáp, thiết bị xử lý thông tin, thiết bị phụ trợ, và toàn bộ thiết bị có thể được tháo dỡ, sửa chữa, bán lại, tái dùng hoặc loại bỏ khỏi môi trường vận hành.

### C. Key Points của Chương 7 (Control 7.12, 7.13, 7.14)
- **Mục tiêu quản trị:** Nhóm control này bảo vệ lớp hạ tầng vật lý kỹ thuật của tổ chức, từ đường cáp, bảo trì thiết bị cho đến xóa sạch dữ liệu trước khi hủy hoặc tái sử dụng.
- **Yêu cầu chính của 7.12:** Cáp phải được bảo vệ khỏi nghe lén, nhiễu hoặc hư hỏng, đồng thời cần phân tách cáp nguồn và cáp truyền thông, gắn nhãn, kiểm tra định kỳ và áp dụng biện pháp bảo vệ bổ sung cho hệ thống nhạy cảm.
- **Yêu cầu chính của 7.13:** Thiết bị phải được bảo trì theo hướng dẫn nhà cung cấp, do người được ủy quyền thực hiện, có hồ sơ theo dõi, giám sát khi sửa chữa tại chỗ hoặc từ xa, và kiểm tra trước khi đưa vào vận hành lại.
- **Yêu cầu chính của 7.14:** Thiết bị chứa storage media phải được xác minh và làm sạch dữ liệu, nhãn nhận diện và các kiểm soát an ninh trước khi tiêu hủy hoặc tái sử dụng; nếu cần phải có hủy vật lý hoặc xóa an toàn tương ứng.
- **Lưu ý thực tế:** Các rủi ro ở giai đoạn cuối vòng đời thiết bị thường bị đánh giá thấp, nhưng đây lại là lúc dữ liệu, cấu hình và nhận diện tổ chức dễ bị để lộ nhất nếu quy trình không chặt.

### D. Deep Summary của Chương 7 (Control 7.12, 7.13, 7.14)
**Bối cảnh:**
Nhóm control này bao phủ ba điểm yếu có liên quan chặt chẽ trong vận hành hạ tầng vật lý: cáp truyền dẫn có thể bị chặn nghe hoặc bị can thiệp; thiết bị có thể xuống cấp nếu bảo trì sai; và thiết bị cũ có thể trở thành nguồn rò rỉ dữ liệu nếu không được xử lý đúng trước khi rời khỏi vòng kiểm soát của tổ chức.

**Nội dung cốt lõi:**
- `7.12` yêu cầu bảo vệ cáp nguồn, cáp dữ liệu và cáp dịch vụ bằng cách đi ngầm khi có thể, tách riêng nguồn và truyền thông, gắn nhãn, và kiểm tra các điểm phân phối hoặc kết cuối cáp để phát hiện can thiệp trái phép.
- `7.12` nhấn mạnh rằng các hệ thống nhạy cảm có thể cần bảo vệ bổ sung như conduit gia cường, phòng khóa, báo động, che chắn điện từ hoặc cáp quang.
- `7.13` yêu cầu bảo trì thiết bị theo lịch trình và tiêu chuẩn kỹ thuật, chỉ cho phép nhân viên được ủy quyền, giám sát hoạt động sửa chữa và ghi nhận đầy đủ sự cố, bảo trì phòng ngừa và khắc phục.
- `7.13` cũng xử lý rủi ro khi thiết bị được đưa ra ngoài cơ sở để bảo trì hoặc khi có bảo hiểm yêu cầu cụ thể, vì lúc này tài sản không còn ở trong vùng kiểm soát vật lý quen thuộc.
- `7.14` buộc tổ chức phải xác minh thiết bị trước khi loại bỏ hoặc tái sử dụng, bao gồm làm sạch storage media, xóa nhãn nhận diện, cân nhắc tháo bỏ kiểm soát an ninh tại cuối hợp đồng thuê hoặc khi di chuyển cơ sở.
- `7.14` nhấn mạnh việc cần xử lý đặc biệt với thiết bị hỏng có chứa dữ liệu nhạy cảm và xem xét mã hóa toàn bộ đĩa như một lớp giảm thiểu rủi ro khi thiết bị bị thanh lý.

**Dữ liệu đáng chú ý:**
- `7.12` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Availability`, thuộc `#Physical_security` và miền `#Protection`.
- `7.13` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Physical_security#Asset_management` và miền `#Protection#Resilience`.
- `7.14` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, thuộc `#Physical_security#Asset_management` và miền `#Protection`.
- `7.12` có thể liên quan đến hạ tầng dùng chung trong môi trường đồng sở hữu, nên cần phối hợp với tổ chức cùng hạ tầng.
- `7.14` tham chiếu thêm các hướng dẫn về xóa dữ liệu và sanitize storage media, cho thấy tiêu hủy thiết bị không chỉ là vấn đề vật lý mà còn là dữ liệu trên media bên trong.

**Rủi ro / Lưu ý:**
- Nếu cáp không được bảo vệ đúng cách, tổ chức có thể chịu nghe lén, nhiễu tín hiệu, mất kết nối hoặc bị can thiệp vật lý mà khó phát hiện.
- Nếu bảo trì thiết bị không có kiểm soát, lỗi cấu hình, thất thoát linh kiện hoặc truy cập trái phép trong lúc sửa chữa có thể làm suy giảm bảo mật và tính sẵn sàng.
- Nếu thiết bị được đưa đi sửa hoặc thanh lý mà không xóa sạch dữ liệu và nhãn nhận diện, tổ chức có thể vô tình rò rỉ thông tin mật hoặc để lộ cấu trúc hệ thống.
- Nếu không có quy trình cuối vòng đời rõ ràng, việc bỏ lại thiết bị, kiểm soát an ninh hoặc media có dữ liệu tại địa điểm cũ có thể tạo ra rủi ro kéo dài.

### E. Structured Output của Chương 7 (Control 7.12, 7.13, 7.14)
**Section:** 7.12
**Title:** Cabling security

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Physical_security |
| Security domains | #Protection |

**Control:**
Cables carrying power, data or supporting information services should be protected from interception, interference or damage.

**Purpose:**
To prevent loss, damage, theft or compromise of information and other associated assets and interruption to the organization’s operations related to power and communications cabling.

**Guidance:**
The following guidelines for cabling security should be considered:
- power and telecommunications lines into information processing facilities being underground where possible, or subject to adequate alternative protection, such as floor cable protector and utility pole; if cables are underground, protecting them from accidental cuts (e.g. with armoured conduits or signals of presence);
- segregating power cables from communications cables to prevent interference;
- for sensitive or critical systems, further controls to consider include:
  1. installation of armoured conduit and locked rooms or boxes and alarms at inspection and termination points;
  2. use of electromagnetic shielding to protect the cables;
  3. periodical technical sweeps and physical inspections to detect unauthorized devices being attached to the cables;
  4. controlled access to patch panels and cable rooms (e.g. with mechanical keys or PINs);
  5. use of fibre-optic cables;
- labelling cables at each end with sufficient source and destination details to enable the physical identification and inspection of the cable.

Specialist advice should be sought on how to manage risks arising from cabling incidents or malfunctions.

**Other information:**
Sometimes power and telecommunications cabling are shared resources for more than one organization occupying co-located premises.

---
**Section:** 7.13
**Title:** Equipment maintenance

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Physical_security #Asset_management |
| Security domains | #Protection #Resilience |

**Control:**
Equipment should be maintained correctly to ensure availability, integrity and confidentiality of information.

**Purpose:**
To prevent loss, damage, theft or compromise of information and other associated assets and interruption to the organization’s operations caused by lack of maintenance.

**Guidance:**
The following guidelines for equipment maintenance should be considered:
- maintaining equipment in accordance with the supplier’s recommended service frequency and specifications;
- implementing and monitoring of a maintenance programme by the organization;
- only authorized maintenance personnel carrying out repairs and maintenance on equipment;
- keeping records of all suspected or actual faults, and of all preventive and corrective maintenance;
- implementing appropriate controls when equipment is scheduled for maintenance, taking into account whether this maintenance is performed by personnel on site or external to the organization; subjecting the maintenance personnel to a suitable confidentiality agreement;
- supervising maintenance personnel when carrying out maintenance on site;
- authorizing and controlling access for remote maintenance;
- applying security measures for assets off-premises (see 7.9) if equipment containing information is taken off premises for maintenance;
- complying with all maintenance requirements imposed by insurance;
- before putting equipment back into operation after maintenance, inspecting it to ensure that the equipment has not been tampered with and is functioning properly;
- applying measures for secure disposal or re-use of equipment (see 7.14) if it is determined that equipment is to be disposed of.

**Other information:**
Equipment includes technical components of information processing facilities, uninterruptible power supply (UPS) and batteries, power generators, power alternators and converters, physical intrusion detection systems and alarms, smoke detectors, fire extinguishers, air conditioning and lifts.

---
**Section:** 7.14
**Title:** Secure disposal or re-use of equipment

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Physical_security #Asset_management |
| Security domains | #Protection |

**Control:**
Items of equipment containing storage media should be verified to ensure that any sensitive data and licensed software has been removed or securely overwritten prior to disposal or re-use.

**Purpose:**
To prevent leakage of information from equipment to be disposed or re-used.

**Guidance:**
Equipment should be verified to ensure whether or not storage media is contained prior to disposal or re-use.

Storage media containing confidential or copyrighted information should be physically destroyed or the information should be destroyed, deleted or overwritten using techniques to make the original information non-retrievable rather than using the standard delete function. See 7.10 for detailed guidance on secure disposal of storage media and 8.10 for guidance on information deletion.

Labels and markings identifying the organization or indicating the classification, owner, system or network, should be removed prior to disposal, including reselling or donating to charity.

The organization should consider the removal of security controls such as access controls or surveillance equipment at the end of lease or when moving out of premises. This depends on factors such as:
- its lease agreement to return the facility to original condition;
- minimizing the risk of leaving systems with sensitive information on them for the next tenant (e.g. user access lists, video or image files);
- the ability to reuse the controls at the next facility.

**Other information:**
Damaged equipment containing storage media can require a risk assessment to determine whether the items should be physically destroyed rather than sent for repair or discarded. Information can be compromised through careless disposal or re-use of equipment.

In addition to secure disk deletion, full-disk encryption reduces the risk of disclosure of confidential information when equipment is disposed of or redeployed, provided that:
- the encryption process is sufficiently strong and covers the entire disk (including slack space, swap files);
- the cryptographic keys are long enough to resist brute force attacks;
- the cryptographic keys are themselves kept confidential (e.g. never stored on the same disk).

For further advice on cryptography, see 8.24.

Techniques for securely overwriting storage media differ according to the storage media technology and the classification level of the information on the storage media. Overwriting tools should be reviewed to make sure that they are applicable to the technology of the storage media.

See ISO/IEC 27040 for detail on methods for sanitizing storage media.