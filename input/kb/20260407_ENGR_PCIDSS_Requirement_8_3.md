### A. Tài liệu gốc của Requirement 8

### B. Summary Overview của Control Objective 8.3
Tài liệu này mô tả chi tiết** Control Objective 8.3** của **Requirement 8 **trong **PCI-DSS v4.0.1**, tập trung vào việc xác thực người dùng và bảo vệ các yếu tố xác thực.
Mục tiêu chính là đảm bảo việc xác thực được thực hiện an toàn, các yếu tố xác thực được bảo vệ, quản lý chặt chẽ và không bị lạm dụng hoặc khai thác.
Gồm 11 sub-requirement chính:
- 8.3.1: Yếu tố xác thực
- 8.3.2: Mã hóa yếu tố xác thực
- 8.3.3: Xác minh khi thay đổi
- 8.3.4: Khóa tài khoản
- 8.3.5: Thiết lập và reset mật khẩu
- 8.3.6: Độ phức tạp mật khẩu
- 8.3.7: Lịch sử mật khẩu
- 8.3.8: Tài liệu hóa chính sách
- 8.3.9: Thay đổi định kỳ/Phân tích động
- 8.3.10: Hướng dẫn cho khách hàng (Service Provider)
- 8.3.11: Quản lý Token và Chứng chỉ
Áp dụng cho tất cả user, cơ chế xác thực và các yếu tố xác thực trong môi trường, ngoại trừ các tài khoản trên thiết bị POS chỉ truy cập một số thẻ tại một thời điểm

### C. Key Points của Control Objective 8.3
- **Phạm vi áp dụng:**Tất cả user, authentication factor và cơ chế xác thực
- **Trách nhiệm:** Tài liệu hóa và quản lý xác thực người dùng
- **Xác thực:** Sử dụng ít nhất một authentication factor (know/have/are)
- **Bảo vệ dữ liệu:**Authentication factor phải được mã hóa khi lưu trữ và truyền
- **Kiểm soát truy cập:**Giới hạn login sai và yêu cầu re-authentication
- **Quản lý password:** Áp dụng độ dài, complexity và lịch sử password
- **Chính sách người dùng:**Phổ biến hướng dẫn sử dụng và bảo vệ password

### D. Deep Summary của Control Objective 8.3
**Bối cảnh:**
Việc sử dụng các yếu tố xác thực yếu hoặc không được bảo vệ là kẽ hở lớn để kẻ tấn công xâm nhập hệ thống và chiếm đoạt quyền truy cập hợp lệ. Kiểm soát này giúp giảm thiểu rủi ro từ các cuộc tấn công dò mật khẩu (brute-force) hoặc kỹ thuật xã hội (social engineering)
**Nội dung cốt lõi:**
- Sử dụng authentication factor phù hợp (password, token, biometric)
- Bảo vệ authentication factor bằng strong cryptography
- Xác minh danh tính trước khi thay đổi authentication factor
- Giới hạn số lần login sai và lock account
- Áp dụng chính sách password mạnh (độ dài, complexity, history)
- Quản lý vòng đời password và cập nhật định kỳ
- Phổ biến hướng dẫn cho người dùng về bảo vệ thông tin xác thực
**Dữ liệu đáng chú ý:**
- Lock account sau ≤ 10 lần đăng nhập sai
- Lock tối thiểu 30 phút hoặc đến khi xác minh
- Password ≥ 12 ký tự (hoặc ≥ 8 nếu hệ thống hạn chế)
- Thay đổi mật khẩu ít nhất mỗi 90 ngày nếu chỉ dùng xác thực đơn yếu tố
**Rủi ro / Lưu ý:**
- Password yếu → dễ bị brute force
- Không mã hóa → lộ authentication factor
- Không lock account → attacker thử nhiều lần
- Không verify identity → bị social engineering
- Reuse password → tăng nguy cơ compromise

