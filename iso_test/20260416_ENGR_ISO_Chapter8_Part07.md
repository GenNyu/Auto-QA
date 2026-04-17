### A. Tài liệu gốc của Chương 8 (Control 8.11)

### B. Summary Overview của Chương 8 (Control 8.11)
Tài liệu này mô tả chi tiết **mục 8.11** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào việc che giấu hoặc làm giảm khả năng nhận diện dữ liệu nhạy cảm, đặc biệt là PII, khi dữ liệu được xử lý hoặc chia sẻ.
Mục tiêu là **giảm mức lộ lọt thông tin nhạy cảm, bảo vệ PII theo yêu cầu pháp lý và kiểm soát cách dữ liệu được ẩn, thay thế hoặc làm ẩn danh trong từng bối cảnh sử dụng**.
Gồm 1 mục chính:
- `8.11`: Data masking - che giấu, ẩn danh hoặc giả danh dữ liệu nhạy cảm để hạn chế lộ thông tin

Áp dụng cho dữ liệu nhạy cảm, dữ liệu PII, dữ liệu dùng cho báo cáo, phân tích, chia sẻ nội bộ/bên ngoài và các môi trường mà người dùng không cần xem toàn bộ thông tin gốc.

### C. Key Points của Chương 8 (Control 8.11)
- **Mục tiêu quản trị:** `8.11` giảm rủi ro lộ PII hoặc dữ liệu nhạy cảm bằng cách chỉ hiển thị mức thông tin tối thiểu cần thiết cho đúng người, đúng mục đích.
- **Yêu cầu chính:** Tổ chức phải dùng data masking, pseudonymization hoặc anonymization theo chính sách truy cập, chính sách dữ liệu và yêu cầu pháp lý liên quan.
- **Yêu cầu kỹ thuật quan trọng:** Cần xác minh dữ liệu đã được che giấu đủ mạnh, vì nếu còn các trường phụ trợ thì vẫn có thể suy ra danh tính hoặc thông tin nhạy cảm.
- **Điểm vận hành quan trọng:** Data masking không thay thế access control; nó là lớp bổ sung để giảm mức lộ dữ liệu khi truy cập hoặc chia sẻ là cần thiết nhưng không nên thấy toàn bộ nội dung gốc.
- **Lưu ý thực tế:** Với các trường hợp nhạy cảm như hồ sơ y tế hoặc dữ liệu thanh toán, tổ chức cần xác định mức che giấu phù hợp, quyền xem từng vai trò và cơ chế ghi nhận việc cấp/nhận dữ liệu đã che giấu.

### D. Deep Summary của Chương 8 (Control 8.11)
**Bối cảnh:**
Đây là control dùng để giảm mức lộ thông tin chứ không nhất thiết xóa bỏ thông tin. Trong nhiều tình huống, dữ liệu vẫn cần được dùng cho vận hành, phân tích, hỗ trợ hoặc chia sẻ, nhưng không phải ai cũng được thấy dữ liệu gốc. Vì vậy, data masking, pseudonymization và anonymization trở thành lớp bảo vệ thực dụng giữa tính hữu ích của dữ liệu và yêu cầu bảo mật.

**Nội dung cốt lõi:**
- `8.11` yêu cầu chọn kỹ thuật che giấu phù hợp với mục đích xử lý và mức độ nhạy cảm của dữ liệu, thay vì áp dụng một phương pháp chung cho mọi tình huống.
- `8.11` phân biệt giữa masking, pseudonymization và anonymization, trong đó mức độ bảo vệ và khả năng tái nhận dạng khác nhau rõ rệt.
- `8.11` yêu cầu kiểm tra xem dữ liệu đã được ẩn đủ tốt hay chưa, vì dữ liệu phụ trợ hoặc mối liên hệ gián tiếp vẫn có thể làm lộ danh tính.
- `8.11` cũng xử lý các yêu cầu đặc thù như obfuscation theo vai trò, dữ liệu thanh toán, dữ liệu y tế và các trường hợp người được bảo vệ không muốn lộ ngay cả dấu hiệu rằng dữ liệu đã bị che giấu.
- `8.11` có ý nghĩa vận hành cao trong báo cáo, analytics, chia sẻ dữ liệu, cloud và nghiên cứu thống kê, nơi dữ liệu cần hữu dụng nhưng không cần tiết lộ trực tiếp.

