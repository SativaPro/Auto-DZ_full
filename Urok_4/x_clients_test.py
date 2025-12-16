from page.companyApi import CompanyApi

api = CompanyApi("http://5.101.50.27:8000")


# получение компаний 1
def test_get_active_companies1():
    # Получить список всех компаний
    full_list = api.get_company_list()
    # Получить список активных компаний
    filtered_list = api.get_company_list(params_to_add={'active': 'true'})

    # Проверить, что список 1 > списка 2
    assert len(full_list) > len(filtered_list)

# полный флоу
def test_add_new():
    # 1. получить количество компаний
    full_list = api.get_company_list()
    len_before = len(full_list)

    # 2. создать новую компанию
    name = "Autotest Sativa"
    descr = "Info QA"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # 2.1 обращаемся к компании
    new_company = api.get_company(new_id)

    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["is_active"] is True

    # 3. получить количество компнаний
    full_list = api.get_company_list()
    len_after = len(full_list)

    # 4. проверить что стало +1
    assert len_after - len_before == 1

    # 5. проверить название и описание последней компании
    assert full_list[-1]["name"] == name
    assert full_list[-1]["description"] == descr

    # 6. проверить, что ID последней компании = ответу из шага 2
    #assert full_list[-1]["id"] == new_id

    # 7. удалить добавленную компанию
    api.delete_company(new_id)

    # 8. Проверяем, что список компаний меньше на 1
    full_list = api.get_company_list()
    len_after = len(full_list)
    assert len_before - len_after == 0

    # 9. Проверяем, что удаленная компания не находится по id
    deleted = api.get_company(new_id)
    assert deleted['detail'] == 'Компания не найдена'


# Изменение данных компании
def test_edit():
    name = "Company to be edited"
    descr = "Edit me"
    result = api.create_company(name, descr)
    new_id = result["id"]

    new_name = "Updated"
    new_descr = "_upd_"

    edited = api.edit_company(new_id, new_name, new_descr)

    # Проверяем, что название компании поменялось
    assert edited["name"] == new_name
    # Проверяем, что описание компании поменялось
    assert edited["description"] == new_descr


# Деактивация компании
def test_deactivate():
    # Создаем компанию
    name = "Company to be deactivated"
    result = api.create_company(name)
    new_id = result["id"]
    # Деактивируем компанию
    body = api.set_active_state(new_id, False)
    # Проверяем, что у компании статус «неактивная»
    assert body["is_active"] is False

    # Активируем компанию с помощью параметра True
    body_a = api.set_active_state(new_id, True)
    # Проверяем, что компания активная
    assert body_a["is_active"] is True