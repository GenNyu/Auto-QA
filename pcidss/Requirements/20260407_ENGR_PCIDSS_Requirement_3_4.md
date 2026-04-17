### A. Tài liệu gốc của Requirement 3

### B. Summary Overview của Requirement 3
Tài liệu này mô tả chi tiết **Control Objective 3.4 **của** Requirement 3** trong **PCI-DSS v4.0.1**, tập trung vào việc hạn chế hiển thị và kiểm soát việc truy cập, sao chép dữ liệu PAN nhằm giảm thiểu rủi ro lộ dữ liệu.
Mục tiêu chính là đảm bảo PAN chỉ được hiển thị ở mức tối thiểu cần thiết và không bị sao chép hoặc di chuyển trái phép, đặc biệt trong các môi trường truy cập từ xa.
Gồm 2 sub-requirement chính:
- 3.4.1: Masking PAN khi hiển thị
- 3.4.2: Kiểm soát sao chép/di chuyển PAN qua remote access
Áp dụng cho tất cả các hình thức hiển thị PAN (màn hình, in ấn, báo cáo) và các công nghệ truy cập từ xa có khả năng truy cập hoặc thao tác với PAN.

### C. Key Points của Control Objective 3.4
- **Phạm vi áp dụng:**Tất cả nơi hiển thị PAN và môi trường remote access
- **Trách nhiệm:** Tài liệu hóa role, phân rõ quyền truy cập PAN đầy đủ
- **Kiểm soát hiển thị:**PAN phải được masking (tối đa BIN + last 4)
- **Phân quyền:**Chỉ role có business need mới được xem full PAN
- **Kiểm soát kỹ thuật:** Ngăn chặn copy/relocate PAN qua remote access
- **Danh sách quyền:** Phải duy trì danh sách user/role được phép truy cập hoặc thao tác PAN

### D. Deep Summary của Control Objective 3.4
**Bối cảnh:**Việc hiển thị hoặc sao chép PAN không kiểm soát là nguyên nhân phổ biến dẫn đến rò rỉ dữ liệu và gian lận thẻ. Các kênh hiển thị và remote access là điểm dễ bị khai thác.
**Nội dung cốt lõi:**
- Masking PAN khi hiển thị, chỉ hiển thị tối đa BIN + 4 số cuối
- Chỉ cho phép hiển thị full PAN với role có business need rõ ràng
- Áp dụng kiểm soát truy cập theo role
- Ngăn chặn copy/relocate PAN trong môi trường remote access
- Chỉ cho phép thao tác PAN khi có explicit authorization
**Dữ liệu đáng chú ý:**
- Masking ≠ truncation (masking có thể unmask, truncation thì không)
- Remote access bao gồm VDI, remote desktop, cloud session
**Rủi ro / Lưu ý:**
- Hiển thị full PAN không kiểm soát → rò rỉ dữ liệu
- Không kiểm soát remote access → dễ bị copy ra local hoặc thiết bị ngoài
- Thiếu phân quyền rõ ràng → user xem dữ liệu vượt nhu cầu
- Lưu PAN trên thiết bị local → mở rộng scope PCI DSS không cần thiết

