### A. Tài liệu gốc của Chapter 7

### B. Summary Overview của Chapter 7
Tài liệu này mô tả chi tiết **Chapter 7** trong **PCI-DSS v4.0.1**, tập trung vào việc **định nghĩa các khung thời gian (timeframes)** được sử dụng xuyên suốt trong các yêu cầu của tiêu chuẩn. 
Mục tiêu chính là thiết lập sự thống nhất cho các hoạt động cần thực hiện định kỳ thông qua quy trình lặp lại và có lịch trình cụ thể, đảm bảo các biện pháp kiểm soát được duy trì liên tục và hiệu quả.

### C. Key Points của Chapter 7
- **Tính nhất quán của hoạt động:** Các hoạt động phải được thực hiện ở các khoảng thời gian sát với khung thời gian quy định nhất có thể và không được vượt quá thời hạn đó.
- **Quyền tự chủ của thực thể:** Thực thể có quyền lựa chọn thực hiện các hoạt động thường xuyên hơn so với yêu cầu tối thiểu của tiêu chuẩn (ví dụ: thực hiện hàng tháng thay vì hàng quý).
- **Định nghĩa "Định kỳ" (Periodically):** Tần suất thực hiện do thực thể tự quyết định nhưng phải được tài liệu hóa và hỗ trợ bởi phân tích rủi ro của chính thực thể đó.
- **Quy trình xử lý sự cố:** Thực thể phải có quy trình để phát hiện và xử lý ngay lập tức khi một hoạt động định kỳ bị bỏ lỡ, bao gồm việc xác định nguyên nhân và lập lại lịch trình.
- **Linh hoạt cho đánh giá lần đầu:** Đối với các yêu cầu có khung thời gian, đánh giá lần đầu chỉ yêu cầu thực thể chứng minh đã thực hiện hoạt động trong kỳ gần nhất và có chính sách duy trì cho tương lai.

### D. Deep Summary của Chapter 7
**Bối cảnh:**
PCI DSS yêu cầu nhiều hoạt động bảo mật phải được thực hiện lặp đi lặp lại. Việc định nghĩa rõ ràng các thuật ngữ như "hàng quý" hay "hàng năm" giúp tránh sự hiểu lầm giữa thực thể và kiểm toán viên, đảm bảo an ninh môi trường dữ liệu không bị gián đoạn.

**Nội dung cốt lõi:**
Chương này cung cấp bảng tra cứu chuẩn (Table 4) cho các thuật ngữ thời gian:
1.  **Hàng ngày (Daily):** Mỗi ngày trong năm, không chỉ tính ngày làm việc.
2.  **Hàng tuần (Weekly):** Ít nhất một lần mỗi 7 ngày.
3.  **Hàng tháng (Monthly):** Ít nhất một lần mỗi 30-31 ngày.
4.  **Hàng quý (Quarterly):** Ít nhất một lần mỗi 90-92 ngày.
5.  **Hàng năm (Annually):** Ít nhất một lần mỗi 365 ngày (hoặc 366 ngày năm nhuận).
6.  **Thay đổi đáng kể (Significant change):** Định nghĩa các trường hợp cần thực hiện lại các biện pháp kiểm soát như khi thêm phần cứng/phần mềm mới, thay đổi luồng dữ liệu hoặc thay đổi nhà cung cấp dịch vụ bên thứ ba.

**Dữ liệu đáng chú ý:**
- **Khung thời gian 6 tháng:** Được định nghĩa là ít nhất một lần mỗi 180-184 ngày.
- **Yêu cầu cho các năm tiếp theo:** Sau kỳ đánh giá đầu tiên, hoạt động phải được thực hiện đủ số lần trong năm (ví dụ: 4 lần cho yêu cầu hàng quý) với khoảng cách không vượt quá quy định.
- **Nguyên tắc "Ngay lập tức" (Immediately):** Được hiểu là thực hiện trong thời gian thực hoặc gần như thời gian thực, không có sự chậm trễ.

**Rủi ro / Lưu ý:**
- **Lỗi quản trị:** Nếu một hoạt động bị bỏ lỡ do quản lý kém hoặc thiếu giám sát mà không có quy trình khắc phục, thực thể sẽ bị coi là không tuân thủ yêu cầu đó.
- **Cách tiếp cận hợp lý:** Thực thể sẽ không bị coi là không tuân thủ ngay lập tức nếu thực hiện hoạt động trễ, miễn là họ đã thực hiện đúng quy trình: thông báo kịp thời -> xác định nguyên nhân -> thực hiện bù ngay khi có thể -> lập lại lịch trình.
- **Yêu cầu tài liệu:** Mọi hoạt động phát hiện và khắc phục khi bỏ lỡ lịch trình đều phải được tạo thành hồ sơ tài liệu để kiểm toán viên rà soát.

