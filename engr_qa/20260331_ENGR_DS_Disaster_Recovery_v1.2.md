# Disaster Recovery - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Disaster Recovery**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 22
- **Phân loại (Category):** Disaster Recovery

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Does your enterprise have a Disaster Recovery Program with policies and standards, roles and responsibilities, and documented and approved disaster recovery plan(s) which define in-scope systems, prioritization of systems, recovery objectives, key stakeholders, and detailed recovery procedures for the resumption of critical business processes that is reviewed and updated at least annually?
### Answer:
Yes

---
### Question:
Is there a segregation of duties in disaster recovery plan(s) and exercise(s) between the person creating or updating plan(s) and conducting exercises and the person approving the plan or signing off on exercise results?
### Answer:
No

---
### Question:
What is the documented recovery time objective (RTO) for the reviewed service?
### Answer:
1h

---
### Question:
What Strategies does your DR Plan employ: (check all that apply)
### Answer:
If Synchronous replication then Yes. 
Else if Asynchronous replication then No. 
Else if High availability then No. 
Else if VM/SRM recovery then No. 
Else if Dedicated DR hardware then No. 
Else if Repurposing of hardware then No. 
Else if Other then No, please explain.

---
### Question:
Does your Disaster Recovery program include a testing program?
### Answer:
Yes

---
### Question:
Which strategies do you test?
### Answer:
Other
### Comment:
AWS Cloud Service

---
### Question:
What is the date of your most recent Disaster Recovery exercise?
### Answer:
12/12/2022

---
### Question:
Which strategies were tested?
### Answer:
Other
### Comment:
AWS Cloud Service

---
### Question:
What was the recovery time actual (RTA) of your most recent test?
### Answer:
10 minutes

---
### Question:
What were the results of your most recent test:
### Answer:
Successful

---
### Question:
What was the recovery point actual (RPA) of your most recent test?
### Answer:
10 minutes

---
### Question:
Separate from data replication solutions, Are backups created regularly, encrypted, and stored in an offsite location?
### Answer:
N/A
### Comment:
bản sao lưu được lưu trữ trong dịch vụ backup của AWS. AWS sẽ tự lưu trữ ở S3. và có mã hóa bản backup.
Mã hóa thì dùng chuẩn: AES-256

---
### Question:
How frequently is it being sent off site
### Answer:
N/A

---
### Question:
What is the documented recovery point objective (RPO) for the reviewed service?
### Answer:
3h

---
### Question:
Does your Disaster Recovery strategy involve the use of an alternate location?
### Answer:
Yes

---
### Question:
Please provide the location or region of your primary and alternate site.
### Answer:
HN + HCM

---
### Question:
What is the distance between your primary and alternate site?
### Answer:
2 hours

---
### Question:
When last did you operate out of the alternate site(s)?
### Answer:
N/A

---
### Question:
For how long?
### Answer:
N/A

---
### Question:
Does the service being reviewed employ cloud services?
### Answer:
Yes

---
### Question:
What type of cloud services are employed?
### Answer:
AWS Cloud

---
### Question:
Who is your cloud service provider?
### Answer:
AWS
