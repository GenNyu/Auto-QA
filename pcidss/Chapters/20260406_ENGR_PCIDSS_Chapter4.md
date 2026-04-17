### A. Tài liệu gốc của Chapter 4

### B. Summary Overview của Chapter 4
Tài liệu này mô tả chi tiết **Chapter 4** trong **PCI-DSS v4.0.1**, tập trung vào việc xác định **Phạm vi (Scope) của các yêu cầu PCI DSS**.
Mục tiêu chính là hướng dẫn các thực thể xác định chính xác các thành phần hệ thống, con người và quy trình thuộc phạm vi đánh giá, từ đó đảm bảo dữ liệu tài khoản được bảo vệ tối ưu và giảm thiểu rủi ro cho toàn bộ hệ sinh thái thanh toán.

### C. Key Points của Chapter 4
- **Xác nhận phạm vi hàng năm:** Các thực thể phải thực hiện xác nhận tính chính xác của phạm vi PCI DSS ít nhất một lần mỗi năm theo Yêu cầu 12.5.2.
- **Thành phần hệ thống:** Bao gồm mọi thiết bị mạng, máy chủ, thành phần ảo hóa, thành phần đám mây, phần mềm và thiết bị đầu cuối lưu trữ, xử lý hoặc truyền dẫn dữ liệu tài khoản.
- **Phân đoạn mạng (Segmentation):** Mặc dù không bắt buộc, phân đoạn được khuyến khích mạnh mẽ để giảm phạm vi đánh giá, giảm chi phí và hạn chế rủi ro.
- **Quản lý bên thứ ba (TPSP):** Việc sử dụng một TPSP đạt chuẩn không giúp khách hàng mặc nhiên đạt tuân thủ; trách nhiệm giám sát và xác nhận tuân thủ vẫn thuộc về thực thể.
- **Kênh dữ liệu ngoài ý muốn:** Nếu nhận được dữ liệu thẻ qua các kênh không mong muốn, thực thể phải chọn giữa việc đưa kênh đó vào phạm vi quản lý hoặc xóa dữ liệu an toàn.

### D. Deep Summary của Chapter 4
**Bối cảnh:**
Xác định phạm vi là bước chuẩn bị tiên quyết và quan trọng nhất cho bất kỳ cuộc đánh giá PCI DSS nào. Một phạm vi không chính xác sẽ dẫn đến việc bỏ sót các lỗ hổng bảo mật nghiêm trọng.

**Nội dung cốt lõi:**
- **Môi trường dữ liệu chủ thẻ (CDE):** Bao gồm các thành phần trực tiếp tham gia vào luồng dữ liệu thẻ và cả các hệ thống không tham gia trực tiếp nhưng có kết nối không hạn chế với CDE.
- **Hệ thống có ảnh hưởng bảo mật:** Các hệ thống cung cấp dịch vụ an ninh (như máy chủ xác thực, SIEM) hoặc hệ thống phân đoạn mạng cũng nằm trong phạm vi vì chúng bảo vệ hoặc ảnh hưởng đến an ninh của CDE.
- **Logic phân đoạn:** Nếu không phân đoạn hiệu quả (mạng phẳng), toàn bộ mạng của tổ chức sẽ bị coi là nằm trong phạm vi đánh giá. Hiệu quả của việc phân đoạn phải được kiểm toán viên xác nhận thông qua kiểm tra thực tế.

**Dữ liệu đáng chú ý:**
- **Sơ đồ luồng dữ liệu:** Việc lập sơ đồ này là bắt buộc để hiểu cách dữ liệu thẻ đi vào, lưu trú và di chuyển trong tổ chức.
- **Dò tìm Wireless lạ (Rogue detection):** Phải được thực hiện định kỳ ngay cả khi thực thể có chính sách cấm sử dụng công nghệ không dây trong môi trường của mình.
- **Ma trận trách nhiệm:** Khi sử dụng TPSP, các bên cần làm rõ trách nhiệm đối với từng yêu cầu bảo mật cụ thể (Shared Responsibility).

