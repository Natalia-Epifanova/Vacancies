from src.json_filter import JSONFilter


def test_json_filter_init(vacancies_for_filter):
    json_filter_test = JSONFilter(vacancies_for_filter)
    assert len(json_filter_test.vacancies_list) == 3


def test_filter_vacancies(vacancies_for_filter):
    json_filter_test = JSONFilter(vacancies_for_filter)
    json_filter_test.filter_vacancies(["HTML", "CSS"])
    assert str(json_filter_test) == (
        "Вакансия номер 1: Название: Junior Developer (стажер), "
        "Ссылка: https://hh.ru/vacancy/116792570, Зарплата: 70000, "
        "Описание: Требования: Базовые знания фронтенд-технологий: HTML, CSS, JavaScript. "
        "Обязанности: Участие в разработке программного обеспечения "
    )


def test_get_vacancies_by_salary(vacancies_for_filter):
    json_filter_test = JSONFilter(vacancies_for_filter)
    json_filter_test.get_vacancies_by_salary(190000.0, 210000.0)
    assert str(json_filter_test) == (
        "Вакансия номер 1: Название: QA инженер/Тестировщик, "
        "Ссылка: https://hh.ru/vacancy/116907826, Зарплата: 200000, "
        "Описание: Требования: Стаж написания автоматических тестов от 1 года ..."
    )


def test_sort_vacancies(vacancies_for_filter, sorted_vacancies):
    json_filter_test = JSONFilter(vacancies_for_filter)
    json_filter_test.sort_vacancies()
    assert str(json_filter_test) == sorted_vacancies


def test_get_top_vacancies(vacancies_for_filter):
    json_filter_test = JSONFilter(vacancies_for_filter)
    json_filter_test.sort_vacancies()
    json_filter_test.get_top_vacancies(1)
    assert str(json_filter_test) == (
        "Вакансия номер 1: Название: QA инженер/Тестировщик, "
        "Ссылка: https://hh.ru/vacancy/116907826, Зарплата: 200000, "
        "Описание: Требования: Стаж написания автоматических тестов от 1 года ..."
    )
