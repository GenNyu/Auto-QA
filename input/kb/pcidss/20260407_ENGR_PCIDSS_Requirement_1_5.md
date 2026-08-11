### A. Tài liệu gốc của Requirement 1

### B. Summary Overview của Control Objective 1.5
Tài liệu này mô tả chi tiết **Control Objective 1.5 **của **Requirement 1 **trong **PCI-DSS v4.0.1, **tập trung vào việc **Giảm thiểu rủi ro từ các thiết bị kết nối đồng thời vào mạng không tin cậy và CDE**
Mục tiêu là ngăn thiết bị (laptop, mobile, BYOD…) mang mối đe dọa vào CDE và đảm bảo thiết bị có security controls phù hợp trước khi kết nối
Gồm 1 sub-requirement chính:
- 1.5.1: Áp dụng security controls trên endpoint (company & BYOD)
Áp dụng cho tất cả thiết bị kết nối đồng thời Internet / mạng không tin cậy và CDE

### C. Key Points của Control Objective 1.5
- **Endpoint security:** Phải có security controls (EDR, firewall…)
- **Configuration:** Có cấu hình bảo mật rõ ràng
- **Enforcement:** Controls phải luôn hoạt động
- **User restriction:** Người dùng không được tự ý tắt
- **BYOD:** Áp dụng cả thiết bị cá nhân
- **VPN:** Hạn chế split-tunneling

### D. Deep Summary của Control Objective 1.5
**Bối cảnh:**
Thiết bị người dùng (laptop, mobile, BYOD) thường xuyên kết nối Internet nên dễ bị nhiễm malware. Khi các thiết bị này kết nối vào CDE, chúng có thể trở thành điểm xâm nhập cho attacker.
**Nội dung cốt lõi:**
- **Bảo vệ endpoint:**Thiết bị phải có security controls (endpoint protection, firewall…)
- **Cấu hình bảo mật:**Có thiết lập để ngăn threat từ mạng không tin cậy
- **Thực thi kiểm soát:**Controls phải luôn chạy và không bị user tự ý thay đổi
- **Kiểm soát truy cập:**Thiết bị chỉ được kết nối khi đáp ứng yêu cầu bảo mật
- **Quản lý ngoại lệ:**Chỉ được tắt controls khi có phê duyệt và trong thời gian giới hạn
**Dữ liệu đáng chú ý:**
- Áp dụng cho cả thiết bị công ty và BYOD
- Bao gồm laptop, mobile, tablet và thiết bị di động khác
**Rủi ro / Lưu ý:**
- Thiết bị nhiễm malware → lây vào CDE
- User tắt security controls → mất lớp bảo vệ
- Split-tunneling → bypass kiểm soát mạng
- Thiết bị không kiểm soát → trở thành điểm tấn công
- Không quản lý BYOD → mở rộng attack surface

### E. Structured Output của Control Objective 1.5
**Control objectives:**1.5
**Sub-requirement:** 1.5.1 *(Tag: endpoint security, VPN, split tunneling, device hardening)*
**Defined Approach Requirements of 1.5.1:**Security controls are implemented on any computing devices, including company- and employee-owned devices, that connect to both untrusted networks (including the Internet) and the CDE as follows:
• Specific configuration settings are defined to prevent threats being introduced into the entity's network.
• Security controls are actively running.
• Security controls are not alterable by users of the computing devices unless specifically documented and authorized by management on a case-by-case basis for a limited period.
**Defined Approach Testing Procedures of 1.5.1:**
- "1.5.1.a": Examine policies and configuration standards and interview personnel to verify security controls for computing devices that connect to both untrusted networks, and the are implemented in accordance with all elements specified in this requirement.
- "1.5.1.b": Examine configuration settings on computing devices that connect to both untrusted networks and the CDE to verify settings are implemented in accordance with all elements specified in this requirement.
**Customized Approach Objective of 1.5.1:**Devices that connect to untrusted environments and also connect to the CDE cannot introduce threats to the entity's CDE.
**Applicability Notes of 1.5.1:**These security controls may be temporarily disabled only if there is legitimate technical need, as authorized by management on a case-by-case basis. If these security controls need to be disabled for a specific
**Guidance - Purpose of 1.5.1:**Computing devices that are allowed to connect to the Internet from outside the corporate environment-for example, desktops, laptops, tablets, smartphones, and other mobile computing devices used by employees-are more vulnerable to Internet-based threats. Use of security controls such as host-based controls (for example, personal firewall software or end-point protection solutions), network-based security controls (for example, firewalls, network- based heuristics inspection, and malware simulation), or hardware, helps to protect devices from Internet-based attacks, which could use the device to gain access to the organization's systems and data when the device reconnects to the network.
**Guidance - Good Practice of 1.5.1:**The specific configuration settings are determined by the entity and should be consistent with its network security policies and procedures. Where there is a legitimate need to temporarily disable security controls on a company-owned or employee-owned device that connects to both an untrusted network and the CDE-for example, to support a specific maintenance activity or investigation of a technical problem-the reason for taking such action is understood and approved by an appropriate management representative. Any disabling or altering of these security controls, including on administrators' own devices, is performed by authorized personnel. It is recognized that administrators have privileges that may allow them to disable security controls on their own computers, but there should be alerting mechanisms in place when such controls are disabled and follow up that occurs to ensure processes were followed.
**Guidance - Examples of 1.5.1:**Practices include forbidding split-tunneling of VPNs for employee-owned or corporate-owned mobile devices and requiring that such devices boot up into a VPN.