**Rủi ro / Lưu ý:**
- **Lầm tưởng về mã hóa:** Việc mã hóa dữ liệu thẻ không làm cho hệ thống đó thoát khỏi phạm vi PCI DSS nếu khóa giải mã vẫn hiện diện trong cùng môi trường hoặc thuộc quyền quản lý của thực thể.
- **Quy trình BAU:** Việc xác nhận phạm vi nên được tích hợp vào các hoạt động kinh doanh hàng ngày (BAU) để đảm bảo tính tuân thủ liên tục giữa các kỳ đánh giá.
- **Lưu trữ vật lý:** Các bản in giấy, tệp ghi âm cuộc gọi chứa dữ liệu thẻ cũng là đối tượng phải quản lý nghiêm ngặt trong phạm vi PCI DSS.

### E. Structured Output của Chapter 4
PCI DSS requirements apply to:
- The cardholder data environment (CDE), which is comprised of:
    - System components, people, and processes that store, process, or transmit cardholder data and/or sensitive authentication data, and,
    - System components that may not store, process, or transmit CHD/SAD but have unrestricted connectivity to system components that store, process, or transmit CHD/SAD.
AND
- System components, people, and processes that could impact the security of cardholder data and/or sensitive authentication data. (Footnote 4)

“System components” include network devices, servers, computing devices, virtual components, cloud components, and software. Examples of system components include but are not limited to:
- Systems that store, process, or transmit account data (for example, payment terminals, authorization systems, clearing systems, payment middleware systems, payment back-office systems, shopping cart and store front systems, payment gateway/switch systems, fraud monitoring systems).
- Systems that provide security services (for example, authentication servers, access control servers, security information and event management (SIEM) systems, physical security systems (for example, badge access or CCTV), multi-factor authentication systems, anti-malware systems).
- Systems that facilitate segmentation (for example, internal network security controls).
- Systems that could impact the security of account data or the CDE (for example, name resolution, or e-commerce (web) redirection servers).
- Virtualization components such as virtual machines, virtual switches/routers, virtual appliances, virtual applications/desktops, and hypervisors.
- Cloud infrastructure and components, both external and on premises, and including instantiations of containers or images, virtual private clouds, cloud-based identity and access management, CDEs residing on premises or in the cloud, service meshes with containerized applications, and container orchestration tools.
- Network components, including but not limited to network security controls, switches, routers, VoIP network devices, wireless access points, network appliances, and other security appliances.
- Server types, including but not limited to web, application, database, authentication, mail, proxy, Network Time Protocol (NTP), and Domain Name System (DNS).
- End-user devices, such as computers, laptops, workstations, administrative workstations, tablets, and mobile devices.
- Printers, and multi-function devices that scan, print, and fax.
- Storage of account data in any format (for example, paper, data files, audio files, images, and video recordings).
- Applications, software, and software components, serverless applications, including all purchased, subscribed (for example, Software-as-a-Service), bespoke and custom software, including internal and external (for example, Internet) applications.
- Tools, code repositories, and systems that implement software configuration management or for deployment of objects to the CDE or to systems that can impact the CDE.

(Footnote 4: For additional guidance, refer to Information Supplement: Guidance for PCI DSS Scoping and Network Segmentation on the PCI SSC website.)

