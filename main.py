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
    save_to_json_hh.save_vacancies(hh_vacancies)
    return save_to_json_hh.json_filtered_vacancies()


def sj_save_to_json(keyword, city, num_vacancies):
    keyword_sj = keyword + ' ' + city
    sj_api = SuperJobAPI(keyword, num_vacancies)
    sj_vacancies = sj_api.get_vacancies(keyword_sj, num_vacancies)
    json_server_spj = JSONSaverSJ(keyword_sj)
    json_server_spj.save_vacancies(sj_vacancies)
    return json_server_spj.json_filtered_vacancies()


def main():
    print("Парсер вакансий для Head Hunter и Superjob")
    print("Внимание! Для работы с HH.ru необходимо указать хотя-бы один параметр из трех!")

    check_input = input("Если хотите продолжить, нажмите д/н ")
    if check_input == "д".lower() or check_input == 'y'.lower():
        keyword, city, num_vacancies = params_to_search()
        hh_info = hh_save_to_json(keyword, city, num_vacancies)
        for i in hh_info:
            print(i)

    user_input = input(f"Хотите продолжить поиск на сайте Super Job? Нажмите д/н ")
    if user_input == "д".lower() or user_input == 'y'.lower():
        keyword, city, num_vacancies = params_to_search()
        info_sj = sj_save_to_json(keyword, city, num_vacancies)
        for row in info_sj:
            print(row)
    else:
        print('Ладно, до свидания!')


if __name__ == "__main__":
    main()

