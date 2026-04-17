### A. Tài liệu gốc của Chương 5 (Control 5.11, 5.12)

### B. Summary Overview của Chương 5 (Control 5.11, 5.12)
Tài liệu này mô tả chi tiết **mục 5.11 và 5.12** trong **chương 5. Organizational controls** của **ISO/IEC 27002:2022**, tập trung vào việc bảo đảm tài sản được hoàn trả đúng cách khi thay đổi quan hệ làm việc và thông tin được phân loại phù hợp với mức độ quan trọng, nhạy cảm và nhu cầu bảo vệ của tổ chức.
Mục tiêu chung của nhóm nội dung này là **bảo vệ tài sản và thông tin xuyên suốt vòng đời sử dụng**, từ thời điểm nhân sự hoặc bên liên quan rời vai trò của họ cho đến việc xác định đúng mức độ bảo vệ cần áp dụng cho từng loại thông tin.
Gồm 2 mục chính:
- `5.11`: Return of assets - bảo đảm tài sản và thông tin liên quan được hoàn trả, chuyển giao hoặc xử lý an toàn khi thay đổi hoặc chấm dứt quan hệ làm việc
- `5.12`: Classification of information - phân loại thông tin theo mức độ quan trọng và nhu cầu bảo vệ về confidentiality, integrity và availability
Áp dụng cho bộ phận nhân sự, an toàn thông tin, quản trị tài sản, vận hành hệ thống, chủ sở hữu thông tin và các cá nhân hoặc bên liên quan đang nắm giữ tài sản hay xử lý thông tin của tổ chức.

### C. Key Points của Chương 5 (Control 5.11, 5.12)
- **Mục tiêu quản trị:** Nhóm control này giúp tổ chức tránh thất thoát tài sản, tri thức và thông tin khi nhân sự thay đổi vai trò, đồng thời bảo đảm mọi loại thông tin được xử lý theo mức độ nhạy cảm và tác động kinh doanh tương ứng.
- **Yêu cầu chính của 5.11:** Tổ chức cần formalize quy trình thay đổi hoặc chấm dứt quan hệ làm việc để thu hồi tài sản vật lý, tài sản điện tử và thông tin liên quan, đồng thời ngăn chặn việc sao chép trái phép trong giai đoạn chuyển tiếp.
- **Yêu cầu chính của 5.12:** Tổ chức phải có classification scheme rõ ràng để chủ sở hữu thông tin xác định mức bảo vệ cần thiết, gắn phân loại với cách chia sẻ, hạn chế truy cập, xử lý và bảo vệ thông tin trong suốt vòng đời của nó.
- **Điểm vận hành quan trọng:** Classification chỉ có giá trị khi thống nhất trên toàn tổ chức, gắn với access control, handling rules và review định kỳ; nếu không, cùng một loại thông tin có thể bị xử lý khác nhau ở các bộ phận khác nhau.
- **Lưu ý thực tế:** Với thiết bị cá nhân hoặc tài sản không thuộc sở hữu trực tiếp của tổ chức, việc hoàn trả thông tin thường khó hơn hoàn trả tài sản vật lý, nên cần có thêm các biện pháp bù trừ như transfer, deletion verification, access revocation hoặc cryptographic protection.

### D. Deep Summary của Chương 5 (Control 5.11, 5.12)
**Bối cảnh:**
Nhóm control `5.11-5.12` xử lý hai điểm rất căn bản nhưng thường bị xem nhẹ trong vận hành thực tế: một là tài sản và thông tin phải được thu hồi hoặc chuyển giao an toàn khi nhân sự rời đi hoặc thay đổi vai trò, hai là thông tin phải được phân loại đúng để các biện pháp bảo vệ về sau không bị áp dụng quá mức hoặc thiếu mức cần thiết.

