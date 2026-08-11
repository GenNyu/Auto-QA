### A. Tài liệu gốc của Appendix G

### B. Summary Overview của Appendix G
Tài liệu này mô tả chi tiết **Appendix G** trong **PCI-DSS v4.0.1**, tập trung vào **các thuật ngữ, từ viết tắt và định nghĩa (Glossary of Terms, Abbreviations, and Definitions)**.
Mục tiêu chính là cung cấp một bộ quy chuẩn ngôn ngữ thống nhất, giúp các thực thể, đánh giá viên và các bên liên quan hiểu chính xác các khái niệm kỹ thuật, vai trò và quy trình được sử dụng xuyên suốt trong tiêu chuẩn PCI DSS.

### C. Key Points của Appendix G
*   **Phân loại dữ liệu tài khoản:** Định nghĩa rõ ràng sự khác biệt giữa Dữ liệu chủ thẻ (Cardholder Data - CHD) và Dữ liệu xác thực nhạy cảm (Sensitive Authentication Data - SAD).
*   **Các vai trò trong hệ sinh thái thanh toán:** Giải thích chức năng của các bên như Acquirer (Ngân hàng thanh toán), Issuer (Ngân hàng phát hành), Merchant (Người bán hàng) và Service Provider (Nhà cung cấp dịch vụ).
*   **Các khái niệm kỹ thuật cốt lõi:** Định nghĩa về Môi trường dữ liệu chủ thẻ (CDE), Mật mã học mạnh (Strong Cryptography), Xác thực đa yếu tố (MFA) và Phân đoạn mạng (Segmentation).
*   **Các từ viết tắt tiêu chuẩn:** Cung cấp ý nghĩa cho các công cụ báo cáo và thực thể như AOC, ROC, SAQ, ASV, QSA và HSM.
*   **Phương pháp bảo vệ dữ liệu:** Làm rõ các kỹ thuật như Hashing (Băm), Masking (Che vùng dữ liệu), Truncation (Cắt bớt dữ liệu) và Encryption (Mã hóa).

### D. Deep Summary của Appendix G
**Bối cảnh:**
Trong một tiêu chuẩn quốc tế phức tạp như PCI DSS, việc hiểu sai một thuật ngữ có thể dẫn đến những lỗ hổng bảo mật nghiêm trọng hoặc thất bại trong quá trình đánh giá tuân thủ. Appendix G đóng vai trò là "nguồn sự thật duy nhất" về mặt ngôn ngữ để đảm bảo tất cả các bên đều có chung một cách hiểu.

**Nội dung cốt lõi:**
Phụ lục này cung cấp các định nghĩa chi tiết theo thứ tự bảng chữ cái. Một điểm quan trọng là việc phân biệt các loại phần mềm: **Bespoke software** (phát triển bởi bên thứ ba theo yêu cầu) và **Custom software** (thực thể tự phát triển cho chính mình). Ngoài ra, nó định nghĩa các cơ chế truy cập như **Administrative Access** (quyền quản trị cao cấp) và **Phishing Resistant Authentication** (xác thực chống tấn công giả mạo) để phản ánh các mối đe dọa hiện đại.

**Dữ liệu đáng chú ý:**
*   **Strong Cryptography:** Được xác định dựa trên các thuật ngữ được ngành chấp nhận, với độ dài khóa tối thiểu là **112-bit hiệu dụng**, nhưng khuyến nghị tất cả các triển khai mới sử dụng tối thiểu **128-bit**.
*   **Cardholder Data (CHD):** Tối thiểu phải bao gồm số thẻ (PAN) đầy đủ, và có thể bao gồm tên chủ thẻ, ngày hết hạn và mã dịch vụ.
*   **Sensitive Authentication Data (SAD):** Bao gồm mã xác minh thẻ (CAV2/CVC2/CVV2/CID), dữ liệu track đầy đủ, mã PIN và khối PIN.
*   **CDE (Cardholder Data Environment):** Không chỉ bao gồm các hệ thống lưu trữ/xử lý/truyền dữ liệu mà còn cả các thành phần hệ thống có kết nối không hạn chế tới các khu vực đó.

