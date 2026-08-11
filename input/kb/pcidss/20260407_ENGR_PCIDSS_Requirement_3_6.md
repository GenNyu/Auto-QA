### A. Tài liệu gốc của Requirement 3

### B. Summary Overview của Control Objective 3.6
Tài liệu này mô tả chi tiết **Control Objective 3.6** của **Requirement 3 **trong **PCI-DSS v4.0.1**, tập trung vào việc bảo vệ khóa mật mã dùng để bảo vệ dữ liệu tài khoản lưu trữ.
Mục tiêu chính là đảm bảo các khóa mật mã được bảo vệ khỏi việc lộ hoặc bị lạm dụng thông qua kiểm soát truy cập, lưu trữ an toàn và phân tách hợp lý.
Gồm 1 sub-requirement chính:
- 3.6.1: Bảo vệ khóa mật mã
Áp dụng cho tất cả các khóa mật mã dùng để bảo vệ dữ liệu tài khoản, bao gồm cả data-encrypting keys và key-encrypting keys.

### C. Key Points của Control Objective 3.6
- **Phạm vi áp dụng:**Tất cả khóa mật mã bảo vệ dữ liệu tài khoản
- **Trách nhiệm:**Tài liệu hóa, phân rõ vai trò key custodian và kiểm soát truy cập
- **Kiểm soát truy cập:**Giới hạn quyền truy cập khóa cho số ít nhân sự cần thiết
- **Phân tách khóa:** Key-encrypting keys phải tách biệt với data-encrypting keys
- **Bảo vệ khóa:** Lưu trữ khóa trong môi trường an toàn (HSM, mã hóa, key components)
- **Giảm thiểu rủi ro:**Lưu khóa ở số lượng location tối thiểu

### D. Deep Summary của Control Objective 3.6
**Bối cảnh:**
Khóa mật mã là yếu tố quyết định để giải mã dữ liệu. Nếu khóa bị lộ, toàn bộ cơ chế bảo vệ dữ liệu sẽ bị vô hiệu hóa.
**Nội dung cốt lõi:**
- Xây dựng quy trình bảo vệ khóa khỏi disclosure và misuse
- Giới hạn số lượng người có quyền truy cập khóa (key custodian)
- Lưu trữ khóa an toàn: mã hóa, HSM hoặc chia thành key components
- Đảm bảo key-encrypting keys mạnh và tách biệt với data-encrypting keys
- Giảm số lượng location lưu trữ khóa để kiểm soát tốt hơn
**Dữ liệu đáng chú ý:**
- Áp dụng cho cả data-encrypting keys và key-encrypting keys
- Khuyến nghị sử dụng hệ thống quản lý khóa tập trung (KMS/HSM)
**Rủi ro / Lưu ý:**
- Lộ khóa → dữ liệu PAN có thể bị giải mã hoàn toàn
- Lưu khóa cùng vị trí với dữ liệu → tăng rủi ro compromise
- Quá nhiều người có quyền truy cập → khó kiểm soát và audit
- Lưu khóa ở nhiều location → tăng khả năng bị lộ

