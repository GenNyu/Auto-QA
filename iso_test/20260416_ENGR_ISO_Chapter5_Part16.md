### A. Tài liệu gốc của Chương 5 (Control 5.33, 5.34)

### B. Summary Overview của Chương 5 (Control 5.33, 5.34)
Tài liệu này mô tả chi tiết **mục 5.33 và 5.34** trong **Chương 5 (Organizational controls)** của **ISO/IEC 27002:2022**, tập trung vào việc bảo vệ hồ sơ/tài liệu có giá trị lưu trữ và bảo vệ dữ liệu cá nhân định danh (PII) theo yêu cầu pháp lý, hợp đồng và kỳ vọng xã hội.
Mục tiêu là bảo đảm hồ sơ không bị mất, sửa, tiết lộ trái phép và PII được xử lý đúng nghĩa vụ bảo mật, quyền riêng tư và tuân thủ theo từng bối cảnh pháp lý.
Gồm 2 mục chính:
- `5.33`: Protection of records - bảo vệ hồ sơ khỏi mất mát, hủy hoại, sửa đổi hoặc truy cập/phát hành trái phép.
- `5.34`: Privacy and protection of PII - xác định và đáp ứng yêu cầu bảo vệ quyền riêng tư và PII.

Áp dụng cho các cá nhân, bộ phận và vai trò xử lý hồ sơ, dữ liệu cá nhân và các nghĩa vụ tuân thủ liên quan.

### C. Key Points của Chương 5 (Control 5.33, 5.34)
- **Mục tiêu quản trị:** Bảo đảm dữ liệu lưu trữ và PII được quản lý có kiểm soát, không chỉ để an toàn thông tin mà còn để đáp ứng yêu cầu pháp lý.
- **Yêu cầu chính của 5.33-5.34:** Phải bảo vệ hồ sơ khỏi mất mát/sửa đổi/truy cập trái phép và phải xác định rõ trách nhiệm, quy trình khi xử lý PII.
- **Điểm vận hành quan trọng:** Cần có quy tắc lưu trữ, giữ gìn chuỗi bàn giao, thời hạn lưu giữ và kiểm soát quyền truy cập phù hợp.
- **Lưu ý thực tế:** Nếu không quản lý đúng phạm vi và thời hạn lưu giữ, tổ chức có thể vừa mất bằng chứng nghiệp vụ vừa vi phạm riêng tư.

### D. Deep Summary của Chương 5 (Control 5.33, 5.34)
**Bối cảnh:**
Đây là nhóm control gắn với việc quản lý thông tin có giá trị lưu trữ lâu dài và dữ liệu nhạy cảm của cá nhân. Điểm quan trọng không chỉ là bảo mật mà còn là khả năng chứng minh tuân thủ và xử lý dữ liệu đúng mục đích.

**Nội dung cốt lõi:**
- 5.33 yêu cầu bảo vệ hồ sơ theo vòng đời đầy đủ: tạo lập, lưu trữ, truy xuất, lưu giữ và hủy bỏ.
- 5.33 cũng nhấn mạnh chuỗi bàn giao, tính toàn vẹn và khả năng truy xuất trong thời gian lưu giữ.
- 5.34 yêu cầu tổ chức xác định nghĩa vụ pháp lý và thiết lập vai trò, quy trình, kiểm soát để bảo vệ PII.
- Hai control này thường gắn chặt với quản lý hồ sơ, dữ liệu khách hàng, nhân sự và các nền tảng lưu trữ dài hạn.

**Dữ liệu đáng chú ý:**
- 5.33 gắn với `Preventive`, vì trọng tâm là ngăn ngừa mất mát hoặc lộ lọt hồ sơ từ sớm.
- 5.34 cũng là `Preventive`, vì cần kiểm soát dữ liệu cá nhân ngay từ khâu thiết kế quy trình và hệ thống.
- Cả hai control đều gắn với `Identify #Protect`, cho thấy việc nhận diện đúng loại thông tin là điều kiện tiên quyết để áp kiểm soát phù hợp.

**Rủi ro / Lưu ý:**
- Nếu không có quy tắc lưu giữ và hủy bỏ rõ ràng, hồ sơ có thể bị mất giá trị pháp lý hoặc bị giữ quá mức cần thiết.
- Nếu không kiểm soát PII theo bối cảnh pháp lý từng quốc gia, việc chuyển dữ liệu xuyên biên giới hoặc xử lý sai mục đích có thể phát sinh rủi ro lớn.
- Nếu không xác định rõ người chịu trách nhiệm, việc xử lý hồ sơ và PII dễ bị phân tán, khó kiểm soát và khó audit.

