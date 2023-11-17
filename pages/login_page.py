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
    LOGGED_IN_DROPDOWN_MENU = (By.XPATH, "//button[@class='action switch'][1]")
    SIGN_OUT_MENU_OPTION = (By.LINK_TEXT, "Sign Out")

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
