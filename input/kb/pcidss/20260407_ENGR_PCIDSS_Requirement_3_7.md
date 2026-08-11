### A. Tài liệu gốc của Requirement 3

### B. Summary Overview của Control Objective 3.7
Tài liệu này mô tả chi tiết **Control Objective 3.7 **của **Requirement 3** trong** PCI-DSS v4.0.1**, tập trung vào việc quản lý vòng đời khóa mật mã dùng để bảo vệ dữ liệu tài khoản.
Mục tiêu chính là đảm bảo khóa mật mã được quản lý xuyên suốt vòng đời từ tạo, phân phối, lưu trữ, sử dụng đến thay thế và hủy bỏ một cách an toàn.
Gồm 9 sub-requirement chính:
- 3.7.1: Tạo khóa mật mã
- 3.7.2: Phân phối khóa an toàn
- 3.7.3: Lưu trữ khóa an toàn
- 3.7.4: Thay đổi khóa theo cryptoperiod
- 3.7.5: Thu hồi / thay thế / hủy khóa
- 3.7.6: Split knowledge & dual control
- 3.7.7: Ngăn thay thế khóa trái phép
- 3.7.8: Cam kết trách nhiệm key custodian
- 3.7.9: Hướng dẫn quản lý khóa cho khách hàng (service provider)
Áp dụng cho toàn bộ quy trình quản lý khóa mật mã liên quan đến bảo vệ dữ liệu tài khoản, bao gồm cả môi trường nội bộ và service provider (nếu có)

### C. Key Points của Control Objective 3.7
- **Phạm vi áp dụng:**Toàn bộ vòng đời khóa mật mã
- **Trách nhiệm:** Tài liệu hóa, phân rõ vai trò key custodian và trách nhiệm liên quan
- **Quản lý vòng đời:**Bao gồm tạo, phân phối, lưu trữ, sử dụng, rotation và hủy khóa
- **Kiểm soát truy cập:**Áp dụng split knowledge và dual control khi xử lý khóa cleartext
- **Kiểm soát bảo mật:**Ngăn thay thế khóa trái phép và bảo vệ khóa khỏi lộ
- **Quản lý chu kỳ:**Định nghĩa cryptoperiod và thực hiện rotation đúng hạn
- **Service provider:** Phải cung cấp hướng dẫn quản lý khóa cho khách hàng khi chia sẻ khóa

### D. Deep Summary của Control Objective 3.7
**Bối cảnh:**
Khóa mật mã nếu không được quản lý đúng vòng đời sẽ dẫn đến việc bị lộ, sử dụng sai mục đích hoặc tiếp tục sử dụng sau khi không còn an toàn.
**Nội dung cốt lõi:**
- Tạo khóa bằng strong cryptography
- Phân phối và lưu trữ khóa một cách an toàn
- Định nghĩa cryptoperiod và thay đổi khóa đúng hạn
- Thu hồi, thay thế hoặc hủy khóa khi hết hạn hoặc bị compromise
- Áp dụng split knowledge và dual control cho thao tác manual
- Ngăn chặn việc thay thế khóa trái phép
- Đảm bảo key custodian hiểu và cam kết trách nhiệm
**Dữ liệu đáng chú ý:**
- Cryptoperiod phụ thuộc vào thuật toán, độ dài khóa và mức độ nhạy cảm dữ liệu
- Key management áp dụng xuyên suốt từ tạo → hủy khóa
**Rủi ro / Lưu ý:**
- Không rotate khóa → tăng nguy cơ bị brute force hoặc lộ khóa
- Không thu hồi khóa bị compromise → dữ liệu có thể bị giải mã
- Thiếu dual control → một cá nhân có thể kiểm soát toàn bộ khóa
- Không kiểm soát thay thế khóa → attacker có thể chèn khóa giả

### E. Structured Output của Requirement 3
**Control objectives:**3.7
**Sub-requirement:**3.7.1 (Tag: key generation, strong cryptography, entropy)
**Defined Approach Requirements of 3.7.1:**Key-management policies and procedures are implemented to include generation of strong cryptographic keys used to protect stored account data.
**Defined Approach Testing Procedures of 3.7.1:**
- "3.7.1.a": Examine the documented key-management policies and procedures for keys used for protection of stored account data to verify that they define generation of strong cryptographic keys.
- "3.7.1.b": Observe the method for generating keys to verify that strong keys are generated.
**Customized Approach Objective of 3.7.1:**Strong cryptographic keys are generated.
**Guidance - Purpose of 3.7.1:**Use of strong cryptographic keys significantly increases the level of security of encrypted account data.
**Guidance - Further Information of 3.7.1:**See the sources referenced at Cryptographic Key Generation in Appendix G.

