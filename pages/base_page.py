import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    @allure.step('Ожидания появления элемента  в DOM ')
    def wait_for_element_presense_located(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    @allure.step('Ожидание видимости элемента')
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step('Ожидание кликабельности элемента')
    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        element = self.wait_for_element_clickable(locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script('arguments[0].click();', element)

    @allure.step('Ввести данные')
    def fill_input(self, locator, text):
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Открыть URL')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Вернуть текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Скролл к элементу')
    def js_scroll(self, locator):
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Получить текст элемента')
    def get_text(self, locator):
        return self.wait_for_element_visible(locator).text
    
    @allure.step('Обновить сайт')
    def refresh(self):
        self.driver.refresh()