import allure

from litres_project_tests.helpers.base_api import BaseApi
from litres_project_tests.helpers.logging_and_attach import log_and_attach_allure_info

base_api = BaseApi()


@allure.epic('API Корзины')
@allure.story('Добавление и удаление книг в корзину неавторизованным пользователем')
class TestBasket:

    @allure.title('Добавление неавторизованным пользователем книги в корзину')
    @allure.feature('Неавторизованный пользователь')
    @allure.label('API')
    @allure.tag('basket')
    @allure.severity('critical')
    def test_add_book_to_basket(self, api_url):
        with allure.step('Получить id книги из раздела Рекомендации для вас'):
            book_id = base_api.get_available_book(api_url)
        with allure.step('Добавить книгу в корзину'):
            result = base_api.add_book_in_basket(api_url, book_id)
        log_and_attach_allure_info(result)

    @allure.title('Удаление книги из корзины неавторизованным пользователем')
    @allure.feature('Неавторизованный пользователь')
    @allure.label('API')
    @allure.tag('basket')
    @allure.severity('critical')
    def test_delete_book_from_basket(self, api_url):
        with allure.step('Получить id книги из раздела Рекомендации для вас'):
            book_id = base_api.get_available_book(api_url)
        with allure.step('Добавить книгу в корзину неавторизованным пользователем'):
            base_api.add_book_in_basket(api_url, book_id)
        with allure.step('Удалить книгу из корзины неавторизованным пользователем'):
            result = base_api.delete_book_in_basket(api_url, book_id)
        log_and_attach_allure_info(result)
