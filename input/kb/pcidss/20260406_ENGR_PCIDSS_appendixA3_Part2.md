### E. Structured Output của Appendix A3
**Sub-appendix:** `A3.1.4`
**Defined Approach Requirements:** Up-to-date PCI DSS and/or information security training is provided at least once every 12 months to personnel with PCI DSS compliance responsibilities (as identified in A3.1.3). 
PCI DSS Reference : Requirement 12
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Defined Approach Testing Procedures:**
- `A3.1.4.a`: Examine information security policies and procedures to verify that PCI DSS and/or information security training is required at least once every 12 months for each role with PCI DSS compliance responsibilities.
- `A3.1.4.b`: Interview personnel and examine certificates of attendance or other records to verify that personnel with PCI DSS compliance responsibility receive up-to-date PCI DSS and/or similar information security training at least once every 12 months.
**Guidance - Purpose:** Personnel responsible for PCI DSS compliance have specific training needs exceeding that which is typically provided by general security awareness training to enable them to perform their role
**Guidance - Good Practice:** Individuals with PCI DSS compliance responsibilities should receive specialized training that, in addition to a general awareness of information security, focuses on specific security topics, skills, processes, or methodologies that must be followed for those individuals to perform their compliance responsibilities effectively. Training may be offered by third parties such as the PCI SSC (for example, PCI Awareness, PCIP, and ISA), payment brands, and acquirers, or training may be internal. Training content should be applicable for the individual's job function, be current, and include the latest security threats and/or version of PCI DSS
**Guidance - Further Information:** For additional guidance, refer to Information Supplement: Best Practices for Implementing a Security Awareness Program A3.2 PCI DSS scope is documented and validated.

---
**Sub-appendix:** `A3.2.1`
**Defined Approach Requirements:** PCI DSS scope is documented and confirmed for accuracy at least once every three months and upon significant changes to the in- scope environment. At a minimum, the scoping validation includes: 
• Identifying all data flows for the various payment stages (for example, authorization, capture, settlement, chargebacks, and refunds) and acceptance channels (for example, card- present, card-not-present, and e-commerce). 
• Updating all data-flow diagrams per Requirement 1.2.4. 
• Identifying all locations where account data is stored, processed, and transmitted, including but not limited to 1) any locations outside of the currently defined CDE, 2) applications that process CHD, 3) transmissions between systems and networks, and 4) file backups. 
• For any account data found outside of the currently defined CDE, either 1) securely delete it, 2) migrate it into the currently defined CDE, or 3) expand the currently defined CDE to include it. 
• Identifying all system components in the CDE, connected to the CDE, or that could impact security of the CDE. 
• Identifying all segmentation controls in use and the environment(s) from which the CDE is segmented, including justification for environments being out of scope
• Identifying all connections to third-party entities with access to the CDE.
• Confirming that all identified data flows, account data, system components, segmentation controls, and connections from third parties with access to the CDE are included in scope.
PCI DSS Reference: Scope of PCI DSS Requirements, Requirement 12.
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Defined Approach Testing Procedures:**
- `A3.2.1.a`: Examine documented results of scope reviews and interview personnel to verify that the reviews are performed: 
• At least once every three months. 
• After significant changes to the in-scope environment.
- `A3.2.1.b`: Examine documented results of scope reviews occurring at least once every three months to verify that scoping validation includes all elements specified in this requirement. 
**Guidance - Purpose:** Frequent validation of PCI DSS scope helps to ensure PCI DSS scope remains up to date and aligned with changing business objectives, and therefore that security controls are protecting all appropriate system components
**Guidance - Good Practice:** Accurate scoping involves critically evaluating the CDE and all connected system components to determine the necessary coverage for PCI DSS requirements. Scoping activities, including careful analysis and ongoing monitoring, help to ensure that in-scope systems are appropriately secured. When documenting account data locations, the entity can consider creating a table or spreadsheet that includes the following information: • Data stores (databases, files, cloud, etc.), including purpose of data storage and the retention period, • Which CHD elements are stored (PAN, expiry date, cardholder name, and/or any elements of SAD prior to completion of authorization), • How data is secured (type of encryption and strength, hashing algorithm and strength, truncation, tokenization), • How access to data stores is logged, including a description of logging mechanism(s) in use (enterprise solution, application level, operating system level, etc.).
In addition to internal systems and networks, all connections from third-party entities-for example, business partners, entities providing remote support services, and other service providers-need to be identified to determine inclusion for PCI DSS scope. Once the in-scope connections have been identified, the applicable PCI DSS controls can be implemented to reduce the risk of a third-party connection being used to compromise an entity's CDE. A data discovery tool or methodology can be used to facilitate identifying all sources and locations of PAN, and to look for PAN that resides on systems and networks outside the currently defined CDE or in unexpected places within the defined CDE- for example, in an error log or memory dump file. This approach can help ensure that previously unknown locations of PAN are detected and that the PAN is either eliminated or properly secured. 
**Further Information:** Refer to Information Supplement: Guidance for PCI DSS Scoping and Network Segmentation for additional guidance.

---
**Sub-appendix:** `A3.2.2`
**Defined Approach Requirements:** PCI DSS scope impact for all changes to systems or networks is determined, including additions of new systems and new network connections. Processes include: 
• Performing a formal PCI DSS impact assessment. 
• Identifying applicable PCI DSS requirements to the system or network. 
• Updating PCI DSS scope as appropriate. 
• Documented sign-off of the results of the impact assessment by responsible personnel (as defined in A3.1.3). 
PCI DSS Reference : Scope of PCI DSS Requirements; Requirements 1-12
**Customized Approach Objective:** This requirement is not eligible for the customized approach
**Defined Approach Testing Procedures:**
- `A3.2.2`: Examine change documentation and interview personnel to verify that for each change to systems or networks the PCI DSS scope impact is determined, and includes all elements specified in this requirement.
**Guidance - Purpose:** Changes to systems or networks can have a significant impact on PCI DSS scope. For example, changes to network security control rulesets can bring whole network segments into scope, or new systems may be added to the CDE that have to be appropriately protected. A formal impact assessment performed in advance of a change gives the entity assurance that the change will not adversely affect the security of the CDE
**Guidance - Good Practice:** Processes to determine the potential impact that changes to systems and networks may have on an entity's PCI DSS scope may be performed as part of a dedicated PCI DSS compliance program or may fall under an entity's overarching compliance and/or governance program