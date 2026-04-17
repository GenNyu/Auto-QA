### A. Tài liệu gốc của Requirement 3

### https://docs.google.com/document/d/18t2FQJDbxwK6VmJ_qoJw3gLzNKC1-pMxB_VG6QT3VYA/edit?usp=sharing

### B. Summary Overview của Control Objective 3.1
Tài liệu này mô tả chi tiết **Control Objective 3.1 **của **Requirement 3 **trong **PCI-DSS v4.0.1**, tập trung vào việc **Quản lý chính sách, quy trình và trách nhiệm liên quan đến bảo vệ dữ liệu tài khoản**
Mục tiêu chính là đảm bảo các chính sách và quy trình được tài liệu hóa, cập nhật, áp dụng thực tế, được phổ biến
Gồm 2 sub-requirement chính:
- 3.1.1: Chính sách & quy trình
- 3.1.2: Vai trò & trách nhiệm
Áp dụng cho toàn bộ hoạt động bảo vệ dữ liệu lưu trữ trong Requirement 3.

### C. Key Points của Control Objective 3.1
- **Phạm vi:**Chính sách bảo vệ dữ liệu tài khoản
- **Trách nhiệm:**Phân rõ vai trò (RACI)
- **Tài liệu:**Phải có, cập nhật và được sử dụng
- **Nhận thức:** Nhân sự phải hiểu và tuân thủ
- **Vận hành:** Repeatable, consistent

### D. Deep Summary của Control Objective 3.1
**Bối cảnh:**Thiếu chính sách và phân công trách nhiệm rõ ràng có thể dẫn đến việc bảo vệ dữ liệu không nhất quán và phát sinh rủi ro bảo mật. 3.1 đóng vai trò là nền tảng quản trị cho toàn bộ Requirement 3.
**Nội dung cốt lõi:**
- **Quản lý quy trình:**Tài liệu hóa, cập nhật và áp dụng các chính sách bảo vệ dữ liệu
- **Vai trò & trách nhiệm: P**hân rõ RACI, đảm bảo mọi hoạt động đều có người chịu trách nhiệm
- **Vận hành hiệu quả:**Các hoạt động phải lặp lại được, nhất quán, có thể kiểm chứng
**Dữ liệu đáng chú ý:**
- Không có mốc thời gian cụ thể
- Mang tính continuous compliance (tuân thủ liên tục)
**Rủi ro / Lưu ý:**
- Không có chính sách rõ ràng → bảo vệ dữ liệu không nhất quán
- Không phân công trách nhiệm → bỏ sót kiểm soát
- Chính sách không được phổ biến → thực thi sai
- Quy trình không cập nhật → không phản ánh thực tế

### E. Structured Output của Control Objective 3.1
**Control objectives:**3.1
**Sub-requirement:**3.1.1 *(Tag: data protection policy, stored account data policy, documentation governance, compliance awareness)*
**Defined Approach Requirements of 3.1.1:**All security policies and operational procedures that are identified in Requirement 3 are:
• Documented.
• Kept up to date.
• In use.
• Known to all affected parties.
**Defined Approach Testing Procedures of 3.1.1:**Examine documentation and interview personnel to verify that security policies and operational procedures identified in Requirement 3 are managed in accordance with all elements specified in this requirement.
**Customized Approach Objective of 3.1.1:**Expectations, controls, and oversight for meeting activities within Requirement 3 are defined and adhered to by affected personnel. All supporting activities are repeatable, consistently applied, and conform to management's intent.
**Guidance - Purpose of 3.1.1:**Requirement 3.1.1 is about effectively managing and maintaining the various policies and procedures specified throughout Requirement 3. While it is important to define the specific policies or procedures called out in Requirement 3, it is equally important to ensure they are properly documented, maintained, and disseminated.
**Guidance - Good Practice of 3.1.1:**It is important to update policies and procedures as needed to address changes in processes, technologies, and business objectives. For this reason, consider updating these documents as soon as possible after a change occurs and not only on a periodic cycle.
**Guidance - Definitions of 3.1.1:**Security policies define the entity's security objectives and principles. Operational procedures describe how to perform activities, and define the controls, methods, and processes that are followed to achieve the desired result in a consistent manner and in accordance with policy objectives.

