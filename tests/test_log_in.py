from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import StellarBurgersServiceTestData
from conftest import driver
from conftest import page
import settings


class TestLogInStellarBurgers:
    def test_check_button_login_in_main_page(self, driver, page):
        # Нажатие на кнопку "Войти в аккаунт" на главной странице
        driver.get(settings.URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(page.MAIN_PAGE_LOGIN_BUTTON))
        driver.find_element(*page.MAIN_PAGE_LOGIN_BUTTON).click()
        # теперь авторизируемся
        driver.find_element(*page.AUTH_PAGE_LOGIN_FIELD).send_keys(StellarBurgersServiceTestData.AUTH_EMAIL)
        driver.find_element(*page.AUTH_PAGE_PASSWORD_FIELD).send_keys(StellarBurgersServiceTestData.AUTH_PASSWORD)
        driver.find_element(*page.AUTH_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(page.MAIN_PAGE_ORDER_BUTTON))

        assert driver.find_element(*page.MAIN_PAGE_ORDER_BUTTON)

    def test_check_button_personal_account(self, driver, page):
        # нажать на кнопку "Личный кабинет" с главной страницы
        driver.get(settings.URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(page.MAIN_PAGE_PROFILE_LINK))
        driver.find_element(*page.MAIN_PAGE_PROFILE_LINK).click()

        assert driver.find_element(*page.AUTH_PAGE_LOGIN_BUTTON)