**Nội dung cốt lõi:**
- `5.11` yêu cầu tổ chức đưa việc hoàn trả tài sản vào quy trình chính thức khi thay đổi hoặc chấm dứt hợp đồng, bao gồm cả tài sản vật lý, thiết bị điện tử, phương tiện xác thực và các bản sao thông tin mà cá nhân đang nắm giữ.
- `5.11` không chỉ dừng ở việc thu hồi tài sản hữu hình, mà còn nhấn mạnh việc chuyển giao tri thức, ngăn chặn sao chép trái phép trong thời gian notice period và xử lý an toàn dữ liệu nằm trên thiết bị cá nhân hoặc thiết bị không thuộc sở hữu tổ chức.
- `5.12` yêu cầu tổ chức xây dựng topic-specific policy về classification, trong đó thông tin được phân loại dựa trên mức độ ảnh hưởng nếu bị compromise và dựa trên các yêu cầu về confidentiality, integrity, availability cũng như yêu cầu từ bên liên quan.
- `5.12` mở rộng từ nhãn phân loại sang governance của toàn bộ cách xử lý thông tin: classification phải nhất quán toàn tổ chức, được review theo thời gian, gắn với access control và có thể cần cơ chế đối chiếu khi thông tin di chuyển giữa các tổ chức có classification scheme khác nhau.

**Dữ liệu đáng chú ý:**
- `5.11` là kiểm soát `#Preventive`, thiên về bảo vệ tài sản và giảm nguy cơ rò rỉ hoặc thất thoát trong các giai đoạn chuyển đổi nhân sự hoặc hợp đồng.
- `5.12` cũng là kiểm soát `#Preventive`, gắn với `#Identify`, vì classification là điều kiện tiên quyết để tổ chức hiểu thông tin nào cần được bảo vệ ở mức nào.
- `5.12` có liên hệ mạnh với các control về labeling, access control và handling rules, vì phân loại chỉ có ý nghĩa khi kéo theo các biện pháp bảo vệ cụ thể và nhất quán.
- Cặp control này bổ trợ trực tiếp cho governance của information life cycle: một control xử lý đầu ra khi tài sản hoặc con người rời hệ thống, control còn lại định nghĩa mức bảo vệ cần áp dụng trong suốt thời gian tài sản và thông tin còn được sử dụng.

**Rủi ro / Lưu ý:**
- Nếu tài sản và thông tin không được thu hồi hoặc chuyển giao có kiểm soát khi nhân sự rời đi, tổ chức có thể mất dữ liệu, mất tri thức vận hành hoặc để lộ thông tin trên các thiết bị mà mình không còn kiểm soát.
- Nếu classification không rõ hoặc không được dùng thống nhất, cùng một loại thông tin có thể bị chia sẻ quá rộng, bảo vệ quá yếu hoặc ngược lại bị over-classified gây tốn chi phí và làm chậm vận hành.
- Với thiết bị cá nhân hoặc tài sản của bên ngoài, việc bảo đảm xóa bỏ và thu hồi thông tin khó hơn nhiều so với tài sản sở hữu nội bộ, nên cần thêm bằng chứng và kiểm soát kỹ thuật để giảm rủi ro.
- Over-classification và under-classification đều nguy hiểm: một bên làm tăng chi phí và độ phức tạp không cần thiết, bên còn lại khiến thông tin nhạy cảm không được bảo vệ đúng mức.

### E. Structured Output của Chương 5 (Control 5.11, 5.12)
**Section:** 5.11
**Title:** Return of assets

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Informationsecurity properties | #Confidentiality#Integrity#Availability |
| Cybersecurityconcepts | #Protect |
| Operationalcapabilities | #Asset_manage-ment |
| Security domains | #Protection |

**Control:**
Personnel and other interested parties as appropriate should return all the organization’s assets in their possession upon change or termination of their employment, contract or agreement.

**Purpose:**
To protect the organization’s assets as part of the process of changing or terminating employment, contract or agreement.

