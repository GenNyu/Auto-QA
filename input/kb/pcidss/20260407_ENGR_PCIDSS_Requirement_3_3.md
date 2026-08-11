### A. Tài liệu gốc của Requirement 3

### B. Summary Overview của Control Objective 3.3
Tài liệu này mô tả chi tiết **Control Objective 3.3 **của **Requirement 3** trong **PCI-DSS v4.0.1**, tập trung vào việc không lưu trữ dữ liệu xác thực nhạy cảm (SAD) sau khi hoàn tất quá trình ủy quyền.
Mục tiêu chính là đảm bảo SAD không được lưu trữ dưới bất kỳ hình thức nào sau authorization, và nếu có xử lý trước đó thì phải được xóa hoặc làm không thể khôi phục ngay lập tức.
Gồm 3 sub-requirement chính:
- 3.3.1: Không lưu SAD sau authorization
- 3.3.2: Mã hóa SAD trước authorization (nếu lưu tạm)
- 3.3.3: Yêu cầu bổ sung cho Issuer lưu SAD
Áp dụng cho tất cả hệ thống xử lý, truyền hoặc lưu trữ dữ liệu xác thực nhạy cảm (SAD), bao gồm cả bộ nhớ, log, database và các nguồn dữ liệu liên quan.

### C. Key Points của Control Objective 3.3
- **Phạm vi áp dụng:**Toàn bộ hệ thống có xử lý SAD (memory, log, DB, file, cloud…)
- **Trách nhiệm:**Tài liệu hóa, kiểm soát và đảm bảo không lưu SAD sau authorization
- **Kiểm soát lưu trữ: T**uyệt đối không lưu SAD sau authorization, kể cả khi đã mã hóa
- **Xử lý dữ liệu:**SAD phải được xóa hoặc làm không thể khôi phục ngay khi hoàn tất authorization
- **Thành phần SAD:**Bao gồm track data, CVV, PIN, PIN block
- **Lưu trữ tạm:**Nếu lưu trước authorization phải mã hóa mạnh (strong cryptography)
- **Ngoại lệ:**Chỉ áp dụng cho Issuer nếu có business justification hợp lệ

### D. Deep Summary của Control Objective 3.3
**Bối cảnh:** SAD là loại dữ liệu có giá trị cao đối với kẻ tấn công, có thể bị lợi dụng để tạo thẻ giả và thực hiện giao dịch gian lận. Việc lưu trữ SAD sau authorization làm tăng rủi ro nghiêm trọng.
**Nội dung cốt lõi:**
- Cấm hoàn toàn lưu SAD sau khi hoàn tất authorization
- SAD phải được xóa hoặc làm không thể khôi phục ngay sau khi xử lý
- Bao gồm tất cả loại SAD: full track, CVV, PIN, PIN block
- Nếu lưu trước authorization: phải mã hóa bằng strong cryptography
- Kiểm soát cả memory (RAM), log, file, database, dump
- Trường hợp Issuer: chỉ được lưu khi có business justification và phải bảo vệ chặt chẽ
**Dữ liệu đáng chú ý:**
- Authorization hoàn tất khi nhận response (approve/decline)
- SAD có thể tồn tại tạm trong non-persistent memory nhưng phải xóa ngay sau khi dùng
**Rủi ro / Lưu ý:**
- Lưu SAD sau authorization → vi phạm nghiêm trọng PCI DSS
- Mã hóa không làm hợp lệ việc lưu SAD sau authorization
- Bỏ sót log/debug/dump → rủi ro rò rỉ dữ liệu
- Lưu trong persistent storage (disk, DB) → không được phép ngay cả khi mã hóa

### E. Structured Output của Control Objective 3.3
**Control objectives:**3.3
**Sub-requirement:**3.3.1 *(Tag: SAD prohibition, post-authorization data handling, secure deletion, volatile memory control)*
**Defined Approach Requirements of 3.3.1:**SAD is not stored after authorization, even if encrypted. All sensitive authentication data received is rendered unrecoverable upon completion of the authorization process.
**Defined Approach Testing Procedures of 3.3.1:**
- "3.3.1.a": If SAD is received, examine documented policies, procedures, and system configurations to verify the data is not stored after authorization.
- "3.3.1.b": If SAD is received, examine the documented procedures and observe the secure data deletion processes to verify the data is rendered unrecoverable upon completion of the authorization process.
**Customized Approach Objective of 3.3.1:**This requirement is not eligible for the customized approach.
**Applicability Notes of 3.3.1:**Issuers and companies that support issuing services, where there is a legitimate and documented business need to store SAD, are not required to meet this requirement. A legitimate business need is one that is necessary for the performance of the function being provided by or for the issuer. Refer to Requirement 3.3.3 for additional requirements specifically for these entities. Sensitive authentication data includes the data cited in Requirements 3.3.1.1 through 3.3.1.3.
**Guidance - Purpose of 3.3.1:**SAD is very valuable to malicious individuals as it allows them to generate counterfeit payment cards and create fraudulent transactions. Therefore, the storage of SAD upon completion of the authorization process is prohibited.
**Guidance - Good Practice of 3.3.1:**It may be acceptable for an entity to store SAD in non- persistent memory for a short time after authorization is complete, if following conditions are met:
• There is a legitimate business need to access SAD in memory after authorization is complete.
• SAD is only ever stored in non-persistent memory (for example, RAM, volatile memory).
• Controls are in place to ensure that memory maintains a non-persistent state.
• SAD is removed as soon as the business purpose is complete. It is not permissible to store SAD in persistent memory.
**Guidance - Definitions of 3.3.1:**The authorization process completes when a merchant receives a transaction response (for example, an approval or decline). Refer to Appendix G for the definition of 'authorization.'

