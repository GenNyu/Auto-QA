# Owasp Assessment Part 3 - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Owasp Risk Assessment Form**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 13
- **Phân loại (Category):** Owasp Risk Assessment Form

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Scanning cycle for all CLS environments
### Answer:
Yes, we have scan every 6 months.

---
### Question:
Patching cycle of all CLS environments
### Answer:
Yes

---
### Question:
Please provide current vulnerability scans
### Answer:
https://automation.urbox.vn/scanAPI/Urbox%20PCI%20Quarterly%20External%20Scan_rescan_20240918.pdf

---
### Question:
Have all vulnerabilities for CLS been remediated
### Answer:
Yes, All identified vulnerabilities have been fixed.

---
### Question:
Please provide password complexity and rotation requirements
### Answer:
Passwords must be at least 8 characters long and include a mix of special
characters, numbers, uppercase letters, lowercase letters, and other
permissible special characters if the system allows. Valid password
requirements must be automatically checked when setting passwords.
Passwords must be changed every 90 days. Entering the wrong password
5 times will result in the account being locked for a minimum of 30
minutes or until an administrator reactivates it.

---
### Question:
Please list the requirements for Administrative Privilege vs Normal Log In
### Answer:
Administrative Privilege:
- Strong Authentication: Strong password, mandatory 2FA.
- Access Control: Role-based access, approval for high-risk actions.
- Audit Logs: Track all actions performed by administrators.
- Least Privilege: Assign only necessary permissions.
- Advanced Security: Use encryption
- Regular Security Audits: Ensure current protections are effective.
Normal Log In:
- Authentication: Password meets minimum criteria, 2FA optional.
- Limited Permissions: Access only necessary areas for the user’s role.
- No Installation Rights: Cannot install software or change system settings.
- Follow Security Policies: Must comply with password, encryption,

---
### Question:
Is there separate accounts for Admin and Users? List
### Answer:
Yes, separate accounts should be used to enhance security and reduce risk.
Admin Accounts: Used for tasks requiring elevated privileges in systems such as Google Workspace, Internal Tools, Development Tools, and AWS Console.
User Accounts: Used for day-to-day activities like read-only access on Databases, normal access to Google Workspace (email, documents), and other routine tasks.

---
### Question:
Is two factor employed? YES/ NO, if yes also explain all environments and roles 2FA is used.
### Answer:
YES
***Admin Accounts****:
Google Workspace: Admins are required to use 2FA for accessing the administrative console and managing organizational settings.
Internal Tools: All admin users accessing internal systems (e.g., internal dashboards, monitoring tools) must authenticate using 2FA.
Development Tools: Access to version control systems (like GitLab/GitHub) and CI/CD pipelines require 2FA for all administrative roles.
AWS Console: Admin users in AWS must use 2FA when accessing the AWS Management Console, especially for tasks like EC2 management, IAM configuration, and billing.
OpenVPN: Admins using VPN for secure access to internal systems must authenticate with 2FA for an added security layer.
****User Accounts****:
Google Workspace: Regular users are encouraged (but not required) to use 2FA for accessing their emails, documents, and other Workspace features.
Internal Webserver: Access to internal web services like Ustaff Portal and Urcard Portal requires VPN for private domain access and login via 2FA (email-based).

---
### Question:
Type of 2FA used and Vendor
### Answer:
Email-based Authentication, Vendor: Google Workspace (used for login to internal systems and web portals).
OTP (One-Time Password) via App: Google Authenticator (used for generating time-based one-time passwords for systems like VPN, AWS Console, and Internal Tools).

---
### Question:
LEVEL OF ENCRYPTION for Data at Rest ( Provide Evidence)
### Answer:
Our data is hosted on AWS and is encrypted at rest using AWS KMS with AES-256 encryption.

---
### Question:
Level of encryption for data at storage ( Provide Evidence)
### Answer:
For Data at Storage, AWS uses AES-256 encryption, managed by AWS Key Management Service (KMS) services like RDS

---
### Question:
What roles and personnel manage crypto keys and how are they managed?
### Answer:
Cryptographic keys on AWS are managed by AWS KMS using AWS Managed Keys. AWS handles key creation, management, and rotation automatically, while access to these keys is controlled through IAM policies and all key activities are logged via AWS CloudTrail for auditing and security compliance.

---
### Question:
Length customer records will be retained and why
### Answer:
We will store customer records in 1 year for two main purposes:
- Reconcile with merchants and issuers
- Customer support
The stored data include detail of transactions (First 6 and last 4 digits of card, authorization date, settlement date, payment amount, authorization code, MCC, MID)