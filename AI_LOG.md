# Nhật ký sử dụng AI

Ngày 03/11/2026. Công cụ: ChatGPT/Codex.

AI hỗ trợ phân tích đề FIT4014 A2.2 và tạo phần lớn HTML, CSS, JavaScript, tài liệu ban đầu. Người dùng yêu cầu bỏ Hồ sơ bài nộp, checklist và phản biện khỏi giao diện; phiên bản này đã áp dụng yêu cầu đó.

Các commit do trợ lý tạo trong phiên làm việc thực tế. Không coi đó là lịch sử sinh viên tự phát triển. Người học cần tự đọc và giải thích code, sửa thông tin, kiểm tra bộ lọc, dialog, responsive, in CV và URL triển khai.

Đã kiểm tra cú pháp JavaScript, tài nguyên nội bộ và anchor. Bộ lọc và dialog của bản ban đầu đã được kiểm tra trong trình duyệt. Chưa xác nhận sinh viên tự kiểm chứng hoặc bản mới được kiểm tra trực tiếp trên điện thoại.

## Kết quả triển khai và cách tự kiểm chứng

AI tạo repository, đưa nguồn lên bằng các commit, bật Pages và kiểm tra workflow. Bản ban đầu triển khai thành công, HTML/CSS/JS trả HTTP 200 và trùng byte với bản clone local. Có commit fix giới hạn dialog và cuộn nền. Xem docs/VERIFICATION.md để phân biệt commit đã kiểm tra và phiên bản cần tái kiểm tra.

Sinh viên chạy python scripts/verify.py --online, đối chiếu SHA workflow, thao tác các nút và chụp bằng chứng. Chưa có xác nhận sinh viên đã tự làm các bước này.