---
**Control objectives:**3.1
**Sub-requirement:**3.1.2 *(Tag: roles & responsibilities, data ownership, key management responsibility, RACI)*
**Defined Approach Requirements of 3.1.2:**Roles and responsibilities for performing activities in Requirement 3 are documented, assigned, and understood.
**Defined Approach Testing Procedures of 3.1.2:**
- "3.1.2.a": Examine documentation to verify that descriptions of roles and responsibilities performing activities in Requirement 3 are documented and assigned.
- "3.1.2.b": Interview personnel with responsibility performing activities in Requirement 3 to verify roles and responsibilities are assigned as documented and are understood.
**Customized Approach Objective of 3.1.2:**Day-to-day responsibilities for performing all the activities in Requirement 3 are allocated. Personnel are accountable for successful, continuous operation of these requirements.
**Guidance - Purpose of 3.1.2:**If roles and responsibilities are not formally assigned, personnel may not be aware of their day-to-day responsibilities, and critical activities may not occur.
**Guidance - Good Practice of 3.1.2:**Roles and responsibilities may be documented within policies and procedures or maintained within separate documents. As part of communicating roles and responsibilities, entities can consider having personnel acknowledge their acceptance and understanding of their assigned roles and responsibilities.
**Guidance - Examples of 3.1.2:**A method to document roles and responsibilities is a responsibility assignment matrix that includes who is responsible, accountable, consulted, and informed (also called a RACI matrix).

================

### A. Tài liệu gốc của Requirement 3

### https://docs.google.com/document/d/18t2FQJDbxwK6VmJ_qoJw3gLzNKC1-pMxB_VG6QT3VYA/edit?usp=sharing

### B. Summary Overview của Control Objective 3.2
Tài liệu này mô tả chi tiết **Control Objective 3.2 **của **Requirement 3** trong **PCI-DSS v4.0.1**, tập trung vào việc giảm thiểu lưu trữ dữ liệu tài khoản thông qua chính sách lưu trữ và tiêu hủy dữ liệu.
Mục tiêu chính là đảm bảo dữ liệu tài khoản chỉ được lưu trữ khi cần thiết, trong thời gian tối thiểu và được xóa hoặc làm không thể khôi phục khi không còn nhu cầu.
Gồm 1 sub-requirement chính:
- 3.2.1: Chính sách lưu trữ và tiêu hủy dữ liệu
Áp dụng cho toàn bộ hệ thống, quy trình và vị trí có lưu trữ dữ liệu tài khoản (bao gồm cả môi trường bên thứ ba nếu có).

### C. Key Points của Control Objective 3.2
- **Phạm vi áp dụng**: Tất cả vị trí lưu trữ dữ liệu tài khoản (bao gồm backup, archive, thiết bị rời, TPSP)
- **Trách nhiệm:**Tài liệu hóa, phân rõ vai trò và đảm bảo thực thi chính sách lưu trữ/tiêu hủy
- **Quản lý lưu trữ dữ liệu:** Giới hạn loại dữ liệu, thời gian lưu trữ theo yêu cầu pháp lý/kinh doanh
- **Chính sách & quy trình:**Phải có retention policy rõ ràng, có business justification
- **Xóa dữ liệu:**Phải xóa an toàn hoặc làm dữ liệu không thể khôi phục
- **Kiểm soát định kỳ:** Kiểm tra ít nhất mỗi 3 tháng để đảm bảo dữ liệu quá hạn đã được xóa

### D. Deep Summary của Control Objective 3.2
**Bối cảnh:**
Lưu trữ dữ liệu quá mức hoặc không kiểm soát làm tăng rủi ro rò rỉ dữ liệu. Việc không xóa dữ liệu đúng hạn khiến hệ thống giữ lại thông tin nhạy cảm không cần thiết.
**Nội dung cốt lõi:**
- Xác định rõ dữ liệu nào cần lưu, lưu ở đâu, bao lâu
- Giới hạn lưu trữ theo yêu cầu pháp lý, quy định hoặc kinh doanh
- Tài liệu hóa retention period và business justification
- Thiết lập quy trình xóa an toàn hoặc làm dữ liệu không thể khôi phục
- Kiểm tra định kỳ (≥ 3 tháng/lần) việc xóa dữ liệu quá hạn
- Bao phủ cả SAD lưu trước khi authorization (yêu cầu bắt buộc sau 31/03/2025)
**Dữ liệu đáng chú ý:**
- Tần suất kiểm tra xóa dữ liệu: ít nhất 3 tháng/lần
- Bao phủ toàn bộ location lưu trữ (bao gồm TPSP, cloud, backup, giấy tờ…)
**Rủi ro / Lưu ý:**
- Không kiểm soát retention → lưu dữ liệu vượt nhu cầu → tăng rủi ro lộ dữ liệu
- Xóa thông thường (OS delete) không đủ → dữ liệu vẫn có thể khôi phục
- Bỏ sót location lưu trữ (backup, archive…) → vi phạm compliance
- Phụ thuộc TPSP nhưng không kiểm soát → không đảm bảo xóa dữ liệu đúng yêu cầu

