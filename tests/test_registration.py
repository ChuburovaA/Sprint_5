from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import StellarBurgersServiceTestData
from random_emails import generate_random_emails
from conftest import driver
from conftest import page
import settings


class TestStellarBurgersRegistration:
    def test_completed_registration(self, driver, page):
        driver.get(settings.URL + "/register")
        # оказалась на странице с регистрацией
        driver.find_element(*page.USER_NAME_INPUT).send_keys(StellarBurgersServiceTestData.NAME)
        email = generate_random_emails()
        driver.find_element(*page.USER_EMAIL_INPUT).send_keys(email)
        driver.find_element(*page.USER_PASSWORD_INPUT).send_keys("chuburova123")
        driver.find_element(*page.REG_BUTTON).click()
        # теперь после регистрации прохожу авторизацию на "Вход"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(page.AUTH_PAGE_LOGIN_BUTTON))
        driver.find_element(*page.AUTH_PAGE_LOGIN_FIELD).send_keys(email)
        driver.find_element(*page.AUTH_PAGE_PASSWORD_FIELD).send_keys("chuburova123")
        driver.find_element(*page.AUTH_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(page.MAIN_PAGE_ORDER_BUTTON))

        assert driver.find_element(*page.MAIN_PAGE_ORDER_BUTTON)
