import json
import logging
import allure
from allure_commons.types import AttachmentType

from litres.helpers.API.base_api import BaseApi

base_api = BaseApi()


@allure.epic('API Поиска')
@allure.story('Поиск книги через поисковую строку неавторизованным пользователем')
class TestSearch:

    @allure.title('Поиск книги через поисковую строку')
    @allure.feature('Неавторизованный пользователь')
    @allure.label('API')
    @allure.tag('search')
    @allure.severity('critical')
    def test_search_book(self, api_url):
        with allure.step('Отправить поисковый запрос'):
            key_word = 'Мой театр'
            result = base_api.search_book(api_url, key_word)

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
