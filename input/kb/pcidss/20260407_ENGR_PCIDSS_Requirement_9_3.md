### A. Tài liệu gốc của Requirement 9

### B. Summary Overview của Control Objective 9.3
Tài liệu này mô tả chi tiết **Control Objective 9.3** của **Requirement 9 **trong **PCI-DSS v4.0.1**, tập trung vào việc quản lý và kiểm soát truy cập vật lý của nhân sự và khách vào CDE.
Mục tiêu chính là đảm bảo chỉ những cá nhân được ủy quyền mới được phép truy cập vật lý vào CDE và mọi hoạt động truy cập đều được kiểm soát, nhận diện và truy vết.
Gồm 4 sub-requirement chính:
- 9.3.1: Quản lý truy cập của nhân sự
- 9.3.2: Quản lý truy cập của visitor
- 9.3.3: Thu hồi badge visitor
- 9.3.4: Ghi log visitor
Áp dụng cho tất cả nhân sự và visitor có truy cập vật lý vào facility và CDE.

### C. Key Points của Control Objective 9.3
- Phạm vi áp dụng: Nhân sự và visitor truy cập vào CDE
- Trách nhiệm: Tài liệu hóa và kiểm soát quy trình cấp/thu hồi quyền truy cập vật lý
- Nhận diện: Nhân sự và visitor phải được nhận diện rõ ràng (badge, ID)
- Kiểm soát truy cập: Cấp quyền dựa trên job function và được ủy quyền
- Quản lý visitor: Visitor phải được approve, escort và có badge riêng
- Ghi nhận hoạt động: Phải ghi log visitor đầy đủ và lưu trữ ≥ 3 tháng

### D. Deep Summary của Control Objective 9.3
**Bối cảnh:**
Không kiểm soát truy cập vật lý của nhân sự và visitor có thể dẫn đến truy cập trái phép vào khu vực chứa dữ liệu thẻ.
**Nội dung cốt lõi:**
- Thiết lập quy trình cấp, thay đổi và thu hồi quyền truy cập vật lý cho nhân sự
- Nhận diện rõ ràng nhân sự trong khu vực CDE
- Thu hồi ngay quyền truy cập khi nhân sự nghỉ việc
- Kiểm soát visitor: phải được ủy quyền, escort và nhận diện rõ
- Thu hồi hoặc disable badge visitor sau khi rời khỏi facility
- Ghi log visitor đầy đủ (tên, thời gian, người phê duyệt…)
**Dữ liệu đáng chú ý:**
- Visitor log phải lưu ≥ 3 tháng
- Badge visitor phải phân biệt rõ với nhân sự
**Rủi ro / Lưu ý:**
- Không kiểm soát visitor → dễ truy cập trái phép
- Không thu hồi badge → bị reuse để truy cập lại
- Không log visitor → không truy vết được sự cố
- Không revoke access khi nghỉ việc → nhân sự cũ vẫn truy cập được

### E. Structured Output của Control Objective 9.3
**Control objectives:**9.3
**Sub-requirement:**9.3.1
**Defined Approach Requirements:**Procedures are implemented for authorizing and managing physical access of personnel to the CDE, including:
• Identifying personnel.
• Managing changes to an individual's physical access requirements.
• Revoking or terminating personnel identification.
• Limiting access to the identification process or system to authorized personnel.
**Defined Approach Testing Procedures:**
- "9.3.1.a": Examine documented procedures to verify that procedures to authorize and manage physical access of personnel to the CDE are defined in accordance with all elements specified in this requirement.
- "9.3.1.b": Observe identification methods, such as ID badges, and processes to verify that personnel in the CDE are clearly identified.
- "9.3.1.c": Observe processes to verify that access to the identification process, such as a badge system, is limited to authorized personnel.
**Customized Approach Objective:**Requirements for access to the physical CDE are defined and enforced to identify and authorize personnel.
**Guidance - Purpose:**Establishing procedures for granting, managing, and removing access when it is no longer needed ensures non-authorized individuals are prevented from gaining access to areas containing cardholder data. In addition, it is important to limit access to the actual badging system and badging materials to prevent unauthorized personnel from making their own badges and/or setting up their own access rules.
**Guidance - Good Practice:**It is important to visually identify the personnel that are physically present, and whether the individual is a visitor or an employee.
**Guidance - Definitions:**Refer to Appendix G for the definition of 'personnel.'
**Guidance - Examples:**One way to identify personnel is to assign them badges.

