### A. Tài liệu gốc của Appendix C

### B. Summary Overview của Appendix C
Tài liệu này mô tả chi tiết **Appendix C** trong **PCI-DSS v4.0.1**, tập trung vào **Bảng tính Biện pháp Kiểm soát Bù đắp (Compensating Controls Worksheet)**. 
Mục tiêu chính là cung cấp một biểu mẫu bắt buộc để các thực thể xác định và giải trình chi tiết các biện pháp kiểm soát thay thế khi họ sử dụng chúng để đáp ứng các yêu cầu của PCI DSS.
### C. Key Points của Appendix C
Bảng tính này yêu cầu các thực thể phải cung cấp đầy đủ thông tin cho 6 mục cốt lõi sau:
- **Hạn chế (Constraints):** Hồ sơ về các rào cản kỹ thuật hoặc kinh doanh chính đáng ngăn cản việc tuân thủ yêu cầu gốc.
- **Định nghĩa biện pháp bù đắp (Definition of Compensating Controls):** Giải thích cách các biện pháp này đáp ứng mục tiêu của kiểm soát gốc và giải quyết rủi ro tăng thêm.
- **Mục tiêu (Objective):** Xác định mục tiêu của kiểm soát gốc và mục tiêu mà biện pháp bù đắp sẽ đạt được.
- **Rủi ro đã xác định (Identified Risk):** Nêu rõ bất kỳ rủi ro bổ sung nào phát sinh do thiếu kiểm soát gốc.
- **Xác thực biện pháp bù đắp (Validation of Compensating Controls):** Mô tả quy trình và cách thức các biện pháp bù đắp được kiểm tra và xác thực.
- **Duy trì (Maintenance):** Định nghĩa các quy trình và cơ chế kiểm soát để duy trì tính hiệu quả của biện pháp bù đắp.
### D. Deep Summary của Appendix C
**Bối cảnh:**
Appendix C đóng vai trò là công cụ thực thi các nguyên tắc đã nêu tại Appendix B. Việc sử dụng bảng tính này là bắt buộc đối với bất kỳ thực thể nào muốn sử dụng biện pháp bù đắp để đạt được sự tuân thủ.

**Nội dung cốt lõi:**
Nội dung của bảng tính buộc doanh nghiệp phải thực hiện một phân tích sâu sắc về sự tương đương trong bảo mật. Thay vì chỉ tuyên bố có biện pháp thay thế, doanh nghiệp phải chứng minh được bằng văn bản các hạn chế thực tế và cách thức mà biện pháp mới "khớp" với mục tiêu an ninh ban đầu (thường dựa trên Mục tiêu của Phương pháp tiếp cận tùy chỉnh).

**Dữ liệu đáng chú ý:**
- Các biện pháp bù đắp phải được tài liệu hóa đồng nhất giữa bảng tính này và phần tương ứng trong Báo cáo Tuân thủ (ROC).
- Chỉ những thực thể có các hạn chế về công nghệ hoặc kinh doanh **chính đáng và đã được lập hồ sơ** mới được phép cân nhắc sử dụng bảng tính này.
- Phần "Mục tiêu" cho phép linh hoạt bằng cách sử dụng các Mục tiêu của Phương pháp tiếp cận tùy chỉnh (Customized Approach Objective) để làm căn cứ so sánh hiệu quả.

**Rủi ro / Lưu ý:**
- **Tính toàn vẹn của tài liệu:** Thiếu sót trong bất kỳ mục nào của 6 mục nêu trên có thể dẫn đến việc biện pháp bù đắp không được đánh giá viên chấp nhận.
- **Trách nhiệm duy trì:** Việc thiết lập biện pháp bù đắp chỉ là bước đầu; thực thể phải có quy trình định nghĩa rõ ràng để đảm bảo chúng không bị mất hiệu lực sau khi quá trình đánh giá kết thúc.
- **Sự tách biệt:** Giống như Appendix B, bảng tính này không phải là một lựa chọn nếu thực thể đang áp dụng Phương pháp tiếp cận tùy chỉnh (Customized Approach) theo Appendix D.
### E. Structured Output của Appendix C
The entity must use this worksheet to define compensating controls for any requirement where compensating controls are used to meet a PCI DSS requirement. Note that compensating controls should also be documented in accordance with instructions in the Report on Compliance in the corresponding PCI DSS requirement section.

**Note:** Only entities that have legitimate and documented technological or business constraints can consider the use of compensating controls to achieve compliance.

**Requirement Number and Definition:**
**Information Required Explanation:**
1. **Constraints:** Document the legitimate technical or business constraints precluding compliance with the original requirement.
2. **Definition of Compensating Controls:** Define the compensating controls: explain how they address the objectives of the original control and the increased risk, if any.
3. **Objective:** Define the objective of the original control (for example, the Customized Approach Objective). Identify the objective met by the compensating control (note: this can be, but is not required to be, the stated Customized Approach Objective for the PCI DSS requirement).
4. **Identified Risk:** Identify any additional risk posed by the lack of the original control.
5. **Validation of Compensating Controls:** Define how the compensating controls were validated and tested.
6. **Maintenance:** Define process(es) and controls in place to maintain compensating controls.