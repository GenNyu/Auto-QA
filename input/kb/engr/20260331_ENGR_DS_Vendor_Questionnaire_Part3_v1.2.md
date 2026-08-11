# Vendor Questionnaire Part 3 - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Vendor Questionnaire**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 13
- **Phân loại (Category):** Vendor Questionnaire

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Do you store backups on disks, tapes, or other kinds of removable media?
### Answer:
we only store backup data on Cloud AWS in 2 places, Singapore and Tokyo

---
### Question:
Are unique user IDs required for all users?
### Answer:
unique user IDs are required for all users within our organization. Each user is identified by a distinct identifier, helping to prevent unauthorized access and track individual actions on our systems.

---
### Question:
Are complex passwords required for all users?
### Answer:
complex passwords are required for all users within our organization. Requiring complex passwords—ones that include a combination of upper and lower case letters, numbers, and special characters

---
### Question:
How often are passwords changed?
### Answer:
90 days

---
### Question:
Does your organization authenticate user access with multi factors authentication?
### Answer:
UrBox uses multi-factor authentication (MFA) to authenticate users' access to critical systems. We only use SMS OTP for multi-factor authentication.

---
### Question:
Does your organization immediately removes, or modifies access, when personnel terminate, transfer, or change job functions.
### Answer:
UrBox has a well-defined process in place to immediately remove or modify access when personnel terminate, transfer, or change job functions. This process ensures that access rights are promptly revoked or adjusted based on changes in an employee's status or role within the organization.

---
### Question:
Does your organization ensure that critical data, or systems, are accessible by at least two trusted and authorised individuals, in order to limit having a single point of service failure?
### Answer:
our organization follows a policy to ensure that critical data and systems are accessible by at least two trusted and authorized individuals. This practice is implemented to prevent a single point of failure and enhance the resilience of our operations.

---
### Question:
Does your organization ensure that users have the authority to only read or modify those programs, or data, which are needed to perform their duties?
### Answer:
our organization implements a principle of least privilege to ensure that users are granted authority only to read or modify programs and data that are necessary for them to perform their designated duties.

---
### Question:
Does your organization implement privileged accounts management best practices (using privileged accounts management software, monitoring of privileges usage, record and audit, periodically review..)
### Answer:
UrBox follows privileged accounts management best practices to ensure the security and integrity of our systems. We monitor the usage of these accounts, keeping records and conducting audits to track activities and detect any unusual behavior. Periodic reviews are also conducted to ensure that access to privileged accounts remains appropriate and necessary.

---
### Question:
Does your organization implement least privilege and need to know principle?
### Answer:
our organization implements the least privilege and need to know principles as fundamental components of our access control strategy

---
### Question:
Does your organization follow separation of duties principles?
### Answer:
UrBox follows the separation of duties (SoD) principle to enhance security and prevent conflicts of interest. This principle involves distributing tasks and responsibilities among different individuals to ensure that no single person has control over all aspects of a critical process.

---
### Question:
What is the time frame that access is revoked for terminated employees or contractors? (choose from drop list)
### Answer:
within 24 hours

---
### Question:
Does your organization implement the Software Development Lifecycle policy?
### Answer:
UrBox  implements a Software Development Lifecycle (SDLC) policy. The SDLC policy outlines the processes and guidelines that our development teams follow when creating, testing, deploying, and maintaining software applications. This policy ensures that software is developed in a structured and secure manner, with considerations for quality assurance, security testing, and adherence to coding standards. The SDLC policy helps us produce reliable, secure, and well-maintained software applications that meet the needs of our users and stakeholders.