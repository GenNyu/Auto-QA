# Security general requirements - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Security general requirements**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 4
- **Phân loại (Category):** Security general requirements

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
- Describe Data Protection mechanism for sensitive information in your solution: when store, transmit and process
### Answer:
UrBox system uses AWS services to secure data storage and transmission as follows:
- Data Storage: Utilize Amazon S3 (Simple Storage Service) to store data and enables server-side encryption to ensure data is securely stored. Sets up lifecycle management rules to automatically move data to different storage classes based on requirements and reduce storage costs.
- Data Transmission: Use Amazon CloudFront to provide Content Delivery Network (CDN) services and Cloudflare to optimize data transmission with high speed, while also supporting SSL/TLS to ensure security during transmission.
- Data Processing: Utilize AWS Key Management Service (KMS) to manage access and encrypt data during data processing when accessing the database."

---
### Question:
Describe the security communication between customer and Bank system mechanism
### Answer:
Not relevant

---
### Question:
- Describe Logging mechanism in your solution
- Which information can be log, can we select it?
- Where is your solution store log?
### Answer:
The UrBox system has many layers of logging information system activities, including:
- Activity logs when the database changes are centralized to the datawarehouse
- Activity logs of requests processed in Elastic Search
- Infrastructure change logs are saved at AWS Cloudtrail

---
### Question:
Describe how your solution to compliance with OWASP top 10 security vulnerability. Detail for each of 10 vulnerability
### Answer:
UrBox system relies on Cloudflare to adhere to specific OWASP Top 10 vulnerabilities as follows:
- Injection (SQL, NoSQL, OS, and LDAP injection): Cloudflare WAF is meticulously configured to scrutinize and filter incoming requests, fortifying our defenses against potential injection threats, encompassing SQL, NoSQL, OS, and LDAP vulnerabilities.
- Broken Authentication: Two-factor authentication (2FA) is enforced through Cloudflare Access, ensuring that only authorized personnel can access critical company resources. Furthermore, our team actively monitors Cloudflare Access logs for any irregularities in authentication activities.
- Sensitive Data Exposure: Cloudflare's SSL/TLS features are actively employed to encrypt data during transit, establishing a robust defense against potential data exposure. Regular audits are conducted to verify the proper implementation of encryption protocols.
- XML External Entities (XXE): Cloudflare WAF rules are specifically tailored to thwart and mitigate XML External Entity (XXE) attacks. We consistently monitor XML input to promptly identify and rectify any potential XXE vulnerabilities.
- Broken Access Control: Cloudflare Access serves as the linchpin for our access control strategies, ensuring that employees possess the appropriate permissions to access company resources. Routine reviews of access control configurations are conducted to pinpoint and rectify any potential issues.
- Security Misconfigurations: Cloudflare WAF is finely tuned to minimize security misconfigurations, and the Optimization feature is deployed to align Cloudflare settings with our stringent security policies. Regular security reviews are conducted to rectify any misconfigurations promptly.
- Cross-Site Scripting (XSS): Cloudflare WAF is configured to detect and mitigate Cross-Site Scripting (XSS) attacks. Ongoing developer training emphasizes secure coding practices to thwart the introduction of XSS vulnerabilities into our company applications.
- Insecure Deserialization: Cloudflare WAF provides specific rules to identify and block insecure deserialization attempts. Our development team is committed to adhering to secure coding practices and promptly updating libraries and frameworks to mitigate deserialization vulnerabilities.
- Using Components with Known Vulnerabilities: Cloudflare's Automatic Platform Optimization (APO) is implemented to mitigate the risk associated with using components with known vulnerabilities. Regular vulnerability scans are conducted, and APO settings are adjusted accordingly to address any identified issues.
- Insufficient Logging & Monitoring: Cloudflare's logging and monitoring tools are extensively utilized to track and analyze system activities. Automated alerts are configured to notify the security team promptly of any suspicious behavior, ensuring swift responses to potential security incidents.