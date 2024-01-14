import json
import logging
import allure
from allure_commons.types import AttachmentType

from litres.helpers.API.base_api import BaseApi

base_api = BaseApi()


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
            book_id = base_api.get_available_book(api_url)
        with allure.step('Добавить книгу в Отложенные'):
            result = base_api.add_book_in_wishlist(api_url, book_id)

        allure.attach(body=result.request.url,
                      name="Request url",
                      attachment_type=AttachmentType.TEXT)
        allure.attach(body=result.request.method,
                      name="Request method",
                      attachment_type=AttachmentType.TEXT)
        allure.attach(body=json.dumps(result.request.body, indent=4, ensure_ascii=True),
                      name="Request body",
                      attachment_type=AttachmentType.JSON,
                      extension="json")
        allure.attach(body=str(result.cookies),
                      name="Response cookies",
                      attachment_type=AttachmentType.TEXT,
                      extension="txt")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.cookies)
        logging.info(result.text)

    @allure.title('Удаление неавторизованным пользователем книги из Отложенные')
    @allure.feature('Неавторизованный пользователь')
    @allure.label('API')
    @allure.tag('wishlist')
    @allure.severity('critical')
    def test_delete_from_wishlist(self, api_url):
        with allure.step('Получить id книги из раздела Рекомендации для вас'):
            book_id = base_api.get_available_book(api_url)
        with allure.step('Добавить книгу в Отложенные'):
            added_to_wishlist: base_api.add_book_in_wishlist(api_url, book_id)
        with allure.step('Отправить запрос для удаления добавленной книги из Отложенных'):
            result = base_api.delete_book_in_wishlist(api_url, book_id)

        allure.attach(body=result.request.url,
                      name="Request url",
                      attachment_type=AttachmentType.TEXT)
        allure.attach(body=result.request.method,
                      name="Request method",
                      attachment_type=AttachmentType.TEXT)
        allure.attach(body=json.dumps(result.request.body, indent=4, ensure_ascii=True),
                      name="Request body",
                      attachment_type=AttachmentType.JSON,
                      extension="json")
        allure.attach(body=str(result.cookies),
                      name="Response cookies",
                      attachment_type=AttachmentType.TEXT,
                      extension="txt")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.cookies)
        logging.info(result.text)
