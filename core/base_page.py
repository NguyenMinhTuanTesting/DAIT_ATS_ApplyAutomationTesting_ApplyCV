import logging
import allure
from playwright.sync_api import Page, expect
from typing import Optional


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)

    @allure.step("Nhập liệu bằng cách gõ phím: '{value}' vào {selector}")
    def type_and_verify(self, selector: str, value: str, delay: int = 50, timeout: float = 10000):
        """
        Xóa trắng và gõ từng ký tự (mimic human typing) để kích hoạt sự kiện UI.
        """
        self.logger.info(f"Typing '{value}' into {selector}")
        self.highlight(selector)

        locator = self.page.locator(selector)
        # 1. Click và Xóa dữ liệu cũ
        locator.click()
        locator.clear()

        # 2. Gõ từng phím với độ trễ (mặc định 50ms giữa các phím)
        locator.press_sequentially(value, delay=delay, timeout=timeout)

        # 3. Xác minh kết quả
        try:
            expect(locator).to_have_value(value, timeout=3000)
        except AssertionError:
            self.logger.error(f"Typing verification failed for {selector}. Expected: {value}")
            raise

    # --- Dropdown selection (2 OPTIONS) ---
    @allure.step("dropdown: Tìm kiếm và chọn '{option_text}' qua {trigger_selector}")
    def dropdown_by_search(self, trigger_selector: str, option_text: str,
                           search_input_selector: str = "//input[@role='searchbox' or @type='search']"):
        """
        Cải tiến: Thêm tham số search_input_selector để linh hoạt hơn.
        Mặc định dùng các selector phổ biến của Select2/AntD/Bootstrap.
        """
        self.logger.info(f"dropdown by Search: '{option_text}' via {trigger_selector}")

        # 1. Click mở dropdown
        self.click(trigger_selector)

        # 2. Đợi ô search hiển thị và nhập liệu với delay để tránh lỗi UI
        self.page.wait_for_selector(search_input_selector, state="visible", timeout=5000)
        search_field = self.page.locator(search_input_selector)

        # Xóa trắng trước khi gõ (nếu có rác)
        search_field.click()
        # Gõ từ khóa với delay 50ms để UI kịp filter
        search_field.press_sequentially(option_text, delay=50)

        # 3. Đợi kết quả filter hiển thị (Tránh click nhầm item cũ)
        item_xpath = f"//ul[@role='listbox']//li[contains(normalize-space(), '{option_text}')]"
        self.page.wait_for_selector(item_xpath, state="visible", timeout=5000)

        # 4. Click chọn item
        self.click(item_xpath)

    @allure.step("dropdown: Chọn trực tiếp '{option_text}' từ {trigger_selector}")
    def dropdown_by_text(self, trigger_selector: str, option_text: str):
        """
        Dùng khi danh sách ngắn: Click -> Click trực tiếp vào text mong muốn.
        """
        self.logger.info(f"dropdown by Direct Text: '{option_text}' via {trigger_selector}")

        # 1. Click mở dropdown
        self.click(trigger_selector)

        # 2. Đợi listbox hiện ra và click trực tiếp vào text
        item_xpath = f"//ul[@role='listbox']//li[contains(normalize-space(), '{option_text}')]"
        self.click(item_xpath)
    # --- CÁC ACTION NỀN TẢNG ---
    @allure.step("Click vào element: {selector}")
    def click(self, selector: str, timeout: float = 10000):
        self.logger.info(f"Clicking on {selector}")
        self.highlight(selector)
        self.page.click(selector, timeout=timeout)

    @allure.step("Mở URL: {url}")
    def goto(self, url: str):
        self.logger.info(f"Navigating to: {url}")
        self.page.goto(url, wait_until="networkidle")

    @allure.step("Upload file vào {selector}")
    def upload_file(self, selector: str, file_path: str):
        self.logger.info(f"Uploading file: {file_path}")
        self.page.set_input_files(selector, file_path)

    @allure.step("Chọn trạng thái checkbox/radio: {checked} cho {selector}")
    def set_checked(self, selector: str, checked: bool = True):
        locator = self.page.locator(selector)
        if checked:
            locator.check()
        else:
            locator.uncheck()
    # ---XÁC MINH & DEBUG ---
    @allure.step("Xác nhận {selector} hiển thị")
    def wait_for_visible(self, selector: str, timeout: float = 10000):
        expect(self.page.locator(selector)).to_be_visible(timeout=timeout)

    def highlight(self, selector: str):
        """Hiệu ứng trực quan khi chạy test mode Headed"""
        try:
            self.page.locator(selector).evaluate(
                "el => { el.style.border = '2px solid red'; el.style.backgroundColor = 'rgba(255, 255, 0, 0.3)'; }"
            )
        except:
            pass

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text().strip()

    def take_screenshot(self, name: str):
        allure.attach(
            self.page.screenshot(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )