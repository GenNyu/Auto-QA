# Authentication - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Authentication**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 17
- **Phân loại (Category):** Authentication

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Support form-base authentication
### Answer:
No

---
### Question:
Support at least one authentication methods. Which should be included but not limited:
- Username/password authentication
- Two-Factor Authentication, which vendor support
- PKI
- Biometric
(Depend in each Biz, system Security member will select approricate authentication method)
### Answer:
TCB loads the web page through API authentication. Only TCB can get the webpage.

---
### Question:
Support mutiple factor authentication method for functions such as fund transfer, payment,…, authentication method is based-on transaction amount. 
Support authentication methods:  password, SMS OTP, software token OTP, transaction signing, PKI signning, Pushnotification authen.
### Answer:
Not relevant

---
### Question:
Bank admin can setup multiple authentication methods for each function: fund transfer, payment, change password,…
### Answer:
Not relevant

---
### Question:
Support Captcha or other method to prevent brute force attack. Pls suggest your solutions
### Answer:
Google ReCaptcha v3 Invisible

---
### Question:
Support Single Sign On. Describle detail SSO method that solution support
### Answer:
Not relevant

---
### Question:
Support authenticate bank user via Active Directory (Microsoft) with multiple domain controllers
### Answer:
Not relevant

---
### Question:
Support setup/check complexity password :
- Minimum characters
- Uppercase, lowercase
- Numeric and special characters
### Answer:
Not relevant

---
### Question:
Support setup password policy:
- Password age (by day, eg 60 days)
- Password history (by times, eg 5 time password history)
- Notify for user before password expired
### Answer:
Not relevant

---
### Question:
Support setup account policy:
- account locking after long time don't use
- account locking after continue unsuccess login
Locking time, number of continue unsuccessful login can setup by bank admin.
### Answer:
Not relevant

---
### Question:
Locked account can unlock only by Bank admin before lockout time expires
### Answer:
Not relevant

---
### Question:
Authentication must be performed on the server side
### Answer:
Not relevant

---
### Question:
Password field must be set auto-complete=off
### Answer:
Not relevant

---
### Question:
Sign-out button/function must be appear clearly
### Answer:
Not relevant

---
### Question:
Password must be hashed by SHA256 at least and include Salt or using salt supported cryptography like  scrypt, bcrypt
### Answer:
Not relevant

---
### Question:
Support setup Re-Authenticate for each change: update, edit, delete: account, business function, customer information …
### Answer:
Not relevant

---
### Question:
Support Virtual keyboard to prevent keylogger
### Answer:
Not relevant