import json
import requests

from src.Vacancy import Vacancy
from src.abstract import AbstractVacancyAPI
from src.json_saver import SaveToJson


class HeadHunterAPI(AbstractVacancyAPI):
    """Класс запроса данных по API HH.ru"""
    def request_api(self, keyword):
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
            list_of_vacancies = self.request_api(keyword)
            print(f"С сайта HH.ru найдено: {len(list_of_vacancies)} вакансий\n")
            response.extend(list_of_vacancies)

        return response



class JSONSaverHH(SaveToJson):
    """Класс для сохранения информации о вакансиях в файл"""

    def json_filtered_vacancies(self):
        """Метод для чтения информации о вакансиях из json файла"""
        with open(self.filename(suffix='hh'), 'r', encoding='utf-8') as file:
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

        filtered_data = []
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

