### A. Tài liệu gốc của Chapter 5

### B. Summary Overview của Chapter 5
Tài liệu này mô tả chi tiết **Chapter 5** trong **PCI-DSS v4.0.1**, tập trung vào các **Thực thi tốt nhất để tích hợp PCI DSS vào các quy trình hoạt động kinh doanh hàng ngày (Business-as-Usual - BAU)**
Mục tiêu chính là đảm bảo các biện pháp kiểm soát bảo mật đã triển khai tiếp tục được thực hiện đúng đắn và vận hành hiệu quả như một phần của hoạt động kinh doanh bình thường, giúp duy trì tính tuân thủ liên tục giữa các kỳ đánh giá định kỳ

### C. Key Points của Chapter 5
- **Trách nhiệm giải trình:** Phân công trách nhiệm quản lý tuân thủ PCI DSS cho một cá nhân hoặc nhóm cụ thể, bao gồm việc báo cáo cho ban điều hành
- **Giám sát liên tục:** Thiết lập các chỉ số hiệu suất (metrics) để đo lường hiệu quả của các biện pháp kiểm soát quan trọng như IDS/IPS, anti-malware và kiểm soát truy cập
- **Phản ứng nhanh với sự cố:** Đảm bảo mọi thất bại trong các biện pháp kiểm soát bảo mật được phát hiện và xử lý kịp thời thông qua quy trình: Khôi phục -> Xác định nguyên nhân -> Khắc phục lỗ hổng -> Ngăn ngừa tái phát
- **Quản lý thay đổi:** Đánh giá rủi ro và tác động đến phạm vi (scoping) trước khi thực hiện các thay đổi về hệ thống, mạng hoặc cấu trúc tổ chức (như sáp nhập/mua lại),
- **Duy trì bằng chứng:** Thực hiện các đánh giá định kỳ để xác nhận nhân sự đang tuân thủ đúng quy trình và lưu giữ đầy đủ bằng chứng (như log, báo cáo quét lỗ hổng) cho kỳ đánh giá tiếp theo,

### D. Deep Summary của Chapter 5
**Bối cảnh:**
Bảo mật không phải là một sự kiện nhất thời mà là một quá trình liên tục. BAU giúp các tổ chức không bị rơi vào tình trạng "mất tuân thủ" sau khi kết thúc đợt đánh giá hàng năm bằng cách biến các yêu cầu bảo mật thành thói quen vận hành hàng ngày

**Nội dung cốt lõi:**
Chương này hướng dẫn cách tích hợp bảo mật vào vòng đời vận hành của doanh nghiệp thông qua:
1.  **Phân tích log thường xuyên hơn:** Xem xét dữ liệu log để nhận diện các xu hướng hoặc hành vi bất thường mà việc giám sát tự động có thể bỏ sót
2.  **Quy trình quản lý thay đổi nghiêm ngặt:** Đối với mỗi thay đổi đáng kể (significant change), thực thể phải cập nhật sơ đồ mạng, danh mục thiết bị và lịch quét lỗ hổng
3.  **Xác nhận định kỳ:** Kiểm tra xem các tiêu chuẩn cấu hình có còn được áp dụng, mật khẩu mặc định đã được gỡ bỏ và các bản vá lỗi đã được cập nhật hay chưa

**Dữ liệu đáng chú ý:**
- **Chu kỳ rà soát công nghệ:** Cần xem xét các công nghệ phần cứng và phần mềm ít nhất **một lần mỗi 12 tháng** để đảm bảo chúng vẫn được nhà cung cấp hỗ trợ và đáp ứng yêu cầu bảo mật
- **Hệ thống tài liệu hỗ trợ:** Có hơn **60 tài liệu hướng dẫn** bổ sung trên website của PCI SSC để hỗ trợ các hoạt động BAU

**Rủi ro / Lưu ý:**
- **Kiểm soát trong tương lai:** Các biện pháp kiểm soát chưa được triển khai thực tế hoặc mới chỉ "lên lịch" thực hiện trong tương lai sẽ **không được coi là đã thực thi** tại thời điểm đánh giá
- **Hoạt động bị bỏ lỡ:** Nếu một hoạt động định kỳ (ví dụ quét lỗ hổng hàng quý) bị bỏ lỡ do quản lý kém hoặc thiếu giám sát, thực thể sẽ bị coi là không tuân thủ trừ khi có quy trình phát hiện và khắc phục ngay lập tức
- **Tính phổ quát:** Mặc dù một số nội dung là "best practices", PCI SSC khuyến khích tất cả các thực thể (bao gồm cả các doanh nghiệp nhỏ tự đánh giá) nên áp dụng để tăng cường an ninh

