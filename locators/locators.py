class Locators(object):
    # Home Page Locators
    veg_search_textbox = "//input[@type='search']"
    veg_search_button = "//button[@type='submit']"
    veg_search_results = ".products img"
    add_to_cart = "//button[contains(text(),'ADD TO CART')]"
    veg_cart_btn = "// img[ @ alt = 'Cart']"

    # Proceed to Check Out Page
    proceed_to_checkout_btn = "//button[contains(text(),'PROCEED TO CHECKOUT')]"

    # Place Order Page
    promo_code_textbox = ".promocode"
    promo_code_apply_btn = "button.promoBtn"
    place_an_order = "//button[contains(text(),'Place Order')]"

    # Promo Code Info
    promo_code_info = ".promoInfo"

    # GreenkartPayment Page
    choose_country_drpdown = "//label[contains(text(),'Choose Country')]/following::select"
    agree_checkbox = ".chkAgree"
    proceed_btn = "//button[text()='Proceed']"
    success_message = "//span[contains(text(),'Thank you')]"

