# Cryptographic Safeguard - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Cryptographic Safeguard**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 26
- **Phân loại (Category):** Cryptographic Safeguard

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Does your organization have a policy on the use of encryption, including cryptographic authentication and integrity controls such as digital signatures and message authentication codes, and cryptographic key management?
### Answer:
Yes

---
### Question:
What protocol(s) does your organization use to encrypt? Please list or explain.
### Answer:
SSL, TLS

---
### Question:
What is the name and version of the encryption software?
### Answer:
SHA-256
TripleDes
JWT

---
### Question:
Describe your encryption key management processes to securely manage keys throughout their lifecycle (generation, transmission, storage, rotation, disposal) and key management solutions used.
### Answer:
Encryptuon key will be created by DevOps & Head of Technology and then saved on production system

---
### Question:
Are there documented plans or procedures for cryptographic key owners to handle compromised keys and revoke and/or rotate the keys on an emergency basis?
### Answer:
Yes

---
### Question:
Are there documented plans or procedures for key rotation?
### Answer:
Yes

---
### Question:
Are there procedures for protection from key loss and corruption?
### Answer:
Yes

---
### Question:
Is there an access control policy implemented to limit access to only parties authorized by the key owner?
### Answer:
Yes

---
### Question:
Does your disaster recovery and business continuity plans account for lost or corrupted cryptographic keys?
### Answer:
Yes

---
### Question:
Are your organization's encryption keys stored separately?
### Answer:
Yes

---
### Question:
Is Segregation of Duties implemented where keys protecting more than 10 GB of highly confidential Manulife data is stored such that two or more persons are required to access the key, using methods such as dual knowledge, split custody or access controls?
### Answer:
Yes

---
### Question:
Are Certificate Authority (CA) used to trust a digital certificate and confirm the key lifecycle?
### Answer:
Yes

---
### Question:
Are Certificate Authority signing privilege reviewed annually by the CA root key owner?
### Answer:
Yes

---
### Question:
Where certificate authority cannot be used, are there compensating controls that the individual establishing the trust can apply?
### Answer:
Yes

---
### Question:
Are self-signed certificates utilized in providing services to Manulife/John Hancock?
### Answer:
No

---
### Question:
Are production certificates, utilized in providing services to Manulife/John Hancock, signed by an approved certificate authority (CA) with the support of key revocation functionality?
### Answer:
Yes

---
### Question:
Does your organization Encrypt data In Transit over internal Networks?
### Answer:
No

---
### Question:
Does your organization Encrypt data In Transit over external Networks?
### Answer:
Yes

---
### Question:
What is the encryption algorithm and key strength used?
### Answer:
256

---
### Question:
Does your organization have a team responsible to ensure that all encryption or other cryptographic techniques must use the approved algorithm (AES 256)?
### Answer:
Yes

---
### Question:
Are all data in-transit to or from, or at-rest on a mobile devices, workstations and any other in-scope end user devices encrypted?
### Answer:
Yes

---
### Question:
Do laptop computers have full disk encryption applied?
### Answer:
Yes

---
### Question:
Is your staff able to transfer information to removable media unencrypted?
### Answer:
Yes

---
### Question:
Does your organization require emails / instant messages containing Manulife/John Hancock data to be encrypted?
### Answer:
Yes

---
### Question:
Does your organization use any process or solutions to encrypt data at rest at the data, file, field, column, or volume-level?
Please describe the process and solutions in place to encrypt Manulife/JH data at rest.
ie. data owner encrypts data in transit and at rest based on data classification and approved encryption methods.
### Answer:
UrBox will encrypted all sensitive data (Personal information, gift code)  using TriplesDes algorithm

---
### Question:
If Manulife/John Hancock data is backed up or archived, are the databases or tapes supporting backups encrypted in transit and at rest?
If so, please provide a description of the process, solution, and encryption algorithm strength.
ie. the (System/Information Owner) ensures backups containing confidential and highly confidential data is encrypted during transport and at rest. In the event rest encryption cannot be applied additional controls are in place, including access control and alerting when the data is accessed for any reason.
### Answer:
For data at rest, the access keys are kept by only one authorised person, who will not know where the data is stored. There is 1 level of key hierarchy and keys will be rotated or replaced in every 6 months
For data in transit, all sensititve data (web sessions, data in transit between web, application and data layers, …) in motion have encryption. Communication protocol on data flows is SFTP/FTPS. We use version 1.2 of TLS