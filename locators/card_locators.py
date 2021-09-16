from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class CardLocators:
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[@class='btn btn-success']")
    DELETE_BUTTON = (By.XPATH, "//a[.='Delete']")