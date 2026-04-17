### A. Tài liệu gốc của Chương 5 (Control 5.15, 5.16)

### B. Summary Overview của Chương 5 (Control 5.15, 5.16)
Tài liệu này mô tả chi tiết **mục 5.15 và 5.16** trong **Chương 5 (Organizational controls)** của **ISO/IEC 27002:2022**, tập trung vào việc kiểm soát quyền truy cập vào thông tin và tài sản liên quan, đồng thời quản lý vòng đời định danh để gán đúng quyền cho đúng đối tượng.
Mục tiêu chung của nhóm nội dung này là bảo đảm chỉ đối tượng được phép mới có thể truy cập tài sản thông tin, đồng thời mỗi người dùng hay hệ thống đều có định danh rõ ràng để việc cấp, rà soát và thu hồi quyền truy cập diễn ra nhất quán.
Gồm 2 mục chính:
- `5.15`: Access control - thiết lập và thực thi quy tắc kiểm soát truy cập vật lý và logic theo nhu cầu nghiệp vụ và an toàn thông tin
- `5.16`: Identity management - quản lý đầy đủ vòng đời định danh để gán quyền truy cập phù hợp

Áp dụng cho bộ phận quản trị truy cập, vận hành hệ thống, chủ sở hữu tài sản thông tin và các bên có liên quan đến việc cấp quyền hoặc xác thực định danh.

### C. Key Points của Chương 5 (Control 5.15, 5.16)
- **Mục tiêu quản trị:** nhóm control này tạo nền tảng để xác định ai được truy cập gì, theo điều kiện nào, và trên cơ sở định danh nào.
- **Yêu cầu chính của 5.15:** tổ chức phải thiết lập và vận hành access control dựa trên yêu cầu nghiệp vụ và bảo mật, bao gồm cả truy cập vật lý lẫn logic.
- **Yêu cầu chính của 5.16:** tổ chức phải quản lý toàn bộ vòng đời định danh, từ cấp mới, gán cho đúng đối tượng, đến cập nhật, vô hiệu hóa và thu hồi khi không còn cần thiết.
- **Điểm vận hành quan trọng:** access control và identity management phải đi cùng nhau; nếu định danh không chuẩn thì quyền truy cập, log và truy vết cũng mất độ tin cậy.
- **Lưu ý thực tế:** các mô hình như least privilege, need-to-know, RBAC hay ABAC chỉ hiệu quả khi có quy trình phê duyệt, rà soát định kỳ và trách nhiệm rõ ràng.

### D. Deep Summary của Chương 5 (Control 5.15, 5.16)
**Bối cảnh:**
Đây là nhóm control nền tảng cho việc quản lý truy cập trong toàn bộ hệ thống an toàn thông tin. Tổ chức không chỉ phải quyết định ai được vào hệ thống, mà còn phải biết đối tượng đó là ai, định danh nào đang được sử dụng và quyền nào đang gắn với định danh đó.

**Nội dung cốt lõi:**
- `5.15` đặt ra yêu cầu kiểm soát truy cập dựa trên nhu cầu nghiệp vụ và mức bảo vệ cần thiết cho từng loại thông tin, tài sản, hệ thống hoặc dịch vụ.
- `5.15` nhấn mạnh việc xác định rõ quyền truy cập, giới hạn truy cập đặc quyền, phân tách nhiệm vụ và kiểm soát cả kênh truy cập vật lý lẫn logic.
- `5.15` cũng yêu cầu cân nhắc môi trường triển khai thực tế như kết nối phân tán, quyền truy cập theo ngữ cảnh, và mức độ chi tiết của rule access control.
- `5.16` tập trung vào việc quản lý định danh theo vòng đời đầy đủ: xác minh, tạo lập, kích hoạt, thay đổi, vô hiệu hóa và ghi nhận sự kiện liên quan.
- `5.16` đặc biệt quan trọng khi tổ chức dùng shared identity, identity của bên thứ ba hoặc định danh cho thực thể không phải con người, vì các trường hợp này làm tăng rủi ro trách nhiệm và truy vết.

**Dữ liệu đáng chú ý:**
- `5.15` gắn với `#Preventive`, `#Protect`, `#Identity_and_access_management` và `#Protection`, cho thấy đây là control có vai trò ngăn chặn truy cập trái phép bằng cơ chế quản trị rõ ràng.
- `5.16` cũng là `#Preventive` và thuộc cùng miền quản trị truy cập, nên hai control được thiết kế để bổ trợ trực tiếp cho nhau.
- `5.15` liên kết mạnh với `5.10`, `5.12`, `5.13`, `5.16`, `5.17`, `5.18`, `8.15`, phản ánh rằng access control không thể vận hành độc lập.
- `5.16` nêu rõ sự khác biệt giữa định danh cá nhân, định danh dùng chung, định danh của thực thể không phải con người và định danh do bên thứ ba cung cấp.

**Rủi ro / Lưu ý:**
- Nếu access control được thiết kế quá lỏng, tổ chức sẽ dễ cấp thừa quyền, đặc quyền kéo dài hoặc truy cập vượt phạm vi cần thiết.
- Nếu identity lifecycle không được quản lý chặt, tài khoản mồ côi, shared identity hoặc duplicate identity sẽ làm suy yếu khả năng truy vết và quy trách nhiệm.
- Việc chỉ có policy mà không có procedure, ownership và review định kỳ sẽ khiến access control trở thành tài liệu hình thức.
- Các control này cần được gắn với logging, approval, monitoring và periodic review; nếu không, tổ chức khó phát hiện quyền sai hoặc sử dụng sai.

