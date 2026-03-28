# 🚀 CTGroup Automation Testing - Recruitment E2E Flow

Dự án Automation Test toàn trình (End-to-End) cho luồng tuyển dụng tập đoàn CT Group. Hệ thống tự động hóa từ bước **Ứng viên nộp hồ sơ** đến bước **Chuyên viên tuyển dụng (TA) verify trên hệ thống ATS**.

---

## 🛠 1. Cài đặt Allure Report (Dành cho người mới)

Allure là công cụ xuất báo cáo chuyên nghiệp. Nếu máy bạn chưa có, làm theo trình tự sau:

1. Tải về:
   - Truy cập: Allure Framework Releases
   - Tìm bản mới nhất, tải file `allure-2.xx.x.zip`.

2. Giải nén:
   - Giải nén file vừa tải vào một thư mục cố định (ví dụ: `C:\allure`).

3. Cấu hình biến môi trường (Windows Path):
   - Nhấn phím Windows, gõ `env` → Chọn **Edit the system environment variables**.
   - Chọn **Environment Variables** → Ở ô **System variables**, tìm dòng **Path** → Nhấn **Edit**.
   - Nhấn **New** → Dán đường dẫn đến thư mục `bin` của Allure (ví dụ: `C:\allure\bin`).
   - Nhấn **OK** liên tiếp 3 lần để lưu.

**QUAN TRỌNG:** Tắt hẳn VS Code và tất cả các cửa sổ Terminal/CMD đang mở, sau đó mở lại để máy nhận diện lệnh `allure`.

---

## 📥 2. Cài đặt Dự án (Setup từ đầu)

Bước 1 — Clone dự án về máy:
git clone https://github.com/NguyenMinhTuanTesting/DAIT_ATS_ApplyAutomationTesting_ApplyCV.git
cd DAIT_ATS_ApplyAutomationTesting_ApplyCV

Bước 2 — Khởi tạo và kích hoạt môi trường ảo (Virtual Env)

Trên Windows (PowerShell):
powershell
python -m venv .venv
.venv\Scripts\activate

Trên macOS/Linux:
bash
python3 -m venv .venv
source .venv/bin/activate

(Khi kích hoạt thành công, bạn sẽ thấy (.venv) hiện ở đầu dòng lệnh.)

Bước 3 — Nâng cấp pip & cài đặt thư viện:
# Nâng cấp pip
python -m pip install --upgrade pip

# Cài đặt toàn bộ thư viện dự án
pip install -r requirements.txt

# Cài đặt trình duyệt cho Playwright
python -m playwright install

⚙️ 3. Cấu hình biến môi trường (.env)
Tạo file tên là .env tại thư mục gốc của dự án. Copy nội dung bên dưới và thay đổi thông tin cá nhân của bạn:

ini
# --- Môi trường (URLs) ---
URL_APPLY_CV="https://hr-dev.ctgroupvietnam.com/apply-job"
URL_ATS_LOGIN="https://hr-dev.ctgroupvietnam.com/web/login"
URL_MENU="https://hr-dev.ctgroupvietnam.com"

# --- Tài khoản TA (Hệ thống nội bộ - Thay bằng tài khoản của bạn) ---
TA_EMAIL="your_email@ctmcorp.com.vn"
TA_PASSWORD="your_password_here"

# --- Cấu hình Browser ---
HEADLESS=False
SLOW_MO=50
BROWSER_TIMEOUT=30000

# --- QUAN TRỌNG: Cấu hình Đường dẫn Dữ liệu (Dùng đường dẫn tuyệt đối) ---
# Lưu ý: Thay đổi đường dẫn cho đúng với vị trí folder trên máy bạn
AVT_FOLDER="D:/Project/data/candidate/images"
CV_FOLDER="D:/Project/data/candidate/files_cv"
DOC_FOLDER="D:/Project/data/candidate/others"

🚀 4. Thực thi Test (Execution)
Dự án hỗ trợ chạy song song nhiều worker để tối ưu tốc độ. Ví dụ chạy 2 worker:

python -m pytest tests/ -n 2 --alluredir=allure-results --clean-alluredir --html=reports/report.html --self-contained-html

(Tùy chỉnh số worker bằng cách thay -n 2.)

📊 5. Xem báo cáo (Reporting)
Cách 1 — Allure Report (đầy đủ log & ảnh chụp màn hình):

allure serve allure-results

Cách 2 — HTML Report (nhanh gọn):

Mở file reports/report.html bằng trình duyệt.
📁 6. Cấu trúc thư mục (Project Structure)
core/: Chứa BasePage và các hàm tương tác dùng chung.
pages/: Page Object Model (Logic xử lý cho từng trang riêng biệt).
locators/: Quản lý tập trung các Selector (ID, Xpath, CSS).
dto/: Data Transfer Object (Đóng gói dữ liệu bằng Pydantic).
data/: Chứa file JSON mẫu và bộ sinh dữ liệu ngẫu nhiên.
tests/: Các kịch bản kiểm thử E2E.
allure-results/: Thư mục output cho Allure (khi chạy pytest với --alluredir).
reports/: Báo cáo HTML được sinh ra.
