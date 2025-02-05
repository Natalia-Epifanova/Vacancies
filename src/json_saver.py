import json
from typing import List, Dict

from src.utils import type_of_salary, type_of_description
from src.vacancy import Vacancy
from src.work_with_files import WorkWithFiles


class JSONSaver(WorkWithFiles):

    def __init__(self, filename="../data/vacancies.json"):
        self.filename = filename
        self.vacancies_list = []

    def __vacancies_in_list(self):
        existing_vacancies = self.read_data()
        new_list = []
        for vac in existing_vacancies:
            data = {
                "name": vac.vacancy_name,
                "alternate_url": vac.vacancy_url,
                "salary": vac.salary,
                "snippet": vac.description,
            }
            new_list.append(data)

        self.vacancies_list = new_list

    def add_vacancy(self, vacancy: Vacancy):
        self.__vacancies_in_list()
        list_of_vacancies = self.vacancies_list
        new_vac = {
            "name": vacancy.vacancy_name,
            "alternate_url": vacancy.vacancy_url,
            "salary": vacancy.salary,
            "snippet": vacancy.description,
        }
        list_of_vacancies.append(new_vac)
        with open(self.filename, "w") as file:
            json.dump(list_of_vacancies, file, ensure_ascii=False, indent=4)

    def read_data(self):
        try:
            with open(self.filename, "r") as json_file:
                data = json.load(json_file)
            for vacancy_data in data:
                next_vacancy = Vacancy(
                    vacancy_data["name"],
                    vacancy_data["alternate_url"],
                    type_of_salary(vacancy_data),
                    type_of_description(vacancy_data),
                )
                self.vacancies_list.append(next_vacancy)
            return self.vacancies_list
        except FileNotFoundError:
            print(f"Файл {self.filename} не найден")
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле {self.filename}. Убедитесь, что файл содержит корректный JSON.")

    def delete_vacancy(self, vacancy):
        pass


vac2 = Vacancy(
    "Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет..."
)
vac1 = Vacancy(
    "Python Developer_1",
    "<https://hh.ru/vacancy/123456>",
    "100 000-150 000 руб.",
    "Требования: опыт работы от 3 лет...",
)

# # Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.add_vacancy(vac1)
# json_saver.delete_vacancy(vac)
