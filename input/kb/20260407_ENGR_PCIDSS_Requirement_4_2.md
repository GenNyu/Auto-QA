### A. Tài liệu gốc của Requirement 4

### B. Summary Overview của Control Objective 4.2
Tài liệu này mô tả chi tiết **Control Objective 4.2** của **Requirement 4** trong **PCI-DSS v4.0.1**, tập trung vào việc bảo vệ PAN trong quá trình truyền tải qua mạng công cộng và các kênh giao tiếp.
Mục tiêu chính là đảm bảo PAN không thể bị đọc hoặc đánh chặn khi truyền qua các mạng mở bằng cách sử dụng mã hóa mạnh và giao thức bảo mật phù hợp.
Gồm 2 sub-requirement chính:
- 4.2.1: Bảo vệ PAN khi truyền qua mạng công cộng
- 4.2.2: Bảo vệ PAN qua end-user messaging
Áp dụng cho tất cả các kênh truyền dữ liệu PAN qua mạng công cộng, mạng không dây và các công nghệ giao tiếp người dùng.

### C. Key Points của Control Objective 4.2
- **Phạm vi áp dụng:**Tất cả kênh truyền PAN qua open/public network, wireless và messaging
- **Trách nhiệm:** Tài liệu hóa và đảm bảo áp dụng cơ chế mã hóa khi truyền dữ liệu
- **Bảo vệ truyền tải:** Sử dụng strong cryptography và secure protocols
- **Quản lý certificate:**Chỉ chấp nhận certificate hợp lệ, không hết hạn hoặc bị revoke
- **Kiểm soát giao thức:** Không cho phép fallback sang giao thức yếu
- **Kiểm soát messaging:**PAN gửi qua email/chat/SMS phải được mã hóa
- **Wireless:** Áp dụng strong cryptography cho authentication và transmission

### D. Deep Summary của Control Objective 4.2
**Bối cảnh:**
Dữ liệu truyền qua mạng công cộng dễ bị sniffing hoặc interception. Nếu không mã hóa, PAN có thể bị thu thập và sử dụng cho gian lận.
**Nội dung cốt lõi:**
- Mã hóa PAN bằng strong cryptography khi truyền qua open/public network
- Sử dụng secure protocol, không cho phép downgrade/fallback
- Chỉ sử dụng trusted keys và certificates hợp lệ
- Bảo vệ PAN khi truyền qua wireless network
- Kiểm soát việc gửi PAN qua end-user messaging (email, chat, SMS)
- Có thể mã hóa ở data level, session level hoặc cả hai
**Dữ liệu đáng chú ý:**
- Open/public network bao gồm Internet, Wi-Fi, Bluetooth, cellular
- Certificate có thể được kiểm tra qua CA, CRL hoặc OCSP
**Rủi ro / Lưu ý:**
- Sử dụng giao thức yếu (SSL, TLS cũ) → dễ bị tấn công
- Certificate không hợp lệ → nguy cơ MITM
- Gửi PAN qua email/chat không mã hóa → rò rỉ dữ liệu
- Wireless không bảo mật → bị sniffing dễ dàng

