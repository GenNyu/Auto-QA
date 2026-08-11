### A. Tài liệu gốc của Appendix F

### B. Summary Overview của Appendix F
Tài liệu này mô tả chi tiết **Appendix F** trong **PCI-DSS v4.0.1**, tập trung vào việc **tận dụng Khung Bảo mật Phần mềm PCI (Software Security Framework - SSF)** để hỗ trợ thực hiện Yêu cầu 6. 
Mục tiêu chính là giúp các thực thể đáp ứng các yêu cầu về phát triển và duy trì phần mềm an toàn thông qua việc sử dụng các phần mềm được phát triển theo Tiêu chuẩn Phần mềm An toàn (Secure Software Standard) hoặc Tiêu chuẩn Vòng đời Phần mềm An toàn (Secure SLC Standard), từ đó giảm thiểu các thử nghiệm chi tiết bổ sung và hỗ trợ Phương pháp tiếp cận tùy chỉnh cho các yêu cầu khác.
### C. Key Points của Appendix F
- **Đối tượng áp dụng:** Chỉ dành cho phần mềm bespoke (đặt làm riêng) và phần mềm tùy chỉnh được phát triển/duy trì theo các tiêu chuẩn SSF cụ thể.
- **Cơ chế hỗ trợ:** Việc sử dụng phần mềm đạt chuẩn SSF có thể giúp một số mục trong Yêu cầu 6 được coi là "đã thực hiện" (in place) mà không cần kiểm tra thêm.
- **Phân định trách nhiệm:** Dù sử dụng phần mềm từ nhà cung cấp đạt chuẩn, thực thể vẫn chịu trách nhiệm cài đặt bản vá và quản lý thay đổi khi triển khai vào môi trường vận hành.
- **Yêu cầu đối với đánh giá viên:** Phải xác nhận trạng thái niêm yết của nhà cung cấp trên PCI SSC, các thực hành vòng đời phần mềm đã được đánh giá và việc tuân thủ hướng dẫn triển khai.
- **Thời hạn và chứng thực:** Đánh giá SSF đầy đủ có giá trị trong 36 tháng, nhưng yêu cầu Chứng thực hàng năm (Annual Attestation) nếu đánh giá đầy đủ đã quá 12 tháng.
### D. Deep Summary của Appendix F
**Bối cảnh:**
PCI DSS Requirement 6 yêu cầu khắt khe về việc phát triển phần mềm an toàn. Do các tiêu chuẩn SSF của PCI SSC vốn đã bao gồm các yêu cầu bảo mật nghiêm ngặt, Appendix F cung cấp cách thức để các tổ chức tận dụng sự tuân thủ SSF nhằm đáp ứng các yêu cầu của PCI DSS một cách hiệu quả hơn.

**Nội dung cốt lõi:**
Trọng tâm là bảng đối chiếu cách SSF hỗ trợ Requirement 6:
- **Yêu cầu 6.2:** Phần mềm theo chuẩn Secure SLC giúp đáp ứng toàn bộ yêu cầu này; trong khi chuẩn Secure Software đáp ứng cụ thể mục 6.2.4.
- **Hỗ trợ Customized Approach:** Chuẩn Secure SLC hỗ trợ phương pháp tiếp cận tùy chỉnh cho các mục tiêu của Yêu cầu 6.3 (lỗ hổng bảo mật) và 6.5 (quản lý thay đổi).
- **Tài liệu chứng minh:** Cần có đầy đủ Báo cáo Tuân thủ (ROC), Báo cáo Xác thực (ROV) và các Giấy chứng nhận (AOC/AOV) từ các Đánh giá viên SSF chuyên trách.

**Dữ liệu đáng chú ý:**
- Các tổ chức tự phát triển phần mềm nội bộ cũng có thể thuê Đánh giá viên Secure SLC để kiểm tra và nhận được sự hỗ trợ tuân thủ tương tự như khi mua phần mềm từ bên ngoài.
- Nhà cung cấp phải duy trì tên trong danh sách **Secure SLC Qualified Vendors** của PCI SSC để các chứng chỉ còn hiệu lực hỗ trợ.
- Mọi thực hành quản lý vòng đời phải được xác nhận là đã nằm trong phạm vi đánh giá SSF trước đó.

