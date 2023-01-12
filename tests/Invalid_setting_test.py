
from api import PetFriends
from settings import valid_email, valid_password
from invalid_setting import invalid_email, invalid_password

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """Проверяем что при валидном email и password запрос api ключа возвращает статус 200
     и в результате содержится слово key"""
    # Сравниваем полученный ответ с ожидаемым результатом
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result
    # Все в порядке. Ключ получен.


def test_get_api_key_for_invalid_email_user(email=invalid_email, password=valid_password):
    """Проверяем что при невалидном значении email запрос api ключа возвращает статус 403
     и в результате не содержится слово key(ключ не получен)"""
    # Сравниваем полученный ответ с ожидаемым результатом
    status, result = pf.get_api_key(email, password)
    # Можно упростить и написать status != 200, но мы хотим убедиться, что именно
    # "доступ к запрошенному ресурсу запрещен" поэтому сравним так:
    assert status == 403
    assert 'key' not in result
    # Ок. С невалидным значением email доступ запрещен, ключ не получен.


def test_get_api_key_for_invalid_password_user(email=valid_email, password=invalid_password):
    """Проверяем что при невалидном значении password запрос api ключа возвращает статус 403
     и в результате не содержится слово key(ключ не получен)"""

    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result
    # С невалидным значением password доступ запрещен, ключ не получен.


def test_get_api_key_for_full_invalid_setting(email=invalid_email, password=invalid_password):
    """Проверяем что при невалидных значениях и email и password запрос api ключа возвращает статус 403
     и в результате не содержится слово key(ключ не получен)"""

    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result
    # Чуда не произошло, с невалидными значениями и email и password доступ запрещен, ключ не получен.

# Нет никакого смысла делать другие тесты с невалидными значениями email или password, так как эти тесты показали,
# что получение ключа невозможно, доступ к ресурсу запрещен.
