### A. Tài liệu gốc của Requirement 3

### B. Summary Overview của Control Objective 3.5
Tài liệu này mô tả chi tiết **Control Objective 3.5 **của **Requirement 3 **trong **PCI-DSS v4.0.1**, tập trung vào việc bảo vệ PAN lưu trữ bằng cách làm dữ liệu không thể đọc được khi truy cập trái phép.
Mục tiêu chính là đảm bảo PAN được render unreadable ở mọi vị trí lưu trữ thông qua các cơ chế như mã hóa, hashing, truncation hoặc tokenization.
Gồm 1 sub-requirement chính:
- 3.5.1: Bảo vệ PAN lưu trữ (render unreadable)
Áp dụng cho tất cả môi trường lưu trữ PAN, bao gồm primary storage (database, file) và non-primary storage (backup, log, archive).

### C. Key Points của Control Objective 3.5
- **Phạm vi áp dụng:**Tất cả nơi lưu trữ PAN (DB, file, log, backup…)
- **Trách nhiệm:**Tài liệu hóa phương pháp bảo vệ PAN và đảm bảo áp dụng thực tế
- **Bảo vệ dữ liệu:** PAN phải được render unreadable bằng hashing, truncation, tokenization hoặc mã hóa mạnh
- **Kiểm soát kết hợp:**Nếu tồn tại nhiều dạng PAN (hash + truncate), phải ngăn việc correlation
- **Kiểm soát mã hóa:**Disk-level encryption không đủ nếu dùng đơn lẻ
- **Quản lý truy cập:**Chỉ giải mã PAN khi có business need hợp lệ

### D. Deep Summary của Control Objective 3.5
**Bối cảnh:**
PAN lưu trữ là mục tiêu chính khi hệ thống bị xâm nhập. Nếu dữ liệu ở dạng cleartext, attacker có thể khai thác trực tiếp để gian lận.
**Nội dung cốt lõi:**
- PAN phải được làm không thể đọc được tại mọi nơi lưu trữ
- Áp dụng các phương pháp: hashing, truncation, tokenization, strong cryptography
- Đảm bảo không thể kết hợp các dạng dữ liệu để khôi phục PAN gốc
- Disk-level encryption chỉ là lớp bổ sung, không phải cơ chế chính
- Chỉ cho phép giải mã khi có business need rõ ràng
**Dữ liệu đáng chú ý:**
- Áp dụng cho cả primary và non-primary storage (log, backup…)
- Có thể tồn tại cleartext tạm thời trong quá trình xử lý (encrypt/decrypt)
**Rủi ro / Lưu ý:**
- Lưu PAN dạng cleartext → rủi ro rò rỉ nghiêm trọng
- Chỉ dùng disk encryption → không đáp ứng yêu cầu PCI DSS
- Có thể reconstruct PAN nếu không kiểm soát correlation giữa các dạng dữ liệu
- Bỏ sót log/backup → lộ dữ liệu ngoài kiểm soát

### E. Structured Output của Requirement 3
**Control objectives:**3.5
**Sub-requirement:**3.5.1 *(Tag: PAN protection, encryption, tokenization, hashing, truncation, data security at rest)*
**Defined Approach Requirements of 3.5.1:**PAN is rendered unreadable anywhere it is stored by using any of the following approaches:
• One-way hashes based on strong cryptography of the entire PAN.
• Truncation (hashing cannot be used to replace the truncated segment of PAN). - If hashed and truncated versions of the same PAN, or different truncation formats of the same PAN, are present in an environment, additional controls are in place such that the different versions cannot be correlated to reconstruct the original PAN.
• Index tokens.
• Strong cryptography with associated key- management processes and procedures.
**Defined Approach Testing Procedures of 3.5.1:**
- "3.5.1.a": Examine documentation about the system used to render PAN unreadable, including the vendor, type of system/process, and the encryption algorithms (if applicable) to verify that the PAN is rendered unreadable using any of the methods specified in this requirement.
- "3.5.1.b": Examine data repositories and audit logs, including payment application logs, to verify the PAN is rendered unreadable using any of the methods specified in this requirement.
- "3.5.1.c": If hashed and truncated versions of the same PAN are present in the environment, examine implemented controls to verify that the hashed and truncated versions cannot be correlated to reconstruct the original PAN.
**Customized Approach Objective of 3.5.1:**Cleartext PAN cannot be read from storage media.
**Applicability Notes of 3.5.1:**This requirement applies to PANs stored in primary storage (databases, or flat files such as text files spreadsheets) as well as non-primary storage (backup, audit logs, exception, or troubleshooting logs). This requirement does not preclude the use of temporary files containing cleartext PAN while encrypting and decrypting PAN.
**Guidance - Purpose of 3.5.1:**Rendering stored PAN unreadable is a defense in depth control designed to protect the data if an unauthorized individual gains access to stored data by taking advantage of a vulnerability or misconfiguration of an entity's primary access control.
**Guidance - Good Practice of 3.5.1:**It is a relatively trivial effort for a malicious individual to reconstruct original PAN data if they have access to both the truncated and hashed versions of a PAN. Controls that prevent the correlation of this data will help ensure that the original PAN remains unreadable. Implementing keyed cryptographic hashes with associated key management processes and procedures in accordance with Requirement 3.5.1.1 is a valid additional control to prevent correlation.
**Guidance - Further Information of 3.5.1:**For information about truncation formats and truncation in general, see PCI SSC's FAQs on the topic. Sources for information about index tokens include:
• PCI SSC's Tokenization Product Security Guidelines ( https://www.pcisecuritystandards.org/documents/Tokenization_Product_Security_Guidelines.pdf )
• ANSI X9.119-2-2017: Retail Financial Services - Requirements For Protection Of Sensitive Payment Card Data - Part 2: Implementing Post-Authorization Tokenization Systems

