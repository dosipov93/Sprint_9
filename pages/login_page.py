import allure
from pages.base_page import BasePage
from locators.auth_locators import LoginLocators
from config.urls import Urls


class LoginPage(BasePage):

    @allure.step('Открыть страницу авторизации')
    def open_login_page(self):
        self.open_url(Urls.LOGIN_URL)

    @allure.step('Заполнить поле "Email"')
    def fill_user_name(self, user_name):
        self.fill_input(LoginLocators.EMAIL_FIELD, user_name)

    @allure.step('Заполнить поле "Пароль"')
    def fill_password(self, password):
        self.fill_input(LoginLocators.PASSWORD_FIELD, password)

    @allure.step('Нажать кнопку "Войти"')
    def click_login_btn(self):
        self.click_to_element(LoginLocators.LOGIN_BTN)

    @allure.step('Проверить, что форма авторизации отображается')
    def get_login_form(self):
        return self.wait_for_element_visible(LoginLocators.SIGNIN_HEADER)
    
    @allure.step('Получить кнопку "Выход"')
    def get_logout_btn(self):
        return self.wait_for_element_visible(LoginLocators.LOGOUT_BTN)
        
    @allure.step('Логин')
    def login(self, user_name, password):
        self.open_login_page()
        self.fill_user_name(user_name)
        self.fill_password(password)
        self.click_login_btn()
        self.get_logout_btn()
    

    