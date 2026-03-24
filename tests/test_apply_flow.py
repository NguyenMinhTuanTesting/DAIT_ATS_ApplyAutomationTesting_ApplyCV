import os
import pytest
import allure
from dotenv import load_dotenv
from pages.apply_cv_page import ApplyCVPage
from data.candidate_generator import CandidateGenerator

# Load biến môi trường từ .env
load_dotenv()


@allure.feature("Candidate Application")
@allure.story("Apply CV with full 4 pages")
def test_apply_cv_successfully(page):
    # 1. Khởi tạo Data và Generator
    gen = CandidateGenerator()
    candidate = gen.get_candidate()

    # 2. Inject đường dẫn file từ .env vào DTO trước khi chạy
    candidate.page_1.avatar_path = os.getenv("AVATAR_PATH")
    candidate.page_4.cv_file_path = os.getenv("CV_PATH")

    apply_url = os.getenv("URL_APPLY_CV")
    expected_menu_url = os.getenv("URL_MENU")

    # 3. Khởi tạo Page Object
    apply_page = ApplyCVPage(page)

    # --- BẮT ĐẦU LUỒNG TEST ---
    with allure.step(f"Truy cập trang apply: {apply_url}"):
        apply_page.goto(apply_url)
        apply_page.setup_language_vi()

    # Thực hiện điền 4 trang (Modular Actions)
    apply_page.fill_page_1(candidate.page_1)
    apply_page.fill_page_2(candidate.page_2)
    apply_page.fill_page_3(candidate.page_3)
    apply_page.fill_page_4(candidate.page_4)

    # 4. Kiểm tra kết quả (Assertion)
    with allure.step(f"Kiểm tra điều chuyển sang URL Menu: {expected_menu_url}"):
        # Đợi cho đến khi URL thay đổi hoặc network ổn định
        page.wait_for_url(f"{expected_menu_url}/**", timeout=15000)

        current_url = page.url
        assert expected_menu_url in current_url, \
            f"Lỗi: Không được chuyển hướng về trang chủ. URL hiện tại: {current_url}"

        apply_page.take_screenshot("Apply_Success_Redirect")