### E. Structured Output của Chương 5 (Control 5.15, 5.16)
**Section:** 5.15
**Title:** Access control

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Informationsecurity properties | #Confidentiality#Integrity#Availability |
| Cybersecurityconcepts | #Protect |
| Operationalcapabilities | #Identity_and_ac-cess_management |
| Security domains | #Protection |

**Control:**
Rules to control physical and logical access to information and other associated assets should be established and implemented based on business and information security requirements.

**Purpose:**
To ensure authorized access and to prevent unauthorized access to information and other associated assets.

**Guidance:**
Owners of information and other associated assets should determine information security and business requirements related to access control. A topic-specific policy on access control should be defined which takes account of these requirements and should be communicated to all relevant interested parties.
These requirements and the topic-specific policy should consider the following:
- determining which entities require which type of access to the information and other associated assets;
- security of applications (see 8.26);
- physical access, which needs to be supported by appropriate physical entry controls (see 7.2, 7.3, 7.4);
- information dissemination and authorization (e.g. the need-to-know principle) and information security levels and classification of information (see 5.10, 5.12, 5.13);
- restrictions to privileged access (see 8.2);
- segregation of duties (see 5.3);
- relevant legislation, regulations and any contractual obligations regarding limitation of access to data or services (see 5.31, 5.32, 5.33, 5.34, 8.3);
- segregation of access control functions (e.g. access request, access authorization, access administration);
- formal authorization of access requests (see 5.16 and 5.18);
- the management of access rights (see 5.18);
- logging (see 8.15).

Access control rules should be implemented by defining and mapping appropriate access rights and restrictions to the relevant entities (see 5.16). An entity can represent a human user as well as a technical or logical item (e.g. a machine, device or a service). To simplify the access control management, specific roles can be assigned to entity groups.
The following should be taken into account when defining and implementing access control rules:
- consistency between the access rights and information classification;
- consistency between the access rights and the physical perimeter security needs and requirements;
- considering all types of available connections in distributed environments so entities are only provided with access to information and other associated assets, including networks and network services, that they are authorized to use;
- considering how elements or factors relevant to dynamic access control can be reflected.

**Other information:**
There are often overarching principles used in the context of access control. Two of the most frequently used principles are:
- need-to-know: an entity is only granted access to the information which that entity requires in order to perform its tasks (different tasks or roles mean different need-to-know information and hence different access profiles);
- need-to-use: an entity is only assigned access to information technology infrastructure where a clear need is present.
Care should be taken when specifying access control rules to consider:
- establishing rules based on the premise of least privilege, “Everything is generally forbidden unless expressly permitted”, rather than the weaker rule, “Everything is generally permitted unless expressly forbidden”;
- changes in information labels (see 5.13) that are initiated automatically by information processing facilities and those initiated at the discretion of a user;
- changes in user permissions that are initiated automatically by the information system and those initiated by an administrator;
- when to define and regularly review the approval.

Access control rules should be supported by documented procedures (see 5.16, 5.17, 5.18, 8.2, 8.3, 8.4, 8.5, 8.18) and defined responsibilities (see 5.2, 5.17).
There are several ways to implement access control, such as MAC (mandatory access control), DAC (discretionary access control), RBAC (role-based access control) and ABAC (attribute-based access control).
Access control rules can also contain dynamic elements (e.g. a function that evaluates past accesses or specific environment values). Access control rules can be implemented in different granularity, ranging from covering whole networks or systems to specific data fields and can also consider properties such as user location or the type of network connection that is used for access. These principles and how granular access control is defined can have a significant cost impact. Stronger rules and more granularity typically lead to higher cost. Business requirements and risk considerations should be used to define which access control rules are applied and which granularity is required.

---
**Section:** 5.16
**Title:** Identity management

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Informationsecurity properties | #Confidentiality#Integrity#Availability |
| Cybersecurityconcepts | #Protect |
| Operationalcapabilities | #Identity_and_ac-cess_management |
| Security domains | #Protection |

**Control:**
The full life cycle of identities should be managed.

**Purpose:**
To allow for the unique identification of individuals and systems accessing the organization’s information and other associated assets and to enable appropriate assignment of access rights.

**Guidance:**
The processes used in the context of identity management should ensure that:
- for identities assigned to persons, a specific identity is only linked to a single person to be able to hold the person accountable for actions performed with this specific identity;
- identities assigned to multiple persons (e.g. shared identities) are only permitted where they are necessary for business or operational reasons and are subject to dedicated approval and documentation;
- identities assigned to non-human entities are subject to appropriately segregated approval and independent ongoing oversight;
- identities are disabled or removed in a timely fashion if they are no longer required (e.g. if their associated entities are deleted or no longer used, or if the person linked to an identity has left the organization or changed the role);
- in a specific domain, a single identity is mapped to a single entity, [i.e. mapping of multiple identities to the same entity within the same context (duplicate identities) is avoided];
- records of all significant events concerning the use and management of user identities and of authentication information are kept.

The organization should have a supporting process in place to handle changes to information related to user identities. These processes can include re-verification of trusted documents related to a person.
When using identities provided or issued by third parties (e.g. social media credentials), the organization should ensure the third-party identities provide the required trust level and any associated risks are known and sufficiently treated. This can include controls related to the third parties (see 5.19) as well as controls related to associated authentication information (see 5.17).

**Other information:**
Providing or revoking access to information and other associated assets is usually a multi-step procedure:
- confirming the business requirements for an identity to be established;
- verifying the identity of an entity before allocating them a logical identity;
- establishing an identity;
- configuring and activating the identity. This also includes configuration and initial setup of related authentication services;
- providing or revoking specific access rights to the identity, based on appropriate authorization or entitlement decisions (see 5.18).