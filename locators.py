from selenium.webdriver.common.by import By

class StellarBurgersLocators:
    # Форма регистрации
    USER_NAME_INPUT = (By.XPATH, "(.//input[@name='name'])[1]")  # имя
    USER_EMAIL_INPUT = (By.XPATH, "(.//input[@name='name'])[2]")  # логин
    USER_PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")  # пароль
    REG_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться"
    REG_PAGE_LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")  # кнопка "Войти"
    REG_PAGE_ERROR_MESSAGE = (By.CLASS_NAME, "input__error")

    # Кнопка "Войти в аккаунт"/"Оформить заказ" на Главной странице
    MAIN_PAGE_LOGIN_BUTTON = (
    By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной странице
    MAIN_PAGE_ORDER_BUTTON = (
    By.XPATH, ".//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ" на главной странице