from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class ContactPageLocators:
    CONTACT_EMAIL = (By.ID, "recipient-email")
    CONTACT_NAME = (By.ID, "recipient-name")
    INPUT_MASSAGE = (By.ID, "message-text")
    SEND_MESSAGE_BUTTON = (By.XPATH, "//button[.='Send message']")
    CLOSE_BUTTON = (By.XPATH, "//div[@id='exampleModal']//button[@class='btn btn-secondary']")