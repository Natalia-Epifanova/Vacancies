from typing import List, Dict

from src.utils import get_min_salary


class JSONFilter:
    """Класс для обработки данных в JSON файле"""
    vacancies_list: list

    def __init__(self, vacancies_list: list) -> None:
        """Инициализация класса"""
        self.vacancies_list = vacancies_list

    def __str__(self):
        """Магический метод для отображения отфильтрованных вакансий для пользователей"""
        result = []
        i = 1
        for vac in self.vacancies_list:
            result.append(f"Вакансия номер {i}: Название: {vac.vacancy_name}, Ссылка: {vac.vacancy_url}, "
                          f"Зарплата: {vac.salary}, Описание: {vac.description}")
            i += 1
        return "\n".join(result) or "Нет вакансий для отображения."

    def filter_vacancies(self, list_of_keywords: list) -> List[Dict]:
        """Метод для фильтрации вакансий по ключевым словам"""
        filtered_vacancies = []
        for vacancy in self.vacancies_list:
            if any(keyword.lower() in vacancy.vacancy_name.lower() or keyword.lower() in vacancy.description.lower() for
                   keyword in list_of_keywords):
                filtered_vacancies.append(vacancy)
            self.vacancies_list = filtered_vacancies
        return filtered_vacancies

    def get_vacancies_by_salary(self, min_salary:float, max_salary:float) -> List[Dict]:
        """Метод для фильтрации вакансий по диапазону зарплат"""
        filtered_vacancies = []
        for vacancy in self.vacancies_list:
            salary_str = vacancy.salary
            salary_min = get_min_salary(salary_str)
            if salary_min != float('inf') and min_salary <= salary_min <= max_salary:
                filtered_vacancies.append(vacancy)
            self.vacancies_list = filtered_vacancies
        return filtered_vacancies

    def sort_vacancies(self) -> List[Dict]:
        """Метод для сортировки вакансий по минимальной зарплате по убыванию"""
        sorted_vacancies = sorted(self.vacancies_list, key=lambda x: get_min_salary(x.salary), reverse=True)
        self.vacancies_list = sorted_vacancies
        return sorted_vacancies

    def get_top_vacancies(self, top_number: int) -> List[Dict]:
        """Метод для получения топ N вакансий"""
        self.vacancies_list = self.vacancies_list[:top_number]
        return self.vacancies_list


