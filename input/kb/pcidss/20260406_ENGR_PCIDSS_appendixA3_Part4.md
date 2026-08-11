### E. Structured Output của Appendix A3
**Sub-appendix:** `A3.2.5.2`
**Defined Approach Requirements:** Response procedures are implemented to be initiated upon the detection of cleartext PAN outside the CDE to include: 
• Determining what to do if cleartext PAN is discovered outside the CDE, including its retrieval, secure deletion, and/or migration into the currently defined CDE, as applicable. 
• Determining how the data ended up outside the CDE. 
• Remediating data leaks or process gaps that resulted in the data being outside the CDE. 
 Identifying the source of the data. 
 • Identifying whether any track data is stored with the PANs
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Defined Approach Testing Procedures:**
- `A3.2.5.2.a`: Examine documented response procedures to verify that procedures for responding to the detection of cleartext PAN outside the CDE are defined and include all elements specified in this requirement.
- `A3.2.5.2.b`: Interview personnel and examine records of response actions to verify that remediation activities are performed when cleartext PAN is detected outside the CDE.
**Guidance - Purpose:** Having documented response procedures that are followed in the event cleartext PAN is found outside the CDE helps to identify the necessary remediation actions and prevent future leaks
**Guidance - Good Practice:** If PAN was found outside the CDE, an analysis should be performed to 1) determine whether it was saved independently of other data or with sensitive authentication data, 2) to identify the source of the data, and 3) identify the control gaps that resulted in the data being outside the CDE. Entities should consider whether contributory factors, such as business processes, user behavior, improper system configurations, etc., caused the PAN to be stored in an unexpected location. If such contributory factors are present, they should be addressed per this Requirement to prevent a recurrence

---
**Sub-appendix:** `A3.2.6`
**Defined Approach Requirements:** Mechanisms are implemented for detecting and preventing cleartext PAN from leaving the CDE via an unauthorized channel, method, or process, including mechanisms that are: 
• Actively running. 
• Configured to detect and prevent cleartext PAN leaving the CDE via an unauthorized channel, method, or process. 
• Generating audit logs and alerts upon detection of cleartext PAN leaving the CDE via an unauthorized channel, method, or process. 
PCI DSS Reference : Scope of PCI DSS Requirements, Requirement 12
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Defined Approach Testing Procedures:**
- `A3.2.6.a`: Examine documentation and observe implemented mechanisms to verify that the mechanisms are in accordance with all elements specified in this requirement.
- `A3.2.6.b`: Examine audit logs and alerts, and interview responsible personnel to verify that alerts are investigated.
**Guidance - Purpose:** The use of mechanisms to detect and prevent unauthorized PAN from leaving the CDE allows an organization to detect and prevent situations that may lead to data loss
**Guidance - Good Practice:** Coverage of the mechanisms should include, but not be limited to, e-mails, downloads to removable media, and output to printers
**Guidance - Examples:** Mechanisms to detect and prevent unauthorized loss of cleartext PAN may include the use of appropriate tools such as data loss prevention (DLP) solutions as well as manual processes and procedures

---
**Sub-appendix:** `A3.2.6.1`
**Defined Approach Requirements:** Response procedures are implemented to be initiated upon the detection of attempts to remove cleartext PAN from the CDE via an unauthorized channel, method, or process. Response procedures include: 
• Procedures for the prompt investigation of alerts by responsible personnel. 
• Procedures for remediating data leaks or process gaps, as necessary, to prevent any data loss. 
PCI DSS Reference : Requirement 12
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Defined Approach Testing Procedures:**
- `A3.2.6.1.a`: Examine documented response procedures to verify that procedures for responding to the attempted removal of cleartext PAN from the CDE via an unauthorized channel, method, or process include all elements specified in this requirement: 
• Procedures for the prompt investigation of alerts by responsible personnel. 
• Procedures for remediating data leaks or process gaps, as necessary, to prevent any data loss.
- `A3.2.6.1.b`: Interview personnel and examine records of actions taken when cleartext PAN is detected leaving the CDE via an unauthorized channel, method, or process and verify that remediation activities were performed.
**Guidance - Purpose:** Attempts to remove cleartext PAN via an unauthorized channel, method, or process may indicate malicious intent to steal data, or may be the actions of an authorized employee who is unaware of or simply not following the proper methods. Prompt investigation of these occurrences can identify where remediation needs to be applied and provides valuable information to help understand from where the threats are coming

