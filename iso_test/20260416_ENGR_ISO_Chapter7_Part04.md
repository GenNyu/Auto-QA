### A. Tài liệu gốc của Chương 7 (Control 7.10, 7.11)

### B. Summary Overview của Chương 7 (Control 7.10, 7.11)
Tài liệu này mô tả chi tiết **mục 7.10 và 7.11** trong **chương 7. Physical controls** của **ISO/IEC 27002:2022**, tập trung vào việc quản lý vòng đời vật lý của phương tiện lưu trữ và bảo đảm các tiện ích hỗ trợ cho hệ thống thông tin luôn sẵn sàng và ổn định.
Mục tiêu là **ngăn rò rỉ hoặc mất mát dữ liệu trên storage media, đồng thời giảm nguy cơ gián đoạn hoạt động do mất điện, nước, viễn thông hoặc các utility hỗ trợ khác**.
Gồm 2 mục chính:
- `7.10`: Storage media - quản lý phương tiện lưu trữ trong toàn bộ vòng đời
- `7.11`: Supporting utilities - bảo vệ các tiện ích hỗ trợ như điện, nước, viễn thông, điều hòa

Áp dụng cho phương tiện lưu trữ giấy hoặc điện tử, thiết bị chứa dữ liệu, và toàn bộ hạ tầng utility hỗ trợ hoạt động của hệ thống xử lý thông tin.

### C. Key Points của Chương 7 (Control 7.10, 7.11)
- **Mục tiêu quản trị:** Nhóm control này bảo vệ dữ liệu ở trạng thái lưu trữ và bảo đảm cơ sở hạ tầng hỗ trợ không bị đứt gãy, vì cả hai đều có thể làm thất thoát thông tin hoặc ngưng trệ vận hành.
- **Yêu cầu chính của 7.10:** Storage media phải được quản lý xuyên suốt vòng đời từ mua, dùng, vận chuyển đến tiêu hủy; khi cần dùng lại hoặc loại bỏ phải có quy trình xóa an toàn, hủy an toàn và lưu vết phù hợp.
- **Yêu cầu chính của 7.11:** Các utility như điện, nước, gas, viễn thông, thông gió và điều hòa phải được giám sát, bảo trì, kiểm thử và có phương án dự phòng để không làm gián đoạn hệ thống thông tin.
- **Điểm vận hành quan trọng:** `7.10` không chỉ áp dụng cho media điện tử mà còn bao gồm giấy tờ; `7.11` yêu cầu phối hợp giữa cấu hình thiết bị, cấp nguồn, cảnh báo, lối thoát khẩn cấp và dữ liệu liên hệ khi xảy ra sự cố.
- **Lưu ý thực tế:** Việc lưu trữ, tái sử dụng và tiêu hủy media, cũng như quản lý utility, cần gắn với phân loại dữ liệu và mức độ nhạy cảm, không dùng một quy trình duy nhất cho mọi trường hợp.

### D. Deep Summary của Chương 7 (Control 7.10, 7.11)
**Bối cảnh:**
Hai control này xử lý hai rủi ro nền tảng nhưng dễ bị bỏ qua: dữ liệu còn sót trên storage media và sự phụ thuộc vào các tiện ích hỗ trợ bên ngoài hệ thống thông tin. Nếu media không được quản lý đúng vòng đời, thông tin có thể lộ ra khi tái sử dụng, vận chuyển hoặc tiêu hủy. Nếu utility đứt gãy, toàn bộ hạ tầng xử lý thông tin có thể dừng hoạt động dù bản thân hệ thống vẫn còn nguyên.

**Nội dung cốt lõi:**
- `7.10` yêu cầu tổ chức quản lý storage media theo toàn bộ vòng đời, bao gồm quy tắc sử dụng, cấp phép mang ra ngoài, theo dõi chuỗi bàn giao và bảo vệ theo mức độ phân loại thông tin.
- `7.10` nhấn mạnh bảo vệ media khỏi môi trường xung quanh như nhiệt, ẩm, từ trường, lão hóa, và sử dụng mã hóa khi tính bảo mật hoặc toàn vẹn là quan trọng.
- `7.10` yêu cầu quy trình tái sử dụng hoặc tiêu hủy an toàn, bao gồm xóa dữ liệu trước khi dùng lại, hủy vật lý khi cần và ghi log tiêu hủy để tạo audit trail.
- `7.11` yêu cầu bảo đảm các utility được cấu hình, vận hành, kiểm tra và giám sát theo chuẩn, đồng thời có báo động, nguồn cấp đa tuyến hoặc tách mạng nếu cần.
- `7.11` cũng yêu cầu chuẩn bị các cơ chế khẩn cấp như chiếu sáng khẩn cấp, công tắc cắt điện/nước/gas, và thông tin liên hệ để ứng phó khi utility bị gián đoạn.

**Dữ liệu đáng chú ý:**
- `7.10` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Physical_security#Asset_management` và miền `#Protection`.
- `7.11` là kiểm soát `#Preventive #Detective`, gắn với `#Integrity`, `#Availability`, thuộc `#Physical_security` và miền `#Protection`.
- `7.10` cho phép áp dụng cho cả storage media không điện tử, nên media giấy vẫn thuộc phạm vi kiểm soát.
- `7.11` coi utility là một phần của nền tảng vận hành, không phải hạ tầng phụ trợ thứ yếu.
- `7.10` gợi ý rằng nếu dữ liệu trên media không được mã hóa, cần bổ sung bảo vệ vật lý mạnh hơn.

