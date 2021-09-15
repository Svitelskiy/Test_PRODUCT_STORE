from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


def wait_for_alert_and_accept(browser, time_to_wait):
    WebDriverWait(browser, time_to_wait).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert.accept()


def wait_for_element_be_located(browser, time_to_wait, by_element, element_id):
    if by_element == "CLASS_NAME":
        return WebDriverWait(browser, time_to_wait).until(EC.visibility_of_element_located((By.CLASS_NAME, element_id)))
    elif by_element == "XPATH":
        return WebDriverWait(browser, time_to_wait).until(EC.visibility_of_element_located((By.XPATH, element_id)))
    elif by_element == "ID":
        return WebDriverWait(browser, time_to_wait).until(EC.visibility_of_element_located((By.ID, element_id)))
    elif by_element == "CSS_SELECTOR":
        return WebDriverWait(browser, time_to_wait).until(EC.visibility_of_element_located((By.CSS_SELECTOR, element_id)))


