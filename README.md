# Sprint_5
Тестирование сервиса Stellar Burgers

Структура проекта:
1) Все тесты находятся в папке - tests
2) Фикстуры распологаются в файле - conftest.py
3) Констаты распологаются в файле - data.py
4) Локаторы распологаются в файле - locators.py
5) Генератор email распологается в файле - random_emails
6) URL распологается в файле - settings.py
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
platform win32 -- Python 3.12.2, pytest-8.1.1, pluggy-1.4.0 -- C:\Users\Admin\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Admin\Sprint_5
collected 13 items

tests/test_chapter_constructor.py::TestConstructorStellarBurgers::test_open_bread_section
DevTools listening on ws://127.0.0.1:59524/devtools/browser/cc65ed8d-0605-4133-822e-e26936c687ca
PASSED                                                 [  7%]
tests/test_chapter_constructor.py::TestConstructorStellarBurgers::test_open_sause_section 
DevTools listening on ws://127.0.0.1:59547/devtools/browser/8925c2f1-9462-4bf4-a30a-33cdc27977b4
PASSED                                                 [ 15%]
tests/test_chapter_constructor.py::TestConstructorStellarBurgers::test_open_filling_section 
DevTools listening on ws://127.0.0.1:59572/devtools/browser/9f13579d-ee24-42a5-9811-410278734e03
PASSED                                               [ 23%]
tests/test_log_in.py::TestLogInStellarBurgers::test_check_button_login_in_main_page 
DevTools listening on ws://127.0.0.1:59595/devtools/browser/96137dc7-bead-441e-a9cf-7ca581d477f5
PASSED                                                       [ 30%]
tests/test_log_in.py::TestLogInStellarBurgers::test_check_button_personal_account 
DevTools listening on ws://127.0.0.1:59619/devtools/browser/0b849607-dccf-4178-8ef4-1b90f54ddf53
PASSED                                                         [ 38%]
tests/test_log_in.py::TestLogInStellarBurgers::test_check_button_login_in_form_registration 
DevTools listening on ws://127.0.0.1:59642/devtools/browser/e23b90b1-53a2-424b-bde7-cf06519226a9
PASSED                                               [ 46%]
tests/test_log_in.py::TestLogInStellarBurgers::test_check_button_in_foggot_password 
DevTools listening on ws://127.0.0.1:59671/devtools/browser/c3b94283-b83b-40d4-b66a-d0697a854b30
PASSED                                                       [ 53%]
tests/test_log_out.py::TestLogOutInAccountStellarBurgers::test_check_button_exit_in_account 
DevTools listening on ws://127.0.0.1:59694/devtools/browser/839416fc-735b-4a64-97ad-6a51fbf246e0
PASSED                                               [ 61%]
tests/test_profile_page.py::TestProfilePageStellarBurgers::test_check_open_profile_from_main_page 
DevTools listening on ws://127.0.0.1:59727/devtools/browser/cdffc599-c2c8-4d00-a757-257469d74e27
PASSED                                         [ 69%]
tests/test_profile_page.py::TestProfilePageStellarBurgers::test_check_transfer_from_account_page_to_constructor 
DevTools listening on ws://127.0.0.1:59751/devtools/browser/27b5eca5-3bfd-4ff5-83eb-3002e37c9145
PASSED                           [ 76%]
tests/test_profile_page.py::TestProfilePageStellarBurgers::test_check_transfer_from_account_page_to_logo_stellarburgers 
DevTools listening on ws://127.0.0.1:59776/devtools/browser/ee8fb215-3721-462c-95ce-ce792892742a
ncorrect_password
DevTools listening on ws://127.0.0.1:59823/devtools/browser/dbc5f7f3-0ba5-40df-a055-12cfa99752fd
PASSED                                                 [100%]

=========================================================== 13 passed in 304.32s (0:05:04) ============================================================ 