### E. Structured Output của Requirement 3
**Control objectives:**3.6
**Sub-requirement:**3.6.1 *(Tag: key protection, key security, key storage, key segregation, least privilege)*
**Defined Approach Requirements of 3.6.1:**Procedures are defined and implemented to protect cryptographic keys used to protect stored account data against disclosure and misuse that include:
• Access to keys is restricted to the fewest number of custodians necessary.
• Key-encrypting keys are at least as strong as the data-encrypting keys they protect.
• Key-encrypting keys are stored separately from data-encrypting keys.
• Keys are stored securely in the fewest possible locations and forms.
**Defined Approach Testing Procedures of 3.6.1:**Examine documented key-management policies and procedures to verify that processes to protect cryptographic keys used to protect stored account data against disclosure and misuse are defined to include all elements specified in this requirement.
**Customized Approach Objective of 3.6.1:**Processes that protect cryptographic keys used to protect stored account data against disclosure and misuse are defined and implemented.
**Applicability Notes of 3.6.1:**This requirement applies to keys used to protect stored account data and to key-encrypting keys used to protect data-encrypting keys. The requirement to protect keys used to protect stored account data from disclosure and misuse applies to both data-encrypting keys and key- encrypting keys. Because one key-encrypting key may grant access to many data-encrypting keys, the key-encrypting keys require strong protection measures.
**Guidance - Purpose of 3.6.1:**Cryptographic keys must be strongly protected because those who obtain access will be able to decrypt data.
**Guidance - Good Practice of 3.6.1:**Having a centralized key management system based on industry standards is recommended for managing cryptographic keys.
**Guidance - Further Information of 3.6.1:**The entity's key management procedures will benefit through alignment with industry requirements, Sources for information on cryptographic key management life cycles include:
• ISO 11568-1 Banking -Key management (retail) -Part 1 : Principles (specifically Chapter 10 and the referenced Parts 2 & 4)
• NIST SP 800-57 Part 1 Revision 5- Recommendation for Key Management, Part 1: General .

---
**Control objectives:**3.6
**Sub-requirement:**3.6.1.1 *(Tag: cryptographic architecture, KMS, HSM, key inventory)*
**Defined Approach Requirements of 3.6.1.1:**Additional requirement for service providers only: A documented description of the cryptographic architecture is maintained that includes:
• Details of all algorithms, protocols, and keys used for the protection of stored account data, including key strength and expiry date.
• Preventing the use of the same cryptographic keys in production and test environments. This bullet is a best practice until its effective date; refer to Applicability Notes below for details.
• Description of the key usage for each key.
• Inventory of any hardware security modules (HSMs), key management systems (KMS), and other secure cryptographic devices (SCDs) used for key management, including type and location of devices, to support meeting Requirement 12.3.4.
**Defined Approach Testing Procedures of 3.6.1.1:**Additional testing procedure for service provider assessments only: Interview responsible personnel and examine documentation to verify that a document exists to describe the cryptographic architecture that includes all elements specified in this requirement.
**Customized Approach Objective of 3.6.1.1:**Accurate details of the cryptographic architecture are maintained and available.
**Applicability Notes of 3.6.1.1:**This requirement applies only when the entity being assessed is a service provider. In cloud HSM implementations, responsibility for the cryptographic architecture according to this Requirement will be shared between the cloud provider and the cloud customer. The bullet above (for including, in the cryptographic architecture, that the use of the same cryptographic keys in production and test is prevented) is a best practice until 31 March 2025, after which it will be required as part of Requirement 3.6.1.1 and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose of 3.6.1.1:**Maintaining current documentation of the cryptographic architecture enables an entity to understand the algorithms, protocols, and cryptographic keys used to protect stored account data, as well as the devices that generate, use, and protect the keys. This allows an entity to keep pace with evolving threats to its architecture and plan for updates as the assurance level provided by different algorithms and key strengths changes. Maintaining such documentation also allows an entity to detect lost or missing keys or key- management devices and identify unauthorized additions to its cryptographic architecture. The use of the same cryptographic keys in both production and test environments introduces a risk of exposing the key if the test environment is not at the same security level as the production environment.
**Guidance - Good Practice of 3.6.1.1:**Having an automated reporting mechanism can assist with maintenance of the cryptographic attributes. Accurate details of the cryptographic architecture are maintained and available.

