# Customer IAM - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Customer IAM**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 10
- **Phân loại (Category):** Customer IAM

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
All web applications that require a login account must show appropriate Terms & Conditions for Access to each user the first time they log in.
There must be a record of agreement to the access arrangement. The record may be a traditionally signed paper contract or an e-signature record, as deemed appropriate by the application's line of business and the Legal department.
### Answer:
Per Article 43.1 & 10 of UrBox IT Security Policy.
Web Portal / Microsite AP: T&C is displayed on first login; user must explicitly agree (checkbox/acknowledgement) before access is granted. Record of acceptance (timestamp + user ID) is retained.
Zalo Mini App (VN): UrBox supplements this with in-app T&C acknowledgement at first access to the Mini App. Record of acceptance is logged on UrBox's backend.

---
### Question:
Each individual person that accesses a Visa business application must use a unique personal account. Personal accounts must not be shared.
### Answer:
Per Article 19.1 of UrBox IT Security Policy.
Web Portal / Microsite AP: Each user is assigned a unique personal account. Account sharing is prohibited.

---
### Question:
During failed authentication attempts, do not divulge which piece of authentication data was incorrect. i.e., do not indicate whether an ID was not found or a password was found to be incorrect. Keep message generic, such as "authentication failed".
### Answer:
Per Article 21.2.b of UrBox IT Security Policy.
Web Portal / Microsite AP: Generic error message returned on failed login (e.g. 'Authentication failed') — does not reveal whether username or password was incorrect.

---
### Question:
When collecting passwords from a user on a traditional computer (desktop or laptop), neither full passwords nor individual characters of the password may be displayed or echoed back to the user as they are typed, without the explicit consent of the user each time (e.g. “show password” toggle)
On a mobile device, individual characters of the password may be displayed for no more than three (3) seconds while typed, unless the user explicitly requests / toggles a control to display the password.
### Answer:
Per Article 21.2.g of UrBox IT Security Policy.
Web Portal / Microsite AP: Password fields are masked by default. 'Show password' toggle available only upon explicit user action.

---
### Question:
The business application, for password-based authentication, must:
a) Enforce minimum password complexity of: case sensitive, minimum 8 characters, at least one upper-case letter, one lower-case letter, one special character and one numeric character;
b) Must not contain the associated User ID (or PAN)
### Answer:
Per Article 20.4.a of UrBox IT Security Policy: Minimum 8 characters, mixed case, numbers and special characters required.
Web Portal / Microsite AP: Password complexity enforced at application layer — minimum 8 characters, uppercase, lowercase, number, and special character required. Complexity validated automatically on set.

---
### Question:
Changed passwords must differ from, at a minimum, the last 4 passwords for B2B accounts, and the last 1 for B2C accounts.
### Answer:
Per Article 20.4.c of UrBox IT Security Policy: Last 6 passwords cannot be reused.
Web Portal / Microsite AP: Last 6 passwords are prevented from reuse — exceeds DSR minimum of last 4 (B2B) and last 1 (B2C).

---
### Question:
When the initial password for a user is not self-selected, the initial password must be required to be changed by the user upon first login.
Initial passwords must be unique and randomly generated.
### Answer:
Per Article 20.2 of UrBox IT Security Policy: Default/assigned passwords must be changed on first login.
Web Portal / Microsite AP: System-assigned initial passwords must be changed on first login before application access is granted. Initial passwords sent via secure one-time channel.

---
### Question:
a) Any system that allows a user to change their password must first request and validate the user's current password.
b) An out of band notification must be sent whenever a password is successfully changed or when the change is attempted.
### Answer:
Per Article 21.3.a & 20.1 of UrBox IT Security Policy.
Web Portal / Microsite AP: Current password must be validated before a password change is permitted. Out-of-band notification (email/SMS) sent to user upon any password change.

---
### Question:
A user must be authenticated prior to password recovery. The following methods are recommended to authenticate the user, in order of strength:
1) Send a one-time-password to a mobile device on record for the user
2) Send a one-time-password to an email address on record for the user
3) Present a challenge question in addition to the one-time-password or out of band email link which should expire within two hours.
### Answer:
Per Article 20 of UrBox IT Security Policy.
Web Portal / Microsite AP: Two-method forgotten password flow — both require authentication before reset:
1) OTP via SMS/Email: Valid for ≤ 5 minutes, single-use.
2) Security questions: User must answer pre-registered security questions or use a magiclink to recover, defined by VSRP

---
### Question:
To qualify as multi-factor, an authentication scheme must include use of at least two-different factors. The available factors are:
1) Something you know such as a password, PIN or answer to a challenge question;
2) Something you have, such as an x.509 digital certificate, private key, or a one-time password generator (aka hardware token or fob);
3) Something you are, such as a biometric representation of a fingerprint, voice, iris or retina.
Note: Use of one-time passwords (OTP) alone is not considered multi-factor. OTP must be combined with a PIN, password, adaptive authentication or biometric to be considered multi-factor.
Biometric systems may never store a reversible or full representation of a biometric (such as a photo image of a fingerprint or a voice recording). Only non-reversible hashes (or equivalent) built from the biometric data may be stored.
### Answer:
Per Article 21.2.d of UrBox IT Security Policy.
Web Portal / Microsite AP: MFA is currently available as an optional feature for B2C users (OTP via SMS/email as second factor). MFA is enforced by default for all Admin Portal access. Biometric authentication (Face ID / fingerprint) is planned for Phase 2 as an additional MFA option for B2C users.