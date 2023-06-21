import json
from src.Vacancy import Vacancy


class SaveToJson:
    """Класс для сохранения информации о вакансиях в файл"""

    def __init__(self, keyword):
        self.keyword = keyword.title()

    def filename(self, suffix):
        return f"{self.keyword}_{suffix}.json"

    def save_vacancies(self, data, suffix):
        """Метод для записи информации о вакансиях в json файл"""
        try:
            vacancies = self.vacancy_list_to_print(data)
        except:
            pass

        filtered_data = []

        try:
            for vacancy in vacancies:
                filtered_data.append({'Компания': vacancy.employer,
                                      'Профессия': vacancy.title,
                                      'От': vacancy.salary_from,
                                      'До': vacancy.salary_to,
                                      'Валюта': vacancy.currency,
                                      'Город': vacancy.city,
                                      'Ссылка': vacancy.link})

            with open(f"FILTERED_{self.filename(suffix).upper()}", 'w',
                      encoding='utf-8') as file:  # тут сохраняем отфильтрованный json
                json.dump(filtered_data, file, ensure_ascii=False, indent=4)

            return vacancies
        except UnboundLocalError:
            pass

        except TypeError:
            pass

    @staticmethod
    def vacancy_list_to_print(self):
        pass
