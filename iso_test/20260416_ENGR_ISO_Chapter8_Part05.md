### A. Tài liệu gốc của Chương 8 (Control 8.8)

### B. Summary Overview của Chương 8 (Control 8.8)
Tài liệu này mô tả chi tiết **mục 8.8** trong **chương 8. Technological controls** của **ISO/IEC 27002:2022**, tập trung vào việc phát hiện, đánh giá và xử lý lỗ hổng kỹ thuật trên các hệ thống và phần mềm đang sử dụng.
Mục tiêu là **ngăn khai thác lỗ hổng trước khi chúng bị lợi dụng, đồng thời bảo đảm tổ chức có quy trình cập nhật, kiểm thử, khắc phục và theo dõi lỗ hổng một cách có kiểm soát**.
Gồm 1 mục chính:
- `8.8`: Management of technical vulnerabilities - quản lý lỗ hổng kỹ thuật từ phát hiện đến khắc phục

Áp dụng cho hệ thống thông tin, phần mềm, dịch vụ, thành phần bên thứ ba, hạ tầng cloud và các tài sản công nghệ cần được theo dõi, đánh giá lỗ hổng và vá lỗi theo vòng đời vận hành.

### C. Key Points của Chương 8 (Control 8.8)
- **Mục tiêu quản trị:** `8.8` bảo đảm tổ chức không chỉ biết lỗ hổng tồn tại, mà còn có quy trình đánh giá rủi ro, ưu tiên khắc phục và theo dõi hiệu quả xử lý.
- **Yêu cầu chính:** Tổ chức phải có inventory chính xác, nguồn thông tin về lỗ hổng, quy trình đánh giá, lịch phản ứng, thử nghiệm bản vá, cơ chế khắc phục và phương án thay thế khi chưa thể vá ngay.
- **Vulnerability disclosure:** Tổ chức nên có đầu mối công khai để nhận báo cáo lỗ hổng, quy trình xử lý báo cáo, và cơ chế phối hợp với vendor, threat intelligence hoặc bug bounty nếu phù hợp.
- **Điểm vận hành quan trọng:** Việc vá lỗi phải gắn với change management hoặc incident response tùy mức độ khẩn cấp; đồng thời cần kiểm tra update từ nguồn hợp pháp trước khi triển khai rộng.
- **Lưu ý thực tế:** Với cloud, trách nhiệm lỗ hổng có thể chia giữa provider và customer; vì vậy hợp đồng dịch vụ cần ghi rõ ai chịu trách nhiệm phần nào của tài sản và dịch vụ.

### D. Deep Summary của Chương 8 (Control 8.8)
**Bối cảnh:**
Đây là control cốt lõi của phòng thủ công nghệ hiện đại, vì phần lớn sự cố bắt đầu từ một lỗ hổng chưa được nhận diện, đánh giá sai hoặc vá chậm. Quản lý technical vulnerabilities không chỉ là quét lỗ hổng, mà là chuỗi hoạt động từ inventory, theo dõi, xác minh, ưu tiên xử lý, triển khai khắc phục, đến học hỏi và cập nhật thông tin cho các bên liên quan.

**Nội dung cốt lõi:**
- `8.8` yêu cầu tổ chức có inventory tài sản đủ chính xác để biết phần mềm nào đang chạy ở đâu, do ai chịu trách nhiệm và phụ thuộc vào vendor nào.
- `8.8` đòi hỏi xác định nguồn thông tin về lỗ hổng, theo dõi báo cáo từ vendor, cộng đồng, threat intelligence và các kênh tiếp nhận disclosure.
- `8.8` yêu cầu phân tích lỗ hổng để xác định rủi ro và hành động tương ứng, từ vá lỗi, áp dụng workaround đến tắt dịch vụ hoặc tăng kiểm soát biên mạng.
- `8.8` nhấn mạnh việc kiểm thử bản vá, kiểm tra tính xác thực của remediation và ghi log toàn bộ các bước để phục vụ audit và điều tra sau này.
- `8.8` cũng mở rộng sang cloud và thành phần bên thứ ba, nơi trách nhiệm vá lỗi có thể phân tách giữa nhà cung cấp và khách hàng sử dụng dịch vụ.

