
class SaveToJson:
    """Класс для сохранения информации о вакансиях в файл"""

    def __init__(self, keyword):
        self.keyword = keyword.title()

    def filename(self, suffix):
        return f"{self.keyword}_{suffix}.json"

    @staticmethod
    def save_vacancies(self, data, suffix=''):
        """Метод для записи информации о вакансиях в json файл"""
        pass

    @staticmethod
    def json_filtered_vacancies(self):
        pass

