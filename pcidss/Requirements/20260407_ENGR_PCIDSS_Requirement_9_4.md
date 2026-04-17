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