**Rủi ro / Lưu ý:**
- **Không áp dụng rộng rãi:** Sự hỗ trợ này **chỉ giới hạn** cho phần mềm đạt chuẩn, không áp dụng cho các thành phần hệ thống khác trong phạm vi Yêu cầu 6.
- **Trách nhiệm thực thi:** Việc nhà cung cấp tuân thủ SSF không thay thế trách nhiệm của thực thể trong việc đảm bảo phần mềm được triển khai và cập nhật an toàn trong môi trường sản xuất của chính họ.
- **Hết hạn xác thực:** Nếu đánh giá đầy đủ đã quá 36 tháng hoặc thiếu Chứng thực hàng năm sau 12 tháng, thực thể sẽ không được tận dụng các lợi ích từ phụ lục này.
### E. Structured Output của Appendix F
PCI DSS Requirement 6 defines requirements for the development and maintenance of secure systems and software. Because the PCI SSC Secure Software Standard and the Secure SLC Standard (collectively, the Software Security Framework) include rigorous software security requirements, the use of bespoke and custom software that is developed and maintained in accordance with either standard can help the entity to meet several requirements in PCI DSS Requirement 6 without having to perform additional detailed testing, and may also support use of the Customized Approach for other requirements. For details, see Table 7.

**Note:** This support for meeting Requirement 6 applies only to software that is specifically developed and maintained in accordance with the Secure Software Standard or the Secure SLC Standard; it does not extend to other software or system components in scope for Requirement 6.


#### Table 7. Leveraging the PCI Software Security Framework to Support Requirement 6

---
**PCI DSS Requirements:** 6.1 Processes and mechanisms for performing activities in Requirement 6 are defined and understood.
**How PCI DSS Requirements Apply to Software Developed and Maintained in Accordance with the Secure Software Standard:** PCI DSS requirements/objectives apply as usual.
**How PCI DSS Requirements Apply to Software Developed and Maintained in Accordance with the Secure SLC Standard:** PCI DSS requirements/objectives apply as usual.

---
**PCI DSS Requirements:** 6.2 Bespoke and custom software is developed securely.
**How PCI DSS Requirements Apply to Software Developed and Maintained in Accordance with the Secure Software Standard:** PCI DSS Requirement 6.2.4 can be considered in place for software that is developed and maintained in accordance with the Secure Software Standard.
**How PCI DSS Requirements Apply to Software Developed and Maintained in Accordance with the Secure SLC Standard:** PCI DSS Requirement 6.2 can be considered in place for software that is developed and maintained in accordance with the Secure SLC Standard.

---
**PCI DSS Requirements:** 6.3 Security vulnerabilities are identified and addressed.
**How PCI DSS Requirements Apply to Software Developed and Maintained in Accordance with the Secure Software Standard:** PCI DSS requirements/objectives apply as usual. Software developed and maintained in accordance with the Secure SLC Standard may support the customized approach for Requirement 6.3 objectives. While use of software developed and maintained in accordance with the Secure SLC Standard provides assurance that the vendor makes security patches and software updates available in a timely manner, the entity retains responsibility for ensuring that patches and updates are installed in accordance with PCI DSS requirements.
**How PCI DSS Requirements Apply to Software Developed and Maintained in Accordance with the Secure SLC Standard:** PCI DSS requirements/objectives apply as usual. Software developed and maintained in accordance with the Secure SLC Standard may support the customized approach for Requirement 6.3 objectives. While use of software developed and maintained in accordance with the Secure SLC Standard provides assurance that the vendor makes security patches and software updates available in a timely manner, the entity retains responsibility for ensuring that patches and updates are installed in accordance with PCI DSS requirements.

---
**PCI DSS Requirements:** 6.4 Public-facing web applications are protected against attacks.
**How PCI DSS Requirements Apply to Software Developed and Maintained in Accordance with the Secure Software Standard:** PCI DSS requirements/objectives apply as usual.
**How PCI DSS Requirements Apply to Software Developed and Maintained in Accordance with the Secure SLC Standard:** PCI DSS requirements/objectives apply as usual.

