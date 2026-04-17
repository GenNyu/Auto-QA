# Secure Development Management - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Secure Development Management**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 25
- **Phân loại (Category):** Secure Development Management

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Does your organization perform in-house development on any systems where Manulife/John Hancock data will be processed?
### Answer:
No

---
### Question:
Does your organization have a version control management process to restrict changes to the production environment?
### Answer:
Yes

---
### Question:
Is the user access to the version control system approved by the System Owner/Application Owner prior to access being provisioned?
### Answer:
Yes

---
### Question:
How frequently is a review performed to identify any inappropriate access within the version control system?
### Answer:
Quarterly

---
### Question:
Is production data masked or desensitised when used in non-production environments?
### Answer:
Yes

---
### Question:
Are controls in place to prevent unauthorized access to systems, applications and program source code to ensure development of software and systems is managed throughout their lifecycle?
### Answer:
Yes

---
### Question:
As part of application functionality testing, do development teams document the results of their testing within the system of record and ensure application specific security controls are functioning as designed, and that critical, high and medium issues are identified and remediated prior to moving to production?
### Answer:
Yes

---
### Question:
Does your organization maintain a formal Systems Development Life Cycle (SDLC) methodology that governs the development, acquisition, implementation, and maintenance of information systems, related technology, and infrastructure?
### Answer:
Yes

---
### Question:
In the design of projects or major changes, does your organization conduct security architecture reviews of threat modeling exercises to identify new risks that a system may introduce to the environment?
### Answer:
Yes

---
### Question:
For application development, are security code reviews conducted to identify malicious code or code flaws?
a. Are these reviews conducted manually or are they automated (dynamic code scanning and static code scanning) by a solution? 
b. What is the process of remediating any findings resulting from these code reviews?
### Answer:
Yes

---
### Question:
Are these reviews conducted manually or are they automated (dynamic code scanning and static code scanning) by a solution?
### Answer:
Manual

---
### Question:
What is the process of remediating any findings resulting from these code reviews?
### Answer:
When an issue is found, we will create an issue on Jira to manage

---
### Question:
Are all development and testing activities conducted within a non-production environment that is logically or physically segregated from production?
### Answer:
Yes

---
### Question:
Who is responsible for deploying projects or changes to production?
### Answer:
DevOps

---
### Question:
Is security testing (e.g., vulnerability scanning, application penetration testing, configuration reviews), conducted on all projects and major changes prior to deployment?
### Answer:
Yes

---
### Question:
Is access to source code libraries restricted to personnel who have a strict business need?
### Answer:
Yes

---
### Question:
Are version control histories enabled to allow for rollback capabilities?
### Answer:
Yes

---
### Question:
Do Application owners review access to program source code?
### Answer:
Yes

---
### Question:
How frequently are reviews of program source code performed?
### Answer:
Monthly

---
### Question:
Is there a change management policy/procedure in place?
### Answer:
Yes

---
### Question:
Does your organization follow a formal change and release management process for security configuration management for all network hardware and software assets on its networks?
### Answer:
Yes

---
### Question:
Is there an emergency change procedure in place for when required?
### Answer:
Yes

---
### Question:
Is there a process in place to migrate from testing and eventually to production?
### Answer:
Yes

---
### Question:
Are users who develop changes different from users who migrate to production?
### Answer:
No

---
### Question:
Are back-out plans documented as part of change management procedures?
### Answer:
Yes