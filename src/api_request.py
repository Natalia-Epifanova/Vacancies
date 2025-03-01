from abc import ABC, abstractmethod
from typing import Any


class APIRequest(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def _api_connect(self) -> Any:
        """Абстрактный метод для подключения по API"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> Any:
        """Абстрактный метод получения вакансий по API"""
        pass
