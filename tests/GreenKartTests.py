import time
import unittest
import warnings

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from base.webdriver_factory import WebDriverSetup
from pages.final_page import GreenkartFinal
from pages.greenkart_home_page import GreenKartHome
from pages.payment_page import GreenkartPayment
from pages.place_order_page import PlaceOrder
from pages.proceed_to_checkout_page import ProceedToCheckOut
from pages.promo_code_apply_page import PromoCode


class GreenkartHomeTests(unittest.TestCase):
    driver = None
    waittime = None

    def test1_setupdriver(self):
        print("*********************************** Test-1 **************************************")
        # To ignore the resource warnings message to console
        warnings.simplefilter('ignore', ResourceWarning)
        if self.driver is None:
            objWebDriverSetup = WebDriverSetup()
            self.__class__.driver = objWebDriverSetup.launch_application()
        if self.waittime is None:
            self.__class__.waittime = WebDriverWait(self.driver, 60)

    def test2_add_vegs_tokart(self):
        print("*********************************** Test-2 **************************************")
        objGreenKartHome = GreenKartHome(self.driver)

        # To enter the veg names in the search box
        elm_veg_search_textbox = objGreenKartHome.get_search_box()
        elm_veg_search_textbox.click()
        time.sleep(1)
        elm_veg_search_textbox.send_keys("ber")
        time.sleep(3)
        print("Entered 'ber' in the search text box")

        # To enter the veg names in the search box
        elm_veg_search_button = objGreenKartHome.get_search_button()
        elm_veg_search_button.click()
        print("Clicked on 'search' veg icon")
        time.sleep(3)

        objGreenKartHome = GreenKartHome(self.driver)
        elm_veg_search_results = objGreenKartHome.get_search_results()
        results_count = len(elm_veg_search_results)
        print("Total results displayed count : " + str(results_count))

        elm_addtocart_btns = objGreenKartHome.get_add_to_cart_button()
        for elmbtn in elm_addtocart_btns:
            elmbtn.click()
        print("Added all the results to Card for purchase")

    def test3_proceed_to_checkout(self):
        print("*********************************** Test-3 **************************************")
        objGreenKartHome = GreenKartHome(self.driver)
        elm_cart_btn = objGreenKartHome.get_cart_button()
        elm_cart_btn.click()
        print("Clicked on 'Cart' button")

        objProceedToCheckOut = ProceedToCheckOut(self.driver)
        elm_proceed_to_checkout_btn = objProceedToCheckOut.get_proceed_to_checkout_btn()
        elm_proceed_to_checkout_btn.click()
        print("Clicked on 'Proceed to checkout' button")

    def test4_promo_code_apply(self):
        print("*********************************** Test-4 **************************************")
        objPlaceOrder = PlaceOrder(self.driver)
        self.waittime.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promocode")))
        elm_promocode_textbox = objPlaceOrder.get_promo_code_textbox()
        elm_promocode_textbox.send_keys("rahulshettyacademy")
        print("Entered 'rahulshettyacademy' in the coupon textbox")

        objPlaceOrder = PlaceOrder(self.driver)
        elm_promocode_apply_btn = objPlaceOrder.get_promo_code_apply_btn()
        elm_promocode_apply_btn.click()
        print("Clicked on 'Apply' coupon button")

        objPromoCode = PromoCode(self.driver)
        self.waittime.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
        elm_promoinfo_msg = objPromoCode.get_promo_code_info()
        print("Fetched the coupon info from the UI '" + elm_promoinfo_msg.text + "'")

        assert elm_promoinfo_msg.text == "Code applied ..!"
        print("Asserted coupon validation with the expected value and passed")

    def test5_place_order(self):
        print("*********************************** Test-5 **************************************")
        objPlaceOrder = PlaceOrder(self.driver)
        elm_place_order = objPlaceOrder.get_place_order_btn()
        elm_place_order.click()
        print("Clicked on the 'Place Order' button")

    def test6_payment(self):
        print("*********************************** Test-6 **************************************")
        objPayment = GreenkartPayment(self.driver)
        elm_choose_country_drpdown = objPayment.get_choose_country_drpdown()
        drpdown_county = Select(elm_choose_country_drpdown)
        drpdown_county.select_by_value("India")
        print("Selected country as 'India' from dropdown")

        elm_agree_checkbox = objPayment.get_agree_checkbox()
        elm_agree_checkbox.click()
        assert elm_agree_checkbox.is_selected()
        print("Selected agree terms and conditions checkbox and asserted successfully")

        elm_proceed_btn = objPayment.get_proceed_btn()
        elm_proceed_btn.click()
        print("Clicked on the 'Proceed' button")

    def test7_greenkat_success(self):
        print("*********************************** Test-7 **************************************")
        objGreenkartFinal = GreenkartFinal(self.driver)
        # To validate the success message
        elm_success_message = objGreenkartFinal.get_success_message()
        assert "Thank you, your order has been placed successfully" in elm_success_message.text
        print("purchase success!!!")

    def test8_close_application(self):
        print("*********************************** Test-8 **************************************")
        print("Quiting browser")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