### E. Structured Output của Control Objective 3.2
**Control objectives:**3.2
**Sub-requirement:**3.2.1 *(Tag: data retention policy, data minimization, storage limitation, secure deletion, data lifecycle management)*
**Defined Approach Requirements of 3.2.1:**Account data storage is kept to a minimum through implementation of data retention and disposal policies, procedures, and processes that include at least the following:
• Coverage for all locations of stored account data.
• Coverage for any sensitive authentication data (SAD) stored prior to completion of authorization. This bullet is a best practice until its effective date; refer to Applicability Notes below for details.
• Limiting data storage amount and retention time to that which is required for legal or regulatory, and/or business requirements.
• Specific retention requirements for stored account data that defines length of retention period and includes a documented business justification.
• Processes for secure deletion or rendering account data unrecoverable when no longer needed per the retention policy.
• A process for verifying, at least once every three months, that stored account data exceeding the defined retention period has been securely deleted or rendered unrecoverable.
**Defined Approach Testing Procedures of 3.2.1:**
- "3.2.1.a": Examine the data retention and disposal policies, procedures, and processes and interview personnel to verify processes are defined to include all elements specified in this requirement.
- "3.2.1.b": Examine files and system records on system components where account data is stored to verify that the data storage amount and retention time does not exceed the requirements defined in the data retention policy.
- "3.2.1.c": Observe the mechanisms used to render account data unrecoverable to verify data cannot be recovered.
**Customized Approach Objective of 3.2.1:**Account data is retained only where necessary and for the least amount of time needed and is securely deleted or rendered unrecoverable when no longer needed.
**Applicability Notes of 3.2.1:**Where account data is stored by a TPSP (for example, in a cloud environment), entities are responsible for working with their service providers to understand how the TPSP meets this requirement for the entity. Considerations include ensuring that all geographic instances of a data element are securely deleted. The bullet above (for coverage of SAD stored prior to completion of authorization) is a best practice until 31 March 2025, after which it will be required as part of Requirement 3.2.1 and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose of 3.2.1:**A formal data retention policy identifies what data needs to be retained, for how long, and where that data resides so it can be securely destroyed or deleted as soon as it is no longer needed. The only account data that may be stored after authorization is the primary account number or PAN (rendered unreadable), expiration date, cardholder name, and service code. The storage of SAD data prior to the completion of the authorization process is also included in the data retention and disposal policy so that storage of this sensitive data is kept to minimum, and only retained for the defined amount of time.
**Guidance - Good Practice of 3.2.1:**When identifying locations of stored account data, consider all processes and personnel with access to the data, as data could have been moved and stored in different locations than originally defined. Storage locations that are often overlooked include backup and archive systems, removable data storage devices, paper-based media, and audio recordings. To define appropriate retention requirements, an entity first needs to understand its own business needs as well as any legal or regulatory obligations that apply to its industry or to the type of data being retained. Implementing an automated process to ensure data is automatically and securely deleted upon its defined retention limit can help ensure that account data is not retained beyond what is necessary for business, legal, or regulatory purposes.
Methods of eliminating data when it exceeds the retention period include secure deletion to complete removal of the data or rendering it unrecoverable and unable to be reconstructed. Identifying and securely eliminating stored data that has exceeded its specified retention period prevents unnecessary retention of data that is no longer needed. This process may be automated, manual, or a combination of both. The deletion function in most operating ystems is not "secure deletion" as it allows deleted data to be recovered, so instead, a dedicated secure deletion function or application must be used to make data unrecoverable. Remember, if you don't need it, don't store it!
**Guidance - Examples of 3.2.1:**An automated, programmatic procedure could be run to locate and remove data, or a manual review of data storage areas could be performed. Whichever method is used, it is a good idea to monitor the process to ensure it is completed successfully, and that the results are recorded and validated as being complete. Implementing secure deletion methods ensures that the data cannot be retrieved when it is no longer needed.
**Guidance - Further Information of 3.2.1:**See NIST SP 800-88 Rev. 1, Guidelines for Media Sanitization .

