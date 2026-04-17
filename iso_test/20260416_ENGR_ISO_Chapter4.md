### A. Tài liệu gốc của Chương 4

### B. Summary Overview của Chương 4
Tài liệu này mô tả chi tiết **Chương 4. Structure of this document** của **ISO/IEC 27002:2022**, tập trung vào **cấu trúc tổng thể của tiêu chuẩn**, bao gồm các clause chính, hai annex mang tính thông tin và cơ chế sử dụng theme cùng attribute để phân loại và nhìn nhận các control theo nhiều góc độ khác nhau.
Mục tiêu là **giúp người đọc hiểu rõ cách tổ chức nội dung của tài liệu**, cách các control được phân nhóm, cũng như cách sử dụng attribute để xây dựng các góc nhìn (view) phục vụ tra cứu, phân tích và trình bày trong nội bộ.
Gồm 3 phần chính:
- `4.1`: `Clauses` - mô tả các clause chính và các annex thông tin
- `4.2`: `Themes and attributes` - mô tả theme và hệ attribute của control
- `4.3`: `Control layout` - mô tả bố cục chuẩn của một control

Áp dụng cho toàn bộ tài liệu ISO/IEC 27002:2022 và cho các tổ chức muốn xây dựng view kiểm soát theo nhu cầu của mình.

### C. Key Points của Chương 4
- **Mục tiêu chính:** Chuẩn hóa cách tiếp cận và đọc tài liệu, giúp cùng một bộ control có thể được phân tích theo nhiều góc nhìn khác nhau.
- **Cấu trúc tài liệu:** Bao gồm các clause từ 5 đến 8 (các nhóm control chính) và hai annex mang tính tham chiếu (`Annex A`, `Annex B`).
- **Cơ chế phân loại:** Control được tổ chức theo hai lớp:
  - `Themes`: phản ánh bản chất và phạm vi của control
  - `Attributes`: cho phép lọc, nhóm và trình bày control theo nhu cầu sử dụng
- **Giá trị thực tiễn:** Attribute giúp xây dựng các “view” linh hoạt phục vụ audit, quản trị rủi ro và báo cáo nội bộ.
- **Tính linh hoạt:** Tổ chức có thể sử dụng bộ attribute mặc định hoặc tùy chỉnh thêm để phù hợp với mô hình quản trị riêng.

### D. Deep Summary của Chương 4
**Bối cảnh:**
Chương 4 đóng vai trò là “meta-structure” của toàn bộ tiêu chuẩn, không đưa ra yêu cầu kiểm soát cụ thể mà định nghĩa cách tổ chức, phân loại và diễn giải các control. Đây là nền tảng để đảm bảo việc hiểu và áp dụng các clause sau (5–8) được nhất quán và có thể mở rộng theo nhu cầu tổ chức.

**Nội dung cốt lõi:**
- Bộ control được tổ chức theo các clause 5–8, tương ứng với các nhóm: organizational, people, physical và technological.
- Hai annex hỗ trợ việc sử dụng tài liệu:
  - `Annex A`: hướng dẫn cách sử dụng attribute để phân tích control
  - `Annex B`: cung cấp mapping với phiên bản 2013 để phục vụ chuyển đổi
- `Themes` cung cấp phân loại cấp cao theo nội dung control, trong khi `attributes` đóng vai trò là lớp metadata giúp tạo các góc nhìn phân tích khác nhau.
- Bộ attribute mặc định gồm 5 nhóm chính, hỗ trợ phân tích control theo loại kiểm soát, mục tiêu bảo mật, khả năng vận hành và domain bảo mật.
- Tiêu chuẩn cho phép tổ chức tùy chỉnh hoặc mở rộng attribute, miễn là vẫn đảm bảo tính nhất quán trong cách sử dụng.

**Dữ liệu đáng chú ý:**
- Clause 5–8 tương ứng với 4 nhóm control chính (organizational, people, physical, technological).
- Hai annex thông tin:
  - `Annex A – Using attributes`
  - `Annex B – Correspondence with ISO/IEC 27002:2013`
- `Control type`: `Preventive`, `Detective`, `Corrective`
- `Operational capabilities`: bao gồm các năng lực như governance, asset management, IAM, threat & vulnerability management, và incident management
- `Security domains`: gồm governance & ecosystem, protection, defence và resilience