### E. Structured Output của Control Objective 8.3
**Control objectives:**8.3
**Sub-requirement:**8.3.1
**Defined Approach Requirements:**All user access to system components for users and administrators is authenticated via at least one of the following authentication factors:
• Something you know, such as a password or passphrase.
• Something you have, such as a token device or smart card.
• Something you are, such as a biometric element.
**Defined Approach Testing Procedures:**
- "8.3.1.a": Examine documentation describing the authentication factor(s) used to verify that user access to system components is authenticated via at least one authentication factor specified in this requirement.
- "8.3.1.b": For each type of authentication factor used with each type of system component, observe an authentication to verify that authentication is functioning consistently with documented authentication factor(s).
**Customized Approach Objective:**An account cannot be accessed except with a combination of user identity and an authentication factor.
**Applicability Notes:**This requirement is not intended to apply to user accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction. This requirement does not supersede multi-factor authentication (MFA) requirements but applies to those in-scope systems not otherwise subject to MFA requirements. A digital certificate is a valid option for 'something you have' if it is unique for a particular user.
**Guidance - Purpose:**When used in addition to unique IDs, an authentication factor helps protect user IDs from being compromised, since the attacker needs to have the unique ID and compromise the associated authentication factor(s).
**Guidance - Good Practice:**A common approach for a malicious individual to compromise a system is to exploit weak or nonexistent authentication factors (for example, passwords/passphrases). Requiring strong authentication factors helps protect against this attack.
**Guidance - Further Information:**See fidoalliance.org for more information about using tokens, smart cards, or biometrics as authentication factors.

---
**Control objectives:**8.3
**Sub-requirement:**8.3.2
**Defined Approach Requirements:**Strong cryptography is used to render all authentication factors unreadable during transmission and storage on all system components.
**Defined Approach Testing Procedures:**
- "8.3.2.a": Examine vendor documentation and system configuration settings to verify that authentication factors are rendered unreadable with strong cryptography during transmission and storage.
- "8.3.2.b": Examine repositories of authentication factors to verify that they are unreadable during storage.
- "8.3.2.c": Examine data transmissions to verify that authentication factors are unreadable during transmission.
**Customized Approach Objective:**Cleartext authentication factors cannot be obtained, derived, or reused from the interception of communications or from stored data.
**Guidance - Purpose:**Network devices and applications have been known to transmit unencrypted, readable authentication factors (such as passwords and passphrases) across the network and/or store these values without encryption. As a result, a malicious individual can easily intercept this information during transmission using a 'sniffer,' or directly access unencrypted authentication factors in files where they are stored, and then use this data to gain unauthorized access.

---
**Control objectives:**8.3
**Sub-requirement:**8.3.3
**Defined Approach Requirements:**User identity is verified before modifying any authentication factor.
**Defined Approach Testing Procedures:**Examine procedures for modifying authentication factors and observe security personnel to verify that when a user requests a modification of an authentication factor, the user's identity is verified before the authentication factor is modified.
**Customized Approach Objective:**Unauthorized individuals cannot gain system access by impersonating the identity of an authorized user.
**Guidance - Purpose:**Malicious individuals use "social engineering' techniques to impersonate a user of a system- for example, calling a help desk and acting as a legitimate user-to have an authentication factor changed so they can use a valid user ID. Requiring positive identification of a user reduces the probability of this type of attack succeeding.
**Guidance - Good Practice:**Modifications to authentication factors for which user identity should be verified include but are not limited to performing password resets, provisioning new hardware or software tokens, and generating new keys.
**Guidance - Examples:**Methods to verify a user's identity include a secret question/answer, knowledge-based information, and calling the user back at a known and previously established phone number.

---
**Control objectives:**8.3
**Sub-requirement:**8.3.4
**Defined Approach Requirements:**Invalid authentication attempts are limited by:
• Locking out the user ID after not more than 10 attempts.
• Setting the lockout duration to a minimum of 30 minutes or until the user's identity is confirmed.
**Defined Approach Testing Procedures:**
- "8.3.4.a": Examine system configuration settings to verify that authentication parameters are set to require that user accounts be locked out after not more than 10 invalid logon attempts.
- "8.3.4.b": Examine system configuration settings to verify that password parameters are set to require that once a user account is locked out, it remains locked for a minimum of 30 minutes or until the user's identity is confirmed.
**Customized Approach Objective:**An authentication factor cannot be guessed in a brute force, online attack.
**Applicability Notes:**This requirement is not intended to apply to user accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction.
**Guidance - Purpose:**Without account-lockout mechanisms in place, an attacker can continually try to guess a password through manual or automated tools (for example, password cracking) until the attacker succeeds and gains access to a user's account. If an account is locked out due to someone continually trying to guess a password, controls to delay reactivation of the locked account stop the malicious individual from guessing the password, as they will have to stop for a minimum of 30 minutes until the account is reactivated.
**Guidance - Good Practice:**Before reactivating a locked account, the user's identity should be confirmed. For example, the administrator or help desk personnel can validate that the actual account owner is requesting reactivation, or there may be password reset self- service mechanisms that the account owner uses to verify their identity.

