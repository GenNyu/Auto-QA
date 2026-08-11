### A. Tài liệu gốc của Appendix A

### B. Summary Overview của Appendix A3
Tài liệu này mô tả chi tiết **Appendix A3** của **Appendix A** trong **PCI-DSS v4.0.1**, tập trung vào các yêu cầu bổ sung đối với các thực thể được chỉ định (Designated Entities) nhằm duy trì tính an toàn liên tục cho dữ liệu tài khoản.

Mục tiêu chính là thiết lập chương trình tuân thủ có sự giám sát của cấp điều hành và tích hợp việc phát hiện và ứng phó sự cố vào hoạt động hàng ngày (BAU) để đảm bảo các kiểm soát bảo mật luôn hoạt động hiệu quả
### C. Key Points của Appendix A3
- Phạm vi áp dụng: Áp dụng cho các tổ chức được chỉ định có mức độ rủi ro cao hoặc yêu cầu kiểm soát bổ sung theo PCI DSS.
- Trách nhiệm cấp điều hành: Thiết lập charter và báo cáo định kỳ ít nhất 12 tháng/lần.
- Xác nhận phạm vi: Rà soát scope PCI DSS ít nhất 3 tháng/lần hoặc sau thay đổi lớn.
- Data Discovery: Quét tìm PAN chưa mã hóa toàn hệ thống tối thiểu 3 tháng/lần.
- BAU (Duy trì bảo mật): Phát hiện và xử lý ngay lỗi kiểm soát bảo mật quan trọng; đánh giá tuân thủ BAU mỗi 3 tháng/lần; review quyền truy cập mỗi 6 tháng/lần.
- Giám sát thông minh: Triển khai cơ chế phát hiện hành vi bất thường và cảnh báo sớm.
### D. Deep Summary của Appendix A3
**Bối cảnh:** Nhằm đảm bảo an ninh không chỉ là một sự kiện đánh giá hàng năm mà là một phần của văn hóa vận hành. Các thay đổi về cấu trúc tổ chức (M&A) phải được đánh giá tác động đến bảo mật ngay lập tức

**Nội dung cốt lõi:**
- Thiết lập một chương trình tuân thủ chính thức bao gồm phân tích tác động kinh doanh và đào tạo chuyên sâu cho nhân sự phụ trách
- Thực thể phải có cơ chế ngăn chặn dữ liệu PAN rời khỏi môi trường CDE qua các kênh trái phép (như email, thiết bị lưu trữ rời)

**Dữ liệu đáng chú ý:**
- Báo cáo lãnh đạo & Đào tạo: Mỗi 12 tháng
- Xác nhận phạm vi & Khám phá dữ liệu: Mỗi 3 tháng
- Kiểm thử phân đoạn & Xem xét quyền truy cập: Mỗi 6 tháng

**Rủi ro / Lưu ý:** 
- Việc tìm thấy PAN ngoài CDE (trong log lỗi hoặc bộ nhớ đệm) yêu cầu quy trình ứng phó nghiêm ngặt để xác định nguyên nhân gốc rễ và ngăn chặn tái diễn
- Sự chậm trễ trong việc phản ứng với các cảnh báo thất bại của kiểm soát bảo mật sẽ tạo cơ hội cho kẻ tấn công xâm nhập sâu hơn
### E. Structured Output của Appendix A3
**Sub-appendix:** `A3.1.1`
**Defined Approach Requirements:** Responsibility is established by executive management for the protection of account data and a PCI DSS compliance program that includes: 
• Overall accountability for maintaining PCI DSS compliance. 
• Defining a charter for a PCI DSS compliance program. 
• Providing updates to executive management and board of directors on PCI DSS compliance initiatives and issues, including remediation activities, at least once every 12 months. 
PCI DSS Reference : Requirement 12
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Defined Approach Testing Procedures:**
- `A3.1.1.a`: Examine documentation to verify executive management has assigned overall accountability for maintaining the entity's PCI DSS compliance.
- `A3.1.1.b`: Examine the company's PCI DSS charter to verify it outlines the conditions under which the PCI DSS compliance program is organized.
- `A3.1.1.c`: Examine executive management and board of directors meeting minutes and/or presentations to ensure PCI DSS compliance initiatives and remediation activities are communicated at least once every 12 months.
**Guidance - Purpose:** Executive management assignment of PCI DSS compliance responsibilities ensures executive- level visibility into the PCI DSS compliance program and allows for the opportunity to ask appropriate questions to determine the effectiveness of the program and influence strategic priorities
**Guidance - Good Practice:** Executive management may include C-level positions, board of directors, or equivalent. The specific titles will depend on the particular organizational structure. Responsibility for the PCI DSS compliance program may be assigned to individual roles and/or to business units within the organization