---
**Control objectives:**3.3
**Sub-requirement:**3.3.1.1 *(Tag: track data, magnetic stripe, chip data, card cloning risk)*
**Defined Approach Requirements of 3.3.1.1:**The full contents of any track are not stored upon completion of the authorization process.
**Defined Approach Testing Procedures of 3.3.1.1:**Examine data sources to verify that the full contents of any track are not stored upon completion of the authorization process.
**Customized Approach Objective of 3.3.1.1:**This requirement is not eligible for the customized approach.
**Applicability Notes of 3.3.1.1:**In the normal course of business, the following data elements from the track may need to be retained:
• Cardholder name.
• Primary account number (PAN).
• Expiration date.
• Service code. To minimize risk, store securely only these data elements as needed for business.
**Guidance - Purpose of 3.3.1.1:**If full contents of any track (from the magnetic stripe on the back of a card if present, equivalent data contained on a chip, or elsewhere) is stored, malicious individuals who obtain that data can use it to reproduce payment cards and complete fraudulent transactions.
**Guidance - Definitions of 3.3.1.1:**Full track data is alternatively called full track, track, track 1, track 2, and magnetic-stripe data. Each track contains a number of data elements, and this requirement specifies only those that may be retained post-authorization.
**Guidance - Examples of 3.3.1.1:**Data sources to review to ensure that the full contents of any track are not retained upon completion of the authorization process include, but are not limited to:
• Incoming transaction data.
• All logs (for example, transaction, history, debugging, error).
• History files.
• Trace files.
• Database schemas.
• Contents of databases, and on-premise and cloud data stores.
• Any existing memory/crash dump files.

---
**Control objectives:**3.3
**Sub-requirement:**3.3.1.2 *(Tag: CVV protection, card-not-present security, fraud prevention)*
**Defined Approach Requirements of 3.3.1.2:**The card verification code is not stored upon completion of the authorization process.
**Defined Approach Testing Procedures of 3.3.1.2:**Examine data sources, to verify that the card verification code is not stored upon completion of the authorization process.
**Customized Approach Objective of 3.3.1.2:**This requirement is not eligible for the customized approach.
**Applicability Notes of 3.3.1.2:**The card verification code is the three- or four-digit number printed on the front or back of a payment card.
**Guidance - Purpose of 3.3.1.2:**If card verification code data is stolen, malicious individuals can execute fraudulent Internet and mail- order/telephone-order (MO/TO) transactions. Not storing this data reduces the probability of it being compromised.
**Guidance - Examples of 3.3.1.2:**If card verification codes are stored on paper media prior to completion of authorization, a method of erasing or covering the codes should prevent them from being read after authorization is complete. Example methods of rendering the codes unreadable include removing the code with scissors and applying a suitably opaque and un-removable marker over the code. Data sources to review to ensure that the card verification code is not retained upon completion of the authorization process include, but are not limited to:
• Incoming transaction data.
• All logs (for example, transaction, history, debugging, error).
• History files.
• Trace files.
• Database schemas.
• Contents of databases, and on-premise and cloud data stores.
• Any existing memory/crash dump files.

