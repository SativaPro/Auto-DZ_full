import requests
from lesson_08.config import BASE_URL, LOGIN, PASSWORD, COMPANY_ID


class AuthApi:
    def __init__(self):
        self.base_url = BASE_URL

    # Получить список компаний пользователя
    def get_companies(self):
        body = {
            "login": LOGIN,
            "password": PASSWORD
        }
        return requests.post(
            f"{self.base_url}/auth/companies",
            json=body)

    # создать API-key для компании
    def create_api_key(self):
        body = {
            "login": LOGIN,
            "password": PASSWORD,
            "companyId": COMPANY_ID
        }
        resp = requests.post(
            f"{self.base_url}/auth/keys",
            json=body)
        return resp

    # получить список всех ключей
    def get_api_keys(self):
        body = {
            "login": LOGIN,
            "password": PASSWORD,
            "companyId": COMPANY_ID
        }
        return requests.post(
            f"{self.base_url}/auth/keys/get",
            json=body)

    # удалить ключ по его значению
    def delete_api_key(self, key):
        return requests.delete(
            f"{self.base_url}/auth/keys/{key}",
            headers={"Content-Type": "application/json"})
