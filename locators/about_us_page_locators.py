from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class AboutUsPageLocators:
    PLAY_BUTTON = (By.XPATH, "//div[@class='vjs-poster']")
    CLOSE_BUTTON = (By.XPATH, "//div[@id='videoModal']//button[@class='btn btn-secondary']")
