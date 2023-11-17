from selenium.webdriver.common.by import By
import time

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_PAGE_URL = "https://magento.softwaretestingboard.com/customer/account/login"

    # definim selectorii
    # ACCEPTA_COOKIES_BUTTON = (By.CSS_SELECTOR, "button.amgdprcookie-button.-allow.-save")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "pass")
    SIGN_IN_BUTTON = (By.ID, "send2")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.message-error")
    ACCOUNT_INFORMATIONS = (By.CSS_SELECTOR, ".box-information > div:nth-child(2)")
    LOGGED_IN_DROPDOWN_MENU = (By.XPATH, "(//button[@class='action switch'])[1]")
    SIGN_OUT_MENU_OPTION = (By.LINK_TEXT, "Sign Out")
    FORGOT_PSWD_LINK = (By.XPATH, "//a[@class='action remind']")
    FORGOT_PSWD_EMAIL_INPUT = (By.XPATH, "//input[@id='email_address']")
    RESET_PSWD_BUTTON = (By.XPATH, "//button[@class='action submit primary']")
    RESET_PSWD_SUCCESS_MESSAGE = (By.XPATH, "//div[@class='message-success success message']")

    # definim actiunile
    def navigate_to_login_page(self):
        self.driver.delete_all_cookies()
        self.driver.get(self.LOGIN_PAGE_URL)
        time.sleep(1)

    # def accept_cookies_ckeck(self):
    #     if self.is_element_displayed(self.ACCEPTA_COOKIES_BUTTON):
    #         self.click(self.ACCEPTA_COOKIES_BUTTON)
    #     else:
    #         pass

    def set_email(self, email):
        self.type(self.EMAIL_INPUT, email)
        time.sleep(1)

    def set_password(self, password):
        self.type(self.PASSWORD_INPUT, password)
        time.sleep(1)

    def click_sign_in_button(self):
        self.click(self.SIGN_IN_BUTTON)
        time.sleep(3)

    def is_error_message_displayed(self):
        return self.is_element_displayed(self.ERROR_MESSAGE)

    def get_error_message_text(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_user_name(self):
        return self.get_text(self.ACCOUNT_INFORMATIONS)

    def click_logged_in_dropdown_menu(self):
        self.click(self.LOGGED_IN_DROPDOWN_MENU)

    def click_sign_out_menu_option(self):
        self.click(self.SIGN_OUT_MENU_OPTION)

    def click_forgot_password_link(self):
        self.click(self.FORGOT_PSWD_LINK)

    def set_forgot_pswd_email(self):
        email = self.randomtext('weak', 10) + '@email.com'
        self.type(self.FORGOT_PSWD_EMAIL_INPUT, email)

    def click_reset_pswd_button(self):
        self.click(self.RESET_PSWD_BUTTON)

    def is_success_message_displayed(self):
        return self.is_element_displayed(self.RESET_PSWD_SUCCESS_MESSAGE)

    def get_success_message_text(self):
        return self.get_text(self.RESET_PSWD_SUCCESS_MESSAGE)
