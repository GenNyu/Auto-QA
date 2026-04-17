### A. Tài liệu gốc của Chương 5 (Control 5.24, 5.25, 5.26)

### B. Summary Overview của Chương 5 (Control 5.24, 5.25, 5.26)
Tài liệu này mô tả chi tiết **mục 5.24, 5.25 và 5.26** trong **Chương 5 (Organizational controls)** của **ISO/IEC 27002:2022**, tập trung vào việc xử lý sự cố an toàn thông tin từ khâu chuẩn bị quy trình đến đánh giá sự kiện và phản ứng theo thủ tục đã được tài liệu hóa.
Mục tiêu là bảo đảm việc xử lý sự cố diễn ra nhanh, nhất quán, có vai trò trách nhiệm rõ ràng và có thể phối hợp hiệu quả giữa các bên liên quan.
Gồm 3 mục chính:
- `5.24`: Information security incident management planning and preparation - lập kế hoạch, chuẩn bị và phân công trách nhiệm cho quản lý sự cố.
- `5.25`: Assessment and decision on information security events - đánh giá sự kiện an toàn thông tin để quyết định có phải sự cố hay không.
- `5.26`: Response to information security incidents - phản ứng theo thủ tục đã được tài liệu hóa.

Áp dụng cho các bộ phận chịu trách nhiệm tiếp nhận, đánh giá, xử lý và báo cáo sự cố an toàn thông tin.

### C. Key Points của Chương 5 (Control 5.24, 5.25, 5.26)
- **Mục tiêu quản trị:** Thiết lập quy trình và trách nhiệm rõ ràng để tổ chức phản ứng sự cố nhất quán.
- **Yêu cầu chính của 5.24-5.26:** Phải có kế hoạch quản lý sự cố, cơ chế đánh giá sự kiện và thủ tục phản ứng đã được phê duyệt.
- **Điểm vận hành quan trọng:** Cần có đầu mối tiếp nhận, quy trình phân loại, cơ chế escalation, ghi log và lưu bằng chứng.
- **Lưu ý thực tế:** Nếu phân công trách nhiệm mơ hồ hoặc đánh giá chậm, sự cố dễ kéo dài và lan rộng sang các bên liên quan.

### D. Deep Summary của Chương 5 (Control 5.24, 5.25, 5.26)
**Bối cảnh:**
Đây là chuỗi control dùng để xây dựng một luồng xử lý sự cố hoàn chỉnh: chuẩn bị trước, phân loại đúng và phản ứng có kiểm soát. Giá trị chính của nhóm này nằm ở khả năng tổ chức vận hành, ghi nhận bằng chứng và phối hợp nhiều bên khi sự cố xảy ra.

**Nội dung cốt lõi:**
- 5.24 yêu cầu tổ chức chuẩn bị quy trình, vai trò, đào tạo và kênh báo cáo trước khi sự cố xảy ra.
- 5.25 đặt ra cơ chế đánh giá để phân loại sự kiện một cách nhất quán, tránh nhầm lẫn giữa sự kiện và sự cố.
- 5.26 yêu cầu phản ứng theo thủ tục, gồm cô lập, thu thập bằng chứng, escalation, phối hợp và đóng sự cố có kiểm soát.
- Ba control này vận hành theo chuỗi: chuẩn bị tốt thì đánh giá nhanh, đánh giá đúng thì phản ứng mới hiệu quả.

**Dữ liệu đáng chú ý:**
- 5.24 gắn với control type `Corrective`, nhấn mạnh năng lực quản trị và xử lý sự cố.
- 5.25 là `Detective`, đặt trọng tâm vào phân loại và quyết định trước khi phản ứng.
- 5.26 quay lại `Corrective`, tập trung vào `Respond` và `Recover`.
- Nhóm control này cũng đòi hỏi phối hợp nội bộ và bên ngoài khi sự cố vượt ra ngoài phạm vi một đơn vị.

**Rủi ro / Lưu ý:**
- Nếu không có đầu mối rõ ràng, sự cố dễ bị bỏ sót hoặc xử lý chồng chéo.
- Nếu không ghi nhận và lưu bằng chứng kịp thời, việc điều tra nguyên nhân và chứng minh tuân thủ sẽ yếu.
- Nếu thủ tục escalation và truyền thông không rõ, sự cố có thể lan sang các bên liên quan hoặc vượt quá thời gian phản ứng chấp nhận được.

### E. Structured Output của Chương 5 (Control 5.24, 5.25, 5.26)
**Section:** 5.24
**Title:** Information security incident management planning and preparation

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Corrective |
| Information security properties | #Confidentiality#Integrity#Availability |
| Cybersecurity concepts | #Respond #Recover |
| Operational capabilities | #Governance#Information_security_event_management |
| Security domains | #Defence |

**Control:**
The organization should plan and prepare for managing information security incidents by defining, establishing and communicating information security incident management processes, roles and responsibilities.

**Purpose:**
To ensure quick, effective, consistent and orderly response to information security incidents, including communication on information security events.