---
**Sub-appendix:** `A3.1.2`
**Defined Approach Requirements:** A formal PCI DSS compliance program is in place that includes: 
• Definition of activities for maintaining and monitoring overall PCI DSS compliance, including business-as-usual activities. 
• Annual PCI DSS assessment processes. 
• Processes for the continuous validation of PCI DSS requirements (for example, daily, weekly, every three months, as applicable per the requirement). 
• A process for performing business-impact analysis to determine potential PCI DSS impacts for strategic business decisions. 
PCI DSS Reference : Requirements 1-12
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Defined Approach Testing Procedures:**
- `A3.1.2.a`: Examine information security policies and procedures to verify that processes are defined for a formal PCI DSS compliance program that includes all elements specified in this requirement.
- `A3.1.2.b`: Interview personnel and observe compliance activities to verify that a formal PCI DSS compliance program is implemented in accordance with all elements specified in this requirement.
**Guidance - Purpose:** A formal compliance program allows an organization to monitor the health of its security controls, be proactive if a control fails, and effectively communicate activities and compliance status throughout the organization
**Guidance - Good Practice:** The PCI DSS compliance program can be a dedicated program or part of overarching compliance and/or governance program, and should include a well-defined methodology that demonstrates consistent and effective evaluation. Strategic business decisions that should be analyzed for potential PCI DSS impacts may include mergers and acquisitions, new technology purchases, or new payment-acceptance channels
**Guidance - Definitions:** Maintaining and monitoring an organization's overall PCI DSS compliance includes identifying activities to be performed daily, weekly, monthly, every three months, or annually, and ensuring these activities are being performed accordingly (for example, using a security self-assessment or PDCA methodology)
**Guidance - Examples:** Methodologies that support the management of compliance programs include Plan-Do-Check-Act (PDCA), ISO 27001, COBIT, DMAIC, and Six Sigma

---
**Sub-appendix:** `A3.1.3`
**Defined Approach Requirements:** PCI DSS compliance roles and responsibilities are specifically defined and formally assigned to one or more personnel, including: 
• Managing PCI DSS business-as-usual activities. 
• Managing annual PCI DSS assessments. 
• Managing continuous validation of PCI DSS requirements (for example, daily, weekly, every three months, as applicable per the requirement). 
• Managing business-impact analysis to determine potential PCI DSS impacts for strategic business decisions. 
PCI DSS Reference : Requirement 12 
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Defined Approach Testing Procedures:**
- `A3.1.3.a`: Examine information security policies and procedures and interview personnel to verify that PCI DSS compliance roles and responsibilities are specifically defined and formally assigned to one or more personnel in accordance with all elements of this requirement.
- `A3.1.3.b`: Interview responsible personnel and verify they are familiar with and performing their designated PCI DSS compliance responsibilities.
**Guidance - Purpose:** The formal definition of specific PCI DSS compliance roles and responsibilities helps to ensure accountability and monitoring of ongoing PCI DSS compliance efforts
**Guidance - Good Practice:** Ownership should be assigned to individuals with the authority to make risk-based decisions, and upon whom accountability rests for the specific function. Duties should be formally defined, and owners should be able to demonstrate an understanding of their responsibilities and accountability. Compliance roles may be assigned to a single owner or multiple owners for different requirement elements