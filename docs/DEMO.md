# Kịch bản demo và phản biện

## Kịch bản 4–5 phút

0:00–0:30: “Đây là Portfolio CV cá nhân cho FIT4014 A2.2, xây dựng bằng HTML, CSS và JavaScript. Em có sử dụng AI, phạm vi khai báo trong AI_LOG.” Chỉ nói các bước em thực sự đã tự thực hiện.

0:30–1:30: Mở URL GitHub Pages công khai (khi đã có). Giới thiệu bố cục; chọn Web để lọc; mở chi tiết Portfolio; Escape để đóng; chuyển giao diện mobile và mở in preview.

1:30–2:30: Mở repository. Giải thích cấu trúc HTML/CSS/JS, tài liệu và workflow. Mở ít nhất 3 commit thực tế, chọn commit sửa lỗi và giải thích diff. Không nói các commit do AI tạo là lịch sử em tự viết.

2:30–3:30: Mở workflow thành công, đối chiếu SHA với repository; mở DevTools Network và tải lại để minh chứng không 404. Mở tag v1.0.0 và GitHub Release thực tế.

3:30–4:30: Trình bày README, AI_LOG và giới hạn. Chốt bằng nội dung tự học được và trả lời câu hỏi.

URL demo: https://duckhuy7.github.io/BT-TKW/

## Phản biện gợi ý

**Git và GitHub khác nhau?** Git quản lý phiên bản; GitHub lưu repository từ xa và cung cấp cộng tác, Actions, Pages.

**Commit, tag, release khác nhau?** Commit là snapshot thay đổi; tag đánh dấu commit; release là bản phát hành có mô tả/tài sản gắn với tag trên GitHub.

**Vì sao chọn web tĩnh?** Phạm vi là portfolio giới thiệu, không cần tài khoản hay dữ liệu động; dễ kiểm tra, triển khai và phù hợp Pages.

**Vì sao CSS chạy local nhưng lỗi khi lên Pages?** Dấu `/` đầu đường dẫn trỏ về gốc domain, bỏ phần tên repo. Dùng đường dẫn tương đối, kiểm tra chữ hoa/thường và artifact.

**Làm sao biết bản online đúng nguồn?** Đối chiếu SHA local, repository và workflow; kiểm tra bản triển khai thực tế. Có thể thêm dấu hiệu nội dung phiên bản khi cần.

**Nếu deploy thất bại?** Đọc log bước lỗi, sửa nguyên nhân, commit/push lại; không xoá lịch sử để che lỗi.

**Rollback thế nào?** Dùng `git revert` commit lỗi, push và triển khai lại. Revert giữ lịch sử; không force push tùy tiện.

**AI đã làm gì?** AI đã hỗ trợ phần lớn mã và tài liệu ban đầu. Em cần trình bày chính xác phần mình đã tự sửa, kiểm tra và hiểu, tham chiếu nhật ký thực tế.

**Vì sao hồ sơ bài nộp không xuất hiện trên trang?** Portfolio dành cho người xem dự án; tài liệu kỹ thuật và bài nộp được đặt riêng trong repository.

**Nút In/Lưu CV có tạo file sẵn không?** Không; nó gọi window.print(), dùng CSS print; người dùng chọn Save as PDF trong hộp thoại hệ thống.
