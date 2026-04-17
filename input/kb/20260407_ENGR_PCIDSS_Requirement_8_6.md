### A. Tài liệu gốc của Requirement 8

### B. Summary Overview của Control Objective 8.6
Tài liệu này mô tả chi tiết **Control Objective 8.6** của **Requirement 8** trong **PCI-DSS v4.0.1**, tập trung vào việc quản lý và bảo vệ tài khoản hệ thống và ứng dụng.
Mục tiêu chính là đảm bảo các account hệ thống và ứng dụng được kiểm soát chặt chẽ, không bị lạm dụng và các yếu tố xác thực liên quan được bảo vệ an toàn.
Gồm 3 sub-requirement chính:
- 8.6.1: Kiểm soát interactive login cho system/application account
- 8.6.2: Không hardcode password
- 8.6.3: Bảo vệ password system/application account
Áp dụng cho tất cả system account và application account trong môi trường.

### C. Key Points của Control Objective 8.6
- **Phạm vi áp dụng:**Tất cả system account và application account
- **Trách nhiệm:** Tài liệu hóa và kiểm soát việc sử dụng account đặc quyền
- **Kiểm soát truy cập:**Hạn chế interactive login, chỉ cho phép khi có exception
- **Quản lý password:**Không được hardcode password trong code/config
- **Bảo vệ xác thực:**Password phải được thay đổi định kỳ và có độ phức tạp phù hợp
- **Truy vết:**Mọi hành động phải truy vết được về cá nhân

### D. Deep Summary của Control Objective 8.6
**Bối cảnh:**
System và application account thường có quyền cao, nếu bị compromise sẽ gây ảnh hưởng nghiêm trọng đến hệ thống và dữ liệu.
**Nội dung cốt lõi:**
- Không cho phép interactive login với system/application account trừ khi có exception được phê duyệt
- Nếu sử dụng interactive login, phải đảm bảo truy vết được về cá nhân
- Không hardcode password trong source code, script hoặc config
- Bảo vệ password bằng cách thay đổi định kỳ và tăng độ phức tạp
- Áp dụng kiểm soát bổ sung (vault, managed solution) để bảo vệ credential
**Dữ liệu đáng chú ý:**
- Password change frequency dựa trên risk analysis (Requirement 12.3.1)
- Có thể sử dụng password vault để quản lý credential
**Rủi ro / Lưu ý:**
- Hardcoded password → dễ bị lộ qua source code
- System account bị lạm dụng → khó truy vết
- Không rotate password → tăng nguy cơ bị brute force
- Interactive login không kiểm soát → mất accountability

### E. Structured Output của Control Objective 8.6
**Control objectives:**8.6
**Sub-requirement:**8.6.1
**Defined Approach Requirements:**If accounts used by systems or applications can be used for interactive login, they are managed as follows:
• Interactive use is prevented unless needed for an exceptional circumstance.
• Interactive use is limited to the time needed for the exceptional circumstance.
• Business justification for interactive use is documented.
• Interactive use is explicitly approved by management.
• Individual user identity is confirmed before access to account is granted.
• Every action taken is attributable to an individual user.
**Defined Approach Testing Procedures:**Examine application and system accounts that can be used interactively and interview administrative personnel to verify that application and system accounts are managed in accordance with all elements specified in this requirement.
**Customized Approach Objective:**When used interactively, all actions with accounts designated as system or application accounts are authorized and attributable to an individual person.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Like individual user accounts, system and application accounts require accountability and strict management to ensure they are used only for the intended purpose and are not misused. Attackers often compromise system or application accounts to gain access to cardholder data.
**Guidance - Good Practice:**Where possible, configure system and application accounts to disallow interactive login to prevent unauthorized individuals from logging in and using the account with its associated system privileges, and to limit the machines and devices on which the account can be used.
**Guidance - Definitions:**Interactive login is the ability for a person to log into a system or application account in the same manner as a normal user account. Using system and application accounts this way means there is no accountability and traceability of actions taken by the user. Refer to Appendix G for the definition of 'application and system accounts.'

