### A. Tài liệu gốc của Chương 8 (Control 8.27)

### B. Summary Overview của Chương 8 (Control 8.27)
Tài liệu này mô tả **mục 8.27** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào việc đưa nguyên tắc an toàn vào kiến trúc và kỹ thuật hệ thống ngay từ giai đoạn thiết kế.
Mục tiêu là bảo đảm hệ thống được thiết kế, triển khai, vận hành và mở rộng theo một bộ nguyên tắc an toàn nhất quán trong toàn bộ vòng đời phát triển.
Gồm 1 mục chính:
- `8.27`: `Secure system architecture and engineering principles` - nguyên tắc kiến trúc và kỹ thuật an toàn cho hệ thống

Áp dụng cho kiến trúc nhiều lớp, zero trust, xác thực và quản lý phiên, kiểm soát truy cập, hardening và việc ràng buộc các nguyên tắc này trong phát triển thuê ngoài.

### C. Key Points của Chương 8 (Control 8.27)
- **Mục tiêu quản trị:** Đưa security vào kiến trúc và kỹ thuật hệ thống từ đầu để giảm lỗi thiết kế và giảm phụ thuộc vào biện pháp vá chữa sau triển khai.
- **Yêu cầu chính:** Cần có bộ nguyên tắc được ghi nhận, duy trì và áp dụng nhất quán cho business, data, application và technology layers.
- **Điểm quan trọng về thiết kế:** Phải xem xét cơ chế xác thực, quản lý session, data validation/sanitisation, hardening và cách các control hỗ trợ lẫn nhau.
- **Zero trust:** Không mặc định tin tưởng mạng nội bộ; mọi yêu cầu phải được xác thực, ủy quyền và truyền mã hóa end-to-end.
- **Lưu ý thực tế:** Nếu nguyên tắc kiến trúc không được rà soát định kỳ, hệ thống dễ lệch khỏi chuẩn an toàn khi công nghệ, threat hoặc mô hình triển khai thay đổi.

### D. Deep Summary của Chương 8 (Control 8.27)
**Bối cảnh:**
Control này đặt nền móng cho cách tổ chức thiết kế an toàn ở cấp kiến trúc. Thay vì coi bảo mật là lớp bổ sung sau cùng, nó yêu cầu security được nhúng vào thiết kế, công nghệ và quy trình kỹ thuật ngay từ đầu.

**Nội dung cốt lõi:**
- Tổ chức phải có bộ nguyên tắc kỹ thuật an toàn được lập thành văn bản và áp dụng cho mọi hoạt động phát triển hệ thống.
- Thiết kế an toàn phải bao phủ toàn bộ kiến trúc: business, data, application và technology.
- Khi đánh giá một thiết kế, cần xác định control nào cần có, control đó phòng ngừa hay phát hiện hay phản ứng, và các control kết hợp với nhau như thế nào.
- Bộ nguyên tắc phải tính đến nền tảng kỹ thuật sẵn có, năng lực nội bộ, chi phí, độ phức tạp và thực hành tốt hiện hành.
- Zero trust được nêu như một cách tiếp cận thực tiễn để giảm giả định tin cậy mặc định trong hệ thống và mạng.

**Dữ liệu đáng chú ý:**
- `8.27` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Application_security#System_and_network_security` và miền `#Protection`.
- Tài liệu nêu rõ các nguyên tắc kiến trúc phổ biến như `security by design`, `defence in depth`, `security by default`, `default deny`, `fail securely`, `least privilege` và `least functionality`.
- Zero trust trong control này nhấn mạnh `never trust and always verify`, mã hóa end-to-end và xác thực theo ngữ cảnh.
- Nguyên tắc an toàn cũng phải được phản ánh trong hợp đồng và thỏa thuận ràng buộc khi phát triển thuê ngoài.
- Tài liệu cho phép áp dụng các nguyên tắc này cho resilience, segregation và tamper resistance.

**Rủi ro / Lưu ý:**
- Nếu nguyên tắc kiến trúc không được cập nhật theo công nghệ mới, các control triển khai sau đó có thể không còn phù hợp hoặc không còn hiệu lực.
- Nếu chỉ dựa vào perimeter security, mô hình phòng thủ sẽ yếu khi nội bộ bị xâm nhập hoặc khi có luồng truy cập từ bên ngoài.
- Nếu bỏ qua design review, các lỗi an ninh gốc như session control yếu, validation kém hoặc trust boundary sai sẽ lọt vào production.
- Nếu phát triển thuê ngoài nhưng không ràng buộc nguyên tắc kỹ thuật bằng hợp đồng, việc thực thi sẽ thiếu nhất quán và khó kiểm soát.

