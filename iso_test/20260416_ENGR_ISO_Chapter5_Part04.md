### A. Tài liệu gốc của Chương 5 (Control 5.9, 5.10)

### B. Summary Overview của Chương 5 (Control 5.9, 5.10)
Tài liệu này mô tả chi tiết **mục 5.9 và 5.10** trong **chương 5. Organizational controls** của **ISO/IEC 27002:2022**, tập trung vào việc giúp tổ chức nhận diện đúng tài sản thông tin, gán trách nhiệm quản lý phù hợp và kiểm soát cách các tài sản đó được sử dụng, xử lý và bảo vệ trong thực tế.
Mục tiêu chung của nhóm nội dung này là **tạo nền tảng quản trị tài sản thông tin rõ ràng**, từ khâu kiểm kê, phân loại, gán chủ sở hữu cho đến việc quy định hành vi sử dụng chấp nhận được đối với thông tin và các tài sản liên quan.
Gồm 2 mục chính:
- `5.9`: Inventory of information and other associated assets - nhận diện, kiểm kê và gán ownership cho tài sản thông tin và tài sản liên quan
- `5.10`: Acceptable use of information and other associated assets - thiết lập quy tắc sử dụng và xử lý tài sản thông tin theo cách phù hợp và được kiểm soát

Áp dụng cho các bộ phận quản trị tài sản, an toàn thông tin, vận hành hệ thống, người dùng nội bộ và các bên liên quan tham gia sử dụng, lưu trữ hoặc xử lý thông tin và tài sản hỗ trợ.

### C. Key Points của Chương 5 (Control 5.9, 5.10)
- **Mục tiêu quản trị:** Nhóm control này giúp tổ chức có cái nhìn đầy đủ về tài sản thông tin đang sở hữu hoặc sử dụng, từ đó áp dụng phân loại, phân quyền, trách nhiệm và cách sử dụng phù hợp với mức độ quan trọng của từng tài sản.
- **Yêu cầu chính của 5.9:** Tổ chức phải xây dựng và duy trì inventory cho thông tin và các tài sản liên quan, đồng thời xác định ownership rõ ràng để làm cơ sở cho việc bảo vệ, phân loại, rà soát và xử lý rủi ro trong toàn bộ vòng đời tài sản.
- **Yêu cầu chính của 5.10:** Tổ chức cần ban hành quy tắc và thủ tục về acceptable use để người dùng hiểu rõ hành vi được phép, hành vi bị cấm và trách nhiệm xử lý thông tin, bản sao, phương tiện lưu trữ hay tài sản hỗ trợ theo đúng mức bảo vệ yêu cầu.
- **Điểm vận hành quan trọng:** Inventory chỉ có giá trị khi luôn chính xác, được cập nhật kịp thời và liên kết được với phân loại, access restriction, disposal và các quy trình quản trị tài sản khác; nếu không, ownership và control phía sau sẽ nhanh chóng mất hiệu lực.
- **Lưu ý thực tế:** Trong nhiều trường hợp tài sản không thuộc sở hữu trực tiếp của tổ chức như cloud services, tổ chức vẫn phải nhận diện, kiểm soát việc sử dụng và ràng buộc trách nhiệm bảo vệ thông tin thông qua các cơ chế phù hợp như hợp đồng hoặc thỏa thuận dịch vụ.

### D. Deep Summary của Chương 5 (Control 5.9, 5.10)
**Bối cảnh:**
Nhóm control `5.9-5.10` tập trung vào nền tảng rất thực tế của quản trị an toàn thông tin: tổ chức phải biết mình đang có tài sản gì, ai chịu trách nhiệm với từng tài sản, và các tài sản đó được phép sử dụng như thế nào. Nếu không có inventory rõ ràng và quy tắc sử dụng nhất quán, nhiều kiểm soát khác như phân loại, phân quyền, xử lý rủi ro hay xóa bỏ an toàn sẽ khó vận hành hiệu quả.