#### Figure 1. Understanding PCI DSS Scoping
[Figure 1. Understanding PCI DSS Scoping][https://drive.google.com/file/d/1o72nLwn3RJg4Ha7_Oce2EK6wPszJ7gjd/view?usp=sharing]

**Mục tiêu**
Xác định hệ thống nào nằm trong hoặc ngoài phạm vi PCI DSS dựa trên việc xử lý dữ liệu thẻ và mức độ ảnh hưởng đến CDE.

**1. Cardholder Data Environment (CDE)**
Một system được coi là **in scope** nếu:
- Lưu trữ, xử lý hoặc truyền CHD/SAD  
- Và/Hoặc:
  - Nằm cùng network với hệ thống xử lý CHD/SAD  
  - Có kết nối không bị giới hạn tới các hệ thống đó  

**2. Connected-to hoặc Security-impacting Systems**
System không trực tiếp xử lý dữ liệu thẻ nhưng vẫn **in scope** nếu:
Kết nối với CDE:
- Kết nối trực tiếp tới CDE  
- Kết nối gián tiếp tới CDE  

Ảnh hưởng đến bảo mật CDE:
- Ảnh hưởng đến cấu hình hoặc bảo mật của CDE  
- Cung cấp chức năng bảo mật cho CDE  
- Thực hiện segmentation giữa CDE và hệ thống ngoài phạm vi  
- Hỗ trợ các requirement của PCI DSS  

Lưu ý:
- System được coi là connected nếu khi bị compromise có thể ảnh hưởng đến bảo mật của CDE  
- Nếu không có kết nối trực tiếp hoặc gián tiếp:
  - Phải có control rõ ràng  
  - Phải được kiểm chứng (ví dụ: penetration testing)  

**3. Out-of-Scope Systems**
Một system chỉ được coi là **out of scope** khi thỏa tất cả điều kiện:
- Không lưu, xử lý hoặc truyền CHD/SAD  
- Không cùng subnet hoặc VLAN với hệ thống CDE  
- Không thể kết nối tới bất kỳ system nào trong CDE  
- Không thuộc nhóm connected-to hoặc security-impacting  

**Điều kiện bổ sung**
- Có thể tồn tại kết nối với hệ thống in-scope nếu:
  - Có control ngăn truy cập vào CDE  
- Nếu tất cả điều kiện trên được đáp ứng:
  → system được coi là ngoài phạm vi PCI DSS  

**Tóm tắt**
- Có liên quan hoặc ảnh hưởng đến CDE → in scope  
- Không liên quan và không thể ảnh hưởng → out of scope  

#### Annual PCI DSS Scope Confirmation
The first step in preparing for a PCI DSS assessment is for the entity to accurately determine the scope of the review. The assessed entity must confirm the accuracy of their PCI DSS scope according to PCI DSS Requirement 12.5.2 by identifying all locations and flows of account data, and identifying all systems that are connected to or, if compromised, could impact the CDE (for example, authentication servers, remote access servers, logging servers) to ensure they are included in the PCI DSS scope. All types of systems and locations should be considered during the scoping process, including backup/recovery sites and fail-over systems.

The minimum steps for an entity to confirm the accuracy of their PCI DSS scope are specified in PCI DSS Requirement 12.5.2. The entity is expected to retain documentation to show how PCI DSS scope was determined. The documentation is retained for assessor review and for reference during the entity’s next PCI DSS scope confirmation activity. For each PCI DSS assessment, the assessor validates that the entity accurately defined and documented the scope of the assessment.

**Note:** This annual confirmation of PCI DSS scope is defined at PCI DSS Requirement at 12.5.2 and is an activity expected to be performed by the entity. This activity is not the same, nor is it intended to be replaced by, the scoping confirmation performed by the entity’s assessor during the assessment.

#### Segmentation
Segmentation (or isolation) of the CDE from the remainder of an entity’s network is not a PCI DSS requirement. However, it is strongly recommended as a method that may reduce the:
- Scope of the PCI DSS assessment
- Cost of the PCI DSS assessment
- Cost and difficulty of implementing and maintaining PCI DSS controls
- Risk to an organization relative to payment account data (reduced by consolidating that data into fewer, more controlled locations)

Without adequate segmentation (sometimes called a "flat network"), the entire network is in scope for the PCI DSS assessment. Segmentation can be achieved using a number of physical or logical methods, such as properly configured internal network security controls, routers with strong access control lists, or other technologies that restrict access to a particular segment of a network. To be considered out of scope for PCI DSS, a system component must be properly segmented (isolated) from the CDE, such that the out-of-scope system component could not impact the security of cardholder data and/or sensitive authentication data, even if that component was compromised.

An important prerequisite to reduce the scope of the CDE is a clear understanding of business needs and processes related to the storage, processing, and transmission of account data. Restricting account data to as few locations as possible by eliminating unnecessary data and consolidating necessary data may require reengineering of long-standing business practices.

Documenting account data flows via a data-flow diagram helps an entity fully understand how account data comes into an organization, where it resides within the organization, and how it traverses through various systems within the organization. Data-flow diagrams also illustrate all locations where account data is stored, processed, and transmitted. This information supports an entity implementing segmentation and can also support confirming that segmentation is being used to isolate the CDE from out-of-scope networks.

If segmentation is used to reduce the scope of the PCI DSS assessment, the assessor must verify that the segmentation is adequate to reduce the scope of the assessment, as illustrated in Figure 2. At a high level, adequate segmentation isolates systems that store, process, or transmit account data from those that do not. However, the adequacy of a specific segmentation implementation is highly variable and depends on several factors such as a given network's configuration, the technologies deployed, and other controls that may be implemented.

#### [Figure 2. Segmentation and Impact to PCI DSS Scope]
[Figure 2. Segmentation and Impact to PCI DSS Scope][https://drive.google.com/file/d/1TbHc7QN0BxtGTqHNip3es8Jss0TyK44b/view?usp=sharing]
**Mục tiêu**
Sử dụng segmentation (phân tách mạng) để giảm phạm vi PCI DSS.
Điều kiện: các hệ thống ngoài phạm vi không được ảnh hưởng đến bảo mật của CDE.

**Flow quyết định**
1. Có segmentation không?
- Không có  
  → Toàn bộ hệ thống nằm trong phạm vi PCI DSS
- Có  
  → Chuyển sang bước 2

**2. Segmentation có được validate không?**
- Không validate được hiệu quả  
  → Toàn bộ hệ thống vẫn nằm trong phạm vi PCI DSS
- Đã validate hiệu quả  
  → Chuyển sang bước 3

**3. Kết quả**
Assessor phải:
- Ghi nhận cách segmentation được triển khai
- Ghi nhận cách kiểm chứng hiệu quả
Khi hợp lệ:
Phạm vi PCI DSS được giới hạn lại chỉ còn:
1. Hệ thống lưu, xử lý hoặc truyền CHD
2. Hệ thống kết nối với CDE
3. Hệ thống có thể ảnh hưởng đến bảo mật của CDE

**Tóm tắt**
- Không có segmentation → toàn bộ hệ thống in scope  
- Có segmentation nhưng không chứng minh được → vẫn toàn bộ in scope  
- Có segmentation và chứng minh được → scope được thu hẹp  

**Ví dụ**
Case 1:
- Tất cả hệ thống chung network với CDE  
→ Toàn bộ in scope  
Case 2:
- Có tách mạng nhưng không kiểm chứng  
→ Vẫn toàn bộ in scope  
Case 3:
- Có segmentation + firewall + kiểm chứng bằng testing  
→ Chỉ hệ thống liên quan CDE nằm trong scope  

#### Wireless
If wireless technology is used to store, process, or transmit account data (for example, wireless point-of-sale devices), or if a wireless local area network (WLAN) is part of or connected to the CDE, the PCI DSS requirements and testing procedures for securing wireless environments apply and must be performed.

Rogue wireless detection must be performed per PCI DSS Requirement 11.2.1 even when wireless is not used within the CDE and the entity has a policy that prohibits the use of wireless technology within its environment. This is because of the ease with which a wireless access point can be attached to a network, the difficulty in detecting its presence, and the increased risk presented by unauthorized wireless devices.

Before wireless technology is implemented, an entity should carefully evaluate the need for the technology against the risk. Consider deploying wireless technology only for non-sensitive data transmission.

#### When Cardholder Data and/or Sensitive Authentication Data is Accidentally Received via an Unintended Channel
There could be occurrences where an entity receives cardholder data and/or sensitive authentication data unsolicited via an insecure communication channel that was not intended for the purpose of receiving sensitive data. In this situation, the entity can choose to either:
- Include the channel in the scope of their CDE and secure it according to PCI DSS
Or
- Securely delete the data and implement measures to prevent the channel from being used in the future for sending such data.

#### Encrypted Cardholder Data and Impact on PCI DSS Scope
Encryption of cardholder data with strong cryptography is an acceptable method of rendering the data unreadable according to PCI DSS Requirement 3.5. However, encryption alone is generally insufficient to render the cardholder data out of scope for PCI DSS and does not remove the need for PCI DSS in that environment. The entity’s environment is still in scope for PCI DSS due to the presence of cardholder data. For example, for a merchant card-present environment, there is physical access to the payment cards to complete a transaction and there may also be paper reports or receipts with cardholder data. Similarly, in merchant card-not-present environments, such as mail-order/telephone-order and e-commerce, payment card details are provided via channels that need to be evaluated and protected according to PCI DSS.

The following are each in scope for PCI DSS:
- Systems performing encryption and/or decryption of cardholder data, and systems performing key management functions,
- Encrypted cardholder data that is not isolated from the encryption and decryption and key management processes,
- Encrypted cardholder data that is present on a system or media that also contains the decryption key,
- Encrypted cardholder data that is present in the same environment as the decryption key,
- Encrypted cardholder data that is accessible to an entity that also has access to the decryption key.

**Note:** A PCI-listed P2PE solution can significantly reduce the number of PCI DSS requirements applicable to a merchant’s cardholder data environment. However, it does not completely remove the applicability of PCI DSS in the merchant environment.

#### Encrypted Cardholder Data and Impact to PCI DSS Scope for Third-Party Service Providers
Where a third-party service provider (TPSP) receives and/or stores only data encrypted by another entity, and where they do not have the ability to decrypt the data, the TPSP may be able to consider the encrypted data out of scope if certain conditions are met. This is because responsibility for the data generally remains with the entity, or entities, with the ability to decrypt the data or impact the security of the encrypted data. Determining which party is responsible for specific PCI DSS controls will depend on several factors, including who has access to the decryption keys, the role performed by each party, and the agreement between parties. Responsibilities should be clearly defined and documented to ensure both the TPSP and the entity providing the encrypted data understand which entity is responsible for which security controls.

As an example, a TPSP providing storage services receives and stores encrypted cardholder data provided by customers for back-up purposes. This TPSP does not have access to the encryption or decryption keys, nor does it perform any key management for its customers. The TPSP can exclude any such encrypted data when determining its PCI DSS scope. However, the TPSP does maintain responsibility for controlling access to the encrypted data storage as part of its service agreements with its customers.

Responsibility for ensuring that the encrypted data and the cryptographic keys are protected according to applicable PCI DSS requirements is often shared between entities. In the above example, the customer determines which of their personnel are authorized to access the storage media, and the storage facility is responsible for managing the physical and/or logical access controls to ensure that only persons authorized by the customer are granted access to the storage media. The specific PCI DSS requirements applicable to a TPSP will depend on the services provided and the agreement between the two parties. In the example of a TPSP providing storage services, the physical and logical access controls provided by the TPSP will need to be reviewed at least annually. This review could be performed as part of the merchant’s PCI DSS assessment or, alternatively, the review could be performed, and controls validated, by the TPSP with appropriate evidence provided to the merchant. For information about “appropriate evidence,” see Options for TPSPs to Validate PCI DSS Compliance for TPSP Services that Meet Customers’ PCI DSS Requirements.

As another example, a TPSP that receives only encrypted cardholder data for the purposes of routing to other entities, and that does not have access to the data or cryptographic keys, may not have any PCI DSS responsibility for that encrypted data. In this scenario, where the TPSP is not providing any security services or access controls, they may be considered the same as a public or untrusted network, and it would be the responsibility of the entity(s) sending/receiving account data through the TPSP’s network to ensure PCI DSS controls are applied to protect the data being transmitted.

#### Use of Third-Party Service Providers
An entity (referred to as the “customer” in this section) might choose to use a third-party service provider (TPSP) to store, process, or transmit account data or to manage in-scope system components on the customer’s behalf. Use of a TPSP may have an impact on the security of a customer’s CDE.

**Note:** Use of a PCI DSS compliant TPSP does not make a customer PCI DSS compliant, nor does it remove the customer’s responsibility for its own PCI DSS compliance. Even if a customer uses a TPSP, that customer remains responsible for confirming its own compliance as requested by organizations that manage compliance programs (for example, payment brands and acquirers). Customers should contact these organizations for any requirements.

#### Using TPSPs and the Impact on Customers Meeting PCI DSS Requirement 12.8
There are many different scenarios where a customer might use one or more TPSPs for functions within or related to the customer’s CDE. In all scenarios where a TPSP is used, the customer must manage and oversee all their TPSP relationships and monitor the PCI DSS compliance status of their TPSPs in accordance with Requirement 12.8, including TPSPs that:
- Have access to the customer’s CDE,
- Manage in-scope system components on the customer’s behalf, and/or
- Can impact the security of the customer’s cardholder data and/or sensitive authentication data.

Managing TPSP relationships in accordance with Requirement 12.8 includes performing due diligence, having appropriate agreements in place, identifying which requirements apply to the customer and which apply to the TPSP, and monitoring the compliance status of TPSPs at least annually.

Requirement 12.8 does not specify that the customer’s TPSPs must be PCI DSS compliant, only that the customer monitors their compliance status as specified in the requirement. Therefore, a TPSP does not need to be PCI DSS compliant for its customer to meet Requirement 12.8.

#### Impact of Using TPSPs for Services that Meet Customers’ PCI DSS Requirements
When the TPSP provides a service that meets a PCI DSS requirement(s) on the customer’s behalf or where that service may impact the security of the customer’s cardholder data and/or sensitive authentication data, then those requirements are in scope for the customer’s assessment and the compliance of that service will impact the customer’s PCI DSS compliance. The TPSP must demonstrate it meets applicable PCI DSS requirements for those requirements to be in place for its customers. For example, if an entity engages a TPSP to manage its network security controls, and the TPSP does not provide evidence that it meets the applicable requirements in PCI DSS Requirement 1, then those requirements are not in place for the customer’s assessment. As another example, TPSPs that store backups of cardholder data on behalf of customers would need to meet the applicable requirements related to access controls, physical security, etc., for their customers to consider those requirements in place for their assessments.

#### Importance of Understanding Responsibilities Between TPSP Customers and TPSPs
When a TPSP provides a service that meets a PCI DSS requirement(s) on the customer’s behalf or where that service may impact the security of the customer’s cardholder data and/or sensitive authentication data, it is important that customers and TPSPs clearly identify and understand the following:
- The services and system components included in the scope of the TPSP’s PCI DSS assessment,
- The specific PCI DSS requirements and sub-requirements covered by the TPSP’s PCI DSS assessment,
- Any requirements that are the responsibility of the TPSP’s customers to include in their own PCI DSS assessments, and
- Any PCI DSS requirements for which the responsibility is shared between the TPSP and its customers.

For example, a cloud provider should clearly define which of its IP addresses are scanned as part of its quarterly vulnerability scan process and which IP addresses are their customers’ responsibility to scan.

Per Requirement 12.9.2, TPSPs are required to support their customers’ requests for information about the TPSP’s PCI DSS compliance status related to the services provided to customers, and about which PCI DSS requirements are the responsibility of the TPSP, which are the responsibility of the customer, and any responsibilities shared between the customer and the TPSP. Refer to Information Supplement: Third-Party Security Assurance for a sample responsibility matrix template that may be used for documenting and clarifying how responsibilities are shared between TPSPs and customers.

`Note that not all TPSP relationships require that TPSPs provide customers with documentation of how responsibilities are shared between TPSPs and customers. TPSPs are only required to share such documentation if that TPSP is meeting a PCI DSS requirement(s) on the customer’s behalf, if responsibility for meeting a PCI DSS requirement is shared between the TPSP and its customer, or if the TPSP’s service may impact the security of the customer’s cardholder data and/or sensitive authentication data. While a TPSP may not be required to provide its customers with such documentation because there are no shared responsibilities, the TPSP still needs to support customers by providing their PCI DSS compliance status information, so that customers can manage and monitor their TPSPs in accordance with PCI DSS Requirement 12.8.`

#### Options for TPSPs to Validate PCI DSS Compliance for TPSP Services that Meet Customers’ PCI DSS Requirements
TPSPs are responsible for demonstrating their PCI DSS compliance as requested by organizations that manage compliance programs (for example, payment brands and acquirers). TPSPs should contact these organizations for any requirements.

When a TPSP provides services that are intended to meet or facilitate meeting a customer’s PCI DSS requirements or that may impact the security of a customer’s cardholder data and/or sensitive authentication data, these requirements are in scope for the customer’s PCI DSS assessments. There are two options for TPSPs to validate compliance in this scenario:
- Annual assessment: TPSP undergoes an annual PCI DSS assessment(s) and provides evidence to its customers to show the TPSP meets the applicable PCI DSS requirements; or
- Multiple, on-demand assessments: If a TPSP does not undergo an annual PCI DSS assessment, it must undergo assessments upon request of their customers and/or participate in each of its customers’ PCI DSS assessments, with the results of each review provided to the respective customer(s).

If the TPSP undergoes its own PCI DSS assessment, it is expected to provide sufficient evidence to its customers to verify that the scope of the TPSP’s PCI DSS assessment covered the services applicable to the customer, and that the relevant PCI DSS requirements were examined and determined to be in place. If the provider has an PCI DSS Attestation of Compliance (AOC), it is expected that the TPSP provides the AOC to customers upon request. The customer may also request relevant sections of the TPSP’s PCI DSS Report on Compliance (ROC). The ROC may be redacted to protect any confidential information.

If the TPSP does not undergo its own PCI DSS assessment and therefore does not have an AOC, the TPSP is expected to provide specific evidence related to the applicable PCI DSS requirements, so that the customer (or its assessor) is able to confirm that the TPSP is meeting those PCI DSS requirements.

#### TPSP’s Presence on a Payment Brand List(s) of PCI DSS Compliant Service Providers
For a customer that is monitoring a TPSP’s compliance status in accordance with Requirement 12.8, the TPSP’s presence on a payment brand’s list of PCI DSS compliant service providers may be sufficient evidence of the TPSP’s compliance status if it is clear from the list that the services applicable to the customer were covered by the TPSP’s PCI DSS assessment. If it is not clear from the list, the customer should obtain other written confirmation that addresses the TPSP’s PCI DSS compliance status.

For a customer that is looking for evidence of PCI DSS compliance for requirements that a TPSP meets on a customer’s behalf or where the service provided can impact the security of the customer’s cardholder data and/or sensitive authentication data, the TPSP’s presence on a payment brand’s list of PCI DSS compliant service providers is not sufficient evidence that the applicable PCI DSS requirements for that TPSP were included in the assessment. If the TPSP has an PCI DSS AOC, it is expected to provide it to customers upon request.
