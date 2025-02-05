from src.api_request import APIRequest
import requests


class HeadHunterAPI(APIRequest):
    """Класс для работы с вакансиями"""

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []

    def _APIRequest__api_connect(self):
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code == 200:
            return response
        else:
            print(f"Ошибка при получении вакансий: {response.status_code}")

    def get_vacancies(self, keyword):
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = self._APIRequest__api_connect()
            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.__params["page"] += 1
            return self.vacancies


# hh_api = HeadHunterAPI()
# hh_vacancies = hh_api.get_vacancies("Python")
# print(hh_vacancies)
