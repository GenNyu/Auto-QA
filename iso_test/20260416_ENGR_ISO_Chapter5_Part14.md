### A. Tài liệu gốc của Chương 5 (Control 5.27, 5.28, 5.29)

### B. Summary Overview của Chương 5 (Control 5.27, 5.28, 5.29)
Tài liệu này mô tả chi tiết **mục 5.27, 5.28 và 5.29** trong **Chương 5 (Organizational controls)** của **ISO/IEC 27002:2022**, tập trung vào việc rút kinh nghiệm sau sự cố đến thu thập bằng chứng và duy trì an toàn thông tin khi hoạt động bị gián đoạn.
Mục tiêu là giảm khả năng lặp lại sự cố, bảo toàn bằng chứng khi cần điều tra hoặc xử lý kỷ luật/pháp lý, và duy trì mức bảo vệ phù hợp trong giai đoạn gián đoạn.
Gồm 3 mục chính:
- `5.27`: Learning from information security incidents - rút kinh nghiệm từ sự cố để cải thiện control và quy trình.
- `5.28`: Collection of evidence - thiết lập quy trình nhận diện, thu thập và bảo toàn bằng chứng.
- `5.29`: Information security during disruption - lập kế hoạch duy trì an toàn thông tin trong thời gian gián đoạn.

Áp dụng cho các cá nhân, bộ phận và vai trò liên quan đến điều tra sự cố, quản lý bằng chứng và vận hành liên tục.

### C. Key Points của Chương 5 (Control 5.27, 5.28, 5.29)
- **Mục tiêu quản trị:** Biến kinh nghiệm từ sự cố thành cải tiến thực tế cho control, quy trình và nhận thức người dùng.
- **Yêu cầu chính của 5.27-5.29:** Phải có cơ chế học từ sự cố, quy trình xử lý bằng chứng và kế hoạch duy trì an toàn khi gián đoạn.
- **Điểm vận hành quan trọng:** Cần đo lường loại sự cố, khối lượng, chi phí, trách nhiệm bảo toàn bằng chứng và các control bù trừ khi hoạt động bị ngắt quãng.
- **Lưu ý thực tế:** Nếu không ghi nhận và chuẩn hóa kinh nghiệm sau sự cố, tổ chức rất dễ lặp lại cùng một vấn đề dưới hình thức khác.

### D. Deep Summary của Chương 5 (Control 5.27, 5.28, 5.29)
**Bối cảnh:**
Đây là nhóm control giúp tổ chức khép kín vòng đời xử lý sự cố: học từ sự cố đã xảy ra, bảo toàn dữ liệu có giá trị pháp lý và giữ được mức bảo vệ chấp nhận được khi hệ thống hoặc dịch vụ bị gián đoạn.

**Nội dung cốt lõi:**
- 5.27 yêu cầu biến dữ liệu và bài học từ sự cố thành cải tiến cho control, nhận thức và quy trình phản ứng.
- 5.28 yêu cầu quy trình thu thập và bảo toàn bằng chứng đủ chặt để dùng cho điều tra, kỷ luật hoặc tranh tụng.
- 5.29 yêu cầu tổ chức chuẩn bị control bù trừ và kế hoạch duy trì mức an toàn phù hợp trong giai đoạn gián đoạn.
- Ba control này bổ sung nhau: học từ sự cố giúp phòng ngừa, bằng chứng giúp điều tra, còn kiểm soát trong gián đoạn giúp giảm tác động khi sự cố mở rộng sang vận hành.

**Dữ liệu đáng chú ý:**
- 5.27 gắn với `Preventive`, cho thấy trọng tâm là cải tiến và phòng ngừa lặp lại.
- 5.28 gắn với `Corrective`, phản ánh vai trò hỗ trợ điều tra và xử lý hậu quả.
- 5.29 gắn với `Preventive #Corrective`, vì vừa phòng ngừa mất kiểm soát vừa bù trừ khi vận hành bị gián đoạn.
- Cả ba control đều liên quan đến yêu cầu duy trì `Confidentiality`, `Integrity` và `Availability`, nhưng mức ưu tiên có thể thay đổi khi gián đoạn xảy ra.

**Rủi ro / Lưu ý:**
- Nếu không rút kinh nghiệm có hệ thống, tổ chức sẽ lặp lại lỗi cũ và làm tăng chi phí sự cố theo thời gian.
- Nếu không bảo toàn bằng chứng đúng cách, việc điều tra nguyên nhân hoặc bảo vệ lợi ích pháp lý có thể thất bại.
- Nếu không điều chỉnh control theo loại gián đoạn, các biện pháp bảo vệ có thể quá yếu hoặc không khả thi trong vận hành thực tế.

