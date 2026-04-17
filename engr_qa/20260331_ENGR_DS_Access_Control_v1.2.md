# Access Control - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Access Control**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 2
- **Phân loại (Category):** Access Control

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Are the following additional controls applied to privileged IDs (PIDs), including but not limited to server admin, network admin, DBA, application and service accounts and other similar privileged accounts?
- Monthly review of PID activity
- Use of multi-factor authentication
- Use of a PID management tool to release and monitor PID sessions
- Time-limited use of PIDs following an approval process
### Answer:
Yes
### Comment:
- The password of PID couldn't be shared
- The 3rd party does not have the PID management tool in place
[16/12] Could you if your company can fix 2 above issues. If yes, what is the target date
### Evidence:
- The granting and use of privileges will be limited and controlled and for no longer than required—to perform a necessary action or task..
- Operating system, database and application privileges must be granted according to the process of allocating system resources based on the required requirements.
- Privileges must be assigned to a different account than the one used for normal operations.
- When the default administrator accounts are shared to the user group, the password for this account must be secured and changed when an employee leaves the group.
- Monthly review and verify the privileges granted to the person in charge to ensure that they are in line with reality.
Screenshot of control in evidence file
Additional info:
- Urbox has updated the system so an PID and its password is only assigned to one employee.
- For privileged accounts capable of affecting the system such as server accessed account, the request must be appoved by CEO and under the supervision of CTO.
Urbox will conduct research and apply one of two tools: "Centrify Zero Trust Privilege" or "Ping Identity" by June 2021.

---
### Question:
Is the use of passwords enforced on your systems utilized in providing your service/s to AIA? Please share the following password attributes and practices enforced:
- Password length
- Password complexity requirements
- Password expiration
- Password history/reuse
- Account lockout
- Password reset process
- Secure distribution/communication of initial password
Please confirm whether passwords stored are hashed using SHA-2.
### Answer:
Yes
### Comment:
The AIA Password reuse policy: Not use 8 times before.
[16/12] Could you if your company can fix above issue. If yes, what is the target date
### Evidence:
In document: IT Security Policy 
At least 8 characters, including numbers, lowercase letters, capital letters and special characters
(~! @ # $% ^ & * ...).
Does not contain account name or part of user's name.
Do not use the same password 3 times before.
Do not use passwords that are easy to guess, such as dictionary words, friend names, celebrity
names, computer names, company names, birth dates, phone numbers.
Do not use consecutive alphabetic character
Detail in IT Security Policy
The AIA Password reuse policy: Not use 8 times before.
Target Date to fix is at 30/03/2021