---
**Control objectives:**8.3
**Sub-requirement:**8.3.5
**Defined Approach Requirements:**If passwords/passphrases are used as authentication factors to meet Requirement 8.3.1, they are set and reset for each user as follows:
• Set to a unique value for first-time use and upon reset.
• Forced to be changed immediately after the first use.
**Defined Approach Testing Procedures:**Examine procedures for setting and resetting passwords/passphrases (if used as authentication factors to meet Requirement 8.3.1) and observe security personnel to verify that passwords/passphrases are set and reset in accordance with all elements specified in this requirement.
**Customized Approach Objective:**An initial or reset password/passphrase assigned to a user cannot be used by an unauthorized user.
**Guidance - Purpose:**If the same password/passphrase is used for every new user, an internal user, former employee, or malicious individual may know or easily discover the value and use it to gain access to accounts before the authorized user attempts to use the password.

---
**Control objectives:**8.3
**Sub-requirement:**8.3.6
**Defined Approach Requirements:**If passwords/passphrases are used as authentication factors to meet Requirement 8.3.1, they meet the following minimum level of complexity:
• A minimum length of 12 characters (or IF the system does not support 12 characters, a minimum length of eight characters).
• Contain both numeric and alphabetic characters.
**Defined Approach Testing Procedures:**Examine system configuration settings to verify that user password/passphrase complexity parameters are set in accordance with all elements specified in this requirement.
**Customized Approach Objective:**A guessed password/passphrase cannot be verified by either an online or offline brute force attack.
**Applicability Notes:**This requirement is not intended to apply to:
• User accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction.
• Application or system accounts, which are governed by requirements in section 8.6. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. Until 31 March 2025, passwords must be a minimum length of seven characters in accordance with PCI DSS v3.2.1 Requirement 8.2.3.
**Guidance - Purpose:**Strong passwords/passphrases may be the first line of defense into a network since a malicious individual will often first try to find accounts with weak, static, or non-existent passwords. If passwords are short or easily guessable, it is relatively easy for a malicious individual to find these weak accounts and compromise a network under the guise of a valid user ID.
**Guidance - Good Practice:**Password/passphrase strength is dependent on password/passphrase complexity, length, and randomness. Passwords/passphrases should be sufficiently complex, so they are impractical for an attacker to guess or otherwise discover its value. Entities can consider adding increased complexity by requiring the use of special characters and upper- and lower-case characters, in addition to the minimum standards outlined by this requirement. Additional complexity increases the time required for offline brute force attacks of hashed passwords/passphrases. Another option for increasing the resistance of passwords to guessing attacks is by comparing proposed password/passphrases to a bad password list and having users provide new passwords for any passwords found on the list.

---
**Control objectives:**8.3
**Sub-requirement:**8.3.7
**Defined Approach Requirements:**Individuals are not allowed to submit a new password/passphrase that is the same as any of the last four passwords/passphrases used.
**Defined Approach Testing Procedures:**Examine system configuration settings to verify that password parameters are set to require that new passwords/passphrases cannot be the same as the four previously used passwords/passphrases.
**Customized Approach Objective:**A previously used password cannot be used to gain access to an account for at least 12 months.
**Applicability Notes:**This requirement is not intended to apply to user accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction.
**Guidance - Purpose:**If password history is not maintained, the effectiveness of changing passwords is reduced, as previous passwords can be reused over and over. Requiring that passwords cannot be reused for a period reduces the likelihood that passwords that have been guessed or brute-forced will be re- used in the future. Passwords or passphrases may have previously been changed due to suspicion of compromise or because the password or passphrase exceeded its effective use period, both of which are reasons why previously used passwords should not be reused.