**Dữ liệu đáng chú ý:**
- `8.11` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, thuộc `#Information_protection #Protection` và miền `#Protection`.
- Data masking có thể là static, dynamic hoặc on-the-fly tùy vào cách dữ liệu được dùng.
- Pseudonymization khác anonymization ở chỗ vẫn có “additional information” hoặc cơ chế bổ sung để tái nhận dạng ở mức nào đó.
- Hash dùng để anonymize PII nên đi kèm salt để giảm rủi ro enumeration attacks.
- PII trong resource identifiers như file names hoặc URLs cũng cần được tránh hoặc ẩn danh hóa phù hợp.

**Rủi ro / Lưu ý:**
- Nếu masking không đủ mạnh, người dùng vẫn có thể suy ra danh tính hoặc thông tin nhạy cảm từ dữ liệu phụ trợ.
- Nếu nhầm pseudonymization với anonymization, tổ chức có thể đánh giá sai mức bảo vệ và chia sẻ dữ liệu quá rộng.
- Nếu không quản lý “additional information” hoặc salt, kẻ tấn công có thể tái nhận dạng hoặc brute-force dữ liệu đã che giấu.
- Nếu chỉ che dữ liệu trên một hệ thống nhưng bỏ sót file name, URL hoặc log, thông tin nhạy cảm vẫn có thể bị lộ.

### E. Structured Output của Chương 8 (Control 8.11)
**Section:** 8.11
**Title:** Data masking

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Information_protection #Protection |
| Security domains | #Protection |

**Control:**
Data masking should be used in accordance with the organization’s topic-specific policy on access control and other related topic-specific policies, and business requirements, taking applicable legislation into consideration.

**Purpose:**
To limit the exposure of sensitive data including PII, and to comply with legal, statutory, regulatory and contractual requirements.

**Guidance:**
Where the protection of sensitive data (e.g. PII) is a concern, the organization should consider hiding such data by using techniques such as data masking, pseudonymization or anonymization.

Pseudonymization or anonymization techniques can hide PII, disguise the true identity of PII principals or other sensitive information, and disconnect the link between PII and the identity of the PII principal or the link between other sensitive information.

When using pseudonymization or anonymization techniques, it should be verified that data has been adequately pseudonymized or anonymized. Data anonymization should consider all the elements of the sensitive information to be effective. As an example, if not considered properly, a person can be identified even if the data that can directly identify that person is anonymised, by the presence of further data which allows the person to be identified indirectly.

Additional techniques for data masking include:
- encryption (requiring authorized users to have a key);
- nulling or deleting characters (preventing unauthorized users from seeing full messages);
- varying numbers and dates;
- substitution (changing one value for another to hide sensitive data);
- replacing values with their hash.

The following should be considered when implementing data masking techniques:
- not granting all users access to all data, therefore designing queries and masks in order to show only the minimum required data to the user;
- there are cases where some data should not be visible to the user for some records out of a set of data; in this case, designing and implementing a mechanism for obfuscation of data (e.g. if a patient does not want hospital staff to be able to see all of their records, even in case of emergency, then the hospital staff are presented with partially obfuscated data and data can only be accessed by staff with specific roles if it contains useful information for appropriate treatment);
- when data are obfuscated, giving the PII principal the possibility to require that users cannot see if the data are obfuscated (obfuscation of the obfuscation; this is used in health facilities, for example if the patient does not want personnel to see that sensitive information such as pregnancies or results of blood exams has been obfuscated);
- any legal or regulatory requirements (e.g. requiring the masking of payment cards' information during processing or storage).

The following should be considered when using data masking, pseudonymization or anonymization:
- level of strength of data masking, pseudonymization or anonymization according to the usage of the processed data;
- access controls to the processed data;
- agreements or restrictions on usage of the processed data;
- prohibiting collating the processed data with other information in order to identify the PII principal;
- keeping track of providing and receiving the processed data.

**Other information:**
Anonymization irreversibly alters PII in such a way that the PII principal can no longer be identified directly or indirectly.

Pseudonymization replaces the identifying information with an alias. Knowledge of the algorithm (sometimes referred to as the “additional information”) used to perform the pseudonymization allows for at least some form of identification of the PII principal. Such “additional information” should therefore be kept separate and protected.

While pseudonymization is therefore weaker than anonymization, pseudonymized datasets can be more useful in statistical research.

Data masking is a set of techniques to conceal, substitute or obfuscate sensitive data items. Data masking can be static (when data items are masked in the original database), dynamic (using automation and rules to secure data in real-time) or on-the-fly (with data masked in an application’s memory).

Hash functions can be used in order to anonymize PII. In order to prevent enumeration attacks, they should always be combined with a salt function.

PII in resource identifiers and their attributes [e.g. file names, uniform resource locators (URLs)] should be either avoided or appropriately anonymized.

Additional controls concerning the protection of PII in public clouds are given in ISO/IEC 27018.

Additional information on de-identification techniques is available in ISO/IEC 20889.