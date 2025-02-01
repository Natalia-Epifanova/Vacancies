from abc import ABC, abstractmethod

class APIRequest(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def api_connect(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