---
**Control objectives:**3.5
**Sub-requirement:**3.5.1.1 *(Tag: keyed hashing, cryptographic hash, integrity protection)*
**Defined Approach Requirements of 3.5.1.1:**Hashes used to render PAN unreadable (per the first bullet of Requirement 3.5.1) are keyed cryptographic hashes of the entire PAN, with associated key- management processes and procedures in accordance with Requirements 3.6 and 3.7.
**Defined Approach Testing Procedures of 3.5.1.1:**
- "3.5.1.1.a": Examine documentation about the hashing method used to render PAN unreadable, including the vendor, type of system/process, and the encryption algorithms (as applicable) to verify that the hashing method results in keyed cryptographic hashes of the entire PAN, with associated key management processes and procedures.
- "3.5.1.1.b": Examine documentation about the key management procedures and processes associated with the keyed cryptographic hashes to verify keys are managed in accordance with Requirements 3.6 and 3.7.
- "3.5.1.1.c": Examine data repositories to verify the PAN is rendered unreadable.
- "3.5.1.1.d": Examine audit logs, including payment application logs, to verify the PAN is rendered unreadable.
**Customized Approach Objective of 3.5.1.1:**Cleartext PAN cannot be determined from hashes of the PAN.
**Applicability Notes of 3.5.1.1:**All Applicability Notes for Requirement 3.5.1 also apply to this requirement. Key-management processes and procedures (Requirements 3.6 and 3.7) do not apply to system components used to generate individual keyed hashes of a PAN for comparison to another system if:
• The system components only have access to one hash value at a time (hash values are not stored on the system) AND
• There is no other account data stored on the same system as the hashes. This requirement is considered a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. This requirement will replace the bullet in Requirement 3.5.1 for one-way hashes once its effective date is reached.
**Guidance - Purpose of 3.5.1.1:**Rendering stored PAN unreadable is a defense in depth control designed to protect the data if an unauthorized individual gains access to stored data by taking advantage of a vulnerability or misconfiguration of an entity's primary access control. A hashing function that incorporates a randomly generated secret key provides brute force attack resistance and secret authentication integrity.
**Guidance - Definitions of 3.5.1.1:**Refer to Appendix G for the definition of 'keyed cryptographic hash' and for information about appropriate keyed cryptographic hashing algorithms and additional resources.
**Guidance - Examples of 3.5.1.1:**Systems which only have access to one hash value at a time and which store no other account data on the same system as the hash, are not required to meet key-management processes and procedures (Requirements 3.6 and 3.7). Examples of such systems include transaction-originating devices that generate a hash of the PAN for use in a backend system, such as pay-at-gate transit turnstiles. However, in such an implementation, the backend system will have access to more than one hash value at a time, and therefore is required to meet key-management processes and procedures at Requirements 3.6 and 3.7.