---
**Control objectives:**8.3
**Sub-requirement:**8.3.8
**Defined Approach Requirements:**Authentication policies and procedures are documented and communicated to all users including:
• Guidance on selecting strong authentication factors.
• Guidance for how users should protect their authentication factors.
• Instructions not to reuse previously used passwords/passphrases.
• Instructions to change passwords/passphrases there is any suspicion or knowledge that the password/passphrases have been and how to report the incident.
**Defined Approach Testing Procedures:**
- "8.3.8.a": Examine procedures and interview personnel to verify that authentication policies and procedures are distributed to all users.
- "8.3.8.b": Review authentication policies and procedures that are distributed to users and verify they include the elements specified in this requirement.
- "8.3.8.c": Interview users to verify that they are familiar with authentication policies and procedures.
**Customized Approach Objective:**Users are knowledgeable about the correct use of authentication factors and can access assistance and guidance when required.
**Guidance - Purpose:**Communicating authentication policies and procedures to all users helps them to understand and abide by the policies.
**Guidance - Good Practice:**Guidance on selecting strong passwords may include suggestions to help personnel select hard-to-guess passwords that do not contain dictionary words or information about the user, such as the user ID, names of family members, date of birth, etc. Guidance for protecting authentication factors may include not writing down passwords or not saving them in insecure files, and being alert to malicious individuals who may try to exploit their passwords (for example, by calling an employee and asking for their password so the caller can 'troubleshoot a problem'). Alternatively, entities can implement processes to confirm passwords meet password policy, for example, by comparing password choices to a list of unacceptable passwords and having users choose a new password for any that match with one on the list. Instructing users to change passwords if there is a chance the password is no longer secure can prevent malicious users from using a legitimate password to gain unauthorized access.

---
**Control objectives:**8.3
**Sub-requirement:**8.3.9
**Defined Approach Requirements:**If passwords/passphrases are used as the only authentication factor for user access (i.e., in any single-factor authentication implementation) then either:
• Passwords/passphrases are changed at least once every 90 days, OR
• The security posture of accounts is dynamically analyzed, and real-time access to resources is automatically determined accordingly.
**Defined Approach Testing Procedures:**If passwords/passphrases are used as the only authentication factor for user access, inspect system configuration settings to verify that passwords/passphrases are managed in accordance with ONE of the elements specified in this requirement.
**Customized Approach Objective:**An undetected compromised password/passphrase cannot be used indefinitely.
**Applicability Notes:**This requirement does not apply to in-scope system components where MFA is used. This requirement is not intended to apply to user accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction. This requirement does not apply to service providers' customer accounts but does apply to facilitate a single transaction. This requirement does not apply to service providers' customer accounts but does apply to accounts for service provider personnel.
**Guidance - Purpose:**Access to in-scope system components that are not in the CDE may be provided using a single authentication factor, such as a password/passphrase, token device or smart card, or biometric attribute. Where passwords/passphrases are employed as the only authentication factor for such access, additional controls are required to protect the integrity of the password/passphrase.
**Guidance - Good Practice:**Passwords/passphrases that are valid for a long time without a change provide malicious individuals with more time to break the password/phrase. Periodically changing passwords offers less time for a malicious individual to crack a password/passphrase and less time to use a compromised password. Using a password/passphrase as the only authentication factor provides a single point of failure if compromised. Therefore, in these implementations, controls are needed to minimize how long malicious activity could occur via a compromised password/passphrase. Dynamically analyzing an account's security posture is another option that allows for more rapid detection and response to address potentially compromised credentials. Such analysis takes a number of data points, which may include device integrity, location, access times, and the resources accessed to determine in real time whether an account can be granted access to a requested resource. In this way, access can be denied and accounts blocked if it is suspected that authentication credentials have been compromised.
**Guidance - Further Information:**For information about using dynamic analysis to manage user access to resources, see NIST SP 800-207 Zero Trust Architecture .

