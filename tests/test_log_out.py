from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import StellarBurgersServiceTestData
from conftest import driver
from conftest import page
import URLS



class TestLogOutInAccountStellarBurgers:

    def test_check_button_exit_in_account(self, driver, page):
        # зашли в свой профиль
        driver.get(settings.URL + "/login")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(page.HEADER_LOGIN))
        driver.find_element(*page.AUTH_PAGE_LOGIN_FIELD).send_keys(StellarBurgersServiceTestData.AUTH_EMAIL)
        driver.find_element(*page.AUTH_PAGE_PASSWORD_FIELD).send_keys(StellarBurgersServiceTestData.AUTH_PASSWORD)
        driver.find_element(*page.AUTH_PAGE_LOGIN_BUTTON).click()
        # нажали на кнопку "Личный кабинет" на главной странице
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(page.MAIN_PAGE_ORDER_BUTTON))
        driver.find_element(*page.MAIN_PAGE_PROFILE_LINK).click()
        # нажали на кнопку "Выход" в "Личном кабинете"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(page.PROFILE_PAGE_EXIT_BUTTON))
        driver.find_element(*page.PROFILE_PAGE_EXIT_BUTTON).click()

        driver.quit()