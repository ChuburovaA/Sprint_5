import pytest
import settings
from selenium import webdriver
from locators import StellarBurgersLocators

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(settings.URL)

    yield driver # возвращает

    driver.quit()