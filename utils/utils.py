from src.hh import HeadHunterAPI, JSONSaverHH
from src.sj import SuperJobAPI, JSONSaverSJ


def params_to_search():
    keyword_to_search = input("Введите ключевое слово для поиска: ").title()
    city = input("Введите город: ").title()
    num_vacancies = input("Введите количество вакансий: ")
    return keyword_to_search, city, num_vacancies


def hh_save_to_json(keyword, city, num_vacancies):
    keyword_hh = f'{keyword} {city}'
    hh_api = HeadHunterAPI(keyword_hh, num_vacancies)
    hh_vacancies = hh_api.get_vacancies(keyword_hh, num_vacancies)
    save_to_json_hh = JSONSaverHH(keyword_hh)
    save_to_json_hh.save_vacancies(hh_vacancies, suffix='HH')
    return save_to_json_hh.save_vacancies(hh_vacancies, suffix='HH')


def sj_save_to_json(keyword, city, num_vacancies):
    keyword_sj = keyword + ' ' + city
    sj_api = SuperJobAPI(keyword, num_vacancies)
    sj_vacancies = sj_api.get_vacancies(keyword_sj, num_vacancies)
    json_saver_spj = JSONSaverSJ(keyword_sj)
    json_saver_spj.save_vacancies(sj_vacancies, suffix='SJ')
    return json_saver_spj.save_vacancies(sj_vacancies, suffix='SJ')