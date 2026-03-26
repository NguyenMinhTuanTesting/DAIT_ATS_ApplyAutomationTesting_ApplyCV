import os
import allure
import pytest
from dotenv import load_dotenv
from pages.login_page import ATSLoginPage
from data.ta_login_data import VALID_TA_LOGIN, INVALID_TA_LOGIN

load_dotenv()
ATS_URL = os.getenv("URL_ATS_LOGIN")

@pytest.fixture
def page(browser, browser_context_args):
    """Tạo session và tab mới cho mỗi case"""
    context = browser.new_context(**browser_context_args)
    page = context.new_page()
    yield page
    context.close()

@allure.feature("ATS Login")
class TestATSLogin:

    @allure.story("Login Success")
    def test_login_success(self, page):
        login_page = ATSLoginPage(page)
        login_page.open(ATS_URL)
        login_page.login(VALID_TA_LOGIN)
        login_page.take_screenshot("login_success")
        assert "odoo" in page.url

    @allure.story("Login Fail")
    def test_login_fail(self, page):
        login_page = ATSLoginPage(page)
        login_page.open(ATS_URL)
        login_page.login(INVALID_TA_LOGIN)
        login_page.take_screenshot("login_fail")
        assert "login" in page.url

    @allure.story("Transfer Forget Password")
    def test_transfer_forget_password(self, page):
        login_page = ATSLoginPage(page)
        login_page.open(ATS_URL)
        login_page.go_to_forget_password()
        login_page.take_screenshot("forget_password")
        assert "password" in page.url

    @allure.story("Transfer Register Page")
    def test_transfer_register(self, page):
        login_page = ATSLoginPage(page)
        login_page.open(ATS_URL)
        login_page.go_to_register()
        login_page.take_screenshot("register_page")
        assert "signup" in page.url

    @allure.story("Transfer Apply CV Page")
    def test_transfer_apply_cv(self, page):
        login_page = ATSLoginPage(page)
        login_page.open(ATS_URL)
        login_page.go_to_apply_cv()
        login_page.take_screenshot("apply_cv")
        assert "apply" in page.url