---
**Sub-appendix:** `A3.3.1`
**Defined Approach Requirements:** Failures of critical security control systems are detected, alerted, and addressed promptly, including but not limited to failure of: 
• Network security controls 
• IDS/IPS • FIM • Anti-malware solutions 
• Physical access controls 
• Logical access controls 
• Audit logging mechanisms 
• Segmentation controls (if used) 
• Automated audit log review mechanisms. This bullet is a best practice until its effective date; refer to Applicability Notes below for details. 
• Automated code review tools (if used). This bullet is a best practice until its effective date; refer to Applicability Notes below for details. 
PCI DSS Reference : Requirements 1-12 
**Customized Approach Objective:** This requirement is not eligible for the customized
**Applicability Notes:** The bullets above (for automated log review mechanisms and automated code review tools (if used)) are best practices until 31 March 2025, after which they will be required as part of Requirement A3.3.1 and must be fully considered during a PCI DSS assessment
**Defined Approach Testing Procedures:**
- `A3.3.1.a`: Examine documented policies and procedures to verify that processes are defined to promptly detect, alert, and address critical security control failures in accordance with all elements specified in this requirement.
- `A3.3.1.b`: Examine detection and alerting processes, and interview personnel to verify that processes are implemented for all critical security controls specified in this requirement and that each failure of a critical security control results in the generation of an alert.
**Guidance - Purpose:** Without formal processes for the prompt (as soon as possible) detection, alerting, and addressing of critical security control failures, failures may go undetected or remain unresolved for extended periods. In addition, without formalized time- bound processes, attackers will have ample time to compromise systems and steal account data from the CDE
**Guidance - Good Practice:** The specific types of failures may vary, depending on the function of the device system component and technology in use. Typical failures include a system ceasing to perform its security function or not functioning in its intended manner, such as a firewall erasing all its rules or going offline

---
**Sub-appendix:** `A3.3.1.1`
**Defined Approach Requirements:** Failures of any critical security control systems are responded to promptly. Processes for responding to failures in security control systems include: 
• Restoring security functions. 
• Identifying and documenting the duration (date and time from start to end) of the security failure. 
• Identifying and documenting the cause(s) of failure, including root cause, and documenting remediation required to address the root cause. 
• Identifying and addressing any security issues that arose during the failure. 
• Determining whether further actions are required as a result of the security failure. 
• Implementing controls to prevent the cause of failure from reoccurring. 
• Resuming monitoring of security controls. 
PCI DSS Reference : Requirements 1-12 Customized Approach Objective
**Defined Approach Testing Procedures:**
- `A3.3.1.1.a`: Examine documented policies and procedures and interview personnel to verify processes are defined and implemented to respond promptly to a security control failure in accordance with all elements specified in this requirement.
- `A3.3.1.1.b`: Examine records to verify that security control failures are documented to include: 
• Identification of cause(s) of the failure, including root cause. 
• Duration (date and time start and end) of the security failure. 
• Details of the remediation required to address the root cause.
**Guidance - Purpose:** If alerts from failures of critical security control systems are not responded to quickly and effectively, attackers may use this time to insert malicious software, gain control of a system, or steal data from the entity's environment
**Guidance - Good Practice:** Documented evidence (for example, records within a problem management system) should support processes and procedures in place that respond to security failures. In addition, personnel should be aware of their responsibilities in the event of a failure. Actions and responses to the failure should be captured in the documented evidence