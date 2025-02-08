from typing import Any


class Vacancy:
    """Класс для работы с вакансиями"""

    vacancy_name: str
    vacancy_url: str
    salary: str
    description: str

    __slots__ = ("vacancy_name", "vacancy_url", "salary", "description")

    def __init__(self, vacancy_name: str, vacancy_url: str, salary: str, description: str) -> None:
        """Инициализация класса"""
        self.vacancy_name = vacancy_name
        self.vacancy_url = vacancy_url
        self.salary = salary
        self.description = description
        self.__validate()

    def __validate(self) -> None:
        """Метод для валидации данных"""
        if not isinstance(self.vacancy_name, str) or not self.vacancy_name:
            raise ValueError("Название вакансии должно быть указано")
        if not isinstance(self.vacancy_url, str) or "http" not in self.vacancy_url:
            raise ValueError("Ссылка на вакансию должна быть корректной URL.")
        if not isinstance(self.salary, str):
            raise ValueError("Зарплата должна быть указана строкой")
        if not isinstance(self.description, str):
            raise ValueError("Описание должно быть строкой.")
        if not self.salary:
            self.salary = "Зарплата не указана"

    def __lt__(self, other: object) -> Any:
        """Магический метод для сравнения вакансий по зарплате/меньше"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary

    def __gt__(self, other: object) -> Any:
        """Магический метод для сравнения вакансий по зарплате/больше"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary > other.salary
