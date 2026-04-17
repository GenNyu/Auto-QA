### A. Tài liệu gốc của Chapter 9

### B. Summary Overview của Chapter 9
Tài liệu này mô tả chi tiết **Chapter 9** trong **PCI-DSS v4.0.1**, tập trung vào việc **bảo vệ thông tin về vị thế bảo mật (Security Posture) của một thực thể**.
Mục tiêu chính là đảm bảo các tài liệu và bằng chứng (artifacts) phát sinh trong quá trình thiết lập và duy trì tuân thủ PCI DSS được bảo vệ nghiêm ngặt theo chính sách bảo mật của tổ chức, nhằm tránh việc lộ lọt các thông tin nhạy cảm về cấu trúc hệ thống.

### C. Key Points của Chapter 9
- **Phân loại tài liệu nhạy cảm:** Các thực thể phải coi các tài liệu như Báo cáo Tuân thủ (ROC), Bảng câu hỏi tự đánh giá (SAQ), sơ đồ mạng và cấu hình bảo mật là thông tin nhạy cảm cần được bảo vệ.
- **Ngoại lệ cho AOC:** Giấy xác nhận tuân thủ (AOC) **không bị coi là nhạy cảm** và các nhà cung cấp dịch vụ bên thứ ba (TPSP) được kỳ vọng sẽ chia sẻ tài liệu này cho khách hàng của họ.
- **Trách nhiệm của TPSP:** Theo Yêu cầu 12.9, các TPSP có nghĩa vụ hỗ trợ khách hàng bằng cách cung cấp thông tin để theo dõi trạng thái tuân thủ và cung cấp bằng chứng cho các yêu cầu bảo mật mà họ đảm nhiệm.
- **Nghĩa vụ của đơn vị đánh giá (QSA):** Các công ty QSA phải tuân thủ các quy trình đã được lập văn bản để bảo vệ thông tin bí mật của khách hàng thu thập được trong quá trình đánh giá bằng các biện pháp vật lý và điện tử phù hợp.

### D. Deep Summary của Chapter 9
**Bối cảnh:**
Quá trình đánh giá PCI DSS tạo ra rất nhiều "tài sản trí tuệ" về bảo mật. Nếu những thông tin này (như sơ đồ luồng dữ liệu hoặc giao thức quản lý khóa) bị lộ, kẻ tấn công có thể nắm được "bản đồ" chi tiết để xâm nhập vào môi trường dữ liệu chủ thẻ.

**Nội dung cốt lõi:**
- **Bảo vệ bằng chứng nội bộ:** Thực thể cần rà soát tất cả các hiện vật liên quan đến kiểm soát PCI DSS và áp dụng các biện pháp bảo vệ tương đương với mức độ nhạy cảm của thông tin đó.
- **Hỗ trợ khách hàng của TPSP:** Việc bảo vệ thông tin nhạy cảm không được làm cản trở nghĩa vụ của TPSP trong việc cung cấp thông tin cần thiết cho khách hàng để họ quản lý mối quan hệ bên thứ ba theo Yêu cầu 12.8.
- **Ràng buộc pháp lý của QSA:** Các đơn vị đánh giá phải cam kết duy trì tính riêng tư và bảo mật của thông tin, trừ khi việc tiết lộ được yêu cầu bởi cơ quan pháp luật có thẩm quyền.

**Dữ liệu đáng chú ý:**
- **Danh mục hiện vật cần bảo vệ:** Bao gồm ROC/SAQ, sơ đồ mạng, sơ đồ luồng dữ liệu tài khoản, quy tắc bảo mật, tiêu chuẩn cấu hình hệ thống, phương pháp và giao thức mã hóa/quản lý khóa.
- **Yêu cầu 12.9:** Là quy định then chốt buộc TPSP phải hỗ trợ khách hàng về thông tin tuân thủ và trách nhiệm chung.

**Rủi ro / Lưu ý:**
- **Tính minh bạch của AOC:** Mặc dù ROC là nhạy cảm, nhưng AOC là tài liệu công khai để chứng minh tính tuân thủ với các bên liên quan, do đó không cần áp dụng các biện pháp bảo mật quá khắt khe như đối với ROC.
- **An toàn lưu trữ của QSA:** Thực thể nên xác nhận rằng đơn vị đánh giá của mình có các biện pháp bảo vệ (safeguards) phù hợp theo tiêu chuẩn ngành đối với dữ liệu thu thập được trong quá trình làm việc.

### E. Structured Output của Chapter 9
The processes related to becoming and maintaining a PCI DSS compliant environment results in many artifacts that an entity may consider sensitive and may want to protect as such, including such items as the following:

- The Report on Compliance or Self-Assessment Questionnaire (the associated Attestation of Compliance is not considered sensitive and third-party service providers (TPSPs) are expected to share their AOC with customers).
- Network diagrams and account data-flow diagrams, and security configurations and rules.
- System configuration standards.
- Cryptography and key management methods and protocols.

Entities should review all the artifacts related to PCI DSS controls or the assessment and protect them in accordance with the entity’s security policies for this type of information.

TPSPs are required (PCI DSS Requirement 12.9) to support their customers with the following:

- Information needed for customers to monitor the TPSPs’ PCI DSS compliance status (to enable the customer to comply with Requirement 12.8), and
- Evidence that the TPSP is meeting applicable PCI DSS requirements where the TPSP’s services are intended to meet or facilitate meeting a customer’s PCI DSS requirements, or where those services may impact the security of a customer’s cardholder data and/or sensitive authentication data.

This section does not impact or negate a TPSP’s obligation to support and provide information to their customers per Requirement 12.9.

For more details about expectations for TPSPs and relationships between TPSPs and customers, see Use of Third-Party Service Providers.

#### Protection of Confidential and Sensitive Information by Qualified Security Assessor Companies
Each Qualified Security Assessor (QSA) Company signs an agreement with PCI SSC that they will adhere to the Qualification Requirements for QSAs. The Protection of Confidential and Sensitive Information section of that document includes the following:

"The QSA company must have and adhere to a documented process for protection of confidential and sensitive information. This must include adequate physical, electronic, and procedural safeguards consistent with industry-accepted practices to protect confidential and sensitive information against any threats or unauthorized access during storage, processing, and/or communicating of this information.

"The QSA Company must maintain the privacy and confidentiality of information obtained in the course of performing its duties and obligations as a QSA Company, unless (and to the extent) disclosure is required by legal authority."