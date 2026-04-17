### A. Tài liệu gốc của Requirement 12

### B. Summary Overview của Control Objective 12.5
Tài liệu này mô tả chi tiết **Control Objective 12.5** của** Requirement 12** trong **PCI-DSS v4.0.1**, tập trung vào việc xác định, duy trì và xác nhận phạm vi (scope) PCI DSS và các hệ thống liên quan.
Mục tiêu chính là đảm bảo toàn bộ system components, data flow và kết nối liên quan đến cardholder data được xác định đầy đủ và luôn nằm trong phạm vi kiểm soát.
Gồm 3 sub-requirement chính:
- 12.5.1: Quản lý inventory system components
- 12.5.2: Xác nhận và duy trì PCI DSS scope
- 12.5.3: Đánh giá thay đổi cấu trúc tổ chức
Áp dụng cho toàn bộ hệ thống, dữ liệu và môi trường liên quan đến CDE.

### C. Key Points của Control Objective 12.5
- **Phạm vi áp dụng**: Tất cả system components, data flow và kết nối liên quan CDE.
- **Trách nhiệm**: **Tài liệu hóa** và duy trì inventory cũng như xác nhận phạm vi bảo mật.
- **Quản lý tài liệu / cấu hình**: Duy trì danh sách system components kèm mô tả chức năng và cách sử dụng.
- **Xác định scope**: Bao gồm xác định luồng dữ liệu (data flow), vị trí lưu trữ CHD, các hệ thống trong CDE và các kết nối liên quan.
- **Kiểm soát / bảo vệ**: Xác định các biện pháp chia phân vùng (segmentation control) và quản lý các kết nối từ bên thứ ba

### D. Deep Summary của Control Objective 12.5
**Bối cảnh:**
Nếu không xác định đúng phạm vi PCI DSS, các hệ thống chứa hoặc liên quan đến dữ liệu thẻ có thể bị bỏ sót và không được bảo vệ đầy đủ. Việc duy trì danh sách thành phần hệ thống hiện tại cho phép tổ chức thực hiện các yêu cầu bảo mật một cách chính xác và hiệu quả
**Nội dung cốt lõi:**
- Duy trì Inventory: Luôn cập nhật danh sách đầy đủ các system components trong phạm vi để tránh việc vô tình loại bỏ các hệ thống khỏi tiêu chuẩn cấu hình
- Phân tích luồng dữ liệu: Xác định rõ ràng cách thức dữ liệu thẻ di chuyển qua các giai đoạn thanh toán và các kênh chấp nhận khác nhau
- Xác định vị trí dữ liệu: Tìm kiếm và liệt kê tất cả các điểm lưu trữ, xử lý và truyền CHD, bao gồm cả các bản sao lưu và dữ liệu ngoài vùng CDE hiện tại
- Xác nhận phân vùng: Kiểm tra tính hiệu quả của segmentation và các kết nối từ bên thứ ba để đảm bảo ranh giới bảo mật
- Đánh giá thay đổi: Thực hiện rà soát lại phạm vi khi có sự thay đổi lớn về hạ tầng hoặc cấu trúc tổ chức để đảm bảo các kiểm soát vẫn được duy trì
**Dữ liệu đáng chú ý:**
- Phải có sơ đồ luồng dữ liệu (data flow diagram) và danh sách vị trí CHD
- Thực hiện xác nhận scope tối thiểu 12 tháng/lần hoặc sau khi có thay đổi lớn
- Service Provider phải thực hiện xác nhận scope ít nhất 6 tháng/lần
**Rủi ro / Lưu ý:**
- Scope không đầy đủ dẫn đến việc bỏ sót các hệ thống quan trọng cần được bảo vệ
- Thiếu inventory cập nhật khiến tổ chức không biết rõ các hệ thống nào đang nằm trong phạm vi kiểm soát
- Các kết nối từ bên thứ ba không được kiểm soát có thể trở thành điểm xâm nhập rủi ro vào CDE
- Hiểu sai về segmentation dẫn đến việc áp dụng sai phạm vi bảo mật cho môi trường