---
**Control objectives:**3.5
**Sub-requirement:**3.5.1.2 *(Tag: disk encryption risk, data-level encryption, defense-in-depth)*
**Defined Approach Requirements of 3.5.1.2:**If disk-level or partition-level encryption (rather than file-, column-, or field-level database encryption) is used to render PAN unreadable, it is implemented only as follows:
• On removable electronic media OR
• If used for non-removable electronic media, PAN is also rendered unreadable via another mechanism that meets Requirement 3.5.1.
**Defined Approach Testing Procedures of 3.5.1.2:**
- "3.5.1.2.a": Examine encryption processes to verify that, if disk-level or partition-level encryption is used to render PAN unreadable, it is implemented only as follows: • On removable electronic media, OR • If used for non-removable electronic media, examine encryption processes used to verify that PAN is also rendered unreadable via another method that meets Requirement 3.5.1.
- "3.5.1.2.b": Examine configurations and/or vendor documentation and observe encryption processes to verify the system is configured according to vendor documentation the result is that the disk or the partition is rendered unreadable.
**Customized Approach Objective of 3.5.1.2:**Encrypted PAN is only decrypted when there is a legitimate business need to access that PAN.
**Applicability Notes of 3.5.1.2:**This requirement applies to any encryption method that provides clear-text PAN automatically when a system runs, even though an authorized user has not specifically requested that data. While disk or partition encryption may still be present on these types of devices, it cannot be the only mechanism used to protect PAN stored on those systems. Any stored PAN must also be rendered unreadable per Requirement 3.5.1-for example, through truncation or a data-level encryption mechanism. Full disk encryption helps to protect data in the event of physical loss of a disk and therefore its use is appropriate only for removable electronic media storage devices. Media that is part of a data center architecture (for example, hot-swappable drives, bulk tape-backups) is considered non-removable electronic media to which Requirement 3.5.1 applies. Disk or partition encryption implementations must also meet all other PCI DSS encryption and key-management requirements. For issuers and companies that support issuing services: This requirement does not apply to PANs being accessed for real-time transaction processing. However, it does apply to PANs stored for other purposes. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose of 3.5.1.2:**Disk-level and partition-level encryption typically encrypts the entire disk or partition using the same key, with all data automatically decrypted when the system runs or when an authorized user requests it. For this reason, disk-level encryption is not appropriate to protect stored PAN on computers, laptops, servers, storage arrays, or any other system that provides transparent decryption upon user authentication.
**Guidance - Further Information of 3.5.1.2:**Where available, following vendors' hardening and industry best practice guidelines can assist in securing PAN on these devices.

---
**Control objectives:**3.5
**Sub-requirement:**3.5.1.3 *(Tag: encryption access control, key separation, authentication control)*
**Defined Approach Requirements of 3.5.1.3:**If disk-level or partition-level encryption is used (rather than file-, column-, or field-level database encryption) to render PAN unreadable, it is managed as follows:
• Logical access is managed separately and independently of native operating system authentication and access control mechanisms.
• Decryption keys are not associated with user accounts.
• Authentication factors (passwords, passphrases, or cryptographic keys) that allow access to unencrypted data are stored securely.
**Defined Approach Testing Procedures of 3.5.1.3:**
- "3.5.1.3.a": If disk-level or partition-level encryption is used to render PAN unreadable, examine the system configuration and observe the authentication process to verify that logical access is implemented in accordance with all elements specified in this requirement.
- "3.5.1.3.b": Examine files containing authentication factors (passwords, passphrases, or cryptographic keys) and interview personnel to verify that authentication factors that allow access to unencrypted data are stored securely and are independent from the native operating system's authentication and access control methods. 3.6 Cryptographic keys used to protect stored account data are secured.
**Customized Approach Objective of 3.5.1.3:**Disk encryption implementations are configured to require independent authentication and logical access controls for decryption.
**Applicability Notes of 3.5.1.3:**Disk or partition encryption implementations must also meet all other PCI DSS encryption and key-management requirements.
**Guidance - Purpose of 3.5.1.3:**Disk-level encryption typically encrypts the entire disk or partition using the same key, with all data automatically decrypted when the system runs or when an authorized user requests it. Many disk-encryption solutions intercept operating system read/write operations and perform the appropriate cryptographic transformations without any special action by the user other than supplying a password or passphrase at system start-up or at the beginning of a session. This provides no protection from a malicious individual that has already managed to gain access to a valid user account.
**Guidance - Good Practice of 3.5.1.3:**Full disk encryption helps to protect data in the event of physical loss of a disk and therefore its use is best limited only to removable electronic media storage devices. 3.6 Cryptographic keys used to protect stored account data are secured. 3.6 Cryptographic keys used to protect stored account data are secured.