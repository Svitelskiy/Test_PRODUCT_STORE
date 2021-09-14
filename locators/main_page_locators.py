from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class DemoMainPageLocators:
    LOGIN = (By.ID, "login2")
    SIGN_UP_BUTTON = (By.ID, "signin2")