### E. Structured Output của Chương 8 (Control 8.27)
**Section:** 8.27
**Title:** Secure system architecture and engineering principles

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Application_security #System_and_network_security |
| Security domains | #Protection |

**Control:**
Principles for engineering secure systems should be established, documented, maintained and applied to any information system development activities.

**Purpose:**
To ensure information systems are securely designed, implemented and operated within the development life cycle.

**Guidance:**
Security engineering principles should be established, documented and applied to information system engineering activities. Security should be designed into all architecture layers (business, data, applications and technology). New technology should be analysed for security risks and the design should be reviewed against known attack patterns.

Secure engineering principles provide guidance on user authentication techniques, secure session control and data validation and sanitisation.

Secure system engineering principles should include analysis of:

- the full range of security controls required to protect information and systems against identified threats;
- the capabilities of security controls to prevent, detect or respond to security events;
- specific security controls required by particular business processes (e.g. encryption of sensitive information, integrity checking and digitally signing information);
- where and how security controls are to be applied (e.g. by integrating with a security architecture and the technical infrastructure);
- how individual security controls (manual and automated) work together to produce an integrated set of controls.

Security engineering principles should take account of:

- the need to integrate with a security architecture;
- technical security infrastructure [e.g. public key infrastructure (PKI), identity and access management (IAM), data leakage prevention and dynamic access management];
- capability of the organization to develop and support the chosen technology;
- cost, time and complexity of meeting security requirements;
- current good practices.

Secure system engineering should involve:

- the use of security architecture principles, such as “security by design”, “defence in depth”, “security by default”, “default deny”, “fail securely”, “distrust input from external applications”, “security in deployment”, “assume breach”, "least privilege", “usability and manageability” and “least functionality”;
- a security-oriented design review to help identify information security vulnerabilities, ensure security controls are specified and meet security requirements;
- documentation and formal acknowledgement of security controls that do not fully meet requirements (e.g. due to overriding safety requirements);
- hardening of systems.

The organization should consider "zero trust" principles such as:

- assuming the organization’s information systems are already breached and thus not be reliant on network perimeter security alone;
- employing a “never trust and always verify” approach for access to information systems;
- ensuring that requests to information systems are encrypted end-to-end;
- verifying each request to an information system as if it originated from an open, external network, even if these requests originated internal to the organization (i.e. not automatically trusting anything inside or outside its perimeters);
- using "least privilege" and dynamic access control techniques (see 5.15, 5.18 and 8.2). This includes authenticating and authorizing requests for information or to systems based on contextual information such as authentication information (see 5.17), user identities (see 5.16), data about the user endpoint device, and data classification (see 5.12);
- always authenticating requesters and always validating authorization requests to information systems based on information including authentication information (see 5.17) and user identities (5.16), data about the user endpoint device, and data classification (see 5.12), for example enforcing strong authentication (e.g. multi-factor, see 8.5).

The established security engineering principles should be applied, where applicable, to outsourced development of information systems through the contracts and other binding agreements between the organization and the supplier to whom the organization outsources. The organization should ensure that suppliers’ security engineering practices align with the organization’s needs.

The security engineering principles and the established engineering procedures should be regularly reviewed to ensure that they are effectively contributing to enhanced standards of security within the engineering process. They should also be regularly reviewed to ensure that they remain up-to-date in terms of combatting any new potential threats and in remaining applicable to advances in the technologies and solutions being applied.

**Other information:**
Secure engineering principles can be applied to the design or configuration of a range of techniques, such as:

- fault tolerance and other resilience techniques;
- segregation (e.g. through virtualization or containerization);
- tamper resistance.

Secure virtualization techniques can be used to prevent interference between applications running on the same physical device. If a virtual instance of an application is compromised by an attacker, only that instance is affected. The attack has no effect on any other application or data.

Tamper resistance techniques can be used to detect tampering of information containers, whether physical (e.g. a burglar alarm) or logical (e.g. a data file). A characteristic of such techniques is that there is a record of the attempt to tamper with the container. In addition, the control can prevent the successful extraction of data through its destruction (e.g. device memory can be deleted).