
from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_add_null_pet(name='', animal_type='', age=''):
    """Проверяем возможность добавления карточки питомца с пустыми полями."""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца с пустыми полями данных
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name
    # Это баг. Вопреки ожиданиям питомец добавлен на ресурс со всеми пустыми значениями.


def test_add_new_pet_with_negative_age(name='Pet', animal_type='555', age='-10'):
    """Проверяем что можно добавить питомца с отрицательным значением возраста"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['age'] == age
    # Это баг. Значение возраст не может быть отрицательным


def test_add_new_pet_with_negative_animal_type(name='Pet', animal_type='555', age='10'):
    """Проверяем что можно добавить питомца с числовыми значениями вместо названия породы"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['animal_type'] == animal_type
    # Это баг. Значение порода должно быть осмысленным


def test_add_new_pet_with_webp_photo(name='WEBP', animal_type='двортерьер',
                                     age='104', pet_photo='image/dr-n.webp'):
    """Проверяем что можно добавить питомца с корректными данными и картинкой в формате WEBP"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name
    # ЭТО БАГ. Тест пройден успешно. Добавлен питомец с фото в WEBP формате. Согласно документации Swagger,
    # этот формат не должен приниматься.
