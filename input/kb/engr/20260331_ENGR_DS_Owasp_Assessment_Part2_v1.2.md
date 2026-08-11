# Owasp Assessment Part 2 - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Owasp Risk Assessment Form**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 6
- **Phân loại (Category):** Owasp Risk Assessment Form

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Has Background checks and a 3rd party Risk Assessment been performed on all 3rd parties? Please provide specifics.
### Answer:
We do have a security management policy for 3rd parties, which is specified in our IT security pocily. 
I. Information System Security for Partners
- Before entering into contracts for the supply of goods, services, or before connecting to the UrBox information system, assess the technical capability of partners in the field of safety and security. Pay particular attention to issues of confidentiality, integrity, availability, reliability, maximum performance, disaster recovery capability, and storage media of the information system.
- Products, services, or information systems of partners intending to connect to the UrBox information system must undergo security assessments according to security standards set by UrBox.
- Identify all risks based on the results of security assessments and establish risk mitigation measures before connecting to the UrBox information system.
- Contracts with partners and subcontractors must include clauses regarding penalties for violations of information security regulations and the responsibility to compensate damages for violations by partners and subcontractors resulting in harm.
- Apply strict monitoring measures and limit the access rights of partners when granting them access to the UrBox information system. Partners are not allowed to exploit their connection to the UrBox information system to collect, store, share, or perform other actions that could affect the safety and security of UrBox customer data.
- Information system security clauses must be included in contracts or commitment documents with partners. These clauses must include, but are not limited to, the following: 
+ Adherence to information system security regulations according to legal requirements and those of UrBox. 
+ Responsibility for information system security issues related to products and services provided to UrBox. 
+ Commitment to safeguard UrBox information accessed during the provision of products, services, or connection to the UrBox information system.
- Monitor and assess the services provided by partners to ensure their safety and operational capabilities meet the agreed terms.
- Manage changes related to services provided by partners, including upgrading to new versions, using new techniques, tools, and development environments. Perform a comprehensive impact assessment of changes to ensure safety upon implementation.
II. Partner Workforce Management
1. Prior to Work Deployment: 
- Request partners and subcontractors to provide a list of personnel involved. 
- Verify the legal status and professional capabilities of partners and subcontractors to meet job requirements. 
- Require partners and subcontractors to sign a commitment not to disclose information.
2. During Work Deployment: 
- Provide and ensure partners and subcontractors adhere to the company's policies and data security regulations. 
- Monitor compliance with the security regulations by personnel from partners and subcontractors. 
- In case of identifying signs of violations of data security regulations by partners or subcontractors, UrBox should: 
- Temporarily suspend or halt the activities of partners or subcontractors based on the severity of the violation. 
- Notify partners and subcontractors of security breaches involving their personnel. 
- Investigate, identify, and report the extent of the violation and inform partners and subcontractors of the damage incurred. 
- Revoke the data system access rights previously granted to partners and subcontractors.
3. Upon Completion of Work: 
- Demand partners and subcontractors to hand over company assets used during the execution of the work. 
- Revoke the granted access rights from partners and subcontractors upon termination. Erase UrBox information from partners' devices before returning. 
- Change locks, passwords, and access rights after receiving handover from partners and subcontractors.

---
### Question:
Please attach Data Flow Diagram of customer data flow from beginning to end
### Answer:
https://drive.google.com/file/d/1KCNgrfSgk8140bNQtIFoAa3QJG2jOl-7/view?usp=drive_link

---
### Question:
What Security Frameworks do you follow?
### Answer:
We follow security Frameworks: 
ISO27001:2013 and PCI DSS 4.0

---
### Question:
Will you provide or be providing yearly PEN Tests Yes/No?
### Answer:
Yes

---
### Question:
Name of company performing PEN Test with estimated completion date
### Answer:
UrBox used tool Zap of CheckMarx to Pentest

---
### Question:
If completed, have all vulnerabilities of the PEN Test been completed? If not when?
### Answer:
Yes, UrBox will fix the error within 15 days if has error