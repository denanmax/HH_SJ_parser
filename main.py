from src.hh import HeadHunterAPI, JSONSaverHH
from src.sj import SuperJobAPI, JSONSaverSJ


def main():
    keyword = input("Введите ключевое слово для поиска на HH.ru: ")
    hh_api = HeadHunterAPI()

    hh_vacancies = hh_api.get_vacancies(keyword)

    save_to_json_hh = JSONSaverHH(keyword)
    save_to_json_hh.save_vacancies(hh_vacancies)

    hh_info = save_to_json_hh.json_filtered_vacancies()

    for i in hh_info:
        print(i)

    user_input = input(f"Хотите продолжить поиск на сайте Super Job? Нажмите д/н ")
    if user_input == "д".lower() or user_input == 'y'.lower():
        sj_api = SuperJobAPI()

        sj_vacancies = sj_api.get_vacancies(keyword)

        json_server_spj = JSONSaverSJ(keyword)
        json_server_spj.save_vacancies(sj_vacancies)
        info_sj = json_server_spj.json_filtered_vacancies()
        for row in info_sj:
            print(row)
    else:
        print('Ладно, до свидания!')


if __name__ == "__main__":
    main()

