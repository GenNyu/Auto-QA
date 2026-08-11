### A. Tài liệu gốc của Requirement 7

### B. Summary Overview của Control Objective 7.3
Tài liệu này mô tả chi tiết **Control Objective 7.3 **của **Requirement 7** trong **PCI-DSS v4.0.1**, tập trung vào việc triển khai và cấu hình hệ thống kiểm soát truy cập để thực thi các quyền đã được định nghĩa.
Mục tiêu chính là đảm bảo quyền truy cập được thực thi tự động thông qua access control system, dựa trên nguyên tắc need-to-know và least privilege.
Gồm 3 sub-requirement chính:
- 7.3.1: Triển khai access control system
- 7.3.2: Thực thi quyền truy cập theo role
- 7.3.3: Cấu hình mặc định deny all
Áp dụng cho tất cả system components, user, application và hệ thống truy cập.

### C. Key Points của Control Objective 7.3
- **Phạm vi áp dụng:**Tất cả system components và cơ chế kiểm soát truy cập
- **Trách nhiệm:** Triển khai và cấu hình access control system đúng nguyên tắc
- **Kiểm soát truy cập:** Áp dụng need-to-know và least privilege
- **Thực thi quyền:** Quyền được enforce tự động qua system
- **Cấu hình mặc định:** Phải thiết lập deny all

### D. Deep Summary của Control Objective 7.3
**Bối cảnh:**
Nếu không có cơ chế tự động thực thi quyền truy cập, việc cấp quyền có thể bị sai sót hoặc bị lạm dụng, dẫn đến truy cập trái phép.
**Nội dung cốt lõi:**
- Triển khai access control system bao phủ toàn bộ system components
- Thực thi quyền truy cập dựa trên role và job function
- Đảm bảo quyền chỉ được cấp theo need-to-know
- Cấu hình mặc định deny all, chỉ cho phép khi có rule rõ ràng
**Dữ liệu đáng chú ý:**
- Access control system phải quản lý cả user, application và system account
- Quyền truy cập được kế thừa từ group/role
**Rủi ro / Lưu ý:**
- Không có access control system → khó kiểm soát truy cập
- Cấu hình allow by default → mở rộng quyền ngoài kiểm soát
- Không enforce role-based → dễ cấp sai quyền
- Không áp dụng deny all → tăng nguy cơ truy cập trái phép

### E. Structured Output của Control Objective 7.3
**Control objectives:**7.3
**Sub-requirement:**7.3.1
**Defined Approach Requirements:**An access control system(s) is in place that restricts access based on a user's need to know and covers all system components.
**Defined Approach Testing Procedures:**Examine vendor documentation and system settings to verify that access is managed for each system component via an access control system(s) that restricts access based on a user's need to know and covers all system components.
**Customized Approach Objective:**Access rights and privileges are managed via mechanisms intended for that purpose.
**Guidance - Purpose:**Without a mechanism to restrict access based on user's need to know, a user may unknowingly be granted access to cardholder data. Access control systems automate the process of restricting access and assigning privileges.

---
**Control objectives:**7.3
**Sub-requirement:**7.3.2
**Defined Approach Requirements:**The access control system(s) is configured to enforce permissions assigned to individuals, applications, and systems based on job classification and function.
**Defined Approach Testing Procedures:**Examine vendor documentation and system settings to verify that the access control system(s) is configured to enforce permissions assigned to individuals, applications, and systems based on job classification and function.
**Customized Approach Objective:**Individual account access rights and privileges to systems, applications, and data are only inherited from group membership.
**Guidance - Purpose:**Restricting privileged access with an access control system reduces the opportunity for errors in the assignment of permissions to individuals, applications, and systems.

---
**Control objectives:**7.3
**Sub-requirement:**7.3.3
**Defined Approach Requirements:**The access control system(s) is set to 'deny all' by default.
**Defined Approach Testing Procedures:**Examine vendor documentation and system settings to verify that the access control system(s) is set to 'deny all' by default.
**Customized Approach Objective:**Access rights and privileges are prohibited unless expressly permitted.
**Guidance - Purpose:**A default setting of 'deny all' ensures no one is granted access unless a rule is established specifically granting such access.
**Guidance - Good Practice:**It is important to check the default configuration of access control systems because some are set by default to 'allow all,' thereby permitting access unless/until a rule is written to specifically deny it.