---
**Control objectives:**3.3
**Sub-requirement:**3.3.1.3 *(Tag: PIN security, PIN block protection, ATM/POS fraud prevention)*
**Defined Approach Requirements of 3.3.1.3:**The personal identification number (PIN) and the PIN block are not stored upon completion of the authorization process.
**Defined Approach Testing Procedures of 3.3.1.3:**Examine data sources, to verify that PINs and PIN blocks are not stored upon completion of the authorization process.
**Customized Approach Objective of 3.3.1.3:**This requirement is not eligible for the customized approach.
**Applicability Notes of 3.3.1.3:**PIN blocks are encrypted during the natural course of transaction processes, but even if an entity encrypts the PIN block again, it is still not allowed to be stored after the completion of the authorization process.
**Guidance - Purpose of 3.3.1.3:**PIN and PIN blocks should be known only to the card owner or entity that issued the card. If this data is stolen, malicious individuals can execute fraudulent PIN-based transactions (for example, in-store purchases and ATM withdrawals). Not storing this data reduces the probability of it being compromised.
**Guidance - Examples of 3.3.1.3:**Data sources to review to ensure that PIN and PIN blocks are not retained upon completion of the authorization process include, but are not limited to:
• Incoming transaction data.
• All logs (for example, transaction, history, debugging, error).
• History files.
• Trace files.
• Database schemas.
• Contents of databases, and on-premise and cloud data stores.
• Any existing memory/crash dump files.

---
**Control objectives:**3.3
**Sub-requirement:**3.3.2 *(Tag: SAD encryption, pre-authorization storage, strong cryptography)*
**Defined Approach Requirements of 3.3.2:**SAD that is stored electronically prior to completion of authorization is encrypted using strong cryptography.
**Defined Approach Testing Procedures of 3.3.2:**Examine data stores, system configurations, and/or vendor documentation to verify that all SAD that is stored electronically prior to completion of authorization is encrypted using strong cryptography.
**Customized Approach Objective of 3.3.2:**This requirement is not eligible for the customized approach.
**Applicability Notes of 3.3.2:**Whether SAD is permitted to be stored prior to authorization is determined by the organizations that manage compliance programs (for example, payment brands and acquirers). Contact these organizations for any additional criteria. This requirement applies to all storage of SAD, even if no PAN is present in the environment. Refer to Requirement 3.2.1 for an additional requirement that applies if SAD is stored prior to completion of authorization. Issuers and companies that support issuing services, where there is a legitimate and documented business need to store SAD, are not required to meet this requirement. A legitimate business need is one that is necessary for the performance of the function being provided by or for the issuer. Refer to Requirement 3.3.3 for requirements specifically for these entities. This requirement does not replace how PIN blocks are required to be managed, nor does it mean that a properly encrypted PIN block needs to be encrypted again. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose of 3.3.2:**SAD can be used by malicious individuals to increase the probability of successfully generating counterfeit payment cards and creating fraudulent transactions.
**Guidance - Good Practice of 3.3.2:**Entities should consider encrypting SAD with a different cryptographic key than is used to encrypt PAN. Note that this does not mean that PAN present in SAD (as part of track data) would need to be separately encrypted.
**Guidance - Definitions of 3.3.2:**The authorization process is completed when a merchant receives a transaction response (for example, an approval or decline) . Refer to Appendix G for the definition of 'authorization.'

---
**Control objectives:**3.3
**Sub-requirement:**3.3.3 *(Tag: issuer SAD storage, business justification, encryption requirement)*
**Defined Approach Requirements of 3.3.3:**Additional requirement for issuers and companies that support issuing services and store sensitive authentication data: Any storage of sensitive authentication data is:
• Limited to that which is needed for a legitimate issuing business need and is secured.
• Encrypted using strong cryptography. This bullet is a best practice until its effective date; refer to Applicability Notes below for details.
**Defined Approach Testing Procedures of 3.3.3:**
- "3.3.3.a": Additional testing procedure for issuers and companies that support issuing services and store sensitive authentication data: Examine documented policies and interview personnel to verify there is a documented business justification for the storage of sensitive authentication data.
- "3.3.3.b": Additional testing procedure for issuers and companies that support issuing services and store sensitive authentication data: Examine data stores and system configurations to verify that the sensitive authentication data is stored securely.
**Customized Approach Objective of 3.3.3:**Sensitive authentication data is retained only as required to support issuing functions and is secured from unauthorized access.
**Applicability Notes of 3.3.3:**This requirement applies only to issuers and companies that support issuing services and store sensitive authentication data. Entities that issue payment cards or that perform or support issuing services will often create and control sensitive authentication data as part of the issuing function. It is allowable for companies that perform, facilitate, or support issuing services to store sensitive authentication data ONLY IF they have a legitimate business need to store such data. A legitimate issuing business need is one that is necessary for the performance of the function being provided by or for the issuer. The bullet above (for encrypting stored SAD with strong cryptography) is a best practice until 31 March 2025, after which it will be required as part of Requirement 3.3.3 and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose of 3.3.3:**SAD can be used by malicious individuals to increase the probability of successfully generating counterfeit payment cards and creating fraudulent transactions .
**Guidance - Good Practice of 3.3.3:**Entities should consider encrypting SAD with a different cryptographic key than is used to encrypt PAN. Note that this does not mean that PAN present in SAD (as part of track data) would need to be separately encrypted.