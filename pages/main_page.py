import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.about_us_page_locators import AboutUsPageLocators
from locators.cart_order_locators import OrderPageLocators
from locators.contact_page_locators import ContactPageLocators
from locators.main_page_locators import DemoMainPageLocators, DemoCategoryLocators, PhoneDemoProductLocators, \
    MonitorsDemoProductLocators, LaptopDemoProductLocators, EachProduct
from utils import wait_for_element_be_located


class HeaderPage:
    def __init__(self, browser,  registered=False):
        self.browser = browser

        self.login = self.browser.find_element(*DemoMainPageLocators.LOGIN)
        self.sign_up_button = self.browser.find_element(*DemoMainPageLocators.SIGN_UP_BUTTON)
        self.home_button = self.browser.find_element(*DemoMainPageLocators.HOME_PAGE_BUTTON)
        self.contact_button = self.browser.find_element(*DemoMainPageLocators.CONTACT_BUTTON)
        self.cart_button = self.browser.find_element(*DemoMainPageLocators.CART_BUTTON)
        self.about_us_button = self.browser.find_element(*DemoMainPageLocators.ABOUT_US_BUTTON)

        if registered:
            self.welcome_label = self.browser.find_element(*DemoMainPageLocators.WELCOME_BUTTON)
            self.logout_button = self.browser.find_element(*DemoMainPageLocators.LOGOUT_BUTTON)

        else:

            self.login = self.browser.find_element(*DemoMainPageLocators.LOGIN)

    def navigate_to_homepage(self):
        self.home_button.click()

    def navigate_to_cart(self):
        # wait_for_element_be_located(self.browser, 4, "ID", "cartur")
        self.cart_button.click()

    def navigate_to_login_page(self):
        wait_for_element_be_located(self.browser, 4, "ID", "login2")
        self.login.click()
        time.sleep(5)

    def navigate_to_signup_page(self):
        wait_for_element_be_located(self.browser, 4, "ID", "signin2")
        self.sign_up_button.click()
        time.sleep(2)

    def navigate_to_contact(self):
        wait_for_element_be_located(self.browser, 4, "XPATH", "//a[.='Contact']")
        self.contact_button.click()
        time.sleep(2)

    def navigate_to_about_us(self):
        wait_for_element_be_located(self.browser, 4, "XPATH", "//a[.='About us']")
        self.about_us_button.click()
        time.sleep(2)

    def press_logout_button(self):
        wait_for_element_be_located(self.browser, 4, "ID", "logout2")
        self.logout_button.click()
        time.sleep(2)


class DemoMainPage(HeaderPage):
    def __init__(self, browser, registered=False):
        super().__init__(browser, registered)

        self.category_phone_button = self.browser.find_element(*DemoCategoryLocators.PHONES_BUTTON)
        self.category_monitors_button = self.browser.find_element(*DemoCategoryLocators.MONITORS_BUTTON)
        self.category_laptop_button = self.browser.find_element(*DemoCategoryLocators.LAPTOPS_BUTTON)

        self.category_next_page_button = self.browser.find_element(*DemoCategoryLocators.NEXT_BUTTON)
        self.category_previous_page_button = self.browser.find_element(*DemoCategoryLocators.PREVIOUS_BUTTON)
        self.home_page_label = self.browser.find_element(*DemoMainPageLocators.HOME_PAGE_BUTTON)

    def navigate_to_phone_category(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[.='Phones']")))
        self.category_phone_button.click()

    def navigate_to_monitors_category(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[.='Monitors']")))
        self.category_monitors_button.click()

    def navigate_to_laptops_category(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[.='Laptops']")))
        self.category_laptop_button.click()

    def push_next_category_page(self):
        wait_for_element_be_located(self.browser, 4, "ID", "next2")
        self.category_next_page_button.click()
        time.sleep(2)

    def push_previous_category_page(self):
        wait_for_element_be_located(self.browser, 4, "ID", "prev2")
        self.category_previous_page_button.click()
        time.sleep(2)


class ContactFromPage(HeaderPage):
    def __init__(self, browser, registered=False):
        super().__init__(browser, registered)

        self.contact_email = self.browser.find_element(*ContactPageLocators.CONTACT_EMAIL)
        self.contact_name = self.browser.find_element(*ContactPageLocators.CONTACT_NAME)
        self.message = self.browser.find_element(*ContactPageLocators.INPUT_MASSAGE)
        self.close_button = self.browser.find_element(*ContactPageLocators.CLOSE_BUTTON)
        self.send_message_button = self.browser.find_element(*ContactPageLocators.SEND_MESSAGE_BUTTON)

    def send_message(self, contact_email, message, contact_name):
        self.contact_name.send_keys(contact_name)
        self.contact_email.send_keys(contact_email)
        self.message.send_keys(message)
        self.send_message_button.click()


class AboutUsPage(HeaderPage):
    def __init__(self, browser, registered=False):
        super().__init__(browser, registered)
        self.play_button = self.browser.find_element(*AboutUsPageLocators.PLAY_BUTTON)
        self.close_button = self.browser.find_element(*AboutUsPageLocators.CLOSE_BUTTON)

# переименуй с пуш на пресс
    def press_play_button(self):
        wait_for_element_be_located(self.browser, 4, "XPATH", "//div[@id='videoModal']//"
                                                              "button[@class='btn btn-secondary']")
        self.play_button.click()
        time.sleep(5)

    def press_close_button(self):
        wait_for_element_be_located(self.browser, 4, "XPATH", "//div[@id='videoModal']"
                                                              "//button[@class='btn btn-secondary']")
        self.close_button.click()


class PhonesCategory(HeaderPage):
    def __init__(self, browser, registered=False):
        super().__init__(browser, registered)

        self.phones_SAMSUNG_GALAXY_S6 = self.browser.find_element(*PhoneDemoProductLocators.SAMSUNG_GALAXY_S6)
        self.phones_NOKIA_LUMIA_1520 = self.browser.find_element(*PhoneDemoProductLocators.NOKIA_LUMIA_1520)
        self.phones_NEXUS_6 = self.browser.find_element(*PhoneDemoProductLocators.NEXUS_6)

    def navigate_to_samsung_galaxy_product(self):
        self.phones_SAMSUNG_GALAXY_S6.click()


class MonitorsCategory(HeaderPage):
    def __init__(self, browser, registered=False):
        super().__init__(browser, registered)

        self.monitor_APPLE_MONITOR_24 = self.browser.find_element(*MonitorsDemoProductLocators.APPLE_MONITOR_24)
        self.monitor_ASUS_FULL_HD = self.browser.find_element(*MonitorsDemoProductLocators.ASUS_FULL_HD)


class LaptopCategory(HeaderPage):
    def __init__(self, browser, registered=False):
        super().__init__(browser, registered)

        self.laptop_SONY_VAIO_I5 = self.browser.find_element(*LaptopDemoProductLocators.SONY_VAIO_I5)
        self.laptop_SONY_VAIO_I7 = self.browser.find_element(*LaptopDemoProductLocators.SONY_VAIO_I7)
        self.laptop_MACBOOK_AIR = self.browser.find_element(*LaptopDemoProductLocators.MACBOOK_AIR)


class EachProductClass(HeaderPage):

    def __init__(self, browser, registered=False):
        super().__init__(browser, registered)

        self.add_to_cart = self.browser.find_element(*EachProduct.ADD_TO_CART_BUTTON)

    def add_product_to_cart(self):
        self.add_to_cart.click()
