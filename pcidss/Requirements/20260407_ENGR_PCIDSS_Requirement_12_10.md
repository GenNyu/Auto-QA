### A. Tài liệu gốc của Requirement 12

### B. Summary Overview của Control Objective 12.10
Tài liệu này mô tả chi tiết **Control Objective 12.10** của **Requirement 12** trong **PCI-DSS v4.0.1**, tập trung vào việc thiết lập, duy trì và vận hành quy trình ứng phó sự cố bảo mật.
Mục tiêu chính là đảm bảo các sự cố bảo mật được phát hiện, xử lý kịp thời và có quy trình rõ ràng nhằm giảm thiểu tác động đến hệ thống và cardholder data.
Gồm 6 sub-requirement chính:
- 12.10.1: Thiết lập incident response plan
- 12.10.2: Review và test kế hoạch
- 12.10.3: Đảm bảo nhân sự 24/7
- 12.10.4: Đào tạo nhân sự ứng phó sự cố
- 12.10.5: Xử lý alert từ hệ thống giám sát
- 12.10.6: Cập nhật kế hoạch theo bài học
- 12.10.7: Xử lý PAN ngoài phạm vi
Áp dụng cho toàn bộ hệ thống, nhân sự và quy trình liên quan đến ứng phó sự cố trong môi trường.

### C. Key Points của Control Objective 12.10
- **Phạm vi áp dụng:**Toàn bộ hệ thống, CDE và hoạt động security monitoring
- **Trách nhiệm:** Tài liệu hóa và vận hành incident response plan
- **Ứng phó sự cố:**Có quy trình rõ ràng (containment, mitigation, recovery)
- **Sẵn sàng:**Có nhân sự trực 24/7 để xử lý sự cố
- **Đào tạo:**Nhân sự phải được đào tạo định kỳ
- **Giám sát:**Xử lý alert từ IDS/IPS, FIM, network control…
- **Cập nhật:** Kế hoạch phải được review, test và cải tiến liên tục

### D. Deep Summary của Control Objective 12.10
**Bối cảnh:**
Không có quy trình ứng phó sự cố rõ ràng sẽ dẫn đến xử lý chậm, gây thiệt hại lớn về tài chính, uy tín và pháp lý.
**Nội dung cốt lõi:**
- Xây dựng incident response plan đầy đủ (role, communication, recovery…)
- Review và test kế hoạch ít nhất hàng năm
- Đảm bảo nhân sự sẵn sàng 24/7
- Đào tạo nhân sự về quy trình và kỹ năng xử lý sự cố
- Xử lý alert từ các hệ thống giám sát bảo mật
- Cập nhật kế hoạch dựa trên bài học và threat mới
- Có quy trình riêng khi phát hiện PAN ngoài phạm vi
**Dữ liệu đáng chú ý:**
- Incident response plan phải bao gồm cả legal, communication và backup
- Training và test phải thực hiện định kỳ
- Bao phủ alert từ nhiều nguồn (IDS/IPS, FIM, wireless…)
**Rủi ro / Lưu ý:**
- Không có plan → xử lý sự cố rối loạn
- Không test → plan không khả thi
- Không có 24/7 response → chậm phản ứng
- Không xử lý alert → bỏ lỡ tấn công
- Không cập nhật → không đáp ứng threat mới
- Không xử lý PAN ngoài scope → rò rỉ dữ liệu không kiểm soát

### E. Structured Output của Control Objective 12.10
**Control objectives:**12.10
**Sub-requirement:**12.10.1
**Defined Approach Requirements:**An incident response plan exists and is ready to be activated in the event of a suspected or confirmed security incident. The plan includes, but is not limited to:
• Roles, responsibilities, and communication and contact strategies in the event of a suspected or confirmed security incident, including notification of payment brands and acquirers, at a minimum.
• Incident response procedures with specific containment and mitigation activities for different types of incidents.
• Business recovery and continuity procedures.
• Data backup processes.
• Analysis of legal requirements for reporting compromises.
• Coverage and responses of all critical system components.
• Reference or inclusion of incident response procedures from the payment brands.
**Defined Approach Testing Procedures:**
- "12.10.1.a": Examine the incident response plan to verify that the plan exists and includes at least the elements specified in this requirement.
- "12.10.1.b": Interview personnel and examine documentation from previously reported incidents or alerts to verify that the documented incident response plan and procedures were followed.
**Customized Approach Objective:**A comprehensive incident response plan that meets card brand expectations is maintained.
**Guidance - Purpose:**Without a comprehensive incident response plan that is properly disseminated, read, and understood by the parties responsible, confusion and lack of a unified response could create further downtime for the business, unnecessary public media exposure, as well as risk of financial and/or reputational loss and legal liabilities.
**Guidance - Good Practice:**The incident response plan should be thorough and contain all the key elements for stakeholders (for example, legal, communications) to allow the entity to respond effectively in the event of a breach that could impact account data. It is important to keep the plan up to date with current contact information of all individuals designated as having a role in incident response. Other relevant parties for notifications may include customers, financial institutions (acquirers and issuers), and business partners. Entities should consider how to address all compromises of data within the CDE in their incident response plans, including compromises to account data, wireless encryption keys, encryption keys used for transmission and storage or account data or cardholder data, etc.
**Guidance - Examples:**Legal requirements for reporting compromises include those in most US states, the EU General Data Protection Regulation (GDPR), and the Personal Data Protection Act (Singapore).
**Guidance - Further Information:**For more information, refer to the NIST SP 800- 61 Rev. 2, Computer Security Incident Handling Guide .

