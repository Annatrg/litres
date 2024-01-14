import jsonschema
import json

import allure
import requests
from requests import Response


class BaseApi:

    def get_available_book(self, api_url):
        endpoint = '/arts/personal-recommendations'
        book_list: Response = requests.get(api_url + endpoint)
        book_id = book_list.json().get('payload').get("data")[0].get('id')
        return str(book_id)

    def add_book_in_wishlist(self, api_url, book_id):
        endpoint = '/wishlist/arts/'
        result: Response = requests.put(api_url + endpoint + f'{book_id}')

        with allure.step('Проверить, что API возвращает 204 код ответа'):
            assert result.status_code == 204
        with allure.step('Проверить, что нет тела ответа'):
            assert not result.content

        return result

    def delete_book_in_wishlist(self, api_url, book_id):
        endpoint = '/wishlist/arts/'
        result: Response = requests.delete(url=f'{api_url}{endpoint}' + f'{book_id}')
        with allure.step('Проверить, что API возвращает 204 код ответа'):
            assert result.status_code == 204
        with allure.step('Проверить, что нет тела ответа'):
            assert not result.content

        return result

    def add_book_in_basket(self, api_url, book_id):
        endpoint = '/cart/arts/add'
        book = int(book_id)
        body = {"art_ids": [book]}
        result: Response = requests.put(url=f'{api_url}{endpoint}', data=body)
        with allure.step('Проверить, что API возвращает 200 код ответа'):
            assert result.status_code == 200
        with allure.step('Проверить схему ответа'):
            with open('C:/Users/annaa/PycharmProjects/litres/litres/helpers/schemas/add_book_in_basket.json') as file:
                schema = json.load(file)
                jsonschema.validate(result.json(), schema), f'Схема ответа не соответствует ожидаемой'
        return result

    def delete_book_in_basket(self, api_url, book_id):
        endpoint = '/cart/arts/remove'
        book = int(book_id)
        body = {"art_ids": [book]}
        result: Response = requests.put(url=f'{api_url}{endpoint}', data=body)
        with allure.step('Проверить, что API возвращает 200 код ответа'):
            assert result.status_code == 204
        with allure.step('Проверить, что нет тела ответа'):
            assert not result.content
        return result

    def get_basket(self, api_url):
        endpoint = '/cart/status'
        result: Response = requests.get(url=f'{api_url}{endpoint}')
        with allure.step('что API возвращает 200 код ответа'):
            assert result.status_code == 200
        with allure.step('Проверить схему ответа'):
            with open('C:/Users/annaa/PycharmProjects/litres/litres/helpers/schemas/get_basket.json') as file:
                schema = json.load(file)
                jsonschema.validate(result.json(), schema), f'Схема ответа не соответствует ожидаемой'
        return result

    def search_book(self, api_url, key_word):
        endpoint = '/search/suggestions'
        query_params = f'q={key_word}'
        result: Response = requests.get(url=f'{api_url}{endpoint}?{query_params}')
        with allure.step('Проверить, что API возвращает 200 код ответа'):
            assert result.status_code == 200
        with allure.step('Проверить, что в ответе содержится ключевая фраза'):
            assert 'мой театр' in result.text
        with allure.step('Проверить схему ответа'):
            with open('C:/Users/annaa/PycharmProjects/litres/litres/helpers/schemas/search.json') as file:
                schema = json.load(file)
                jsonschema.validate(result.json(), schema), f'Схема ответа не соответствует ожидаемой'
        return result
