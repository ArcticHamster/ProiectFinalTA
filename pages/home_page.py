from selenium.webdriver.common.by import By
import time
import random
from pages.base_page import BasePage


class HomePage(BasePage):
    HOME_PAGE_URL = "https://magento.softwaretestingboard.com/"
    LOGO_BUTTON = (By.XPATH, "//a[@class='logo']")
    SEARCH_BOX = (By.ID, "search")
    SEARCH_BUTTON = (By.XPATH, "//button[@class='action search']")
    SEARCH_RESULTS = (By.XPATH, "//div[@class='search results']//img[@class='product-image-photo']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@id='product-addtocart-button']")
    GENERATED_ERROR = (By.XPATH, "//div[@generated='true'][1]")
    SIZE_OPTION = (By.XPATH, "//div[@class='swatch-option text']")
    COLOR_OPTION = (By.XPATH, "//div[@class='swatch-option color']")
    ADDED_TO_CART_MESSAGE = (By.XPATH, "//div[@class='message-success success message']")
    SHOW_CART_BUTTON = (By.XPATH, "//a[@class='action showcart']")
    ITEMS_LIST = (By.XPATH, "//li[@data-role='product-item']")
    VIEW_AND_EDIT_CART_BUTTON = (By.XPATH, "//a[@class='action viewcart']")
    CART_ITEMS_LIST = (By.XPATH, "//tbody[@class='cart item']")
    SUBTOTAL_PRICE_PER_ITEM = (By.XPATH, "//tbody[@class='cart item']//td[@class='col subtotal']//span[@class='price']")
    SUBTOTAL = (By.XPATH, "//td[@class='amount']//span[@class='price']")

    def click_logo_button(self):
        self.click(self.LOGO_BUTTON)
        time.sleep(2)

    def set_search_term(self, term):
        self.type(self.SEARCH_BOX, term)
        time.sleep(1)

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)
        time.sleep(3)

    def click_random_product_from_search_result_list(self):
        search_result_list = self.driver.find_elements(*self.SEARCH_RESULTS)
        (random.choice(search_result_list)).click()
        time.sleep(1)

    def click_add_to_cart_button(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def is_error_message_displayed(self):
        return self.is_element_displayed(self.GENERATED_ERROR)

    def get_error_message_text(self):
        return self.get_text(self.GENERATED_ERROR)

    def click_random_size_of_selected_product(self):
        available_size = self.driver.find_elements(*self.SIZE_OPTION)
        (random.choice(available_size)).click()
        time.sleep(2)

    def click_random_color_of_selected_product(self):
        available_color = self.driver.find_elements(*self.COLOR_OPTION)
        (random.choice(available_color)).click()
        time.sleep(2)

    def is_confirmation_message_displayed(self):
        return self.is_element_displayed(self.ADDED_TO_CART_MESSAGE)

    def get_confirmation_message_text(self):
        return self.get_text(self.ADDED_TO_CART_MESSAGE)

    def click_show_cart_button(self):
        self.click(self.SHOW_CART_BUTTON)
        time.sleep(1)

    def is_cart_items_list_displayed(self):
        return self.is_element_displayed(self.ITEMS_LIST)

    def click_view_and_edit_cart_button(self):
        self.click(self.VIEW_AND_EDIT_CART_BUTTON)
        time.sleep(2)

    def calculate_cart_subtotal(self):
        subtotal_per_item_list = self.driver.find_elements(*self.SUBTOTAL_PRICE_PER_ITEM)
        index = 0
        subtotal = 0
        while index < len(subtotal_per_item_list):
            subtotal += float(subtotal_per_item_list[index].text[1:])
            index += 1
        return subtotal

    def get_subtotal_from_page(self):
        return float(self.get_text(self.SUBTOTAL)[1:])
