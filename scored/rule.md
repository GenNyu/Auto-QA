Rule chấm điểm
Phân loại
* ENTAILED (Khớp): Dùng khi Candidate khớp về mã yêu cầu (Requirement ID) và nội dung thực tế với Gold.
    * 9-10 điểm: Khớp hoàn toàn mã yêu cầu và nội dung cốt lõi. Có bổ sung thông tin từ tài liệu tiêu chuẩn chính xác.
    * 7-8 điểm: Khớp nội dung nhưng thiếu một vài mã yêu cầu phụ, hoặc đưa thêm thông tin ngoài Gold (trừ 1-2 điểm nếu thông tin đó không có trong tiêu chuẩn).
* NOT_SUPPORTED (Không được hỗ trợ): Dùng khi hệ thống không tìm thấy dữ liệu hoặc đưa ra thông tin không liên quan.
    * 1 điểm: Candidate trả lời "không đủ dữ liệu" trong khi Gold có đáp án rõ ràng (Lỗi Retrieval).
    * 2-3 điểm: Đưa ra mã Requirement ID sai hoàn toàn so với tiêu chuẩn (Anchor Drift/Hallucination).
* CONTRADICTED (Mâu thuẫn): Dùng khi Candidate đưa ra thông tin trái ngược với Gold hoặc tiêu chuẩn.
    * 1-3 điểm: Nội dung sai lệch nghiêm trọng về mặt kỹ thuật bảo mật.

Quy tắc chấm điểm ưu tiên (Scoring Rules)
Quy tắc 1: Xác thực mã yêu cầu (Anchor Match) - Quan trọng nhất
Mã Requirement ID là "neo" pháp lý trong PCI DSS.
* Khớp hoàn toàn: Nếu mã Requirement ID (ví dụ: 1.2.1, 12.10.1) khớp với Gold và tài liệu gốc.
* Sai mã (Anchor Drift): Nếu Candidate dẫn sai mã (ví dụ: dùng mã v3.2.1 cho v4.0.1) hoặc gán nội dung của yêu cầu này cho mã kia. Điểm tối đa: 3.
* Tự chế mã (Hallucination): Nếu Candidate liệt kê các mã không tồn tại trong tài liệu tiêu chuẩn. Điểm tối đa: 2.
Quy tắc 2: Xử lý lỗi truy xuất (Retrieval Failure)
* Nếu Gold có đáp án nhưng Candidate báo "không tìm thấy thông tin" (The current knowledge base does not provide enough data...): Chấm 1 điểm và gán nhãn NOT_SUPPORTED.
Quy tắc 3: Sự thật cốt lõi (Core Facts)
* Nội dung kỹ thuật (ví dụ: "vô hiệu hóa ID ngay lập tức", "MFA cho mọi truy cập không trực tiếp") phải khớp với Gold.
* Bổ sung thông tin: Cho phép Candidate bổ sung các thông tin từ phần Guidance hoặc Good Practice của tài liệu tiêu chuẩn PCI DSS v4.0.1 nếu nó làm rõ thêm cho câu trả lời của Gold mà không làm thay đổi ý nghĩa.
Quy tắc 4: Kiểm soát kiến thức ngoài (External Knowledge)
* Trừ 1-2 điểm: Nếu Candidate tự đưa vào các con số cụ thể về thời gian (SLA) hoặc tần suất không có trong Gold (ví dụ: "vá lỗi trong 3 ngày", "phản ứng trong 24 giờ") trừ khi thông tin đó được trích xuất trực tiếp từ tài liệu tiêu chuẩn đi kèm
