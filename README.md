# Sprint_5
Тестирование сервиса Stellar Burgers

Структура проекта:
1) Все тесты находятся в папке - tests
2) Фикстуры распологаются в файле - conftest.py
3) Констаты распологаются в файле - data.py
4) Локаторы распологаются в файле - locators.py
5) Генератор email распологается в файле - random_emails
6) URL распологается в файле - URLS.py
7) Описание теста распологается в файле - README.md

Краткое описание тестов:
1) Проверка регистрации на сайте, файл - test_registration.py
Проверялся ввод: Имени, логина и пароля. Логин(email) вводился с помощью генирации.
Так же было проеврено на ошибку при введении неверного пароля.

2) Проверка входа на сайте, файл - test_log_in.py
Проверяли: вход по кнопке «Войти в аккаунт» на главной, вход через кнопку «Личный кабинет», вход через кнопку в форме регистрации, вход через кнопку в форме восстановления пароля.

3) Проверка профиля, файл - test_profile_page.py
Проверяли:переход по клику на «Личный кабинет», переход по клику на «Конструктор», переход на логотип Stellar Burgers.

4) Проверка выхода из аккаунта, файл - test_log_out.py
Проверяли выход по кнопке «Выйти» в личном кабинете.

5) Проверяли раздел "Конструктор", файл - test_chapter_constructor.py
Проверяли переходы по разделам: «Булки», «Соусы», «Начинки».


Результаты теста:
================================================================= test session starts =================================================================
platform win32 -- Python 3.12.2, pytest-8.1.1, pluggy-1.4.0 -- C:\Users\Admin\PycharmProjects\Sprin_5-main\.venv\Scripts\python.exe
cachedir: .pytest_cache                                                                                                            
rootdir: C:\Users\Admin\PycharmProjects\Sprin_5-main
collected 13 items

tests/test_chapter_constructor.py::TestConstructorStellarBurgers::test_open_bread_section
DevTools listening on ws://127.0.0.1:63289/devtools/browser/e00793fb-ca19-4faf-914c-6abaaa7959dc
PASSED                                                 [  7%]
tests/test_chapter_constructor.py::TestConstructorStellarBurgers::test_open_sause_section 
DevTools listening on ws://127.0.0.1:63312/devtools/browser/cbdb6861-a3ec-4f18-ab7e-84ba2c2b2c82
PASSED                                                 [ 15%]
tests/test_chapter_constructor.py::TestConstructorStellarBurgers::test_open_filling_section 
DevTools listening on ws://127.0.0.1:63336/devtools/browser/79f098f7-7f4c-4a64-8881-c8b62bb69560
PASSED                                               [ 23%]
tests/test_log_in.py::TestLogInStellarBurgers::test_check_button_login_in_main_page 
DevTools listening on ws://127.0.0.1:63361/devtools/browser/516e1203-1fb2-4154-af31-6877396d8afe
PASSED                                                       [ 30%]
tests/test_log_in.py::TestLogInStellarBurgers::test_check_button_personal_account 
DevTools listening on ws://127.0.0.1:63385/devtools/browser/8e8b4288-933b-4ceb-b9f3-7d9ed245fded
PASSED                                                         [ 38%]
tests/test_log_in.py::TestLogInStellarBurgers::test_check_button_login_in_form_registration 
DevTools listening on ws://127.0.0.1:63408/devtools/browser/812d6375-b48e-4d4d-a61e-c48535a5e76d
PASSED                                               [ 46%]
tests/test_log_in.py::TestLogInStellarBurgers::test_check_button_in_foggot_password 
DevTools listening on ws://127.0.0.1:63431/devtools/browser/83c97b95-3838-4dd4-a0b1-e86fa8919afe
PASSED                                                       [ 53%]
tests/test_log_out.py::TestLogOutInAccountStellarBurgers::test_check_button_exit_in_account 
DevTools listening on ws://127.0.0.1:63455/devtools/browser/960f0ebf-9121-480d-8b49-557b73600749
PASSED                                               [ 61%]
tests/test_profile_page.py::TestProfilePageStellarBurgers::test_check_open_profile_from_main_page 
DevTools listening on ws://127.0.0.1:63493/devtools/browser/7ab4b7f9-f3d9-4e37-9bb6-5309a27b7e10
PASSED                                         [ 69%]
tests/test_profile_page.py::TestProfilePageStellarBurgers::test_check_transfer_from_account_page_to_constructor 
DevTools listening on ws://127.0.0.1:63516/devtools/browser/585bbb00-03fe-4da7-bdf0-ffef10cb916d
PASSED                           [ 76%]
tests/test_profile_page.py::TestProfilePageStellarBurgers::test_check_transfer_from_account_page_to_logo_stellarburgers 
DevTools listening on ws://127.0.0.1:63544/devtools/browser/a4418106-0967-4bf5-9e07-f9687a86c656
PASSED                   [ 84%]
tests/test_registration.py::TestStellarBurgersRegistration::test_completed_registration 
DevTools listening on ws://127.0.0.1:63568/devtools/browser/cb5c4d56-841d-4738-a129-2b85f595590a
PASSED                                                   [ 92%]
tests/test_registration.py::TestStellarBurgersRegistration::test_check_incorrect_password 
DevTools listening on ws://127.0.0.1:63595/devtools/browser/25cd3348-1077-41d1-995c-61baad07ff88
PASSED                                                 [100%]

=========================================================== 13 passed in 200.50s (0:03:20) ============================================================ 