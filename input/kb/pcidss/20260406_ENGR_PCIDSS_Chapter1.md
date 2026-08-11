### A. Tài liệu gốc của Chapter 1

### B. Summary Overview của Chapter 1
Tài liệu này mô tả chi tiết **Chapter 1** trong **PCI-DSS v4.0.1**, tập trung vào việc giới thiệu tổng quan về tiêu chuẩn bảo mật dữ liệu thẻ thanh toán và các yêu cầu cốt lõi của nó
Mục tiêu chính là cung cấp một bộ khung các yêu cầu kỹ thuật và vận hành cơ bản (baseline) nhằm bảo vệ dữ liệu tài khoản thanh toán và thúc đẩy việc áp dụng các biện pháp bảo mật nhất quán trên phạm vi toàn cầu,

### C. Key Points của Chapter 1
- **Cấu trúc cốt lõi:** PCI DSS bao gồm 12 yêu cầu chính được thiết kế để xây dựng và duy trì hệ thống mạng an toàn, bảo vệ dữ liệu chủ thẻ, quản lý lỗ hổng và kiểm soát truy cập nghiêm ngặt,
- **Tính toàn diện:** Tiêu chuẩn cung cấp không chỉ các yêu cầu bảo mật chi tiết mà còn đi kèm với các quy trình kiểm tra tương ứng và hướng dẫn thực thi tốt nhất cho các đơn vị
- **Phạm vi mở rộng:** Mặc dù tập trung vào dữ liệu tài khoản, PCI DSS còn có thể được sử dụng để bảo vệ các thành phần khác trong hệ sinh thái thanh toán chống lại các mối đe dọa
- **Nguồn lực hỗ trợ:** PCI SSC cung cấp một thư viện tài liệu phong phú với hơn 60 hướng dẫn chuyên sâu về các chủ đề như Điện toán đám mây, xác thực đa yếu tố (MFA) và quản lý bên thứ ba,

### D. Deep Summary của Chapter 1
**Bối cảnh:**
PCI DSS được phát triển để nâng cao tính an toàn cho dữ liệu tài khoản thanh toán trong bối cảnh các mối đe dọa an ninh mạng ngày càng phức tạp. Đây là tiêu chuẩn bắt buộc cho các thực thể tham gia vào việc lưu trữ, xử lý hoặc truyền dẫn dữ liệu thẻ,

**Nội dung cốt lõi:**
Chương này thiết lập nền tảng thông qua **12 yêu cầu bảo mật chính**, chia thành 6 nhóm mục tiêu lớn:
1.  Xây dựng mạng và hệ thống an toàn (Yêu cầu 1 & 2)
2.  Bảo vệ dữ liệu tài khoản (Yêu cầu 3 & 4)
3.  Duy trì chương trình quản lý lỗ hổng (Yêu cầu 5 & 6)
4.  Triển khai các biện pháp kiểm soát truy cập mạnh (Yêu cầu 7, 8 & 9)
5.  Thường xuyên theo dõi và kiểm tra mạng (Yêu cầu 10 & 11)
6.  Duy trì chính sách bảo mật thông tin (Yêu cầu 12)

**Dữ liệu đáng chú ý:**
- **Phiên bản hiện tại:** v4.0.1 (xuất bản tháng 6/2024)
- **Số lượng tài liệu hướng dẫn:** Có hơn **60 tài liệu** bổ sung và hướng dẫn chuyên sâu trên website của PCI SSC
- **Quy trình đánh giá:** Bao gồm các bước từ xác nhận phạm vi đến thực hiện remediation (khắc phục) nếu cần thiết,

**Rủi ro / Lưu ý:**
- **Ưu tiên pháp luật:** Nếu có bất kỳ yêu cầu nào trong tiêu chuẩn xung đột với luật pháp quốc gia hoặc địa phương, **luật pháp địa phương sẽ được ưu tiên áp dụng**
- **Yêu cầu tối thiểu:** PCI DSS chỉ là bộ yêu cầu tối thiểu; các đơn vị nên bổ sung thêm các biện pháp kiểm soát khác dựa trên phân tích rủi ro và quy định riêng của từng khu vực
- **Thông tin bổ sung:** Các tài liệu bổ sung (Information Supplements) giúp hỗ trợ thực thi nhưng không thay thế hoặc mở rộng các yêu cầu bắt buộc của PCI DSS

