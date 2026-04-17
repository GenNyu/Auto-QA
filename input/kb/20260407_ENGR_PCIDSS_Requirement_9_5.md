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