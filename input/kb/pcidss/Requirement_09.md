### A. Tài liệu gốc của Requirement 9

### B. Summary Overview của Control Objective 9.1
Tài liệu này mô tả chi tiết **Control Objective 9.1** của **Requirement 9** trong **PCI-DSS v4.0.1**, tập trung vào việc thiết lập và duy trì chính sách, quy trình và phân công trách nhiệm liên quan đến kiểm soát truy cập vật lý.
Mục tiêu chính là đảm bảo các chính sách, quy trình và vai trò trách nhiệm được tài liệu hóa, cập nhật, áp dụng thực tế và được hiểu rõ bởi các bên liên quan trong hoạt động kiểm soát truy cập vật lý.
Gồm 2 sub-requirement chính:
- 9.1.1: Quản lý chính sách và quy trình
- 9.1.2: Phân công vai trò và trách nhiệm
Áp dụng cho toàn bộ tổ chức và nhân sự tham gia vào các hoạt động kiểm soát truy cập vật lý theo Requirement 9.

### C. Key Points của Control Objective 9.1
- **Phạm vi áp dụng:** Tất cả chính sách, quy trình và nhân sự liên quan kiểm soát truy cập vật lý
- **Trách nhiệm:**Phân rõ vai trò, đảm bảo nhân sự hiểu và thực hiện đúng
- **Quản lý tài liệu:**Chính sách và quy trình phải được tài liệu hóa, cập nhật và phổ biến
- **Áp dụng thực tế:**Quy trình phải được triển khai và sử dụng thực tế
- **Truyền thông:**Đảm bảo các bên liên quan được phổ biến và hiểu nội dung

### D. Deep Summary của Control Objective 9.1
**Bối cảnh:**
Nếu chính sách và trách nhiệm không rõ ràng, các kiểm soát truy cập vật lý có thể không được thực hiện đầy đủ, dẫn đến nguy cơ truy cập trái phép vào khu vực chứa dữ liệu nhạy cảm.
**Nội dung cốt lõi:**
- Tài liệu hóa chính sách và quy trình kiểm soát truy cập vật lý
- Cập nhật khi có thay đổi về cơ sở hạ tầng hoặc quy trình vận hành
- Đảm bảo quy trình được áp dụng thực tế
- Phổ biến đến tất cả nhân sự liên quan
- Phân rõ vai trò và trách nhiệm cho từng hoạt động
**Dữ liệu đáng chú ý:**
- Chính sách và quy trình phải "in use" và "known to all affected parties"
- Có thể sử dụng RACI matrix để quản lý trách nhiệm
**Rủi ro / Lưu ý:**
- Chính sách không cập nhật → không phù hợp thực tế vận hành
- Quy trình không được thực thi → bỏ sót kiểm soát vật lý
- Nhân sự không rõ trách nhiệm → lỏng lẻo kiểm soát truy cập
- Thiếu phân công rõ ràng → không có accountability

### E. Structured Output của Control Objective 9.1
**Control objectives:**9.1
**Sub-requirement:**9.1.1
**Defined Approach Requirements:**All security policies and operational procedures that are identified in Requirement 9 are:
• Documented.
• Kept up to date.
• In use.
• Known to all affected parties.
**Defined Approach Testing Procedures:**Examine documentation and interview personnel to verify that security policies and operational procedures identified in Requirement 9 are managed in accordance with all elements specified in this requirement.
**Customized Approach Objective:**Expectations, controls, and oversight for meeting activities within Requirement 9 are defined and adhered to by affected personnel. All supporting activities are repeatable, consistently applied, and conform to management's intent.
**Guidance - Purpose:**Requirement 9.1.1 is about effectively managing and maintaining the various policies and procedures specified throughout Requirement 9. While it is important to define the specific policies or procedures called out in Requirement 9, it is equally important to ensure they are properly documented, maintained, and disseminated.
**Guidance - Good Practice:**It is important to update policies and procedures as needed to address changes in processes, technologies, and business objectives. For this reason, consider updating these documents as soon as possible after a change occurs and not only on a periodic cycle.
**Guidance - Definitions:**Security policies define the entity's security objectives and principles. Operational procedures describe how to perform activities, and define the controls, methods, and processes that are followed to achieve the desired result in a consistent manner and in accordance with policy objectives. Policies and procedures, including updates, are actively communicated to all affected personnel, and are supported by operating procedures describing how to perform activities.

