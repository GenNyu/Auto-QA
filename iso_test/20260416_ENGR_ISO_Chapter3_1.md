### A. Tài liệu gốc của Chương 3 (Mục 3.1)

### B. Summary Overview của Chương 3 (Mục 3.1)
Tài liệu này mô tả chi tiết **mục 3.1 (Terms and definitions)** trong **Chương 3 (Terms, definitions and abbreviated terms)** của **ISO/IEC 27002:2022**, tập trung vào việc **xây dựng hệ thống ngôn ngữ quản trị và kỹ thuật thống nhất cho an toàn thông tin**.
Mục tiêu là **loại bỏ sự mơ hồ trong cách hiểu các khái niệm, đảm bảo mọi bên liên quan (từ vận hành đến audit) có cùng một hệ quy chiếu khi triển khai và đánh giá các biện pháp kiểm soát**.
Gồm **38** định nghĩa cốt lõi, chia thành các nhóm chính:
- **Nhóm Tài sản và Rủi ro:** Định nghĩa về tài sản (Asset), mối đe dọa (Threat), lỗ hổng (Vulnerability) và tấn công (Attack).
- **Nhóm Vận hành và Sự cố:** Phân cấp rõ rệt giữa sự kiện (Event), vi phạm (Breach) và sự cố (Incident).
- **Nhóm Quản trị và Tuân thủ:** Định nghĩa về chính sách (Policy), quy trình (Procedure), bằng chứng (Record) và kiểm soát (Control).

Áp dụng cho **tất cả cán bộ tham gia vào hệ thống ISMS, đội ngũ pháp chế và kiểm toán viên để làm căn cứ định danh sai phạm và hiệu quả kiểm soát**.

### C. Key Points của Chương 3 (Mục 3.1)
- **Phân loại tài sản đa tầng:** Tài sản không chỉ là thiết bị vật lý mà bao gồm tài sản sơ cấp (quy trình kinh doanh, thông tin) và tài sản hỗ trợ (nhân sự, hạ tầng, phần mềm).
- **Bản chất thực thi của Control:** Một biện pháp chỉ được coi là "kiểm soát" nếu nó thực sự **duy trì hoặc thay đổi được mức độ rủi ro**, không đơn thuần là sự tồn tại của một công cụ.
- **Chuỗi bằng chứng (Chain of custody):** Yêu cầu bắt buộc về khả năng chứng minh quá trình sở hữu, di chuyển và lưu trữ tài liệu/vật chứng để phục vụ mục đích pháp lý và điều tra.
- **Chỉ số hồi phục định lượng:** Việc áp dụng RTO (thời gian hồi phục tối đa) và RPO (mức độ mất dữ liệu tối đa) là yêu cầu tiên quyết để đo lường tính sẵn sàng sau gián đoạn.
- **Mở rộng phạm vi nhân sự:** Định nghĩa "Personnel" bao gồm cả nhân viên tạm thời, nhà thầu và tình nguyện viên, buộc các kiểm soát về con người phải bao phủ toàn bộ nhóm này thay vì chỉ nhân viên chính thức.
- **Phân định trách nhiệm PII:** Phải phân biệt rõ PII Principal (chủ thể dữ liệu), Controller (bên kiểm soát) và Processor (bên xử lý) để áp dụng đúng các nghĩa vụ pháp lý về quyền riêng tư.

### D. Deep Summary của Chương 3 (Mục 3.1)
**Bối cảnh:**
Chương 3.1 cung cấp "nền tảng ngôn ngữ" cho toàn bộ tiêu chuẩn. Nếu không thống nhất được các định nghĩa này, tổ chức sẽ gặp rủi ro "ông nói gà bà nói vịt" khi triển khai các chương 5-8, dẫn đến việc xây dựng các biện pháp kiểm soát sai lệch so với mục đích (intent) ban đầu của tiêu chuẩn.

**Nội dung cốt lõi:**
Trọng tâm là thiết lập mối liên kết logic giữa các thành phần rủi ro: **Mối đe dọa (Threat)** khai thác **Lỗ hổng (Vulnerability)** của **Tài sản (Asset)** hoặc **Biện pháp kiểm soát (Control)** để gây ra **Sự cố (Incident)**. Điểm đáng chú ý là sự phân biệt giữa "Sự kiện" (có khả năng gây hại) và "Sự cố" (đã gây hại thực tế), giúp tổ chức ưu tiên nguồn lực phản ứng phù hợp.