### E. Structured Output của Chương 5 (Control 5.27, 5.28, 5.29)
**Section:** 5.27
**Title:** Learning from information security incidents

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality#Integrity#Availability |
| Cybersecurity concepts | #Identify #Protect |
| Operational capabilities | #Information_security_event_management |
| Security domains | #Defence |

**Control:**
Knowledge gained from information security incidents should be used to strengthen and improve the information security controls.

**Purpose:**
To reduce the likelihood or consequences of future incidents.

**Guidance:**
The organization should establish procedures to quantify and monitor the types, volumes and costs of information security incidents.
The information gained from the evaluation of information security incidents should be used to:
- enhance the incident management plan including incident scenarios and procedures (see 5.24);
- identify recurring or serious incidents and their causes to update the organization’s information security risk assessment and determine and implement necessary additional controls to reduce the likelihood or consequences of future similar incidents. Mechanisms to enable that include collecting, quantifying and monitoring information about incident types, volumes and costs;
- enhance user awareness and training (see 6.3) by providing examples of what can happen, how to respond to such incidents and how to avoid them in the future.

**Other information:**
The ISO/IEC 27035 series provides further guidance.

---
**Section:** 5.28
**Title:** Collection of evidence

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Corrective |
| Information security properties | #Confidentiality#Integrity#Availability |
| Cybersecurity concepts | #Detect #Respond |
| Operational capabilities | #Information_security_event_management |
| Security domains | #Defence |

**Control:**
The organization should establish and implement procedures for the identification, collection, acquisition and preservation of evidence related to information security events.

**Purpose:**
To ensure a consistent and effective management of evidence related to information security incidents for the purposes of disciplinary and legal actions.

**Guidance:**
Internal procedures should be developed and followed when dealing with evidence related to information security events for the purposes of disciplinary and legal actions. The requirements of different jurisdictions should be considered to maximize chances of admission across the relevant jurisdictions.
In general, these procedures for the management of evidence should provide instructions for the identification, collection, acquisition and preservation of evidence in accordance with different types of storage media, devices and status of devices (i.e. powered on or off). Evidence typically needs to be collected in a manner that is admissible in the appropriate national courts of law or another disciplinary forum. It should be possible to show that:
- records are complete and have not been tampered with in any way;
- copies of electronic evidence are probably identical to the originals;
- any information system from which evidence has been gathered was operating correctly at the time the evidence was recorded.

Where available, certification or other relevant means of qualification of personnel and tools should be sought, so as to strengthen the value of the preserved evidence.
Digital evidence can transcend organizational or jurisdictional boundaries. In such cases, it should be ensured that the organization is entitled to collect the required information as digital evidence.

**Other information:**
When an information security event is first detected, it is not always obvious whether or not the event will result in court action. Therefore, the danger exists that necessary evidence is destroyed intentionally or accidentally before the seriousness of the incident is realized. It is advisable to involve legal advice or law enforcement early in any contemplated legal action and take advice on the evidence required.
ISO/IEC 27037 provides definitions and guidelines for identification, collection, acquisition and preservation of digital evidence.
The ISO/IEC 27050 series deals with electronic discovery, which involves the processing of electronically stored information as evidence.

---
**Section:** 5.29
**Title:** Information security during disruption

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive #Corrective |
| Information security properties | #Confidentiality#Integrity#Availability |
| Cybersecurity concepts | #Protect #Respond |
| Operational capabilities | #Continuity |
| Security domains | #Protection#Resilience |

**Control:**
The organization should plan how to maintain information security at an appropriate level during disruption.

**Purpose:**
To protect information and other associated assets during disruption.

**Guidance:**
The organization should determine its requirements for adapting information security controls during disruption. Information security requirements should be included in the business continuity management processes.
Plans should be developed, implemented, tested, reviewed and evaluated to maintain or restore the security of information of critical business processes following interruption or failure. Security of information should be restored at the required level and in the required time frames.
The organization should implement and maintain:
- information security controls, supporting systems and tools within business continuity and ICT continuity plans;
- processes to maintain existing information security controls during disruption;
- compensating controls for information security controls that cannot be maintained during disruption.

**Other information:**
In the context of business continuity and ICT continuity planning, it can be necessary to adapt the information security requirements depending on the type of disruption, compared to normal operational conditions. As part of the business impact analysis and risk assessment performed within business continuity management, the consequences of loss of confidentiality and integrity of information should be considered and prioritized in addition to the need for maintaining availability.
Information on business continuity management systems can be found in ISO 22301 and ISO 22313.
Further guidance on business impact analysis (BIA) can be found in ISO/TS 22317.