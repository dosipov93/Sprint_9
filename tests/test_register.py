import allure
import pytest
from utils.generator import generate_user_data
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from config.urls import Urls

class TestRegister:
    @allure.title('Регистрация нового пользователя и проверка перехода на страницу авторизации')
    def test_register_new_user(self, driver):
        user_data = generate_user_data()
        register_page = RegisterPage(driver)
        register_page.open_register_page()
        register_page.fill_first_name(user_data['first_name'])
        register_page.fill_last_name(user_data['last_name'])
        register_page.fill_username(user_data['user_name'])
        register_page.fill_email(user_data['email'])
        register_page.fill_password(user_data['password'])
        register_page.click_create_account_btn()
        login_page = LoginPage(driver)
        assert login_page.get_login_form().is_displayed(), (
            'Форма авторизации не отображается после регистрации'
        )


        