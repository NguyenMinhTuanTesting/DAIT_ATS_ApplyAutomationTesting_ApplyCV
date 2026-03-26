import allure
from core.base_page import BasePage
from locators.ats_list_candidate import ats_list_candidate


class ATSListCandidatePage(BasePage):
    @allure.step("Tìm kiếm ứng viên: {name}")
    def search_and_open_candidate(self, name: str):
        # Chuyển sang chế độ danh sách (List Mode) nếu cần
        if self.page.locator(ats_list_candidate.LIST_MODE).is_visible():
            self.click(ats_list_candidate.LIST_MODE)

        # Step 8: Dọn sạch thanh search (xóa bộ lọc mặc định)
        self.click(ats_list_candidate.SEARCH_BAR)
        self.page.keyboard.press("Control+A")
        self.page.keyboard.press("Backspace")

        # Điền tên và Enter
        self.type_and_verify(ats_list_candidate.SEARCH_BAR, name)
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(2000)  # Đợi kết quả search filter xong

        # Step 9: Click vào kết quả trùng tên
        candidate_item = self.page.locator(ats_list_candidate.CANDIDATE_NAME).filter(has_text=name).first
        candidate_item.click()