**Dữ liệu đáng chú ý:**
- **Mô hình tài sản 2 lớp:** Tài sản sơ cấp (Thông tin, Quy trình) là mục tiêu bảo vệ; Tài sản hỗ trợ (Phần cứng, Nhân sự, Site) là phương tiện thực thi.
- **Hệ thống phân cấp văn bản:** Policy (ý định chiến lược) -> Rule (nguyên tắc bắt buộc) -> Procedure (cách thức thực hiện).
- **Tính xác thực (Authenticity) và Không thể phủ nhận (Non-repudiation):** Hai thuộc tính then chốt để đảm bảo tính pháp lý của các giao dịch và hoạt động hệ thống.

**Rủi ro / Lưu ý:**
- **Rủi ro thất bại Audit:** Nếu tổ chức định nghĩa sai "Control" (ví dụ: coi một phần mềm là control mà không có quy trình vận hành đi kèm), kiểm toán viên có thể đánh giá là "không tuân thủ" do biện pháp đó không có khả năng thay đổi rủi ro.
- **Lỗ hổng quản trị nhân sự:** Việc hiểu sai định nghĩa "User" hoặc "Personnel" dẫn đến việc bỏ sót các đối tác bên ngoài trong các quy trình cấp phát quyền truy cập hoặc đào tạo nhận thức.
- **Impact nếu fail:** Hiểu sai các thuật ngữ về hồi phục (RTO/RPO) sẽ dẫn đến việc thiết lập phương án dự phòng không đáp ứng được mục tiêu kinh doanh, gây thiệt hại nghiêm trọng khi có gián đoạn thực tế.

### E. Structured Output của Chương 3 (Mục 3.1)
**Purpose:**
For the purposes of this document, the following terms and definitions apply.

ISO and IEC maintain terminology databases for use in standardization at the following addresses:
- ISO Online browsing platform: available at https://www.iso.org/obp
- IEC Electropedia: available at https://www.electropedia.org/

---
**Section:** 3.1.1
**Title:** access control

**Definition:**
means to ensure that physical and logical access to assets (3.1.2) is authorized and restricted based on business and information security requirements

---
**Section:** 3.1.2
**Title:** asset

**Definition:**
anything that has value to the organization

**Note 1 to entry:**
In the context of information security, two kinds of assets can be distinguished:
- the primary assets:
  - information;
  - business processes (3.1.27) and activities;
- the supporting assets (on which the primary assets rely) of all types, for example:
  - hardware;
  - software;
  - network;
  - personnel (3.1.20);
- site;
- organization’s structure.

---
**Section:** 3.1.3
**Title:** attack

**Definition:**
successful or unsuccessful unauthorized attempt to destroy, alter, disable, gain access to an asset (3.1.2) or any attempt to expose, steal, or make unauthorized use of an asset (3.1.2)

---
**Section:** 3.1.4
**Title:** authentication

**Definition:**
provision of assurance that a claimed characteristic of an entity (3.1.11) is correct

---
**Section:** 3.1.5
**Title:** authenticity

**Definition:**
property that an entity (3.1.11) is what it claims to be

---
**Section:** 3.1.6
**Title:** chain of custody

**Definition:**
demonstrable possession, movement, handling and location of material from one point in time until another

**Note 1 to entry:**
Material includes information and other associated assets (3.1.2) in the context of ISO/IEC 27002.

**Source:**
ISO/IEC 27050-1:2019, 3.1, modified - "Note 1 to entry" added

---
**Section:** 3.1.7
**Title:** confidential information

**Definition:**
information that is not intended to be made available or disclosed to unauthorized individuals, entities (3.1.11) or processes (3.1.27)

---
**Section:** 3.1.8
**Title:** control

**Definition:**
measure that maintains and/or modifies risk

**Note 1 to entry:**
Controls include, but are not limited to, any process (3.1.27), policy (3.1.24), device, practice or other conditions and/or actions which maintain and/or modify risk.

**Note 2 to entry:**
Controls may not always exert the intended or assumed modifying effect.

**Source:**
ISO 31000:2018, 3.8

