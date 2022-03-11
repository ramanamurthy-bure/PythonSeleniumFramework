from selenium.webdriver.common.by import By

from locators.locators import Locators


class GreenkartPayment(object):
    def __init__(self, driver):
        self.driver = driver

        self.elm_choose_country_drpdown = driver.find_element(By.XPATH, Locators.choose_country_drpdown)
        self.elm_agree_checkbox = driver.find_element(By.CSS_SELECTOR, Locators.agree_checkbox)
        self.elm_proceed_btn = driver.find_element(By.XPATH, Locators.proceed_btn)

    def get_choose_country_drpdown(self):
        return self.elm_choose_country_drpdown

    def get_agree_checkbox(self):
        return self.elm_agree_checkbox

    def get_proceed_btn(self):
        return self.elm_proceed_btn
