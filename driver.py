from selenium import webdriver


class Driver:
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.implicitly_wait(3)

    def close(self):
        self.driver.quit()