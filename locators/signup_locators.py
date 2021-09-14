from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class SignUpWindowLocators:
    USERNAME_INPUT = (By.ID, "sign-username")
    SING_PASSWORD_INPUT = (By.ID, "sign-password")
    SIGNUP_ENTER = (By.XPATH, "//button[.='Sign up']")
    SIGNUP_CLOSE = (By.XPATH, "//div[@id='signInModal']//button[@class='btn btn-secondary']")