---
**Control objectives:**9.1
**Sub-requirement:**9.1.2
**Defined Approach Requirements:**Roles and responsibilities for performing activities in Requirement 9 are documented, assigned, and understood. 9.2 Physical access controls manage entry into facilities and systems containing cardholder data.
**Defined Approach Testing Procedures:**
- "9.1.2.a": Examine documentation to verify that descriptions of roles and responsibilities for performing activities in Requirement 9 are documented and assigned.
- "9.1.2.b": Interview personnel with responsibility for performing activities in Requirement 9 to verify that roles and responsibilities are assigned as documented and are understood.
**Customized Approach Objective:** Day-to-day responsibilities for performing all the activities in Requirement 9 are allocated. Personnel are accountable for successful, continuous operation of these requirements.
**Guidance - Purpose:**If roles and responsibilities are not formally assigned, personnel may not be aware of their day-to-day responsibilities, and critical activities may not occur.
**Guidance - Good Practice:**Roles and responsibilities may be documented within policies and procedures or maintained within separate documents. As part of communicating roles and responsibilities, entities can consider having personnel acknowledge their acceptance and understanding of their assigned roles and responsibilities. A method to document roles and responsibilities is a responsibility assignment matrix that includes who is responsible, accountable, consulted, and informed (also called a RACI matrix).

================

### A. Tài liệu gốc của Requirement 9

### B. Summary Overview của Control Objective 9.2
Tài liệu này mô tả chi tiết **Control Objective 9.2** của **Requirement 9** trong **PCI-DSS v4.0.1**, tập trung vào việc triển khai các kiểm soát truy cập vật lý để hạn chế truy cập trái phép vào hệ thống và khu vực chứa dữ liệu thẻ.
Mục tiêu chính là đảm bảo chỉ những cá nhân được ủy quyền mới có thể truy cập vật lý vào CDE và các thành phần hệ thống liên quan.
Gồm 4 sub-requirement chính:
- 9.2.1: Kiểm soát truy cập vào facility/CDE
- 9.2.2: Kiểm soát network jack công cộng
- 9.2.3: Bảo vệ thiết bị mạng và hạ tầng
- 9.2.4: Khóa console tại khu vực nhạy cảm
Áp dụng cho tất cả khu vực vật lý, thiết bị và hạ tầng có liên quan đến CDE.

### C. Key Points của Control Objective 9.2
- Phạm vi áp dụng: Facility, CDE, thiết bị mạng và khu vực nhạy cảm
- Trách nhiệm: Triển khai và duy trì kiểm soát truy cập vật lý
- Kiểm soát truy cập: Chỉ cho phép personnel được ủy quyền vào CDE
- Giám sát: Theo dõi entry/exit tại khu vực nhạy cảm (camera/access control)
- Kiểm soát kết nối: Hạn chế sử dụng network jack tại khu vực công cộng
- Bảo vệ thiết bị: Giới hạn truy cập vật lý vào thiết bị mạng và telecom
- Kiểm soát console: Khóa console khi không sử dụng

### D. Deep Summary của Control Objective 9.2
**Bối cảnh:**
Truy cập vật lý trái phép có thể dẫn đến đánh cắp thiết bị, thay đổi cấu hình hoặc cài cắm thiết bị độc hại vào hệ thống.
**Nội dung cốt lõi:**
- Thiết lập cơ chế kiểm soát truy cập vào facility và khu vực CDE
- Giám sát entry/exit tại khu vực nhạy cảm và lưu trữ log
- Hạn chế truy cập vào network jack tại khu vực công cộng
- Bảo vệ thiết bị mạng, wireless và telecom khỏi truy cập trái phép
- Khóa console khi không sử dụng để ngăn truy cập trái phép
**Dữ liệu đáng chú ý:**
- Monitoring data phải được lưu ≥ 3 tháng
- Áp dụng cho tất cả entry/exit point tại khu vực nhạy cảm
**Rủi ro / Lưu ý:**
- Không kiểm soát vật lý → attacker có thể truy cập trực tiếp hệ thống
- Network jack công cộng → điểm vào dễ bị khai thác
- Thiết bị mạng không bảo vệ → bị gắn thiết bị nghe lén
- Console không khóa → bị truy cập trái phép ngay tại chỗ

### E. Structured Output của Control Objective 9.2
**Control objectives:**9.2
**Sub-requirement:**9.2.1
**Defined Approach Requirements:**Appropriate facility entry controls are in place to restrict physical access to systems in the CDE.
**Defined Approach Testing Procedures:**Observe entry controls and interview responsible personnel to verify that physical security controls are in place to restrict access to systems in the CDE.
**Customized Approach Objective:**System components in the CDE cannot be physically accessed by unauthorized personnel.
**Applicability Notes:**This requirement does not apply to locations that are publicly accessible by consumers (cardholders).
**Guidance - Purpose:**Without physical access controls, unauthorized persons could potentially gain access to the CDE and sensitive information, or could alter system configurations, introduce vulnerabilities into the network, or destroy or steal equipment. Therefore, the purpose of this requirement is that physical access to the CDE is controlled via physical security controls such as badge readers or other mechanisms such as lock and key.
**Guidance - Good Practice:**Whichever mechanism meets this requirement, it must be sufficient for the organization to verify that only authorized personnel are granted access.
**Guidance - Examples:**Facility entry controls include physical security controls at each computer room, data center, and other physical areas with systems in the CDE. It can also include badge readers or other devices that manage physical access controls, such as lock and key with a current list of all individuals holding the keys.

