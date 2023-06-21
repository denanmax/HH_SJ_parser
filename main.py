from utils.utils import hh_save_to_json, params_to_search, sj_save_to_json

def main():
    print("Парсер вакансий для Head Hunter и Superjob")
    print("Внимание! Для работы с HH.ru необходимо указать хотя-бы один параметр из трех!")

    check_input = input("Если хотите продолжить, нажмите д/н ")
    if check_input == "д".lower() or check_input == 'y'.lower():
        keyword, city, num_vacancies = params_to_search()
        hh_info = hh_save_to_json(keyword, city, num_vacancies)
        try:
            for i in hh_info:
                print(i)
        except TypeError:
            pass

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