---
**Control objectives:**8.3
**Sub-requirement:**8.3.10
**Defined Approach Requirements:**Additional requirement for service providers only: If passwords/passphrases are used as the only authentication factor for customer user access to cardholder data (i.e., in any single- factor authentication implementation), then guidance is provided to customer users including:
• Guidance for customers to change their user passwords/passphrases periodically.
• Guidance as to when, and under what circumstances, passwords/passphrases are to be changed.
**Defined Approach Testing Procedures:**Additional testing procedure for service provider assessments only: If passwords/passphrases are used as the only authentication factor for customer user access to cardholder data, examine guidance provided to customer users to verify that the guidance includes all elements specified in this requirement.
**Customized Approach Objective:**Passwords/passphrases for service providers' customers cannot be used indefinitely.
**Applicability Notes:**This requirement applies only when the entity being assessed is a service provider. This requirement does not apply to accounts of consumer users accessing their own payment card information.
This requirement for service providers will be superseded by Requirement 8.3.10.1 once 8.3.10.1 becomes effective.
**Guidance - Purpose:**Using a password/passphrase as the only authentication factor provides a single point of failure if compromised. Therefore, in these implementations, controls are needed to minimize how long malicious activity could occur via a compromised password/passphrase.
**Guidance - Good Practice:**Passwords/passphrases that are valid for a long time without a change provide malicious individuals with more time to break the password/phrase. Periodically changing passwords offers less time for a malicious individual to crack a password/passphrase and less time to use a compromised password.

---
**Control objectives:**8.3
**Sub-requirement:**8.3.10.1
**Defined Approach Requirements:**Additional requirement for service providers only: If passwords/passphrases are used as the only authentication factor for customer user access (i.e., in any single-factor authentication implementation) then either:
• Passwords/passphrases are changed at least once every 90 days, OR
• The security posture of accounts is dynamically analyzed, and real-time access to resources is automatically determined accordingly.
**Defined Approach Testing Procedures:**Additional testing procedure for service provider assessments only: If passwords/passphrases are used as the only authentication factor for customer user access, inspect system configuration settings to verify that passwords/passphrases are managed in accordance with ONE of the elements specified in this requirement.
**Customized Approach Objective:**Passwords/passphrases for service providers' customers cannot be used indefinitely.
**Applicability Notes:**This requirement applies only when the entity being assessed is a service provider. This requirement does not apply to accounts of consumer users accessing their own payment card information. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. Until this requirement is effective on 31 March 2025, service providers may meet either Requirement 8.3.10 or 8.3.10.1.
**Guidance - Purpose:**Using a password/passphrase as the only authentication factor provides a single point of failure if compromised. Therefore, in these implementations, controls are needed to minimize how long malicious activity could occur via a compromised password/passphrase.
**Guidance - Good Practice:**Passwords/passphrases that are valid for a long time without a change provide malicious individuals with more time to break the password/phrase. Periodically changing passwords offers less time for a malicious individual to crack a password/passphrase and less time to use a compromised password. Dynamically analyzing an account's security posture is another option that allows for more rapid detection and response to address potentially compromised credentials. Such analysis takes a number of data points which may include device integrity, location, access times, and the resources accessed to determine in real time whether an account can be granted access to a requested resource. In this way, access can be denied and accounts blocked if it is suspected that account credentials have been compromised.
**Guidance - Further Information:**For information about using dynamic analysis to manage user access to resources, refer to NIST SP 800-207 Zero Trust Architecture .

---
**Control objectives:**8.3
**Sub-requirement:**8.3.11
**Defined Approach Requirements:**Where authentication factors such as physical or logical security tokens, smart cards, or certificates are used:
• Factors are assigned to an individual user and not shared among multiple users.
• Physical and/or logical controls ensure only the intended user can use that factor to gain access.
**Defined Approach Testing Procedures:**
- "8.3.11.a": Examine authentication policies and procedures to verify that procedures for using authentication factors such as physical security tokens, smart cards, and certificates are defined and include all elements specified in this requirement.
- "8.3.11.b": Interview security personnel to verify authentication factors are assigned to an individual user and not shared among multiple users.
- "8.3.11.c": Examine system configuration settings and/or observe physical controls, as applicable, to verify that controls are implemented to ensure only the intended user can use that factor to gain access.
**Customized Approach Objective:**An authentication factor cannot be used by anyone other than the user to which it is assigned.
**Guidance - Purpose:**If multiple users can use authentication factors such as tokens, smart cards, and certificates, it may be impossible to identify the individual using the authentication mechanism.
**Guidance - Good Practice:**Having physical and/or logical controls (for example, a PIN, biometric data, or a password) to uniquely authenticate the user of the account will prevent unauthorized users from gaining access to the user account through use of a shared authentication factor.