---
**Control objectives:**9.2
**Sub-requirement:**9.2.1.1
**Defined Approach Requirements:**Individual physical access to sensitive areas within the CDE is monitored with either video cameras or physical access control mechanisms (or both) as follows:
• Entry and exit points to/from sensitive areas within the CDE are monitored.
• Monitoring devices or mechanisms are protected from tampering or disabling.
• Collected data is reviewed and correlated with other entries.
• Collected data is stored for at least three months, unless otherwise restricted by law.
**Defined Approach Testing Procedures:**
- "9.2.1.1.a": Observe locations where individual physical access to sensitive areas within the CDE occurs to verify that either video cameras or physical access control mechanisms (or both) are in place to monitor the entry and exit points.
- "9.2.1.1.b": Observe locations where individual physical access to sensitive areas within the CDE occurs to verify that either video cameras or physical access control mechanisms (or both) are protected from tampering or disabling.
- "9.2.1.1.c": Observe the physical access control mechanisms and/or examine video cameras and interview responsible personnel to verify that:
• Collected data from video cameras and/or physical access control mechanisms is reviewed and correlated with other entries.
• Collected data is stored for at least three months.
**Customized Approach Objective:**Trusted, verifiable records are maintained of individual physical entry to, and exit from, sensitive areas.
**Guidance - Purpose:**Maintaining details of individuals entering and exiting the sensitive areas can help with investigations of physical breaches by identifying individuals that physically accessed the sensitive areas, as well as when they entered and exited.
**Guidance - Good Practice:**Whichever mechanism meets this requirement, it should effectively monitor all entry and exit points to sensitive areas. Criminals attempting to gain physical access to sensitive areas will often try to disable or bypass the monitoring controls. To protect these controls from tampering, video cameras could be positioned so they are out of reach and/or be monitored to detect tampering. Similarly, physical access control mechanisms could be monitored or have physical protections installed to prevent them from being damaged or disabled by malicious individuals

---
**Control objectives:**9.2
**Sub-requirement:**9.2.2
**Defined Approach Requirements:**Physical and/or logical controls are implemented to restrict use of publicly accessible network jacks within the facility.
**Defined Approach Testing Procedures:**Interview responsible personnel and observe locations of publicly accessible network jacks to verify that physical and/or logical controls are in place to restrict access to publicly accessible network jacks within the facility.
**Customized Approach Objective:**Unauthorized devices cannot connect to the entity's network from public areas within the facility.
**Guidance - Purpose:**Restricting access to network jacks (or network ports) will prevent malicious individuals from plugging into readily available network jacks and gaining access to the CDE or systems connected to the CDE.
**Guidance - Good Practice:**Whether logical or physical controls, or a combination of both, are used, they should prevent an individual or device that is not explicitly authorized from being able to connect to the network.
**Guidance - Examples:**Methods to meet this requirement include network jacks located in public areas and areas accessible to visitors could be disabled and only enabled when network access is explicitly authorized. Alternatively, processes could be implemented to ensure that visitors are escorted at all times in areas with active network jacks.

---
**Control objectives:**9.2
**Sub-requirement:**9.2.3
**Defined Approach Requirements:**Physical access to wireless access points, gateways, networking/communications hardware, and telecommunication lines within the facility is restricted
**Defined Approach Testing Procedures:**Interview responsible personnel and observe locations of hardware and lines to verify that physical access to wireless access points, gateways, networking/communications hardware, and telecommunication lines within the facility is restricted.
**Customized Approach Objective:** Physical networking equipment cannot be accessed by unauthorized personnel.
**Guidance - Purpose:**Without appropriate physical security over access to wireless components and devices, and computer networking and telecommunications equipment and lines, malicious users could gain access to the entity's network resources. Additionally, they could connect their own devices to the network to gain unauthorized access to the CDE or systems connected to the CDE. Additionally, securing networking and communications hardware prevents malicious users from intercepting network traffic or physically connecting their own devices to wired network resources.

---
**Control objectives:**9.2
**Sub-requirement:**9.2.4
**Defined Approach Requirements:**Access to consoles in sensitive areas is restricted via locking when not in use.
**Defined Approach Testing Procedures:**Observe a system administrator's attempt to log into consoles in sensitive areas and verify that they are 'locked' to prevent unauthorized use. 9.3 Physical access for personnel and visitors is authorized and managed.
**Customized Approach Objective:**Physical consoles within sensitive areas cannot be used by unauthorized personnel.
**Guidance - Purpose:**Locking console login screens prevents unauthorized persons from gaining access to sensitive information, altering system configurations, introducing vulnerabilities into the network, or destroying records.

================

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

================

### A. Tài liệu gốc của Requirement 9

