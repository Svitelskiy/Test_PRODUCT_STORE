import time

from locators.main_page_locators import DemoMainPageLocators
from utils import wait_for_element_be_located


class DemoMainPage:
    def __init__(self, browser, registered=False):
        self.browser = browser

        self.login = self.browser.find_element(*DemoMainPageLocators.LOGIN)
        self.sign_up_button = self.browser.find_element(*DemoMainPageLocators.SIGN_UP_BUTTON)

        if registered:
            self.login = self.browser.find_element(*DemoMainPageLocators.LOGIN)
        else:
            self.login = self.browser.find_element(*DemoMainPageLocators.LOGIN)

    def navigate_to_login_page(self):
        wait_for_element_be_located(self.browser, 4, "ID", "login2")
        self.login.click()
        time.sleep(5)

    def navigate_to_signup_page(self):
        wait_for_element_be_located(self.browser, 4, "ID", "signin2")
        self.sign_up_button.click()
        time.sleep(5)




