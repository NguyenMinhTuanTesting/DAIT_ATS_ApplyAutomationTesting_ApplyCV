import allure
from playwright.sync_api import Page
from core.base_page import BasePage
from locator.apply_cv import ApplyCVLocators_Page1, ApplyCVLocators_Base
from dto.candidate_dto import CandidatePage1DTO


class ApplyCVPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = ApplyCVLocators_Page1
        self.base_loc = ApplyCVLocators_Base

    @allure.step("Mở trang Apply CV và chuyển sang Tiếng Việt")
    def open_and_set_language(self, url: str):
        self.goto(url)
        # Chuyển đổi ngôn ngữ
        self.click("(//li[@data-name='Language Selector']//button)[1]")
        self.click("(//a[@title=' Tiếng Việt'])[1]")
        # Đợi trang reload và ổn định
        self.page.wait_for_load_state("networkidle")
        self.wait_for_visible(self.loc.NGANH_NGHE_UNG_TUYEN)

    @allure.step("Bước 1: Hoàn thiện ngành nghề ứng tuyển")
    def fill_job_info(self, data: CandidatePage1DTO):
        job = data.job_info
        self.dropdown_by_search(self.loc.NGANH_NGHE_UNG_TUYEN, job.job_apply)
        self.dropdown_by_search(self.loc.LINH_VUC, job.expertise)
        self.dropdown_by_search(self.loc.CAP_BAC, job.rank)
        self.type_and_verify(self.loc.DIA_DIEM_LAM_VIEC, job.work_location)
        self.dropdown_by_search(self.loc.VI_TRI_UNG_TUYEN, job.job_opening)

    @allure.step("Bước 2: Hoàn thiện thông tin cá nhân")
    def fill_personal_info(self, data: CandidatePage1DTO):
        per = data.personal_info
        # a) Upload ảnh đại diện
        self.upload_file(self.loc.AVATAR, per.avatar_path)

        # b-d) Họ tên, Giới tính, Ngày sinh
        self.type_and_verify(self.loc.HO_TEN_CA_NHAN, per.full_name)
        # Giới tính: Click vào radio/input tương ứng với text Nam/Nữ
        gender_xpath = f"//div[@id='gender']//label[contains(text(), '{per.gender}')]"
        self.click(gender_xpath)

        self.type_and_verify(self.loc.NGAY_SINH, per.dob)

        # e-h) Quốc tịch, Nơi sinh, Dân tộc, Tôn giáo
        self.dropdown_by_search(self.loc.QUOC_TICH, per.nationality)
        self.dropdown_by_search(self.loc.NOI_SINH, per.place_of_birth)
        self.dropdown_by_search(self.loc.DAN_TOC, per.ethnicity)
        self.dropdown_by_search(self.loc.TON_GIAO, per.religion)

        # i-k) CCCD
        self.type_and_verify(self.loc.CCCD, per.citizen_id)
        self.type_and_verify(self.loc.NGAY_CAP_CCCD, per.issued_date)
        self.dropdown_by_search(self.loc.NOI_CAP_CCCD, per.issued_place)

    @allure.step("Bước 3: Hoàn thiện thông tin địa chỉ")
    def fill_address_info(self, data: CandidatePage1DTO):
        addr = data.address_info
        # Thường trú
        self.type_and_verify(self.loc.DIA_CHI_THUONG_TRU, addr.perm_address)
        self.dropdown_by_search(self.loc.THUONG_TRU_TINH, addr.perm_province)
        self.dropdown_by_search(self.loc.THUONG_TRU_PHUONG, addr.perm_ward)

        # Tạm trú
        self.type_and_verify(self.loc.DIA_CHI_TAM_TRU, addr.temp_address)
        self.dropdown_by_search(self.loc.TAM_TRU_TINH, addr.temp_province)
        self.dropdown_by_search(self.loc.TAM_TRU_PHUONG, addr.temp_ward)

    @allure.step("Bước 4, 5, 6: Liên hệ, Mạng xã hội & Hôn nhân")
    def fill_contact_and_social(self, data: CandidatePage1DTO):
        contact = data.contact_info
        # Liên hệ
        self.type_and_verify(self.loc.SDT_1, contact.phone_1)
        self.type_and_verify(self.loc.EMAIL, contact.email)
        self.type_and_verify(self.loc.TEN_NGUOI_LIEN_HE_KHAN, contact.emergency_name)
        self.type_and_verify(self.loc.SDT_LIEN_HE_KHAN, contact.emergency_phone)
        self.type_and_verify(self.loc.MOI_QUAN_HE_KHAN, contact.emergency_relation)

        # Mạng xã hội
        if contact.facebook:
            self.type_and_verify(self.loc.FACEBOOK, contact.facebook)
        if contact.linkedin:
            self.type_and_verify(self.loc.LINKEDIN, contact.linkedin)

        # Hôn nhân
        self.dropdown_by_search(self.loc.TINH_TRANG_HON_NHAN, contact.marital_status)

    @allure.step("Bước 7: Nhấn Next sang trang 2")
    def click_next(self):
        self.click(self.base_loc.TIEP_THEO)
        # Đợi một element đặc trưng của trang 2 xuất hiện để verify chuyển trang thành công
        # Ví dụ: self.page.wait_for_selector("//h3[contains(text(), 'Kinh nghiệm')]", timeout=10000)

    def complete_page_1(self, data: CandidatePage1DTO):
        """Hàm tổng hợp chạy toàn bộ các bước của Trang 1"""
        self.fill_job_info(data)
        self.fill_personal_info(data)
        self.fill_address_info(data)
        self.fill_contact_and_social(data)
        self.click_next()