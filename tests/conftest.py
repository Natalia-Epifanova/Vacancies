import pytest

from src.vacancy import Vacancy


@pytest.fixture()
def first_vacancy():
    return Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100000 - 150000 руб.", "Требования: опыт работы от 3 лет...")


@pytest.fixture
def second_vacancy():
    return Vacancy("Java Developer", "https://hh.ru/vacancy/123457", "120000 - 150000 руб.", "Требования: опыт работы от 3 лет...")