**Dữ liệu đáng chú ý:**
- `8.8` là kiểm soát `#Preventive`, gắn với `#Confidentiality`, `#Integrity`, `#Availability`, thuộc `#Threat_and_vulnerability_management` và miền `#Governance_and_Ecosystem #Protection #Defence`.
- Control này bao phủ cả phát hiện lỗ hổng nội bộ lẫn tiếp nhận báo cáo từ bên ngoài.
- `8.8` có tham chiếu đến `8.19`, `8.32`, `5.20`, `5.23`, `5.26`, `8.13`, `8.20` đến `8.22`, `ISO/IEC 29147`, `ISO/IEC 30111`, `ISO/IEC 27017`, `ISO/IEC 19086`, `ISO/IEC 27031`.
- `8.8` coi vulnerability scanning chỉ là một phần của quá trình, không phải toàn bộ giải pháp.
- `8.8` nhấn mạnh rằng một số môi trường, như industrial control systems, có thể cần cách tiếp cận khác do hạn chế cập nhật hoặc kiểm thử.

**Rủi ro / Lưu ý:**
- Nếu inventory không chính xác, tổ chức có thể bỏ sót hệ thống còn lỗ hổng hoặc vá nhầm đối tượng không còn dùng.
- Nếu chỉ quét lỗ hổng mà không có quy trình đánh giá và khắc phục, báo cáo sẽ tăng nhưng rủi ro thực tế không giảm.
- Nếu patch được triển khai mà không kiểm thử, có thể gây side effect, gián đoạn dịch vụ hoặc tạo lỗi mới.
- Nếu trách nhiệm cloud/provider/customer không được ghi rõ, lỗ hổng có thể bị bỏ trống vì mỗi bên nghĩ bên kia sẽ xử lý.

### E. Structured Output của Chương 8 (Control 8.8)
**Section:** 8.8
**Title:** Management of technical vulnerabilities

**Attributes:**
| Field | Value |
| --- | --- |
| Control type | #Preventive |
| Information security properties | #Confidentiality #Integrity #Availability |
| Cybersecurity concepts | #Identify #Protect |
| Operational capabilities | #Threat_and_vulnerability_management |
| Security domains | #Governance_and_Ecosystem #Protection #Defence |

**Control:**
Information about technical vulnerabilities of information systems in use should be obtained, the organization’s exposure to such vulnerabilities should be evaluated and appropriate measures should be taken.

**Purpose:**
To prevent exploitation of technical vulnerabilities.

**Guidance:**
***Identifying technical vulnerabilities***
The organization should have an accurate inventory of assets (see 5.9 to 5.14) as a prerequisite for effective technical vulnerability management; the inventory should include the software vendor, software name, version numbers, current state of deployment (e.g. what software is installed on what systems) and the person(s) within the organization responsible for the software.

To identify technical vulnerabilities, the organization should consider:
- defining and establishing the roles and responsibilities associated with technical vulnerability management, including vulnerability monitoring, vulnerability risk assessment, updating, asset tracking and any coordination responsibilities required;
- for software and other technologies (based on the asset inventory list, see 5.9), identifying information resources that will be used for identifying relevant technical vulnerabilities and maintaining awareness about them. Updating the list of information resources based on changes in the inventory or when other new or useful resources are found;
- requiring suppliers of information system (including their components) to ensure vulnerability reporting, handling and disclosure, including the requirements in applicable contracts (see 5.20);
- using vulnerability scanning tools suitable for the technologies in use to identify vulnerabilities and to verify whether the patching of vulnerabilities was successful;
- conducting planned, documented and repeatable penetration tests or vulnerability assessments by competent and authorized persons to support the identification of vulnerabilities. Exercising caution as such activities can lead to a compromise of the security of the system;
- tracking the usage of third-party libraries and source code for vulnerabilities. This should be included in secure coding (see 8.28).

The organization should develop procedures and capabilities to:
- detect the existence of vulnerabilities in its products and services including any external component used in these;
- receive vulnerability reports from internal or external sources.

The organization should provide a public point of contact as part of a topic-specific policy on vulnerability disclosure so that researchers and others are able to report issues. The organization should establish vulnerability reporting procedures, online reporting forms and making use of appropriate threat intelligence or information sharing forums. The organization should also consider bug bounty programs where rewards are offered as an incentive to assist organizations in identifying vulnerabilities in order to appropriately remediate them. The organization should also share information with competent industry bodies or other interested parties.

***Evaluating technical vulnerabilities***
To evaluate identified technical vulnerabilities, the following guidance should be considered:
- analyse and verify reports to determine what response and remediation activity is needed;
- once a potential technical vulnerability has been identified, identifying the associated risks and the actions to be taken. Such actions can involve updating vulnerable systems or applying other controls.