**Rủi ro / Lưu ý:**
- Nếu storage media không được quản lý theo vòng đời, dữ liệu có thể bị sao chép, tái sử dụng trái phép hoặc lộ ra khi tiêu hủy không đúng cách.
- Nếu media chứa dữ liệu nhạy cảm bị mang ra ngoài mà không có thẩm quyền hoặc audit trail, tổ chức sẽ khó truy vết và khó chứng minh trách nhiệm khi có sự cố.
- Nếu utility không được kiểm tra và dự phòng đầy đủ, sự cố mất điện, nước, viễn thông hoặc điều hòa có thể làm dừng hoạt động và gây hư hại thiết bị.
- Nếu công tắc khẩn cấp, thông tin liên hệ hoặc quy trình phản ứng không sẵn sàng, tổ chức sẽ phản ứng chậm khi utility bị gián đoạn.

### E. Structured Output của Chương 7 (Control 7.10, 7.11)
**Section:** 7.10
**Title:** Storage media

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Physical_security #Asset_management |
| Security domains | #Protection |

**Control:**
Storage media should be managed through their life cycle of acquisition, use, transportation and disposal in accordance with the organization’s classification scheme and handling requirements.

**Purpose:**
To ensure only authorized disclosure, modification, removal or destruction of information on storage media.

**Guidance:**
***Removable storage media***
The following guidelines for the management of removable storage media should be considered:
- establishing a topic-specific policy on the management of removable storage media and communicating such topic- specific policy to anyone who uses or handles removable storage media;
- where necessary and practical, requiring authorization for storage media to be removed from the organization and keeping a record of such removals in order to maintain an audit trail;
- storing all storage media in a safe, secure environment according to their information classification and protecting them against environmental threats (such as heat, moisture, humidity, electronic field or ageing), in accordance with manufacturers’ specifications;
- if information confidentiality or integrity are important considerations, using cryptographic techniques to protect information on removable storage media;
- to mitigate the risk of storage media degrading while stored information is still needed, transferring the information to fresh storage media before becoming unreadable;
- storing multiple copies of valuable information on separate storage media to further reduce the risk of coincidental information damage or loss;
- considering the registration of removable storage media to limit the chance for information loss;
- only enabling removable storage media ports [e.g. secure digital (SD) card slots and universal serial bus (USB) ports] if there is an organizational reason for their use;
- where there is a need to use removable storage media, monitoring the transfer of information to such storage media;
- information can be vulnerable to unauthorized access, misuse or corruption during physical transport, for instance when sending storage media via the postal service or via courier.

In this control, media includes paper documents. When transferring physical storage media, apply security measures in 5.14.

***Secure reuse or disposal***
Procedures for the secure reuse or disposal of storage media should be established to minimize the risk of confidential information leakage to unauthorized persons. The procedures for secure reuse or disposal of storage media containing confidential information should be proportional to the sensitivity of that information. The following items should be considered:
- if storage media containing confidential information need to be reused within the organization, securely deleting data or formatting the storage media before reuse (see 8.10);
- disposing of storage media containing confidential information securely when not needed anymore (e.g. by destroying, shredding or securely deleting the content);
- having procedures in place to identify the items that can require secure disposal;
- many organizations offer collection and disposal services for storage media. Care should be taken in selecting a suitable external party supplier with adequate controls and experience;
- logging the disposal of sensitive items in order to maintain an audit trail;
- when accumulating storage media for disposal, giving consideration to the aggregation effect, which can cause a large quantity of non-sensitive information to become sensitive.

A risk assessment should be performed on damaged devices containing sensitive data to determine whether the items should be physically destroyed rather than sent for repair or discarded (see 7.14).

**Other information:**
When confidential information on storage media is not encrypted, additional physical protection of the storage media should be considered.

---
**Section:** 7.11
**Title:** Supporting utilities

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive #Detective |
| Information security properties | #Integrity #Availability |
| Cybersecurity concepts | #Protect #Detect |
| Operational capabilities | #Physical_security |
| Security domains | #Protection |

**Control:**
Information processing facilities should be protected from power failures and other disruptions caused by failures in supporting utilities.

**Purpose:**
To prevent loss, damage or compromise of information and other associated assets, or interruption to the organization’s operations due to failure and disruption of supporting utilities.

**Guidance:**
Organizations depend on utilities (e.g. electricity, telecommunications, water supply, gas, sewage, ventilation and air conditioning) to support their information processing facilities. Therefore, the organization should:
- ensure equipment supporting the utilities is configured, operated and maintained in accordance with the relevant manufacturer’s specifications;
- ensure utilities are appraised regularly for their capacity to meet business growth and interactions with other supporting utilities;
- ensure equipment supporting the utilities is inspected and tested regularly to ensure their proper functioning;
- if necessary, raise alarms to detect utilities malfunctions;
- if necessary, ensure utilities have multiple feeds with diverse physical routing;
- ensure equipment supporting the utilities is on a separate network from the information processing facilities if connected to a network;
- ensure equipment supporting the utilities is connected to the internet only when needed and only in a secure manner.

Emergency lighting and communications should be provided. Emergency switches and valves to cut off power, water, gas or other utilities should be located near emergency exits or equipment rooms. Emergency contact details should be recorded and available to personnel in the event of an outage.

**Other information:**
Additional redundancy for network connectivity can be obtained by means of multiple routes from more than one utility provider.