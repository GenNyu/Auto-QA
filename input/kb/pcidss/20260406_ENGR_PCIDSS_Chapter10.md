### A. Tài liệu gốc của Chapter 10

### B. Summary Overview của Chapter 10
Tài liệu này mô tả chi tiết **Chapter 10** trong **PCI-DSS v4.0.1**, tập trung vào các **Phương pháp kiểm tra (Testing Methods)** được sử dụng trong quy trình đánh giá các yêu cầu của tiêu chuẩn.
Mục tiêu chính là định nghĩa các hoạt động mà kiểm toán viên (assessor) cần thực hiện để xác định xem một thực thể đã đáp ứng các yêu cầu bảo mật hay chưa, đồng thời tạo ra sự hiểu biết chung giữa bên được đánh giá và bên đánh giá về các hoạt động sẽ diễn ra.

### C. Key Points của Chapter 10
- **Ba phương pháp cốt lõi:** Quy trình kiểm tra dựa trên ba kỹ thuật chính: **Kiểm tra tài liệu (Examine)**, **Quan sát (Observe)** và **Phỏng vấn (Interview)**.
- **Tính linh hoạt theo thực tế:** Các đối tượng cụ thể cần kiểm tra, quan sát hoặc nhân sự cần phỏng vấn phải phù hợp với cả yêu cầu đang được đánh giá và cách thức triển khai riêng biệt của từng thực thể.
- **Mục đích minh chứng:** Các phương pháp này được thiết kế để cho phép thực thể được đánh giá có cơ hội chứng minh cách họ đã đáp ứng một yêu cầu cụ thể như thế nào.
- **Yêu cầu về ghi chép:** Khi ghi lại kết quả đánh giá, kiểm toán viên phải xác định rõ các hoạt động kiểm tra đã thực hiện và kết quả của từng hoạt động đó.

### D. Deep Summary của Chapter 10
**Bối cảnh:**
Mỗi yêu cầu trong PCI DSS đều đi kèm với các quy trình kiểm tra cụ thể. Chapter 10 đóng vai trò là "bộ từ điển" giải thích ý nghĩa và mục đích đằng sau các hành động mà kiểm toán viên sẽ thực hiện trong môi trường của doanh nghiệp.

**Nội dung cốt lõi:**
Chương này phân tích chi tiết ý định của từng phương pháp kiểm tra:
1.  **Examine (Kiểm tra):** Kiểm toán viên đánh giá một cách nghiêm túc các bằng chứng dữ liệu. Các ví dụ phổ biến bao gồm tài liệu (giấy hoặc điện tử), ảnh chụp màn hình, tệp cấu hình, nhật ký hệ thống (audit logs) và các tệp dữ liệu.
2.  **Observe (Quan sát):** Kiểm toán viên xem xét một hành động hoặc quan sát trực tiếp các thành phần trong môi trường. Đối tượng quan sát có thể là nhân viên đang thực hiện một nhiệm vụ, các thành phần hệ thống đang phản hồi đầu vào, hoặc các điều kiện môi trường và biện pháp kiểm soát vật lý.
3.  **Interview (Phỏng vấn):** Kiểm toán viên trò chuyện với nhân sự để xác nhận xem một hoạt động có được thực hiện hay không, cách thức thực hiện và kiểm tra xem nhân viên có kiến thức hoặc sự hiểu biết cụ thể về quy trình đó hay không.

**Dữ liệu đáng chú ý:**
- **Bằng chứng dữ liệu:** Bao gồm cấu hình hệ thống, nhật ký kiểm toán và các bằng chứng điện tử khác mà kiểm toán viên sẽ "critically evaluate" (đánh giá nghiêm túc).
- **Tính xác thực:** Phương pháp phỏng vấn không chỉ để nghe mô tả mà còn để xác nhận nhận thức (understanding) của nhân sự về bảo mật.

**Rủi ro / Lưu ý:**
- **Sự phối hợp:** Việc thiếu hiểu biết chung về các phương pháp này có thể dẫn đến sự nhầm lẫn giữa thực thể và kiểm toán viên về những hoạt động đánh giá cần thực hiện.
- **Tính chính xác của báo cáo:** Kiểm toán viên có trách nhiệm phải nhận diện và ghi lại chính xác từng hoạt động thử nghiệm đã thực hiện cùng kết quả tương ứng trong hồ sơ đánh giá.

### E. Structured Output của Chapter 10
The testing methods identified in the Testing Procedures for each requirement describe the expected activities to be performed by the assessor to determine whether the entity has met the requirement. The intent behind each testing method is described as follows:

- Examine: The assessor critically evaluates data evidence. Common examples include documents (electronic or physical), screenshots, configuration files, audit logs, and data files.
- Observe: The assessor watches an action or views something in the environment. Examples of observation subjects include personnel performing a task or process, system components performing a function or responding to input, environmental conditions, and physical controls.
- Interview: The assessor converses with individual personnel. Interview objectives may include confirmation of whether an activity is performed, descriptions of how an activity is performed, and whether personnel have particular knowledge or understanding.

The testing methods are intended to allow the assessed entity to demonstrate how they have met a requirement. They also provide the assessed entity and the assessor with a common understanding of the assessment activities to be performed. The specific items to be examined or observed and personnel to be interviewed should be appropriate for both the requirement being assessed and each entity’s particular implementation. When documenting the assessment results, the assessor identifies the testing activities performed and the result of each activity.