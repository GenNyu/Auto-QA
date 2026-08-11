### E. Structured Output của Appendix A3
**Sub-appendix:** `A3.2.2.1`
**Defined Approach Requirements:** Upon completion of a change, all relevant PCI DSS requirements are confirmed to be implemented on all new or changed systems and networks, and documentation is updated as applicable. 
PCI DSS Reference : Scope of PCI DSS Requirements; Requirement 1-12 
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Defined Approach Testing Procedures:**
- `A3.2.2.1`: Examine change records and the systems/networks, and interview personnel to verify that all relevant PCI DSS requirements affected were confirmed to be implemented and documentation updated as part of the change.
**Guidance - Purpose:** It is important to have processes to analyze all changes made to systems or networks, to ensure that all appropriate PCI DSS controls are applied to any systems or networks added to the in-scope environment due to a change. Building this validation into change management processes helps ensure that device inventories and configuration standards are kept up to date, and security controls are applied where needed
**Guidance - Good Practice:** A change management process should include supporting evidence that PCI DSS requirements are implemented or preserved through an iterative process
**Guidance - Examples:** PCI DSS requirements that should be verified include, but are not limited to: • Network diagrams are updated to reflect changes. 
• Systems are configured per configuration standards, with all default passwords changed and unnecessary services disabled. 
• Systems are protected with required controls-for example, file integrity monitoring, antimalware, patches, and audit logging. 
• Sensitive authentication data is not stored, and all account data storage is documented and incorporated into data-retention policy and procedures. 
• New systems are included in the quarterly vulnerability scanning process

---
**Sub-appendix:** `A3.2.3`
**Defined Approach Requirements:** Changes to organizational structure result in a formal (internal) review of the impact to PCI DSS scope and applicability of controls. PCI DSS Reference : Requirement 12
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Defined Approach Testing Procedures:**
- `A3.2.3`: Examine policies and procedures to verify that a change to organizational structure results in formal a review of the impact on PCI DSS scope and applicability of controls.
**Guidance - Purpose:** An organization's structure and management define the requirements and protocol for effective and secure operations. Changes to this structure could have negative effects to existing controls and frameworks by reallocating or removing resources that once supported PCI DSS controls or inheriting new responsibilities that may not have established controls in place. Therefore, it is important to revisit PCI DSS scope and controls when there are changes to an organization's structure and management to ensure controls are in place and active
**Guidance - Examples:** Changes to organizational structure include, but are not limited to, company mergers or acquisitions, and significant changes or reassignments of personnel with responsibility for security control

---
**Sub-appendix:** `A3.2.4`
**Defined Approach Requirements:** If segmentation is used, PCI DSS scope is confirmed as follows:
• Per the entity’s methodology defined at Requirement 11.4.1.
• Penetration testing is performed on segmentation controls at least once every six months and after any changes to segmentation controls/methods.
• The penetration testing covers all segmentation controls/methods in use.
• The penetration testing verifies that segmentation controls/methods are operational and effective, and isolate the CDE from all out- of-scope systems.
PCI DSS Reference: Requirement 11
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Defined Approach Testing Procedures:**
- `A3.2.4`: Examine the results from the most recent penetration test to verify that the test was conducted in accordance with all elements specified in this requirement.
**Guidance - Purpose:** PCI DSS normally requires segmentation controls to be verified by penetration testing every twelve
months. Validating segmentation controls more frequently is likely to discover failings in segmentation before they can be exploited by an attacker attempting to pivot laterally from an out-of-scope untrusted network to the CDE.
**Guidance - Good Practice:** Although the requirement specifies that this scope validation is carried out at least once every six months and after a significant change, this exercise should be performed as frequently as possible to ensure it remains effective at isolating the CDE from other networks.
**Guidance - Further Information:** Refer to Information Supplement: Penetration Testing Guidance for additional guidance.

---
**Sub-appendix:** `A3.2.5`
**Defined Approach Requirements:** A data-discovery methodology is implemented that: 
• Confirms PCI DSS scope. 
• Locates all sources and locations of cleartext PAN at least once every three months and upon significant changes to the CDE or processes. 
• Addresses the potential for cleartext PAN to reside on systems and networks outside the currently defined CDE. 
PCI DSS Reference : Scope of PCI DSS Requirements 
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Defined Approach Testing Procedures:**
- `A3.2.5.a`: Examine the documented data-discovery methodology to verify it includes all elements specified in this requirement.
- `A3.2.5.b`: Examine results from recent data discovery efforts, and interview responsible personnel to verify that data discovery is performed at least once every three months and upon significant changes to the CDE or processes.
**Guidance - Purpose:** PCI DSS requires that, as part of the scoping exercise, assessed entities must identify and document the existence of all cleartext PAN in their environments. Implementing a data- discovery methodology that identifies all sources and locations of cleartext PAN and looks for cleartext PAN on systems and networks outside the currently defined CDE or in unexpected places within the defined CDE-for example, in an error log or memory dump file- helps to ensure that previously unknown locations of cleartext PAN are detected and properly secured
**Guidance - Examples:** A data-discovery process can be performed via a variety of methods, including, but not limited to 1) commercially available data-discovery software, 2) an in-house developed data-discovery program, or 3) a manual search. A combination of methodologies may also be used as needed. Regardless of the method used, the goal of the effort is to find all sources and locations of cleartext PAN (not just in the defined CDE)

---
**Sub-appendix:** `A3.2.5.1`
**Defined Approach Requirements:** Data discovery methods are confirmed as follows: 
• Effectiveness of methods is tested. 
• Methods are able to discover cleartext PAN on all types of system components and file formats in use. 
• The effectiveness of data-discovery methods is confirmed at least once every 12 months. 
PCI DSS Reference : Scope of PCI DSS Requirements 
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Defined Approach Testing Procedures:**
- `A3.2.5.1.a`: Interview personnel and review documentation to verify: 
• The entity has a process in place to test the effectiveness of methods used for data discovery. 
• The process includes verifying the methods are able to discover cleartext PAN on all types of system components and file formats in use.
- `A3.2.5.1.b`: Examine the results of effectiveness tests to verify that the effectiveness of data- discovery methods is confirmed at least once every 12 months.
**Guidance - Purpose:** A process to test the effectiveness of the methods used for data discovery ensures the completeness and accuracy of account data detection
**Guidance - Good Practice:** For completeness, system components in the in- scope networks, and systems in out-of-scope networks, should be included in the data- discovery process. The data-discovery process should be effective on all operating systems and platforms in use. Accuracy can be tested by placing test PANs on system components and file formats in use and confirming that the data-discovery method detected the test PANs