from selenium.webdriver.common.by import By
import time
import random
from pages.base_page import BasePage

class HomePage(BasePage):
    HOME_PAGE_URL = "https://magento.softwaretestingboard.com/"
    LOGO_BUTTON = (By.XPATH, "//a[@class='logo']")
    SEARCH_BOX = (By.XPATH, "//.[@id='search']")
    SEARCH_RESULTS = (By.XPATH, "//.[@class='product-image-photo']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@id='product-addtocart-button']")
    GENERATED_ERROR = (By.XPATH, "//div[@generated='true']")

    def click_logo_button(self):
        self.click(self.LOGO_BUTTON)

    def set_search_term(self, term):
        self.type(self.SEARCH_BOX, term)
        time.sleep(1)

    def click_random_product_from_search_result_list(self):
        search_result_list = self.driver.find_elements(self.SEARCH_RESULTS)
        self.click(random.choice(search_result_list))
        time.sleep(1)

    def click_add_to_cart_button(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def check_error_presence

