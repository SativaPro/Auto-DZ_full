from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


cookie = {
    "name": "cookie_policy",
    "value": "1"
}

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.maximize_window()


def open_labirint():
    # перейти на сайт Лабиринт
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(5)
    browser.add_cookie(cookie)

def search(term):
    # найти все книги по слову
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

#def switch_to_table():
    # переключиться на таблицу (ЯВНОЕ ОЖИДАНИЕ)
    #WebDriverWait(browser, 10).until(
        #EC.presence_of_element_located( (By.CSS_SELECTOR, "table")))

def add_books():
    # добавить все книги в корзину и посчитать кол-во
    cart_button = browser.find_elements(
        By.CSS_SELECTOR, "[data-carttext]")
    
    counter = 0
    for cart in cart_button:
        cart.click()
        counter += 1
    return counter

def go_to_cart():
    # перейти в корзину
    browser.get("https://www.labirint.ru/cart/")

def get_cart_counter():
    # проверить счетчик товаров (должет быть =числу нажатий)
    # 1. получить текущее значение
    txt = browser.find_element(By.ID, 'basket-default-prod-count2').text

    # 2. сравнить с counter
    return int(txt.split()[0]) # приведение текста к числу для сравнения равенства

def close_driver():
    # закрытие браузера
    browser.quit()



def test_cart_counter():
    open_labirint()
    search('python')
    add = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    close_driver
    assert add == cart_counter


def test_empty_search_result():
    open_labirint()
    search('python')
    txt = browser.find_element(By.CSS_SELECTOR, ".b-rfooter-info-e-text").text.strip()
    close_driver()

    assert txt.split("?")[0].strip() == \
        "Пока не нашли для себя ничего в Лабиринте"

# python -m pytest Urok_3/labirint_method_test.py -v -s