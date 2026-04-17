### A. Tài liệu gốc của Requirement 11

### B. Summary Overview của Control Objective 11.4
Tài liệu này mô tả chi tiết **Control Objective 11.4** của **Requirement 11** trong **PCI-DSS v4.0.1**, tập trung vào việc thực hiện penetration testing để đánh giá khả năng phòng thủ của hệ thống trước các tấn công thực tế.
Mục tiêu chính là đảm bảo các lỗ hổng có thể khai thác được được phát hiện thông qua kiểm thử mô phỏng tấn công và được khắc phục kịp thời.
Gồm 7 sub-requirement chính:
- 11.4.1: Xây dựng phương pháp pentest
- 11.4.2: Thực hiện internal pentest
- 11.4.3: Thực hiện external pentest
- 11.4.4: Khắc phục lỗ hổng
- 11.4.5: Kiểm thử segmentation
- 11.4.6: Segmentation cho Service Provider
- 11.4.7: Hỗ trợ Multi-tenant Service Provider
Áp dụng cho toàn bộ hệ thống, mạng và CDE trong môi trường.

### C. Key Points của Control Objective 11.4
- **Phạm vi áp dụng:**Toàn bộ hệ thống, ứng dụng và môi trường dữ liệu chủ thẻ (CDE)
- **Trách nhiệm:**Tài liệu hóa phương pháp và thực hiện kiểm thử bởi nhân sự có năng lực, đảm bảo tính độc lập về mặt tổ chức
- **Phương pháp:**Áp dụng các phương pháp kiểm thử theo chuẩn công nghiệp như OWASP hoặc OSSTMM
- **Kiểm thử định kỳ:**Thực hiện ít nhất mỗi 12 tháng và ngay sau khi có các thay đổi lớn về hạ tầng hoặc ứng dụng

### D. Deep Summary của Control Objective 11.4
**Bối cảnh:**
Penetration testing giúp mô phỏng hành vi của kẻ tấn công thực tế để phát hiện các điểm yếu và chuỗi khai thác mà các phương pháp quét tự động không thể nhận diện được
**Nội dung cốt lõi:**
- Phương pháp toàn diện: Phải xây dựng methodology bao quát cả lớp mạng (network layer) và lớp ứng dụng (application layer)
- Kiểm thử đa chiều: Thực hiện đánh giá từ cả bên trong và bên ngoài mạng, bao gồm cả các hệ thống quan trọng và điểm biên CDE
- Xác minh phân tách: Kiểm tra tính hiệu quả của các biện pháp chia phân vùng (segmentation) để đảm bảo các hệ thống ngoài phạm vi không thể truy cập vào CDE
- Khắc phục và tái kiểm tra: Các lỗ hổng phát hiện được phải được xử lý dựa trên đánh giá rủi ro và thực hiện kiểm thử lại để xác nhận kết quả khắc phục
**Dữ liệu đáng chú ý:**
- Kết quả kiểm thử và hoạt động khắc phục lỗ hổng phải được lưu giữ ít nhất 12 tháng
- Đối với Service Provider, việc kiểm thử segmentation phải thực hiện ít nhất 6 tháng một lần
**Rủi ro / Lưu ý:**
- Chỉ thực hiện quét (scan) mà không thực hiện khai thác thử nghiệm (exploit) sẽ dẫn đến việc đánh giá thiếu hiệu quả và bỏ sót lỗ hổng thực tế
- Nếu không kiểm tra tính hiệu quả của segmentation, tổ chức dễ bị tấn công leo thang hoặc di chuyển ngang (lateral movement) từ các vùng mạng kém an toàn
- Việc sử dụng tester không đủ năng lực hoặc không có tính độc lập sẽ khiến kết quả kiểm thử không khách quan và không đáng tin cậy

