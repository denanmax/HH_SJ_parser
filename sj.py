import json

import requests

from Vacancy import Vacancy
from json_saver import SaveToJson


class SuperJobAPI:

    URL = "https://api.superjob.ru/2.0/vacancies/?"

    def __init__(self):
        self.list_of_vacancies = []

    def request_api(self, keyword):
        header = {
            'X-Api-App-Id':
                "v3.r.128133351.1ee4ce9abaa8c792c86bfabef8bb09847f471b29.93066d454cf5352926f7ca0527e018ba62acb14e"
        }

        params = {
            'test': keyword.title(),
            'count': 100,
        }

        return requests.get(self.URL, headers=header, params=params).json()['objects']

    def get_vacancies(self, keyword):
        pages = 1
        response = []

        for page in range(pages):
            list_of_vacancies = self.request_api(keyword)
            print(f"Вакансий найдено: {len(list_of_vacancies)}")
            response.extend(list_of_vacancies)

        return response


class JSONSaverSJ(SaveToJson):
    """Класс для сохранения информации о вакансиях в файл по определённым критериям"""
    def __init__(self, keyword):
        super().__init__(keyword)

    def json_read_sj(self):
        with open(self.filename(), 'r', encoding='utf-8') as file:
            data = json.load(file)

        vacancies = []
        for row in data:
            payment_from, payment_to, currency = None, None, None
            if row['payment_from']:
                salary_from = row['payment_from']
                salary_to = row['payment_to']
                currency = row['currency']
            vacancies.append(Vacancy(row['firm_name'],
                                     salary_from,
                                     salary_to,
                                     currency,
                                     row['profession'], row['town']['title'],
                                     row['link']))

        return vacancies


sj_keyword = 'морской'

spj_api = SuperJobAPI()

spj_vacancies = spj_api.get_vacancies(sj_keyword)

json_server_spj = JSONSaverSJ(sj_keyword)
json_server_spj.save_vacancies(spj_vacancies)
data_spj = json_server_spj.json_read_sj()
for row in data_spj:
    print(row)

