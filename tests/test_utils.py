from src.utils import dict_to_vac, get_min_salary, type_of_description, type_of_salary, vac_to_dict


def test_vac_to_dict(first_vacancy):
    """Тест функции для преобразования объекта класса Vacancy в словарь"""
    result = vac_to_dict(first_vacancy)
    assert result == {
        "name": "Python Developer",
        "alternate_url": "<https://hh.ru/vacancy/123456>",
        "salary": "100000 - 150000 руб.",
        "snippet": "Требования: опыт работы от 3 лет...",
    }


def test_dict_to_vac(vacancy_dict):
    """Тест функции для преобразования словаря в объект класса Vacancy"""
    result = dict_to_vac(vacancy_dict)
    assert result.vacancy_name == "Python Developer"
    assert result.vacancy_url == "<https://hh.ru/vacancy/123456>"
    assert result.salary == "100000 - 150000 руб."
    assert result.description == "Требования: опыт работы от 3 лет..."


def test_get_min_salary(salary_test):
    """Тест функции для выделения минимальной зарплаты из диапазона"""
    assert get_min_salary(salary_test) == 100000.0


def test_type_of_salary(vacancy_from_hh):
    """Тест функции для приведения зарплаты к нужному формату"""
    result = type_of_salary(vacancy_from_hh)
    assert result == "350000 - 450000"


def test_type_of_description(vacancy_from_hh):
    """Тест функции для приведения описания к нужному формату"""
    result = type_of_description(vacancy_from_hh)
    assert (
        result == "Требования: Занимать активную жизненную позицию.... \n"
        "Обязанности: Оценивать вид из окна: встречать рассветы на кухне..."
    )


def test_type_of_salary_from(vacancy_half_of_params):
    """Тест функции для приведения зарплаты к нужному формату, когда есть только from"""
    result = type_of_salary(vacancy_half_of_params)
    assert result == "350000"


def test_type_of_description_requirement(vacancy_half_of_params):
    """Тест функции для приведения описания к нужному формату, когда есть только requirement"""
    result = type_of_description(vacancy_half_of_params)
    assert result == "Требования: Занимать активную жизненную позицию...."


def test_type_of_salary_to(vacancy_half_of_params_2):
    """Тест функции для приведения зарплаты к нужному формату, когда есть только to"""
    result = type_of_salary(vacancy_half_of_params_2)
    assert result == "450000"


def test_type_of_description_responsibility(vacancy_half_of_params_2):
    """Тест функции для приведения описания к нужному формату, когда есть только responsibility"""
    result = type_of_description(vacancy_half_of_params_2)
    assert result == "Обязанности: Оценивать вид из окна: встречать рассветы на кухне..."


def test_get_min_salary_no_digits():
    """Тест функции для выделения минимальной зарплаты, когда она не указана"""
    result = get_min_salary("Зарплата не указана")
    assert result == float("inf")


def test_get_min_salary_empty_string():
    """Тест функции для выделения минимальной зарплаты, когда строка пустая"""
    result = get_min_salary("")
    assert result == float("inf")
