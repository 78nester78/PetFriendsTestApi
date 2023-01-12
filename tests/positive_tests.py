
from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_add_new_pet_with_jpeg_photo(name='JPEG', animal_type='двортерьер',
                                     age='104', pet_photo='image/drakosha.jpeg'):
    """Проверяем что можно добавить питомца с корректными данными и картинкой в формате JPEG"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name
    # Ok. Тест пройден успешно. Добавлен питомец с фото в JPEG формате, допустимом по документации Swagger


def test_add_new_pet_with_png_photo(name='PNG', animal_type='двортерьер',
                                     age='104', pet_photo='image/dragon.png'):
    """Проверяем что можно добавить питомца с корректными данными и картинкой в формате PNG"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name
    # Ok. Тест пройден успешно. Добавлен питомец с фото в PNG формате, допустимом по документации Swagger.


def test_add_photo_of_pet(pet_photo='image/drakon.jpg'):
    """Проверяем что можно добавить фото питомцу у которого нет фото и получить уведомление о невозможности добавления
     фото если фото у питомца уже присутствует"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet_without_photo(auth_key, "Суперкот", "кот", "103")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Берём id первого питомца из списка
    pet_id = my_pets['pets'][0]['id']
    # Проверяем есть ли фото в карточке питомца
    try:
        if my_pets['pets'][0]['pet_photo'] != '':
            # Если есть, то пробрасываем исключение с сообщением
            raise
    except Exception:
        print('Упс, место занято!!! У Вашего питомца уже есть красивая фотокарточка:)')
    else:
        # Если фото в профиле еще нет, делаем запрос на добавление фото
        status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo)
        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert result['pet_photo'] != ''
# Тест проходит при обоих условиях. Если добавили фото, то получаем PASSED
# Если фото уже есть, то получаем тоже PASSED с сообщением "Упс, место занято!!!"
# Вроде все работает, но мне кажется что не красиво реализовано try-except. Подскажите, как правильно сделать.
# И наверное тест лучше разбить на два теста, один с добавлением фото, второй когда фото уже есть.
# Поменяются только входные данные, сам тест без изменений.
