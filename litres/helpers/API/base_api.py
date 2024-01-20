import jsonschema
import json

import allure
import requests
from requests import Response

from litres.utils.data import load_schema



class BaseApi:

    def get_available_book(self, api_url):
        endpoint = '/arts/personal-recommendations'
        book_list: Response = requests.get(api_url + endpoint)
        book_id = book_list.json().get('payload').get("data")[0].get('id')
        return int(book_id)

    def add_book_in_wishlist(self, api_url, book_id):
        endpoint = '/wishlist/arts/'
        result: Response = requests.put(url=f'{api_url}{endpoint}{book_id}')

        with allure.step('Проверить, что API возвращает 204 код ответа'):
            assert result.status_code == 204
        with allure.step('Проверить, что нет тела ответа'):
            assert not result.content

        return result

    def delete_book_in_wishlist(self, api_url, book_id):
        endpoint = '/wishlist/arts/'
        result: Response = requests.delete(url=f'{api_url}{endpoint}{book_id}', headers={'Wishlist': f'{book_id}'})

        with allure.step('Проверить, что API возвращает 204 код ответа'):
            assert result.status_code == 204
        with allure.step('Проверить, что нет тела ответа'):
            assert not result.content

        return result

    def add_book_in_basket(self, api_url, book_id):
        add_book_schema = load_schema('add_book_in_basket.json')
        endpoint = '/cart/arts/add'
        body = {"art_ids": [book_id]}
        result: Response = requests.put(url=f'{api_url}{endpoint}', headers={'Content-Type': 'application/json'},
                                        data=json.dumps(body))
        with allure.step('Проверить, что API возвращает 200 код ответа'):
            assert result.status_code == 200
        with allure.step('Проверить схему ответа'):
            add_book_result = result.json()
            jsonschema.validate(add_book_result, add_book_schema)
        return result

    def delete_book_in_basket(self, api_url, book_id):
        endpoint = '/cart/arts/remove'
        book = int(book_id)
        body = {"art_ids": [book]}
        result: Response = requests.put(url=f'{api_url}{endpoint}', data=json.dumps(body))
        with allure.step('Проверить, что API возвращает 204 код ответа'):
            assert result.status_code == 204
        with allure.step('Проверить, что нет тела ответа'):
            assert not result.content

        return result

    def get_basket(self, api_url):
        get_basket_schema = load_schema('get_basket.json')
        endpoint = '/cart/status'
        result: Response = requests.get(url=f'{api_url}{endpoint}')
        with allure.step('что API возвращает 200 код ответа'):
            assert result.status_code == 200
        with allure.step('Проверить схему ответа'):
            get_basket_result = result.json()
            jsonschema.validate(get_basket_result, get_basket_schema)
        return result

    def search_book(self, api_url, key_word):
        search_book_schema = load_schema('get_basket.json')
        endpoint = '/search/suggestions'
        query_params = f'q={key_word}'
        result: Response = requests.get(url=f'{api_url}{endpoint}?{query_params}')
        with allure.step('Проверить, что API возвращает 200 код ответа'):
            assert result.status_code == 200
        with allure.step('Проверить, что в ответе содержится ключевая фраза'):
            assert 'мой театр' in result.text
        with allure.step('Проверить схему ответа'):
            search_book_result = result.json()
            jsonschema.validate(search_book_result, search_book_schema)
        return result