***Taking appropriate measures to address technical vulnerabilities***
A software update management process should be implemented to ensure the most up-to-date approved patches and application updates are installed for all authorized software. If changes are necessary, the original software should be retained and the changes applied to a designated copy. All changes should be fully tested and documented, so that they can be reapplied, if necessary, to future software upgrades. If required, the modifications should be tested and validated by an independent evaluation body.

The following guidance should be considered to address technical vulnerabilities:
- taking appropriate and timely action in response to the identification of potential technical vulnerabilities; defining a timeline to react to notifications of potentially relevant technical vulnerabilities;
- depending on how urgently a technical vulnerability needs to be addressed, carrying out the action according to the controls related to change management (see 8.32) or by following information security incident response procedures (see 5.26);
- only using updates from legitimate sources (which can be internal or external to the organization);
- testing and evaluating updates before they are installed to ensure they are effective and do not result in side effects that cannot be tolerated [i.e. if an update is available, assessing the risks associated with installing the update (the risks posed by the vulnerability should be compared with the risk of installing the update)];
- addressing systems at high risk first;
- develop remediation (typically software updates or patches);
- test to confirm if the remediation or mitigation is effective;
- provide mechanisms to verify the authenticity of remediation;
- if no update is available or the update cannot be installed, considering other controls, such as:
  1. applying any workaround suggested by the software vendor or other relevant sources;
  2. turning off services or capabilities related to the vulnerability;
  3. adapting or adding access controls (e.g. firewalls) at network borders (see 8.20 to 8.22);
  4. shielding vulnerable systems, devices or applications from attack through deployment of suitable traffic filters (sometimes called virtual patching);
  5. increasing monitoring to detect actual attacks;
  6. raising awareness of the vulnerability.

For acquired software, if the vendors regularly release information about security updates for their software and provide a facility to install such updates automatically, the organization should decide whether to use the automatic update or not.

***Other considerations***
An audit log should be kept for all steps undertaken in technical vulnerability management.

The technical vulnerability management process should be regularly monitored and evaluated in order to ensure its effectiveness and efficiency.

An effective technical vulnerability management process should be aligned with incident management activities, to communicate data on vulnerabilities to the incident response function and provide technical procedures to be carried out in case an incident occurs.

Where the organization uses a cloud service supplied by a third-party cloud service provider, technical vulnerability management of cloud service provider resources should be ensured by the cloud service provider. The cloud service provider’s responsibilities for technical vulnerability management should be part of the cloud service agreement and this should include processes for reporting the cloud service provider's actions relating to technical vulnerabilities (see 5.23). For some cloud services, there are respective responsibilities for the cloud service provider and the cloud service customer. For example, the cloud service customer is responsible for vulnerability management of its own assets used for the cloud services.

**Other information:**
Technical vulnerability management can be viewed as a sub-function of change management and as such can take advantage of the change management processes and procedures (see 8.32).

There is a possibility that an update does not address the problem adequately and has negative side effects. Also, in some cases, uninstalling an update cannot be easily achieved once the update has been applied.

If adequate testing of the updates is not possible (e.g. because of costs or lack of resources) a delay in updating can be considered to evaluate the associated risks, based on the experience reported by other users. The use of ISO/IEC 27031 can be beneficial.

Where software patches or updates are produced, the organization can consider providing an automated update process where these updates are installed on affected systems or products without the need for intervention by the customer or the user. If an automated update process is offered, it can allow the customer or user to choose an option to turn off the automatic update or control the timing of the installation of the update.

Where the vendor provides an automated update process and the updates can be installed on affected systems or products without the need for intervention, the organization determines if it applies the automated process or not. One reason for not electing for automated update is to retain control over when the update is performed. For example, a software used for a business operation cannot be updated until the operation has completed.

A weakness with vulnerability scanning is that it is possible it does not fully account for defence in depth: two countermeasures that are always invoked in sequence can have vulnerabilities that are masked by strengths in the other. The composite countermeasure is not vulnerable, whereas a vulnerability scanner can report that both components are vulnerable. The organization should therefore take care in reviewing and acting on vulnerability reports.

Many organizations supply software, systems, products and services not only within the organization but also to interested parties such as customers, partners or other users. These software, systems, products and services can have information security vulnerabilities that affect the security of users.

Organizations can release remediation and disclose information about vulnerabilities to users (typically through a public advisory) and provide appropriate information for software vulnerability database services.

For more information relating to the management of technical vulnerabilities when using cloud computing, see the ISO/IEC 19086 series and ISO/IEC 27017.

ISO/IEC 29147 provides detailed information on receiving vulnerability reports and publishing vulnerability advisories. ISO/IEC 30111 provides detailed information about handling and resolving reported vulnerabilities.