### E. Structured Output của Control Objective 11.4
**Control objectives:**11.4
**Sub-requirement:**11.4.1
**Defined Approach Requirements:**A penetration testing methodology is defined, documented, and implemented by the entity, and includes:
• Industry-accepted penetration testing approaches.
• Coverage for the entire CDE perimeter and critical systems.
• Testing from both inside and outside the network.
• Testing to validate any segmentation and scope- reduction controls.
• Application-layer penetration testing to identify, at a minimum, the vulnerabilities listed in Requirement 6.2.4.
• Network-layer penetration tests that encompass all components that support network functions as well as operating systems.
• Review and consideration of threats and vulnerabilities experienced in the last 12 months.
• Documented approach to assessing and addressing the risk posed by exploitable vulnerabilities and security weaknesses found during penetration testing. Retention of penetration testing results and remediation activities results for at least 12 months.
**Defined Approach Testing Procedures:**Examine documentation and interview personnel to verify that the penetration-testing methodology defined, documented, and implemented by the entity includes all elements specified in this requirement.
**Customized Approach Objective:**A formal methodology is defined for thorough technical testing that attempts to exploit vulnerabilities and security weaknesses via simulated attack methods by a competent manual attacker.
**Applicability Notes:** Testing from inside the network (or 'internal penetration testing') means testing from both inside the CDE and into the CDE from trusted and untrusted internal networks. Testing from outside the network (or 'external penetration testing') means testing the exposed external perimeter of trusted networks, and critical systems connected to or accessible to public network infrastructures.
**Guidance - Purpose:**Attackers spend a lot of time finding external and internal vulnerabilities to leverage to obtain access to cardholder data and then to exfiltrate that data. As such, entities need to test their networks thoroughly, just as an attacker would do. This testing allows the entity to identify and remediate weakness that might be leveraged to compromise the entity's network and data, and then to take appropriate actions to protect the network and system components from such attacks.
**Guidance - Good Practice:**Penetration testing techniques will differ based on an organization's needs and structure and should be suitable for the tested environment-for example, fuzzing, injection, and forgery tests might be appropriate. The type, depth, and complexity of the testing will depend on the specific environment and the needs of the organization.
**Guidance - Definitions:**Penetration tests simulate a real-world attack situation intending to identify how far an attacker could penetrate an environment, given differing amounts of information provided to the tester. This allows an entity to better understand its potential exposure and develop a strategy to defend against attacks. A penetration test differs from a vulnerability scan, as a penetration test is an active process that usually includes exploiting identified vulnerabilities.
Scanning for vulnerabilities alone is not a penetration test, nor is a penetration test adequate if the focus is solely on trying to exploit vulnerabilities found in a vulnerability scan. Conducting a vulnerability scan may be one of the first steps, but it is not the only step a penetration tester will perform to plan the testing strategy. Even if a vulnerability scan does not detect known vulnerabilities, the penetration tester will often gain enough knowledge about the system to identify possible security gaps. Penetration testing is a highly manual process. While some automated tools may be used, the tester uses their knowledge of systems to gain access into an environment. Often the tester will chain several types of exploits together with the goal of breaking through layers of defenses. For example, if the tester finds a way to gain access to an application server, the tester will then use the compromised server as a point to stage a new attack based on the resources to which the server has access. In this way, a tester can simulate the techniques used by an attacker to identify areas of potential weakness in the environment. The testing of security monitoring and detection methods-for example, to confirm the effectiveness of logging and file integrity monitoring mechanisms, should also be considered. Scanning for vulnerabilities alone is not a penetration test, nor is a penetration test adequate if the focus is solely on trying to exploit vulnerabilities found in a vulnerability scan. Conducting a vulnerability scan may be one of the first steps, but it is not the only step a penetration tester will perform to plan the testing strategy. Even if a vulnerability scan does not detect known vulnerabilities, the penetration tester will often gain enough knowledge about the system to identify possible security gaps. Penetration testing is a highly manual process. While some automated tools may be used, the tester uses their knowledge of systems to gain access into an environment. Often the tester will chain several types of exploits together with the goal of breaking through layers of defenses. For example, if the tester finds a way to gain access to an application server, the tester will then use the compromised server as a point to stage a new attack based on the resources to which the server has access. In this way, a tester can simulate the techniques used by an attacker to identify areas of potential weakness in the environment. The testing of security monitoring and detection methods-for example, to confirm the effectiveness of logging and file integrity monitoring mechanisms, should also be considered.
**Guidance - Further Information:**Refer to the Information Supplement: Penetration Testing Guidance for additional guidance. Industry-accepted penetration testing approaches include: The Open Source Security Testing Methodology and Manual (OSSTMM) Open Web Application Security Project (OWASP) penetration testing programs.

