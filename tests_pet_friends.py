import pytest
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password


def tests_pet_friends():
    """Проверка карточек питомцев всех пользователей
    на наличие фото, имени и описания (порода и возраст)"""

    # Установка неявного ожидания
    pytest.driver.implicitly_wait(10)

    # Ввод эл.почты
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

    # Ввод пароля
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

    # Клик по кнопке "Войти"
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверка того, что осуществлен переход на главную страницу пользователя
    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

    # Объявление трех переменных, в которые будут записаны все найденные элементы на странице:
    # в images — все картинки питомцев, в names — все их имена, в descriptions — все виды и возрасты

    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    # Далее следуют проверки:

    assert names[0].text != ''

    for i in range(len(names)):

        # Берём элемент с номером i (картинка для i-й карточки питомца).
        # Каждая картинка имеет атрибут src, если была загружена, и не
        # имеет его, если отсутствует для данного питомца

        assert images[i].get_attribute('src') != ''

        # Для проверки существования фотографии в карточке проверяем,
        # что путь, указанный в атрибуте src, не пустой

        assert names[i].text != ''

        # Берём i-го питомца и смотрим, что элемент, который должен
        # содержать его имя, имеет не пустой текст

        assert descriptions[i].text != ''
        assert ',' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0