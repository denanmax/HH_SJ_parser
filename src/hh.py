import requests

from src.Vacancy import Vacancy
from src.abstract import AbstractVacancyAPI
from src.json_saver import SaveToJson


class HeadHunterAPI(AbstractVacancyAPI):
    """Класс запроса данных по API HH.ru"""
    def __init__(self, keyword, num_vacancies):
        super().__init__(keyword, num_vacancies)

    def request_api(self,  keyword, num_vacancies):
        """Метод запроса по API"""
        params = {
            "text": self.keyword,
            "per_page": self.num_vacancies
        }
        headers = {"HH-User-Agent": 'VacancyMachine/2.0'}

        try:
            return requests.get("https://api.hh.ru/vacancies", params=params, headers=headers).json()['items']

        except KeyError:
            pass
        except ConnectionError:
            raise print("Нужен доступ в интернет")

    def get_vacancies(self, keyword, num_vacancies):
        """Метод поиска всех вакансий по заданным параметрам"""
        pages = 1
        response = []

        try:
            for page in range(pages):
                list_of_vacancies = self.request_api(keyword, num_vacancies)
                print(f"С сайта HH.ru найдено: {len(list_of_vacancies)} вакансий\n")
                response.extend(list_of_vacancies)
                return response
        except TypeError:
            print(f"Произошла ошибка при получении вакансий c HH.ru. Нам очень жаль :(")
        except ConnectionError:
            print("Нужен доступ в интернет")


class JSONSaverHH(SaveToJson):
    """Класс для сохранения информации о вакансиях в файл"""
    def vacancy_list_to_print(self, data):
        """Метод для создания списка объектов из полученных данных для вывода на экран"""
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