### B. Summary Overview của Control Objective 9.4
Tài liệu này mô tả chi tiết **Control Objective 9.4** của** Requirement 9** trong **PCI-DSS v4.0.1**, tập trung vào việc bảo vệ, quản lý và xử lý media chứa dữ liệu thẻ.
Mục tiêu chính là đảm bảo media chứa cardholder data được bảo vệ khỏi truy cập trái phép trong suốt vòng đời, bao gồm lưu trữ, vận chuyển và tiêu hủy.
Gồm 6 sub-requirement chính:
- 9.4.1: Bảo vệ media chứa CHD
- 9.4.2: Phân loại media
- 9.4.3: Kiểm soát vận chuyển media
- 9.4.4: Phê duyệt di chuyển media
- 9.4.5: Quản lý inventory media
- 9.4.6: Tiêu hủy hard-copy media
- 9.4.7: Tiêu hủy electronic media
Áp dụng cho tất cả media chứa cardholder data, bao gồm electronic và hard-copy.

### C. Key Points của Control Objective 9.4
- **Phạm vi áp dụng:**Tất cả media chứa cardholder data (electronic và hard-copy)
- **Trách nhiệm:**Tài liệu hóa và kiểm soát toàn bộ vòng đời media
- **Bảo vệ dữ liệu:**Media phải được bảo vệ vật lý khỏi truy cập trái phép
- **Quản lý vận chuyển:**Media gửi ra ngoài phải được log, track và bảo vệ
- **Kiểm soát inventory:**Duy trì danh sách và kiểm kê định kỳ
- **Tiêu hủy:**Media phải được tiêu hủy an toàn, không thể khôi phục

### D. Deep Summary của Control Objective 9.4
**Bối cảnh:**
Media chứa dữ liệu thẻ nếu không được bảo vệ có thể bị mất, đánh cắp hoặc truy cập trái phép, dẫn đến rò rỉ dữ liệu nghiêm trọng.
**Nội dung cốt lõi:**
- Bảo vệ vật lý tất cả media chứa CHD
- Phân loại media theo mức độ nhạy cảm
- Kiểm soát vận chuyển: log, tracking và secure courier
- Yêu cầu phê duyệt khi di chuyển media ra ngoài facility
- Duy trì inventory và kiểm kê định kỳ
- Tiêu hủy hard-copy (shred/incinerate) và electronic media (wipe/destroy)
**Dữ liệu đáng chú ý:**
- Inventory media phải được kiểm kê ít nhất 12 tháng/lần
- Visitor/media log và tracking phải lưu ≥ 3 tháng
**Rủi ro / Lưu ý:**
- Media không bảo vệ → dễ bị mất hoặc đánh cắp
- Không tracking khi vận chuyển → mất kiểm soát vị trí
- Không inventory → không phát hiện mất mát
- Tiêu hủy không đúng → dữ liệu có thể bị khôi phục
- Hardcopy bị bỏ đi → rủi ro "dumpster diving"

### E. Structured Output của Control Objective 9.4
**Control objectives:**9.4
**Sub-requirement:**9.4.1
**Defined Approach Requirements:**All media with cardholder data is physically secured.
**Defined Approach Testing Procedures:**. Examine documentation to verify that the procedures defined for protecting cardholder data include controls for physically securing all media.
**Customized Approach Objective:**Media with cardholder data cannot be accessed by unauthorized personnel.
**Guidance - Purpose:**Controls for physically securing media are intended to prevent unauthorized persons from gaining access to cardholder data on any media. Cardholder data is susceptible to unauthorized viewing, copying, or scanning if it is unprotected while it is on removable or portable media, printed out, or left on someone's desk.

---
**Control objectives:**9.4
**Sub-requirement:**9.4.1.1
**Defined Approach Requirements:**Offline media backups with cardholder data are stored in a secure location.
**Defined Approach Testing Procedures:**
- "9.4.1.1.a": Examine documentation to verify that procedures are defined for physically securing offline media backups with cardholder data in a secure location.
- "9.4.1.1.b": Examine logs or other documentation and interview responsible personnel at the storage location to verify that offline media backups are stored in a secure location.
**Customized Approach Objective:**Offline backups cannot be accessed by unauthorized personnel.
**Guidance - Purpose:**If stored in a non-secured facility, backups containing cardholder data may easily be lost, stolen, or copied for malicious intent.
**Guidance - Good Practice:**For secure storage of backup media, a good practice is to store media in an off-site facility, such as an alternate or backup site or commercial storage facility.

---
**Control objectives:**9.4
**Sub-requirement:**9.4.1.2
**Defined Approach Requirements:**The security of the offline media backup location(s) with cardholder data is reviewed at least once every 12 months.
**Defined Approach Testing Procedures:**
- "9.4.1.2.a": Examine documentation to verify that procedures are defined for reviewing the security of the offline media backup location(s) with cardholder data at least once every 12 months.
- "9.4.1.2.b": Examine documented procedures, logs, or other documentation, and interview responsible personnel at the storage location(s) to verify that the storage location's security is reviewed at least once every 12 months.
**Customized Approach Objective:**The security controls protecting offline backups are verified periodically by inspection.
**Guidance - Purpose:**Conducting regular reviews of the storage facility enables the organization to address identified security issues promptly, minimizing the potential risk. It is important for the entity to be aware of the security of the area where media is being stored.