### E. Structured Output của Control Objective 12.5
**Control objectives:**12.5
**Sub-requirement:**12.5.1
**Defined Approach Requirements:**An inventory of system components that are in scope for PCI DSS, including a description of function/use, is maintained and kept current.
**Defined Approach Testing Procedures:**
- "12.5.1.a": Examine the inventory to verify it includes all in-scope system components and a description of function/use for each.
- "12.5.1.b": Interview personnel to verify the inventory is kept current.
**Customized Approach Objective:**All system components in scope for PCI DSS are identified and known.
**Guidance - Purpose:**Maintaining a current list of all system components will enable an organization to define the scope of its environment and implement PCI DSS requirements accurately and efficiently. Without an inventory, some system components could be overlooked and be inadvertently excluded from the organization's configuration standards.
**Guidance - Good Practice:**If an entity keeps an inventory of all assets, those system components in scope for PCI DSS should be clearly identifiable among the other assets. Inventories should include containers or images that may be instantiated. Assigning an owner to the inventory helps to ensure the inventory stays current.
**Guidance - Examples:**Methods to maintain an inventory include as a database, as a series of files, or in an inventory- management tool.

---
**Control objectives:**12.5
**Sub-requirement:**12.5.2
**Defined Approach Requirements:**PCI DSS scope is documented and confirmed by the entity at least once every 12 months and upon significant change to the in-scope environment. At a minimum, the scoping validation includes:
• Identifying all data flows for the various payment stages (for example, authorization, capture settlement, chargebacks, and refunds) and acceptance channels (for example, card- present, card-not-present, and e-commerce).
• Updating all data-flow diagrams per Requirement 1.2.4.
• Identifying all locations where account data is stored, processed, and transmitted, including but not limited to: 1) any locations outside of the currently defined CDE, 2) applications that process CHD, 3) transmissions between systems and networks, and 4) file backups.
• Identifying all system components in the CDE, connected to the CDE, or that could impact security of the CDE.
• Identifying all segmentation controls in use and the environment(s) from which the CDE is segmented, including justification for environments being out of scope.
• Identifying all connections from third-party entities with access to the CDE.
• Confirming that all identified data flows, account data, system components, segmentation controls, and connections from third parties with access to the CDE are included in scope.
**Defined Approach Testing Procedures:**
- "12.5.2.a": Examine documented results of scope reviews and interview personnel to verify that the reviews are performed: • At least once every 12 months. • After significant changes to the in-scope environment.
- "12.5.2.b": Examine documented results of scope reviews performed by the entity to verify that PCI DSS scoping confirmation activity includes all elements specified in this requirement.
**Customized Approach Objective:**PCI DSS scope is verified periodically, and after significant changes, by comprehensive analysis and appropriate technical measures.
**Applicability Notes:**This annual confirmation of PCI DSS scope is an activity expected to be performed by the entity under assessment, and is not the same, nor is it intended to be replaced by, the scoping confirmation performed by the entity's assessor during the annual assessment.
**Guidance - Purpose:**Frequent validation of PCI DSS scope helps to ensure PCI DSS scope remains up to date and aligned with changing business objectives, and therefore that security controls are protecting all appropriate system components.
**Guidance - Good Practice:**Accurate scoping involves critically evaluating the CDE and all connected system components to determine the necessary coverage for PCI DSS requirements. Scoping activities, including careful analysis and ongoing monitoring, help to ensure that in-scope systems are appropriately secured. When documenting account data locations, the entity can consider creating a table or spreadsheet that includes the following information:
• Data stores (databases, files, cloud, etc.), including the purpose of data storage and the retention period,
• Which CHD elements are stored (PAN, expiry date, cardholder name, and/or any elements of SAD prior to completion of authorization),
• How data is secured (type of encryption and strength, hashing algorithm and strength, truncation, tokenization),
• How access to data stores is logged, including a description of logging mechanism(s) in use (enterprise solution, application level, operating system level, etc.).
In addition to internal systems and networks, all connections from third-party entities—for example, business partners, entities providing remote support services, and other service providers—need to be identified to determine inclusion for PCI DSS scope. Once the in-scope connections have been identified, the applicable PCI DSS controls can be implemented to reduce the risk of a third-party connection being used to compromise an entity's CDE. A data discovery tool or methodology can be used to facilitate identifying all sources and locations of PAN, and to look for PAN that resides on systems and networks outside the currently defined CDE or in unexpected places within the defined CDE—for example, in an error log or memory dump file. This approach can help ensure that previously unknown locations of PAN are detected and that the PAN is either eliminated or properly secured.
**Guidance - Further Information:**For additional guidance, refer to Information Supplement: Guidance for PCI DSS Scoping and Network Segmentation .

---
**Control objectives:**12.5
**Sub-requirement:**12.5.2.1
**Defined Approach Requirements:**Additional requirement for service providers only: PCI DSS scope is documented and confirmed by the entity at least once every six months and upon significant change to the in-scope environment. At a minimum, the scoping validation includes all the elements specified in Requirement 12.5.2.
**Defined Approach Testing Procedures:**
- "12.5.2.1.a": Additional testing procedure for service provider assessments only: Examine documented results of scope reviews and interview personnel to verify that reviews per Requirement 12.5.2 are performed: • At least once every six months, and • After significant changes
- "12.5.2.1.b": Additional testing procedure for service provider assessments only: Examine documented results of scope reviews to verify that scoping validation includes all elements specified
**Customized Approach Objective:** The accuracy of PCI DSS scope is verified to be continuously accurate by comprehensive analysis and appropriate technical measures.
**Applicability Notes:** This requirement applies only when the entity being assessed is a service provider. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose:**Service providers typically have access to greater volumes of cardholder data than do merchants, or can provide an entry point that can be exploited to then compromise multiple other entities. Service providers also typically have larger and more complex networks that are subject to more frequent change. The probability of overlooked changes to scope in complex and dynamic networks is greater in service-providers environments. Validating PCI DSS scope more frequently is likely to discover such overlooked changes before they can be exploited by an attacker.

---
**Control objectives:**12.5
**Sub-requirement:**12.5.3
**Defined Approach Requirements:**Additional requirement for service providers only: Significant changes to organizational structure result in a documented (internal) review of the impact to PCI DSS scope and applicability of controls, with results communicated to executive management.
**Defined Approach Testing Procedures:**
- "12.5.3.a": Additional testing procedure for service provider assessments only: Examine policies and procedures to verify that processes are defined such that a significant change to organizational structure results in documented review of the impact to PCI DSS scope and applicability of controls.
- "12.5.3.b": Additional testing procedure for service provider assessments only: Examine documentation (for example, meeting minutes) and interview responsible personnel to verify that significant changes to organizational structure resulted in documented reviews that included all elements specified in this requirement, with results communicated to executive management.
**Customized Approach Objective:**PCI DSS scope is confirmed after significant organizational change.
**Applicability Notes:**This requirement applies only when the entity being assessed is a service provider. This requirement is a best practice until 31 March 2025, after which it will be required and must be
**Guidance - Purpose:**An organization's structure and management define the requirements and protocol for effective and secure operations. Changes to this structure could have negative effects to existing controls and frameworks by reallocating or removing resources that once supported PCI DSS controls or inheriting new responsibilities that may not have established controls in place. Therefore, it is important to revisit PCI DSS scope and controls when there are changes to an organization's structure and management to ensure controls are in place and active.
**Guidance - Examples:**Changes to organizational structure include, but are not limited to, company mergers or acquisitions, and significant changes or reassignments of personnel with responsibility for security controls.