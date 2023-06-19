from abc import ABC, abstractmethod


class AbstractVacancyAPI(ABC):
    @abstractmethod
    def request_api(self, keyword):
        pass
    @abstractmethod
    def get_vacancies(self, keyword):
        pass