---
**Control objectives:**9.4
**Sub-requirement:**9.4.2
**Defined Approach Requirements:**All media with cardholder data is classified in accordance with the sensitivity of the data.
**Defined Approach Testing Procedures:**
- "9.4.2.a": Examine documentation to verify that procedures are defined for classifying media with cardholder data in accordance with the sensitivity of the data.
- "9.4.2.b": Examine media logs or other documentation to verify that all media is classified in accordance with the sensitivity of the data.
**Customized Approach Objective:**Media are classified and protected appropriately.
**Guidance - Purpose:**Media not identified as confidential may not be adequately protected or may be lost or stolen.
**Guidance - Good Practice:**It is important that media be identified such that its classification status is apparent. This does not mean however that the media needs to have a 'confidential' label.

---
**Control objectives:**9.4
**Sub-requirement:**9.4.3
**Defined Approach Requirements:**Media with cardholder data sent outside the facility is secured as follows:
• Media sent outside the facility is logged.
• Media is sent by secured courier or other delivery method that can be accurately tracked.
• Offsite tracking logs include details about media location.
**Defined Approach Testing Procedures:**
- "9.4.3.a": Examine documentation to verify that procedures are defined for securing media sent outside the facility in accordance with all elements specified in this requirement.
- "9.4.3.b": Interview personnel and examine records to verify that all media sent outside the facility is logged and sent via secured courier or other delivery method that can be tracked.
- "9.4.3.c": Examine offsite tracking logs for all media to verify tracking details are documented.
**Customized Approach Objective:**Media is secured and tracked when transported outside the facility.
**Guidance - Purpose:**Media may be lost or stolen if sent via a non- trackable method such as regular postal mail. The use of secure couriers to deliver any media that contains cardholder data allows organizations to use their tracking systems to maintain inventory and location of shipments.

---
**Control objectives:**9.4
**Sub-requirement:**9.4.4
**Defined Approach Requirements:**Management approves all media with cardholder data that is moved outside the facility (including when media is distributed to individuals).
**Defined Approach Testing Procedures:**
- "9.4.4.a": Examine documentation to verify that procedures are defined to ensure that media moved outside the facility is approved by management.
- "9.4.4.b": Examine offsite media tracking logs and interview responsible personnel to verify that proper management authorization is obtained for all media moved outside the facility (including media distributed to individuals).
**Customized Approach Objective:**Media cannot leave a facility without the approval of accountable personnel.
**Applicability Notes:**Individuals approving media movements should have the appropriate level of management authority to grant this approval. However, it is not specifically required that such individuals have 'manager' as part of their title.
**Guidance - Purpose:**Without a firm process for ensuring that all media movements are approved before the media is removed from secure areas, the media would not be tracked or appropriately protected, and its location would be unknown, leading to lost or stolen media.

---
**Control objectives:**9.4
**Sub-requirement:**9.4.5
**Defined Approach Requirements:**Inventory logs of all electronic media with cardholder data are maintained.
**Defined Approach Testing Procedures:**
- "9.4.5.a": Examine documentation to verify that procedures are defined to maintain electronic media inventory logs.
- "9.4.5.b": Examine electronic media inventory logs and interview responsible personnel to verify that logs are maintained.
**Customized Approach Objective:**Accurate inventories of stored electronic media are maintained.
**Guidance - Purpose:**Without careful inventory methods and storage controls, stolen or missing electronic media could go unnoticed for an indefinite amount of time.

---
**Control objectives:**9.4
**Sub-requirement:**9.4.5.1
**Defined Approach Requirements:**Inventories of electronic media with cardholder data are conducted at least once every 12 months.
**Defined Approach Testing Procedures:**
- "9.4.5.1.a": Examine documentation to verify that procedures are defined to conduct inventories of electronic media with cardholder data at least once every 12 months.
- "9.4.5.1.b": Examine electronic media inventory logs and interview personnel to verify that electronic media inventories are performed at least once every 12 months.
**Customized Approach Objective:**Media inventories are verified periodically.
**Guidance - Purpose:**Without careful inventory methods and storage controls, stolen or missing electronic media could go unnoticed for an indefinite amount of time.

