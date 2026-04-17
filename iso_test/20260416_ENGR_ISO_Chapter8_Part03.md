### A. Tài liệu gốc của Chương 8 (Control 8.4, 8.5)

### B. Summary Overview của Chương 8 (Control 8.4, 8.5)
Tài liệu này mô tả chi tiết **mục 8.4 và 8.5** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào việc kiểm soát truy cập mã nguồn và triển khai cơ chế xác thực an toàn cho hệ thống, ứng dụng và dịch vụ.
Mục tiêu là **ngăn thay đổi trái phép vào source code, bảo vệ tài sản trí tuệ trong quá trình phát triển và bảo đảm chỉ đúng thực thể mới được xác thực trước khi truy cập hệ thống**.
Gồm 2 mục chính:
- `8.4`: Access to source code - kiểm soát truy cập mã nguồn, công cụ phát triển và thư viện phần mềm
- `8.5`: Secure authentication - triển khai xác thực an toàn cho hệ thống và dịch vụ

Áp dụng cho kho mã nguồn, công cụ phát triển, môi trường build/test, cơ chế đăng nhập, và toàn bộ hệ thống hoặc ứng dụng yêu cầu xác thực người dùng hay thực thể.

### C. Key Points của Chương 8 (Control 8.4, 8.5)
- **Mục tiêu quản trị:** `8.4` giảm nguy cơ sửa mã trái phép hoặc lộ bí mật phát triển; `8.5` giảm nguy cơ xác thực yếu, đăng nhập bị lạm dụng và truy cập trái phép vào hệ thống.
- **Yêu cầu chính của 8.4:** Mã nguồn, thư viện và công cụ phát triển phải được kiểm soát chặt, phân quyền theo vai trò, ghi log truy cập và gắn với quy trình thay đổi được phê duyệt.
- **Yêu cầu chính của 8.5:** Cơ chế xác thực phải phù hợp với mức độ nhạy cảm của thông tin, có thể bao gồm mật khẩu mạnh, token, smart card, certificate, biometrics và multi-factor authentication.
- **Điểm vận hành quan trọng:** `8.5` không chỉ là chọn phương thức login; nó còn bao gồm thiết kế log-on process, chống brute force, xử lý session không hoạt động và cảnh báo sự kiện xác thực bất thường.
- **Lưu ý thực tế:** Với dữ liệu hoặc mã nguồn có giá trị cao, tổ chức cần kết hợp kiểm soát truy cập, xác thực mạnh và giám sát để giảm khả năng cả tấn công bên trong lẫn tấn công từ bên ngoài.

### D. Deep Summary của Chương 8 (Control 8.4, 8.5)
**Bối cảnh:**
Hai control này bảo vệ lớp nền rất quan trọng của môi trường công nghệ: mã nguồn và cơ chế xác thực. Nếu mã nguồn bị sửa trái phép, tổ chức có thể vô tình phát hành phần mềm chứa backdoor, lỗi bảo mật hoặc mất tài sản trí tuệ. Nếu xác thực yếu, kẻ tấn công chỉ cần vượt qua lớp đăng nhập là có thể tiếp cận hệ thống, ứng dụng và dữ liệu.

**Nội dung cốt lõi:**
- `8.4` yêu cầu kiểm soát chặt quyền đọc/ghi source code, tài liệu thiết kế, công cụ build và môi trường phát triển, thường thông qua source code management system hoặc repo trung tâm.
- `8.4` nhấn mạnh quyền đọc và quyền ghi có thể khác nhau theo vai trò; write access phải giới hạn cho người có thẩm quyền và gắn với change control.
- `8.4` cũng yêu cầu log đầy đủ truy cập và thay đổi, đồng thời cân nhắc cơ chế bảo đảm tính toàn vẹn nếu mã nguồn được công bố công khai.
- `8.5` yêu cầu chọn kỹ thuật xác thực phù hợp với mức độ nhạy cảm của dữ liệu và hệ thống, thường phải mạnh hơn password đơn thuần đối với hệ thống quan trọng.
- `8.5` còn bao gồm hardening cho quy trình log-on: hiển thị thông báo chung, tránh tiết lộ thông tin hỗ trợ kẻ tấn công, chống brute force, khóa session nhàn rỗi và cảnh báo khi có dấu hiệu tấn công.

**Dữ liệu đáng chú ý:**
- `8.4` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Identity_and_access_management#Application_security#Secure_configuration` và miền `#Protection`.
- `8.5` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Identity_and_access_management` và miền `#Protection`.
- `8.4` có tham chiếu thêm đến change control (8.32) khi cập nhật mã hoặc cấp quyền truy cập mã nguồn.
- `8.5` có tham chiếu đến ISO/IEC 29115 cho phần assurance của entity authentication.
- `8.5` nêu rõ biometrics cần phương án thay thế, vì có thể bị ảnh hưởng bởi điều kiện sử dụng hoặc bị compromise.

**Rủi ro / Lưu ý:**
- Nếu truy cập source code không được kiểm soát, mã có thể bị sửa trái phép, rò rỉ dữ liệu phát triển hoặc làm lộ cấu hình, bí mật triển khai.
- Nếu tài khoản quản trị dùng cho việc thường ngày, rủi ro lạm dụng đặc quyền và sai sót vận hành sẽ tăng đáng kể.
- Nếu xác thực chỉ dựa vào mật khẩu yếu hoặc log-on process tiết lộ quá nhiều thông tin, kẻ tấn công sẽ dễ brute force hoặc social engineering.
- Nếu không có timeout, cảnh báo, hoặc step-up authentication, session bị bỏ quên có thể trở thành điểm xâm nhập thuận lợi.

