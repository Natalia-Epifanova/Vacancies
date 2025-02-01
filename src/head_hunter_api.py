from src.api_request import APIRequest
import requests


class HeadHunterAPI(APIRequest):
    """Класс для работы с вакансиями"""

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def api_connect(self):
        return requests.get(self.url, headers=self.headers, params=self.params)

    def get_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = self.api_connect()
            if response.status_code == 200:
                vacancies = response.json()['items']
                self.vacancies.extend(vacancies)
                self.params['page'] += 1
            else:
                print(f"Ошибка при получении вакансий: {response.status_code}")
