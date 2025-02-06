from typing import List, Dict

from src.utils import get_min_salary


class JSONFilter:
    """Класс для обработки данных в JSON файле"""
    vacancies_list: list

    def __init__(self, vacancies_list: list) -> None:
        """Инициализация класса"""
        self.vacancies_list = vacancies_list

    def filter_vacancies(self, list_of_keywords: list) -> List[Dict]:
        """Метод для фильтрации вакансий по ключевым словам"""
        filtered_vacancies = []
        for vacancy in self.vacancies_list:
            if any(keyword.lower() in vacancy['name'].lower() or keyword.lower() in vacancy['snippet'].lower() for
                   keyword in list_of_keywords):
                filtered_vacancies.append(vacancy)
        return filtered_vacancies

    def get_vacancies_by_salary(self, min_salary:float, max_salary:float) -> List[Dict]:
        """Метод для фильтрации вакансий по диапазону зарплат"""
        filtered_vacancies = []
        for vacancy in self.vacancies_list:
            salary_str = vacancy['salary']
            salary_min = get_min_salary(salary_str)
            if salary_min != float('inf') and min_salary <= salary_min <= max_salary:
                filtered_vacancies.append(vacancy)
        return filtered_vacancies

    def sort_vacancies(self) -> List[Dict]:
        """Метод для сортировки вакансий по минимальной зарплате по убыванию"""
        sorted_vacancies = sorted(self.vacancies_list, key=lambda x: get_min_salary(x['salary']), reverse=True)
        return sorted_vacancies

    def get_top_vacancies(self, top_number: int) -> List[Dict]:
        """Метод для получения топ N вакансий"""
        return self.vacancies_list[:top_number]

