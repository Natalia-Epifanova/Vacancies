from abc import ABC, abstractmethod

class WorkWithFiles(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def read_data(self):
        pass


    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

#Определить абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
# получения данных из файла по указанным критериям и удаления информации о вакансиях. Создать класс
# для сохранения информации о вакансиях в JSON-файл. Дополнительно, по желанию, можно реализовать классы
# для работы с другими форматами, например с CSV- или Excel-файлом, с TXT-файлом.