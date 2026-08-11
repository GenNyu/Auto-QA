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