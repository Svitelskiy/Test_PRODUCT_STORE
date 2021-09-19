from pages.main_page import DemoMainPage
from pages.login_page import LoginPage
from pages.sign_page import SignUpPage
from utils import wait_for_element_be_located, wait_for_alert_and_accept


def test_login_into_account(browser, user):
    main_page = DemoMainPage(browser)
    main_page.navigate_to_signup_page()

    SignUpPage(browser).enter_valid_credentials(login=user["login"], password=user["password"])
    wait_for_alert_and_accept(browser, 5)

    main_page.navigate_to_login_page()
    LoginPage(browser).enter_valid_credentials(login=user["login"], password=user["password"])
    wait_for_element_be_located(browser, 10, "ID", "nameofuser")
    assert DemoMainPage(browser, registered=True).welcome_label.text == f"Welcome {user['login']}"
