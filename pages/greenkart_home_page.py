from selenium.webdriver.common.by import By

from locators.locators import Locators


class GreenKartHome(object):
    def __init__(self, driver):
        self.driver = driver

        self.elm_veg_search_textbox = driver.find_element(By.XPATH, Locators.veg_search_textbox)
        self.elm_veg_search_button = driver.find_element(By.XPATH, Locators.veg_search_button)
        self.elm_veg_search_results = driver.find_elements(By.CSS_SELECTOR, Locators.veg_search_results)
        self.elm_add_to_cart_btn = driver.find_elements(By.XPATH, Locators.add_to_cart)
        self.elm_cart_btn = driver.find_element(By.XPATH, Locators.veg_cart_btn)



    def get_search_box(self):
        return self.elm_veg_search_textbox

    def get_search_button(self):
        return self.elm_veg_search_button

    def get_search_results(self):
        return self.elm_veg_search_results

    def get_add_to_cart_button(self):
        return self.elm_add_to_cart_btn

    def get_cart_button(self):
        return self.elm_cart_btn
