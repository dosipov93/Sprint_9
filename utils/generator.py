from faker import Faker


fake_en = Faker('en_US')
fake_ru = Faker('ru_RU')

def generate_user():
    return {
        'first_name': fake_ru.first_name(),
        'last_name': fake_ru.last_name(),
        'user_name': fake_en.user_name(),
        'email': fake_en.email(),
        'password': fake_en.password(length=10)
    }

def generate_recipe_data():
    return {
        'title': 'Том Ям "8 жизней"',
        'ingredient_name': 'ежевика',
        'quantity': '80',
        'cooking_time': '30',
        'description': 'Всего 300 калорий и 100% чувство вины. Рекомендуется запивать валерьянкой для спокойствия совести.',
        'photo': 'tom_yam_8_lives.jpg'
    }