**Nội dung cốt lõi:**
- `5.9` yêu cầu tổ chức nhận diện, lập danh mục và duy trì thông tin về các tài sản thông tin cũng như tài sản liên quan, đồng thời gán ownership để có đầu mối chịu trách nhiệm quản lý trong suốt vòng đời tài sản.
- `5.9` không chỉ dừng ở việc có một danh sách tài sản, mà còn yêu cầu inventory phải chính xác, cập nhật, liên kết với phân loại thông tin, access restriction, disposal và các hoạt động quản trị rủi ro hoặc audit.
- `5.10` yêu cầu tổ chức xây dựng topic-specific policy và thủ tục cụ thể để kiểm soát acceptable use, từ đó xác định rõ cách người dùng được phép sử dụng, sao chép, lưu trữ, truyền tải hoặc hủy bỏ thông tin và tài sản hỗ trợ.
- `5.10` mở rộng phạm vi từ hành vi người dùng sang governance của toàn bộ information life cycle, bao gồm bản sao tạm thời hoặc lâu dài, phương tiện lưu trữ, quy trình disposal và cả tình huống sử dụng tài sản của bên thứ ba như dịch vụ đám mây.

**Dữ liệu đáng chú ý:**
- `5.9` là kiểm soát `#Preventive`, gắn với `#Identify`, cho thấy inventory là điểm khởi đầu để tổ chức biết cái gì cần được bảo vệ và ai là người chịu trách nhiệm.
- `5.9` có liên hệ chặt với `5.12` và `5.13`, vì inventory và ownership chỉ thực sự hữu ích khi đi kèm với classification và labeling phù hợp.
- `5.10` là kiểm soát `#Preventive`, gắn nhiều hơn với `#Protect`, phản ánh việc acceptable use đóng vai trò hướng dẫn hành vi sử dụng và xử lý tài sản theo các mức bảo vệ đã xác định.
- Cả hai control đều thuộc lớp governance và protection, nghĩa là chúng vừa hỗ trợ định hướng quản trị ở cấp tổ chức, vừa ảnh hưởng trực tiếp đến cách kiểm soát được thực hiện hàng ngày bởi người dùng và đội vận hành.

**Rủi ro / Lưu ý:**
- Nếu inventory thiếu, sai hoặc không được cập nhật, tổ chức có thể bỏ sót tài sản quan trọng, gán ownership không đúng, hoặc áp dụng phân loại và quyền truy cập không phù hợp với mức độ nhạy cảm thực tế.
- Nếu acceptable use chỉ tồn tại trên tài liệu mà không được truyền đạt rõ cho người dùng, nguy cơ sử dụng sai mục đích, sao chép không kiểm soát hoặc xử lý tài sản không an toàn sẽ tăng lên đáng kể.
- Với tài sản của bên thứ ba như public cloud services, tổ chức vẫn phải chịu trách nhiệm đối với việc bảo vệ thông tin liên quan; không thể xem việc thuê ngoài là chuyển giao toàn bộ nghĩa vụ kiểm soát.
- Các control này chỉ phát huy hiệu quả khi được kết nối với các quy trình khác như classification, access control, disposal, logging, incident response và supplier management.

### E. Structured Output của Chương 5 (Control 5.9, 5.10)
**Section:** 5.9
**Title:** Inventory of information and other associated assets

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Informationsecurity properties | #Confidentiality#Integrity#Availability |
| Cybersecurityconcepts | #Identify |
| Operationalcapabilities | #Asset_manage-ment |
| Security domains | #Governance_and_Eco-system #Protection |

**Control:**
An inventory of information and other associated assets, including owners, should be developed and maintained.

**Purpose:**
To identify the organization’s information and other associated assets in order to preserve their information security and assign appropriate ownership.

**Guidance:**
***Inventory:***
The organization should identify its information and other associated assets and determine their importance in terms of information security. Documentation should be maintained in dedicated or existing inventories as appropriate.
The inventory of information and other associated assets should be accurate, up to date, consistent and aligned with other inventories. Options for ensuring accuracy of an inventory of information and other associated assets include:
- conducting regular reviews of identified information and other associated assets against the asset inventory;
- automatically enforcing an inventory update in the process of installing, changing or removing an asset.