---
**Control objectives:**3.7
**Sub-requirement:**3.7.2 *(Tag: key distribution, secure transmission, key exchange)*
**Defined Approach Requirements of 3.7.2:**Key-management policies and procedures are implemented to include secure distribution of cryptographic keys used to protect stored account data.
**Defined Approach Testing Procedures of 3.7.2:**
- "3.7.2.a": Examine the documented key-management policies and procedures for keys used for protection of stored account data to verify that they define secure distribution of cryptographic keys.
- "3.7.2.b": Observe the method for distributing keys to verify that keys are distributed securely.
**Customized Approach Objective of 3.7.2:**Cryptographic keys are secured during distribution.
**Guidance - Purpose of 3.7.2:**Secure distribution or conveyance of secret or private cryptographic keys means that keys are distributed only to authorized custodians, as identified in Requirement 3.6.1.2, and are never distributed insecurely.

---
**Control objectives:**3.7
**Sub-requirement:**3.7.3 *(Tag: key storage, HSM, secure key vault)*
**Defined Approach Requirements of 3.7.3:**Key-management policies and procedures are implemented to include secure storage of cryptographic keys used to protect stored account data.
**Defined Approach Testing Procedures of 3.7.3:**
- "3.7.3.a": Examine the documented key-management policies and procedures for keys used for protection of stored account data to verify that they define secure storage of cryptographic keys.
- "3.7.3.b": Observe the method for storing keys to verify that keys are stored securely.
**Customized Approach Objective of 3.7.3:**Cryptographic keys are secured when stored.
**Guidance - Purpose of 3.7.3:**Storing keys without proper protection could provide access to attackers, resulting in the decryption and exposure of account data.
**Guidance - Good Practice of 3.7.3:**Data encryption keys can be protected by encrypting them with a key-encrypting key. Keys can be stored in a Hardware Security Module (HSM). Secret or private keys that can decrypt data should never be present in source code.

---
**Control objectives:**3.7
**Sub-requirement:**3.7.4* (Tag: key rotation, cryptoperiod, key expiry)*
**Defined Approach Requirements of 3.7.4:**Key management policies and procedures are implemented for cryptographic key changes for keys that have reached the end of their cryptoperiod, as defined by the associated application vendor or key owner, and based on industry best practices and guidelines, including the following:
• A defined cryptoperiod for each key type in use.
• A process for key changes at the end of the defined cryptoperiod.
**Defined Approach Testing Procedures of 3.7.4:**
- "3.7.4.a": Examine the documented key-management policies and procedures for keys used for protection of stored account data to verify that they define changes to cryptographic keys that have reached the end of their cryptoperiod and include all elements specified in this requirement.
- "3.7.4.b": Interview personnel, examine documentation, and observe key storage locations to verify that keys are changed at the end of the defined cryptoperiod(s).
**Customized Approach Objective of 3.7.4:**Cryptographic keys are not used beyond their defined cryptoperiod.
**Guidance - Purpose of 3.7.4:**Changing encryption keys when they reach the end of their cryptoperiod is imperative to minimize the risk of someone obtaining the encryption keys and using them to decrypt data.
**Guidance - Definitions of 3.7.4:**A cryptoperiod is the time span during which a cryptographic key can be used for its defined purpose. Cryptoperiods are often defined in terms of the period for which the key is active and/or the amount of cipher- text that has been produced by the key. Considerations for defining the cryptoperiod include, but are not limited to, the strength of the underlying algorithm, size or length of the key, risk of key compromise, and the sensitivity of the data being encrypted.
**Guidance - Further Information of 3.7.4:**NIST SP 800-57 Part 1, Revision 5, Section 5.3 Cryptoperiods - provides guidance for establishing the time span during which a specific key is authorized for use by legitimate entities, or the keys for a given system will remain in effect. See Table 1 of SP 800-57 Part 1 for suggested cryptoperiods for different key types.

