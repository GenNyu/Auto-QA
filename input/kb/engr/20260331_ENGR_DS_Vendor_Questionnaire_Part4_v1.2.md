# Vendor Questionnaire Part 4 - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Vendor Questionnaire**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 14
- **Phân loại (Category):** Vendor Questionnaire

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Does the organization have policy in order to protect client information against unauthorized access, prohibit sharing of individual accounts and passwords, protect privileged account with the following concerps: need to know, least privilege and checks and balances
### Answer:
our company has implemented a comprehensive policy to protect client information against unauthorized access. This policy includes measures to prohibit the sharing of individual accounts and passwords. Privileged accounts are particularly safeguarded through the principles of "need to know" and "least privilege," ensuring that access is granted only to those who require it for their roles. Additionally, a system of checks and balances is in place to monitor and review privileged account usage, reducing the risk of misuse and maintaining a higher level of security.

---
### Question:
Is secure coding principle applied in your organization?
### Answer:
our company applies secure coding principles in our software development practices. Secure coding involves following established best practices to write code that is resilient to security vulnerabilities and threats. This includes practices like input validation, proper error handling, avoiding known security pitfalls, and using encryption where needed.

---
### Question:
Is access to source code managed and protected from unauthorized access?
### Answer:
access to source code is managed and protected from unauthorized access in our organization. We implement strict access controls and authentication mechanisms to ensure that only authorized individuals, such as developers and relevant team members, can access the source code. This helps prevent unauthorized modifications, data breaches, and other potential security risks associated with source code exposure. Additionally, version control systems and secure repositories are often used to further enhance source code management and protection.

---
### Question:
Are anti-malware applications installed on all systems?
### Answer:
anti-malware applications are installed on all systems within our organization.

---
### Question:
How frequent are antivirus signatures files updated?
### Answer:
Antivirus signature files are automatically updated daily.

---
### Question:
Is there a data loss prevention (DLP) tool in use?
### Answer:
Our company has not used DLP tools

---
### Question:
If the vendor provides applications as part of their service, are applications security scans conducted to ensure secure coding?
### Answer:
we will conduct application security scans to ensure secure coding.

---
### Question:
If wireless networks are used in your environment, is WPA2 encryption implemented?
### Answer:
We use WPA3 encryption

---
### Question:
Is all in transit data encrypted?
### Answer:
all in-transit data is encrypted within our organization. We use TLS 1.2 (Transport Layer Security) for web communications and secure VPN connections for remote access.

---
### Question:
Is sensitive data encrypted at rest?
### Answer:
Yes, sensitive data is encrypted at rest with SHA encryption

---
### Question:
Is full-disk encryption implemented on laptops?
### Answer:
we use bitlocker encryption for windows computers and File Vault for MacOS

---
### Question:
Are operating system and application patches implemented as per your policy
### Answer:
We follows a structured process to test and apply patches in a timely manner, ensuring that systems remain protected against the latest security threats.

---
### Question:
Do you have users who save sensitive data on their local hard drives or removable media?
### Answer:
Our sensitive data is only stored on cloud servers, we strictly prohibit the act of storing sensitive data on hard drives or removable media

---
### Question:
Does your organization implement system event logging on all servers and records at a  minimum who, what, and when for all transaction?
### Answer:
We implements system event logging on all servers and records, at a minimum, the "who, what, and when" for all transactions. We use ElasticSearch, Cloudtrail, GuardDuty to record logs system. By capturing information about who performed actions, what actions were taken, and when they occurred, we ensure accountability, detect anomalies, and have an audit trail of system activities. This helps in investigating security incidents, compliance reporting, and maintaining the overall security posture of our IT environment.