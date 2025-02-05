# from src.head_hunter_api import HeadHunterAPI
# from src.json_saver import JSONSaver, type_of_salary
# from src.utils import type_of_description
# from src.vacancy import Vacancy
#
# hh_api = HeadHunterAPI()
#
# hh_vacancies = hh_api.get_vacancies("Python")
#
# json_saver = JSONSaver('data/vacancies.json')
# first = hh_vacancies[0]
# second = hh_vacancies[1]
# vac = Vacancy(vacancy_name=first["name"], vacancy_url=first['alternate_url'], salary=type_of_salary(first), description=type_of_description(first))
# vac2 = Vacancy(vacancy_name=second["name"], vacancy_url=second['alternate_url'], salary=type_of_salary(second), description=type_of_description(second))
# json_saver.add_vacancy(vac)
# json_saver.add_vacancy(vac2)
# for vacancy_data in hh_vacancies:
#     # print(vacancy_data)
#     print(vacancy_data["name"])
#     next_vacancy = Vacancy(vacancy_name=vacancy_data["name"], vacancy_url=vacancy_data['alternate_url'],
#                            salary=type_of_salary(vacancy_data), description=type_of_description(vacancy_data))
#     print(next_vacancy.vacancy_name)
#     json_saver.add_vacancy(next_vacancy)
#
# # for vacancy_data in hh_vacancies:
# #     print(vacancy_data)
# #     next_vacancy = Vacancy(
# #         vacancy_data['name'],
# #         vacancy_data['alternate_url'],
# #         type_of_salary(vacancy_data),
# #         type_of_description(vacancy_data)
# #     )
# #
# #     json_saver.add_vacancy(next_vacancy)
#
# #
# # # Преобразование набора данных из JSON в список объектов
# # vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
# #
# # # Пример работы конструктора класса с одной вакансией
# # vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
# # .add_vacancy(vacancy)
# #
# #
# # print(vacancy)
# # # Сохранение информации о вакансиях в файл
# # json_saver = JSONSaver()
# # json_saver.add_vacancy(vacancy)
# # json_saver.delete_vacancy(vacancy)
# #
# # # Функция для взаимодействия с пользователем
# # def user_interaction():
# #     platforms = ["HeadHunter"]
# #     search_query = input("Введите поисковый запрос: ")
# #     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
# #     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
# #     salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
# #
# #     filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
# #
# #     ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
# #
# #     sorted_vacancies = sort_vacancies(ranged_vacancies)
# #     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
# #     print_vacancies(top_vacancies)
# #
# #
# # if __name__ == "__main__":
# #     user_interaction()
