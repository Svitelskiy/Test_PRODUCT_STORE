from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class LoginWindowLocators:
    LOGIN_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    ENTER_BUTTON = (By.XPATH, "//button[.='Log in']")
    CLOSE_BUTTON = (By.XPATH, "//div[@id='logInModal']//button[@class='btn btn-secondary']")