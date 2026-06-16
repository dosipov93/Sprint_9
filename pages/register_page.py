import allure
from pages.base_page import BasePage
from locators.auth_locators import RegisterLocators
from config.urls import Urls


class RegisterPage(BasePage):

    @allure.step('Открыть страницу регистрации')
    def open_register_page(self):
        self.open_url(Urls.REGISTER_URL)

    @allure.step('Заполнить поле "Имя"')
    def fill_first_name(self, first_name):
        self.fill_input(RegisterLocators.FIRST_NAME_FIELD, first_name)
    
    @allure.step('Заполнить поле "Фамилия"')
    def fill_last_name(self, last_name):
        self.fill_input(RegisterLocators.LAST_NAME_FIELD, last_name)

    @allure.step('Заполнить поле "Имя пользователя"')
    def fill_username(self, user_name):
        self.fill_input(RegisterLocators.USER_NAME_FIELD, user_name)

    @allure.step('Заполнить поле "Email"')
    def fill_email(self, email):
        self.fill_input(RegisterLocators.EMAIL_FIELD, email)

    @allure.step('Заполнить поле "Пароль"')
    def fill_password(self, password):
        self.fill_input(RegisterLocators.PASSWORD_FIELD, password)
    
    @allure.step('Нажать кнопку "Создать аккаунт"')
    def click_create_account_btn(self):
        self.click_to_element(RegisterLocators.CREATE_ACCOUNT_BTN)

    @allure.step('Регистрация')
    def register(self, first_name, last_name, user_name, email, password):
        self.open_register_page()
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_username(user_name)
        self.fill_email(email)
        self.fill_password(password)
        self.click_create_account_btn()
        


        
