import os
import allure
import pytest
from dotenv import load_dotenv
from playwright.sync_api import expect

# Import DTOs và Generator
from dto.ta_login_dto import TALoginDTO
from data.candidate_generator import CandidateGenerator

# Import Page Objects
from pages.apply_cv_page import ApplyCVPage
from pages.login_page import ATSLoginPage
from pages.dashboard_page import ATSDashboardPage
from pages.list_candidate_page import ATSListCandidatePage
from pages.detail_candidate_page import ATSCandidateDetailPage

load_dotenv()


@allure.feature("E2E Recruitment Flow")
@allure.story("Apply CV and Verify in ATS")
def test_apply_cv_and_verify_ats(browser, browser_context_args):
    # --- 0. CHUẨN BỊ ---
    gen = CandidateGenerator()
    candidate = gen.get_candidate()

    # Đóng gói dữ liệu TA vào DTO
    ta_login_dto = TALoginDTO(
        email=os.getenv("TA_EMAIL"),
        password=os.getenv("TA_PASSWORD")
    )

    # --- GIAI ĐOẠN 1: SESSION ỨNG VIÊN ---
    candidate_context = browser.new_context(**browser_context_args)
    candidate_page = candidate_context.new_page()
    apply_page = ApplyCVPage(candidate_page)

    with allure.step("BƯỚC 1: Ứng viên nộp hồ sơ"):
        apply_page.goto(os.getenv("URL_APPLY_CV"))
        apply_page.setup_language_vi()

        # Điền 4 trang
        apply_page.fill_page_1(candidate.page_1)
        apply_page.fill_page_2(candidate.page_2)
        apply_page.fill_page_3(candidate.page_3)
        apply_page.fill_page_4(candidate.page_4)

        # Chỉ cần đợi request cuối bay đi là đóng session
        candidate_page.wait_for_load_state("networkidle", timeout=5000)
        candidate_context.close()
        print(f"Đã nộp hồ sơ xong cho: {candidate.page_1.full_name}")

    # --- GIAI ĐOẠN 2: SESSION TA (Verify trên ATS) ---
    with allure.step("BƯỚC 2: TA kiểm tra hồ sơ trên ATS"):
        ta_context = browser.new_context(**browser_context_args)
        ta_page = ta_context.new_page()

        # 1. Login
        login_page = ATSLoginPage(ta_page)
        login_page.open(os.getenv("URL_ATS_LOGIN"))
        login_page.login(ta_login_dto)

        # 2. Dashboard:chuyển tới danh sách ứng viên
        dashboard = ATSDashboardPage(ta_page)
        dashboard.transfer_to_recruitment()
        dashboard.transfer_to_all_candidates()

        # 3. List: Bước 7, 8, 9 (Search và Click ứng viên)
        list_page = ATSListCandidatePage(ta_page)
        list_page.search_and_open_candidate(candidate.page_1.full_name)

        # 4. Detail: Bước 10 (Verify dữ liệu)
        detail_page = ATSCandidateDetailPage(ta_page)
        detail_page.verify_candidate_e2e(candidate)

        ta_context.close()