from dataclasses import dataclass


@dataclass
class ats_login:
    email = "//input[@id='login']"
    password = "//input[@id='password']"
    set_again_transfer = "//label[@for='password']//a"
    register_transfer = "//a[@href='/web/signup']"
    login_btn = "//button[@type='submit']"
    apply_cv_transfer = "//div[@id='apply-job-btn']//p"