### E. Structured Output của Requirement 3
**Control objectives:**3.4
**Sub-requirement:**3.4.1 *(Tag: PAN masking, data masking, display protection, least privilege, BIN + last4)*
**Defined Approach Requirements of 3.4.1:**PAN is masked when displayed (the BIN and last four digits are the maximum number of digits to be displayed), such that only personnel with a legitimate business need can see more than the BIN and last four digits of the PAN.
**Defined Approach Testing Procedures of 3.4.1:**
- "3.4.1.a": Examine documented policies and procedures for masking the display of PANs to verify:
• A list of roles that need access to more than the BIN and last four digits of the PAN (includes full PAN) is documented, together with a legitimate business need for each role to have such access.
• PAN is masked when displayed such that only personnel with a legitimate business need can see more than the BIN and last four digits of the PAN.
• All roles not specifically authorized to see the full PAN must only see masked PANs.
- "3.4.1.b": Examine system configurations to verify that full PAN is only displayed for roles with a documented business need, and that PAN is masked for all other requests.
- "3.4.1.c": Examine displays of PAN (for example, on screen, on paper receipts) to verify that PANs are masked when displayed, and that only those with a legitimate business need are able to see more than the BIN and/or last four digits of the PAN.
**Customized Approach Objective of 3.4.1:**PAN displays are restricted to the minimum number of digits necessary to meet a defined business need.
**Applicability Notes of 3.4.1:**This requirement does not supersede stricter requirements in place for displays of cardholder data- for example, legal or payment brand requirements for point-of-sale (POS) receipts. This requirement relates to protection of PAN where it is displayed on screens, paper receipts, printouts, etc., and is not to be confused with Requirement 3.5.1 for protection of PAN when stored, processed, or transmitted.
**Guidance - Purpose of 3.4.1:**The display of full PAN on computer screens, payment card receipts, paper reports, etc. can result in this data being obtained by unauthorized individuals and used fraudulently. Ensuring that the full PAN is displayed only for those with a legitimate business need minimizes the risk of unauthorized persons gaining access to PAN data.
**Guidance - Good Practice of 3.4.1:**Applying access controls according to defined roles is one way to limit access to viewing full PAN to only those individuals with a defined business need. The masking approach should always display only the number of digits needed to perform a specific business function. For example, if only the last four digits are needed to perform a business function, PAN should be masked to only show the last four digits. As another example, if a function needs to view the bank identification number (BIN) for routing purposes, unmask only the BIN digits for that function.
**Guidance - Definitions of 3.4.1:**Masking is not synonymous with truncation and these terms cannot be used interchangeably. Masking refers to the concealment of certain digits during display or printing, even when the entire PAN is stored on a system. This is different from truncation, in which the truncated digits are removed and cannot be retrieved within the system. Masked PAN could be 'unmasked', but there is no "un-truncation" without recreating the PAN from another source. Refer to Appendix G for definitions of 'masking' and 'truncation.'
**Guidance - Further Information of 3.4.1:**For more information about masking and truncation, see PCI SSC's FAQs on these topics.

---
**Control objectives:**3.4
**Sub-requirement:**3.4.2 *(Tag: PAN exfiltration prevention, remote access control, data leakage prevention, endpoint control)*
**Defined Approach Requirements of 3.4.2:**When using remote-access technologies, technical controls prevent copy and/or relocation of PAN for all personnel, except for those with documented, explicit authorization and a legitimate, defined business need.
**Defined Approach Testing Procedures of 3.4.2:**
- "3.4.2.a": Examine documented policies and procedures and documented evidence for technical controls that prevent copy and/or relocation of PAN when using remote-access technologies onto local hard drives or removable electronic media to verify the following:
• Technical controls prevent all personnel not specifically authorized from copying and/or relocating PAN.
• A list of personnel with permission to copy and/or relocate PAN is maintained, together with the documented, explicit authorization and legitimate, defined business need.
- "3.4.2.b": Examine configurations for remote-access technologies to verify that technical controls to prevent copy and/or relocation of PAN for all personnel, unless explicitly authorized.
- "3.4.2.c": Observe processes and interview personnel to verify that only personnel with documented, explicit authorization and a legitimate, defined business need have permission to copy and/or relocate PAN when using remote-access technologies.
**Customized Approach Objective of 3.4.2:**PAN cannot be copied or relocated by unauthorized personnel using remote-access technologies.
**Applicability Notes of 3.4.2:**Storing or relocating PAN onto local hard drives, removable electronic media, and other storage devices brings these devices into scope for PCI DSS. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment.
**Guidance - Purpose of 3.4.2:**Relocation of PAN to unauthorized storage devices is a common way for this data to be obtained and used fraudulently. Methods to ensure that only those with explicit authorization and a legitimate business reason can copy or relocate PAN minimizes the risk of unauthorized persons gaining access to PAN.
**Guidance - Good Practice of 3.4.2:**Copying and relocation of PAN should only be done to storage devices that are permissible and authorized for that individual.
**Guidance - Definitions of 3.4.2:**A virtual desktop is an example of a remote-access technology. Such remote access technologies often include tools to disable copy and/or relocation functionality. Storage devices include, but are not limited to, local hard drives, virtual drives, removable electronic media, network drives, and cloud storage.
**Guidance - Further Information of 3.4.2:**Vendor documentation for the remote-access technology in use will provide information about the system settings needed to implement this requirement.