---
**Control objectives:**8.6
**Sub-requirement:**8.6.2
**Defined Approach Requirements:**Passwords/passphrases for any application and system accounts that can be used for interactive login are not hard coded in scripts, configuration/property files, or bespoke and custom source code.
**Defined Approach Testing Procedures:**
- "8.6.2.a": Interview personnel and examine system development procedures to verify that processes are defined for application and system accounts that can be used for interactive login, specifying that passwords/passphrases are not hard coded in scripts, configuration/property files, or bespoke and custom source code.
- "8.6.2.b": Examine scripts, configuration/property files, and bespoke and custom source code for application and system accounts that can be used for interactive login, to verify passwords/passphrases for those accounts are not present.
**Customized Approach Objective:**Passwords/passphrases used by application and system accounts cannot be used by unauthorized personnel.
**Applicability Notes:**Stored passwords/passphrases are required to be encrypted in accordance with PCI DSS Requirement 8.3.2. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Not properly protecting passwords/passphrases used by application and system accounts, especially if those accounts can be used for interactive login, increases the risk and success of unauthorized use of those privileged accounts.
**Guidance - Good Practice:**Changing these values due to suspected or confirmed disclosure can be particularly difficult to implement. Tools can facilitate both management and security of authentication factors for application and system accounts. For example, consider password vaults or other system-managed controls.

---
**Control objectives:**8.6
**Sub-requirement:**8.6.3
**Defined Approach Requirements:**Passwords/passphrases for any application and system accounts are protected against misuse as follows:
• Passwords/passphrases are changed periodically (at the frequency defined in the entity's targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1) and upon suspicion or confirmation of compromise.
• Passwords/passphrases are constructed with sufficient complexity appropriate for how frequently the entity changes the passwords/passphrases.
**Defined Approach Testing Procedures:**
- "8.6.3.a": Examine policies and procedures to verify that procedures are defined to protect passwords/passphrases for application or system accounts against misuse in accordance with all elements specified in this requirement.
- "8.6.3.b": Examine the entity's targeted risk analysis for the change frequency and complexity for passwords/passphrases for application and system accounts to verify the risk analysis was performed in accordance with all elements specified in Requirement 12.3.1 and addresses:
• The frequency defined for periodic changes to application and system passwords/passphrases.
• The complexity defined for passwords/passphrases and appropriateness of the complexity relative to the frequency of changes.
- "8.6.3.c": Interview responsible personnel and examine system configuration settings to verify that passwords/passphrases for any application and system accounts are protected against misuse in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Passwords/passphrases used by application and system accounts cannot be used indefinitely and are structured to resist brute-force and guessing attacks.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Systems and application accounts pose more inherent security risk than user accounts because they often run in an elevated security context, with access to systems that may not be typically granted to user accounts, such as programmatic access to databases, etc. As a result, special consideration must be made to protect passwords/passphrases used for application and system accounts.
**Guidance - Good Practice:**Entities should consider the following risk factors when determining how to protect application and system passwords/passphrases against misuse:
• How securely the passwords/passphrases are stored (for example, whether they are stored in a password vault).
• Staff turnover.
• The number of people with access to the authentication factor.
• Whether the account can be used for interactive login.
• Whether the security posture of accounts is dynamically analyzed, and real-time access to resources is automatically determined accordingly (see Requirement 8.3.9). All these elements affect the level of risk for application and system accounts and might impact the security of systems accessed by the system and application accounts.
Entities should correlate their selected change frequency for application and system passwords/passwords with their selected complexity for those passwords/passphrases - i.e., the complexity should be more rigorous when passwords/passphrases are changed infrequently and can be less rigorous when changed more frequently. For example, a longer change frequency is more justifiable when passwords/passphrases complexity is set to 36 alphanumeric characters with upper- and lower- case letters, numbers, and special characters. Best practices are to consider password changes at least once a year, a password/passphrase length of at least 15 characters, and complexity for the passwords/passphrase of alphanumeric characters, with upper- and lower-case letters, and special characters.
**Guidance - Further Information:**For information about variability and equivalency of password strength for passwords/passphrases of different formats, see the industry standards (for example, the current version of NIST SP 800- 63 Digital Identity Guidelines).