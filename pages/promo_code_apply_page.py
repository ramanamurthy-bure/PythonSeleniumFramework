from selenium.webdriver.common.by import By

from locators.locators import Locators


class PromoCode(object):
    def __init__(self, driver):
        self.driver = driver
        self.promo_code_info = driver.find_element(By.CSS_SELECTOR, Locators.promo_code_info)

    def get_promo_code_info(self):
        return self.promo_code_info