---
**Control objectives:**11.4
**Sub-requirement:**11.4.2
**Defined Approach Requirements:**Internal penetration testing is performed:
• Per the entity's defined methodology,
• At least once every 12 months
• After any significant infrastructure or application upgrade or change
• By a qualified internal resource or qualified external third-party
• Organizational independence of the tester exists (not required to be a QSA or ASV).
**Defined Approach Testing Procedures:**
- "11.4.2.a": Examine the scope of work and results from the most recent internal penetration test to verify that penetration testing is performed in accordance with all elements specified in this requirement.
- "11.4.2.b": Interview personnel to verify that the internal penetration test was performed by a qualified internal resource or qualified external third-party and that organizational independence the tester exists (not required to be a QSA or ASV).
**Customized Approach Objective:**Internal system defenses are verified by technical testing according to the entity's defined methodology as frequently as needed to address evolving and new attacks and threats and ensure that significant changes do not introduce unknown vulnerabilities.
**Guidance - Purpose:**Internal penetration testing serves two purposes. Firstly, just like an external penetration test, it discovers vulnerabilities and misconfigurations that could be used by an attacker that had managed to get some degree of access to the internal network, whether that is because the attacker is an authorized user conducting unauthorized activities, or an external attacker that had managed to penetrate the entity's perimeter. Secondly, internal penetration testing also helps entities to discover where their change control process failed by detecting previously unknown systems. Additionally, it verifies the status of many of the controls operating within the CDE. A penetration test is not truly a 'test' because the outcome of a penetration test is not something that can be classified as a 'pass' or a 'fail.' The best outcome of a test is a catalog of vulnerabilities and misconfigurations that an entity did not know about, and the penetration tester found them before an attacker could. A penetration test that found nothing is typically indicative of shortcomings of the penetration tester, rather than being a positive reflection of the security posture of the entity.
**Guidance - Good Practice:**Some considerations when choosing a qualified resource to perform penetration testing include:
• Specific penetration testing certifications, which may be an indication of the tester's skill level and competence.
• Prior experience conducting penetration testing—for example, the number of years of experience, and the type and scope of prior engagements can help confirm whether the tester's experience is appropriate for the needs of the engagement.
**Guidance - Further Information:** Refer to the Information Supplement: Penetration Testing Guidance on the PCI SSC website for additional guidance.

---
**Control objectives:**11.4
**Sub-requirement:**11.4.3
**Defined Approach Testing Procedures:**
- "11.4.3.a": Examine the scope of work and results from the most recent external penetration test to verify that penetration testing is performed according to all elements specified in this requirement.
- "11.4.3.b": Interview personnel to verify that the external penetration test was performed by a qualified internal resource or qualified external third party and that organizational independence of the tester exists (not required to be a QSA or ASV).
**Customized Approach Objective:** External system defenses are verified by technical testing according to the entity's defined methodology as frequently as needed to address evolving and new attacks and threats, and to ensure that significant changes do not introduce unknown vulnerabilities.
**Guidance - Purpose:**Internal penetration testing serves two purposes. Firstly, just like an external penetration test, it discovers vulnerabilities and misconfigurations that could be used by an attacker that had managed to get some degree of access to the internal network, whether that is because the attacker is an authorized user conducting unauthorized activities, or an external attacker that had managed to penetrate the entity's perimeter. Secondly, internal penetration testing also helps entities to discover where their change control process failed by detecting previously unknown systems. Additionally, it verifies the status of many of the controls operating within the CDE. A penetration test is not truly a 'test' because the outcome of a penetration test is not something that can be classified as a 'pass' or a 'fail.' The best outcome of a test is a catalog of vulnerabilities and misconfigurations that an entity did not know about, and the penetration tester found them before an attacker could. A penetration test that found nothing is typically indicative of shortcomings of the penetration tester, rather than being a positive reflection of the security posture of the entity.
**Guidance - Good Practice:**Some considerations when choosing a qualified resource to perform penetration testing include:
• Specific penetration testing certifications, which may be an indication of the tester's skill level and competence.
• Prior experience conducting penetration testing—for example, the number of years of experience, and the type and scope of prior engagements can help confirm whether the tester's experience is appropriate for the needs of the engagement.
**Guidance - Further Information:** Refer to the Information Supplement: Penetration Testing Guidance on the PCI SSC website for additional guidance.

