from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import *
from conftest import *


class TestConstructorStellarBurgers:

    def test_open_bread_section(self, driver, class_loc):
        # проверяем в конструкторе, что переход работает в раздел "Булки"
        driver.get(Urls.BASE_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.MAIN_PAGE_LOGIN_BUTTON))
        # выбрала сначал другую категорию "Начинки", а затем проверила уже "Булки"
        driver.find_element(*class_loc.MAIN_PAGE_FILLINGS_TAB).click()
        assert driver.find_element(*class_loc.MAIN_PAGE_TAB_CONSTRUCTOR).text == "Начинки"

        driver.find_element(*class_loc.MAIN_PAGE_BREAD_TAB).click()
        assert driver.find_element(*class_loc.MAIN_PAGE_TAB_CONSTRUCTOR).text == "Булки"

    def test_open_sause_section(self, driver, class_loc):
        # проверяем в конструкторе, что переход работает в раздел "Соусы"
        driver.get(Urls.BASE_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.MAIN_PAGE_LOGIN_BUTTON))
        driver.find_element(*class_loc.MAIN_PAGE_SOUCES_TAB).click()

        assert driver.find_element(*class_loc.MAIN_PAGE_TAB_CONSTRUCTOR).text == "Соусы"

    def test_open_filling_section(self, driver, class_loc):
        # проверяем в конструкторе, что переход работает в раздел "Начинки"
        driver.get(Urls.BASE_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(class_loc.MAIN_PAGE_LOGIN_BUTTON))
        driver.find_element(*class_loc.MAIN_PAGE_FILLINGS_TAB).click()

        assert driver.find_element(*class_loc.MAIN_PAGE_TAB_CONSTRUCTOR).text == "Начинки"