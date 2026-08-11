### A. Tài liệu gốc của Requirement 12

### B. Summary Overview của Control Objective 12.2
Tài liệu này mô tả chi tiết **Control Objective 12.2** của **Requirement 12** trong **PCI-DSS v4.0.1**, tập trung vào việc thiết lập và quản lý chính sách sử dụng chấp nhận được đối với các công nghệ người dùng cuối.
Mục tiêu chính là đảm bảo việc sử dụng các thiết bị và công nghệ của người dùng được kiểm soát, chỉ sử dụng đúng mục đích và trong phạm vi được ủy quyền.
Gồm 1 sub-requirement chính:
- 12.2.1: Chính sách sử dụng chấp nhận được (acceptable use policy)
Áp dụng cho tất cả công nghệ người dùng cuối như laptop, mobile, email, Internet, wireless và remote access.

### C. Key Points của Control Objective 12.2
- **Phạm vi áp dụng:**Tất cả end-user technologies (device, software, network usage)
- **Trách nhiệm:**Tài liệu hóa và thực thi chính sách sử dụng
- **Kiểm soát sử dụng:**Quy định rõ các hành vi được phép và không được phép
- **Phê duyệt:** Việc sử dụng phải được phê duyệt bởi bên có thẩm quyền
- **Quản lý tài sản:**Danh sách thiết bị và phần mềm được phép sử dụng
- **Áp dụng thực tế:**Chính sách phải được triển khai và enforce

### D. Deep Summary của Control Objective 12.2
**Bối cảnh:**
Việc sử dụng công nghệ người dùng cuối không kiểm soát có thể dẫn đến rò rỉ dữ liệu, malware hoặc vi phạm chính sách bảo mật.
**Nội dung cốt lõi:**
- Xây dựng acceptable use policy cho các công nghệ người dùng
- Quy định rõ cách sử dụng đúng và sai đối với thiết bị và hệ thống
- Yêu cầu phê duyệt trước khi sử dụng công nghệ
- Duy trì danh sách thiết bị và phần mềm được phép
- Kết hợp policy với kiểm soát kỹ thuật để enforce
- Phổ biến cho người dùng để đảm bảo tuân thủ
**Dữ liệu đáng chú ý:**
- Bao gồm nhiều loại công nghệ: laptop, mobile, email, Internet, removable media
- Chính sách nên rõ ràng dạng "do / do not"
**Rủi ro / Lưu ý:**
- Sử dụng thiết bị không kiểm soát → rò rỉ dữ liệu
- Không có policy rõ ràng → người dùng sử dụng sai mục đích
- Không enforce → policy không có hiệu lực thực tế
- Thiếu phê duyệt → sử dụng công nghệ không được phép

### E. Structured Output của Control Objective 12.2
**Control objectives:**12.2
**Sub-requirement:**12.2.1
**Defined Approach Requirements:**Acceptable use policies for end-user technologies are documented and implemented, including:
• Explicit approval by authorized parties.
• Acceptable uses of the technology.
• List of products approved by the company for employee use, including hardware and software.
**Defined Approach Testing Procedures:**Examine the acceptable use policies for end-user technologies and interview responsible personnel to verify processes are documented and implemented in accordance with all elements specified in this requirement.
**Customized Approach Objective:**The use of end-user technologies is defined and managed to ensure authorized usage.
**Applicability Notes:**Examples of end-user technologies for which acceptable use policies are expected include, but are not limited to, remote access and wireless technologies, laptops, tablets, mobile phones, and removable electronic media, email usage, and Internet usage.
**Guidance - Purpose:**End-user technologies are a significant investment and may pose significant risk to an organization if not managed properly. Acceptable use policies outline the expected behavior from personnel when using the organization's information technology and reflect the organization's risk tolerance These policies instruct personnel on what they can and cannot do with company equipment and instruct personnel on correct and incorrect uses of company Internet and email resources. Such policies can legally protect an organization and allow it to act when the policies are violated.
**Guidance - Good Practice:**It is important that usage policies are supported by technical controls to manage the enforcement of the policies. Structuring polices as simple 'do' and 'do not' requirements that are linked to a purpose can help remove ambiguity and provide personnel with the context for the requirement.