---
**Control objectives:**12.10
**Sub-requirement:**12.10.2
**Defined Approach Requirements:**At least once every 12 months, the security incident response plan is:
• Reviewed and the content is updated as needed.
• Tested, including all elements listed in Requirement 12.10.1.
**Defined Approach Testing Procedures:**Interview personnel and review documentation to verify that, at least once every 12 months, the security incident response plan is:
• Reviewed and updated as needed.
• Tested, including all elements listed in Requirement 12.10.1.
**Customized Approach Objective:**The incident response plan is kept current and tested periodically.
**Guidance - Purpose:**Proper testing of the security incident response plan can identify broken business processes and ensure key steps are not missed, which could result in increased exposure during an incident. Periodic testing of the plan ensures that the processes remain viable, as well as ensuring that all relevant personnel in the organization are familiar with the plan.
**Guidance - Good Practice:**The test of the incident response plan can include simulated incidents and the corresponding responses in the form of a 'table-top exercise' that includes participation by relevant personnel. A review of the incident and the quality of the response can provide entities with the assurance that all required elements are included in the plan.

---
**Control objectives:**12.10
**Sub-requirement:**12.10.3
**Defined Approach Requirements:**Specific personnel are designated to be available on a 24/7 basis to respond to suspected or confirmed security incidents.
**Defined Approach Testing Procedures:**Examine documentation and interview responsible personnel occupying designated roles to verify that specific personnel are designated to be available on a 24/7 basis to respond to security incidents.
**Customized Approach Objective:**Incidents are responded to immediately where appropriate.
**Guidance - Purpose:**An incident could occur at any time, therefore if a person who is trained in incident response and familiar with the entity's plan is available when an incident is detected, the entity's ability to correctly respond to the incident is increased.
**Guidance - Good Practice:**Often, specific personnel are designated to be part of a security incident response team, with the team having overall responsibility for responding to incidents (perhaps on a rotating schedule basis) and managing those incidents in accordance with the plan. The incident response team can consist of core members who are permanently assigned or 'on-demand' personnel who may be called up as necessary, depending on their expertise and the specifics of the incident. Having available resources to respond quickly to incidents minimizes disruption to the organization. Examples** **of types of activity the team or individuals should respond to include any evidence of unauthorized activity, detection of unauthorized wireless access points, critical IDS alerts, and reports of unauthorized critical system or content file changes.

---
**Control objectives:**12.10
**Sub-requirement:**12.10.4
**Defined Approach Requirements:**Personnel responsible for responding to suspected and confirmed security incidents are appropriately and periodically trained on their incident response responsibilities.
**Defined Approach Testing Procedures:** Examine training documentation and interview incident response personnel to verify that personnel are appropriately and periodically trained on their incident response responsibilities.
**Customized Approach Objective:**Personnel are knowledgeable about their role and responsibilities in incident response and are able to access assistance and guidance when required.
**Guidance - Purpose:**Without a trained and readily available incident response team, extended damage to the network could occur, and critical data and systems may become 'polluted' by inappropriate handling of the targeted systems. This can hinder the success of a post-incident investigation.
**Guidance - Good Practice:**It is important that all personnel involved in incident response are trained and knowledgeable about managing evidence for forensics and investigations.

---
**Control objectives:**12.10
**Sub-requirement:**12.10.4.1
**Defined Approach Requirements:**The frequency of periodic training for incident response personnel is defined in the entity's targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1.
**Defined Approach Testing Procedures:**
- "12.10.4.1.a": Examine the entity's targeted risk analysis for the frequency of training for incident response personnel to verify the risk analysis was performed in accordance with all elements specified in Requirement 12.3.1.
- "12.10.4.1.b": Examine documented results of periodic training of incident response personnel and interview personnel to verify training is performed at the frequency defined in the entity's targeted risk analysis performed for this requirement.
**Customized Approach Objective:**Incident response personnel are trained at a frequency that addresses the entity's risk.
**Applicability Notes:** This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Each entity's environment and incident response plan are different, and the approach will depend on a number of factors, including the size and complexity of the entity, the degree of change in the environment, the size of the incident response team, and the turnover in personnel. Performing a risk analysis will allow the entity to determine the optimum frequency for training personnel with incident response responsibilities.

