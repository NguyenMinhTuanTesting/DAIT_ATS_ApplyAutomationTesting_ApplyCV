import logging
import os

import allure
from playwright.sync_api import Page, expect
from typing import Optional

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)

    @allure.step("Nhập liệu: '{value}' vào {selector}")
    def type_and_verify(self, selector: str, value: str, delay: int = 50, timeout: float = 10000):
        self.logger.info(f"Typing '{value}' into {selector}")
        self.highlight(selector)
        locator = self.page.locator(selector)
        locator.click()
        locator.clear()
        locator.press_sequentially(value, delay=delay, timeout=timeout)
        expect(locator).to_have_value(value, timeout=3000)

    @allure.step("Dropdown search: chọn '{option_text}' qua {trigger_selector}")
    def dropdown_by_search(self, trigger_selector: str, option_text: str,
                           search_input_selector: str = "//input[@role='searchbox' or @type='search']"):
        self.logger.info(f"Dropdown search: '{option_text}' via {trigger_selector}")
        self.click(trigger_selector)
        search_field = self.page.locator(search_input_selector).last
        search_field.wait_for(state="visible", timeout=5000)
        search_field.fill(option_text)
        self.page.wait_for_timeout(500)
        item = self.page.locator("ul[role='listbox'] li").filter(has_text=option_text).first

        try:
            item.wait_for(state="visible", timeout=5000)
            item.click()
        except Exception:
            item.click(force=True)

    @allure.step("Dropdown text: chọn '{option_text}' qua {trigger_selector}")
    def dropdown_by_text(self, trigger_selector: str, option_text: str):
        self.logger.info(f"Dropdown text: '{option_text}' via {trigger_selector}")
        self.click(trigger_selector)
        item_xpath = f"//ul[@role='listbox']//li[contains(normalize-space(), '{option_text}')]"
        self.click(item_xpath)

    @allure.step("Click: {selector}")
    def click(self, selector: str, timeout: float = 10000):
        self.logger.info(f"Clicking {selector}")
        self.highlight(selector)
        self.page.click(selector, timeout=timeout)

    @allure.step("Goto: {url}")
    def goto(self, url: str):
        self.logger.info(f"Navigating to {url}")
        self.page.goto(url, wait_until="networkidle")

    @allure.step("Upload file: {selector}")
    def upload_file(self, selector: str, file_path: str):
        if not file_path:
            self.logger.error("Đường dẫn file bị rỗng!")
            return

        # Chuẩn hóa đường dẫn tuyệt đối
        absolute_path = os.path.abspath(os.path.normpath(file_path))

        if not os.path.exists(absolute_path):
            self.logger.error(f"❌ File không tồn tại: {absolute_path}")
            return

        self.logger.info(f"✅ Đang upload: {absolute_path}")

        # Tìm locator mục tiêu
        target = self.page.locator(selector)

        # KIỂM TRA: Nếu selector không phải thẻ INPUT, tìm thẻ INPUT ẩn bên trong hoặc lân cận
        is_input = target.evaluate("node => node.tagName === 'INPUT'")

        if not is_input:
            # Tìm thẻ input[type='file'] là con hoặc là anh em gần nhất
            final_locator = self.page.locator(f"{selector} >> xpath=..//input[@type='file']").first
        else:
            final_locator = target

        # Thực hiện upload và đợi một chút để website xử lý ảnh
        final_locator.set_input_files(absolute_path)
        self.page.wait_for_timeout(2000)

    @allure.step("Set checked: {checked} cho {selector}")
    def set_checked(self, selector: str, checked: bool = True):
        locator = self.page.locator(selector)
        if checked:
            locator.check()
        else:
            locator.uncheck()

    @allure.step("Nhập tiền tệ: '{value}' vào {selector}")
    def type_currency(self, selector: str, value: str, timeout: float = 3000):
        """
        Dành cho các ô tự động format dấu phẩy (20,000,000)
        """
        self.logger.info(f"Typing currency '{value}' into {selector}")
        self.highlight(selector)
        locator = self.page.locator(selector)

        locator.click()
        locator.clear()
        locator.press_sequentially(value, delay=50)

        # Tự động định dạng value để verify: 20000000 -> 20,000,000
        # Dùng f-string hoặc format để thêm dấu phẩy ngăn cách hàng nghìn
        formatted_value = "{:,}".format(int(value))

        self.logger.info(f"Expecting formatted value: {formatted_value}")
        expect(locator).to_have_value(formatted_value, timeout=timeout)

    @allure.step("Nhập ngày tháng thông minh: '{value}' vào {selector}")
    def fill_date(self, selector: str, value: str):
        """
        Tự động nhận diện type='date' hoặc type='text' để điền đúng định dạng.
        Chấp nhận đầu vào: YYYY-MM-DD, YYYY-MM hoặc DD/MM/YYYY
        """
        locator = self.page.locator(selector)
        input_type = locator.get_attribute("type")

        # 1. Chuẩn hóa dữ liệu đầu vào về các thành phần Ngày, Tháng, Năm
        # Dù bạn truyền 2023-11-26 hay 26/11/2023 thì cũng tách ra được
        val = value.replace("/", "-")
        parts = val.split("-")

        if len(parts[0]) == 4:  # Định dạng YYYY-MM-DD
            y, m = parts[0], parts[1]
            d = parts[2] if len(parts) > 2 else "01"
        else:  # Định dạng DD-MM-YYYY
            d, m, y = parts[0], parts[1], parts[2]

        # 2. Quyết định định dạng điền vào dựa trên TYPE của thẻ input
        if input_type == "date":
            # Thẻ date xịn: Bắt buộc YYYY-MM-DD
            final_value = f"{y}-{m.zfill(2)}-{d.zfill(2)}"
        else:
            # Thẻ text (như ô Ngày Sinh): Thường dùng DD/MM/YYYY
            final_value = f"{d.zfill(2)}/{m.zfill(2)}/{y}"

        self.logger.info(f"Detected type '{input_type}'. Filling: {final_value}")
        self.highlight(selector)

        # 3. Điền và Verify
        locator.fill(final_value)
        expect(locator).to_have_value(final_value, timeout=3000)

    @allure.step("Wait visible: {selector}")
    def wait_for_visible(self, selector: str, timeout: float = 10000):
        expect(self.page.locator(selector)).to_be_visible(timeout=timeout)

    def highlight(self, selector: str):
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