**Guidance:**
The change or termination process should be formalized to include the return of all previously issued physical and electronic assets owned by or entrusted to the organization.
In cases where personnel and other interested parties purchase the organization’s equipment or use their own personal equipment, procedures should be followed to ensure that all relevant information is traced and transferred to the organization and securely deleted from the equipment (see 7.14).
In cases where personnel and other interested parties have knowledge that is important to ongoing operations, that information should be documented and transferred to the organization.
During the notice period and thereafter, the organization should prevent unauthorized copying of relevant information (e.g. intellectual property) by personnel under notice of termination.
The organization should clearly identify and document all information and other associated assets to be returned which can include:
- user endpoint devices;
- portable storage devices;
- specialist equipment;
- authentication hardware (e.g. mechanical keys, physical tokens and smartcards) for information systems, sites and physical archives;
- physical copies of information.

**Other information:**
It can be difficult to return information held on assets which are not owned by the organization. In such cases, it is necessary to restrict the use of information using other information security controls such as access rights management (5.18) or use of cryptography (8.24).

---
**Section:** 5.12
**Title:** Classification of information

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Informationsecurity properties | #Confidentiality#Integrity#Availability |
| Cybersecurityconcepts | #Identify |
| Operationalcapabilities | #Information_pro-tection |
| Security domains | #Protection#Defence |

**Control:**
Information should be classified according to the information security needs of the organization based on confidentiality, integrity, availability and relevant interested party requirements.

**Purpose:**
To ensure identification and understanding of protection needs of information in accordance with its importance to the organization.

**Guidance:**
The organization should establish a topic-specific policy on information classification and communicate it to all relevant interested parties.
The organization should take into account requirements for confidentiality, integrity and availability in the classification scheme.
Classifications and associated protective controls for information should take account of business needs for sharing or restricting information, for protecting integrity of information and for assuring availability, as well as legal requirements concerning the confidentiality, integrity or availability of the information. Assets other than information can also be classified in compliance with classification of information, which is stored in, processed by or otherwise handled or protected by the asset.
Owners of information should be accountable for their classification.
The classification scheme should include conventions for classification and criteria for review of the classification over time. Results of classification should be updated in accordance with changes of the value, sensitivity and criticality of information through their life cycle.
The scheme should be aligned to the topic-specific policy on access control (see 5.1) and should be able to address specific business needs of the organization.
The classification can be determined by the level of impact that the information's compromise would have for the organization. Each level defined in the scheme should be given a name that makes sense in the context of the classification scheme’s application.
The scheme should be consistent across the whole organization and included in its procedures so that everyone classifies information and applicable other associated assets in the same way. In this manner, everyone has a common understanding of protection requirements and applies appropriate protection.
The classification scheme used within the organization can be different from the schemes used by other organizations, even if the names for levels are similar. In addition, information moving between organizations can vary in classification depending on its context in each organization, even if their classification schemes are identical. Therefore, agreements with other organizations that include information sharing should include procedures to identify the classification of that information and to interpret the classification levels from other organizations. Correspondence between different schemes can be determined by looking for equivalence in the associated handling and protection methods.
**Other information:**
Classification provides people who deal with information with a concise indication of how to handle and protect it. Creating groups of information with similar protection needs and specifying information security procedures that apply to all the information in each group facilitates this. This approach reduces the need for case-by-case risk assessment and custom design of controls.
Information can cease to be sensitive or critical after a certain period of time. For example, when the information has been made public, it no longer has confidentiality requirements but can still require protection for its integrity and availability properties. These aspects should be taken into account, as over-classification can lead to the implementation of unnecessary controls resulting in additional expense or, on the contrary, under-classification can lead to insufficient controls to protect the information from compromise.
As an example, an information confidentiality classification scheme can be based on four levels as follows:
- disclosure causes no harm;
- disclosure causes minor reputational damage or minor operational impact;
- disclosure has a significant short-term impact on operations or business objectives;
- disclosure has a serious impact on long term business objectives or puts the survival of the organization at risk.