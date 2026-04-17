# Customer IAM - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Customer IAM**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 7
- **Phân loại (Category):** Customer IAM

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
a. One-Time Passwords may only be valid for up to 5 minutes or until they have been successfully used, whichever is the shortest. After one successful use, the password may not be used again. When the OTP is used in an email as a StepUp method, Then the maximum OTP validity can be 10 minutes if the user has already been authenticated, and if the user email address has been approved for transmitting OTPs.
b. One-Time Passwords must be a minimum of 6 characters long. There are no construction restrictions.
c. Provide only one valid One-Time Passwords per request at any given time.
d. Allow maximum 6 requests to (re)send the OTP.
e. Allow maximum 6 wrong OTP entries.
f. An out of band notification must be sent whenever a password is successfully changed or when the change is attempted. The Message should explicitly mention the context of the OTP usage.
g. All in-house developed One-Time Password algorithms and implementations must be reviewed and approved by Cybersecurity Security Architecture and Product Security & Assurance.
### Answer:
Per Article 20 & 21 of UrBox IT Security Policy.
Web Portal / Microsite AP: OTPs are valid for a maximum of 5 minutes or until used (whichever comes first). Each OTP is single-use and generated via CSPRNG (non-predictable). Delivered via secure out-of-band channel (SMS/ZNS/ Email)

---
### Question:
Visa applications and related entitlement systems must prevent excessive access over the business application and data by:
a) Employing the concept of least privilege, allowing only authorized accesses for users (and processes acting on behalf of users) which are necessary to accomplish assigned tasks (need-to-know);
b) Enforcing the use of non-privileged accounts, or roles, when accessing non-privileged (regular user) functions and data; and
c) Auditing any use of privileged accounts or roles.
### Answer:
Per Article 17.2 & 19 of UrBox IT Security Policy.
Web Portal / Microsite AP: Role-based access control (RBAC) is implemented. Users are granted minimum permissions required for their role. Privileged access is separate from standard user access. Access rights reviewed annually and revoked upon offboarding.

---
### Question:
The business application must:
a) Enforce a limit of not more than six (6) failed consecutive invalid login attempts by a user during a 30-minute time period;
b) Automatically lock the account for at least 30 minutes or until released by an administrator when the maximum number of unsuccessful attempts is exceeded;
c) Not disclose which component of the login process failed (ID or authenticators);
d) Not disclose how many attempts remain before the account will be locked; and
e) Not disclose for how long the account will be locked.
f) Implement API level rate limiting for login API
### Answer:
Per Article 20.4.a of UrBox IT Security Policy: Account locked after 5 failed attempts for a minimum of 30 minutes.
Web Portal / Microsite AP: Account locked after 5 consecutive failed login attempts (within DSR maximum of 6). Lockout duration: minimum 30 minutes or until admin reactivation. Failed attempts are logged.

---
### Question:
Active session timeout must conform to a 12-hour active session timeout.
### Answer:
Per Article 21.2 of UrBox IT Security Policy.
Web Portal / Microsite AP: 12-hour active session timeout enforced. Users must re-authenticate after 12 hours of continuous session.
Zalo Mini App (VN): UrBox enforces a 12-hour active session timeout at the UrBox application layer, independent of Zalo's native session management. After 12 hours, users are required to re-authenticate to continue accessing UrBox services within the Mini App.

---
### Question:
Applications must prevent further access to the system by locking or terminating a user's session after 15 minutes of inactivity.
The application may allow session re-establishment after re-authenticating the user, or the session may be permanently terminated, as appropriate.
### Answer:
Per Article 21.2.i & 24.8 of UrBox IT Security Policy: Sessions must be terminated after 15 minutes of inactivity.
Web Portal / Microsite AP: Session automatically locked/terminated after 15 minutes of inactivity. Re-authentication required to resume.

---
### Question:
The business application must: 
a) Audit account creation, modification, change of entitlements, disabling, and termination actions and notify, as required, appropriate individuals including responsible information custodians and business application owners;
b) Create and maintain audit trails appropriate for monitoring and alerting on access to runtime security functions; at minimum, it must track and monitor privileged role assignment and uses.
### Answer:
Per Article 28 & 19 of UrBox IT Security Policy.
Web Portal / Microsite AP: All privileged access actions (account creation, modification, entitlement change, disabling, termination) are logged with timestamp, actor ID, and action detail. Logs protected from tampering, retained 3–6 months, reviewed periodically by the security team.
Note: Automated notification on privileged access events is not currently implemented — periodic log review is the compensating control.

---
### Question:
a) Log all authentication attempts, both successful and failures according Security Logging DSR
b) The Information Custodian must work with relevant application / system development / support teams to ensure appropriate logging and monitoring controls are in place as defined in the Security Logging DSR.
### Answer:
Per Article 28 of UrBox IT Security Policy.
Web Portal / Microsite AP: All authentication events (successful and failed) logged with timestamp, user ID, IP address, and outcome. Logs centrally aggregated, protected from modification, retained 3–6 months. Reviewed regularly by the Technical Team. NTP-synchronized timestamps across all systems.
Tools: Amazon CloudWatch (monitoring & alerting), Elasticsearch (centralized log aggregation).