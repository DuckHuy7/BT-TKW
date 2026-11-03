# BT-TKW — Portfolio cá nhân

Bài tập thiết kế web FIT4014. HTML5, CSS và JavaScript thuần, không cần npm hoặc backend.

## Chức năng

Giới thiệu, kỹ năng, dự án, quy trình và liên hệ. Bộ lọc UI/UX, Web, Hệ thống; hộp thoại chi tiết hỗ trợ Escape; in/lưu CV bằng hộp thoại in trình duyệt. Có CSS responsive và print.

Đã bỏ Hồ sơ bài nộp, checklist và câu hỏi phản biện khỏi giao diện theo yêu cầu.

## Chạy local

Đặt index.html, style.css và script.js cùng thư mục. Mở index.html bằng trình duyệt hoặc Live Server trong VS Code. Hoặc chạy:

```bash
python -m http.server 8000
```

Mở http://localhost:8000.

## Cấu trúc

- index.html: nội dung portfolio.
- style.css: giao diện và responsive.
- script.js: bộ lọc, dialog và nút in.
- AI_LOG.md: khai báo AI.
- RELEASE_NOTES.md: ghi chú phiên bản.

## Repository và demo

Repository: https://github.com/DuckHuy7/BT-TKW

Demo công khai: https://duckhuy7.github.io/BT-TKW/

Pages đã bật từ nhánh main, thư mục /(root), HTTPS bắt buộc. GitHub tự chạy workflow pages build and deployment khi nhánh cập nhật.

## Giới hạn

Chưa có thông tin liên hệ đầy đủ. Hình dự án là minh họa bằng CSS, không phải ảnh chụp sản phẩm thực tế. Không có backend hoặc gửi email. Google Fonts có Arial dự phòng. AI hỗ trợ phần lớn mã nguồn; sinh viên cần đọc hiểu, chỉnh thông tin và tự kiểm chứng trước khi nộp.

## Kiểm chứng và tài liệu bài nộp

```bash
python scripts/verify.py
node --check script.js
python scripts/verify.py --online
git log --oneline
git rev-parse HEAD
```

Chờ workflow triển khai xong trước khi chạy kiểm tra online. Script so sánh byte của HTML, CSS và JavaScript, không chỉ kiểm tra trang mở được.

- [Biên bản kiểm chứng](docs/VERIFICATION.md)
- [Kịch bản demo và phản biện](docs/DEMO.md)
- [Đối chiếu rubric](docs/RUBRIC.md)
- [Release note](RELEASE_NOTES.md)

Tài liệu học phần nằm trong repository, không hiển thị thành các mục trên website.