**Rủi ro / Lưu ý:**
*   **Sự khác biệt giữa Masking và Truncation:** **Masking** được dùng để ẩn dữ liệu khi hiển thị trên màn hình hoặc biên lai giấy, trong khi **Truncation** là phương pháp làm cho dữ liệu PAN không thể đọc được khi được lưu trữ, xử lý hoặc truyền tải điện tử.
*   **Phạm vi của Service Provider:** Một thực thể có thể được coi là nhà cung cấp dịch vụ ngay cả khi họ chỉ cung cấp các dịch vụ có thể tác động đến an ninh của CHD/SAD (như quản lý tường lửa hoặc IDS), chứ không nhất thiết phải trực tiếp xử lý dữ liệu đó.
*   **Trách nhiệm của thực thể:** Các định nghĩa về **Critical Systems** (hệ thống trọng yếu) hoặc **Sensitive Area** (khu vực nhạy cảm) yêu cầu thực thể phải tự xác định dựa trên tầm quan trọng đối với hoạt động kinh doanh và an ninh của mình.
### E. Structured Output của Appendix G
- **Account:** Also referred to as “user ID,” “account ID,” or “application ID.” Used to identify an individual or process on a computer system. See *Authentication Credentials and Authentication Factor.*
- **Account Data:** Account data consists of cardholder data and/or sensitive authentication data. See *Cardholder Data and Sensitive Authentication Data.*
- **Acquirer:** Also referred to as “merchant bank,” “acquiring bank,” or “acquiring financial institution.” Entity, typically a financial institution, that processes payment card transactions for merchants and is defined by a payment brand as an acquirer. Acquirers are subject to *payment brand rules and procedures regarding merchant compliance. See Payment Processor.*
- **Administrative Access:** Elevated or increased privileges granted to an account for that account to manage systems, networks, and/or applications. Administrative access can be assigned to an individual’s account or a built-in system account. Accounts with administrative access are often referred to as “superuser,” “root,” “administrator,” “admin,” “sysadmin,” or “supervisor-state,” depending on the particular operating system and organizational structure.
- **AES:** Acronym for “Advanced Encryption Standard.” See *Strong Cryptography.*
- **ANSI:** Acronym for “American National Standards Institute.”
- **Anti-Malware:** Software that is designed to detect, and remove, block, or contain various forms of malicious software.
- **AOC:** Acronym for “Attestation of Compliance.” The AOC is the official PCI SSC form for merchants and service providers to attest to the results of a PCI DSS assessment, as documented in a Self-Assessment Questionnaire (SAQ) or Report on Compliance (ROC).
- **Application:** Includes all purchased, custom, and bespoke software programs or groups of programs, including both internal and external (for example, web) applications.
- **Application and System Accounts:** Also referred to as “service accounts.” Accounts that execute processes or perform tasks on a computer system or in an application. These accounts usually have elevated privileges that are required to perform specialized tasks or functions and are not typically accounts used by an individual.
- **ASV:** Acronym for “Approved Scanning Vendor.” Company approved by the PCI SSC to conduct external vulnerability scanning services.
- **Audit Log:** Also referred to as “audit trail.” Chronological record of system activities. Provides an independently verifiable trail sufficient to permit reconstruction, review, and examination of sequence of environments and activities surrounding or leading to operation, procedure, or event in a transaction from inception to final results.
- **Authentication:** Process of verifying identity of an individual, device, or process. Authentication typically occurs with one or more authentication factors. *See Account, Authentication Credential, and Authentication Factor.*
- **Authentication Credential:** Combination of the user ID or account ID plus the authentication factor(s) used to authenticate an individual, device, or process. See *Account and Authentication Factor.*
- **Authentication Factor:** The element used to prove or verify the identity of an individual or process on a computer system. Authentication typically occurs with one or more of the following authentication factors: <ul><li>Something you know, such as a password or passphrase,</li><li>Something you have, such as a token device or smart card,</li><li>Something you are, such as a biometric element.</li></ul>The ID (or account) and authentication factor together are considered authentication credentials. *See Account and Authentication Credential.*
- **Authorization:** In the context of access control, authorization is the granting of access or other rights to a user, program, or process. Authorization defines what an individual or program can do after successful authentication. In the context of a payment card transaction, authorization refers to the authorization process, which completes when a merchant receives a transaction response (for example, an approval or decline).