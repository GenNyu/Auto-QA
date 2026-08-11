# Technical Controls - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Technical Controls**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 12
- **Phân loại (Category):** Technical Controls

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Pen Testing:  How many vulnerabilities from your latest pen test remain open and at what severities?
### Answer:
Only a few medium and low level vulnerabilities remain

---
### Question:
Email:  Is your email self hosted or if hosted by a 3rd party service; which one?
### Answer:
UrBox's email system is hosted by a third-party service, specifically Google Workspace. Google Workspace provides email hosting and a suite of productivity tools, including Gmail, which UrBox uses for its email communication needs.

---
### Question:
Email:  Are email servers DMARC, DKIM, and SPF enabled on all send from email domains?
### Answer:
Yes, UrBox has implemented DKIM (DomainKeys Identified Mail) on all send-from email domains. These email security mechanisms are crucial for verifying the authenticity of emails and preventing email spoofing and phishing attacks. Their implementation helps ensure that emails sent from UrBox are more secure and less likely to be marked as spam or subjected to fraudulent activities.

---
### Question:
Email:  Do you have Anti-Spam/Phishing solutions in place for your employees?
### Answer:
Yes, UrBox has implemented Anti-Spam/Phishing solutions in Google Workspace for our employees. These solutions are designed to detect and block spam emails, phishing attempts, and other malicious email activities.

---
### Question:
Email:  Were your email systems included in your last Pen Test or a separate Network Test within the last 12 months?
### Answer:
Because Google Workspace provides robust security measures and is managed by one of the world's leading technology companies, UrBox has decided not to conduct a pentest on our email system.

---
### Question:
Email:  Please list ALL sending address/domain for email communications from your service?  i.e. awards@vendormessaging.com
### Answer:
customer@urbox.vn

---
### Question:
Email:  If provided with an OC Tanner hosted email account, can your service use that for emailing our customers related to award redemption?
### Answer:
No.

---
### Question:
Logging:  Do you generate and monitor logs for your service?
### Answer:
All log to UrBox services: These logs are stored in Elastic Cloud and retained for the latest 12 months.
The logging system captures Nginx access logs at UrBox's ingress. These logs are pushed to Kafka.
A Logstash process retrieves logs from Kafka, parses them into structured fields, and pushes them to Elastic Cloud.

---
### Question:
Logging:  Do you ensure PII is not included in your log data?
### Answer:
Yes, we have implemented measures to ensure that Personally Identifiable Information (PII) is not included in our log data. Protecting sensitive data, including PII, is a fundamental aspect of data security and privacy compliance. Our logging practices are designed to capture relevant information for monitoring and troubleshooting while excluding any PII to minimize the risk of data exposure or breaches. Additionally, we regularly review and update our logging configurations and processes to maintain a high level of data protection.

---
### Question:
Logging:  How long to you store searchable logs (Hot) and archived logs (Cold)
### Answer:
we store searchable logs (Hot) for 3 months and archive logs (Cold) for 12 months

---
### Question:
Security Awareness Training:  What do you do for Security Awareness Training and how often?
### Answer:
Security Awareness Training is a crucial component of our organization's security strategy. Here's an overview of what we do and the frequency:
Training Content: We provide training materials that cover a wide range of security topics, including password best practices, identifying phishing attempts, safe browsing habits, data handling, and compliance with our security policies.
Onboarding Training: New employees receive security awareness training as part of their onboarding process. This ensures that from day one, they have a foundational understanding of our security policies and best practices.
Annual Training: We conduct annual security awareness training for all employees. This refresher training reinforces security principles and updates employees on the latest threats and security measures.

---
### Question:
Breach or Disclosure of PII:  Have you had a breach or unauthorized disclosure of PII within the last 5 years?  If so, please describe the event and remediation.
### Answer:
No.