**Rủi ro / Lưu ý:**
- Hiểu sai cách sử dụng theme và attribute có thể dẫn đến việc phân tích và báo cáo control không nhất quán.
- Không khai thác attribute sẽ làm giảm giá trị của tiêu chuẩn, giới hạn khả năng phân tích đa chiều.
- Việc tùy chỉnh attribute mà không có governance rõ ràng sẽ gây khó khăn trong việc chuẩn hóa và bảo trì tài liệu.
- Không tuân thủ layout chuẩn của control có thể làm mất ý nghĩa giữa các thành phần như purpose, guidance và implementation.

### E. Structured Output của Chương 4
**Section:** 4.1
**Title:** Clauses

**Document structure:**
This document is structured as follows:
a) Organizational controls (Clause 5)
b) People controls (Clause 6)
c) Physical controls (Clause 7)
d) Technological controls (Clause 8)

**Informative annexes:**
There are 2 informative annexes:
- Annex A — Using attributes
- Annex B — Correspondence with ISO/IEC 27002:2013

**Explanation:**
Annex A explains how an organization can use attributes (see 4.2) to create its own views based on the control attributes defined in this document or of its own creation.
Annex B shows the correspondence between the controls in this edition of ISO/IEC 27002 and the previous 2013 edition.

---
**Section:** 4.2
**Title:** Themes and attributes

**Themes (Control categorization by nature):**
The categorization of controls given in Clauses 5 to 8 are referred to as themes.
Controls are categorized as:
a) people, if they concern individual people;
b) physical, if they concern physical objects;
c) technological, if they concern technology;
d) otherwise they are categorized as organizational.

The organization can use attributes to create different views which are different categorizations of controls as seen from a different perspective to the themes. Attributes can be used to filter, sort or present controls in different views for different audiences. Annex A explains how this can be achieved and provides an example of a view.

By way of example, each control in this document has been associated with five attributes with corresponding attribute values (preceded by "#" to make them searchable), as follows:

**a) Control type:**
Control type is an attribute to view controls from the perspective of when and how the control modifies the risk with regard to the occurrence of an information security incident. Attribute values consist of Preventive (the control that is intended to prevent the occurrence of an information security incident), Detective (the control acts when an information security incident occurs) and Corrective (the control acts after an information security incident occurs).

**b) Information security properties:**
Information security properties is an attribute to view controls from the perspective of which characteristic of information the control will contribute to preserving. Attribute values consist of Confidentiality, Integrity and Availability.

**c) Cybersecurity concepts:**
Cybersecurity concepts is an attribute to view controls from the perspective of the association of controls to cybersecurity concepts defined in the cybersecurity framework described in ISO/IEC TS 27110. Attribute values consist of Identify, Protect, Detect, Respond and Recover.

**d) Operational capabilities:**
Operational capabilities is an attribute to view controls from the practitioner’s perspective of information security capabilities. Attribute values consist of Governance, Asset_management, Information_protection, Human_resource_security, Physical_security, System_and_network_ security, Application_security, Secure_configuration, Identity_and_access_management, Threat_and_vulnerability_management, Continuity, Supplier_relationships_security, Legal_and_ compliance, Information_security_event_management and Information_security_assurance.

**e) Security domains:**
Security domains is an attribute to view controls from the perspective of four information security domains: “Governance and Ecosystem” includes “Information System Security Governance & Risk Management” and “Ecosystem cybersecurity management” (including internal and external stakeholders); “Protection” includes “IT Security Architecture”, “IT Security Administration”, “Identity and access management”, “IT Security Maintenance” and “Physical and environmental security”; “Defence” includes “Detection” and “Computer Security Incident Management”; “Resilience” includes “Continuity of operations” and “Crisis management”. Attribute values consist of Governance_and_Ecosystem, Protection, Defence and Resilience.

The attributes given in this document are selected because they are considered generic enough to be used by different types of organizations. Organizations can choose to disregard one or more of the attributes given in this document. They can also create attributes of their own (with the corresponding attribute values) to create their own organizational views. Clause A.2 includes examples of such attributes.

---
**Section:** 4.3
**Title:** Control layout

**Control layout:**
The layout for each control contains the following:
- Control title: Short name of the control;
- Attribute table: A table shows the value(s) of each attribute for the given control;
- Control: What the control is;
- Purpose: Why the control should be implemented;
- Guidance: How the control should be implemented;
- Other information: Explanatory text or references to other related documents.

**Notes:**
Subheadings are used in the guidance text for some controls to aid readability where guidance is lengthy and addresses multiple topics. Such headings are not necessarily used in all guidance text. Subheadings are underlined.