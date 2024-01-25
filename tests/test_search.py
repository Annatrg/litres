import allure

from litres_project_tests.helpers.base_api import base_api
from litres_project_tests.helpers.logging_and_attach import log_and_attach_allure_info


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
        log_and_attach_allure_info(result)