---
**Control objectives:**11.4
**Sub-requirement:**11.4.4
**Defined Approach Requirements:**Exploitable vulnerabilities and security weaknesses found during penetration testing are corrected as follows:
• In accordance with the entity's assessment of the risk posed by the security issue as defined in Requirement 6.3.1.
• Penetration testing is repeated to verify the corrections. Customized Approach Objective Vulnerabilities and security weaknesses found while verifying system defenses are mitigated.
**Defined Approach Testing Procedures:**Examine penetration testing results to verify that noted exploitable vulnerabilities and security weaknesses were corrected in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Vulnerabilities and security weaknesses found while verifying system defenses are mitigated.
**Guidance - Purpose:**The results of a penetration test are usually a prioritized list of vulnerabilities discovered by the exercise. Often a tester will have chained a number of vulnerabilities together to compromise a system component. Remediating the vulnerabilities found by a penetration test significantly reduces the probability that the same vulnerabilities will be exploited by a malicious attacker. Using the entity's own vulnerability risk assessment process (see requirement 6.3.1) ensures that the vulnerabilities that pose the highest risk to the entity will be remediated more quickly.
**Guidance - Good Practice:**As part of the entity's assessment of risk, entities should consider how likely the vulnerability is to be exploited and whether there are other controls present in the environment to reduce the risk. Any weaknesses that point to PCI DSS requirements not being met should be addressed.

---
**Control objectives:**11.4
**Sub-requirement:**11.4.5
**Defined Approach Requirements:**If segmentation is used to isolate the CDE from other networks, penetration tests are performed on segmentation controls as follows:
• At least once every 12 months and after any changes to segmentation controls/methods
• Covering all segmentation controls/methods in use.
• According to the entity's defined penetration testing methodology.
• Confirming that the segmentation controls/methods are operational and effective, and isolate the CDE from all out-of-scope systems.
• Confirming effectiveness of any use of isolation to separate systems with differing security levels (see Requirement 2.2.3).
• Performed by a qualified internal resource or qualified external third party.
• Organizational independence of the tester exists (not required to be a QSA or ASV).
**Defined Approach Testing Procedures:**
- "11.4.5.a": Examine segmentation controls and review penetration-testing methodology to verify that penetration-testing procedures are defined to test all segmentation methods in accordance with all elements specified in this requirement.
- "11.4.5.b": Examine the results from the most recent penetration test to verify the penetration test covers and addresses all elements specified in this requirement.
- "11.4.5.c": Interview personnel to verify that the test was performed by a qualified internal resource or qualified external third party and that organizational independence of the tester exists (not required to be a QSA or ASV).
**Customized Approach Objective:**If segmentation is used, it is verified periodically by technical testing to be continually effective, including after any changes, in isolating the CDE from all out-of-scope systems.
**Guidance - Purpose:**When an entity uses segmentation controls to isolate the CDE from internal untrusted networks, the security of the CDE is dependent on that segmentation functioning. Many attacks have involved the attacker moving laterally from what an entity deemed an isolated network into the CDE. Using penetration testing tools and techniques to validate that an untrusted network is indeed isolated from the CDE can alert the entity to a failure or misconfiguration of the segmentation controls, which can then be rectified.
**Guidance - Good Practice:**Techniques such as host discovery and port scanning can be used to verify out-of-scope segments have no access to the CDE.

