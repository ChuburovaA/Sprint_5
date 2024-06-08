import pytest
from selenium import webdriver

from data import Urls
from locators import StellarBurgersLocators

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.BASE_URL)

    yield driver # возвращает

    driver.quit()

@pytest.fixture(scope='function')
def class_loc():
    class_loc = StellarBurgersLocators()

    return class_loc