---
**Control objectives:**3.7
**Sub-requirement:**3.7.5 *(Tag: key retirement, key revocation, compromised key handling)*
**Defined Approach Requirements of 3.7.5:**Key management policies procedures are implemented to include the retirement, replacement, or destruction of keys used to protect stored account data, as deemed necessary when:
• The key has reached the end of its defined cryptoperiod.
• The integrity of the key has been weakened, including when personnel with knowledge of a cleartext key component leaves the company, or the role for which the key component was known.
• The key is suspected of or known to be compromised. Retired or replaced keys are not used for encryption operations.
**Defined Approach Testing Procedures of 3.7.5:**
- "3.7.5.a": Examine the documented key-management policies and procedures for keys used for protection of stored account data and verify that they define retirement, replacement, or destruction of keys in accordance with all elements specified in this requirement.
- "3.7.5.b": Interview personnel to verify that processes are implemented in accordance with all elements specified in this requirement.
**Customized Approach Objective of 3.7.5:**Keys are removed from active use when it is suspected or known that the integrity of the key is weakened.
**Applicability Notes of 3.7.5:**If retired or replaced cryptographic keys need to be retained, these keys must be securely archived (for
**Guidance - Purpose of 3.7.5:**Keys that are no longer required, keys with weakened integrity, and keys that are known or suspected to be compromised, should be archived, revoked, and/or destroyed to ensure that the keys can no longer be used. If such keys need to be kept (for example, to support archived encrypted data), they should be strongly protected.
**Guidance - Good Practice of 3.7.5:**Archived cryptographic keys should be used only for decryption/verification purposes. The encryption solution should provide for and facilitate a process to replace keys that are due for replacement or that are known to be, or suspected of being, compromised. In addition, any keys that are known to be, or suspected of being, compromised should be managed in accordance with the entity's incident response plan per Requirement 12.10.1.
**Guidance - Further Information of 3.7.5:**Industry best practices for archiving retired keys are outlined in NIST SP 800-57 Part 1, Revision 5, Section 8.3.1 , and includes maintaining the archive with a trusted third party and storing archived key information separately from operational data.
—
**Control objectives:**3.7
**Sub-requirement:**3.7.6* (Tag: split knowledge, dual control, key ceremony)*
**Defined Approach Requirements of 3.7.6:**Where manual cleartext cryptographic key- management operations are performed by personnel, key-management policies and procedures are implemented, including managing these operations using split knowledge and dual control.
**Defined Approach Testing Procedures of 3.7.6:**
- "3.7.6.a": Examine the documented key-management policies and procedures for keys used for protection of stored account data and verify that they define using split knowledge and dual control.
- "3.7.6.b": Interview personnel and/or observe processes to verify that manual cleartext keys are managed with split knowledge and dual control.
**Customized Approach Objective of 3.7.6:**Cleartext secret or private keys cannot be known by anyone. Operations involving cleartext keys cannot be carried out by a single person.
**Applicability Notes of 3.7.6:**This control is applicable for manual key- management operations. A cryptographic key that is simply split into two parts does not meet this requirement. Secret or private keys stored as key components or key shares must be generated via one of the following:
• Using an approved random number generator and within a secure cryptographic device (SCD), such as a hardware security module (HSM) or PTS-approved point-of-interaction device, OR
• According to ISO 19592 or equivalent industry standard for generation of secret key shares.
**Guidance - Purpose of 3.7.6:**Split knowledge and dual control of keys are used to eliminate the possibility of a single person having access to the whole key and therefore being able to gain unauthorized access to the data.
**Guidance - Good Practice of 3.7.6:**Where key components or key shares are used, procedures should ensure that no single custodian ever has access to sufficient key components or shares to reconstruct the cryptographic key. For example, in an m-of-n scheme (for example, Shamir), where only two of any three components are required to reconstruct the cryptographic key, a custodian must not have current or prior knowledge of more than one component. If a custodian was previously assigned component A, which was then reassigned, the custodian should not then be assigned component B or C, as this would give the custodian knowledge of two components and the ability to recreate the key.
**Guidance - Definitions of 3.7.6:**Split knowledge is a method in which two or more people separately have key components, where each person knows only their own key component, and the individual key components convey no knowledge of other components or of the original cryptographic key. Dual control requires two or more people to authenticate the use of a cryptographic key or perform a key-management function. No single person can access or use the authentication factor (for example, the password, PIN, or key) of another.
**Guidance - Examples of 3.7.6:**Key-management operations that might be performed manually include, but are not limited to, key generation, transmission, loading, storage, and destruction.
**Guidance - Further Information of 3.7.6:**Industry standards for managing key components include:
• NIST SP 800-57 Part 2, Revision 1 -- Recommendation for Key Management: Part 2 - Best Practices for Key Management Organizations [4.6 Keying Material Distribution]
• ISO 11568-2 Banking -Key management (retail) -Part 2 : Symmetric ciphers, their key management and life cycle [4.7.2.3 Key components and 4.9.3 Key components]
• European Payments Council EPC342-08 Guidelines on Cryptographic Algorithms Usage and Key Management [especially 4.1.4 Key installation].

---
**Control objectives:**3.7
**Sub-requirement:**3.7.7 *(Tag: key integrity, anti-key substitution, tamper protection)*
**Defined Approach Requirements of 3.7.7:**Key management policies and procedures are implemented to include the prevention of unauthorized substitution of cryptographic keys.
**Defined Approach Testing Procedures of 3.7.7:**
- "3.7.7.a": Examine the documented key-management policies and procedures for keys used for protection of stored account data and verify that they define prevention of unauthorized substitution of cryptographic keys.
- "3.7.7.b": Interview personnel and/or observe processes to verify that unauthorized substitution of keys is prevented.
**Customized Approach Objective of 3.7.7:**Cryptographic keys cannot be substituted by unauthorized personnel.
**Guidance - Purpose of 3.7.7:**If an attacker is able to substitute an entity's key with a key the attacker knows, the attacker will be able to decrypt all data encrypted with that key.
**Guidance - Good Practice of 3.7.7:**The encryption solution should not allow for or accept substitution of keys from unauthorized sources or unexpected processes. Controls should include ensuring that individuals with access to key components or shares do not have access to other components or shares that form the necessary threshold to derive the key.

---
**Control objectives:**3.7
**Sub-requirement:**3.7.8 *(Tag: key custodian accountability, acknowledgment, governance)*
**Defined Approach Requirements of 3.7.8:**Key management policies and procedures are implemented to include that cryptographic key custodians formally acknowledge (in writing or electronically) that they understand and accept their key-custodian responsibilities.
**Defined Approach Testing Procedures of 3.7.8:**
- "3.7.8.a": Examine the documented key-management policies and procedures for keys used for protection of stored account data and verify that they define acknowledgments for key custodians in accordance with all elements specified in this requirement.
- "3.7.8.b": Examine documentation or other evidence showing that key custodians have provided acknowledgments in accordance with all elements specified in this requirement.
**Guidance - Purpose of 3.7.8:**This process will help ensure individuals that act as key custodians commit to the key-custodian role and understand and accept the responsibilities. An annual reaffirmation can help remind key custodians of their responsibilities.
**Guidance - Further Information of 3.7.8:**Industry guidance for key custodians and their roles and responsibilities includes:
• NIST SP 800-130 A Framework for Designing Cryptographic Key Management Systems [5. Roles and Responsibilities (especially) for Key Custodians]
• ISO 11568-1 Banking -- Key management (retail) -- Part 1 : Principles [5 Principles of key management (especially b)]

---
**Control objectives:**3.7
**Sub-requirement:**3.7.9* (Tag: customer key guidance, shared key management, TPSP responsibility)*
**Defined Approach Requirements of 3.7.9:**Additional requirement for service providers only: Where a service provider shares cryptographic keys with its customers for transmission or storage of account data, guidance on secure transmission, storage and updating of such keys is documented and distributed to the service provider's customers. Customized Approach Objective Customers are provided with appropriate key management guidance whenever they receive shared cryptographic keys.
**Defined Approach Testing Procedures of 3.7.9:**Additional testing procedure for service provider assessments only: If the service provider shares cryptographic keys with its customers for transmission or storage of account data, examine the documentation that the service provider provides to its customers to verify it includes guidance on how to securely transmit, store, and update customers' keys in accordance with all elements specified in Requirements 3.7.1 through 3.7.8 above.
**Customized Approach Objective of 3.7.9:**Customers are provided with appropriate key management guidance whenever they receive shared cryptographic keys.
**Applicability Notes of 3.7.9:**This requirement applies only when the entity being assessed is a service provider.
**Guidance - Purpose of 3.7.9:**Providing guidance to customers on how to securely transmit, store, and update cryptographic keys can help prevent keys from being mismanaged or disclosed to unauthorized entities.
**Guidance - Further Information of 3.7.9:**Numerous industry standards for key management are cited above in the Guidance for Requirements 3.7.1- 3.7.8.