================

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

================

### A. Tài liệu gốc của Requirement 3

### B. Summary Overview của Requirement 3
Tài liệu này mô tả chi tiết **Control Objective 3.4 **của** Requirement 3** trong **PCI-DSS v4.0.1**, tập trung vào việc hạn chế hiển thị và kiểm soát việc truy cập, sao chép dữ liệu PAN nhằm giảm thiểu rủi ro lộ dữ liệu.
Mục tiêu chính là đảm bảo PAN chỉ được hiển thị ở mức tối thiểu cần thiết và không bị sao chép hoặc di chuyển trái phép, đặc biệt trong các môi trường truy cập từ xa.
Gồm 2 sub-requirement chính:
- 3.4.1: Masking PAN khi hiển thị
- 3.4.2: Kiểm soát sao chép/di chuyển PAN qua remote access
Áp dụng cho tất cả các hình thức hiển thị PAN (màn hình, in ấn, báo cáo) và các công nghệ truy cập từ xa có khả năng truy cập hoặc thao tác với PAN.

### C. Key Points của Control Objective 3.4
- **Phạm vi áp dụng:**Tất cả nơi hiển thị PAN và môi trường remote access
- **Trách nhiệm:** Tài liệu hóa role, phân rõ quyền truy cập PAN đầy đủ
- **Kiểm soát hiển thị:**PAN phải được masking (tối đa BIN + last 4)
- **Phân quyền:**Chỉ role có business need mới được xem full PAN
- **Kiểm soát kỹ thuật:** Ngăn chặn copy/relocate PAN qua remote access
- **Danh sách quyền:** Phải duy trì danh sách user/role được phép truy cập hoặc thao tác PAN

### D. Deep Summary của Control Objective 3.4
**Bối cảnh:**Việc hiển thị hoặc sao chép PAN không kiểm soát là nguyên nhân phổ biến dẫn đến rò rỉ dữ liệu và gian lận thẻ. Các kênh hiển thị và remote access là điểm dễ bị khai thác.
**Nội dung cốt lõi:**
- Masking PAN khi hiển thị, chỉ hiển thị tối đa BIN + 4 số cuối
- Chỉ cho phép hiển thị full PAN với role có business need rõ ràng
- Áp dụng kiểm soát truy cập theo role
- Ngăn chặn copy/relocate PAN trong môi trường remote access
- Chỉ cho phép thao tác PAN khi có explicit authorization
**Dữ liệu đáng chú ý:**
- Masking ≠ truncation (masking có thể unmask, truncation thì không)
- Remote access bao gồm VDI, remote desktop, cloud session
**Rủi ro / Lưu ý:**
- Hiển thị full PAN không kiểm soát → rò rỉ dữ liệu
- Không kiểm soát remote access → dễ bị copy ra local hoặc thiết bị ngoài
- Thiếu phân quyền rõ ràng → user xem dữ liệu vượt nhu cầu
- Lưu PAN trên thiết bị local → mở rộng scope PCI DSS không cần thiết

