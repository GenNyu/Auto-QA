# Data input/output validation - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Data input/output validation**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 11
- **Phân loại (Category):** Data input/output validation

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
All input data must be validated to ensure following the design document:
- Data Type
- Format
- Length
And reject all in-correct data
### Answer:
Yes

---
### Question:
System provide keyword filter mechanisms: such as SQL queries, XML,HTML Tag, javascript, special characters: < > - : ; ` ' " % 0xff 0x00 0x \ / ( ) * $ & 0x0a 0x0d … Describe in detail.
### Answer:
Yes

---
### Question:
System must have machanism to prevent CSRF attack: CSRF token…
### Answer:
Not relevant

---
### Question:
System can validate file upload to ensure following:
- File type
- File Capacity
- File content, format
### Answer:
not relevant, There is no file uploading

---
### Question:
System must setup captcha or other method to prevent flood submit.
### Answer:
Yes

---
### Question:
System must have machanism to prevent data manipulation attack
### Answer:
RSA with signature

---
### Question:
Validation mechanism must be performed at both client side and server side
### Answer:
Yes

---
### Question:
The output data must be Sanitize, HTML encode
### Answer:
Output

---
### Question:
System must support masking sensitive information.
### Answer:
Not relevant

---
### Question:
Bank admin can define to mask any sesitive field as Card number, account number …
### Answer:
Not relevant

---
### Question:
The error message need converting to meaningful for end-user. The information in error message should be generalized.The message is not allowed to identify account name or password clearly.
### Answer:
Yes