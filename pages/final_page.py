from selenium.webdriver.common.by import By

from locators.locators import Locators


class GreenkartFinal(object):
    def __init__(self, driver):
        self.driver = driver

        self.elm_success_message = driver.find_element(By.XPATH, Locators.success_message)

    def get_success_message(self):
        return self.elm_success_message
