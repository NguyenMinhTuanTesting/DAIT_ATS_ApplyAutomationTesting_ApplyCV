import allure
from core.base_page import BasePage
from locators.ats_dashboard import ats_dashboard


class ATSDashboardPage(BasePage):
    @allure.step("Bước 4: Click button module tuyển dụng")
    def transfer_to_recruitment(self):
        # Click xong là xong, Playwright sẽ tự đợi nút có thể click được
        self.click(ats_dashboard.TUYENDUNG_MODULE)

    @allure.step("Bước 5 & 6: Chuyển đến Danh sách ứng viên")
    def transfer_to_all_candidates(self):
        # Bước 5: Click dropdown ứng viên
        self.page.wait_for_timeout(3000)
        self.click(ats_dashboard.TUYENDUNG_CANDIDATE_DROPDOWN)

        # Bước 6: Click option danh sách ứng viên
        self.click(ats_dashboard.DANH_SACH_UNG_VIEN_TRANSFER)