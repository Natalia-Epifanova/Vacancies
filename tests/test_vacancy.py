import pytest

from src.vacancy import Vacancy


def test_vacancy_init(first_vacancy):
    """Тест корректной инициализации класса"""
    assert first_vacancy.vacancy_name == "Python Developer"
    assert first_vacancy.vacancy_url == "<https://hh.ru/vacancy/123456>"
    assert first_vacancy.salary == "100000 - 150000 руб."
    assert first_vacancy.description == "Требования: опыт работы от 3 лет..."


def test_vacancy_validate_invalid_url():
    """Тест на выбрасывание ошибки при некорректном url"""
    with pytest.raises(ValueError):
        Vacancy("Python Developer", "<invalid_url>", "100000 - 150000 руб.", "Требования: опыт работы от 3 лет...")


def test_vacancy_validate_missing_name():
    """Тест на выбрасывание ошибки при отсутствии указания name"""
    with pytest.raises(ValueError):
        Vacancy("", "https://hh.ru/vacancy/123456", "100000 - 150000 руб.", "Требования: опыт работы от 3 лет...")


def test_vacancy_validate_wrong_salary():
    """Тест на выбрасывание ошибки при некорректной salary"""
    with pytest.raises(ValueError):
        Vacancy("Python Developer", "https://hh.ru/vacancy/123456", 120000, "Требования: опыт работы от 3 лет...")


def test_vacancy_validate_wrong_description():
    """Тест на выбрасывание ошибки при некорректном description"""
    with pytest.raises(ValueError):
        Vacancy("Python Developer", "https://hh.ru/vacancy/123456", "100000 - 150000 руб.", [12, 34, 5])


def test_vacancy_validate_missing_salary():
    """Тест на выбрасывание ошибки при отсутствии salary"""
    vac = Vacancy("Python Developer", "https://hh.ru/vacancy/123456", "", "Требования: опыт работы от 3 лет...")
    vac.salary = "Зарплата не указана"


def test_vacancy_lt(first_vacancy, second_vacancy):
    """Тест магического метода lt"""
    assert first_vacancy < second_vacancy


def test_vacancy_gt(first_vacancy, second_vacancy):
    """Тест магического метода gt"""
    assert second_vacancy > first_vacancy


def test_vacancy_lt_not_a_vacancy(first_vacancy):
    """Тест магического метода lt с некорректными данными"""
    with pytest.raises(TypeError):
        first_vacancy < "string"
    with pytest.raises(TypeError):
        first_vacancy < None
    with pytest.raises(TypeError):
        first_vacancy < 123


def test_vacancy_gt_not_a_vacancy(second_vacancy):
    """Тест магического метода gt с некорректными данными"""
    with pytest.raises(TypeError):
        second_vacancy > "string"
    with pytest.raises(TypeError):
        second_vacancy > None
    with pytest.raises(TypeError):
        second_vacancy > 123
