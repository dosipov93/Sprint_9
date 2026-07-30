import allure
import pytest
from pages.login_page import LoginPage
from config.urls import Urls


class TestLogin:
    @allure.title('Авторизация зарегистрированного пользователя и проверка отображения кнопки "Выход"')
    def test_login_user(self, driver, registered_user):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.fill_user_name(registered_user['user_name'])
        login_page.fill_password(registered_user['password'])
        login_page.click_login_btn()
        assert login_page.get_logout_btn().is_displayed(), (
            'Кнопка "Выход" не отображается после авторизации'
        )
        

