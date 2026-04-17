### A. Tài liệu gốc của Chương 8 (Control 8.24)

### B. Summary Overview của Chương 8 (Control 8.24)
Tài liệu này mô tả chi tiết **mục 8.24** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào việc áp dụng mật mã và quản lý khóa mã hóa một cách đúng đắn.
Mục tiêu là **bảo vệ tính bảo mật, tính toàn vẹn và tính xác thực của thông tin bằng cryptography, đồng thời kiểm soát vòng đời khóa và các ràng buộc pháp lý liên quan**.
Gồm 1 mục chính:
- `8.24`: Use of cryptography - sử dụng mật mã và quản lý khóa mã hóa theo chính sách

Áp dụng cho dữ liệu lưu trữ, dữ liệu truyền qua mạng, thiết bị đầu cuối, storage media, public key infrastructure, và các dịch vụ hoặc sản phẩm mật mã được dùng trong tổ chức.

### C. Key Points của Chương 8 (Control 8.24)
- **Mục tiêu quản trị:** `8.24` đảm bảo cryptography được dùng đúng mục đích, đúng mức độ và đúng quy trình để bảo vệ dữ liệu và hỗ trợ xác thực/tính toàn vẹn.
- **Yêu cầu chính:** Tổ chức phải có topic-specific policy on cryptography, xác định thuật toán, độ mạnh, trách nhiệm, phạm vi áp dụng và xử lý khóa.
- **Yêu cầu key management:** Khóa phải được tạo, lưu, phân phối, quay vòng, sao lưu, khôi phục, hủy và audit theo quy trình an toàn.
- **Điểm vận hành quan trọng:** Mã hóa có thể ảnh hưởng đến content inspection, malware detection và các control dựa trên kiểm tra nội dung, nên phải được cân bằng với yêu cầu giám sát.
- **Lưu ý thực tế:** Việc dùng cryptography còn phải xét đến luật, hạn chế quốc gia, trans-border flow và trách nhiệm với nhà cung cấp dịch vụ mật mã hoặc CA.

### D. Deep Summary của Chương 8 (Control 8.24)
**Bối cảnh:**
Đây là control nền tảng cho mọi chiến lược bảo mật thông tin hiện đại vì nó bảo vệ dữ liệu ở trạng thái lưu trữ, truyền tải và xác thực. Tuy nhiên, cryptography không chỉ là “bật mã hóa lên”; nếu chọn sai thuật toán, quản lý khóa kém hoặc bỏ qua ràng buộc pháp lý, tổ chức có thể tạo ra cảm giác an toàn giả hoặc thậm chí phát sinh thêm rủi ro.

**Nội dung cốt lõi:**
- `8.24` yêu cầu có chính sách mật mã rõ ràng, xác định mức bảo vệ cần thiết, loại thuật toán và cách dùng mật mã theo loại dữ liệu và bối cảnh.
- `8.24` yêu cầu quản lý khóa chặt chẽ trong toàn bộ vòng đời: tạo, lưu, phân phối, thu hồi, sao lưu, lưu trữ, hủy và ghi log.
- `8.24` nhấn mạnh trách nhiệm và vai trò trong key management, vì mật mã mạnh nhưng vận hành khóa yếu vẫn dẫn đến compromise.
- `8.24` yêu cầu xem xét tác động của encrypted information lên các control khác như malware detection hoặc content filtering.
- `8.24` cũng bao gồm yêu cầu về standards, approved algorithms và hợp đồng với bên cung cấp dịch vụ mật mã, nhất là trong các tình huống xuyên biên giới.

**Dữ liệu đáng chú ý:**
- `8.24` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Secure_configuration` và miền `#Protection`.
- `8.24` bao phủ confidentiality, authenticity, integrity và một số trường hợp non-repudiation, authentication.
- `8.24` có liên hệ đến ISO/IEC 11770 cho key management.
- `8.24` cần cân nhắc legal, statutory, regulatory, contractual requirements liên quan đến cryptography.
- `8.24` yêu cầu bảo vệ secret/private keys khỏi sửa đổi, mất mát, sử dụng trái phép và tiết lộ.

