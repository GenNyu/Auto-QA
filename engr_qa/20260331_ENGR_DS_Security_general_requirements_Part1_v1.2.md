# Security general requirements - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Security general requirements**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 14
- **Phân loại (Category):** Security general requirements

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Vendor should have achieved certifications(prefer ISO 27001, PA DSS, SOC II type II). List all your certifications
### Answer:
- ISO 27001:2013
- PCI DSS

---
### Question:
Describe your secure software development life-cycle
### Answer:
Not understand

---
### Question:
Describe the methodology or framework applied in security testing
### Answer:
- The methodology applied in security testing, we follows:
Information Gathering (Reconnaissance) -> Threat Modeling -> Scanning and Enumeration -> Vulnerability Assessment -> Exploitation -> Reporting -> Remediation
- Framework applied in security test: Owasp Zap, Nessus, Qualys Cloud Platform

---
### Question:
The solution should comply web/mobile application security standards (i.e OWAPS, especially OWAPS 10, CWE/SANS top 25)
### Answer:
- OWASP
- OWASP Top Ten

---
### Question:
Provide lastest penetration testing details report of your system
### Answer:
As the attached file (named "report_uploaded.zip")

---
### Question:
Describe life-cyfle of solution, frequency release/update security fix.
### Answer:
Will release/update right away when found out the security issues

---
### Question:
Describe your security architecture
### Answer:
Is this the architecture for only the integration?

---
### Question:
- Describe authentication mechanism in your solution. 
- Which authentication mechanism your solution support for (describe detail):
 + bank user
 + customer user
 + for communication between components in the system
 + for integration between other Techcombank system and Digital channel system (WS, File transfer, Queue, JMS, Socket ..)
- How solution prevent authentication attack, brute force attack ... Describe detail
- How Techcombank can apply your authentication mechanism when customize, extend or develop new function
### Answer:
- Authentication machanism will be API integration between 2 systems using RSA encryption.

---
### Question:
- Describe access control/authorization mechanism in your solution
+ Access control for bank user
+ Access control for customer user
- How your solution prevent authorization bypass attack as path traversal, bypass authorizarion, privilege escalation; prevent user, hacker access information, bank account of other user, coporate …
- How Techcombank can apply your authorization mechanism when customize, extend or develop new function
### Answer:
Not Relevant

---
### Question:
- Describe session management mechanism in your solution
- How your solution create/manage/delete session of customer user, bank user
- How your solution prevent session attack: session prediction, session hijack, session exposed, session bruteforce, csrf … Describe detail 
- How Techcombank can apply your session management mechanism when customize, extend or develop new function
### Answer:
Not Relevant

---
### Question:
- Describe data input validation mechanism in your solution
- How your solution prevents Injection attack as SQL injection, OS command, LDAP injection, Xpath Injection, code injection; prevent buffer over flow vulnerability…
- How Techcombank can apply your validate mechanism when customize, extend or develop new function
### Answer:
DevOps and Engineering

---
### Question:
- Describe data output encode/escape mechanism in your solution
- How your solution prevent XSS attack …
- How your solution masking sensitive information when output
- How Techcombank can apply your  data output encode/escape  mechanism when customize, extend or develop new function
### Answer:
- There is no output
- XSS
- There is no output to display sensitive information
- No need because there is no output

---
### Question:
- Describe Cryptography mechanism support in your solution
- Which does crytography algorithsm support
- How to manage crytography algorithsm key 
- How Techcombank can apply your crypography mechanism when customize, extend or develop new function to encrypt/decrypt sesitive information
### Answer:
- SHA512 to encrypt phonenumber if needed along with RSA signatures to make sure the data is not modified before receiving.
- SHA512
- UrBox will provide public key to TCB. UrBox will use private key to decrypt data from TCB.

---
### Question:
- Describe Error handling mechanism in your solution
- How Techcombank can apply error handling mechanism when customize, extend or develop new function
### Answer:
- Errors will be threw and responsed to client with specified details
- Will discuss in details during the integration period.