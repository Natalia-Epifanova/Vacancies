import pytest

from src.json_saver import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture()
def first_vacancy():
    return Vacancy(
        "Python Developer",
        "<https://hh.ru/vacancy/123456>",
        "100000 - 150000 руб.",
        "Требования: опыт работы от 3 лет...",
    )


@pytest.fixture
def second_vacancy():
    return Vacancy(
        "Java Developer", "https://hh.ru/vacancy/123457", "120000 - 150000 руб.", "Требования: опыт работы от 3 лет..."
    )


@pytest.fixture()
def vacancy_dict():
    return {
        "name": "Python Developer",
        "alternate_url": "<https://hh.ru/vacancy/123456>",
        "salary": "100000 - 150000 руб.",
        "snippet": "Требования: опыт работы от 3 лет...",
    }


@pytest.fixture()
def salary_test():
    return "100000 - 150000"


@pytest.fixture()
def vacancy_from_hh():
    return {
        "id": "93353083",
        "name": "Тестировщик комфорта квартир",
        "salary": {"from": 350000, "to": 450000, "currency": "RUR", "gross": False},
        "snippet": {
            "requirement": "Занимать активную жизненную позицию...",
            "responsibility": "Оценивать вид из окна: встречать рассветы на кухне...",
        },
        "alternate_url": "https://hh.ru/vacancy/93353083",
    }


@pytest.fixture()
def vacancy_half_of_params():
    return {
        "id": "93353083",
        "name": "Тестировщик комфорта квартир",
        "salary": {"from": 350000, "to": None, "currency": "RUR", "gross": False},
        "snippet": {"requirement": "Занимать активную жизненную позицию...", "responsibility": None},
        "alternate_url": "https://hh.ru/vacancy/93353083",
    }


@pytest.fixture()
def vacancy_half_of_params_2():
    return {
        "id": "93353083",
        "name": "Тестировщик комфорта квартир",
        "salary": {"from": None, "to": 450000, "currency": "RUR", "gross": False},
        "snippet": {"requirement": None, "responsibility": "Оценивать вид из окна: встречать рассветы на кухне..."},
        "alternate_url": "https://hh.ru/vacancy/93353083",
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
                "snippet": {"requirement": None, "responsibility": "Разработка приложений"},
            },
            {
                "id": "2",
                "name": "Python-разработчик",
                "alternate_url": "https://hh.ru/vacancy/2",
                "salary": None,
                "snippet": {"requirement": None, "responsibility": "Анализ данных"},
            },
        ]
    }


@pytest.fixture()
def vacancies_for_filter():
    return [
        Vacancy(
            "Промоутер-консультант в школу программирования Sky Pro",
            "https://hh.ru/vacancy/116920119",
            "40000 - 65000",
            "Требования: Ты общительный и любишь людей. *Обладаешь грамотной речью и располагаешь к себе..",
        ),
        Vacancy(
            "QA инженер/Тестировщик",
            "https://hh.ru/vacancy/116907826",
            "200000",
            "Требования: Стаж написания автоматических тестов от 1 года ...",
        ),
        Vacancy(
            "Junior Developer (стажер)",
            "https://hh.ru/vacancy/116792570",
            "70000",
            "Требования: Базовые знания фронтенд-технологий: HTML, CSS, JavaScript. "
            "Обязанности: Участие в разработке программного обеспечения ",
        ),
    ]


@pytest.fixture()
def sorted_vacancies():
    return (
        "Вакансия номер 1: Название: QA инженер/Тестировщик, Ссылка: https://hh.ru/vacancy/116907826, "
        "Зарплата: 200000, Описание: Требования: Стаж написания автоматических тестов от 1 года ...\n"
        "Вакансия номер 2: Название: Junior Developer (стажер), Ссылка: https://hh.ru/vacancy/116792570, "
        "Зарплата: 70000, Описание: Требования: Базовые знания фронтенд-технологий: HTML, CSS, JavaScript. "
        "Обязанности: Участие в разработке программного обеспечения \nВакансия номер 3: "
        "Название: Промоутер-консультант в школу программирования Sky Pro, Ссылка: https://hh.ru/vacancy/116920119, "
        "Зарплата: 40000 - 65000, Описание: Требования: Ты общительный и любишь людей. "
        "*Обладаешь грамотной речью и располагаешь к себе.."
    )


@pytest.fixture
def third_vacancy():
    return Vacancy(
        "Java Developer", "https://hh.ru/vacancy/123457", "120000 - 150000 руб.", "Требования: опыт работы от 3 лет"
    )
