from src.hh import HeadHunterAPI, JSONSaverHH
from src.sj import SuperJobAPI, JSONSaverSJ


def params_to_search():
    """Получаем входные данные"""
    keyword_to_search = input("Введите ключевое слово для поиска: ").title()
    while not keyword_to_search.isalpha():
        keyword_to_search = input('Ключевое слово должно состоять только из букв: ').title()

    city = input("Введите город: ").title()
    while not city.isalpha():
        city = input('Название города должно состоять только из букв: ').title()

    num_vacancies = input("Введите количество вакансий: ")
    while not num_vacancies.isdigit():
        num_vacancies = input('Количество вакансий должно быть числом: ')

    return keyword_to_search, city, num_vacancies


def hh_save_to_json(keyword, city, num_vacancies):
    """Получаем .json для HH.ru"""
    keyword_hh = f'{keyword} {city}'
    hh_api = HeadHunterAPI(keyword_hh, num_vacancies)
    hh_vacancies = hh_api.get_vacancies(keyword_hh, num_vacancies)
    save_to_json_hh = JSONSaverHH(keyword_hh)
    return save_to_json_hh.save_vacancies(hh_vacancies, suffix='HH')


def sj_save_to_json(keyword, city, num_vacancies):
    """Получаем .json для SJ.ru"""
    keyword_sj = keyword + ' ' + city
    sj_api = SuperJobAPI(keyword, num_vacancies)
    sj_vacancies = sj_api.get_vacancies(keyword_sj, num_vacancies)
    json_saver_spj = JSONSaverSJ(keyword_sj)
    return json_saver_spj.save_vacancies(sj_vacancies, suffix='SJ')


def sort_by_salary_max(data):
    """Функция для сортировки зарплат по максимальному порогу"""
    data = sorted(data, key=lambda x: (x.salary_from is not None, x.salary_from), reverse=True)
    return data
