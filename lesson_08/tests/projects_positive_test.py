# успешное создание проекта через API
def test_create_project(projects_api, test_user_id, unique_project_data):
    project_title = unique_project_data["create_title"]
    users = {
        test_user_id: "worker"
    }
    # 1. создаем проект
    create_resp = projects_api.create_project(
        title=project_title,
        users=users)

    assert create_resp.status_code == 201, f"Ошибка создания проекта: {create_resp.text}"

    response_data = create_resp.json()

    # 2. проверяем что в ответе есть ID проекта
    assert "id" in response_data, "Ответ не содержит ID проекта"
    project_id = response_data["id"]

    # 3. Проверяем, что проект действительно создан (получаем его по ID)
    get_resp = projects_api.get_project(project_id)
    assert get_resp.status_code == 200, f"Проект не найден по ID после создания: {get_resp.text}"

    # 4. Теперь проверяем данные проекта (в ответе от get_project есть title)
    project_data = get_resp.json()
    
    # Проверяем название проекта - должно быть то, которое мы отправили
    assert project_data["title"] == project_title, f"Название проекта не совпадает. Ожидалось: {project_title}, Получено: {project_data.get('title')}"
    
    # Проверка пользователей в проекте
    assert "users" in project_data, "Ответ не содержит информации о пользователях"
    assert str(test_user_id) in project_data["users"], f"Тестовый пользователь не добавлен в проект. Пользователи: {project_data['users']}"

# получение данных проекта по ID
def test_get_project(created_project, projects_api):
    project_id = created_project["project_id"]
    expected_title = created_project["title"]  # title из фикстуры
    
    get_resp = projects_api.get_project(project_id)
    
    assert get_resp.status_code == 200, f"Ошибка получения проекта: {get_resp.text}"
    assert get_resp.json()["id"] == project_id, "ID не совпадает"
    assert get_resp.json()["title"] == expected_title, "Название проекта не совпадает"

# обновление данных проекта
def test_update_project(created_project, projects_api, unique_project_data):
    project_id = created_project["project_id"]
    users = created_project["users"]

    # используется уникальное название для обновления
    updated_title = unique_project_data["update_title"]
    update_body = {
        "title": updated_title,
        "deleted": False,
        "users": users
    }
    update_resp = projects_api.update_project(project_id, update_body)

    assert update_resp.status_code == 200, f"Ошибка: {update_resp.text}"
    assert update_resp.json()["id"] == project_id, "ID проекта в ответе не совпадает"
    
    # проверка обновленных данных
    get_after_update = projects_api.get_project(project_id)
    assert get_after_update.status_code == 200
    assert get_after_update.json()["title"] == updated_title, "Название не обновилось"

# удаление проекта
def test_soft_delete_project(created_project, projects_api):
    project_id = created_project["project_id"]
    users = created_project["users"]
    original_title = created_project["title"]
    delete_body = {
        "title": original_title,
        "deleted": True,
        "users": users
    }
    delete_resp = projects_api.update_project(project_id, delete_body)
    
    assert delete_resp.status_code == 200, f"Ошибка при удалении проекта: {delete_resp.text}"
    assert delete_resp.json()["id"] == project_id, "ID проекта не совпадает"
    
    # проверка, что проект помечен как удаленный
    get_after_delete = projects_api.get_project(project_id)
    assert get_after_delete.status_code == 200
    assert get_after_delete.json().get("deleted") is True, "Проект не помечен как удаленный"


# python -m pytest lesson_08/tests/projects_positive_test.py -v -s