### A. Tài liệu gốc của Chương 5 (Control 5.13, 5.14)

### B. Summary Overview của Chương 5 (Control 5.13, 5.14)
Tài liệu này mô tả chi tiết **mục 5.13 và 5.14** trong **chương 5. Organizational controls** của **ISO/IEC 27002:2022**, tập trung vào việc gắn nhãn thông tin theo sơ đồ phân loại của tổ chức và kiểm soát cách thông tin được truyền tải trong nội bộ cũng như ra bên ngoài.
Mục tiêu chung của nhóm nội dung này là **làm cho thông tin dễ nhận diện, dễ xử lý và được bảo vệ nhất quán trong quá trình di chuyển**, từ nhãn phân loại đến các quy tắc, thủ tục và thỏa thuận cho transfer giữa các bên liên quan.
Gồm 2 mục chính:
- `5.13`: Labelling of information - thiết lập thủ tục gắn nhãn phù hợp với classification scheme của tổ chức
- `5.14`: Information transfer - thiết lập quy tắc, thủ tục và thỏa thuận để bảo vệ thông tin trong quá trình chuyển giao

Áp dụng cho các bộ phận an toàn thông tin, vận hành hệ thống, quản trị tài liệu, người dùng nội bộ và các bên liên quan tham gia tạo, chia sẻ, lưu trữ hoặc chuyển thông tin.

### C. Key Points của Chương 5 (Control 5.13, 5.14)
- **Mục tiêu quản trị:** Nhóm control này giúp tổ chức bảo đảm người dùng và hệ thống nhận biết đúng mức phân loại của thông tin, từ đó áp dụng cách xử lý, bảo vệ và chuyển giao phù hợp với từng mức nhạy cảm.
- **Yêu cầu chính của 5.13:** Tổ chức phải xây dựng và áp dụng thủ tục gắn nhãn phù hợp với classification scheme, bảo đảm nhãn rõ ràng, nhất quán và có thể hỗ trợ cả xử lý thủ công lẫn tự động.
- **Yêu cầu chính của 5.14:** Tổ chức cần có rules, procedures hoặc agreements cho tất cả các hình thức transfer để bảo vệ thông tin trong nội bộ và khi trao đổi với bên ngoài, bao gồm cả điện tử, vật lý và bằng lời nói.
- **Điểm vận hành quan trọng:** Gắn nhãn chỉ có giá trị khi được kết nối với transfer control, access control và handling rules; nếu không, cùng một thông tin có thể bị chuyển đi đúng quy trình nhưng vẫn bị hiểu sai hoặc bảo vệ sai trong khâu tiếp nhận.
- **Lưu ý thực tế:** Khi thông tin di chuyển giữa các tổ chức có classification scheme khác nhau, cần cơ chế đối chiếu và thỏa thuận rõ để tránh hiểu sai mức bảo vệ hoặc yêu cầu xử lý tương ứng.

### D. Deep Summary của Chương 5 (Control 5.13, 5.14)
**Bối cảnh:**
Nhóm control `5.13-5.14` xử lý hai điểm kết nối trực tiếp với nhau trong vòng đời thông tin: một là làm sao để thông tin mang theo dấu hiệu nhận diện đúng mức bảo vệ của nó, hai là làm sao để thông tin được truyền đi qua các kênh nội bộ hoặc bên ngoài mà vẫn giữ nguyên mức bảo vệ đó. Nếu thiếu nhãn và quy tắc transfer, classification sẽ khó được thực thi nhất quán.

**Nội dung cốt lõi:**
- `5.13` yêu cầu tổ chức ban hành thủ tục gắn nhãn cho mọi định dạng thông tin và tài sản liên quan, bảo đảm nhãn phản ánh đúng classification, dễ nhận biết và có thể hỗ trợ xử lý tự động trong hệ thống.
- `5.13` không chỉ là gắn nhãn thủ công, mà còn bao gồm metadata, watermark, headers, footers hoặc các cơ chế kỹ thuật khác để giúp hệ thống và người dùng xử lý thông tin đúng cách theo sơ đồ phân loại.
- `5.14` yêu cầu tổ chức xây dựng rules, procedures và agreements cho mọi loại transfer, bao gồm kiểm soát chống truy cập trái phép, sai địa chỉ, sửa đổi, thất lạc, phủ nhận trách nhiệm và các rủi ro trên đường truyền.
- `5.14` mở rộng từ transfer điện tử sang phương tiện lưu trữ vật lý và verbal transfer, đồng thời yêu cầu xử lý cả trách nhiệm, liên hệ, lưu vết, chain of custody và điều kiện pháp lý liên quan.

