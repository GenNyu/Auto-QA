# Vendor Questionnaire Part 5 - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Vendor Questionnaire**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 15
- **Phân loại (Category):** Vendor Questionnaire

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Does your organization implement host firewall protection?
### Answer:
UrBox using Cloudflare to host protection

---
### Question:
Is encryption and integrity protection in place for all internal and external network traffic that potentially carries sensitive information (including passwords, emails, files, source code, management traffic, etc.)?
### Answer:
UrBox implements encryption and integrity protection for all internal and external network traffic that potentially carries sensitive information, including passwords, emails, files, source code, and management traffic. This security measure ensures that data is transmitted securely and cannot be easily intercepted or tampered with by unauthorized parties. Encryption protocols such as HTTPS, SSL/TLS, and other encryption methods are used to safeguard the confidentiality and integrity of the data being transmitted over our networks.

---
### Question:
Are vulnerability scans performed at least twice a year?
### Anwser:
N/A

---
### Question:
Are penetration tests conductedat least annually?
### Anwser:
N/A

---
### Question:
Do you have recovery plan in place? If yes, please explain whether it's an IT Disaster Recovery Plan or a full operational Business Continuity Plan.
### Answer:
we have a comprehensive recovery plan in place. Our plan encompasses both an IT Disaster Recovery Plan and a full operational Business Continuity Plan. The IT Disaster Recovery Plan focuses on the recovery of IT systems, data, and technology infrastructure in the event of a disruption or disaster. This includes procedures for data backup and recovery, system restoration, and ensuring IT services are brought back online efficiently.
Additionally, our Business Continuity Plan addresses the broader operational aspects of our organization. It outlines strategies for maintaining critical business functions and processes during and after disruptive events. This plan covers not only IT systems but also personnel, communication channels, physical facilities, and more. The goal is to ensure that our organization can continue functioning with minimal interruption, safeguarding our operations, reputation, and the interests of our stakeholders.

---
### Question:
Have you conducted a recovery plan exercise within the last 12 months?
### Anwser:
N/A

---
### Question:
How frequently are backups conducted? (choose from drop list)
### Answer:
2h

---
### Question:
How often are backups validated?
### Answer:
2h

---
### Question:
Does your organization have a media sanitization process?  (Removal of information from storage media)  If yes, please describe.
### Answer:
our organization has a media sanitization process in place for the secure removal of information from storage media. This process ensures that data is properly erased or destroyed when storage media reach the end of their lifecycle or are no longer needed. The media sanitization process may involve several methods:
Secure Erasure: Data is overwritten using specialized software to ensure that it cannot be recovered using standard methods. Multiple passes of overwriting may be performed for sensitive data.
Physical Destruction: For storage media that can't be effectively sanitized through erasure, physical destruction methods are used. This can involve shredding hard drives, degaussing magnetic media, or melting down certain types of media.

---
### Question:
Do you allow teleworking?  If so, please describe your remote security implementation.
### Answer:
We allows teleworking, and we have implemented a comprehensive remote security strategy to ensure the security of remote work environments. Remote employees use secure virtual private network (VPN) connections to access our organization's internal network. This encrypts data transmitted between remote devices and the corporate network, ensuring confidentiality.

---
### Question:
Do you have a Mobile Device Management (MDM) system in place?
### Answer:
Currently, we do not have any policy on MDM, employees can only use laptops and computers issued by the company for work purposes.

---
### Question:
Has your organization ever had an independent review of its information security practice? If yes, please provide the results of your last review.
### Answer:
we are assessed and certified by BSI organization ISO 27001:2013

---
### Question:
Has your organization experienced any data breaches in the last 5 years? If so, please describe.
### Answer:
We have not experienced any data breach in the last 5 years

---
### Question:
Has your organization experienced any other malicious or criminal activities directed against it in the last 5 years? If so, please describe.
### Anwser:
N/A

---
### Question:
Is your organization currently involved in any regulatory, compliance, or legal issues that may impact service delivery? If so, please describe.
### Anwser:
N/A
