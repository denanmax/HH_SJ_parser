from abc import ABC, abstractmethod


class AbstractVacancyAPI(ABC):
    def __init__(self, keyword, num_vacancies):
        self.keyword = keyword
        self.num_vacancies = num_vacancies

    @abstractmethod
    def request_api(self,  keyword, num_vacancies):
        pass

    @abstractmethod
    def get_vacancies(self, keyword, num_vacancies):
        pass
