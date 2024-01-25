import allure

from litres_project_tests.helpers.base_api import base
from litres_project_tests.helpers.logging_and_attach import log_and_attach_allure_info



@allure.epic('API Отложенных книг')
@allure.story('Добавление и удаление из Отложенных неавторизованным пользователем')
class TestWishlist:

    @allure.title('Добавление неавторизованным пользователем книги в Отложенные')
    @allure.feature('Неавторизованный пользователь')
    @allure.label('API')
    @allure.tag('wishlist')
    @allure.severity('critical')
    def test_add_to_wishlist(self, api_url):
        with allure.step('Получить id книги из раздела Рекомендации для вас'):
            book_id = base.get_available_book(api_url)
        with allure.step('Добавить книгу в Отложенные'):
            result = base.add_book_in_wishlist(api_url, book_id)
        log_and_attach_allure_info(result)

    @allure.title('Удаление неавторизованным пользователем книги из Отложенные')
    @allure.feature('Неавторизованный пользователь')
    @allure.label('API')
    @allure.tag('wishlist')
    @allure.severity('critical')
    def test_delete_from_wishlist(self, api_url):
        with allure.step('Получить id книги из раздела Рекомендации для вас'):
            book_id = base.get_available_book(api_url)
        with allure.step('Добавить книгу в Отложенные'):
            base.add_book_in_wishlist(api_url, book_id)
        with allure.step('Отправить запрос для удаления добавленной книги из Отложенных'):
            result = base.delete_book_in_wishlist(api_url, book_id)
        log_and_attach_allure_info(result)
