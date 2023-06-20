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
        currency = f"Валюта: {self.currency}" if self.currency else ''
        if self.salary_from is None and self.salary_to is None:
            salary_from = "Заработная плата не указана"
        return f"{self.employer}: {self.title}\n" \
               f"{salary_from} {salary_to} {currency}\n" \
               f"Город: {self.city}\n" \
               f"Cсылка на вакансию: {self.link}\n"

    def __gt__(self, other):
        return int(self.salary_from) > int(other.salary_from)

    def __ge__(self, other):
        return int(self.salary_from) >= int(other.salary_from)

    def __lt__(self, other):
        return int(self.salary_from) < int(other.salary_from)

    def __le__(self, other):
        return int(self.salary_from) <= int(other.salary_from)

    def __eq__(self, other):
        return int(self.salary_from) == int(other.salary_from)
