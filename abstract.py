from abc import ABC, abstractmethod


class AbstractVacancyAPI(ABC):
    @abstractmethod
    def request_hh_api(self, keyword):
        pass