---
**Control objectives:**9.4
**Sub-requirement:**9.4.6
**Defined Approach Requirements:**Hard-copy materials with cardholder data are destroyed when no longer needed for business or legal reasons, as follows:
• Materials are cross-cut shredded, incinerated, or pulped so that cardholder data cannot be reconstructed.
• Materials are stored in secure storage containers prior to destruction.
**Defined Approach Testing Procedures:**
- "9.4.6.a": Examine the media destruction policy to verify that procedures are defined to destroy hard- copy media with cardholder data when no longer needed for business or legal reasons in accordance with all elements specified in this requirement.
- "9.4.6.b": Observe processes and interview personnel to verify that hard-copy materials are cross-cut shredded, incinerated, or pulped such that cardholder data cannot be reconstructed.
- "9.4.6.c": Observe storage containers used for materials that contain information to be destroyed to verify that the containers are secure.
**Customized Approach Objective:**Cardholder data cannot be recovered from media that has been destroyed or which is pending destruction.
**Applicability Notes:**These requirements for media destruction when that media is no longer needed for business or legal reasons are separate and distinct from PCI DSS Requirement 3.2.1, which is for securely deleting cardholder data when no longer needed per the entity's cardholder data retention policies.
**Guidance - Purpose:**If steps are not taken to destroy information contained on hard-copy media before disposal, malicious individuals may retrieve information from the disposed media, leading to a data compromise. For example, malicious individuals may use a technique known as 'dumpster diving,' where they search through trashcans and recycle bins looking for hard-copy materials with information they can use to launch an attack. Securing storage containers used for materials that are going to be destroyed prevents sensitive information from being captured while the materials are being collected.
**Guidance - Good Practice:**Consider 'to-be-shredded' containers with a lock that prevents access to its contents or that physically prevent access to the inside of the container.
**Guidance - Further Information:**See NIST Special Publication 800-88, Revision 1: Guidelines for Media Sanitization.

---
**Control objectives:**9.4
**Sub-requirement:**9.4.7
**Defined Approach Requirements:**Electronic media with cardholder data is destroyed when no longer needed for business or legal reasons via one of the following:
• The electronic media is destroyed.
• The cardholder data is rendered unrecoverable so that it cannot be reconstructed. Customized Approach Objective Cardholder data cannot be recovered from media that has been erased or destroyed. 9.5 Point-of-interaction (POI) devices are protected from tampering and unauthorized substitution.
**Defined Approach Testing Procedures:**
- "9.4.7.a": Examine the media destruction policy to verify that procedures are defined to destroy electronic media when no longer needed for business or legal reasons in accordance with all elements specified in this requirement.
- "9.4.7.b": Observe the media destruction process and interview responsible personnel to verify that electronic media with cardholder data is destroyed via one of the methods specified in this requirement.
**Customized Approach Objective:**Cardholder data cannot be recovered from media that has been erased or destroyed.
**Applicability Notes:**These requirements for media destruction when that media is no longer needed for business or legal reasons are separate and distinct from PCI DSS Requirement 3.2.1, which is for securely deleting cardholder data when no longer needed per the entity's cardholder data retention policies.
**Guidance - Purpose:**If steps are not taken to destroy information contained on electronic media when no longer needed, malicious individuals may retrieve information from the disposed media, leading to a data compromise. For example, malicious individuals may use a technique known as 'dumpster diving,' where they search through trashcans and recycle bins looking for information they can use to launch an attack.
**Guidance - Good Practice:**The deletion function in most operating systems allows deleted data to be recovered, so instead, a dedicated secure deletion function or application should be used to make data unrecoverable.
**Guidance - Examples:**Methods for securely destroying electronic media include secure wiping in accordance with industry-accepted standards for secure deletion, degaussing, or physical destruction (such as grinding or shredding hard disks).
**Guidance - Further Information:**See NIST Special Publication 800-88, Revision 1: Guidelines for Media Sanitization.

================

### A. Tài liệu gốc của Requirement 9

### B. Summary Overview của Control Objective 9.5
Tài liệu này mô tả chi tiết **Control Objective 9.5 **của **Requirement 9** trong **PCI-DSS v4.0.1**, tập trung vào việc bảo vệ thiết bị POI (Point-of-Interaction) khỏi bị can thiệp hoặc thay thế trái phép.
Mục tiêu chính là đảm bảo các thiết bị POI được quản lý, giám sát và kiểm tra nhằm phát hiện kịp thời các hành vi tampering hoặc skimming.
Gồm 1 sub-requirement chính:
- 9.5.1: Bảo vệ và quản lý POI device
Áp dụng cho tất cả POI devices sử dụng trong giao dịch thẻ trực tiếp (card-present).

### C. Key Points của Control Objective 9.5
- **Phạm vi áp dụng:** Tất cả POI devices trong môi trường
- **Trách nhiệm:**Tài liệu hóa, quản lý và kiểm soát thiết bị POI
- **Quản lý thiết bị:**Duy trì danh sách thiết bị (model, location, serial)
- **Kiểm tra định kỳ:** Kiểm tra thiết bị để phát hiện tampering hoặc thay thế
- **Đào tạo nhân sự:** Nhận biết hành vi đáng ngờ và báo cáo kịp thời
- **Kiểm soát truy cập:**Xác minh bên thứ ba trước khi thao tác thiết bị

