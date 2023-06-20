import json
import requests

from Vacancy import Vacancy
from abstract import AbstractVacancyAPI
from json_saver import SaveToJson


class HeadHunterAPI(AbstractVacancyAPI):
    """Класс запроса данных по API HH.ru"""
    def request_api(self, keyword):
        """Метод запроса по API"""
        params = {
            "text": keyword,
            "per_page": 10,
        }
        headers = {"HH-User-Agent": 'VacancyMachine/1.0 (deshis93@gmail.com)'}

        return requests.get("https://api.hh.ru/vacancies", params=params, headers=headers).json()['items']

    def get_vacancies(self, keyword):
        """Метод поиска всех вакансий по заданным параметрам"""
        pages = 1
        response = []

        for page in range(pages):
            list_of_vacancies = self.request_api(keyword)
            print(f"Вакансий найдено: {len(list_of_vacancies)}")
            response.extend(list_of_vacancies)

        return response



class JSONSaverHH(SaveToJson):
    """Класс для сохранения информации о вакансиях в файл"""

    def json_read(self):
        """Метод для чтения информации о вакансиях из json файла"""
        with open(self.filename(suffix='hh'), 'r', encoding='utf-8') as file:
            data = json.load(file)

        vacancies = []
        filtered_data = []
        for row in data:
            salary_min = None
            salary_max = None
            currency = None
            if row['salary']:
                salary_min = row['salary']['from']
                salary_max = row['salary']['to']
                currency = row['salary']['currency']
            vacancies.append(Vacancy(row['name'],
                                     salary_min,
                                     salary_max,
                                     currency,
                                     row['employer']['name'],
                                     row['area']['name'],
                                     row['alternate_url']))

        for vacancy in vacancies:
            filtered_data.append({'Компания': vacancy.employer,
                                  'Профессия': vacancy.title,
                                  'От': vacancy.salary_from,
                                  'До': vacancy.salary_to,
                                  'Валюта': vacancy.currency,
                                  'Город': vacancy.city,
                                  'Ссылка': vacancy.link})

        with open(f"HH_filtered.json", 'w', encoding='utf-8') as file:
            json.dump(filtered_data, file, ensure_ascii=False, indent=4)

        return vacancies

    def save_vacancies(self, data, suffix='hh'):
        """Метод для записи информации о вакансиях в json файл"""
        with open(self.filename(suffix), 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


hh_keyword = 'химик'
hh_api = HeadHunterAPI()

hh_vacancies = hh_api.get_vacancies(hh_keyword)

json_sever_hh = JSONSaverHH(hh_keyword)
json_sever_hh.save_vacancies(hh_vacancies)
data_hh = json_sever_hh.json_read()

for i in data_hh:
    print(i)

