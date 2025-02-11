from src.head_hunter_api import HeadHunterAPI
from src.json_filter import JSONFilter
from src.json_saver import JSONSaver
from src.utils import dict_to_vac, vac_to_dict, is_valid_salary_range
from src.vacancy import Vacancy

hh_api = HeadHunterAPI()
json_saver = JSONSaver()


def user_interaction():
    print("Привет! Добро пожаловать в программу для выгрузки вакансий с Head Hunter.")
    search_query = input("Введите поисковый запрос: ")

    vacancies_list = hh_api.get_vacancies(search_query)
    if vacancies_list:
        for vac in vacancies_list:
            new_vac = dict_to_vac(vac)
            json_saver.add_vacancy(new_vac)

        json_filter = JSONFilter(json_saver.read_data())

        top = input("Введите количество вакансий для вывода в топ N: ")
        if top.isdigit():
            top = int(top)
        else:
            print("Вводимое значение должно быть числом. Будут выведены все вакансии из поиска")

        filter_words = input("Введите ключевые слова для фильтрации вакансий через пробел: ").split()
        while True:
            salary_range = input("Введите диапазон зарплат (Пример: 100000-150000): ")
            if is_valid_salary_range(salary_range):
                salary_range = salary_range.split("-")
                break
            else:
                print("Некорректный формат. Попробуйте снова.")

        filtered_vacancies = json_filter.filter_vacancies(filter_words)

        ranged_vacancies = json_filter.get_vacancies_by_salary(int(salary_range[0]), int(salary_range[1]))

        sorted_vacancies = json_filter.sort_vacancies()

        top_vacancies = json_filter.get_top_vacancies(top)

        print("Отфильтрованные вакансии:")
        print(str(json_filter))
    else:
        print("Вакансии по вашем запросу не найдены")


if __name__ == "__main__":
    user_interaction()