---
**Control objectives:**11.4
**Sub-requirement:**11.4.6
**Defined Approach Requirements:**Additional requirement for service providers only: If segmentation is used to isolate the CDE from other networks, penetration tests are performed on segmentation controls as follows:
• At least once every six months and after any changes to segmentation controls/methods.
• Covering all segmentation controls/methods in use.
• According to the entity's defined penetration testing methodology.
• Confirming that the segmentation controls/methods are operational and effective, and isolate the CDE from all out-of-scope systems.
• Confirming effectiveness of any use of isolation to separate systems with differing security levels (see Requirement 2.2.3).
• Performed by a qualified internal resource or qualified external third party.
• Organizational independence of the tester exists (not required to be a QSA or ASV).
**Defined Approach Testing Procedures:**
- "11.4.6.a": Additional testing procedure for service provider assessments only: Examine the results from the most recent penetration test to verify that the penetration covers and addressed all elements specified in this requirement.
- "11.4.6.b": Additional testing procedure for service provider assessments only: Interview personnel to verify that the test was performed by a qualified internal resource or qualified external third party and that organizational independence of the tester exists (not required to be a QSA or ASV).
**Customized Approach Objective:** If segmentation is used, it is verified by technical testing to be continually effective, including after any changes, in isolating the CDE from out-of-scope systems.
**Applicability Notes:** This requirement applies only when the entity being assessed is a service provider.
**Guidance - Purpose:**Service providers typically have access to greater volumes of cardholder data or can provide an entry point that can be exploited to then compromise multiple other entities. Service providers also typically have larger and more complex networks that are subject to more frequent change. The probability of segmentation controls failing in complex and dynamic networks is greater in service-provider environments. Validating segmentation controls more frequently is likely to discover such failings before they can be exploited by an attacker attempting to pivot laterally from an out-of-scope untrusted network to the CDE.
**Guidance - Good Practice:**Although the requirement specifies that this scope validation is carried out at least once every six months and after significant change, this exercise should be performed as frequently as possible to ensure it remains effective at isolating the CDE from other networks.

---
**Control objectives:**11.4
**Sub-requirement:**11.4.7
**Defined Approach Requirements:**Additional requirement for multi-tenant service providers only: Multi-tenant service providers support their customers for external penetration testing per Requirement 11.4.3 and 11.4.4.
**Defined Approach Testing Procedures:**Additional testing procedure for multi- tenant service providers only: Examine evidence to verify that multi-tenant service providers support their customers for external penetration testing Requirement 11.4.3 and 11.4.4.
**Customized Approach Objective:**Multi-tenant service providers support their customers' need for technical testing either by providing access or evidence that comparable technical testing has been undertaken.
**Applicability Notes:**This requirement applies only when the entity being assessed is a multi-tenant service provider. To meet this requirement, a multi-tenant service provider may either:
• Provide evidence to its customers to show that penetration testing has been performed according to Requirements 11.4.3 and 11.4.4 on the customers' subscribed infrastructure, or
• Provide prompt access to each of its customers, so customers can perform their own penetration testing.
Evidence provided to customers can include redacted penetration testing results but needs to include sufficient information to prove that all elements of Requirements 11.4.3 and 11.4.4 have been met on the customer's behalf. Refer also to Appendix A1: Additional PCI DSS Requirements for Multi-Tenant Service Providers . This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Entities need to conduct penetration tests in accordance with PCI DSS to simulate attacker behavior and discover vulnerabilities in their environment. In shared and cloud environments, the multi-tenant service provider may be concerned about the activities of a penetration tester affecting other customers' systems. Multi-tenant service providers cannot forbid penetration testing because this would leave their customers' systems open to exploitation. Therefore, multi-tenant service providers must support customer requests to conduct penetration testing or for penetration testing results.