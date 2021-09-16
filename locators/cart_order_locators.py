from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class OrderPageLocators:
    TOTAL_AMOUNT = (By.ID, "totalm")
    INPUT_NAME = (By.ID, "name")
    INPUT_COUNTRY = (By.ID, "country")
    INPUT_CITY = (By.ID, "city")
    INPUT_CREDIT_CARD = (By.ID, "card")
    INPUT_MONTH = (By.ID, "month")
    INPUT_YEAR = (By.ID, "year")
    PURCHASE_BUTTON = (By.XPATH, "//button[.='Purchase']")
    CLOSE_BUTTON = (By.ID, "orderModal")
    OK_BUTTON_AFTER_ORDER = (By.XPATH, "//button[@class='confirm btn btn-lg btn-primary']")
