from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import StellarBurgersServiceTestData
from conftest import driver
from conftest import page
import settings

class TestProfilePageStellarBurgers:

    def test_check_open_profile_from_main_page(self, driver, page):
        # проверяем переход по клику на "Личный кабинет" со стартовой страницы
        driver.get(settings.URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(page.MAIN_PAGE_LOGIN_BUTTON))
        driver.find_element(*page.MAIN_PAGE_LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(page.AUTH_PAGE_LOGIN_BUTTON))
        driver.find_element(*page.AUTH_PAGE_LOGIN_BUTTON)

        assert driver.find_element(*page.HEADER_LOGIN)