### E. Structured Output của Requirement 3
**Control objectives:**3.4
**Sub-requirement:**3.4.1 *(Tag: PAN masking, data masking, display protection, least privilege, BIN + last4)*
**Defined Approach Requirements of 3.4.1:**PAN is masked when displayed (the BIN and last four digits are the maximum number of digits to be displayed), such that only personnel with a legitimate business need can see more than the BIN and last four digits of the PAN.
**Defined Approach Testing Procedures of 3.4.1:**
- "3.4.1.a": Examine documented policies and procedures for masking the display of PANs to verify:
• A list of roles that need access to more than the BIN and last four digits of the PAN (includes full PAN) is documented, together with a legitimate business need for each role to have such access.
• PAN is masked when displayed such that only personnel with a legitimate business need can see more than the BIN and last four digits of the PAN.
• All roles not specifically authorized to see the full PAN must only see masked PANs.
- "3.4.1.b": Examine system configurations to verify that full PAN is only displayed for roles with a documented business need, and that PAN is masked for all other requests.
- "3.4.1.c": Examine displays of PAN (for example, on screen, on paper receipts) to verify that PANs are masked when displayed, and that only those with a legitimate business need are able to see more than the BIN and/or last four digits of the PAN.
**Customized Approach Objective of 3.4.1:**PAN displays are restricted to the minimum number of digits necessary to meet a defined business need.
**Applicability Notes of 3.4.1:**This requirement does not supersede stricter requirements in place for displays of cardholder data- for example, legal or payment brand requirements for point-of-sale (POS) receipts. This requirement relates to protection of PAN where it is displayed on screens, paper receipts, printouts, etc., and is not to be confused with Requirement 3.5.1 for protection of PAN when stored, processed, or transmitted.
**Guidance - Purpose of 3.4.1:**The display of full PAN on computer screens, payment card receipts, paper reports, etc. can result in this data being obtained by unauthorized individuals and used fraudulently. Ensuring that the full PAN is displayed only for those with a legitimate business need minimizes the risk of unauthorized persons gaining access to PAN data.
**Guidance - Good Practice of 3.4.1:**Applying access controls according to defined roles is one way to limit access to viewing full PAN to only those individuals with a defined business need. The masking approach should always display only the number of digits needed to perform a specific business function. For example, if only the last four digits are needed to perform a business function, PAN should be masked to only show the last four digits. As another example, if a function needs to view the bank identification number (BIN) for routing purposes, unmask only the BIN digits for that function.
**Guidance - Definitions of 3.4.1:**Masking is not synonymous with truncation and these terms cannot be used interchangeably. Masking refers to the concealment of certain digits during display or printing, even when the entire PAN is stored on a system. This is different from truncation, in which the truncated digits are removed and cannot be retrieved within the system. Masked PAN could be 'unmasked', but there is no "un-truncation" without recreating the PAN from another source. Refer to Appendix G for definitions of 'masking' and 'truncation.'
**Guidance - Further Information of 3.4.1:**For more information about masking and truncation, see PCI SSC's FAQs on these topics.

---
**Control objectives:**3.4
**Sub-requirement:**3.4.2 *(Tag: PAN exfiltration prevention, remote access control, data leakage prevention, endpoint control)*
**Defined Approach Requirements of 3.4.2:**When using remote-access technologies, technical controls prevent copy and/or relocation of PAN for all personnel, except for those with documented, explicit authorization and a legitimate, defined business need.
**Defined Approach Testing Procedures of 3.4.2:**
- "3.4.2.a": Examine documented policies and procedures and documented evidence for technical controls that prevent copy and/or relocation of PAN when using remote-access technologies onto local hard drives or removable electronic media to verify the following:
• Technical controls prevent all personnel not specifically authorized from copying and/or relocating PAN.
• A list of personnel with permission to copy and/or relocate PAN is maintained, together with the documented, explicit authorization and legitimate, defined business need.
- "3.4.2.b": Examine configurations for remote-access technologies to verify that technical controls to prevent copy and/or relocation of PAN for all personnel, unless explicitly authorized.
- "3.4.2.c": Observe processes and interview personnel to verify that only personnel with documented, explicit authorization and a legitimate, defined business need have permission to copy and/or relocate PAN when using remote-access technologies.
**Customized Approach Objective of 3.4.2:**PAN cannot be copied or relocated by unauthorized personnel using remote-access technologies.
**Applicability Notes of 3.4.2:**Storing or relocating PAN onto local hard drives, removable electronic media, and other storage devices brings these devices into scope for PCI DSS. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose of 3.4.2:**Relocation of PAN to unauthorized storage devices is a common way for this data to be obtained and used fraudulently. Methods to ensure that only those with explicit authorization and a legitimate business reason can copy or relocate PAN minimizes the risk of unauthorized persons gaining access to PAN.
**Guidance - Good Practice of 3.4.2:**Copying and relocation of PAN should only be done to storage devices that are permissible and authorized for that individual.
**Guidance - Definitions of 3.4.2:**A virtual desktop is an example of a remote-access technology. Such remote access technologies often include tools to disable copy and/or relocation functionality. Storage devices include, but are not limited to, local hard drives, virtual drives, removable electronic media, network drives, and cloud storage.
**Guidance - Further Information of 3.4.2:**Vendor documentation for the remote-access technology in use will provide information about the system settings needed to implement this requirement.

================

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

================

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

================

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