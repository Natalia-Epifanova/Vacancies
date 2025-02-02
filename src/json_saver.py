import json
from typing import List, Dict

from src.vacancy import Vacancy
from src.work_with_files import WorkWithFiles


class JSONSaver(WorkWithFiles):

    def __init__(self, filename='data/vacancies.json'):
        self.filename = filename
        self.vacancies_list = []

    def add_vacancy(self, vacancies: List[Dict]):
        with open(self.filename, 'w') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def read_data(self):
        try:
            with open(self.filename, 'r') as json_file:
                data = json.load(json_file)
            vacancies_list = []
            for vacancy in data['items']:
                next_vacancy = Vacancy
                next_vacancy.vacancy_name = vacancy['name']
                next_vacancy.vacancy_url = vacancy["alternate_url"]
                next_vacancy.salary = str(vacancy["salary"]["from"] + "-" + vacancy["salary"]["to"])
                next_vacancy.description = f"Требования: {vacancy["snippet"]["requirement"]}. \nОбязанности: {vacancy["snippet"]["responsibility"]}"
                vacancies_list.append(next_vacancy)

                self.vacancies_list = vacancies_list
        except FileNotFoundError:
            print(f'Файл {self.filename} не найден')

    def delete_vacancy(self, vacancy):
        pass
