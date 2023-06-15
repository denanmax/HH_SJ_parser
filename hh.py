import json
import requests

from abstract import AbstractVacancyAPI
from json_saver import SaveToJson


class HeadHunterAPI(AbstractVacancyAPI):
    """Класс запроса данных по API HH.ru"""
    def request_hh_api(self, keyword):
        """Метод запроса по API"""
        params = {
            "text": keyword,
            "per_page": 100,
        }
        headers = {"HH-User-Agent": 'VacancyMachine/1.0 (deshis93@gmail.com)'}

        return requests.get("https://api.hh.ru/vacancies", params=params, headers=headers).json()['items']

    def get_vacancies(self, keyword):
        """Метод поиска всех вакансий по заданным параметрам"""
        pages = 1
        response = []

        for page in range(pages):
            list_of_vacancies = self.request_hh_api(keyword)
            print(f"Вакансий найдено: {len(list_of_vacancies)}")
            response.extend(list_of_vacancies)

        return response


class Vacancy:
    """Класс для формирования критериев отбора вакансий"""

    def __init__(self, title, salary_from, salary_to, currency, employer, city, link):
        self.title = title
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.employer = employer
        self.city = city
        self.link = link

    def __str__(self):
        salary_from = f'От {self.salary_from}' if self.salary_from else ''
        salary_to = f'До {self.salary_to}' if self.salary_to else ''
        currency = self.currency if self.currency else ''
        if self.salary_from is None and self.salary_to is None:
            salary_from = "Заработная плата не указана"
        return f"{self.employer}: {self.title}\n" \
               f"{salary_from} {salary_to}{currency}\n" \
               f"Город: {self.city}\n" \
               f"Cсылка на вакансию: {self.link}"


class JSONSaverHH(SaveToJson):
    """Класс для сохранения информации о вакансиях в файл по определённым критериям"""

    def select(self):
        """Метод для чтения информации о вакансиях из json файла"""
        with open(self.filename(), 'r', encoding='utf-8') as file:
            data = json.load(file)

        vacancies = []
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
        return vacancies


hh_keyword = input('Введите слово для поиска: ')

hh_api = HeadHunterAPI()

hh_vacancies = hh_api.get_vacancies(hh_keyword)

json_sever_hh = JSONSaverHH(hh_keyword)
json_sever_hh.add_vacancies(hh_vacancies)
data_hh = json_sever_hh.select()

for i in data_hh:
    print(i)