**Dữ liệu đáng chú ý:**
- `5.13` là kiểm soát `#Preventive`, gắn với `#Protect`, vì nhãn là cách để tổ chức truyền đạt yêu cầu xử lý và bảo vệ cho người dùng lẫn hệ thống.
- `5.13` có liên hệ chặt với `5.12`, vì nhãn chỉ có ý nghĩa khi bám theo classification scheme đã được xác định trước.
- `5.14` là kiểm soát `#Preventive`, gắn với `#Protect`, vì mục tiêu chính là giữ an toàn cho thông tin trong quá trình di chuyển giữa các điểm xử lý.
- `5.14` tác động tới nhiều miền như asset management, information protection và protection, do nó bao phủ cả transfer nội bộ, transfer ra ngoài và các kênh truyền khác nhau.

**Rủi ro / Lưu ý:**
- Nếu gắn nhãn không nhất quán, người dùng và hệ thống có thể hiểu sai mức bảo vệ cần áp dụng, dẫn đến chia sẻ quá rộng hoặc kiểm soát quá yếu.
- Nếu transfer rules không bao phủ đủ các hình thức truyền tải, tổ chức có thể bỏ sót rủi ro từ email, file sharing, cloud storage, media vật lý hoặc verbal transfer.
- Khi thông tin đi qua bên thứ ba hoặc đối tác bên ngoài, việc không có thỏa thuận rõ về trách nhiệm, xác thực người nhận và chain of custody sẽ làm tăng nguy cơ thất lạc hoặc tranh chấp.
- Với thông tin nhạy cảm, nhãn và transfer control phải đi kèm với các biện pháp bổ trợ như cryptography, access control, recipient verification và retention/disposal rules.

### E. Structured Output của Chương 5 (Control 5.13, 5.14)
**Section:** 5.13
**Title:** Labelling of information

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Informationsecurity properties | #Confidentiality#Integrity#Availability |
| Cybersecurityconcepts | #Protect |
| Operationalcapabilities | #Information_protection |
| Security domains | #Defence#Protection |

**Control:**
An appropriate set of procedures for information labelling should be developed and implemented in accordance with the information classification scheme adopted by the organization.

**Purpose:**
To facilitate the communication of classification of information and support automation of information processing and management.

**Guidance:**
Procedures for information labelling should cover information and other associated assets in all formats. The labelling should reflect the classification scheme established in 5.12. The labels should be easily recognizable. The procedures should give guidance on where and how labels are attached in consideration of how the information is accessed or the assets are handled depending on the types of storage media. The procedures can define:
- cases where labelling is omitted (e.g. labelling of non-confidential information to reduce workloads);
- how to label information sent by or stored on electronic or physical means, or any other format;
- how to handle cases where labelling is not possible (e.g. due to technical restrictions).

Digital information should utilize metadata in order to identify, manage and control information, especially with regard to confidentiality. Metadata should also enable efficient and correct searching for information. Metadata should facilitate systems to interact and make decisions based on the associated classification labels.
The procedures should describe how to attach metadata to information, what labels to use and how data should be handled, in line with the organization’s information model and ICT architecture.
Relevant additional metadata should be added by systems when they process information depending on its information security properties.
Personnel and other interested parties should be made aware of labelling procedures. All personnel should be provided with the necessary training to ensure that information is correctly labelled and handled accordingly.
Output from systems containing information that is classified as being sensitive or critical should carry an appropriate classification label.
***Examples of labelling techniques include:***
- physical labels;
- headers and footers;
- metadata;
- watermarking;
- rubber-stamps.

**Other information:**
Labelling of classified information is a key requirement for information sharing.
Other useful metadata that can be attached to the information is which organizational process created the information and at what time.
Labelling of information and other associated assets can sometimes have negative effects. Classified assets can be easier to identify by malicious actors for potential misuse.
Some systems do not label individual files or database records with their classification but protect all information at the highest level of classification of any of the information that it contains or is permitted to contain. It is usual in such systems to determine and then label information when it is exported.

---
**Section:** 5.14
**Title:** Information transfer

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Informationsecurity properties | #Confidentiality#Integrity#Availability |
| Cybersecurityconcepts | #Protect |
| Operationalcapabilities | #Asset_management#Information_protection |
| Security domains | #Protection |

