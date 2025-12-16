import json #Подкючаем встроенный модуль json для работы

company_json = """
{
    "id": 111,
    "isActive": true,
    "createDateTime": "2024-04-05T17:30:00.713Z",
    "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
    "name": "Барбершоп 'Цирюльникъ'",
    "description": "Крутые стрижки для крутых шишек"
    }
"""

company_list_json = """
[
    {
        "id": 111,
        "isActive": true,
        "createDateTime": "2022-12-23T14:43:26.713Z",
        "lastChangedDateTime": "2022-12-23T14:43:26.713Z",
        "name": "Барбершоп 'Цирюльникъ'",
        "description": "Крутые стрижки для крутых шишек"
    },
    {
        "id": 112,
        "isActive": true,
        "createDateTime": "2022-12-23T14:43:27.113Z",
        "lastChangedDateTime": "2022-12-23T14:43:27.113Z",
        "name": "Кондитерская Профи-тролли",
        "description": "Сладко и точка"
    },
    {
        "id": 114,
        "isActive": false,
        "createDateTime": "2022-12-23T14:43:27.213Z",
        "lastChangedDateTime": "2022-12-23T14:43:27.213Z",
        "name": "Муж на час",
        "description": "Ремонт вообще всего"
    },
    {
        "id": 113,
        "isActive": true,
        "createDateTime": "2022-12-23T14:43:27.213Z",
        "lastChangedDateTime": "2022-12-23T14:43:27.213Z",
        "name": "Клининг-центр 'Клинг-кинг'",
        "description": "Куда по помытому??"
    },
    {
        "id": 115,
        "isActive": true,
        "createDateTime": "2022-12-23T14:43:27.313Z",
        "lastChangedDateTime": "2022-12-23T14:43:27.313Z",
        "name": "Шиномонтаж на Ленинском",
        "description": "Пятое колесо - это хорошо"
    }
]
"""

def test_parse_json():
    company = json.loads(company_json)
    assert company["id"] == 111

def test_parse_array_json():
    company_list = json.loads(company_list_json)
    first_company = company_list[0]
    assert first_company["name"] == "Барбершоп 'Цирюльникъ'"

    assert company_list[1]["id"] == 112
