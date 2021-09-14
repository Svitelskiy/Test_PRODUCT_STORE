import pytest
import random
import string
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.demoblaze.com/index.html")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def random_data():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(5))


@pytest.fixture(scope="function")
def user():
    return {"login": random_data(),
            "password": random_data()}
