import pytest

from src.vacancy import Vacancy


@pytest.fixture()
def first_vacancy():
    return Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100000 - 150000 руб.",
                   "Требования: опыт работы от 3 лет...")


@pytest.fixture
def second_vacancy():
    return Vacancy("Java Developer", "https://hh.ru/vacancy/123457", "120000 - 150000 руб.",
                   "Требования: опыт работы от 3 лет...")


@pytest.fixture()
def vacancy_dict():
    return {"name": "Python Developer",
            "alternate_url": "<https://hh.ru/vacancy/123456>",
            "salary": "100000 - 150000 руб.",
            "snippet": "Требования: опыт работы от 3 лет..."}


@pytest.fixture()
def salary_test():
    return "100000 - 150000"



@pytest.fixture()
def vacancy_from_hh():
    return {"id": "93353083",
            "name": "Тестировщик комфорта квартир",
            "salary": {
                "from": 350000,
                "to": 450000,
                "currency": "RUR",
                "gross": False
            },
            "snippet": {
                "requirement": "Занимать активную жизненную позицию...",
                "responsibility": "Оценивать вид из окна: встречать рассветы на кухне..."
            },
            "alternate_url": "https://hh.ru/vacancy/93353083"
            }
@pytest.fixture()
def vacancy_half_of_params():
    return {"id": "93353083",
            "name": "Тестировщик комфорта квартир",
            "salary": {
                "from": 350000,
                "to": None,
                "currency": "RUR",
                "gross": False
            },
            "snippet": {
                "requirement": "Занимать активную жизненную позицию...",
                "responsibility": None
            },
            "alternate_url": "https://hh.ru/vacancy/93353083"
            }

@pytest.fixture()
def vacancy_half_of_params_2():
    return {"id": "93353083",
            "name": "Тестировщик комфорта квартир",
            "salary": {
                "from": None,
                "to": 450000,
                "currency": "RUR",
                "gross": False
            },
            "snippet": {
                "requirement": None,
                "responsibility": "Оценивать вид из окна: встречать рассветы на кухне..."
            },
            "alternate_url": "https://hh.ru/vacancy/93353083"
            }