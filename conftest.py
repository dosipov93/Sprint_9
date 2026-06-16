import pytest
from selenium import webdriver
from utils.generator import generate_user, generate_recipe_data
from pages.register_page import RegisterPage
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def recipe_data():
    return generate_recipe_data()

@pytest.fixture
def user_data():
    return generate_user()

@pytest.fixture
def registered_user(driver, user_data):
    register_page = RegisterPage(driver)
    register_page.register(
        user_data['first_name'],
        user_data['last_name'],
        user_data['user_name'],
        user_data['email'],
        user_data['password']
    )
    return user_data

@pytest.fixture
def login_user(driver, registered_user):
    login_page = LoginPage(driver)
    login_page.login(
        registered_user['user_name'],
        registered_user['password']
    )

