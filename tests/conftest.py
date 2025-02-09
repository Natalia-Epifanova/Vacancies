import pytest

from src.json_saver import JSONSaver
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


@pytest.fixture()
def json_saver_for_test():
    return JSONSaver()


@pytest.fixture()
def two_vacs_from_hh():
    return {
        "items": [
            {
                "id": "1",
                "name": "Java-разработчик",
                "alternate_url": "https://hh.ru/vacancy/1",
                "salary": None,
                "snippet": {
                    "requirement": None,
                    "responsibility": "Разработка приложений"
                }
            },
            {
                "id": "2",
                "name": "Python-разработчик",
                "alternate_url": "https://hh.ru/vacancy/2",
                "salary": None,
                "snippet": {
                    "requirement": None,
                    "responsibility": "Анализ данных"
                }
            }
        ]
    }


@pytest.fixture()
def vacancies_for_filter():
    return [{
        "name": "Промоутер-консультант в школу программирования Sky Pro",
        "alternate_url": "https://hh.ru/vacancy/116920119",
        "salary": "40000 - 65000",
        "snippet": "Требования: Ты общительный и любишь людей. *Обладаешь грамотной речью и располагаешь к себе.."},
        {
            "name": "QA инженер/Тестировщик",
            "alternate_url": "https://hh.ru/vacancy/116907826",
            "salary": "200000",
            "snippet": "Требования: Стаж написания автоматических тестов от 1 года ..."
        },
        {
            "name": "Junior Developer (стажер)",
            "alternate_url": "https://hh.ru/vacancy/116792570",
            "salary": "70000",
            "snippet": "Требования: Базовые знания фронтенд-технологий: HTML, CSS, JavaScript. Обязанности: Участие в разработке программного обеспечения "
        }]
