from src.head_hunter_api import HeadHunterAPI
from src.json_filter import JSONFilter
from src.json_saver import JSONSaver
from src.utils import dict_to_vac, vac_to_dict
from src.vacancy import Vacancy

hh_api = HeadHunterAPI()
json_saver = JSONSaver()


def user_interaction():
    print("Привет! Добро пожаловать в программу для выгрузки вакансий с Head Hunter.")
    search_query = input("Введите поисковый запрос: ")

    vacancies_list = hh_api.get_vacancies(search_query)

    for vac in vacancies_list:
        new_vac = dict_to_vac(vac)
        json_saver.add_vacancy(new_vac)

    json_filter = JSONFilter(json_saver.read_data())

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий через пробел: ").split()
    salary_range = input("Введите диапазон зарплат (Пример: 100000 - 150000): ").split(" - ")

    filtered_vacancies = json_filter.filter_vacancies(filter_words)

    ranged_vacancies = json_filter.get_vacancies_by_salary(int(salary_range[0]), int(salary_range[1]))

    sorted_vacancies = json_filter.sort_vacancies()

    top_vacancies = json_filter.get_top_vacancies(top_n)

    print("Отфильтрованные вакансии:")
    print(str(json_filter))


if __name__ == "__main__":
    user_interaction()