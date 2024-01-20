import json
import logging
import allure
from allure_commons.types import AttachmentType

from litres.helpers.API.base_api import BaseApi

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