**Guidance:**
***Roles and responsibilities:***
The organization should establish appropriate information security incident management processes. Roles and responsibilities to carry out the incident management procedures should be determined and effectively communicated to the relevant internal and external interested parties.
***The following should be considered:***
- establishing a common method for reporting information security events including point of contact (see 6.8);
- establishing an incident management process to provide the organization with capability for managing information security incidents including administration, documentation, detection, triage, prioritization, analysis, communication and coordinating interested parties;
- establishing an incident response process to provide the organization with capability for assessing, responding to and learning from information security incidents;
- only allowing competent personnel to handle the issues related to information security incidents within the organization. Such personnel should be provided with procedure documentation and periodic training;
- establishing a process to identify required training, certification and ongoing professional development for incident response personnel.

***Incident management procedures:***
The objectives for information security incident management should be agreed with management and it should be ensured that those responsible for information security incident management understand the organization’s priorities for handling information security incidents including resolution time frame based on potential consequences and severity. Incident management procedures should be implemented to meet these objectives and priorities.
Management should ensure that an information security incident management plan is created considering different scenarios and procedures are developed and implemented for the following activities:
- evaluation of information security events according to criteria for what constitutes an information security incident;
- monitoring (see 8.15 and 8.16), detecting (see 8.16), classifying (see 5.25), analysing and reporting (see 6.8) of information security events and incidents (by human or automatic means);
- managing information security incidents to conclusion, including response and escalation (see 5.26), according to the type and the category of the incident, possible activation of crisis management and activation of continuity plans, controlled recovery from an incident and communication to internal and external interested parties;
- coordination with internal and external interested parties such as authorities, external interest groups and forums, suppliers and clients (see 5.5 and 5.6);
- logging incident management activities;
- handling of evidence (see 5.28);
- root cause analysis or post-mortem procedures;
- identification of lessons learned and any improvements to the incident management procedures or information security controls in general that are required.

***Reporting procedures:***
Reporting procedures should include:
- actions to be taken in case of an information security event (e.g. noting all pertinent details immediately such as malfunction occurring and messages on screen, immediately reporting to the point of contact and only taking coordinated actions);
- use of incident forms to support personnel to perform all necessary actions when reporting information security incidents;
- suitable feedback processes to ensure that those persons reporting information security events are notified, to the extent possible, of outcomes after the issue has been addressed and closed;
- creation of incident reports.

Any external requirements on reporting of incidents to relevant interested parties within the defined time frame (e.g. breach notification requirements to regulators) should be considered when implementing incident management procedures.

**Other information:**
Information security incidents can transcend organizational and national boundaries. To respond to such incidents, it is beneficial to coordinate response and share information about these incidents with external organizations as appropriate.
Detailed guidance on information security incident management is provided in the ISO/IEC 27035 series.

---
**Section:** 5.25
**Title:** Assessment and decision on information security events

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Detective |
| Information security properties | #Confidentiality#Integrity#Availability |
| Cybersecurity concepts | #Detect #Respond |
| Operational capabilities | #Information_security_event_management |
| Security domains | #Defence |

**Control:**
The organization should assess information security events and decide if they are to be categorized as information security incidents.

**Purpose:**
To ensure effective categorization and prioritization of information security events.

**Guidance:**
A categorization and prioritization scheme of information security incidents should be agreed for the identification of the consequences and priority of an incident. The scheme should include the criteria to categorize events as information security incidents. The point of contact should assess each information security event using the agreed scheme.
Personnel responsible for coordinating and responding to information security incidents should perform the assessment and make a decision on information security events.
Results of the assessment and decision should be recorded in detail for the purpose of future reference and verification.

**Other information:**
The ISO/IEC 27035 series provides further guidance on incident management.

---
**Section:** 5.26
**Title:** Response to information security incidents

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Corrective |
| Information security properties | #Confidentiality#Integrity#Availability |
| Cybersecurity concepts | #Respond #Recover |
| Operational capabilities | #Information_security_event_management |
| Security domains | #Defence |

**Control:**
Information security incidents should be responded to in accordance with the documented procedures.

**Purpose:**
To ensure efficient and effective response to information security incidents.

**Guidance:**
The organization should establish and communicate procedures on information security incident response to all relevant interested parties.
Information security incidents should be responded to by a designated team with the required competency (see 5.24).
The response should include the following:
- containing, if the consequences of the incident can spread, the systems affected by the incident;
- collecting evidence (see 5.28) as soon as possible after the occurrence;
- escalation, as required including crisis management activities and possibly invoking business continuity plans (see 5.29 and 5.30);
- ensuring that all involved response activities are properly logged for later analysis;
- communicating the existence of the information security incident or any relevant details thereof to all relevant internal and external interested parties following the need-to-know principle;
- coordinating with internal and external parties such as authorities, external interest groups and forums, suppliers and clients to improve response effectiveness and help to minimize consequences for other organizations;
- once the incident has been successfully addressed, formally closing and recording it;
- conducting information security forensic analysis, as required (see 5.28);
- performing post-incident analysis to identify root cause. Ensure it is documented and communicated according to defined procedures (see 5.27);
- identifying and managing information security vulnerabilities and weaknesses including those related to controls which have caused, contributed to or failed to prevent the incident.

**Other information:**
The ISO/IEC 27035 series provides further guidance on incident management.