### E. Structured Output của Chương 8 (Control 8.4, 8.5)
**Section:** 8.4
**Title:** Access to source code

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Identity_and_access_management #Application_security #Secure_configuration |
| Security domains | #Protection |

**Control:**
Read and write access to source code, development tools and software libraries should be appropriately managed.

**Purpose:**
To prevent the introduction of unauthorized functionality, avoid unintentional or malicious changes and to maintain the confidentiality of valuable intellectual property.

**Guidance:**
Access to source code and associated items (such as designs, specifications, verification plans and validation plans) and development tools (e.g. compilers, builders, integration tools, test platforms and environments) should be strictly controlled.

For source code, this can be achieved by controlling central storage of such code, preferably in source code management system.

Read access and write access to source code can differ based on the personnel’s role. For example, read access to source code can be broadly provided inside the organization, but write access to source code is only made available to privileged personnel or designated owners. Where code components are used by several developers within an organization, read access to a centralized code repository should be implemented. Furthermore, if open-source code or third-party code components are used inside an organization, read access to such external code repositories can be broadly provided. However, write access should still be restricted.

The following guidelines should be considered to control access to program source libraries in order to reduce the potential for corruption of computer programs:
- managing the access to program source code and the program source libraries according to established procedures;
- granting read and write access to source code based on business needs and managed to address risks of alteration or misuse and according to established procedures;
- updating of source code and associated items and granting of access to source code in accordance with change control procedures (see 8.32) and only performing it after appropriate authorization has been received;
- not granting developers direct access to the source code repository, but through developer tools that control activities and authorizations on the source code;
- holding program listings in a secure environment, where read and write access should be appropriately managed and assigned;
- maintaining an audit log of all accesses and of all changes to source code.

If the program source code is intended to be published, additional controls to provide assurance on its integrity (e.g. digital signature) should be considered.

**Other information:**
If access to source code is not properly controlled, source code can be modified or some data in the development environment (e.g. copies of production data, configuration details) can be retrieved by unauthorized persons.

---
**Section:** 8.5
**Title:** Secure authentication

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Identity_and_access_management |
| Security domains | #Protection |

**Control:**
Secure authentication technologies and procedures should be implemented based on information access restrictions and the topic-specific policy on access control.

**Purpose:**
To ensure a user or an entity is securely authenticated, when access to systems, applications and services is granted.

**Guidance:**
A suitable authentication technique should be chosen to substantiate the claimed identity of a user, software, messages and other entities.

The strength of authentication should be appropriate for the classification of the information to be accessed. Where strong authentication and identity verification is required, authentication methods alternative to passwords, such as digital certificates, smart cards, tokens or biometric means, should be used.

Authentication information should be accompanied by additional authentication factors for accessing critical information systems (also known as multi-factor authentication). Using a combination of multiple authentication factors, such as what you know, what you have and what you are, reduces the possibilities for unauthorized accesses. Multi-factor authentication can be combined with other techniques to require additional factors under specific circumstances, based on predefined rules and patterns, such as access from an unusual location, from an unusual device or at an unusual time.

Biometric authentication information should be invalidated if it is ever compromised. Biometric authentication can be unavailable depending on the conditions of use (e.g. moisture or aging). To prepare for these issues, biometric authentication should be accompanied with at least one alternative authentication technique.

The procedure for logging into a system or application should be designed to minimize the risk of unauthorized access. Log-on procedures and technologies should be implemented considering the following:
- not displaying sensitive system or application information until the log-on process has been successfully completed in order to avoid providing an unauthorized user with any unnecessary assistance;
- displaying a general notice warning that the system or the application or the service should only be accessed by authorized users;
- not providing help messages during the log-on procedure that would aid an unauthorized user (e.g. if an error condition arises, the system should not indicate which part of the data is correct or incorrect);
- validating the log-on information only on completion of all input data;
- protecting against brute force log-on attempts on usernames and passwords [e.g. using completely automated public Turing test to tell computers and humans apart (CAPTCHA), requiring password reset after a predefined number of failed attempts or blocking the user after a maximum number of errors];
- logging unsuccessful and successful attempts;
- raising a security event if a potential attempted or successful breach of log-on controls is detected (e.g. sending an alert to the user and the organization’s system administrators when a certain number of wrong password attempts has been reached);
- displaying or sending the following information on a separate channel on completion of a successful log-on:
  1. date and time of the previous successful log-on;
  2. details of any unsuccessful log-on attempts since the last successful log-on;
- not displaying a password in clear text when it is being entered; in some cases, it can be required to de-activate this functionality in order to facilitate user log-on (e.g. for accessibility reasons or to avoid blocking users because of repeated errors);
- not transmitting passwords in clear text over a network to avoid being captured by a network "sniffer” program;
- terminating inactive sessions after a defined period of inactivity, especially in high risk locations such as public or external areas outside the organization’s security management or on user endpoint devices;
- restricting connection duration times to provide additional security for high-risk applications and reduce the window of opportunity for unauthorized access.

**Other information:**
Additional information on entity authentication assurance can be found is ISO/IEC 29115.