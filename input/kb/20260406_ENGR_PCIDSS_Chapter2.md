### A. Tài liệu gốc của Chapter 2

### B. Summary Overview của Chapter 2
Tài liệu này mô tả chi tiết **Chapter 2** trong **PCI-DSS v4.0.1**, tập trung vào **thông tin về khả năng áp dụng (applicability)** của tiêu chuẩn đối với các thực thể tham gia vào hệ sinh thái thanh toán. 
Mục tiêu chính là **định nghĩa rõ ràng các loại dữ liệu tài khoản** (Account Data), bao gồm dữ liệu chủ thẻ (CHD) và dữ liệu xác thực nhạy cảm (SAD), đồng thời xác định phạm vi trách nhiệm của các tổ chức khi lưu trữ, xử lý hoặc truyền dẫn các loại dữ liệu này.

### C. Key Points của Chapter 2
- **Đối tượng áp dụng:** Tất cả các thực thể lưu trữ, xử lý, truyền dẫn dữ liệu chủ thẻ (CHD) và dữ liệu xác thực nhạy cảm (SAD), hoặc các thực thể có thể gây ảnh hưởng đến an ninh của môi trường dữ liệu này.
- **Yếu tố xác định (Defining Factor):** Số tài khoản chính (PAN) là yếu tố then chốt để xác định sự hiện diện của dữ liệu chủ thẻ và phạm vi áp dụng (CDE) của tiêu chuẩn.
- **Phân loại dữ liệu:** Phân biệt rõ giữa **Dữ liệu chủ thẻ** (như PAN, tên chủ thẻ, ngày hết hạn) và **Dữ liệu xác thực nhạy cảm** (như dữ liệu track đầy đủ, mã xác thực thẻ CVV, mã PIN).
- **Trách nhiệm thuê ngoài:** Các thực thể thuê bên thứ ba (TPSP) để vận hành thanh toán vẫn phải chịu trách nhiệm đảm bảo dữ liệu tài khoản được bảo vệ theo đúng yêu cầu của PCI DSS.
- **Tính không thể thay thế:** Các thuật ngữ Account Data, CHD và SAD có ý nghĩa riêng biệt và **không thể dùng thay thế cho nhau** trong các yêu cầu của tiêu chuẩn.

### D. Deep Summary của Chapter 2
**Bối cảnh:**
Chapter 2 thiết lập khung pháp lý và kỹ thuật về việc "ai" và "cái gì" phải tuân thủ PCI DSS. Tiêu chuẩn này bao phủ toàn bộ các bên liên quan từ người bán (merchants), đơn vị xử lý (processors), ngân hàng thanh toán (acquirers), ngân hàng phát hành (issuers) cho đến các nhà cung cấp dịch vụ (service providers).

**Nội dung cốt lõi:**
- **Cấu trúc dữ liệu tài khoản:** Dữ liệu tài khoản được chia làm hai nhóm chính với các quy tắc bảo mật khác nhau. Dữ liệu chủ thẻ (CHD) có thể được lưu trữ nếu cần thiết cho kinh doanh nhưng phải được bảo vệ, trong khi dữ liệu xác thực nhạy cảm (SAD) bị nghiêm cấm lưu trữ sau khi đã cấp phép giao dịch (authorization).
- **Điều kiện áp dụng linh hoạt:** Tiêu chuẩn vẫn có thể áp dụng ngay cả khi thực thể không lưu trữ PAN, ví dụ: nếu thực thể lưu trữ SAD, thuê bên thứ ba quản lý CDE, hoặc dữ liệu thẻ chỉ tồn tại trên phương tiện vật lý như giấy.

**Dữ liệu đáng chú ý:**
- **Bảng quy định lưu trữ (Table 3):** Quy định rõ PAN **bắt buộc** phải được làm cho không thể đọc được (unreadable) khi lưu trữ (ví dụ bằng mã hóa mạnh), trong khi tên chủ thẻ và ngày hết hạn thì không bắt buộc nhưng cần được lưu trữ ở mức tối thiểu.
- **Cấm lưu trữ SAD:** Tuyệt đối không lưu trữ dữ liệu track đầy đủ, CVV hoặc mã PIN sau khi hoàn tất bước cấp phép, **ngay cả khi đã được mã hóa** (ngoại trừ một số trường hợp cụ thể cho ngân hàng phát hành).

**Rủi ro / Lưu ý:**
- **Luồng dữ liệu ngoài ý muốn:** Nếu thực thể nhận được dữ liệu thẻ qua các kênh không mong muốn (ví dụ email), họ phải chọn giữa việc đưa kênh đó vào phạm vi quản lý của PCI DSS hoặc xóa dữ liệu an toàn và thực hiện các biện pháp ngăn chặn trong tương lai.
- **Quyền quyết định tuân thủ:** Việc một thực thể có bắt buộc phải xác nhận tuân thủ hay không phụ thuộc vào quy định của các tổ chức quản lý chương trình tuân thủ (như các thương hiệu thẻ hoặc ngân hàng thanh toán).
- **Dữ liệu mã hóa:** Việc mã hóa PAN đơn thuần **không giúp** đưa hệ thống đó ra khỏi phạm vi (out of scope) của PCI DSS nếu thực thể đó vẫn giữ khóa giải mã hoặc có khả năng ảnh hưởng đến an ninh của dữ liệu.

### E. Structured Output của Chapter 2
PCI DSS is intended for all entities that store, process, or transmit cardholder data (CHD) and/or sensitive authentication data (SAD) or could impact the security of the cardholder data and/or sensitive authentication data. This includes all entities involved in payment account processing —including merchants, processors, acquirers, issuers, and other service providers.

