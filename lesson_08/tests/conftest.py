import pytest
import uuid
from lesson_08.pages.auth_api import AuthApi
from lesson_08.pages.users_api import UsersApi
from lesson_08.pages.projects_api import ProjectsApi
from lesson_08.config import TEST_USER_EMAIL
from lesson_08.config import (
    TEST_USER_EMAIL,
    COMPANY_ID,
    PROJECT_CREATE_TITLE,
    PROJECT_UPDATE_TITLE
)


# для АПИ авторизации
@pytest.fixture(scope="session")
def auth_api():
    return AuthApi()


# для получения токена на сессию
@pytest.fixture(scope="session")
def token(auth_api):

    # 1. получить список ключей
    keys_resp = auth_api.get_api_keys()
    assert keys_resp.status_code == 200, f"Ошибка получения списка ключей: {keys_resp.text}"
    
    keys_data = keys_resp.json()
    
    # 2. Ищем ключи для нашей компании
    company_keys = []
    for key_info in keys_data:
        if key_info.get("companyId") == COMPANY_ID:
            company_keys.append(key_info)

    if company_keys:
        last_key = company_keys[-1]["key"]  # взять последний
        print(f"Используем существующий ключ: {last_key[:20]}...")
        return last_key
    else:
        # 3. если ключей нет - создать
        token_resp = auth_api.create_api_key()
        assert token_resp.status_code == 201, f"Ошибка создания ключа: {token_resp.text}"
        return token_resp.json()["key"]


# очищение всех ключей (кроме 2х последних)
@pytest.fixture(scope="session", autouse=True)
def cleanup_tokens(auth_api, token):
    yield  # выполняется после всех тестов

    # получить список всех ключей
    keys_resp = auth_api.get_api_keys()
    if keys_resp.status_code != 200:
        return
    
    keys_data = keys_resp.json()
    
    # фильтрация ключей по ID компании
    company_keys = []
    for key_info in keys_data:
        if key_info.get("companyId") == COMPANY_ID:
            company_keys.append(key_info)
    # удаление всех ключей кроме 2х
    if len(company_keys) > 2:
        keys_to_delete = company_keys[:-2]  # оставляем 2 последних

        for key_info in keys_to_delete:
            key_to_delete = key_info["key"]
            delete_resp = auth_api.delete_api_key(key_to_delete)
            if delete_resp.status_code not in (200, 404):
                # если не ок - поднимаем исключение
                raise Exception(
                    f"Ошибка при удалении ключа {key_to_delete[:20]}...: "
                    f"status_code={delete_resp.status_code}, "
                    f"response={delete_resp.text}")


# для АПИ пользователей
@pytest.fixture(scope="session")
def users_api(token):
    return UsersApi(token)

# для получения ID-пользователя
@pytest.fixture(scope="session")
def test_user_id(users_api):
    invite_resp = users_api.invite_user(TEST_USER_EMAIL)

    if invite_resp.status_code == 201:
        return invite_resp.json()["id"]
    elif invite_resp.status_code == 400:
        # Если уже существует, получаем его ID по имейл
        return users_api.get_user_id_by_email(TEST_USER_EMAIL)
    else:
        pytest.fail(f"Ошибка: {invite_resp.status_code}")

# для АПИ проектов
@pytest.fixture(scope="session")
def projects_api(token):
    return ProjectsApi(token)

@pytest.fixture
def created_project(projects_api, test_user_id, unique_project_data):
    users = {
        test_user_id: "worker"
    }
    project_title = unique_project_data["create_title"]
    
    # создание проекта
    create_resp = projects_api.create_project(
        title=project_title,
        users=users
    )
    assert create_resp.status_code == 201, f"Ошибка создания проекта: {create_resp.text}"
    project_id = create_resp.json()["id"]
    
    # возвращение данных тесту
    yield {
        "project_id": project_id,
        "users": users,
        "title": project_title  # title для использования в тестах
    }

    # пост-обработка
    delete_body = {
        "title": project_title,
        "deleted": True,
        "users": users
    }
    try:
        projects_api.update_project(project_id, delete_body)
    except Exception:
        pass

# для генерации уникальных данных
@pytest.fixture
def unique_project_data():
    unique_id = str(uuid.uuid4())[:8]  # берем первые 8 символов UUID
    return {
        "create_title": f"{PROJECT_CREATE_TITLE} {unique_id}",
        "update_title": f"{PROJECT_UPDATE_TITLE} {unique_id}"
    }

