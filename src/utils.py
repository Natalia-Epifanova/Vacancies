import re
from typing import Any

from src.vacancy import Vacancy


def type_of_salary(vacancy: dict) -> str:
    """Функция, преобразующая зарплату в нужный вид"""
    salary_str = "Зарплата не указана"

    salary = vacancy.get("salary")
    if isinstance(salary, dict) and salary is not None:
        salary_from = salary.get("from")
        salary_to = salary.get("to")
        if salary_from is not None and salary_to is not None:
            salary_str = f"{salary_from} - {salary_to}"
        elif salary_from is not None:
            salary_str = f"{salary_from}"
        elif salary_to is not None:
            salary_str = f"{salary_to}"
    elif isinstance(salary, str):
        salary_str = salary

    return salary_str


def type_of_description(vacancy: dict) -> str:
    """Функция, преобразующая описание в нужный вид"""
    description_str = "Нет информации о требованиях и обязанностях"

    snippet = vacancy.get("snippet")
    if isinstance(snippet, dict) and snippet is not None:
        requirement = snippet.get("requirement")
        responsibility = snippet.get("responsibility")
        if requirement is not None and responsibility is not None:
            description_str = f"Требования: {requirement}. \n" f"Обязанности: {responsibility}"
        elif requirement is not None:
            description_str = f"Требования: {requirement}."
        elif responsibility is not None:
            description_str = f"Обязанности: {responsibility}"
    elif isinstance(snippet, str):
        description_str = snippet

    return description_str


def get_min_salary(salary_str: str) -> Any:
    """Извлекает минимальную зарплату из строки"""
    match = re.search(r"(\d+)", salary_str)
    if match:
        return int(match.group(1))
    return float("inf")


def dict_to_vac(vacancy_dict: dict) -> Vacancy:
    """Метод для преобразования словаря в объект класс Vacancy"""
    remade_vacancy = Vacancy(
        vacancy_dict["name"],
        vacancy_dict["alternate_url"],
        type_of_salary(vacancy_dict),
        type_of_description(vacancy_dict),
    )
    return remade_vacancy


def vac_to_dict(vac: Vacancy) -> dict:
    remade_vacancy = {
        "name": vac.vacancy_name,
        "alternate_url": vac.vacancy_url,
        "salary": vac.salary,
        "snippet": vac.description,
    }
    return remade_vacancy
