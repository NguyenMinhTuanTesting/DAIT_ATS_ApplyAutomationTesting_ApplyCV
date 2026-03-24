import allure
from core.base_page import BasePage
from locators.ats_login import ats_login
from dto.ta_login_dto import TALoginDTO


class ATSLoginPage(BasePage):

    @allure.step("Open ATS Login Page")
    def open(self, url: str):
        self.goto(url)

    @allure.step("Login ATS")
    def login(self, login_dto: TALoginDTO):
        self.type_and_verify(ats_login.email, login_dto.email)
        self.type_and_verify(ats_login.password, login_dto.password)
        self.click(ats_login.login_btn)

    @allure.step("Go to Forget Password Page")
    def go_to_forget_password(self):
        self.click(ats_login.set_again_transfer)

    @allure.step("Go to Register Page")
    def go_to_register(self):
        self.click(ats_login.register_transfer)

    @allure.step("Go to Apply CV Page")
    def go_to_apply_cv(self):
        self.click(ats_login.apply_cv_transfer)