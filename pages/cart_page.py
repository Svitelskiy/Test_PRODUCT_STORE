import time
from locators.card_locators import CardLocators
from locators.cart_order_locators import OrderPageLocators
from utils import wait_for_element_be_located


class CartPage:
    def __init__(self, browser):
        self.browser = browser

        self.delete_button = self.browser.find_element(*CardLocators.DELETE_BUTTON)
        self.place_order_button = self.browser.find_element(*CardLocators.PLACE_ORDER_BUTTON)

    def click_on_place_order(self):
        wait_for_element_be_located(self.browser, 4, "XPATH", "//button[@class='btn btn-success']")
        self.place_order_button.click()
        time.sleep(2)

    def click_on_delete_button(self):
        wait_for_element_be_located(self.browser, 4, "XPATH", "//a[.='Delete']")
        self.delete_button.click()
        time.sleep(2)


class OrderPage:
    def __init__(self, browser, is_purchase_window_displayed=False):
        self.browser = browser

        if is_purchase_window_displayed:
            self.ok_button = self.browser.find_element(*OrderPageLocators.OK_BUTTON_AFTER_ORDER)

        else:
            self.name_input = self.browser.find_element(*OrderPageLocators.INPUT_NAME)
            self.country_input = self.browser.find_element(*OrderPageLocators.INPUT_COUNTRY)
            self.city_input = self.browser.find_element(*OrderPageLocators.INPUT_CITY)
            self.credit_card_input = self.browser.find_element(*OrderPageLocators.INPUT_CREDIT_CARD)
            self.month_input = self.browser.find_element(*OrderPageLocators.INPUT_MONTH)
            self.year_input = self.browser.find_element(*OrderPageLocators.INPUT_YEAR)
            self.close_button = self.browser.find_element(*OrderPageLocators.CLOSE_BUTTON)
            self.purchase_button = self.browser.find_element(*OrderPageLocators.PURCHASE_BUTTON)

    def enter_order_data(self, name, country, credit_card, month, year, city):
        self.name_input.send_keys(name)
        self.country_input.send_keys(country)
        self.credit_card_input.send_keys(credit_card)
        self.month_input.send_keys(month)
        self.year_input.send_keys(year)
        self.city_input.send_keys(city)

    def click_purchase(self):
        self.purchase_button.click()

    def navigate_to_ok_button(self):

        self.ok_button.click()
