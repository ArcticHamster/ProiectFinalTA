from driver import Driver
import random
import string
from selenium.webdriver.support.select import Select

class BasePage(Driver):
    pass

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def double_type(self, locator1, locator2, text):
        self.find(locator1).send_keys(text)
        self.find(locator2).send_keys(text)

    def is_element_displayed(self, locator):
        return self.find(locator).is_displayed()

    def get_text(self, locator):
        return self.find(locator).text

    def is_url_as_expected(self, expected_url):
        return expected_url == self.driver.current_url

    def randomtext(self, complexity, length):

        if complexity == 'weak':
            return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

        if complexity == 'medium':
            return ''.join(random.choice(string.ascii_letters) for i in range(length))

        if complexity == 'strong':
            return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))

        if complexity == 'super_strong':
            return ''.join(random.choice(string.printable) for i in range(length))

        if complexity == 'special':
            return ''.join(random.choice(string.punctuation) for i in range(length))

        if complexity == 'numbers':
            return ''.join(random.choice(string.digits) for i in range(length))

    def select_dropdown_element_by_text(self, dropdown_locator, text):
        dropdown_element = self.find(dropdown_locator)
        select = Select(dropdown_element)
        select.select_by_visible_text(text)