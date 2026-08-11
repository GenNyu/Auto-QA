# Logging: the system must log all activities: - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Logging: the system must log all activities:**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 8
- **Phân loại (Category):** Logging: the system must log all activities:

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Authetication(successful, unsuccessful)
### Answer:
Yes

---
### Question:
All update, change, lock/unlock, add new, delete, access right of account
### Answer:
Yes

---
### Question:
All trassactions, user activities.
### Answer:
Yes

---
### Question:
All update, change in Config, Source code.
### Answer:
Yes

---
### Question:
Each log record must include:
- Action timestamp
- User
- IP ( Direclty IP or thought Reverse Proxy IP)
- URL
- Action detail
- Action status
-Event ID
-Event Category
### Answer:
Hệ thống Log Urbox đang lưu trữ các log record bao gồm :
- Action Timestamp
- User
- IP
- URL
- Action Detail
- Action Status
- Request ID ( Event ID )

---
### Question:
Don't store or masked or tokenize all PII, PAN card information and other sensitive information (Password, OTP ...) in log
### Answer:
Yes

---
### Question:
All configure which information will be masked or tokenize
### Answer:
Yes

---
### Question:
Support integrate with SIEM IBM Qradar
### Answer:
Not Support