### E. Structured Output của Control Objective 4.2
**Control objectives:**4.2
**Sub-requirement:**4.2.1
**Defined Approach Requirements:**Strong cryptography and security protocols are implemented as follows to safeguard PAN during transmission over open, public networks:
• Only trusted keys and certificates are accepted.
• Certificates used to safeguard PAN during transmission over open, public networks are confirmed as valid and are not expired or revoked. This bullet is a best practice until its effective date; refer to applicability notes below for details.
• The protocol in use supports only secure versions or configurations and does not support fallback to, or use of insecure versions, algorithms, key sizes, or implementations.
• The encryption strength is appropriate for the encryption methodology in use.
**Defined Approach Testing Procedures:**
- "4.2.1.a": Examine documented policies and procedures and interview personnel to verify processes are defined to include all elements specified in this requirement.
- "4.2.1.b": Examine system configurations to verify that strong cryptography and security protocols are implemented in accordance with all elements specified in this requirement.
- "4.2.1.c": Examine cardholder data transmissions to verify that all PAN is encrypted with strong cryptography when it is transmitted over open, public networks.
- "4.2.1.d": Examine system configurations to verify that keys and/or certificates that cannot be verified as trusted are rejected. Some protocol implementations (such as SSL, SSH v1.0, and early TLS) have known vulnerabilities that an attacker can use to gain access to the cleartext data. It is critical that entities maintain awareness of industry-defined deprecation dates for the cipher suites they are using and are prepared to migrate to newer versions or protocols when older ones are no longer deemed secure. Verifying that certificates are trusted helps ensure the integrity of the secure connection. To be considered trusted, a certificate should be issued from a trusted source, such as a trusted certificate authority (CA), and not be expired. Up-to-date Certificate Revocation Lists (CRLs) or Online Certificate Status Protocol (OCSP) can be used to validate certificates. Techniques to validate certificates may include certificate and public key pinning, where the trusted certificate or a public key is pinned either during development or upon its first use. Entities can also confirm with developers or review source code to ensure that clients and servers reject connections if the certificate is bad. For browser-based TLS certificates, certificate trust can often be verified by clicking on the lock icon that appears next to the address bar.
**Customized Approach Objective:**Cleartext PAN cannot be read or intercepted from any transmissions over open, public networks.
**Applicability Notes:**A self-signed certificate may also be acceptable if the certificate is issued by an internal CA within the organization, the certificate's author is confirmed, and the certificate is verified-for example, via hash or signature-and has not expired. The bullet above (for confirming that certificates used to safeguard PAN during transmission over open, public networks are valid and are not expired or revoked) is a best practice until 31 March 2025, after which it will be required as part of Requirement 4.2.1 and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Sensitive information must be encrypted during transmission over public networks because it is easy and common for a malicious individual to intercept and/or divert data while in transit.
**Guidance - Good Practice:**The network and data-flow diagrams defined in Requirement 1 are useful resources for identifying all connection points where account data is transmitted or received over open, public networks. While not required, it is considered a good practice for entities to also encrypt PAN over their internal networks, and for entities to establish any new network implementations with encrypted communications. PAN transmissions can be protected by encrypting the data before it is transmitted, or by encrypting the session over which the data is transmitted, or both. While it is not required that strong cryptography be applied at both the data level and the session level, it is strongly recommended. If encrypted at the data level, the cryptographic keys used for protecting the data can be managed in accordance with Requirements 3.6 and 3.7. If the data is encrypted at the session level, designated key custodians should be assigned responsibility for managing transmission keys and certificates.
Some protocol implementations (such as SSL, SSH v1.0, and early TLS) have known vulnerabilities that an attacker can use to gain access to the cleartext data. It is critical that entities maintain awareness of industry-defined deprecation dates for the cipher suites they are using and are prepared to migrate to newer versions or protocols when older ones are no longer deemed secure. Verifying that certificates are trusted helps ensure the integrity of the secure connection. To be considered trusted, a certificate should be issued from a trusted source, such as a trusted certificate authority (CA), and not be expired. Up-to-date Certificate Revocation Lists (CRLs) or Online Certificate Status Protocol (OCSP) can be used to validate certificates. Techniques to validate certificates may include certificate and public key pinning, where the trusted certificate or a public key is pinned either during development or upon its first use. Entities can also confirm with developers or review source code to ensure that clients and servers reject connections if the certificate is bad. For browser-based TLS certificates, certificate trust can often be verified by clicking on the lock icon that appears next to the address bar.
**Guidance - Examples:**Open, public networks include, but are not limited to:
• The Internet and
• Wireless technologies, including Wi-Fi, Bluetooth, cellular technologies, and satellite communications.
**Guidance - Further Information:**Vendor recommendations and industry best practices can be consulted for information about the proper encryption strength specific to the encryption methodology in use. For more information about strong cryptography and secure protocols, see industry standards and best practices such as NIST SP 800-52 and SP 800-57 . For more information about trusted keys and certificates, see NIST Cybersecurity Practice Guide Special Publication 1800-16 , Securing Web Transactions: Transport Layer Security (TLS) Server Certificate Management.

