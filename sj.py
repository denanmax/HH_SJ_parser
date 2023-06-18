import requests


class SuperJobAPI:
    URL = "https://api.superjob.ru/2.0/vacancies/?"

    def __init__(self):
        self.list_of_vacancies = []

    def request_js_api(self, keyword):
        header = {
            'X-Api-App-Id':
                "v3.r.128133351.1ee4ce9abaa8c792c86bfabef8bb09847f471b29.93066d454cf5352926f7ca0527e018ba62acb14e"
        }

        params = {
            'test': keyword.title(),
            'count': 100,
        }

        return requests.get(self.URL, headers=header, params=params).json()['objects']

    def get_vacancies(self, keyword):
        pages = 1
        response = []

        for page in range(pages):
            list_of_vacancies = self.request_js_api(keyword)
            print(f"Вакансий найдено: {len(list_of_vacancies)}")
            response.extend(list_of_vacancies)

        return response


kw = "морской"
sj_api = SuperJobAPI()

sj_vac = sj_api.get_vacancies(kw)
print(sj_vac)


