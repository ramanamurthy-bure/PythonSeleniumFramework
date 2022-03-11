from selenium.webdriver.common.by import By

from locators.locators import Locators


class ProceedToCheckOut(object):
    def __init__(self, driver):
        self.driver = driver

        self.elm_proceed_to_checkout_btn = driver.find_element(By.XPATH, Locators.proceed_to_checkout_btn)

    def get_proceed_to_checkout_btn(self):
        return self.elm_proceed_to_checkout_btn