### E. Structured Output của Chương 5 (Control 5.33, 5.34)
**Section:** 5.33
**Title:** Protection of records

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality#Integrity#Availability |
| Cybersecurity concepts | #Identify #Protect |
| Operational capabilities | #Legal_and_compliance#Asset_management#Information_protection |
| Security domains | #Defence |

**Control:**
Records should be protected from loss, destruction, falsification, unauthorized access and unauthorized release.

**Purpose:**
To ensure compliance with legal, statutory, regulatory and contractual requirements, as well as community or societal expectations related to the protection and availability of records.

**Guidance:**
The organization should take the following steps to protect the authenticity, reliability, integrity and usability of records, as their business context and requirements for their management change over time:
- issue guidelines on the storage, handling chain of custody and disposal of records, which includes prevention of manipulation of records. These guidelines should be aligned with the organization’s topic-specific policy on records management and other records requirements;
- draw up a retention schedule defining records and the period of time for which they should be retained.

The system of storage and handling should ensure identification of records and of their retention period taking into consideration national or regional legislation or regulations, as well as community or societal expectations, if applicable. This system should permit appropriate destruction of records after that period if they are not needed by the organization.
When deciding on protection of specific organizational records, their corresponding information security classification, based on the organization’s classification scheme, should be considered. Records should be categorized into record types (e.g. accounting records, business transaction records, personnel records, legal records), each with details of retention periods and type of allowable storage media which can be physical or electronic.
Data storage systems should be chosen such that required records can be retrieved in an acceptable time frame and format, depending on the requirements to be fulfilled.
Where electronic storage media are chosen, procedures to ensure the ability to access records (both storage media and format readability) throughout the retention period should be established to safeguard against loss due to future technology change. Any related cryptographic keys and programs associated with encrypted archives or digital signatures, should also be retained to enable decryption of the records for the length of time the records are retained (see 8.24).
Storage and handling procedures should be implemented in accordance with recommendations provided by manufacturers of storage media. Consideration should be given to the possibility of deterioration of media used for storage of records.

**Other information:**
Records document individual events or transactions or can form aggregations that have been designed to document work processes, activities or functions. They are both evidence of business activity and information assets. Any set of information, regardless of its structure or form, can be managed as a record. This includes information in the form of a document, a collection of data or other types of digital or analogue information which are created, captured and managed in the course of business.
In the management of records, metadata is data describing the context, content and structure of records, as well as their management over time. Metadata is an essential component of any record.
It can be necessary to retain some records securely to meet legal, statutory, regulatory or contractual requirements, as well as to support essential business activities. National law or regulation can set the time period and data content for information retention. Further information about records management can be found in ISO 15489.

---
**Section:** 5.34
**Title:** Privacy and protection of PII

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality#Integrity#Availability |
| Cybersecurity concepts | #Identify #Protect |
| Operational capabilities | #Information_protection#Legal_and_compliance |
| Security domains | #Protection |

**Control:**
The organization should identify and meet the requirements regarding the preservation of privacy and protection of PII according to applicable laws and regulations and contractual requirements.

**Purpose:**
To ensure compliance with legal, statutory, regulatory and contractual requirements related to the information security aspects of the protection of PII.

**Guidance:**
The organization should establish and communicate a topic-specific policy on privacy and protection of PII to all relevant interested parties.
The organization should develop and implement procedures for the preservation of privacy and protection of PII. These procedures should be communicated to all relevant interested parties involved in the processing of personally identifiable information.
Compliance with these procedures and all relevant legislation and regulations concerning the preservation of privacy and protection of PII requires appropriate roles, responsibilities and controls. Often this is best achieved by the appointment of a person responsible, such as a privacy officer, who should provide guidance to personnel, service providers and other interested parties on their individual responsibilities and the specific procedures that should be followed.
Responsibility for handling PII should be dealt with taking into consideration relevant legislation and regulations.
Appropriate technical and organizational measures to protect PII should be implemented.

**Other information:**
A number of countries have introduced legislation placing controls on the collection, processing, transmission and deletion of PII. Depending on the respective national legislation, such controls can impose duties on those collecting, processing and disseminating PII and can also restrict the authority to transfer PII to other countries.
ISO/IEC 29100 provides a high-level framework for the protection of PII within ICT systems. Further information on privacy information management systems can be found in ISO/IEC 27701. Specific information regarding privacy information management for public clouds acting as PII processors can be found in ISO/IEC 27018.
ISO/IEC 29134 provides guidelines for privacy impact assessment (PIA) and gives an example of the structure and content of a PIA report. Compared with ISO/IEC 27005, this is focused on PII processing and relevant to those organizations that process PII. This can help identify privacy risks and possible mitigations to reduce these risks to acceptable levels.