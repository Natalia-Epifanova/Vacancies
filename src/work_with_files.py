from abc import ABC, abstractmethod
from typing import Any

from src.vacancy import Vacancy


class WorkWithFiles(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Абстрактный метод для добавления вакансии в файл"""
        pass

    @abstractmethod
    def read_data(self) -> Any:
        """Абстрактный метод для чтения данных из файла"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Абстрактный метод для удаления вакансии из файла"""
        pass
