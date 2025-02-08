import json
from typing import Any

from src.utils import type_of_description, type_of_salary, dict_to_vac, vac_to_dict
from src.vacancy import Vacancy
from src.work_with_files import WorkWithFiles


class JSONSaver(WorkWithFiles):
    """Класс для работы с JSON файлами"""
    filename: str
    vacancies_list: list

    def __init__(self, filename: str="data/vacancies.json") -> None:
        """Инициализация класса"""
        self.__filename = filename
        self.vacancies_list = []

    def __vacancies_in_list(self) -> None:
        """Метод для получения вакансий в виде списка в нужном формате"""
        existing_vacancies = self.read_data()
        new_list = []
        for vac in existing_vacancies:
            data = vac_to_dict(vac)
            new_list.append(data)

        self.vacancies_list = new_list

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Метод для добавления вакансии в файл"""
        self.__vacancies_in_list()
        list_of_vacancies = self.vacancies_list
        if vac_to_dict(vacancy) not in list_of_vacancies:
            list_of_vacancies.append(vac_to_dict(vacancy))
        with open(self.__filename, "w") as file:
            json.dump(list_of_vacancies, file, ensure_ascii=False, indent=4)

    def read_data(self) -> Any:
        """Метод для чтения данных из файла"""
        try:
            with open(self.__filename, "r") as json_file:
                data = json.load(json_file)
            self.vacancies_list = [dict_to_vac(vacancy_data) for vacancy_data in data]
            return self.vacancies_list
        except FileNotFoundError:
            print(f"Файл {self.__filename} не найден")
        except json.JSONDecodeError:
            print(
                f"Ошибка декодирования JSON в файле {self.__filename}. "
                f"Убедитесь, что файл содержит корректный JSON."
            )

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Метод для удаления вакансии из файла"""
        pass


    @property
    def filename(self) -> Any:
        """Метод-геттер для получения пути сохранения файла с вакансиями"""
        return self.__filename

    @filename.setter
    def filename(self, new_filename: str) -> None:
        """Метод-сеттер для изменения пути сохранения файла с вакансиями"""
        self.__filename = new_filename

#
# vac2 = Vacancy(
#     "Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет..."
# )
# vac1 = Vacancy(
#     "Python Developer_1",
#     "<https://hh.ru/vacancy/123456>",
#     "100 000-180 000 руб.",
#     "Требования: опыт работы от 3 лет...",
# )
#
# # # Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
#
# json_saver.add_vacancy(vac1)
# # json_saver.delete_vacancy(vac)