---
**Control objectives:**9.3
**Sub-requirement:**9.3.1.1
**Defined Approach Requirements:**Physical access to sensitive areas within the CDE for personnel is controlled as follows:
• Access is authorized and based on individual job function.
• Access is revoked immediately upon termination.
• All physical access mechanisms, such as keys, access cards, etc., are returned or disabled upon termination.
**Defined Approach Testing Procedures:**
- "9.3.1.1.a": Observe personnel in sensitive areas within the CDE, interview responsible personnel, and examine physical access control lists to verify that:
• Access to the sensitive area is authorized.
• Access is required for the individual's job function.
- "9.3.1.1.b": Observe processes and interview personnel to verify that access of all personnel is revoked immediately upon termination.
- "9.3.1.1.c": For terminated personnel, examine physical access controls lists and interview responsible personnel to verify that all physical access mechanisms (such as keys, access cards, etc.) were returned or disabled.
**Customized Approach Objective:**Sensitive areas cannot be accessed by unauthorized personnel.
**Guidance - Purpose:**Controlling physical access to sensitive areas helps ensure that only authorized personnel with a legitimate business need are granted access.
**Guidance - Good Practice:**Where possible, organizations should have policies and procedures to ensure that before personnel leaving the organization, all physical access mechanisms are returned, or disabled as soon as possible upon their departure. This will ensure personnel cannot gain physical access to sensitive areas once their employment has ended.

---
**Control objectives:**9.3
**Sub-requirement:**9.3.2
**Defined Approach Requirements:**Procedures are implemented for authorizing and managing visitor access to the CDE, including:
• Visitors are authorized before entering.
• Visitors are escorted at all times.
• Visitors are clearly identified and given a badge or other identification that expires.
• Visitor badges or other identification visibly distinguishes visitors from personnel.
**Defined Approach Testing Procedures:**
- "9.3.2.a": Examine documented procedures and interview personnel to verify procedures are defined for authorizing and managing visitor access to the CDE in accordance with all elements specified in this requirement.
- "9.3.2.b": Observe processes when visitors are present in the CDE and interview personnel to verify that visitors are:
• Authorized before entering the CDE.
• Escorted at all times within the CDE.
- "9.3.2.c": Observe the use of visitor badges or other identification to verify that the badge or other identification does not permit unescorted access to the CDE.
- "9.3.2.d": Observe visitors in the CDE to verify that:
• Visitor badges or other identification are being used for all visitors.
• Visitor badges or identification easily distinguish visitors from personnel.
- "9.3.2.e": Examine visitor badges or other identification and observe evidence in the badging system to verify visitor badges or other identification expires.
**Customized Approach Objective:**Requirements for visitor access to the CDE are defined and enforced. Visitors cannot exceed any authorized physical access allowed while in the CDE.
**Guidance - Purpose:**Visitor controls are important to reduce the ability of unauthorized and malicious persons to gain access to facilities and potentially to cardholder data. Visitor controls ensure visitors are identifiable as visitors so personnel can monitor their activities, and that their access is restricted to just the duration of their legitimate visit.
**Guidance - Definitions:**Refer to Appendix G for the definition of 'visitor.'

---
**Control objectives:**9.3
**Sub-requirement:**9.3.3
**Defined Approach Requirements:**Visitor badges or identification are surrendered or deactivated before visitors leave the facility or at the date of expiration.
**Defined Approach Testing Procedures:**Observe visitors leaving the facility and interview personnel to verify visitor badges or other identification are surrendered or deactivated before visitors leave the facility or at the date of expiration. upon departure or expiration.
**Customized Approach Objective:**Visitor identification or badges cannot be reused after expiration.
**Guidance - Purpose:**Ensuring that visitor badges are returned or deactivated upon expiry or completion of the visit prevents malicious persons from using a previously authorized pass to gain physical access into the building after the visit has ended.

---
**Control objectives:**9.3
**Sub-requirement:**9.3.4
**Defined Approach Requirements:**Visitor logs are used to maintain a physical record of visitor activity both within the facility and within sensitive areas, including:
• The visitor's name and the organization represented.
• The date and time of the visit.
• The name of the personnel authorizing physical access.
• Retaining the log for at least three months, unless otherwise restricted by law.
**Defined Approach Testing Procedures:**
- "9.3.4.a": Examine the visitor logs and interview responsible personnel to verify that visitor logs are used to record physical access to both the facility and sensitive areas.
- "9.3.4.b": Examine the visitor logs and verify that the logs contain:
• The visitor's name and the organization represented.
• The personnel authorizing physical access.
• Date and time of visit.
- "9.3.4.c": Examine visitor log storage locations and interview responsible personnel to verify that the log is retained for at least three months, unless otherwise restricted by law.
**Customized Approach Objective:** Records of visitor access that enable the identification of individuals are maintained.
**Guidance - Purpose:**A visitor log documenting minimum information about the visitor is easy and inexpensive to maintain. It will assist in identifying historical physical access to a building or room and potential access to cardholder data.
**Guidance - Good Practice:**When logging the date and time of visit, including both in and out times is considered a best practice, since it provides helpful tracking information and provides assurance that a visitor has left at the end of the day. It is also good to verify that a visitor's ID (driver's license, etc.) matches the name they put on the visitor log.