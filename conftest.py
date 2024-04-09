import pytest
import URLS
from selenium import webdriver
from locators import StellarBurgersLocators

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(URLS.URL)

    yield driver # возвращает

    driver.quit()

@pytest.fixture(scope='function')
def page():
    page = StellarBurgersLocators()
    return page