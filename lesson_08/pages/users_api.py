import requests
from lesson_08.config import BASE_URL


class UsersApi:
    def __init__(self, token):
        self.base_url = BASE_URL
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    # Пригласить сотрудника
    def invite_user(self, email, is_admin=False):
        body = {
            "email": email,
            "isAdmin": is_admin
        }
        return requests.post(
            f"{self.base_url}/users",
            headers=self.headers,
            json=body)

    # Получить сотрудника по ID
    def get_user(self, user_id):
        return requests.get(
            f"{self.base_url}/users/{user_id}",
            headers=self.headers)

    # Удалить сотрудника
    def delete_user(self, user_id):
        return requests.delete(
            f"{self.base_url}/users/{user_id}",
            headers=self.headers)

    # Найти ID пользователя по email
    def get_user_id_by_email(self, email):
        resp = requests.get(
            f"{self.base_url}/users",
            headers=self.headers)
        if resp.status_code != 200:
            raise Exception(
                f"Ошибка получения users: {resp.status_code} {resp.text}")
        users = resp.json().get("content", [])
        for user in users:
            if user.get("email") == email:
                return user["id"]
        raise Exception(f"Пользователь с email {email} не найден")