**Control:**
Information transfer rules, procedures, or agreements should be in place for all types of transfer facilities within the organization and between the organization and other parties.

**Purpose:**
To maintain the security of information transferred within an organization and with any external interested party.

**Guidance:**
***General:***
The organization should establish and communicate a topic-specific policy on information transfer to all relevant interested parties. Rules, procedures and agreements to protect information in transit should reflect the classification of the information involved. Where information is transferred between the organization and third parties, transfer agreements (including recipient authentication) should be established and maintained to protect information in all forms in transit (see 5.10).
Information transfer can happen through electronic transfer, physical storage media transfer and verbal transfer.
For all types of information transfer, rules, procedures and agreements should include:
- controls designed to protect transferred information from interception, unauthorized access, copying, modification, misrouting, destruction and denial of service, including levels of access control commensurate with the classification of the information involved and any special controls that are required to protect sensitive information, such as use of cryptographic techniques (see 8.24);
- controls to ensure traceability and non-repudiation, including maintaining a chain of custody for information while in transit;
- identification of appropriate contacts related to the transfer including information owners, risk owners, security officers and information custodians, as applicable;
- responsibilities and liabilities in the event of information security incidents, such as loss of physical storage media or data;
- use of an agreed labelling system for sensitive or critical information, ensuring that the meaning of the labels is immediately understood and that the information is appropriately protected (see 5.13);
- reliability and availability of the transfer service;
- the topic-specific policy or guidelines on acceptable use of information transfer facilities (see 5.10);
- retention and disposal guidelines for all business records, including messages;

***Note:*** Local legislation and regulations can exist regarding retention and disposal of business records.
- the consideration of any other relevant legal, statutory, regulatory and contractual requirements (see 5.31, 5.32, 5.33, 5.34) related to transfer of information (e.g. requirements for electronic signatures).

***Electronic transfer:***
Rules, procedures and agreements should also consider the following items when using electronic communication facilities for information transfer:
- detection of and protection against malware that can be transmitted through the use of electronic communications (see 8.7);
- protection of communicated sensitive electronic information that is in the form of an attachment;
- prevention against sending documents and messages in communications to the wrong address or number;
- obtaining approval prior to using external public services such as instant messaging, social networking, file sharing or cloud storage;
- stronger levels of authentication when transferring information via publicly accessible networks;
- restrictions associated with electronic communication facilities (e.g. preventing automatic forwarding of electronic mail to external mail addresses);
- advising personnel and other interested parties not to send short message service (SMS) or instant messages with critical information since these can be read in public places (and therefore by unauthorized persons) or stored in devices not adequately protected;
- advising personnel and other interested parties about the problems of using fax machines or services, namely:
    1) unauthorized access to built-in message stores to retrieve messages;
    2) deliberate or accidental programming of machines to send messages to specific numbers.

***Physical storage media transfer:***
When transferring physical storage media (including paper), rules, procedures and agreements should also include:
- responsibilities for controlling and notifying transmission, dispatch and receipt;
- ensuring correct addressing and transportation of the message;
- packaging that protects the contents from any physical damage likely to arise during transit and in accordance with any manufacturers’ specifications, for example protecting against any environmental factors that can reduce the effectiveness of restoring storage media such as exposure to heat, moisture or electromagnetic fields; using minimum technical standards for packaging and transmission (e.g. the use of opaque envelopes);
- a list of authorized reliable couriers agreed by management;
- courier identification standards;
- depending on the classification level of the information in the storage media to be transported, use tamper evident or tamper-resistant controls (e.g. bags, containers);
- procedures to verify the identification of couriers;
- approved list of third parties providing transportation or courier services depending on the classification of the information;
- keeping logs for identifying the content of the storage media, the protection applied as well as recording the list of authorised recipients, the times of transfer to the transit custodians and receipt at the destination.

***Verbal transfer:***
To protect verbal transfer of information, personnel and other interested parties should be reminded that they should:
- not have confidential verbal conversations in public places or over insecure communication channels since these can be overheard by unauthorized persons;
- not leave messages containing confidential information on answering machines or voice messages since these can be replayed by unauthorized persons, stored on communal systems or stored incorrectly as a result of misdialling;
- be screened to the appropriate level to listen to the conversation;
- ensure that appropriate room controls are implemented (e.g. sound-proofing, closed door);
- begin any sensitive conversations with a disclaimer so those present know the classification level and any handling requirements of what they are about to hear.

**Other information:**
No other information.