Whether any entity is required to comply with or validate their compliance to PCI DSS is at the discretion of those organizations that manage compliance programs (such as payment brands and acquirers); contact these organizations for any additional criteria.

#### Defining Account Data, Cardholder Data, and Sensitive Authentication Data
Cardholder data and sensitive authentication data are considered account data and are defined as follows:

#### Table 2. Account Data
Account Data
- Cardholder Data includes:
    * Primary Account Number (PAN)
    * Cardholder Name
    * Expiration Date
    * Service Code
- Sensitive Authentication Data includes:
    * Full track data (magnetic-stripe data or equivalent on a chip)
    * Card verification code
    * PINs/PIN blocks

---
PCI DSS requirements apply to entities with environments where account data (cardholder data and/or sensitive authentication data) is stored, processed, or transmitted, and entities with environments that can impact the security of cardholder data and/or sensitive authentication data. Some PCI DSS requirements may also apply to entities with environments that do not store, process, or transmit account datafor example, entities that outsource payment operations or management of their cardholder data environment (CDE) (1). Entities that outsource their payment environments or payment operations to third parties remain responsible for ensuring that the account data is protected by the third party per applicable PCI DSS requirements.

(1) In accordance with those organizations that manage compliance programs (such as payment brands and acquirers); entities should contact these organizations for more details.

The primary account number (PAN) is the defining factor for cardholder data. The term account data therefore covers the following: the full PAN, any other elements of cardholder data that are present with the PAN, and any elements of sensitive authentication data.

If cardholder name, service code, and/or expiration date are stored, processed, or transmitted with the PAN, or are otherwise present in the CDE, they must be protected in accordance with the PCI DSS requirements applicable to cardholder data.

If an entity stores, processes, or transmits PAN, then a CDE exists to which PCI DSS requirements will apply. Some requirements may not be applicable, for example if the entity does not store PAN, then the requirements relating to the protection of stored PAN in Requirement 3 will not be applicable to the entity.

Even if an entity does not store, process, or transmit PAN, some PCI DSS requirements may still apply. Consider the following:
- If the entity stores SAD, requirements specifically related to SAD storage in Requirement 3 will be applicable.
- If the entity engages third-party service providers to store, process or transmit PAN on its behalf, requirements related to the management of service providers in Requirement 12 will be applicable.
- If the entity can impact the security of cardholder data and/or sensitive authentication data because the security of an entity’s infrastructure can affect how cardholder data is processed (for example, via a web server that controls the generation of a payment form or page) some requirements will be applicable.
- If cardholder data is only present on physical media (for example paper), requirements relating to the security and disposal of physical media in Requirement 9 will be applicable.
- Requirements related to an incident response plan are applicable to all entities, to ensure that there are procedures to follow in the event of a suspected or actual breach of the confidentiality of cardholder data.

#### Use of Account Data, Sensitive Authentication Data, Cardholder Data, and Primary Account Number in PCI DSS
PCI DSS includes requirements that specifically refer to account data, cardholder data, and sensitive authentication data. It is important to note that each of these types of data are different and the terms are not interchangeable. Specific references within requirements to account data, cardholder data, or sensitive authentication data are purposeful, and the requirements apply specifically to the type of data that is referenced.

#### Elements of Account Data and Storage Requirements
Table 3 identifies the elements of cardholder and sensitive authentication data, whether storage of each data element is permitted or prohibited, and whether each data element must be rendered unreadable—for example, with strong cryptography—when stored. This table is not exhaustive and is presented to illustrate only how the stated requirements apply to the different data elements.

#### Table 3. Account Data Element Storage Requirements (Non-table format)
**Account Data - Cardholder Data:**
- Primary Account Number (PAN)
    - Storage restrictions: Storage is kept to a minimum as defined in Requirement 3.2.
    - Required to render stored data unreadable: Yes, as defined in Requirement 3.5.
- Cardholder Name
    - Storage restrictions: Storage is kept to a minimum as defined in Requirement 3.2 (2).
    - Required to render stored data unreadable: No.
- Service Code
    - Storage restrictions: Storage is kept to a minimum as defined in Requirement 3.2 (2).
    - Required to render stored data unreadable: No.
- Expiration Date
    - Storage restrictions: Storage is kept to a minimum as defined in Requirement 3.2 (2).
    - Required to render stored data unreadable: No.
**Account Data - Sensitive Authentication Data:**
- Full Track Data
    - Storage restrictions: Cannot be stored after authorization as defined in Requirement 3.3.1 (3).
    - Required to render stored data unreadable: Yes (data stored until authorization is complete must be protected with strong cryptography as defined in Requirement 3.3.2).
- Card verification code
    - Storage restrictions: Cannot be stored after authorization as defined in Requirement 3.3.1 (3).
    - Required to render stored data unreadable: Yes (data stored until authorization is complete must be protected with strong cryptography as defined in Requirement 3.3.2).
- PIN/PIN Block
    - Storage restrictions: Cannot be stored after authorization as defined in Requirement 3.3.1 (3).
    - Required to render stored data unreadable: Yes (data stored until authorization is complete must be protected with strong cryptography as defined in Requirement 3.3.2).

---
Additional Notes on Table 3:
- If PAN is stored with other elements of cardholder data, only the PAN must be rendered unreadable according to PCI DSS Requirement 3.5.1.
- Sensitive authentication data must not be stored after authorization, even if encrypted. This applies even for environments where there is no PAN present.
- (2) Where data exists in the same environment as PAN.
- (3) Except as permitted for issuers and companies that support issuing services. Requirements for issuers and issuing services are separately defined in Requirement 3.3.3.
