# Vendor Questionnaire Part 2- Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Vendor Questionnaire**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 13
- **Phân loại (Category):** Vendor Questionnaire

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Does your organization maintain routers and ACLs?
### Answer:
our UrBox maintains routers (network devices that facilitate data traffic between different networks) and Access Control Lists (ACLs) as part of our network security strategy. ACLs are used to define and enforce rules that control which network traffic is allowed or denied at different points within the network infrastructure. By managing routers and ACLs, we ensure that only authorized traffic is permitted, enhancing the overall security and efficiency of our network operations.

---
### Question:
Does your organzation provide network redundancy?
### Answer:
UrBox implements network redundancy as a part of our infrastructure strategy. For example, using 2 network lines of VNPT and FPT

---
### Question:
Does your organization use DMZ architecture for Internet systems?
### Answer:
UrBox employs a DMZ (Demilitarized Zone) architecture for our internet-facing systems. The DMZ acts as a buffer zone between our internal network and the public internet. Internet-facing servers, such as web servers or email servers, are placed within the DMZ to separate them from our internal network.

---
### Question:
Does your organization use enterprise virus protection on all system?
### Answer:
we only utilize internal antivirus software and the free version for businesses on all systems.

---
### Question:
Does your organization ensure that remote access is only possible over secure connections?
### Answer:
UrBox ensures that remote access is only possible over secure connections. We only enforce the use of secure protocols such as VPN (Virtual Private Network).

---
### Question:
Does your organization manage, secure access points on wireless network?
### Answer:
our organization manages and secures access points on our wireless network. We implement strong security measures such as WPA3 encryption, strong authentication methods, and regular updates to access point firmware.

---
### Question:
Are employees able to access sensitive information from personal devices?
### Answer:
employees are not allowed to access sensitive information from personal devices. Our organization enforces a strict policy that restricts access to sensitive data to authorized devices and secure network connections.

---
### Question:
Are there intrusion detection/prevention systems (IDS/IPS) in use?
### Answer:
Our organization uses intrusion detection and prevention systems (IDS/IPS) as part of its cybersecurity measures. This system is integrated on AWS Cloudflare firewall

---
### Question:
Do you have operating system hardening in place, or build standards for server systems?
### Answer:
our organization has implemented operating system hardening practices and follows specific build standards for server systems as CIS Benmark. Operating system hardening involves configuring the server's operating system to minimize vulnerabilities and reduce the attack surface. This includes tasks such as disabling unnecessary services, applying security patches, configuring proper access controls, and implementing other security best practices.

---
### Question:
Do you perrform Security Updates and Vulnerability Management
### Answer:
UrBox regularly performs security updates and vulnerability management as a crucial part of our cybersecurity practices. This involves monitoring for software vulnerabilities, staying informed about security advisories, and promptly applying patches and updates to address any identified vulnerabilities.

---
### Question:
Do you have procedures in place for regularly auditing administrative access to your servers?
### Answer:
UrBox has established procedures for regularly auditing administrative access to our servers. This process involves monitoring and reviewing the actions of administrators who have access to critical systems. By conducting regular audits, we ensure that administrative activities are aligned with established policies, and any unauthorized or suspicious actions are promptly identified and addressed.

---
### Question:
Do you regularly perform backup on sensitive data?
### Answer:
our organization regularly performs backups of sensitive data as part of our data protection and disaster recovery strategy. These backups are conducted on a scheduled basis 2h/time to ensure that in the event of data loss, corruption, or other incidents, we can restore the information to a previous state.

---
### Question:
Do you sync data to a different site in near real time?
### Answer:
we syncs data to a different site in near real-time as part of our data redundancy and disaster recovery measures.