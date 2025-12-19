import requests
from lesson_08.config import BASE_URL


class ProjectsApi:
    def __init__(self, token):
        self.base_url = BASE_URL
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    # Создать проект
    def create_project(self, title, users):
        body = {
            "title": title,
            "users": users
        }
        return requests.post(
            f"{self.base_url}/projects",
            headers=self.headers,
            json=body)

    # Получить проект по ID
    def get_project(self, project_id):
        return requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers)

    # Изменить проект
    def update_project(self, project_id, body):
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
            json=body)
