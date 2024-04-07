from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import StellarBurgersServiceTestData
from conftest import driver
from conftest import page
import settings

class TestConstructorStellarBurgers:

    def test_open_bread_section(self, driver, page):
        # проверяем в конструкторе, что переход работает в раздел "Булки"
        driver.get(settings.URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(page.MAIN_PAGE_LOGIN_BUTTON))
        # выбрала сначал другую категорию "Начинки", а затем проверила уже "Булки"
        driver.find_element(*page.MAIN_PAGE_FILLINGS_TAB).click()
        assert driver.find_element(*page.MAIN_PAGE_TAB_CONSTRUCTOR).text == "Начинки"
        driver.find_element(*page.MAIN_PAGE_BREAD_TAB).click()
        assert driver.find_element(*page.MAIN_PAGE_TAB_CONSTRUCTOR).text == "Булки"