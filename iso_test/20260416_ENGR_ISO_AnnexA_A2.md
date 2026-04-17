### A. Tài liệu gốc của Phụ lục A1

### B. Summary Overview của Phụ lục A2
Tài liệu này mô tả chi tiết mục **Phụ lục A.2.Organizational views (Annex A.2)** của **ISO/IEC 27002:2022**, tập trung vào việc **hướng dẫn tổ chức thiết lập và tùy chỉnh các thuộc tính (attributes) riêng biệt để đáp ứng nhu cầu quản trị đặc thù**. 
Mục tiêu là **tối ưu hóa quy trình xử lý rủi ro bằng cách tạo ra các góc nhìn linh hoạt, giúp kết nối trực tiếp các biện pháp kiểm soát với bối cảnh thực tế của doanh nghiệp**.
Gồm **04 bước thực thi** chính:
- **Xác định nhu cầu:** Hiểu rõ tại sao cần thuộc tính tùy chỉnh (ví dụ: phục vụ kế hoạch xử lý rủi ro).
- **Định nghĩa giá trị:** Thiết lập các giá trị cụ thể cho thuộc tính (ví dụ: các loại sự cố E1-E9).
- **Ánh xạ dữ liệu:** Gán các giá trị thuộc tính vào danh mục kiểm soát trong cơ sở dữ liệu hoặc bảng tính.
- **Trích xuất thông tin:** Thực hiện truy vấn hoặc sắp xếp để tạo ra báo cáo/góc nhìn cần thiết.

Áp dụng cho **các tổ chức đang vận hành ISMS theo ISO/IEC 27001 muốn tăng cường tính hiệu quả của kế hoạch xử lý rủi ro và báo cáo tuân thủ nội bộ**.

### C. Key Points của Phụ lục A2
- **Quyền tùy biến Metadata:** Tổ chức không bắt buộc phải theo mẫu của tiêu chuẩn mà có thể loại bỏ hoặc thay thế các thuộc tính mặc định bằng các thuộc tính phù hợp với mô hình kinh doanh riêng.
- **Liên kết chặt chẽ với rủi ro:** Thuộc tính tùy chỉnh giúp đẩy nhanh việc đối chiếu các biện pháp kiểm soát "cần thiết" (necessary controls) với Phụ lục A của ISO 27001, đảm bảo không có lỗ hổng kiểm soát nào bị bỏ sót trong kế hoạch xử lý rủi ro.
- **Quản lý trạng thái vận hành:** Cần bổ sung các thuộc tính về **trạng thái triển khai** (chưa làm, đang làm, hoàn thành) và **mức độ ưu tiên** để phục vụ việc theo dõi tiến độ tuân thủ thực tế.
- **Định danh theo sự cố (Event-based):** Khuyến nghị gắn các biện pháp kiểm soát với các kịch bản rủi ro cụ thể (ví dụ: hacking, gian lận, mất thiết bị) để đánh giá trực tiếp khả năng phòng vệ trước từng loại mối đe dọa.
- **Tích hợp đa khung (Multi-framework):** Sử dụng thuộc tính để đánh dấu sự tương thích với các tiêu chuẩn khác mà tổ chức đang áp dụng, giúp giảm chồng chéo trong công tác audit.

### D. Deep Summary của Phụ lục A2
**Bối cảnh:**
Annex A.2 thừa nhận rằng một hệ thống phân loại cố định không thể phản ánh hết độ phức tạp của mọi tổ chức. Đây là phần "mở" của tiêu chuẩn, cho phép biến danh sách các biện pháp kiểm soát thành một công cụ quản trị động (dynamic management tool) thay vì chỉ là một tài liệu tham khảo tĩnh.

**Nội dung cốt lõi:**
Trọng tâm là quy trình chuyển đổi từ yêu cầu rủi ro sang thực thi kiểm soát thông qua 4 bước cấu trúc hóa dữ liệu. Việc sử dụng các công cụ như spreadsheet hoặc database là bắt buộc để có thể thực hiện "query" (truy vấn) các góc nhìn khác nhau, ví dụ: "Hiển thị tất cả các control giúp chống lại tấn công Social Engineering".

**Dữ liệu đáng chú ý:**
- **9 loại sự cố mẫu:** Từ mất thiết bị, hỏa hoạn, gian lận đến tấn công mạng và kỹ thuật xã hội.
- **Các nhóm thuộc tính quản trị mở rộng:** Bao gồm độ chín (maturity), các khu vực tổ chức liên quan (HR, IT, Ban giám đốc), tài sản liên quan, và phân tách giữa giai đoạn xây dựng (build) và vận hành (run).

**Rủi ro / Lưu ý:**
- **Rủi ro fail audit:** Nếu tổ chức không xây dựng được "Organizational views", việc giải trình với Auditor về tính phù hợp của các biện pháp kiểm soát đã chọn trong SoA (Statement of Applicability) sẽ trở nên thiếu thuyết phục và khó chứng minh tính hệ thống.
- **Lưu ý thực thi:** Việc tạo ra quá nhiều thuộc tính mà không có mục đích rõ ràng sẽ gây lãng phí nguồn lực quản trị. Auditor sẽ tập trung kiểm tra xem các thuộc tính này có thực sự giúp tổ chức "đảm bảo không bỏ sót biện pháp kiểm soát cần thiết" hay không.
- **Tính nhất quán:** Khi tùy chỉnh thuộc tính, phải đảm bảo mọi thành viên trong tổ chức có cùng một cách hiểu về các giá trị đã định nghĩa để tránh sai lệch trong báo cáo tình trạng tuân thủ.

### E. Structured Output của Phụ lục A2
Since attributes are used to create different views of controls, organizations can discard the examples of attributes proposed in this document and create their own attributes with different values to address specific needs in the organization. In addition, the values assigned to each attribute can differ between organizations since organizations can have different views on the use or applicability of the control or of the values associated to the attribute (when the values are specific to the context of the organization). The first step is to understand why an organizational-specific attribute is desirable. For example, if an organization has constructed its risk treatment plans [see ISO/IEC 27001:2013, 6.1.3 e)] based on events, it can wish to associate a risk scenario attribute to each control in this document.

The benefit of such an attribute is to speed up the process of fulfilment of ISO/IEC 27001 requirement related to risk treatment, which is to compare the controls determined through the process of risk treatment (referred to as “necessary” controls), with those in ISO/IEC 27001:2013, Annex A (which are issued from in this document) to ensure that no necessary control has been overlooked.

Once the purpose and benefits are known, the next step is to determine the attribute values. For example, the organization might identify 9 events:
1) loss or theft of mobile device;
2) loss or theft from organization’s premises;
3) force majeure, vandalism and terrorism;
4) failure of software, hardware, power, internet and communications;
5) fraud;
6) hacking;
7) disclosure;
8) breach of the law;
9) social engineering.

The second step can therefore be accomplished by assigning identifiers to each event (e.g. E1, E2, ..., E9).
The third step is to copy the control identifiers and control names from this document into a spreadsheet or database and associate the attribute values with each control, remembering that each control can have more than one attribute value.
The final step is to sort the spreadsheet or query the database to extract the required information.

Other examples of organizational attributes (and possible values) include:
a) maturity (values from the ISO/IEC 33000 series or other maturity models);
b) implementation state (to do, in progress, partially implemented, fully implemented);
c) priority (1, 2, 3, etc.);
d) organizational areas involved (security, ICT, human resources, top management, etc.);
e) events;
f) assets involved;
e) build and run, to differentiate controls used in the different steps of the service life cycle;
g) other frameworks the organization works with or can be transitioning from.