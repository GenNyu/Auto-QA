### A. Tài liệu gốc của Chapter 6

### B. Summary Overview của Chapter 6
Tài liệu này mô tả chi tiết **Chapter 6** trong **PCI-DSS v4.0.1**, tập trung vào việc hướng dẫn các kiểm toán viên sử dụng phương pháp **lấy mẫu (sampling)** trong quá trình đánh giá tuân thủ
Mục tiêu chính là tạo điều kiện thuận lợi cho việc đánh giá các môi trường có số lượng lớn các thành phần hệ thống hoặc nhân sự, đảm bảo kiểm toán viên thu thập đủ bằng chứng hợp lý để kết luận về tính hiệu quả và nhất quán của các biện pháp kiểm soát bảo mật

### C. Key Points của Chapter 6
- **Đặc quyền của kiểm toán viên:** Lấy mẫu là một lựa chọn dành riêng cho kiểm toán viên để tối ưu hóa quy trình đánh giá, không phải là phương pháp để thực thể áp dụng nhằm đáp ứng các yêu cầu của tiêu chuẩn
- **Tính độc lập:** Kiểm toán viên phải tự mình lựa chọn mẫu một cách độc lập mà không chịu sự can thiệp hay ảnh hưởng từ thực thể được đánh giá
- **Tính đại diện:** Mẫu được chọn phải đại diện cho tất cả các biến thể trong quần thể (ví dụ: tất cả các phiên bản hệ điều hành, các vai trò nhân sự khác nhau hoặc các nền tảng ứng dụng)
- **Mối liên hệ với sự chuẩn hóa:** Mức độ chuẩn hóa trong các quy trình và biện pháp kiểm soát của thực thể sẽ quyết định quy mô mẫu: quy trình càng chuẩn hóa thì mẫu có thể càng nhỏ và ngược lại
- **Nghĩa vụ chứng minh:** Kiểm toán viên phải ghi lại kết quả thử nghiệm và giải trình chi tiết về kỹ thuật lấy mẫu cũng như lý do chọn quy mô mẫu đó trong Báo cáo Tuân thủ (ROC)

### D. Deep Summary của Chapter 6
**Bối cảnh:**
Trong các môi trường lớn và phức tạp, việc kiểm tra 100% mọi thành phần là không khả thi. Lấy mẫu cho phép kiểm toán viên kiểm tra một phần nhưng vẫn đảm bảo có được cơ sở chuyên môn vững chắc cho ý kiến đánh giá của mình

**Nội dung cốt lõi:**
Quy trình lấy mẫu được xác định qua 3 kịch bản chính dựa trên mức độ chuẩn hóa của thực thể,:
1.  **Một bộ quy trình chuẩn duy nhất:** Áp dụng cho toàn bộ quần thể, cho phép chọn mẫu nhỏ
2.  **Nhiều bộ quy trình chuẩn khác nhau:** Áp dụng cho từng phần của quần thể, yêu cầu mẫu lớn hơn đại diện cho từng nhóm
3.  **Không có quy trình chuẩn:** Từng đối tượng được quản lý riêng lẻ, yêu cầu quy mô mẫu lớn nhất để bao quát mọi biến thể

**Dữ liệu đáng chú ý:**
- **Quy mô mẫu tối thiểu:** Phải luôn lớn hơn 1, trừ khi quần thể chỉ có duy nhất một đối tượng hoặc biện pháp kiểm soát tự động đã được xác nhận hoạt động đúng như lập trình cho toàn bộ quần thể
- **Tính thay đổi:** Kiểm toán viên không được chọn lại cùng một bộ mẫu qua các năm để tránh bỏ sót các biến thể không được lấy mẫu trong quá khứ

**Rủi ro / Lưu ý:**
- **Giới hạn áp dụng:** Thực thể không được phép tự ý lấy mẫu để thực hiện các yêu cầu định kỳ (ví dụ: quét lỗ hổng hàng quý phải thực hiện trên 100% thành phần hệ thống, không được lấy mẫu)
- **Điều chỉnh mẫu:** Nếu trong quá trình kiểm tra, kiểm toán viên nhận thấy các quy trình chuẩn hóa không hoạt động hiệu quả như mong đợi, họ phải tăng ngay quy mô mẫu để đảm bảo tính xác thực
- **Ưu tiên tự động hóa:** PCI SSC khuyến khích sử dụng các quy trình tự động để kiểm tra toàn bộ quần thể nếu có thể, lấy mẫu chỉ là phương án thay thế khi các công cụ này không sẵn có

### E. Structured Output của Chapter 6
Sampling is an option for assessors conducting PCI DSS assessments to facilitate the assessment process when there are large numbers of items in a population being tested.

While it is acceptable for an assessor to sample from similar items in a population being tested as part of its review of an entity’s PCI DSS compliance, it is not acceptable for an entity to apply PCI DSS requirements to only a sample of its environment (for example, requirements for quarterly vulnerability scans apply to all system components). Similarly, it is not acceptable for an assessor to review only a sample of PCI DSS requirements for compliance.

While sampling allows assessors to test less than 100% of a given sampling population, assessors should always strive for the most complete review possible. Assessors are encouraged to use automated processes or other mechanisms if the complete population, regardless of size, can be tested quickly and efficiently with minimal impact on the resources of the entity being assessed. Where automated processes are not available to test 100% of a population, sampling is an equally acceptable approach.