---
**Control objectives:**12.10
**Sub-requirement:**12.10.5
**Defined Approach Requirements:**The security incident response plan includes monitoring and responding to alerts from security monitoring systems, including but not limited to:
• Intrusion-detection and intrusion-prevention systems.
• Network security controls.
• Change-detection mechanisms for critical files.
• The change-and tamper-detection mechanism for payment pages. This bullet is a best practice until its effective date; refer to Applicability Notes below for details.
• Detection of unauthorized wireless access points.
**Defined Approach Testing Procedures:**Examine documentation and observe incident response processes to verify that monitoring and responding to alerts from security monitoring systems are covered in the security incident response plan, including but not limited to the systems specified in this requirement.
**Customized Approach Objective:**Alerts generated by monitoring and detection technologies are responded to in a structured, repeatable manner.
**Applicability Notes:**The bullet above (for monitoring and responding to alerts from a change- and tamper-detection mechanism for payment pages) is a best practice until 31 March 2025, after which it will be required as part of Requirement 12.10.5 and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Responding to alerts generated by security monitoring systems that are explicitly designed to focus on potential risk to data is critical to prevent a breach and therefore, this must be included in the incident-response processes.

---
**Control objectives:**12.10
**Sub-requirement:**12.10.6
**Defined Approach Requirements:**The security incident response plan is modified and evolved according to lessons learned and to incorporate industry developments.
**Defined Approach Testing Procedures:**
- "12.10.6.a": Examine policies and procedures to verify that processes are defined to modify and evolve the security incident response plan according to lessons learned and to incorporate industry developments.
- "12.10.6.b": Examine the security incident response plan and interview responsible personnel to verify that the incident response plan is modified and evolved according to lessons learned and to incorporate industry developments.
**Customized Approach Objective:**The effectiveness and accuracy of the incident response plan is reviewed and updated after each invocation.
**Guidance - Purpose:**Incorporating lessons learned into the incident response plan after an incident occurs and in-step with industry developments, helps keep the plan current and able to react to emerging threats and security trends.
**Guidance - Good Practice:**The lessons-learned exercise should include all levels of personnel. Although it is often included as part of the review of the entire incident, it should focus on how the entity's response to the incident could be improved. It is important to not just consider elements of the response that did not have the planned outcomes but also to understand what worked well and whether lessons from those elements that worked well can be applied to areas of the plan that did not. Another way to optimize an entity's incident response plan is to understand the attacks made against other organizations and use that information to fine-tune the entity's detection, containment, mitigation, or recovery procedures.

---
**Control objectives:**12.10
**Sub-requirement:**12.10.7
**Defined Approach Requirements:**Incident response procedures are in place, to be initiated upon the detection of stored PAN anywhere it is not expected, and include:
• Determining what to do if PAN is discovered outside the CDE, including its retrieval, secure deletion, and/or migration into the currently defined CDE, as applicable.
• Identifying whether sensitive authentication data is stored with PAN.
• Determining where the account data came from and how it ended up where it was not expected.
• Remediating data leaks or process gaps that resulted in the account data being where it was not expected.
**Defined Approach Testing Procedures:**
- "12.10.7.a": Examine documented incident response procedures to verify that procedures for responding to the detection of stored PAN anywhere it is not expected to exist, ready to be initiated, and include all elements specified in this requirement.
- "12.10.7.b": Interview personnel and examine records of response actions to verify that incident response procedures are performed upon detection of stored PAN anywhere it is not expected.
**Customized Approach Objective:**Processes are in place to quickly respond, analyze, and address situations in the event that cleartext PAN is detected where it is not expected.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Having documented incident response procedures that are followed in the event that stored PAN is found anywhere it is not expected to be, helps to identify the necessary remediation actions and prevent future leaks.
**Guidance - Good Practice:**If PAN was found outside the CDE, analysis should be performed to 1) determine whether it was saved independently of other data or with sensitive authentication data, 2) identify the source of the data, and 3) identify the control gaps that resulted in the data being outside the CDE. Entities should consider whether there are contributory factors, such as business processes, user behavior, improper system configurations, etc. that caused the PAN to be stored in an unexpected location. If such contributory factors are present, they should be addressed per this Requirement to prevent recurrence.