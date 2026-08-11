# Cloud Services - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Cloud Services**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 19
- **Phân loại (Category):** Cloud Services

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Are the services provided to Manulife/John Hancock hosted on a third party cloud provider?
### Answer:
Yes

---
### Question:
Who is the cloud provider?
### Answer:
Amazon Web Service

---
### Question:
Is Manulife/John Hancock data hosted on a third party cloud provider?
### Answer:
Yes

---
### Question:
Does your organization have a Cloud Security Strategy that includes regulations for data sovereignty?
### Answer:
Yes

---
### Question:
If a SAAS solution, does your organization have a documented pre-production testing process? Briefly explain how pre-production testing is accomplished and how Manulife is / will be involved in this process.
### Answer:
Yes

---
### Question:
Briefly explain how pre-production testing is accomplished and how Manulife/John Hancock is / will be involved in this process.
### Answer:
UrBox will develop a version on development environment. When doing UAT, Manulife will join to test. After 2 parties finish acceptance, UrBox will run on production environment

---
### Question:
Does your organization conduct network penetration tests of its cloud service infrastructure regularly as prescribed by industry practices and guidance?
### Answer:
Yes

---
### Question:
Are penetration testing engagements reviewed and approved by Information Risk Management and the Business, Application, System or Platform Owner?
### Answer:
Yes

---
### Question:
Are your subcontractors engaged in hosting, storing, or processing Manulife/John Hancock' data as part of cloud deployment services?
### Answer:
No

---
### Question:
Please specify the subcontractors' location(s).
### Anwser:
N/A

---
### Question:
What type of cloud-solution will be used to process Manulife/John Hancock data (e.g., SAAS, PAAS, IAAS)?
### Answer:
PAAS

---
### Question:
Please briefly describe the solution and how data will interact with the solution.
### Answer:
UrBox will develop rewarding system for Manulife, data will be stored on AWS

---
### Question:
Briefly describe what type of environment the cloud solution will process in (e.g., Private, Public, Community or Hybrid).
### Answer:
Public for customer & staff of manulife

---
### Question:
Is user provisioning handled by your organization (as opposed to a third party)?
### Answer:
Yes

---
### Question:
Please explain how the user provisioning for sourced/cloud services are accomplished.
### Answer:
1. Employee creates request
2. Head of department approves
3. IT department review request, provide resources

---
### Question:
Are tenants isolated from each other within the cloud service?
### Answer:
Yes

---
### Question:
Are cryptographic controls in place to protect system information in transit and at rest, to ensure the confidentiality and integrity of the data?
### Answer:
Yes

---
### Question:
Does the data owner encrypt data in transit and at rest based on data classification and approved encryption methods?
### Answer:
Yes

---
### Question:
Please describe the metrics that are / will be available to Manulife/John Hancock to monitor the security health of the cloud solution(s) managing Manulife data?
### Answer:
All Metric on CloudWatch. Example:
+ CPUUtilization
+ DatabaseConnections
+ ReadLatency
+ WriteLatency
+ SlowQuery
+ Service Status
...