After considering the overall scope, complexity, and consistency of the environment being assessed, and the nature (automated or manual) of the processes used by an entity to meet a requirement, the assessor may independently select representative samples from the populations being reviewed in order to assess the entity’s compliance with PCI DSS requirements. Samples must be a representative selection of all variants of the population and must be sufficiently large to provide the assessor with assurance that controls are implemented as expected across the entire population. Where testing the periodic performance of a requirement (for example, weekly or quarterly, or periodically), the assessor should attempt to select a sample that represents the entire period covered by the assessment so that the assessor may make a reasonable judgment that the requirement was met throughout the assessment period. Testing the same sample of items year after year could allow unknown variations in the non-sampled items to remain undetected. Assessors must revalidate the sampling rationale for each assessment and consider previous sample sets. Different samples must be selected for each assessment.

Appropriate selection of the sample depends on what is being considered in examining the sample members. For example, determining the presence of anti-malware on servers known to be affected by malicious software may lead to determining the population to be all servers in the environment, or all servers in the environment that are running a particular operating system, or all servers that are not mainframes, etc. Selection of an appropriate sample would then include representatives of ALL members of the identified population, including all servers running the identified operating system including all versions, as well as servers within the population that are used for different functions (for example, web servers, application servers, and database servers).

In the case that a specific configuration item is being considered, the population might be appropriately divided, and separate sample groups identified. For example, a sample of all servers may not be appropriate when reviewing an operating system configuration setting, where different operating systems are present within the environment. In this case, samples from each operating system type would be appropriate in identifying that the configuration has been appropriately set for each operating system. Each sample set should include servers that are representative of each operating system type, including version, as well as representative functions.

Other examples of sampling include selections of personnel with similar or varied roles, based on the requirement being assessed, for example, a sample of administrators vs. a sample of all employees.

The assessor is required to use professional judgment in the planning, performance, and evaluation of the sample to support their conclusion about whether and how the entity has met a requirement. The assessor’s goal in sampling is to obtain enough evidence to have a reasonable basis for their opinion. When independently selecting samples, assessors should consider the following:

- The assessor must select the sample from the complete population without influence from the assessed entity.
- If the entity has standardized processes and controls in place that ensure consistency and which is applied to each item in the population, the sample can be smaller than if the entity has no standardized processes/controls in place. The sample must be large enough to provide the assessor with reasonable assurance that items in the population adhere to the standardized processes that are applied to each item in the population. The assessor must verify that the standardized controls are implemented and working effectively.
- If the entity has more than one type of standardized process in place (for example, for different types of business facilities/system components), the sample must include items subject to each type of process. For example, populations could be divided into sub-populations based on characteristics that may impact the consistency of the assessed requirements, such as the use of different processes or tools. Samples would then be selected from each sub-population.
- If the entity has no standardized PCI DSS processes/controls in place and each item in the population is managed through non-standardized processes, the sample must be larger for the assessor to be assured that the PCI DSS requirements are appropriately applied to each item in the population.
- Samples of system components must include every type and combination being used. When an entity has more than one CDE, samples must include populations across all in-scope system components. For example, where applications are sampled, the sample must include all versions and platforms for each type of application.
- Sample sizes must always be greater than one unless there is only one item in the given population, or an automated control is used where the assessor has confirmed the control is functioning as programmed for each assessed sample population.
- If the assessor relies on standardized processes and controls being in place as a basis for selecting a sample, but then finds out during testing that standardized processes and controls are not in place or not operating effectively, the assessor should then increase the sample size to attempt to gain assurance that PCI DSS requirements are being met.

For each instance where sampling is used, the assessor must:
- Document the rationale behind the sampling technique and sample size.
- Validate and document the standardized processes and controls used to determine sample size.
- Explain how the sample is appropriate and representative of the overall population.

#### [Figure 3. PCI DSS Sampling Considerations]
[Figure 3. PCI DSS Sampling Considerations][https://drive.google.com/file/d/15RNonO3vy1b9CbmZ6qsdZMQ-qVH_8d5Z/view?usp=sharing]

**Mục tiêu**
Xác định cách chọn **sample (mẫu kiểm tra)** sao cho đại diện cho toàn bộ hệ thống khi audit PCI DSS.

**Bước chuẩn bị**
Assessor thực hiện:
- Xác định việc entity có sử dụng **process và control chuẩn hóa** hay không  
- Xác định **tổng population (tập dữ liệu/hệ thống cần kiểm tra)**  

**Flow quyết định**
**1. Entity có dùng một bộ process/control chuẩn cho toàn bộ không?**
- Có  
  → Assessor chọn **sample nhỏ hơn** nhưng vẫn đại diện cho toàn bộ population  
- Không  
  → Chuyển sang bước 2  
**2. Entity có dùng nhiều bộ process/control khác nhau cho từng phần không?**
- Có  
  → Assessor chọn **sample lớn hơn**, đại diện cho từng nhóm có process/control khác nhau  
- Không  
  → Assessor chọn **sample lớn nhất**, bao phủ tất cả các biến thể trong population  

**Kết quả**
- Assessor phải:
  - Document kết quả test  
  - Giải thích lý do chọn sample (justification)  

**Yêu cầu bổ sung**
Assessor cần:
- Document phương pháp sampling và kích thước sample  
- Xác nhận các process/control được chuẩn hóa  
- Giải thích vì sao sample là **đại diện hợp lý cho toàn bộ population**  

**Tóm tắt**
- Process càng **đồng nhất** → sample càng **nhỏ**  
- Process càng **đa dạng** → sample càng **lớn**  
- Không chứng minh được tính đại diện → audit có thể fail  

---
**Note:** In PCI DSS v4.0, specific references to sampling have been removed from all testing procedures. These references were removed because calling out sampling only in some testing procedures may have implied that sampling was mandatory for those testing procedures (which it was not) or that sampling was only allowable where it was specifically mentioned. Assessors should select samples when it is appropriate to the population being tested, and, per above, render those decisions after considering the overall scope and complexity of an environment.