### E. Structured Output của Chapter 7
Certain PCI DSS requirements have been established with specific timeframes for activities that need to be performed consistently via a regularly scheduled and repeatable process. The intent is that the activity is performed at an interval as close to that timeframe as possible without exceeding it. The entity has the discretion to perform an activity more often than specified (for example, performing an activity monthly where the PCI DSS requirement specifies it be performed every three months).

Table 4 outlines the frequency for the different time periods used in PCI DSS Requirements.

#### Table 4. PCI DSS Requirement Timeframes

| Timeframes in PCI DSS Requirements | Descriptions and Examples |
|-----------------------------------|---------------------------|
| Daily | Every day of the year (not only on business days). |
| Weekly | At least once every seven days. |
| Monthly | At least once every 30 to 31 days, or on the nᵗʰ day of the month. |
| Every three months ("quarterly") | At least once every 90 to 92 days, or on the nᵗʰ day of each third month. |
| Every six months | At least once every 180 to 184 days, or on the nᵗʰ day of each sixth month. |
| Every 12 months ("annually") | At least once every 365 (or 366 for leap years) days or on the same date every year. |
| Periodically | Frequency of occurrence is at the entity’s discretion and is documented and supported by the entity’s risk analysis. The entity must demonstrate that the frequency is appropriate for the activity to be effective and to meet the intent of the requirement. |
| Immediately | Without delay. In real time or near real time. |
| Promptly | As soon as reasonably possible. |
| Significant change | There are several requirements that specify activities to be performed upon a significant change in an entity’s environment. While what constitutes a significant change is highly dependent on the configuration of a given environment, each of the following activities, at a minimum, has potential impacts on the security of the CDE and must be considered and evaluated to determine whether a change is a significant change for an entity in the context of related PCI DSS requirements:<br><br>• New hardware, software, or networking equipment added to the CDE.<br>• Any replacement or major upgrades of hardware and/or software in the CDE.<br>• Any changes in the flow or storage of account data.<br>• Any changes to the boundary of the CDE and/or to the scope of the PCI DSS assessment.<br>• Any changes to the underlying supporting infrastructure of the CDE (including, but not limited to, changes to directory services, time servers, logging, and monitoring).<br>• Any changes to third-party vendors/service providers (or services provided) that support the CDE or meet PCI DSS requirements on behalf of the entity. |

---
For other PCI DSS requirements, where the standard does not define a minimum frequency for recurring activities but instead allows for the requirement to be met “periodically,” the entity is expected to define the frequency as appropriate for its business. The frequency defined by the entity must be supported by the entity’s security policy and the risk analysis conducted according to PCI DSS Requirement 12.3.1. The entity must also be able to demonstrate that the frequency it has defined is appropriate for the activity to be effective and to meet the intent of the requirement.

In both cases, where PCI DSS specifies a required frequency and where PCI DSS allows for “periodic” performance, the entity is expected to have documented and implemented processes to ensure that activities are performed within a reasonable timeframe, including at least the following:
- The entity is promptly notified any time an activity is not performed per its defined schedule.
- The entity determines the events that led to missing a scheduled activity.
- The entity performs the activity as soon as possible after it is missed and either gets back on schedule or establishes a new schedule.
- The entity produces documentation that shows the above elements occurred.

When an entity has the above processes in place to detect and address when a scheduled activity is missed, a reasonable approach is allowable, meaning that if an activity is required to be performed at least once every three months, the entity is not automatically non-compliant if the activity is performed late where the entity’s documented and implemented process (per above) was followed. However, where no such process is in place and/or the activity was not performed according to schedule due to oversight, mismanagement, or lack of monitoring, the entity has not met the requirement. In such cases, the requirement will only be in place when the entity 1) documents (or reconfirms) the process per above to ensure the scheduled activity occurs on time, 2) re-establishes the schedule, and 3) provides evidence that the entity has performed the scheduled activity at least once per their schedule.

**Note:** Where an entity is being assessed for the first time against a PCI DSS requirement with a defined timeframe, it is considered an initial PCI DSS assessment for that requirement. This means the entity has never undergone a prior assessment to that requirement, where the assessment resulted in submission of a compliance validation document (for example, an AOC, SAQ, or ROC).

For an initial assessment against a requirement that has a defined timeframe, it is not required that the activity has been performed for every such timeframe during the previous year, if the assessor verifies:
- The activity was performed in accordance with the applicable requirement within the most recent timeframe (for example, the most recent three-month or six-month period), and
- The entity has documented policies and procedures for continuing to perform the activity within the defined timeframe.

For subsequent years after the initial assessment, the activity must have been performed at least once within each required timeframe. For example, an activity required at least every three months must have been performed at least four times during the previous year at an interval that does not exceed 90-92 days.
