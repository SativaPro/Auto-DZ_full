from lesson_08.pages.auth_api import AuthApi
from lesson_08.pages.users_api import UsersApi
from lesson_08.pages.projects_api import ProjectsApi
from lesson_08.config import TEST_USER_EMAIL


def get_token():

    auth = AuthApi()
    resp = auth.create_api_key()

    assert resp.status_code == 201
    return resp.json()["key"]


# создание проекта без обязательного поля title
def test_create_project_without_title():

    token = get_token()
    projects_api = ProjectsApi(token)
    body = {
        "users": {}   # "title" отсутствует намеренно
        }
    resp = projects_api.create_project(
        title=None,
        users={})

    # ОР ошибка валидации
    assert resp.status_code in (400, 422)
    assert "error" in resp.json()


# запрос проекта с несуществующим ID
def test_get_project_with_wrong_id():

    token = get_token()
    projects_api = ProjectsApi(token)
    wrong_id = "00000000-0000-0000-0000-000000000000"
    resp = projects_api.get_project(wrong_id)

    # ОР ошибка валидации
    assert resp.status_code in (400, 404)
    assert "error" in resp.json()


# попытка обновить проект пустым body
def test_update_project_with_empty_body():

    token = get_token()
    projects_api = ProjectsApi(token)
    wrong_id = "00000000-0000-0000-0000-000000000000"
    resp = projects_api.update_project(
        project_id=wrong_id,
        body={})

    assert resp.status_code in (400, 404)
    assert "error" in resp.json()


# Попытка пригласить пользователя, который уже существует
def test_invite_existing_user():

    token = get_token()
    users_api = UsersApi(token)

    # первый раз создаём пользователя (чтобы он точно был)
    users_api.invite_user(TEST_USER_EMAIL)

    # второй раз пробуем пригласить того же пользователя
    resp = users_api.invite_user(TEST_USER_EMAIL)

    assert resp.status_code == 400
    assert "error" in resp.json() or "message" in resp.json()

# python -m pytest lesson_08/tests/projects_negative_test.py -v -s