The location of an asset should be included in the inventory as appropriate.
The inventory does not need to be a single list of information and other associated assets. Considering that the inventory should be maintained by the relevant functions, it can be seen as a set of dynamic inventories, such as inventories for information assets, hardware, software, virtual machines (VMs), facilities, personnel, competence, capabilities and records.
Each asset should be classified in accordance with the classification of the information (see 5.12) associated to that asset.
The granularity of the inventory of information and other associated assets should be at a level appropriate for the needs of the organization. Sometimes specific instances of assets in the information life cycle are not feasible to be documented due to the nature of the asset. An example of a short-lived asset is a VM instance whose life cycle can be of short duration.
***Ownership:***
For the identified information and other associated assets, ownership of the asset should be assigned to an individual or a group and the classification should be identified (see 5.12, 5.13). A process to ensure timely assignment of asset ownership should be implemented. Ownership should be assigned when assets are created or when assets are transferred to the organization. Asset ownership should be reassigned as necessary when current asset owners leave or change job roles.
***Owner duties:***
The asset owner should be responsible for the proper management of an asset over the whole asset life cycle, ensuring that:
- information and other associated assets are inventoried;
- information and other associated assets are appropriately classified and protected;
- the classification is reviewed periodically;
- components supporting technology assets are listed and linked, such as database, storage, software components and sub-components;
- requirements for the acceptable use of information and other associated assets (see 5.10) are established;
- access restrictions correspond with the classification and that they are effective and are reviewed periodically;
- information and other associated assets, when deleted or disposed, are handled in a secure manner and removed from the inventory;
- they are involved in the identification and management of risks associated with their asset(s);
- they support personnel who have the roles and responsibilities of managing their information.

**Other information:**
Inventories of information and other associated assets are often necessary to ensure the effective protection of information and can be required for other purposes, such as health and safety, insurance or financial reasons. Inventories of information and other associated assets also support risk management, audit activities, vulnerability management, incident response and recovery planning.
Tasks and responsibilities can be delegated (e.g. to a custodian looking after the assets on a daily basis), but the person or group who delegated them remains accountable.
It can be useful to designate groups of information and other associated assets which act together to provide a particular service. In this case, the owner of this service is accountable for the delivery of the service, including the operation of its assets.
See ISO/IEC 19770-1 for additional information on information technology (IT) asset management. See ISO 55001 for additional information on asset management.

---
**Section:** 5.10
**Title:** Acceptable use of information and other associated assets

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Protect |
| Operational capabilities | #Asset_management #Information_pro- tection |
| Security domains | #Governance_and_Ecosys- tem #Protection |

**Control:**
Rules for the acceptable use and procedures for handling information and other associated assets should be identified, documented and implemented.

**Purpose:**
To ensure information and other associated assets are appropriately protected, used and handled.

**Guidance:**
Personnel and external party users using or having access to the organization’s information and other associated assets should be made aware of the information security requirements for protecting and handling the organization’s information and other associated assets. They should be responsible for their use of any information processing facilities.
The organization should establish a topic-specific policy on the acceptable use of information and other associated assets and communicate it to anyone who uses or handles information and other associated assets. The topic-specific policy on acceptable use should provide clear direction on how individuals are expected to use information and other associated assets. The topic-specific policy should state:
- expected and unacceptable behaviours of individuals from an information security perspective;
- permitted and prohibited use of information and other associated assets;
- monitoring activities being performed by the organization.

Acceptable use procedures should be drawn up for the full information life cycle in accordance with its classification (see 5.12) and determined risks. The following items should be considered:
- access restrictions supporting the protection requirements for each level of classification;
- maintenance of a record of the authorized users of information and other associated assets;
- protection of temporary or permanent copies of information to a level consistent with the protection of the original information;
- storage of assets associated with information in accordance with manufacturers’ specifications (see 7.8);
- clear marking of all copies of storage media (electronic or physical) for the attention of the authorized recipient (see 7.10);
- authorization of disposal of information and other associated assets and supported deletion method(s) (see 8.10).

**Other information:**
It can be the case that the assets concerned do not directly belong to the organization, such as public cloud services. The use of such third-party assets and any assets of the organization associated with such external assets (e.g. information, software) should be identified as applicable and controlled, for example, through agreements with cloud service providers. Care should also be taken when a collaborative working environment is used.