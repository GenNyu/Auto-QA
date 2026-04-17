### A. Tài liệu gốc của Requirement 12

### B. Summary Overview của Control Objective 12.7
Tài liệu này mô tả chi tiết **Control Objective 12.7 **của **Requirement 12 **trong **PCI-DSS v4.0.1**, tập trung vào việc sàng lọc nhân sự trước khi cấp quyền truy cập vào CDE.
Mục tiêu chính là giảm thiểu rủi ro từ nội bộ bằng cách đảm bảo nhân sự có quyền truy cập vào hệ thống và dữ liệu thẻ đã được đánh giá phù hợp trước khi tuyển dụng.
Gồm 1 sub-requirement chính:
- 12.7.1: Sàng lọc nhân sự trước khi cấp quyền truy cập CDE
Áp dụng cho các vị trí có quyền truy cập vào CDE.

### C. Key Points của Control Objective 12.7
- **Phạm vi áp dụng:** Nhân sự có quyền truy cập vào CDE
- **Trách nhiệm:** Tài liệu hóa và thực hiện quy trình screening
- **Sàng lọc:**Thực hiện trước khi tuyển dụng (pre-employment screening)
- **Tuân thủ pháp lý:**Thực hiện trong phạm vi luật địa phương
- **Đánh giá rủi ro:**Mức độ screening phù hợp với vai trò và quyền truy cập
- **Áp dụng thực tế:** Có thể áp dụng khi chuyển vai trò nội bộ

### D. Deep Summary của Control Objective 12.7
**Bối cảnh:**
Nhân sự nội bộ có quyền truy cập vào hệ thống là một trong những nguồn rủi ro lớn nếu không được kiểm soát và đánh giá trước.
**Nội dung cốt lõi:**
- Thực hiện screening nhân sự trước khi tuyển dụng cho các vị trí có truy cập CDE
- Đánh giá thông tin như lịch sử làm việc, tham chiếu, hồ sơ công khai
- Áp dụng mức độ screening phù hợp với vai trò và quyền hạn
- Tuân thủ quy định pháp luật địa phương khi thực hiện
- Có thể áp dụng lại screening khi nhân sự chuyển sang vị trí nhạy cảm hơn
**Dữ liệu đáng chú ý:**
- Áp dụng cho vị trí có truy cập CDE (không bắt buộc với vai trò rất hạn chế)
- Screening có thể bao gồm background check, reference check
**Rủi ro / Lưu ý:**
- Không screening → tăng nguy cơ insider threat
- Screening không phù hợp → bỏ sót rủi ro nhân sự
- Không tuân thủ pháp lý → vi phạm luật địa phương
- Không đánh giá theo role → áp dụng kiểm soát không hiệu quả

### E. Structured Output của Control Objective 12.7
**Control objectives:**12.7
**Sub-requirement:**12.7.1
**Defined Approach Requirements:**Potential personnel who will have access to the CDE are screened, within the constraints of local laws, prior to hire to minimize the risk of attacks from internal sources.
**Defined Approach Testing Procedures:**Interview responsible Human Resource department management to verify that screening is conducted, within the constraints of local laws, prior to hiring potential personnel who will have access to the CDE.
**Customized Approach Objective:**The risk related to allowing new members of staff access to the CDE is understood and managed.
**Applicability Notes:**For those potential personnel to be hired for positions such as store cashiers, who only have access to one card number at a time when facilitating a transaction, this requirement is a recommendation only.
**Guidance - Purpose:**Performing thorough screening prior to hiring potential personnel who are expected to be given access to the CDE provides entities with the information necessary to make informed risk decisions regarding personnel they hire that will have access to the CDE. Other benefits of screening potential personnel include helping to ensure workplace safety and confirming information provided by prospective employees on their resumes.
**Guidance - Good Practice:**Entities should consider screening for existing personnel anytime they transfer into roles where they have access to the CDE from roles where they did not have this access. To be effective, the level of screening should be appropriate for the position. For example, positions requiring greater responsibility or that have administrative access to critical data or systems may warrant more detailed or more frequent screening than positions with less responsibility and access.
**Guidance - Examples:**Screening options can include, as appropriate for the entity's region, previous employment history, review of public information/social media resources, criminal record, credit history, and reference checks.