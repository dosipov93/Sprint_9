import allure
from pages.base_page import BasePage
from locators.recipe_locators import RecipeLocators
from config.urls import Urls
from utils.file_utils import get_asset_path


class RecipePage(BasePage):

    @allure.step('Открыть страницу создания рецепта')
    def open_recipe_page(self):
        self.open_url(Urls.CREATE_RECIPE_URL)

    @allure.step('Заполнить название рецепта')
    def fill_title(self, title):
        self.fill_input(RecipeLocators.TITLE_FIELD, title)

    @allure.step('Снять отметку с тега "Завтрак"')
    def deselect_breakfast_tag(self):
        self.click_to_element(RecipeLocators.BREAKFAST_TAG)

    @allure.step('Снять отметку с тега "Ужин"')
    def deselect_dinner_tag(self):
        self.click_to_element(RecipeLocators.DINNER_TAG)

    @allure.step('Ввести название ингредиента')
    def enter_ingredient_name(self, ingredient_name):
        self.fill_input(RecipeLocators.INGREDIENTS_INPUT, ingredient_name)

    @allure.step('Выбрать ингредиент из выпадающего списка')
    def select_ingredient_from_dropdown(self):
        self.wait_for_element_visible(RecipeLocators.INGREDIENT_SELECT_DROPDOWN)
        self.click_to_element(RecipeLocators.INGREDIENT_SELECT_DROPDOWN)

    @allure.step('Ввести количество ингредиента')
    def enter_ingredient_quantity(self, quantity):
        self.fill_input(RecipeLocators.INGREDIENTS_QUANTITY, quantity)
    
    @allure.step('Нажать кнопку "Добавить ингредиент"')
    def click_add_ingredient_btn(self):
        self.click_to_element(RecipeLocators.ACCEPT_INGREDIENT)
        self.wait_for_element_visible(RecipeLocators.DELETE_INGREDIENT_BTN)

    @allure.step('Заполнить время приготовления')
    def fill_cooking_time(self, cooking_time):
        self.fill_input(RecipeLocators.COOKING_TIME_FIELD, cooking_time)

    @allure.step('Заполнить описание рецепта')
    def fill_description(self, description):
        self.fill_input(RecipeLocators.DESCRIPTION_FIELD, description)

    @allure.step('Нажать кнопку "Создать рецепт"')
    def click_create_recipe_btn(self):
        self.js_scroll(RecipeLocators.SUBMIT_BTN)
        self.click_to_element(RecipeLocators.SUBMIT_BTN)

    @allure.step('Загрузить фото рецепта')
    def upload_photo(self, file_name):
        file_path = str(get_asset_path(file_name))
        file_input = self.wait_for_element_presense_located(RecipeLocators.PHOTO_INPUT)
        file_input.send_keys(file_path)
    
    @allure.step('Получить кнопку "Добавить к покупкам"')
    def get_add_to_purchases_btn(self):
        return self.wait_for_element_visible(RecipeLocators.ADD_TO_PURCHASES_BUTTON)
    
    @allure.step('Получить значение атрибута по карточке созданного рецепта')
    def get_recipe_attribute(self):
        element = self.wait_for_element_visible(RecipeLocators.RECIPE_CARD)
        return element.get_attribute('alt')



