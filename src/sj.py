import json

import requests

from src.Vacancy import Vacancy
from src.abstract import AbstractVacancyAPI
from src.json_saver import SaveToJson


class SuperJobAPI(AbstractVacancyAPI):
    """Класс запроса данных по API Super Job"""

    URL = "https://api.superjob.ru/2.0/vacancies/?"

    def __init__(self, keyword, num_vacancies):
        super().__init__(keyword, num_vacancies)

    def request_api(self, keyword, num_vacancies):
        """Метод запроса по API"""
        headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': "v3.r.128133351.1ee4ce9abaa8c792c86bfabef8bb09847f471b29.93066d454cf5352926f7ca0527e018ba62acb14e",
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        params = {
            'keyword': keyword.title(),
            'count': num_vacancies,
        }
        try:
            return requests.get(self.URL, headers=headers, params=params).json()['objects']
        except KeyError:
            raise print("Внимание! Для работы с HH.ru нужно ввести хотя-бы один параметр!")
        except ConnectionError:
            raise print("Нужен доступ в интернет")

    def get_vacancies(self, keyword, num_vacancies):
        """Метод поиска всех вакансий по заданным параметрам"""
        pages = 1
        response = []

        try:
            for page in range(pages):
                list_of_vacancies = self.request_api(keyword, num_vacancies)
                print(f"С сайта Super Job найдено: {len(list_of_vacancies)} вакансий\n")
                response.extend(list_of_vacancies)
                return response
        except TypeError:
            print(f"Произошла ошибка при получении вакансий c HH.ru. Нам очень жаль :(")
        except ConnectionError:
            print("Нужен доступ в интернет")
class JSONSaverSJ(SaveToJson):
    """Класс для сохранения информации о вакансиях в файл"""

    def json_filtered_vacancies(self):
        with open(self.filename(suffix='sj'), 'r', encoding='utf-8') as file:
            data = json.load(file)

        vacancies_sj = []
        filtered_data_sj = []
        for row in data:
            salary_from = None
            salary_to = None
            currency = None
            if row['payment_from']:
                salary_from = row['payment_from']
                salary_to = row['payment_to']
                currency = row['currency']
            vacancies_sj.append(Vacancy(row['firm_name'],
                                        salary_from,
                                        salary_to,
                                        currency,
                                        row['profession'], row['town']['title'],
                                        row['link']))

            for vacancy in vacancies_sj:
                filtered_data_sj.append({'Компания': vacancy.title,
                                         'Профессия': vacancy.employer,
                                         'От': vacancy.salary_from,
                                         'До': vacancy.salary_to,
                                         'Валюта': vacancy.currency,
                                         'Город': vacancy.city,
                                         'Ссылка': vacancy.link})

            with open(f"SJ_filtered.json", 'w', encoding='utf-8') as file:
                json.dump(filtered_data_sj, file, ensure_ascii=False, indent=4)

        return vacancies_sj

    def save_vacancies(self, data, suffix='sj'):
        """Метод для записи информации о вакансиях в json файл"""
        with open(self.filename(suffix), 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