---
**Control objectives:**4.2
**Sub-requirement:**4.2.1.1
**Defined Approach Requirements:**An inventory of the entity's trusted keys and certificates used to protect PAN during transmission is maintained.
**Defined Approach Testing Procedures:**
- "4.2.1.1.a": Examine documented policies and procedures to verify processes are defined for the entity to maintain an inventory of its trusted keys and certificates.
- "4.2.1.1.b": Examine the inventory of trusted keys and certificates to verify it is kept up to date.
**Customized Approach Objective:**All keys and certificates used to protect PAN during transmission are identified and confirmed as trusted..
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**The inventory of trusted keys helps the entity keep track of the algorithms, protocols, key strength, key custodians, and key expiry dates. This enables the entity to respond quickly to vulnerabilities discovered in encryption software, certificates, and cryptographic algorithms.
**Guidance - Good Practice:**For certificates, the inventory should include the issuing CA and certification expiration date.

---
**Control objectives:**4.2
**Sub-requirement:**4.2.1.2
**Defined Approach Requirements:**Wireless networks transmitting PAN or connected to the CDE use industry best practices to implement strong cryptography for authentication and transmission.
**Defined Approach Testing Procedures:**Examine system configurations to verify that wireless networks transmitting PAN or connected to the CDE use industry best practices to implement strong cryptography for authentication and transmission.
**Customized Approach Objective:**Cleartext PAN cannot be read or intercepted from wireless network transmissions.
**Guidance - Purpose:**Since wireless networks do not require physical media to connect, it is important to establish controls limiting who can connect and what transmission protocols will be used. Malicious users use free and widely available tools to eavesdrop on wireless communications. Use of strong cryptography can help limit disclosure of sensitive information across wireless networks. Wireless networks present unique risks to an organization; therefore, they must be identified and protected according to industry requirements. Strong cryptography for authentication and transmission of PAN is required to prevent malicious users from gaining access to the wireless network or utilizing wireless networks to access other internal networks or data.
**Guidance - Good Practice:**Wireless networks should not permit fallback or downgrade to an insecure protocol or lower encryption strength that does not meet the intent of strong cryptography.
**Guidance - Further Information:**Review the vendor's specific documentation for more details on the choice of protocols, configurations, and settings related to cryptography.

---
**Control objectives:**4.2
**Sub-requirement:**4.2.2
**Defined Approach Requirements:**PAN is secured with strong cryptography whenever it is sent via end-user messaging technologies.
**Defined Approach Testing Procedures:**
- "4.2.2.a": Examine documented policies and procedures to verify that processes are defined to secure PAN with strong cryptography whenever sent over end-user messaging technologies.
- "4.2.2.b": Examine system configurations and vendor documentation to verify that PAN is secured with strong cryptography whenever it is sent via end- user messaging technologies.
**Customized Approach Objective:**Cleartext PAN cannot be read or intercepted from transmissions using end-user messaging technologies.
**Applicability Notes:**This requirement also applies if a customer, or other third party, requests that PAN is sent to them via end-user messaging technologies. There could be occurrences where an entity receives unsolicited cardholder data via an insecure communication channel that was not intended for transmissions of sensitive data. In this situation, the entity can choose to either include the channel in the scope of their CDE and secure it according to PCI DSS or delete the cardholder data and implement measures to prevent the channel from being used for cardholder data.
**Guidance - Purpose:**End-user messaging technologies typically can be easily intercepted by packet-sniffing during delivery across internal and public networks.
**Guidance - Good Practice:**The use of end-user messaging technology to send PAN should only be considered where there is a defined business need and should be controlled through the Acceptable Use Policies for end-user technologies defined by the entity according to Requirement 12.2.1.
**Guidance - Examples:**E-mail, instant messaging, SMS, and chat are examples of the type of end-user messaging technology that this requirement refers to.