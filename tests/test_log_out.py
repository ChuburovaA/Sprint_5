import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from data import *
from conftest import *



class TestLogOutInAccountStellarBurgers:

    def test_check_button_exit_in_account(self, driver, class_loc):
        # зашли в свой профиль
        driver.get(Urls.login)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.HEADER_LOGIN))
        driver.find_element(*class_loc.AUTH_PAGE_LOGIN_FIELD).send_keys(LogIn.AUTH_EMAIL)
        driver.find_element(*class_loc.AUTH_PAGE_PASSWORD_FIELD).send_keys(LogIn.AUTH_PASSWORD)
        driver.find_element(*class_loc.AUTH_PAGE_LOGIN_BUTTON).click()
        # нажали на кнопку "Личный кабинет" на главной странице
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.MAIN_PAGE_ORDER_BUTTON))
        driver.find_element(*class_loc.MAIN_PAGE_PROFILE_LINK).click()
        # нажали на кнопку "Выход" в "Личном кабинете"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.PROFILE_PAGE_EXIT_BUTTON))
        driver.find_element(*class_loc.PROFILE_PAGE_EXIT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.AUTH_PAGE_LOGIN_FIELD))
        time.sleep(5)

        assert driver.find_element(*class_loc.HEADER_LOGIN).text == 'Вход'
