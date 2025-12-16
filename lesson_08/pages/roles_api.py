import requests
from lesson_08.config import BASE_URL


class RolesApi:
    def __init__(self, token):
        self.base_url = BASE_URL
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    # Создать роль в проекте
    def create_role(self, project_id, body):
        return requests.post(
            f"{self.base_url}/projects/{project_id}/roles",
            headers=self.headers,
            json=body)

    # Получить список ролей проекта
    def get_roles(self, project_id):
        return requests.get(
            f"{self.base_url}/projects/{project_id}/roles",
            headers=self.headers)