### D. Deep Summary của Control Objective 9.5
**Bối cảnh:**
POI devices là mục tiêu phổ biến của các cuộc tấn công skimming nhằm đánh cắp dữ liệu thẻ thông qua việc gắn thiết bị hoặc thay thế thiết bị hợp lệ.
**Nội dung cốt lõi:**
- Duy trì danh sách đầy đủ và cập nhật các POI device
- Kiểm tra định kỳ thiết bị để phát hiện dấu hiệu tampering hoặc substitution
- Xác định tần suất kiểm tra dựa trên risk analysis
- Đào tạo nhân sự nhận biết dấu hiệu bất thường và quy trình xử lý
- Xác minh danh tính bên thứ ba trước khi cho phép truy cập hoặc sửa chữa thiết bị
**Dữ liệu đáng chú ý:**
- Danh sách thiết bị phải bao gồm model, location và serial
- Tần suất kiểm tra dựa trên targeted risk analysis
**Rủi ro / Lưu ý:**
- Không kiểm tra thiết bị → không phát hiện skimming
- Không quản lý inventory → không biết thiết bị bị thay thế
- Nhân sự không được đào tạo → dễ bị lừa bởi attacker giả danh
- Không verify vendor → cho phép truy cập trái phép vào thiết bị

### E. Structured Output của Control Objective 9.5
**Control objectives:**9.5
**Sub-requirement:**9.5.1
**Defined Approach Requirements:**POI devices that capture payment card data via direct physical interaction with the payment card form factor are protected from tampering and unauthorized substitution, including the following:
• Maintaining a list of POI devices.
• Periodically inspecting POI devices to look for tampering or unauthorized substitution.
• Training personnel to be aware of suspicious behavior and to report tampering or unauthorized substitution of devices.
**Defined Approach Testing Procedures:**Examine documented policies and procedures to verify that processes are defined that include all elements specified in this requirement.
**Customized Approach Objective:**The entity has defined procedures to protect and manage point-of-interaction devices. Expectations, controls, and oversight for the management and protection of POI devices are defined and adhered to by affected personnel.
**Applicability Notes:**These requirements apply to deployed POI devices used in card-present transactions (that is, a payment card form factor such as a card that is swiped, tapped, or dipped). These requirements do not apply to:
• Components used only for manual PAN key entry.
• Commercial off-the-shelf (COTS) devices (for example, smartphones or tablets), which are mobile merchant-owned devices designed for mass-market distribution.
**Guidance - Purpose:**Criminals attempt to steal payment card data by stealing and/or manipulating card-reading devices and terminals. Criminals will try to steal devices so they can learn how to break into them, and they often try to replace legitimate devices with fraudulent devices that send them payment card data every time a card is entered. They will also try to add 'skimming' components to the outside of devices, which are designed to capture payment card data before it enters the device-for example, by attaching an additional card reader on top of the legitimate card reader so that the payment card data is captured twice: once by the criminal's component and then by the device's legitimate component. In this way, transactions may still be completed without interruption while the criminal is 'skimming' the payment card data during the process.
**Guidance - Good Practice:** Entities may consider implementing protection from tampering and unauthorized substitution for:
• Components used only for manual PAN key entry.
• Commercial off-the-shelf (COTS) devices (for example, smartphones or tablets), which are mobile merchant-owned devices designed for mass-market distribution.
**Guidance - Further Information:**Additional best practices on skimming prevention are available on the PCI SSC website.

---
**Control objectives:**9.5
**Sub-requirement:**9.5.1.1
**Defined Approach Requirements:**An up-to-date list of POI devices is maintained, including:
• Make and model of the device.
• Location of device.
• Device serial number or other methods of unique identification.
**Defined Approach Testing Procedures:**
- "9.5.1.1.a": Examine the list of POI devices to verify it includes all elements specified in this requirement.
- "9.5.1.1.b": Observe POI devices and device locations and compare to devices in the list to verify that the list is accurate and up to date.
- "9.5.1.1.c": Interview personnel to verify the list of POI devices is updated when devices are added, relocated, decommissioned, etc.
**Customized Approach Objective:**The identity and location of POI devices is recorded and known at all times.
**Guidance - Purpose:**Keeping an up-to-date list of POI devices helps an organization track where devices are supposed to be and quickly identify if a device is missing or lost.
**Guidance - Good Practice:**The method for maintaining a list of devices may be automated (for example, a device- management system) or manual (for example, documented in electronic or paper records). For on-the-road devices, the location may include the name of the personnel to whom the device is assigned.
**Guidance - Examples:**Methods to maintain device locations include identifying the address of the site or facility where the device is located.

