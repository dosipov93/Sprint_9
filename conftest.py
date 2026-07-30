import os
import pytest
from selenium import webdriver
from selenium.webdriver.remote.file_detector import LocalFileDetector
from utils.generator import generate_user_data
from pages.register_page import RegisterPage
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    selenoid_uri = os.environ.get("SELENOID_URI", "http://127.0.0.1:4444/wd/hub")
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=selenoid_uri,
        options=options
    )
    driver.file_detector = LocalFileDetector()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def registered_user(driver):
    user_data = generate_user_data()
    register_page = RegisterPage(driver)
    register_page.register(
        user_data['first_name'],
        user_data['last_name'],
        user_data['user_name'],
        user_data['email'],
        user_data['password']
    )
    page = LoginPage(driver)
    page.get_login_form()
    return user_data

@pytest.fixture
def login_user(driver, registered_user):
    login_page = LoginPage(driver)
    login_page.login(
        registered_user['user_name'],
        registered_user['password']
    )

