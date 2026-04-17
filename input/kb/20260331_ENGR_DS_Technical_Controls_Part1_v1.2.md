# Technical Controls - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Technical Controls**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 12
- **Phân loại (Category):** Technical Controls

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Vulnerability Management: What are your vulnerability management and system patching commitments?
### Answer:
Critical within 3 Days
High within 7 Days
Medium within 30 Days
Low within 90 Days

---
### Question:
Encryption:  How is data encrypted within your environment?
### Answer:
We utilize RSA 2048 for encrypting data before transmission and employ TLS 1.2 to encrypt the communication channel.

---
### Question:
AV/HIDS/HIPS:  What malware and intrusion prevention solutions are deployed in your platform?
### Answer:
All servers have ClamAV antivirus software installed, and IDS/IPS is integrated into the CloudFlare firewall system.

---
### Question:
Firewalls:  How have you implemented Firewalls to protect your organization?
### Answer:
We use CloudFlare's firewall to protect our infrastructure, and all laptop computers have their software firewalls enabled.

---
### Question:
Passwords:  Do you have an enforced password policy?
### Answer:
UrBox's Policy:
Passwords must be at least 8 characters long and include a mix of special characters, numbers, uppercase letters, lowercase letters, and other permissible special characters if the system allows. Valid password requirements must be automatically checked when setting passwords. Passwords must be changed every 90 days. Entering the wrong password 5 times will result in the account being locked for a minimum of 30 minutes or until an administrator reactivates it.
Default passwords provided by manufacturers in hardware, software, or databases must be changed immediately upon deployment.

---
### Question:
Restrict Data Access:  How do you restrict access to PII and our sensitive data in your organization?
### Answer:
Here are practices and measures that UrBox typically uses to restrict access to PII and sensitive data:
1. Role-Based Access Control (RBAC):
Implement RBAC to assign specific roles and permissions to users based on their job responsibilities.
Ensure that employees only have access to the PII necessary to perform their duties.
2. Access Controls and Permissions:
Implement access controls within applications, databases, and file systems to restrict who can read, modify, or delete PII.
Define and enforce permissions for specific data folders, files, and database records.
3. Need-to-Know Principle:
Adhere to the "need-to-know" principle, where employees are granted access only to the specific PII required for their job tasks.
Minimize access to sensitive data by limiting it to individuals who have a legitimate business need.
4. Least Privilege Principle:
Apply the "least privilege" principle, granting users the minimum level of access required to perform their job tasks.
Review and update permissions regularly to avoid excessive access rights.
5. Encryption:
Encrypt sensitive data at rest and in transit to protect it from unauthorized access, even if physical or network security measures are breached.
6. Access Logs and Auditing:
- Generate access logs to record user activities, including data access.
- Regularly audit access logs to detect unauthorized or suspicious activities.
7. Training and Awareness:
- Provide training to employees on data security best practices, including their responsibilities for handling PII securely.
- Raise awareness about the importance of data protection.
8. Incident Response:
- Develop incident response plans to address unauthorized access incidents promptly and effectively.
- Ensure that employees know how to report security incidents.

---
### Question:
Restrict Data Access:  How is your employee and system access to PII recorded?
### Answer:
Access Logs and Auditing:
- Generate access logs to record user activities, including data access.
- Regularly audit access logs to detect unauthorized or suspicious activities.

---
### Question:
Restrict Data Access: Do you have a DLP (Data Leakage Prevention) solution in place
### Answer:
We have not implemented a DLP solution yet, but plan to do so next year

---
### Question:
Office/Data Center Access:  Is data physically secure within your offices and/or data centers?
### Answer:
Our data center is entirely on AWS Cloud. All documents and records are stored in locked cabinets, and the access points have fingerprint recognition and surveillance cameras.

---
### Question:
Pen Testing: Please provide an Executive Summary of your latest Pen Test
### Answer:
We only perform internal pentests every year and upon product release. We only hire 3rd party pentests upon request from customers.

---
### Question:
Pen Testing: Was Grey Box testing used?
### Answer:
We conduct vulnerability scanning and greybox penetration testing.

---
### Question:
Pen Testing: Did the scope of your pen test include Production Systems, Software, and APIs?
### Answer:
We pentest all elements such as: software, APIs…

---