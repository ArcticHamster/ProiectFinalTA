from selenium.webdriver.common.by import By
import time

from pages.base_page import BasePage


class SignUpPage(BasePage):
    SIGNUP_PAGE_URL = "https://magento.softwaretestingboard.com/customer/account/create"
    FIRST_NAME_INPUT = (By.ID, "firstname")
    LAST_NAME_INPUT = (By.ID, "lastname")
    EMAIL_INPUT = (By.ID, "email_address")
    PASSWORD_INPUT = (By.ID, "password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "password-confirmation")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".action.submit.primary")
    ACCOUNT_ERROR_MESSAGE = (By.XPATH, "//div[@class='message-error error message']")

    def navigate_to_signup_page(self):
        self.driver.get(self.SIGNUP_PAGE_URL)
        time.sleep(2)

    def set_first_name(self, first_name):
        self.type(self.FIRST_NAME_INPUT, first_name)

    def set_last_name(self, last_name):
        self.type(self.LAST_NAME_INPUT, last_name)
        time.sleep(1)

    def set_email(self, email):
        self.type(self.EMAIL_INPUT, email)
        time.sleep(1)

    def set_random_email(self, email):
        self.type(self.EMAIL_INPUT, email)
        time.sleep(1)

    def set_password_and_confirm(self, password):
        self.double_type(self.PASSWORD_INPUT, self.CONFIRM_PASSWORD_INPUT, password)

    def click_create_account_button(self):
        self.click(self.CREATE_ACCOUNT_BUTTON)
        time.sleep(3)

    def is_error_message_displayed(self):
        return self.is_element_displayed(self.ACCOUNT_ERROR_MESSAGE)

    def get_error_message_text(self):
        return self.get_text(self.ACCOUNT_ERROR_MESSAGE)