### E. Structured Output của Chapter 5
An entity that implements business-as-usual processes, otherwise known as BAU, as part of their overall security strategy is taking measures to ensure that the security controls implemented to secure data and an environment continue to be implemented correctly and functioning properly as normal course of business.

Some PCI DSS requirements are intended to act as BAU processes by monitoring security controls to ensure their effectiveness on an ongoing basis. This oversight by the entity assists with providing reasonable assurance that the compliance of its environment is preserved between PCI DSS assessments. While there are currently some BAU requirements defined within the standard, an entity should adopt additional BAU processes specific to their organization and environment when possible. BAU processes are a way to verify that automated and manual controls are performing as expected. Regardless of whether a PCI DSS requirement is automated or manual, it is important for BAU processes to detect anomalies, and alert and report so that responsible individuals address the situation in a timely manner.

Examples of how PCI DSS should be incorporated into BAU activities include, but are not limited to:

- Assigning overall responsibility and accountability for PCI DSS compliance to an individual or team. This can include a charter defined by executive management for a specific PCI DSS compliance program and communication to executive management.
- Developing performance metrics to measure the effectiveness of security initiatives and continuous monitoring of security controls, including those that are heavily relied upon, such as network security controls, intrusion-detection systems/intrusion-prevention systems (IDS/IPS), change-detection mechanisms, anti-malware solutions, and access controls, to ensure they are operating effectively and as intended.
- Reviewing logged data more frequently to gain insights to trends or behaviors that may not be obvious with only monitoring.
- Ensuring that all failures in security controls are detected and responded to promptly. Processes to respond to security control failures should include:
    - Restoring the security control.
    - Identifying the cause of failure.
    - Identifying and addressing any security issues that arose during the failure of the security control.
    - Implementing mitigation, such as process or technical controls, to prevent the cause of the failure from recurring.
    - Resuming monitoring of the security control, perhaps with enhanced monitoring for a period of time, to verify the control is operating effectively.
- Reviewing changes that could introduce security risks to the environment (for example, addition of new systems, changes in system or network configurations) prior to completing the change, and including the following:
    - Perform a risk assessment to determine the potential impact to PCI DSS scope (for example, a new network security control rule that permits connectivity between a system in the CDE and another system could bring additional systems or networks into scope for PCI DSS).
    - Identify PCI DSS requirements applicable to systems and networks affected by the changes (for example, if a new system is in scope for PCI DSS, it would need to be configured per system configuration standards, including change-detection mechanisms, anti-malware software, patches, and audit logging. These new systems and networks would need to be added to the inventory of in-scope system components and to the quarterly vulnerability scan schedule).
    - Update PCI DSS scope and implement security controls as appropriate.
    - Update documentation to reflect implemented changes.
- Reviewing the impact to PCI DSS scope and requirements upon changes to organizational structure (for example, a company merger or acquisition).
- Reviewing external connections and third-party access periodically.
- For entities that use third parties for software development, periodically confirming that those software development activities continue to comply with software development requirements in Requirement 6.
- Performing periodic reviews to confirm that PCI DSS requirements continue to be in place and personnel follow established processes. Periodic reviews should cover all facilities and locations, including retail outlets and data centers, whether self-managed or if a TPSP is used. For example, periodic reviews can be used to confirm that configuration standards have been applied to applicable systems, default vendor accounts and passwords are removed or disabled, patches and anti-malware solutions are up to date, audit logs are being reviewed, and so on. The frequency of periodic reviews should be determined by the entity as appropriate for the size and complexity of their environment, if not otherwise stated in PCI DSS. 

These reviews can also be used to verify that required evidence for a PCI DSS assessment is being maintained. For example, evidence of audit logs, vulnerability scan reports, and reviews of network security control rulesets are necessary to assist the entity in preparing for its next PCI DSS assessment.
- Establishing communication with all impacted parties, both external and internal, about newly identified threats and changes to the organization structure. Communication materials should help recipients understand the impact of threats, mitigating steps, and contact points for further information or escalation.
- Reviewing hardware and software technologies at least once every 12 months to confirm that they continue to be supported by the vendor and can meet the entity’s security requirements, including PCI DSS. If technologies are no longer supported by the vendor or cannot meet the entity’s security needs, the entity should prepare a remediation plan, including replacement of the technology, as necessary.

**Note:** Some best practices in this section are also included as PCI DSS requirements for certain entities. For example, those undergoing a full PCI DSS assessment, service providers validating to the additional “service provider only” requirements, and designated entities that are required to validate according to Appendix A3: Designated Entities Supplemental Validation.

Each entity should consider implementing these best practices into their environment, even if the entity is not required to validate to them (for example, merchants undergoing self-assessment).

Refer to Best Practices for Maintaining PCI DSS Compliance in the Document Library on the PCI SSC website for additional guidance.