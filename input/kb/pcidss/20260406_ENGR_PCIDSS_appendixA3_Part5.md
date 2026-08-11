### E. Structured Output của Appendix A3
**Sub-appendix:** `A3.3.2`
**Defined Approach Requirements:** Hardware and software technologies are reviewed at least once every 12 months to confirm whether they continue to meet the organization's PCI DSS requirements. PCI DSS Reference : Requirements 2, 6, 12
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Applicability Notes:** The process includes a plan for remediating technologies that no longer meet the organization's PCI DSS requirements, up to and including replacement of the technology, as appropriate
**Defined Approach Testing Procedures:**
- `A3.3.2.a`: Examine documented policies and procedures and interview personnel to verify processes are defined and implemented to review hardware and software technologies to confirm whether they continue to meet the organization's PCI DSS requirements.
- `A3.3.2.b`: Review the results of the recent reviews of hardware and software technologies to verify reviews are performed at least once every 12 months.
- `A3.3.2.c`: Review documentation to verify that, for any technologies that have been determined to no longer meet the organization's PCI DSS requirements, a plan is in place to remediate the technology.
**Guidance - Purpose:** Hardware and software technologies are constantly evolving, and organizations need to be aware of changes to the technologies they use, as well as the evolving threats to those technologies. Conducting appropriate reviews of these technologies ensures that they can prepare for, and manage, vulnerabilities in hardware and software that will not be remediated by the vendor or developer
**Guidance - Good Practice:** Organizations should also consider reviewing firmware versions to ensure they remain current and supported by the vendors. Organizations also need to be aware of changes made by technology vendors to their products or processes to understand how such changes may impact the organization's use of the technology. Regular reviews of technologies that impact or influence PCI DSS controls can assist with purchasing, usage, and deployment strategies and ensure controls that rely on those technologies remain effective. These reviews include, but are not limited to, reviewing technologies that are no longer supported by the vendor and/or no longer meet the security needs of the organization

---
**Sub-appendix:** `A3.3.3`
**Defined Approach Requirements:** Reviews are performed at least once every three months to verify BAU activities are being followed. Reviews are performed by personnel assigned to the PCI DSS compliance program (as identified in A3.1.3), and include:
• Confirmation that all BAU activities, including A3.2.2, A3.2.6, and A3.3.1, are being performed.
• Confirmation that personnel are following security policies and operational procedures (for example, daily log reviews, ruleset reviews for network security controls, configuration standards for new systems).
• Documenting how the reviews were completed, including how all BAU activities were verified as being in place. 
• Collection of documented evidence as required for the annual PCI DSS assessment.
• Review and sign-off of results by personnel assigned responsibility for the PCI DSS compliance program, as identified in A3.1.3.
• Retention of records and documentation for at least 12 months, covering all BAU activities.
PCI DSS Reference : Requirements 1-12
**Defined Approach Testing Procedures:**
- `A3.3.3.a`: Examine policies and procedures to verify that processes are defined for reviewing and verifying BAU activities in accordance with all elements specified in this requirement.
- `A3.3.3.b`: Interview responsible personnel and examine records of reviews to verify that: 
• Reviews are performed by personnel assigned to the PCI DSS compliance program. 
• Reviews are performed at least once every three months.
**Guidance - Purpose:** Regularly confirming that security policies and procedures are being followed provides assurance that the expected controls are active and working as intended. The objective of these reviews is not to reperform other PCI DSS requirements, but to confirm that security activities are being performed on an ongoing basis
**Guidance - Good Practice:** These reviews can also be used to verify that appropriate evidence is being maintained-for example, audit logs, vulnerability scan reports, reviews of network security control rulesets-to assist in the entity's preparation for its next PCI DSS assessment
**Guidance - Examples:** Looking at Requirement 1.2.7 as one example, Requirement A3.3.3 is met by confirming, at least once every three months, that reviews of configurations of network security controls have occurred at the required frequency. On the other hand, Requirement 1.2.7 is met by reviewing those configurations as specified in the requirement

---
**Sub-appendix:** `A3.4.1`
**Defined Approach Requirements:** User accounts and access privileges to in- scope system components are reviewed at least once every six months to ensure user accounts and access privileges remain appropriate based on job function, and that all access is authorized. PCI DSS Reference : Requirement 7
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Defined Approach Testing Procedures:**
- `A3.4.1`: Interview responsible personnel and examine supporting documentation to verify that: 
• User accounts and access privileges are reviewed at least every six months. 
• Reviews confirm that access is appropriate based on job function and that all access is authorized.
**Guidance - Purpose:** Regular review of access rights helps to detect excessive access rights remaining after user job responsibilities change, system functions change, or other modifications. If excessive user rights are not revoked in due time, they may be used by malicious users for unauthorized access. This review provides another opportunity to ensure that accounts for all terminated users have been removed (if any were missed at the time of termination), as well as to ensure that any third parties that no longer need access have had their access terminated

---
**Sub-appendix:**** `A3.5.1`
**Defined Approach Requirements:** A methodology is implemented for the prompt identification of attack patterns and undesirable behavior across systems that includes: 
• Identification of anomalies or suspicious activity as it occurs. 
• Issuance of prompt alerts upon detection of suspicious activity or anomaly to responsible personnel. 
• Response to alerts in accordance with documented response procedures. 
PCI DSS Reference : Requirements 10, 12 
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Defined Approach Testing Procedures:**
- `A3.5.1.a`: Examine documentation and interview personnel to verify a methodology is defined and implemented to identify attack patterns and undesirable behavior across systems in a prompt manner, and includes all elements specified in this requirement.
- `A3.5.1.b`: Examine incident response procedures and interview responsible personnel to verify that: 
• On-call personnel receive prompt alerts. 
• Alerts are responded to per documented response procedures.
**Guidance - Purpose:** The ability to identify attack patterns and undesirable behavior across systems-for example, using centrally managed or automated log-correlation tools- is critical in preventing, detecting, or minimizing the impact of a data compromise. The presence of logs in all environments allows thorough tracking, alerting, and analysis when something goes wrong. Determining the cause of a compromise is very difficult, if not impossible, without a process to corroborate information from critical system components and systems that perform security functions, such as network security controls, IDS/IPS, and file integrity monitoring (FIM) systems. Thus, logs for all critical system components and systems that perform security functions need to be collected, correlated, and maintained. This could include using software products and service methodologies to provide real-time analysis, alerting, and reporting, such as security information and event management (SIEM), FIM, or change detection