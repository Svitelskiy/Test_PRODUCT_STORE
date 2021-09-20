import time

from selenium.common.exceptions import TimeoutException

from locators.cart_order_locators import OrderPageLocators
from pages.cart_page import CartPage, OrderPage
from pages.login_page import LoginPage
from pages.main_page import DemoMainPage, PhonesCategory, EachProductClass
from pages.sign_page import SignUpPage
from utils import wait_for_alert_and_accept, wait_for_element_be_located


def test_add_cart_item(browser, user, order_info):
    main_page = DemoMainPage(browser)
    main_page.navigate_to_signup_page()

    SignUpPage(browser).enter_valid_credentials(login=user["login"], password=user["password"])
    wait_for_alert_and_accept(browser, 5)
    main_page.navigate_to_login_page()
    LoginPage(browser).enter_valid_credentials(login=user["login"], password=user["password"])

    time.sleep(2)
    DemoMainPage(browser).navigate_to_phone_category()

    time.sleep(2)
    PhonesCategory(browser).navigate_to_samsung_galaxy_product()

    time.sleep(2)
    product_po = EachProductClass(browser)

    product_po.add_product_to_cart()
    product_po.navigate_to_cart()
    time.sleep(2)
    try:
        wait_for_alert_and_accept(browser, 3)
    except TimeoutException:
        print("Alert message didn't appear")
    time.sleep(1)

    CartPage(browser).click_on_place_order()
    time.sleep(2)
    OrderPage(browser).enter_order_data(name=order_info["name"],
                                        city=order_info["city"],
                                        country=order_info["country"],
                                        credit_card=order_info["credit_card"],
                                        month=order_info["month"],
                                        year=order_info["year"])
    OrderPage(browser).click_purchase()

    OrderPage(browser, is_purchase_window_displayed=True).navigate_to_ok_button()


def test_delete_cart_item(browser, user):
    main_page = DemoMainPage(browser)
    main_page.navigate_to_signup_page()
    SignUpPage(browser).enter_valid_credentials(login=user["login"], password=user["password"])
    wait_for_alert_and_accept(browser, 5)

    main_page.navigate_to_login_page()
    LoginPage(browser).enter_valid_credentials(login=user["login"], password=user["password"])

    time.sleep(2)
    DemoMainPage(browser).navigate_to_phone_category()

    time.sleep(2)
    PhonesCategory(browser).navigate_to_samsung_galaxy_product()

    time.sleep(2)
    product = EachProductClass(browser)
    product.add_product_to_cart()
    product.navigate_to_cart()
    time.sleep(2)

    delete_product = CartPage(browser)
    delete_product.click_on_delete_button()

