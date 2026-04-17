### A. Tài liệu gốc của Appendix B

### B. Summary Overview của Appendix B
Tài liệu này mô tả chi tiết **Appendix B** trong **PCI-DSS v4.0.1**, tập trung vào các **biện pháp kiểm soát bù đắp (compensating controls)**. 
Mục tiêu chính là cung cấp một lộ trình cho các thực thể không thể đáp ứng trực tiếp một yêu cầu PCI DSS do các **hạn chế về kỹ thuật hoặc kinh doanh chính đáng** và đã được ghi chép lại. Các biện pháp này cho phép thực thể giảm thiểu rủi ro liên quan thông qua việc triển khai các biện pháp kiểm soát thay thế nhằm đạt được mức độ bảo mật tương đương.
### C. Key Points của Appendix B
Các biện pháp kiểm soát bù đắp phải đáp ứng đầy đủ các tiêu chí nghiêm ngặt sau:
*   **Đáp ứng mục đích và mức độ nghiêm ngặt:** Phải đạt được ý định của yêu cầu PCI DSS gốc.
*   **Mức độ phòng thủ tương đương:** Cung cấp khả năng phòng vệ tương tự để bù đắp rủi ro mà yêu cầu gốc thiết kế để chống lại.
*   **Vượt trên mức quy định (Above and Beyond):** Không được đơn thuần là việc tuân thủ các yêu cầu PCI DSS khác; nó phải là một nỗ lực bổ sung.
*   **Giải quyết rủi ro phát sinh:** Xử lý được các rủi ro bổ sung do việc không tuân thủ yêu cầu gốc gây ra.
*   **Tính hiện tại và tương lai:** Phải có hiệu lực ngay tại thời điểm đánh giá và trong tương lai, không dùng để bù đắp cho các nhiệm vụ đã bỏ lỡ trong quá khứ.
*   **Sự xác nhận của đánh giá viên:** Tất cả các biện pháp bù đắp phải được đánh giá viên (assessor) xem xét và xác thực về tính đầy đủ và hiệu quả trong môi trường cụ thể.
### D. Deep Summary của Appendix B
**Bối cảnh:** 
Trong thực tế, một số tổ chức gặp phải những rào cản bất khả kháng về hạ tầng kỹ thuật hoặc quy trình kinh doanh khiến họ không thể thực hiện đúng nguyên văn một yêu cầu của PCI DSS. Appendix B được ra đời để đảm bảo tính linh hoạt nhưng vẫn giữ vững tiêu chuẩn an toàn dữ liệu thanh toán.

**Nội dung cốt lõi:** 
Trọng tâm của Appendix B là việc xác định tính hợp lệ của biện pháp kiểm soát thay thế. Một điểm then chốt là nguyên tắc **"Above and Beyond"**: Một yêu cầu PCI DSS hiện có không thể được coi là biện pháp bù đắp nếu nó vốn dĩ đã là yêu cầu bắt buộc đối với đối tượng đang được đánh giá. Tuy nhiên, một yêu cầu từ khu vực khác (không bắt buộc đối với đối tượng này) hoặc sự kết hợp giữa các yêu cầu hiện có với các biện pháp kiểm soát mới có thể tạo thành một biện pháp bù đắp hợp lệ.

**Dữ liệu đáng chú ý:** 
- Các thực thể phải sử dụng một **Worksheet (Appendix C)** cụ thể để định nghĩa và tài liệu hóa các biện pháp này, bao gồm việc giải thích hạn chế, định nghĩa biện pháp, mục tiêu, rủi ro, cách xác thực và quy trình duy trì.
- Việc tài liệu hóa các biện pháp kiểm soát bù đắp là bắt buộc trong Báo cáo Tuân thủ (ROC) hoặc Bản tự đánh giá (SAQ).

**Rủi ro / Lưu ý:** 
- **Hiệu quả phụ thuộc môi trường:** Một biện pháp bù đắp có thể hiệu quả ở môi trường này nhưng lại không hiệu quả ở môi trường khác tùy thuộc vào cấu hình và các kiểm soát xung quanh.
- **Không áp dụng cho quá khứ:** Không thể sử dụng biện pháp này để khắc phục một lỗi tuân thủ đã xảy ra trong các quý trước.
- **Sự loại trừ:** Các biện pháp kiểm soát bù đắp **không phải là một lựa chọn** khi thực thể sử dụng Phương pháp tiếp cận tùy chỉnh (Customized Approach - Appendix D), vì phương pháp đó đã cho phép tự thiết kế kiểm soát ngay từ đầu.
### E. Structured Output của Appendix B
Compensating controls may be considered when an entity cannot meet a PCI DSS requirement explicitly as stated, due to legitimate and documented technical or business constraints but has sufficiently mitigated the risk associated with not meeting the requirement through implementation of other, or compensating, controls.
**Compensating controls must satisfy the following criteria:**
1. Meet the intent and rigor of the original PCI DSS requirement.
2. Provide a similar level of defense as the original PCI DSS requirement, such that the compensating control sufficiently offsets the risk that the original PCI DSS requirement was designed to defend against. To understand the intent of a requirement, see the Customized Approach Objective for most PCI DSS requirements. If a requirement is not eligible for the Customized Approach and therefore does not have a Customized Approach Objective, refer to the Purpose in the Guidance column for that requirement.
3. Be “above and beyond” other PCI DSS requirements. (Simply being in compliance with other PCI DSS requirements is not a compensating control.).
4. When evaluating “above and beyond” for compensating controls, consider the following:
    - a) Existing PCI DSS requirements CANNOT be considered as compensating controls if they are already required for the item under review. For example, passwords for non-console administrative access must be sent encrypted to mitigate the risk of intercepting cleartext administrative passwords. An entity cannot use other PCI DSS password requirements (intruder lockout, complex passwords, etc.) to compensate for lack of encrypted passwords, since those other password requirements do not mitigate the risk of interception of cleartext passwords. Also, the other password controls are already PCI DSS requirements for the item under review (passwords).
    - b) Existing PCI DSS requirements MAY be considered as compensating controls if they are required for another area but are not required for the item under review.
    - c) Existing PCI DSS requirements may be combined with new controls to become a compensating control. For example, if a company is unable to address a vulnerability that is exploitable through a network interface because a security update is not yet available from a vendor, a compensating control could consist of controls that include all of the following: 1) internal network segmentation, 2) limiting network access to the vulnerable interface to only required devices (IP address or MAC address filtering), and 3) IDS/IPS monitoring of all traffic destined to the vulnerable interface.
5. Address the additional risk imposed by not adhering to the PCI DSS requirement.
6. Address the requirement currently and in the future. A compensating control cannot address a requirement that was missed in the past (for example, where performance of a task was required two quarters ago, but that task was not performed).

The assessor is required to thoroughly evaluate compensating controls during each annual PCI DSS assessment to confirm that each compensating control adequately addresses the risk that the original PCI DSS requirement was designed to address, per items 1-6 above.

To maintain compliance, processes and controls must be in place to ensure compensating controls remain effective after the assessment is complete. Additionally, compensating control results must be documented in the applicable report for the assessment (for example, a Report on Compliance or a Self-Assessment Questionnaire) in the corresponding PCI DSS requirement section, and included when the applicable report is submitted to the requesting organization.

**Note:** All compensating controls must be reviewed and validated for sufficiency by the assessor who conducts the PCI DSS assessment. The effectiveness of a compensating control is dependent on the specifics of the environment in which the control is implemented, the surrounding security controls, and the configuration of the control. Entities should be aware that a given compensating control will not be effective in all environments.