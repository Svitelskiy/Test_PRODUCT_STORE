import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage
from pages.main_page import DemoMainPage, ContactFromPage, AboutUsPage
from utils import wait_for_alert_and_accept
from pages.login_page import LoginPage


def test_contact(browser, contact_message_data):
    main_page = DemoMainPage(browser)
    main_page.navigate_to_contact()
    ContactFromPage(browser).send_message(contact_email=contact_message_data["contact_email"],
                                          contact_name=contact_message_data["contact_name"],
                                          message=contact_message_data["message"])
    wait_for_alert_and_accept(browser, 5)


def test_about_us(browser):
    main_page = DemoMainPage(browser)
    main_page.navigate_to_about_us()

    AboutUsPage(browser).press_play_button()

    AboutUsPage(browser).press_close_button()


def test_cart_button(browser):
    main_page = DemoMainPage(browser)
    main_page.navigate_to_cart()


def test_cart_button_after_login(browser, test_creds):
    main_page = DemoMainPage(browser)
    main_page.navigate_to_login_page()
    LoginPage(browser).enter_valid_credentials(login=test_creds["login"], password=test_creds["password"])
    time.sleep(2)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "cartur")))
    DemoMainPage(browser).navigate_to_cart()


def test_nest_previous_category_button(browser):
    main_page = DemoMainPage(browser)
    main_page.push_next_category_page()
    time.sleep(2)
    main_page.push_previous_category_page()


def test_logout_button(browser, test_creds):
    main_page = DemoMainPage(browser)
    main_page.navigate_to_login_page()
    LoginPage(browser).enter_valid_credentials(login=test_creds["login"], password=test_creds["password"])
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "logout2")))
    DemoMainPage(browser, registered=True).press_logout_button()