---
**Section:** 3.1.9
**Title:** disruption

**Definition:**
incident, whether anticipated or unanticipated, that causes an unplanned, negative deviation from the expected delivery of products and services according to an organization’s objectives

**Source:**
ISO 22301:2019, 3.10

---
**Section:** 3.1.10
**Title:** endpoint device

**Definition:**
network connected information and communication technology (ICT) hardware device

**Note 1 to entry:**
Endpoint device can refer to desktop computers, laptops, smart phones, tablets, thin clients, printers or other specialized hardware including smart meters and Internet of things (IoT) devices.

---
**Section:** 3.1.11
**Title:** entity

**Definition:**
item relevant for the purpose of operation of a domain that has recognizably distinct existence

**Note 1 to entry:**
An entity can have a physical or a logical embodiment.

**Example:**
A person, an organization, a device, a group of such items, a human subscriber to a telecom service, a SIM card, a passport, a network interface card, a software application, a service or a website.

**Source:**
ISO/IEC 24760-1:2019, 3.1.1

---
**Section:** 3.1.12
**Title:** information processing facility

**Definition:**
any information processing system, service or infrastructure, or the physical location housing it

**Source:**
ISO/IEC 27000:2018, 3.27, modified - "facilities" has been replaced with facility.

---
**Section:** 3.1.13
**Title:** information security breach

**Definition:**
compromise of information security that leads to the undesired destruction, loss, alteration, disclosure of, or access to, protected information transmitted, stored or otherwise processed

---
**Section:** 3.1.14
**Title:** information security event

**Definition:**
occurrence indicating a possible information security breach (3.1.13) or failure of controls (3.1.8)

**Source:**
ISO/IEC 27035-1:2016, 3.3, modified - "breach of information security" has been replaced with "information security breach"

---
**Section:** 3.1.15
**Title:** information security incident

**Definition:**
one or multiple related and identified information security events (3.1.14) that can harm an organization’s assets (3.1.2) or compromise its operations

**Source:**
ISO/IEC 27035-1:2016, 3.4

---
**Section:** 3.1.16
**Title:** information security incident management

**Definition:**
exercise of a consistent and effective approach to the handling of information security incidents (3.1.15)

**Source:**
ISO/IEC 27035-1:2016, 3.5

---
**Section:** 3.1.17
**Title:** information system

**Definition:**
set of applications, services, information technology assets (3.1.2), or other information-handling components

**Source:**
ISO/IEC 27000:2018, 3.35

---
**Section:** 3.1.18
**Title:** stakeholder

**Definition:**
person or organization that can affect, be affected by, or perceive itself to be affected by a decision or activity

**Source:**
ISO/IEC 27000:2018, 3.37

---
**Section:** 3.1.19
**Title:** non-repudiation

**Definition:**
ability to prove the occurrence of a claimed event or action and its originating entities (3.1.11)

---
**Section:** 3.1.20
**Title:** personnel

**Definition:**
persons doing work under the organization’s direction

**Note 1 to entry:**
The concept of personnel includes the organization’s members, such as the governing body, top management, employees, temporary staff, contractors and volunteers.

---
**Section:** 3.1.21
**Title:** personally identifiable information
**Abbreviation:** PII

**Definition:**
any information that (a) can be used to establish a link between the information and the natural person to whom such information relates, or (b) is or can be directly or indirectly linked to a natural person.

**Note 1 to entry:**
The “natural person” in the definition is the PII principal (3.1.22). To determine whether a PII principal is identifiable, account should be taken of all the means which can reasonably be used by the privacy stakeholder holding the data, or by any other party, to establish the link between the set of PII and the natural person.

**Source:**
ISO/IEC 29100:2011/Amd.1:2018, 2.9

---
**Section:** 3.1.22
**Title:** PII principal

**Definition:**
natural person to whom the personally identifiable information (PII) (3.1.21) relates

**Note 1 to entry:**
Depending on the jurisdiction and the particular data protection and privacy legislation, the synonym “data subject” can also be used instead of the term “PII principal”.

**Source:**
ISO/IEC 29100:2011, 2.11

---
**Section:** 3.1.23
**Title:** PII processor

**Definition:**
privacy stakeholder that processes personally identifiable information (PII) (3.1.21) on behalf of and in accordance with the instructions of a PII controller

