# Session Management - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Session Management**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 10
- **Phân loại (Category):** Session Management

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
One user - One session at the same time. If user re-login the first session must be invalidated
### Answer:
Not relevant

---
### Question:
Bank admin can terminate any session.
### Answer:
Not relevant

---
### Question:
Automatically logout client session after the idle timeout expires.
Bank admin can setup this idle timeout.
### Answer:
Not relevant

---
### Question:
Session token must be generated random, unique, unpredictable, not depend on any factors such as user account, name , IP computer, timestamp... Describe detail.
### Answer:
Not relevant

---
### Question:
Session Token management must be managed on the server side
### Answer:
Not relevant

---
### Question:
Initiate new Session Token when user sign-in successfully
### Answer:
Not relevant

---
### Question:
Set invalid session when user sign-out or timeout.
### Answer:
Not relevant

---
### Question:
Do not allow users to set up and use fixed session token
### Answer:
Not relevant

---
### Question:
Session token is stored in Cookies only
### Answer:
Not relevant

---
### Question:
Cookie Requirements:
- Turn-on the Secure, HTTPonly,non-persistent, no-cache ...
- Don't allow to store any sensitive information: username, password, group … in any format even encoded, encrypted data.
### Answer:
Not relevant