from selenium.webdriver.common.by import By

from locators.locators import Locators


class PlaceOrder(object):
    def __init__(self, driver):
        self.driver = driver
        self.promo_code_textbox = driver.find_element(By.CSS_SELECTOR, Locators.promo_code_textbox)
        self.promo_code_apply_btn = driver.find_element(By.CSS_SELECTOR, Locators.promo_code_apply_btn)
        self.place_order_btn = driver.find_element(By.XPATH, Locators.place_an_order)

    def get_promo_code_textbox(self):
        return self.promo_code_textbox

    def get_promo_code_apply_btn(self):
        return self.promo_code_apply_btn

    def get_place_order_btn(self):
        return self.place_order_btn
