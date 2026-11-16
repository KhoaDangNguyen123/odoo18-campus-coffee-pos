☕ Campus Coffee & Tea — Hệ thống Quản lý Bán hàng & Kho Định lượng (Odoo 18 POS)

Dự án triển khai hệ thống quản lý điểm bán hàng (Point of Sale) kết hợp quản lý kho và định mức nguyên liệu tự động (Bill of Materials - Kit) trên nền tảng **Odoo 18** cho mô hình chuỗi cửa hàng đồ uống **Campus Coffee & Tea**.

## 🚀 Tính năng chính đã triển khai
* **Giao diện POS tối ưu cho F&B**: Phân nhóm thực đơn trực quan (*Cà phê, Trà, Bánh ngọt, Combo*), hỗ trợ chọn biến thể kích cỡ (*Size M, Size L*) tự động cộng phụ phí.
* **Quản lý Khách hàng & Tích điểm (Loyalty)**: Lưu trữ thông tin thành viên và tích lũy điểm thưởng trực tiếp trên từng hóa đơn bán hàng.
* **Hóa đơn tùy chỉnh (Custom Receipt)**: Hiển thị logo thương hiệu, thông tin chi nhánh, chi tiết món, điểm tích lũy và thông tin Wifi tại chân trang.
* **Trừ kho tự động theo công thức pha chế (BoM Kit)**: Thiết lập định mức nguyên liệu cho từng món (ví dụ: `Cà phê sữa đá (Size M)` gồm 25g cà phê hạt, 30g sữa đặc, 1 ly nhựa — giá vốn tự động tính toán **9,550 ₫/ly**) giúp tự động trừ tồn kho nguyên vật liệu ngay khi thanh toán.
* **Quản lý Ca làm việc & Đối soát (POS Session)**: Theo dõi quỹ tiền đầu ca, đối soát tiền mặt cuối ca (*Closing Register*) và xuất báo cáo doanh thu chi tiết (*Sales Details*).

## 📂 Cấu trúc thư mục dự án
```text
odoo18-campus-coffee-pos/
├── database/
│   └── campus_cafe_db.zip                # Bản sao lưu toàn bộ cơ sở dữ liệu Odoo 18
├── data_exports/
│   ├── products_menu.xlsx                # Danh sách thực đơn, giá bán, giá vốn và phân nhóm POS
│   ├── bom_recipes.xlsx                  # Định mức nguyên liệu pha chế (BoM Kit)
│   └── pos_orders.csv                    # Lịch sử giao dịch đơn hàng POS (UTF-8)
├── reports/
│   └── pos_session_report.pdf            # Báo cáo tổng kết phiên bán hàng & doanh thu
├── screenshots/
│   ├── 01_pos_menu_ui.png                # Giao diện màn hình bán hàng chính
│   ├── 02_pos_order_variants_loyalty.png # Thao tác chọn Size và khách hàng thành viên
│   ├── 03_pos_custom_receipt.png         # Mẫu hóa đơn thanh toán hoàn chỉnh
│   ├── 04_pos_closing_register.png       # Đối soát két tiền và chốt ca
│   └── 05_bom_inventory_deduction.png    # Tổng quan định mức BoM và giá vốn
└── README.md

🛠️ Hướng dẫn khôi phục & chạy thử nghiệm
Cài đặt Odoo 18 trên máy cục bộ hoặc qua Docker (http://localhost:8069).
Truy cập trình quản lý cơ sở dữ liệu tại đường dẫn: http://localhost:8069/web/database/manager.
Chọn Restore Database, tải lên tệp database/campus_cafe_db.zip, đặt tên cơ sở dữ liệu mới (ví dụ: campus_cafe_db) và nhấn Continue.Đăng nhập bằng tài khoản quản trị viên để trải nghiệm đầy đủ phân hệ Point of Sale, Inventory và Manufacturing.