### E. Structured Output của Chapter 1
The Payment Card Industry Data Security Standard (PCI DSS) was developed to encourage and enhance payment account data security and facilitate the broad adoption of consistent data security measures globally. PCI DSS provides a baseline of technical and operational requirements designed to protect account data. While specifically designed to focus on environments with payment account data, PCI DSS can also be used to protect against threats and secure other elements in the payment ecosystem.

Table 1 shows the 12 principal PCI DSS requirements.
#### Table 1. Principal PCI DSS Requirements
**PCI Data Security Standard – High Level Overview**
- Build and Maintain a Secure Network and Systems
    1. Install and Maintain Network Security Controls.
    2. Apply Secure Configurations to All System Components.
- Protect Account Data
    3. Protect Stored Account Data.
    4. Protect Cardholder Data with Strong Cryptography During Transmission Over Open, Public Networks.
- Maintain a Vulnerability Management Program
    5. Protect All Systems and Networks from Malicious Software.
    6. Develop and Maintain Secure Systems and Software.
- Implement Strong Access Control Measures
    7. Restrict Access to System Components and Cardholder Data by Business Need to Know.
    8. Identify Users and Authenticate Access to System Components.
    9. Restrict Physical Access to Cardholder Data.
- Regularly Monitor and Test Networks
    10. Log and Monitor All Access to System Components and Cardholder Data.
    11. Test Security of Systems and Networks Regularly.
- Maintain an Information Security Policy
    12. Support Information Security with Organizational Policies and Programs.

---
This document, the Payment Card Industry Data Security Standard Requirements and Testing Procedures, consists of the 12 PCI DSS principal requirements, detailed security requirements, corresponding testing procedures, and other information pertinent to each requirement. The following sections provide detailed guidelines and best practices to assist entities to prepare for, conduct, and report the results of a PCI DSS assessment. The PCI DSS requirements and testing procedures begin on page 43.

PCI DSS comprises a minimum set of requirements for protecting account data and may be enhanced by additional controls and practices to further mitigate risks, and to incorporate local, regional, and sector laws and regulations. Additionally, legislation or regulatory requirements may require specific protection of personal information or other data elements (for example, cardholder name).

#### Limitations
If any of the requirements contained in this standard conflict with country, state, or local laws, the country, state, or local law will apply.

#### PCI DSS Resources
The PCI Security Standards Council (PCI SSC) website (www.pcisecuritystandards.org) provides the following additional resources to assist organizations with their PCI DSS assessments and validations:
- Document Library, including:
    - PCI DSS Summary of Changes
    - PCI DSS Quick Reference Guide
    - Information Supplements and Guidelines
    - Prioritized Approach for PCI DSS
    - Report on Compliance (ROC) Reporting Template and Reporting Instructions
    - Self-Assessment Questionnaires (SAQs) and SAQ Instructions and Guidelines
    - Attestations of Compliance (AOCs)
- Frequently Asked Questions (FAQs)
- PCI for Small Merchants website
- PCI training courses and informational webinars
- List of Qualified Security Assessors (QSAs) and Approved Scanning Vendors (ASVs)
- Lists of PCI approved devices, applications, and solutions

There are over 60 guidance documents and information supplements available on the PCI SSC website that provide specific guidance and considerations for PCI DSS. Examples include:
- Guidance for PCI DSS Scoping and Network Segmentation
- PCI SSC Cloud Computing Guidelines
- Multi-Factor Authentication Guidance
- Third-Party Security Assurance
- Effective Daily Log Monitoring
- Penetration Testing Guidance
- Best Practices for Implementing a Security Awareness Program
- Best Practices for Maintaining PCI DSS Compliance
- PCI DSS for Large Organizations
- Use of SSL/Early TLS and Impact on ASV Scans
- Use of SSL/Early TLS for POS POI Terminal Connections
- Tokenization Product Security Guidelines
- Protecting Telephone-Based Payment Card Data

Refer to the Document Library at www.pcisecuritystandards.org for information about these and other resources.

In addition, refer to Appendix G for definitions of PCI DSS terms.

**Note:** Information Supplements complement PCI DSS and identify additional considerations and recommendations for meeting PCI DSS requirements. Information Supplements do not supersede, replace, or extend PCI DSS or any of its requirements.