**Source:**
ISO/IEC 29100:2011, 2.12

---
**Section:** 3.1.24
**Title:** policy

**Definition:**
intentions and direction of an organization, as formally expressed by its top management

**Source:**
ISO/IEC 27000:2018, 3.53

---
**Section:** 3.1.25
**Title:** privacy impact assessment
**Abbreviation:** PIA

**Definition:**
overall process (3.1.27) of identifying, analysing, evaluating, consulting, communicating and planning the treatment of potential privacy impacts with regard to the processing of personally identifiable information (PII) (3.1.21), framed within an organization’s broader risk management framework

**Source:**
ISO/IEC 29134:2017, 3.7, modified - Note 1 to entry removed.

---
**Section:** 3.1.26
**Title:** procedure

**Definition:**
specified way to carry out an activity or a process (3.1.27)

**Source:**
ISO 30000:2009, 3.12

---
**Section:** 3.1.27
**Title:** process

**Definition:**
set of interrelated or interacting activities that uses or transforms inputs to deliver a result

**Source:**
ISO 9000:2015, 3.4.1, modified - Notes to entry removed.

---
**Section:** 3.1.28
**Title:** record

**Definition:**
information created, received and maintained as evidence and as an asset (3.1.2) by an organization or person, in pursuit of legal obligations or in the transaction of business

**Note 1 to entry:**
Legal obligations in this context include all legal, statutory, regulatory and contractual requirements.

**Source:**
ISO 15489-1:2016, 3.14, modified - "Note 1 to entry" added.

---
**Section:** 3.1.29
**Title:** recovery point objective
**Abbreviation:** RPO

**Definition:**
point in time to which data are to be recovered after a disruption (3.1.9) has occurred

**Source:**
ISO/IEC 27031:2011, 3.12, modified - "must" replaced by "are to be".

---
**Section:** 3.1.30
**Title:** recovery time objective
**Abbreviation:** RTO

**Definition:**
period of time within which minimum levels of services and/or products and the supporting systems, applications, or functions are to be recovered after a disruption (3.1.9) has occurred

**Source:**
ISO/IEC 27031:2011, 3.13, modified - "must" replaced by "are to be".

---
**Section:** 3.1.31
**Title:** reliability

**Definition:**
property of consistent intended behaviour and results

---
**Section:** 3.1.32
**Title:** rule

**Definition:**
accepted principle or instruction that states the organization’s expectations on what is required to be done, what is allowed or not allowed

**Note 1 to entry:**
Rules can be formally expressed in topic-specific policies (3.1.35) and in other types of documents.

---
**Section:** 3.1.33
**Title:** sensitive information

**Definition:**
information that needs to be protected from unavailability, unauthorized access, modification or public disclosure because of potential adverse effects on an individual, organization, national security or public safety

---
**Section:** 3.1.34
**Title:** threat

**Definition:**
potential cause of an unwanted incident, which can result in harm to a system or organization

**Source:**
ISO/IEC 27000:2018, 3.74

---
**Section:** 3.1.35
**Title:** topic-specific policy

**Definition:**
intentions and direction on a specific subject or topic, as formally expressed by the appropriate level of management

**Note 1 to entry:**
Topic-specific policies can formally express rules (3.1.32) or organization standards.

**Note 2 to entry:**
Some organizations use other terms for these topic-specific policies.

**Note 3 to entry:**
The topic-specific policies referred to in this document are related to information security.

**Example:**
Topic-specific policy on access control (3.1.1), topic-specific policy on clear desk and clear screen.

---
**Section:** 3.1.36
**Title:** user

**Definition:**
interested party (3.1.18) with access to the organization’s information systems (3.1.17)

**Example:**
Personnel (3.1.20), customers, suppliers.

---
**Section:** 3.1.37
**Title:** user endpoint device

**Definition:**
endpoint device (3.1.10) used by users to access information processing services

**Note 1 to entry:**
User endpoint device can refer to desktop computers, laptops, smart phones, tablets, thin clients, etc.

---
**Section:** 3.1.38
**Title:** vulnerability

**Definition:**
weakness of an asset (3.1.2) or control (3.1.8) that can be exploited by one or more threats (3.1.34)

**Source:**
ISO/IEC 27000:2018, 3.77