import pytest
import allure
from pages.ats.applycv_page import ApplyCVPage
from data.candidate_data import get_fake_candidate_page1

# Link apply cv
ATS_URL = "https://hr-dev.ctgroupvietnam.com/apply-job"


@allure.feature("ATS Apply CV")
@allure.story("Trang 1: Điền full thông tin bắt buộc")
def test_apply_cv_step_1_full_fields(page):
    """
    Test case: Điền toàn bộ thông tin bắt buộc của Trang 1 và verify đã chuyển sang Trang 2 thành công.
    """
    # 1. Khởi tạo Page và Data
    apply_page = ApplyCVPage(page)
    data = get_fake_candidate_page1()

    # 2. Truy cập và set Tiếng Việt
    apply_page.open_and_set_language(ATS_URL)

    # 3. Thực hiện điền form Trang 1
    apply_page.complete_page_1(data)

    # 4. KIỂM TRA ĐIỀU KIỆN PASS (Sang Trang 2)
    step_2_indicator = "//h3[contains(text(), 'Kinh nghiệm')] | //input[@id='company_name']"

    try:
        apply_page.wait_for_visible(step_2_indicator, timeout=15000)
        allure.step("Xác nhận đã sang Trang 2 thành công")
    except Exception as e:
        apply_page.take_screenshot("failed_to_reach_step_2")
        pytest.fail(f"Không thể chuyển sang Trang 2. Lỗi: {str(e)}")

    apply_page.take_screenshot("successfully_on_step_2")