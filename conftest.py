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


@pytest.fixture(scope="function")
def contact_message_data():
    return {
        "contact_email": "kumis@gmail.com",
        "contact_name": "Petro1234",
        "message": "test to fill message"
    }


@pytest.fixture(scope="function")
def test_creds():
    return {"login": "Sobaka",
            "password": "Qwe123qwer"}


@pytest.fixture(scope="function")
def order_info():
    return {
        "name": "Kosta Lacosta",
        "country": "Ukraine",
        "city": "Lypivka",
        "credit_card": "1233 4112 5123 5214",
        "month": "02",
        "year": "2023"
    }
