import requests

def test_simpe_req():
    resp = requests.get('http://5.101.50.27:8000/company/list')

    response_body = resp.json()
    first_company = response_body[0]

    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"
    assert first_company["name"] == "QA Студия 'ТестировщикЪ'"

#r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))

base_url = "http://5.101.50.27:8000"

# получение компаний
def test_simple_req():
    resp = requests.get(base_url + '/company/list')
    response_body = resp.json()
    first_company = response_body[0]
    assert first_company["name"] == "QA Студия 'ТестировщикЪ'"
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"
    assert len(response_body) > 0

# получение компаний 1
def test_get_active_company1():
    # Получить список всех компаний
    resp = requests.get(base_url+'/company/list')
    full_list = resp.json()

    # Получить список активных компаний
    my_params = {
        'active': 'true'
    }
    resp = requests.get(base_url+'/company/list', params=my_params)
    filtered_list = resp.json()

    # Проверить, что список 1 > списка 2
    assert len(full_list) > len(filtered_list)

# получение компаний 2
def test_get_active_company2():
    # Получить список всех компаний
    resp = requests.get(base_url+'/company/list')
    full_list = resp.json()

    # Получить список активных компаний
    resp = requests.get(base_url+'/company/list?active=true')
    filtered_list = resp.json()

    # Проверить, что список 1 > списка 2
    assert len(full_list) > len(filtered_list)


# авторизация
def test_auth():
    creds = {
        'username': 'harrypotter',  # для передачи словаря обязательны одинарные ковычки
        'password': 'expelliarmus'
    }
    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()["user_token"]
    assert resp.status_code == 200
    assert token is not None

# создание компании
def test_create_company():
    company = {
        "name": "python",
        "description": "request"
    }
    resp = requests.post(base_url + '/company/create', json=company)
    #id_company = 
    assert resp.status_code == 201

