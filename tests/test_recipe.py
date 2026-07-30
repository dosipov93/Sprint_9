import allure
import pytest
from utils.generator import generate_recipe_data
from pages.recipe_page import RecipePage
from utils.file_utils import get_asset_path


class TestRecipe:
    @allure.title('Создание рецепта и проверка отображения карточки с корректным названием')
    def test_create_recipe(self, driver, login_user):
        recipe_data = generate_recipe_data()
        recipe_page = RecipePage(driver)
        recipe_page.open_recipe_page()
        recipe_page.fill_title(recipe_data['title'])
        recipe_page.deselect_breakfast_tag()
        recipe_page.deselect_dinner_tag()
        recipe_page.enter_ingredient_name(recipe_data['ingredient_name'])
        recipe_page.select_ingredient_from_dropdown()
        recipe_page.enter_ingredient_quantity(recipe_data['quantity'])
        recipe_page.click_add_ingredient_btn()
        recipe_page.fill_cooking_time(recipe_data['cooking_time'])
        recipe_page.fill_description(recipe_data['description'])
        recipe_page.upload_photo(recipe_data['photo'])
        recipe_page.click_create_recipe_btn()
        assert recipe_page.get_add_to_purchases_btn().is_displayed(), (
            'Карточка созданного рецепта не отображается'
        )
        assert recipe_page.get_recipe_attribute() in recipe_data['title'], (
            'Название рецепта не соответствует созданному'
        )
      