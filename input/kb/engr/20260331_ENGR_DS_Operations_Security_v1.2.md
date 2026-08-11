# Operations Security - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Operations Security**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 1
- **Phân loại (Category):** Operations Security

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Do you follow security hardening baselines for network components, servers and workstations used in processing, storage or transmission of AIA data by enforcing the following minimum controls before they are used in production?
- Disabling of unnecessary and default user accounts
- Disabling of unnecessary services and ports/interfaces
- Changing of vendor-supplied authentication parameters
- Restricting access to administrative tools and functions
- Patching of operating systems and applications to current version
### Answer:
Yes
### Comment:
[16/12/21] The question of this control is about hardening baseline for network components, servers and workstations.
The answer is more about vulnerability scan.
### Evidence:
Five areas of system hardening:
Network Hardening
- Firewall configuration
- Regular network auditing
- Limit users and secure access points
- Block unnecessary network ports
- Disallow anonymous access
Server Hardening
- Administrative access and rights are allocated properly
- Secure your data center where servers are located
- Disallow shut down initiation without log in
Application Hardening
- Application access control
- Remove default passwords
- Implement password best practices
- Configure account lockout policy
Database Hardening
- Implement admin restrictions on access
- Encrypt data entering and leaving the database
- Remove unused accounts
Operating System Hardening
- Apply necessary updates and patches automatically
- Remove unnecessary files, libraries, drivers, and functionality
- Log all activity, errors, and warnings
- Limit sharing and system permissions
- Configure file system and registry permissions