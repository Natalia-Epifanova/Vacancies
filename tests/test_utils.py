from src.utils import dict_to_vac, get_min_salary, type_of_description, type_of_salary, vac_to_dict


def test_vac_to_dict(first_vacancy):
    result = vac_to_dict(first_vacancy)
    assert result == {
        "name": "Python Developer",
        "alternate_url": "<https://hh.ru/vacancy/123456>",
        "salary": "100000 - 150000 руб.",
        "snippet": "Требования: опыт работы от 3 лет...",
    }


def test_dict_to_vac(vacancy_dict):
    result = dict_to_vac(vacancy_dict)
    assert result.vacancy_name == "Python Developer"
    assert result.vacancy_url == "<https://hh.ru/vacancy/123456>"
    assert result.salary == "100000 - 150000 руб."
    assert result.description == "Требования: опыт работы от 3 лет..."


def test_get_min_salary(salary_test):
    assert get_min_salary(salary_test) == 100000.0


def test_type_of_salary(vacancy_from_hh):
    result = type_of_salary(vacancy_from_hh)
    assert result == "350000 - 450000"


def test_type_of_description(vacancy_from_hh):
    result = type_of_description(vacancy_from_hh)
    assert (
        result == "Требования: Занимать активную жизненную позицию.... \n"
        "Обязанности: Оценивать вид из окна: встречать рассветы на кухне..."
    )


def test_type_of_salary_from(vacancy_half_of_params):
    result = type_of_salary(vacancy_half_of_params)
    assert result == "350000"


def test_type_of_description_requirement(vacancy_half_of_params):
    result = type_of_description(vacancy_half_of_params)
    assert result == "Требования: Занимать активную жизненную позицию...."


def test_type_of_salary_to(vacancy_half_of_params_2):
    result = type_of_salary(vacancy_half_of_params_2)
    assert result == "450000"


def test_type_of_description_responsibility(vacancy_half_of_params_2):
    result = type_of_description(vacancy_half_of_params_2)
    assert result == "Обязанности: Оценивать вид из окна: встречать рассветы на кухне..."


def test_get_min_salary_no_digits():
    result = get_min_salary("Зарплата не указана")
    assert result == float("inf")


def test_get_min_salary_empty_string():
    result = get_min_salary("")
    assert result == float("inf")
