from driver import Driver
from pages.login_page import LoginPage
from pages.signup_page import SignUpPage
from pages.base_page import BasePage


def before_all(context):
    context.browser = Driver()
    context.login_page = LoginPage()
    context.signup_page = SignUpPage()
    context.base_page = BasePage()


def after_all(context):
    context.browser.close()
