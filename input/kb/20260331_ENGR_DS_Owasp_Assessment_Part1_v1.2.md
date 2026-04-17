# Owasp Assessment Part 1 - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Owasp Risk Assessment Form**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 16
- **Phân loại (Category):** Owasp Risk Assessment Form

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Card Link Services Program Name
### Answer:
UrBox Earning Solution

---
### Question:
Card Link Services Business attached to this program (including yourself) and at what capacity (Hosting,Providing,Third Parties, list them all here and what they will be doing) List ALL Parties
### Answer:
NA

---
### Question:
Countries Card Link Services Program will be either operating in and or customers are allowed to participate from
### Answer:
VietNam

---
### Question:
Estimated Yearly Revenue of the CLS Program
### Answer:
500,000 USD - 1mil USD

---
### Question:
3rd Party Certifications (Please attach, example SOC2Type2,ISO)
### Answer:
SOC 2 AWS, SOC 3 AWS 
PCI DSS: 
https://drive.google.com/file/d/1QIZnMM_vSrowTuN-EaaW4OQKg2Vrfq3n/view?usp=sharing
https://drive.google.com/file/d/1LQvm1UEK9O9QQpOsQBb87PuU4NFoqc3A/view?usp=sharing
ISO
https://drive.google.com/file/d/1cR8kPRNDvk7LpaC77rVKZeJnUrgcwLUg/view?usp=sharing

---
### Question:
Organizational Contacts (Please List CSO,CISO,Security Officers) Point of Contacts
### Answer:
_x0008_No - Name - Positon - Email:     
1 - Ngô Thiên Tân - Head of Engineering - tan.ngo@urbox.vn
2 - Lê Hải Thịnh - Member - thinh.lh@urbox.vn
3 - Trương Quốc Thắng - Member - thang.tq@urbox.vn

---
### Question:
Projected Launch Date of CLS Program with Mastercard ( If already a Active Program N/A
### Answer:
NA

---
### Question:
CLS Program Overview ( High Level Overview of entire program and processes from customer enrollment to completion)
### Answer:
Attachment

---
### Question:
List all type of information both PCI/PII Program will touch in its entirety( For example Email, Name, Phone,) PCI( PAN, Last 4,etc)
### Answer:
List all type of Information:
name, first 6 digits and last 4 digits from card number, token

---
### Question:
Amount of customer data program will have
### Answer:
around 500K

---
### Question:
Estimated Yearly amount of transactions the program touches
### Answer:
2 millions

---
### Question:
Can you provide evidence you follow all local Privacy Laws (GDPR, SOX, GLBA etc of the countries you operate in? Attach evidence
### Answer:
In 2023, Vietnamese Government issued Decree 13/2023/ND-CP on protection of personal data. When launching new white label platforms that are involved in the processing of personal data, we all require the consent of users that we will process their personal data, ensuring that the data subject voluntarily and fully knows the following:
- Type of personal data to be processed;
- Purpose of processing personal data;
- Organizations and individuals process data;
- Rights and obligations of data subjects.
All user consents are specifically expressed by actions, either in writing, by voice, by checking a consent box, by text message consent syntax, by selecting technical consent settings or by another action that demonstrates this.
Attachement is the screen when user first login UrBox application. By creating and logging into an account, user agrees to the Terms & Conditions of UrBox - which strictly follow the local Privacy laws
Link evidence: https://drive.google.com/file/d/1WEqB2Lm-0s0o7kZhk2vBlO_1c3VgRqm4/view?usp=share_link

---
### Question:
CLS Website Name, Brochures etc
### Answer:
NA

---
### Question:
Please attach Information Security Policy and Standards
### Answer:
https://drive.google.com/file/d/1LK8vaeFNEn57TUAR9M5lx0sMEa2f3xwO/view?usp=drive_link

---
### Question:
Please list all IT environments the Card Link Services Program will be operating in and give specifics? ( Cloud,IaaS,Paas,SaaS, Hybrid, Local, data center, virtualization) List all Providers and relationships between them.
### Answer:
All services operate 100% in AWS using EC2 (IaaS) and RDS (PaaS)

---
### Question:
List all Penetration Tests completed for every environment touching PCI/PII
### Answer:
List Pentest completed:
- Cross Site Scripting
- Information Leak
- Backup File Disclosure
- Cookie Slack Detector
- Directory Browsing
- Heartbleed OpenSSL Vulnerability
- Hidden File Finder
- Proxy Disclosure
- Remote Code Execution
- Source Code Disclosure
- User Agent Fuzzer
- SQL Injection
- Buffer Overflow
- Cloud Metadata Potentially Exposed
- CRLF Injection
- Expression Language Injection
- Remote OS Command Injection
- Server Side Code Injection
- XPath Injection
- File Upload
- HTTP Only Site
- JWT Scan Rule
- Session Fixation
- Anti-CSRF Tokens Check
- Cross-Domain Misconfiguration
- Insecure HTTP Method
- Httpoxy - Proxy Header Misuse