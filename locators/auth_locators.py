from selenium.webdriver.common.by import By


class RegisterLocators:
    SIGNUP_HEADER_BTN = (By.XPATH, "//a[@href='/signup']") # Кнопка создать аккаунт в хэдере
    FIRST_NAME_FIELD = (By.XPATH, "//input[@name='first_name']") # Поле ввода 'Имя'
    LAST_NAME_FIELD = (By.XPATH, "//input[@name='last_name']")
    USER_NAME_FIELD = (By.XPATH, "//input[@name='username']") # Поле ввода 'Имя пользователя'
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']") # Поле ввода 'Email'
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']") # Поле ввода 'Пароль'
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    

class LoginLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']") # Поле ввода 'Email'
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']") # Поле ввода 'Пароль'
    LOGIN_BTN = (By.XPATH, "//button[contains(text(), 'Войти')]") # Кнопка 'Войти'
    LOGOUT_BTN = (By.XPATH, "//a[contains(text(), 'Выход')]") # Кнопка выход
    SIGNIN_HEADER = (By.XPATH, "//h1[contains(text(), 'Войти на сайт')]") # Заголовок 'Войти на сайт'



    