---
**Control objectives:**9.5
**Sub-requirement:**9.5.1.2
**Defined Approach Requirements:**POI device surfaces are periodically inspected to detect tampering and unauthorized substitution.
**Defined Approach Testing Procedures:**
- "9.5.1.2.a": Examine documented procedures to verify processes are defined for periodic inspections of POI device surfaces to detect tampering and unauthorized substitution.
- "9.5.1.2.b": Interview responsible personnel and observe inspection processes to verify:
• Personnel are aware of procedures for inspecting devices.
• All devices are periodically inspected for evidence of tampering and unauthorized substitution.
**Customized Approach Objective:**Point of interaction devices cannot be tampered with, substituted without authorization, or have skimming attachments installed without timely detection.
**Guidance - Purpose:**Regular inspections of devices will help organizations detect tampering more quickly via external evidence-for example, the addition of a card skimmer-or replacement of a device, thereby minimizing the potential impact of using fraudulent devices.
**Guidance - Good Practice:**Methods for periodic inspection include checking the serial number or other device characteristics and comparing the information to the list of POI devices to verify the device has not been swapped with a fraudulent device.
**Guidance - Examples:**The type of inspection will depend on the device. For instance, photographs of devices known to be secure can be used to compare a device's current appearance with its original appearance to see whether it has changed. Another option may be to use a secure marker pen, such as a UV light marker, to mark device surfaces and device openings so any tampering or replacement will be apparent. Criminals will often replace the outer casing of a device to hide their tampering, and these methods may help to detect such activities. Device vendors may also provide security guidance and 'how to' guides to help determine whether the device has been subject to tampering. Signs that a device might have been tampered with or substituted include:
• Unexpected attachments or cables plugged into the device.
• Missing or changed security labels.
• Broken or differently colored casing.
• Changes to the serial number or other external markings.

---
**Control objectives:**9.5
**Sub-requirement:**9.5.1.2.1
**Defined Approach Requirements:**The frequency of periodic POI device inspections and the type of inspections performed is defined in the entity's targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1.
**Defined Approach Testing Procedures:**
- "9.5.1.2.1.a": Examine the entity's targeted risk analysis for the frequency of periodic POI device inspections and type of inspections performed to verify the risk analysis was performed in accordance with all elements specified in Requirement 12.3.1.
- "9.5.1.2.1.b": Examine documented results of periodic device inspections and interview personnel to verify that the frequency and type of POI device inspections performed match what is defined in the entity's targeted risk analysis conducted for this requirement.
**Customized Approach Objective:**POI devices are inspected at a frequency that addresses the entity's risk.
**Applicability Notes:**This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Entities are best placed to determine the frequency of POI device inspections based on the environment in which the device operates.
**Guidance - Good Practice:**The frequency of inspections will depend on factors such as the location of a device and whether the device is attended or unattended. For example, devices left in public areas without supervision by the organization's personnel might have more frequent inspections than devices kept in secure areas or supervised when accessible to the public. In addition, many POI vendors include guidance in their user documentation about how often POI devices should be checked, and for what - entities should consult their vendors' documentation and incorporate those recommendations into their periodic inspections.

---
**Control objectives:**9.5
**Sub-requirement:**9.5.1.3
**Defined Approach Requirements:**Training is provided for personnel in POI environments to be aware of attempted tampering or replacement of POI devices, and includes:
• Verifying the identity of any third-party persons claiming to be repair or maintenance personnel, before granting them access to modify or troubleshoot devices.
• Procedures to ensure devices are not installed, replaced, or returned without verification.
• Being aware of suspicious behavior around devices.
• Reporting suspicious behavior and indications of device tampering or substitution to appropriate personnel.
**Defined Approach Testing Procedures:**
- "9.5.1.3.a": Review training materials for personnel in POI environments to verify they include all elements specified in this requirement.
- "9.5.1.3.b": Interview personnel in POI environments to verify they have received training and know the procedures for all elements specified in this requirement .
**Customized Approach Objective:**Personnel are knowledgeable about the types of attacks against POI devices, the entity's technical and procedural countermeasures, and can access assistance and guidance when required.
**Guidance - Purpose:**Criminals will often pose as authorized maintenance personnel to gain access to POI devices.
**Guidance - Good Practice:**Personnel training should include being alert to and questioning anyone who shows up to do POI maintenance to ensure they are authorized and have a valid work order, including any agents, maintenance or repair personnel, technicians, service providers, or other third parties. All third parties requesting access to devices should always be verified before being provided access-for example, by checking with management or phoning the POI maintenance company, such as the vendor or acquirer, for verification. Many criminals will try to fool personnel by dressing for the part (for example, carrying toolboxes and dressed in work apparel), and could also be knowledgeable about locations of devices, so personnel should be trained to always follow procedures. Another trick that criminals use is to send a 'new' POI device with instructions for swapping it with a legitimate device and 'returning' the legitimate device. The criminals may even provide return postage to their specified address. Therefore, personnel should always verify with their manager or supplier that the device is legitimate and came from a trusted source before installing it or using it for business.
**Guidance - Examples:**Suspicious behavior that personnel should be aware of includes attempts by unknown persons to unplug or open devices. Ensuring personnel are aware of mechanisms for reporting suspicious behavior and who to report such behavior to-for example, a manager or security officer-will help reduce the likelihood and potential impact of a device being tampered with or substituted.