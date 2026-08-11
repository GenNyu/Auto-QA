# Network Security Controls - Security Assessment Matrix

## A. Summary Overview
Tài liệu này cung cấp chi tiết các câu hỏi và trả lời bảo mật thuộc nhóm **Network Security Controls**. Đây là nguồn dữ liệu chính thống để AI trả lời các truy vấn về tiêu chuẩn bảo mật của Vendor.

## B. Key Metrics
- **Tổng số bản ghi (Items):** 34
- **Phân loại (Category):** Network Security Controls

## C. Insights
- Dữ liệu được cấu trúc theo dạng Hỏi-Đáp (Q&A) để AI dễ dàng trích xuất thông tin.
- Mỗi khối thông tin bao gồm đầy đủ Câu hỏi, Câu trả lời và Minh chứng đi kèm.

## D. Structured Output
### Question:
Does your organization allow access to JH/Manulife data from devices (laptops, tablets and phones)?
### Answer:
No

---
### Question:
What network security controls are in place to ensure data in-transit through the network is secure and reliable?
### Answer:
1. Virtual Private Networks (VPNs)
2. Firewalls
3. Secure Sockets Layer (SSL) or Transport Layer Security (TLS)

---
### Question:
What governing policies are established and implemented that ensures only authorized software is installed in the environment? (ie. whitelisting, blacklisting)
### Answer:
Whitelisting

---
### Question:
Are internet access and web content, from all network zones, inspected at all times through a web control filtering solution?
### Answer:
Yes

---
### Question:
Is network traffic management designed and configured to restrict unauthorized traffic access to and between security zones/subzones?
### Answer:
Yes

---
### Question:
Are access rules allowing cross zone traffic explicitly approved by your network team?
### Answer:
Yes

---
### Question:
Are network security controls in place to ensure the information that travels through the network is secure and reliable?
### Answer:
Yes

---
### Question:
Has your organization implemented network boundary monitoring and protection?
### Answer:
Yes

---
### Question:
Does your organization ensure that the connecting end-point device is isolated from the device's source network once the connection to your organization's network is established, and automated checks (e.g. Network Access Control solutions) are in place for managed devices to ensure that prior to granting access to your organization's network, the remote access device meets the following criteria:
- Approved endpoint protection software (e.g. antivirus, antimalware); not older than 7 days
- Hard disk encryption 
- Current remote device operating system patches; not older than 30 days
- Active and current client certificates.
### Answer:
Yes

---
### Question:
Does your organization's network infrastructure have multiple layers of defense (e.g. cloud based, ISP, on premise) to mitigate against attacks?
### Answer:
Yes

---
### Question:
What processes or solutions does your organization use to detect and mitigate the impact of Distributed Denial Of Service attacks (ie. Publicly available DNS infrastructures are automatically configured to detect DNS DoS, exploits, and cache poisoning, (upon identification) )?
### Answer:
CLoudflare

---
### Question:
Is there a Company issued mobile device security policy/plan?
### Answer:
Yes
### Comment:
IT Security Policy, SECTION 1.2 - MOBILE AND REMOTE WORKING DEVICES

---
### Question:
Does your organization own the mobile devices?
### Answer:
Yes

---
### Question:
If a mobile device management (MDM) solution is in place, does your organization monitor for external connections that are not managed by the MDM?
### Answer:
N/A

---
### Question:
Are Intrusion Detection or Intrusion Prevention Solution/System (IDS/IPS) deployed and (automatically configured) to identify and log attacks against wireless networks deployed in the environment and:
- detect and prevent rogue APs in real time
- automatically prevent connections to "evil twin"  APs 
- misconfigure APs such as private SSIDs without encryption
### Answer:
No

---
### Question:
If signature-based, how frequent are signatures updated on IDS/IPS sensors?
### Answer:
No

---
### Question:
Are Web connection alerts inspected (on an exception basis) by the network team within the (system of record) for data loss protection (DLP) and malware protection?
### Answer:
Yes

---
### Question:
Where are firewalls (physical or virtual) deployed across the network architecture?
### Answer:
Cloudflare
AWS Security Group
AWS NACL (Network Access Control Lists)

---
### Question:
Are they deployed on all externally facing connections?
### Answer:
Yes

---
### Question:
How frequently does your organization conduct firewall reviews to address the accuracy and relevance of firewall rules?
### Answer:
Quarterly

---
### Question:
Does your organization implement externally facing network segments, or demilitarized zones (DMZs), for its internet facing systems to limit external connections to secure zones containing Manulife/John Hancock data?
### Answer:
Yes

---
### Question:
Is access to the network perimeter and remote access to the network restricted to designated personnel?
### Answer:
Yes

---
### Question:
Is network activity logged and monitored by a security team or security operations center?
### Answer:
Yes

---
### Question:
Does your organization's external DNS and Remote Platform Owner periodically define and review a list of important events that represent attack, compromise or abusive behavior, within the system?
### Answer:
Yes

---
### Question:
Is your organization's network configured to automatically detect and block unauthorized network access (i.e. including wired, wireless & remote access)?
### Answer:
Yes

---
### Question:
Is an information security management system defined, maintained and monitored to ensure the privacy and security of assets? ie. the information owner must approve (within a system of record) the transfer of confidential or highly confidential information to a non-production system, along with the masking technique to be used, prior to any masking or transfer of the information.
### Answer:
Yes

---
### Question:
How does your organization ensure that Internal, Confidential, or Highly Confidential Information is not stored in demilitarized zones (DMZs)?
### Answer:
We have private subnet for Internal, Confidential or Highly Confidential Information

---
### Question:
Does your organization allow and have a BYOD (permitting employees to bring personal devices and use the devices to access Manulife/John Hancock data) policy/plan?
### Answer:
No

---
### Question:
Has your organization implemented processes and tools to secure mobile devices and wireless networks?
### Answer:
N/A

---
### Question:
Is VPN used to access into network from these devices?
### Answer:
Yes

---
### Question:
Does your organization document, maintain and review network diagrams annually?
### Answer:
Yes

---
### Question:
Does your organization enforce the use of WPA2 wireless encryption?
### Answer:
Yes

---
### Question:
Is the guest wireless network segmented from the corporate and production environments where Manulife/John Hancock data is stored?
### Answer:
No

---
### Question:
Do policies and procedures describe permissible secure methods for receiving and transmitting client data into and outside of your organization (e.g., email, secure file transfer protocol (SFTP)) including use of encryption?
### Answer:
Yes