---
**Control objectives:**3.6
**Sub-requirement:**3.6.1.2 *(Tag: key storage security, HSM, key encryption keys, split key storage)*
**Defined Approach Requirements of 3.6.1.2:**Secret and private keys used to protect stored account data are stored in one (or more) of the following forms at all times:
• Encrypted with a key-encrypting key that is at least as strong as the data-encrypting key, and that is stored separately from the data- encrypting key.
• Within a secure cryptographic device (SCD), such as a hardware security module (HSM) or PTS-approved point-of-interaction device.
• As at least two full-length key components or key shares, in accordance with an industry- accepted method.
**Defined Approach Testing Procedures of 3.6.1.2:**
- "3.6.1.2.a": Examine documented procedures to verify it is defined that cryptographic keys used to encrypt/decrypt stored account data must exist only in one (or more) of the forms specified in this requirement.
- "3.6.1.2.b": Examine system configurations and key storage locations to verify that cryptographic keys used to encrypt/decrypt stored account data exist in one (or more) of the forms specified in this requirement.
- "3.6.1.2.c": Wherever key-encrypting keys are used, examine system configurations and key storage locations to verify:
• Key-encrypting keys are at least as strong as the data-encrypting keys they protect.
• Key-encrypting keys are stored separately from data-encrypting keys.
**Customized Approach Objective of 3.6.1.2:**Secret and private keys are stored in a secure form that prevents unauthorized retrieval or access.
**Applicability Notes of 3.6.1.2:**It is not required that public keys be stored in one of these forms. Cryptographic keys stored as part of a key management system (KMS) that employs SCDs are acceptable. A cryptographic key that is split into two parts does not meet this requirement. Secret or private keys stored as key components or key shares must be generated via one of the following:
• Using an approved random number generator and within an SCD, OR
• According to ISO 19592 or equivalent industry standard for generation of secret key shares.
**Guidance - Purpose of 3.6.1.2:**Storing cryptographic keys securely prevents unauthorized or unnecessary access that could result in the exposure of stored account data. Storing keys separately means they are stored such that if the location of one key is compromised, the second key is not also compromised.
**Guidance - Good Practice of 3.6.1.2:**Where data-encrypting keys are stored in an HSM, the HSM interaction channel should be protected to prevent interception of encryption or decryption operations.

---
**Control objectives:**3.6
**Sub-requirement:**3.6.1.3 *(Tag: key custodian control, restricted access, key governance)*
**Defined Approach Requirements of 3.6.1.3:**Access to cleartext cryptographic key components is restricted to the fewest number of custodians necessary.
**Defined Approach Testing Procedures of 3.6.1.3:**Examine user access lists to verify that access to cleartext cryptographic key components is restricted to the fewest number of custodians necessary.
**Customized Approach Objective of 3.6.1.3:**Access to cleartext cryptographic key components is restricted to necessary personnel.
**Guidance - Purpose of 3.6.1.3:**Restricting the number of people who have access to cleartext cryptographic key components reduces the risk of stored account data being retrieved or rendered visible by unauthorized parties.
**Guidance - Good Practice of 3.6.1.3:**Only personnel with defined key custodian responsibilities (creating, altering, rotating, distributing, or otherwise maintaining encryption keys) should be granted access to key components. Ideally this will be a very small number of people.

---
**Control objectives:**3.6
**Sub-requirement:**3.6.1.4 *(Tag: key location minimization, key exposure reduction)*
**Defined Approach Requirements of 3.6.1.4:**Cryptographic keys are stored possible locations.
**Defined Approach Testing Procedures of 3.6.1.4:**Examine key storage locations and observe processes to verify that keys are stored in the fewest possible locations.
**Customized Approach Objective of 3.6.1.4:**Access to cleartext cryptographic key components is restricted to necessary personnel.
**Guidance - Purpose of 3.6.1.4:**Storing any cryptographic keys in the fewest locations helps an organization track and monitor all key locations and minimizes the potential for keys to be exposed to unauthorized parties.
**Guidance - Good Practice of 3.6.1.4:**Only personnel with defined key custodian responsibilities (creating, altering, rotating, distributing, or otherwise maintaining encryption keys) should be granted access to key components. Ideally this will be a very small number of people.