**Rủi ro / Lưu ý:**
- Nếu chính sách mật mã không rõ, tổ chức có thể dùng thuật toán không phù hợp hoặc mã hóa sai chỗ, sai mức.
- Nếu key management yếu, kẻ tấn công có thể phá hỏng toàn bộ cơ chế mã hóa dù thuật toán vẫn mạnh.
- Nếu mã hóa làm mất khả năng content inspection mà không có biện pháp bù trừ, malware detection và filtering có thể bị suy giảm.
- Nếu không xét đến ràng buộc pháp lý hoặc xuyên biên giới, việc triển khai cryptography có thể vi phạm yêu cầu địa phương hoặc hợp đồng.

### E. Structured Output của Chương 8 (Control 8.24)
**Section:** 8.24
**Title:** Use of cryptography

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Secure_configuration |
| Security domains | #Protection |

**Control:**
Rules for the effective use of cryptography, including cryptographic key management, should be defined and implemented.

**Purpose:**
To ensure proper and effective use of cryptography to protect the confidentiality, authenticity or integrity of information according to business and information security requirements, and taking into consideration legal, statutory, regulatory and contractual requirements related to cryptography.

**Guidance:**
***General***
When using cryptography, the following should be considered:
- the topic-specific policy on cryptography defined by the organization, including the general principles for the protection of information. A topic-specific policy on the use of cryptography is necessary to maximize the benefits and minimize the risks of using cryptographic techniques and to avoid inappropriate or incorrect use;
- identifying the required level of protection and the classification of the information and consequently establishing the type, strength and quality of the cryptographic algorithms required;
- the use of cryptography for protection of information held on mobile user endpoint devices or storage media and transmitted over networks to such devices or storage media;
- the approach to key management, including methods to deal with the generation and protection of cryptographic keys and the recovery of encrypted information in the case of lost, compromised or damaged keys;
- roles and responsibilities for:
  1. the implementation of the rules for the effective use of cryptography;
  2. the key management, including key generation (see 8.24);
- the standards to be adopted, as well as cryptographic algorithms, cipher strength, cryptographic solutions and usage practices that are approved or required for use in the organization;
- the impact of using encrypted information on controls that rely on content inspection (e.g. malware detection or content filtering).

When implementing the organization’s rules for effective use of cryptography, the regulations and national restrictions that can apply to the use of cryptographic techniques in different parts of the world should be taken into consideration as well as the issues of trans-border flow of encrypted information (see 5.31).

The contents of service level agreements or contracts with external suppliers of cryptographic services (e.g. with a certification authority) should cover issues of liability, reliability of services and response times for the provision of services (see 5.22).

***Key management***
Appropriate key management requires secure processes for generating, storing, archiving, retrieving, distributing, retiring and destroying cryptographic keys.

A key management system should be based on an agreed set of standards, procedures and secure methods for:
- generating keys for different cryptographic systems and different applications;
- issuing and obtaining public key certificates;
- distributing keys to intended entities, including how to activate keys when received;
- storing keys, including how authorized users obtain access to keys;
- changing or updating keys including rules on when to change keys and how this will be done;
- dealing with compromised keys;
- revoking keys including how to withdraw or deactivate keys [e.g. when keys have been compromised or when a user leaves an organization (in which case keys should also be archived)];
- recovering keys that are lost or corrupted;
- backing up or archiving keys;
- destroying keys;
- logging and auditing of key management related activities;
- setting activation and deactivation dates for keys so that the keys can only be used for the period of time according to the organization's rules on key management;
- handling legal requests for access to cryptographic keys (e.g. encrypted information can be required to be made available in an unencrypted form as evidence in a court case).

All cryptographic keys should be protected against modification and loss. In addition, secret and private keys need protection against unauthorized use as well as disclosure. Equipment used to generate, store and archive keys should be physically protected.

In addition to integrity, for many use cases, the authenticity of public keys should also be considered.

**Other information:**
The authenticity of public keys is usually addressed by public key management processes using certificate authorities and public key certificates, but it is also possible to address it by using technologies such as applying manual processes for small number keys.

Cryptography can be used to achieve different information security objectives, for example:
- confidentiality: using encryption of information to protect sensitive or critical information, either stored or transmitted;
- integrity or authenticity: using digital signatures or message authentication codes to verify the authenticity or integrity of stored or transmitted sensitive or critical information. Using algorithms for the purpose of file integrity checking;
- non-repudiation: using cryptographic techniques to provide evidence of the occurrence or nonoccurrence of an event or action;
- authentication: using cryptographic techniques to authenticate users and other system entities requesting access to or transacting with system users, entities and resources.

The ISO/IEC 11770 series provides further information on key management.
