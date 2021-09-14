from locators.signup_locators import SignUpWindowLocators
from selenium.webdriver.common.keys import Keys


class SignUpPage:
    def __init__(self, browser):
        self.browser = browser

        self.username_input = self.browser.find_element(*SignUpWindowLocators.USERNAME_INPUT)
        self.sign_password_input = self.browser.find_element(*SignUpWindowLocators.SING_PASSWORD_INPUT)
        self.sign_enter = self.browser.find_element(*SignUpWindowLocators.SIGNUP_ENTER)
        self.sign_close = self.browser.find_element(*SignUpWindowLocators.SIGNUP_CLOSE)

    def enter_valid_credentials(self, login, password):
        self.username_input.send_keys(login)
        self.sign_password_input.send_keys(password)
        self.sign_enter.click()

