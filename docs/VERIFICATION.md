# Biên bản kiểm chứng FIT4014 A2.2

Ngày 03/11/2026. Kiểm tra bởi trợ lý; sinh viên cần tự thực hiện lại khi demo.

## Chuỗi local → repository → URL công khai

1. Mã nguồn được chuẩn bị local và kiểm tra bằng node --check, kiểm tra tài nguyên và anchor.
2. Đưa nguồn lên DuckHuy7/BT-TKW bằng GitHub Git API, commit nối tiếp, không force push.
3. Clone repository về local bằng git clone để đối chiếu dữ liệu thực tế trên GitHub.
4. Bật Pages từ main, /(root). Workflow đầu tiên 41596607256 có build, deploy và report-build-status đều success.
5. Ở commit db15239aae80bc9cdaa8a707ea6868bdc8c97896, HTTP GET index.html, style.css và script.js đều trả 200 và khớp byte với local clone.
6. Mở URL công khai trong trình duyệt: nội dung và CSS hiển thị; lọc Web chỉ còn Portfolio; mở dialog hiển thị đúng thông tin. Phần Hồ sơ bài nộp đã được bỏ.
7. Sau đó sửa lỗi dialog: giới hạn chiều cao, cho phép cuộn nội dung dài và khóa cuộn nền. Commit fix riêng để thể hiện thay đổi thật.

Workflow ban đầu: https://github.com/DuckHuy7/BT-TKW/actions/runs/41596607256
Demo: https://duckhuy7.github.io/BT-TKW/

## Tái kiểm tra phiên bản mới nhất

```bash
git pull --ff-only
git rev-parse HEAD
python scripts/verify.py
node --check script.js
python scripts/verify.py --online
```

So sánh SHA HEAD với SHA của workflow mới nhất trong Actions. Lệnh online cần chạy sau khi deploy xong. Mã hash và kết quả 200 được in trực tiếp; lưu lại để nộp minh chứng. Không ghi kết quả của commit cũ thành kết quả của commit mới.

## Kiểm tra thủ công cần sinh viên hoàn tất

- Tự điền họ tên, mã sinh viên, lớp và liên hệ chính xác.
- Mở bản công khai trên điện thoại hoặc viewport 390px, kiểm tra không tràn ngang.
- Dùng Tab/Enter/Escape; thử cả ba nhóm lọc và nút Tất cả.
- Mở In/Lưu CV, kiểm tra trước khi lưu PDF.
- DevTools Network: tải lại, chụp tài nguyên CSS/JS không 404.
- Lưu ảnh repository, lịch sử commit, workflow thành công và Release v1.0.0.
- Tự thuyết trình, không nói phần AI làm là do sinh viên tự viết.

Minh họa được dựng bằng CSS nên không có file ảnh dự án bên ngoài. Google Fonts có font Arial dự phòng. Chưa xác nhận kiểm tra mobile hoặc in PDF trực tiếp.
