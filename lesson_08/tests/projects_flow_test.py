from lesson_08.pages.auth_api import AuthApi
from lesson_08.pages.users_api import UsersApi
from lesson_08.pages.projects_api import ProjectsApi
from lesson_08.config import TEST_USER_EMAIL


def test_projects_full_flow():
    # 1. ПОЛУЧЕНИЕ ТОКЕНА
    auth = AuthApi()
    token_resp = auth.create_api_key()

    assert token_resp.status_code == 201
    token = token_resp.json()["key"]

    # 2. ПРИГЛАШЕНИЕ СОТРУДНИКА
    users_api = UsersApi(token)
    invite_resp = users_api.invite_user(TEST_USER_EMAIL)

    assert invite_resp.status_code in (201, 400)
    if invite_resp.status_code == 201:
        user_id = invite_resp.json()["id"]
    else:
        # если пользователь уже существует > тест идёт дальше
        user_id = users_api.get_user_id_by_email(TEST_USER_EMAIL)

    # 3. СОЗДАНИЕ ПРОЕКТА
    projects_api = ProjectsApi(token)
    users = {
        user_id: "worker"
    }
    create_resp = projects_api.create_project(
        title="Autotest Project",
        users=users)

    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]

    # 4. ПОЛУЧЕНИЕ ПРОЕКТА
    get_resp = projects_api.get_project(project_id)

    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == "Autotest Project"

    # 5. ИЗМЕНЕНИЕ ПРОЕКТА
    update_body = {
        "title": "Updated Project",
        "deleted": False,
        "users": users
    }
    update_resp = projects_api.update_project(project_id, update_body)

    assert update_resp.status_code == 200

    # проверка контракта ответа
    assert update_resp.json()["id"] == project_id

    # проверка, что данные обновились
    get_after_update = projects_api.get_project(project_id)

    assert get_after_update.status_code == 200
    assert get_after_update.json()["title"] == "Updated Project"

    # 6. УДАЛЕНИЕ ПРОЕКТА (soft delete)
    delete_body = {
        "title": "Updated Project",
        "deleted": True,
        "users": users
    }
    delete_resp = projects_api.update_project(project_id, delete_body)

    assert delete_resp.status_code == 200

    # проверка контракта ответа
    assert delete_resp.json()["id"] == project_id

    # провка, что проект помечен как удалённый
    get_after_delete = projects_api.get_project(project_id)
    assert get_after_delete.status_code == 200
    assert get_after_delete.json().get("deleted") is True

# python -m pytest lesson_08/tests/projects_flow_test.py -v -s