---
**PCI DSS Requirements:** 6.5 Changes to all system components are managed securely.
**How PCI DSS Requirements Apply to Software Developed and Maintained in Accordance with the Secure Software Standard:** PCI DSS requirements/objectives apply as usual. Software developed and maintained in accordance with the Secure SLC Standard may support the customized approach for Requirement 6.5 objectives. While use of software developed and maintained in accordance with the Secure SLC Standard provides assurance that the vendor follows change management procedures during development of software and related updates, the entity retains responsibility for ensuring that software and other changes to system components are implemented into its production environment in accordance with PCI DSS requirements.
**How PCI DSS Requirements Apply to Software Developed and Maintained in Accordance with the Secure SLC Standard:** PCI DSS requirements/objectives apply as usual. Software developed and maintained in accordance with the Secure SLC Standard may support the customized approach for Requirement 6.5 objectives. While use of software developed and maintained in accordance with the Secure SLC Standard provides assurance that the vendor follows change management procedures during development of software and related updates, the entity retains responsibility for ensuring that software and other changes to system components are implemented into its production environment in accordance with PCI DSS requirements.

---
#### Use of Bespoke and Custom Software Developed and Maintained by a Secure SLC Qualified Vendor**
When validating the use of software developed and maintained by a Secure SLC Qualified Vendor to meet PCI DSS Requirement 6.2 and support the Customized Approach for Requirements 6.3 and 6.5, the assessor must confirm that the following is met:
- The software vendor has a current listing on the PCI SSC List of Secure SLC Qualified Vendors—that is, the validation has not expired.
- The software was developed and is being maintained using software lifecycle management practices that were assessed as part of the software vendor’s validation.
- The entity is following the implementation guidance provided by the Secure SLC Qualified Vendor.

#### Use of Bespoke and Custom Software Developed in Accordance with the Secure SLC Standard
Entities that internally develop software solely for their use or that develop software for use by a single entity may choose to engage a Secure SLC Assessor to assess their software lifecycle management practices against the Secure SLC Standard. The Secure SLC Assessor will document the results of the assessment in a Secure SLC Report on Compliance (ROC) and a Secure SLC Attestation of Compliance (AOC).

Software that is developed and maintained following software lifecycle management practices provides the same support for PCI DSS Requirement 6 as software developed and maintained by a Secure SLC Qualified Vendor, if those practices were assessed by a Secure SLC Assessor and confirmed to meet the Secure SLC Standard requirements, with the results documented in a Secure SLC ROC and AOC.

#### Validating the Use of the Secure SLC Standard
When validating the use of software developed and maintained in accordance with the Secure SLC Standard to meet PCI DSS Requirement 6.2 and support customized approach for Requirements 6.3 and 6.5, the assessor must confirm that the following are met:
- The software lifecycle management practices were assessed by a Secure SLC Assessor and confirmed to meet all Secure SLC Standard requirements with the results documented in a Secure SLC Report on Compliance (ROC) and Secure SLC Attestation of Compliance (AOC).
- The software was developed and maintained using the software lifecycle management practices covered by the Secure SLC assessment.
- A full Secure SLC assessment of the software lifecycle management practices was completed within the previous 36 months. Additionally, if the most recent full Secure SLC assessment occurred more than 12 months ago, an Annual Attestation was provided by the developer/vendor within the previous 12 months that confirms continued adherence to Secure SLC Standard for the software lifecycle management practices in use.

#### Validating the Use of the Secure Software Standard
When validating the use of software developed and maintained in accordance with the Secure Software Standard to meet PCI DSS Requirement 6.2.4 and support customized approach for Requirements 6.3 and 6.5, the assessor must confirm that the following are met:
- The secure software assessment was conducted by a Secure Software Assessor and confirmed to meet all requirements in the Secure Software Standard with the results documented in a Secure Software Report on Validation (ROV) and Secure Software Attestation of Validation (AOV).
- The software was developed and is being maintained using the software lifecycle management practices that were covered by the Secure Software assessment.
- A full Secure Software assessment was completed within the previous 36 months. Additionally, if the most recent full Secure Software assessment occurred more than 12 months ago, an Annual Attestation was provided by the developer/vendor within the previous 12 months that confirms continued adherence to Secure Software Standard.