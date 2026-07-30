from selenium.webdriver.common.by import By


class RecipeLocators:
   
    TITLE_FIELD = (By.XPATH, "//div[contains(text(), 'Название рецепта')]/following-sibling::input") # Поле 'Название рецепта'
    BREAKFAST_TAG = (By.XPATH, "//span[text()='Завтрак']/preceding-sibling::button") # Check_box 'Завтрак'
    DINNER_TAG = (By.XPATH, "//span[text()='Ужин']/preceding-sibling::button") # Check_box 'Ужин'
    INGREDIENTS_INPUT = (By.XPATH, "//div[contains(text(), 'Ингредиенты')]/following-sibling::input") # Поле ввода 'Ингредиенты'
    INGREDIENT_SELECT_DROPDOWN = (By.XPATH, "//div[contains(@class, 'styles_container__')]/div[text()='ежевика']") # Выбор ингредиента из выпадающего списка
    INGREDIENTS_QUANTITY = (By.XPATH, "//div[contains(@class, 'styles_ingredientsAmountInputContainer')]//input") # Поле ввода весового значения 
    ACCEPT_INGREDIENT = (By.XPATH, "//div[contains(text(), 'Добавить ингредиент')]") # Кнопка 'Добавить ингредиент'
    DELETE_INGREDIENT_BTN = (By.XPATH, "//span[text()='Удалить']") # Кнопка 'Удалить'
    COOKING_TIME_FIELD = (By.XPATH, "//div[contains(text(), 'Время приготовления')]/following-sibling::input") # Поле ввода 'Время приготовления'
    DESCRIPTION_FIELD =  (By.XPATH, "//div[contains(text(), 'Описание рецепта')]/following-sibling::textarea") # Поле воода 'Описание рецепта'
    PHOTO_INPUT = (By.XPATH, "//input[@type='file']") # Загрузить фото
    SUBMIT_BTN = (By.XPATH, "//button[contains(text(), 'Создать рецепт')]") # Кнопка 'Создаить рецепт'
    ADD_TO_PURCHASES_BUTTON = (By.XPATH, "//button[contains(text(), 'Добавить в покупки')]") # Кнопка 'Добавить в покупки'
    RECIPE_CARD = (By.XPATH, "//div[contains(@class, 'styles_single-card__')]/img") # Карточка созданного Рецепта
    RECIPE_TITLE = (By.XPATH, "//h1[contains(@class, 'styles_single-card__title__')]") # Название Рецепта