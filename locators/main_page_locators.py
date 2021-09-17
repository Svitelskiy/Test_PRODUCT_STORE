from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class DemoMainPageLocators:
    LOGIN = (By.ID, "login2")
    SIGN_UP_BUTTON = (By.ID, "signin2")
    LOGOUT_BUTTON = (By.ID, "logout2")
    WELCOME_BUTTON = (By.ID, "nameofuser")
    HOME_PAGE_BUTTON = (By.XPATH, "//a[.='Home (current)']")
    CONTACT_BUTTON = (By.XPATH, "//a[.='Contact']")
    ABOUT_US_BUTTON = (By.XPATH, "//a[.='About us']")
    CART_BUTTON = (By.CSS_SELECTOR, "#cartur")



@dataclass
class DemoCategoryLocators:
    PHONES_BUTTON = (By.XPATH, "//a[.='Phones']")
    LAPTOPS_BUTTON = (By.XPATH, "//a[.='Laptops']")
    MONITORS_BUTTON = (By.XPATH, "//a[.='Monitors']")
    NEXT_BUTTON = (By.ID, "next2")
    PREVIOUS_BUTTON = (By.ID, "prev2")


@dataclass
class PhoneDemoProductLocators:
    SAMSUNG_GALAXY_S6 = (By.XPATH, "//a[.='Samsung galaxy s6']")
    NOKIA_LUMIA_1520 = (By.XPATH, "//a[.='Nokia lumia 1520']")
    NEXUS_6 = (By.XPATH, "//a[.='Nexus 6']")


@dataclass
class LaptopDemoProductLocators:
    SONY_VAIO_I5 = (By.XPATH, "//a[.='Sony vaio i5']")
    SONY_VAIO_I7 = (By.XPATH, "//a[contains(.,'Sony vaio i7')]")
    MACBOOK_AIR = (By.XPATH, "//a[.='MacBook air']")


@dataclass
class MonitorsDemoProductLocators:
    APPLE_MONITOR_24 = (By.XPATH, "//a[.='Apple monitor 24']")
    ASUS_FULL_HD = (By.XPATH, "//a[.='ASUS Full HD']")


@dataclass
class EachProduct:
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[.='Add to cart']")
