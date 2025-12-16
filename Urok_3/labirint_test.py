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

def test_cart_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    # перейти на сайт Лабиринт
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(5)
    browser.add_cookie(cookie)

    # найти все книги по слову python
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys('python')
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    # переключиться на таблицу (ЯВНОЕ ОЖИДАНИЕ)
    #WebDriverWait(browser, 10).until(
        #EC.presence_of_element_located( (By.CSS_SELECTOR, "table")))


    # добавить все книги в корзину и посчитать кол-во
    card_button = browser.find_elements(
        By.CSS_SELECTOR, "[data-carttext]")
    print(len(card_button))
    
    counter = 0
    for card in card_button:
        card.click()
        counter += 1
    print(counter)

    # перейти в корзину
    browser.get("https://www.labirint.ru/cart/")

    # проверить счетчик товаров (должет быть =числу нажатий)
    # 1. получить текущее значение
    txt = browser.find_element(By.ID, 'basket-default-prod-count2').text

    # 2. сравнить с counter
    assert counter == int(txt.split()[0]) # приведение текста к числу для сравнения равенства


    sleep(5)
    browser.quit()

# python -m pytest Urok_3/labirint_test.py -v -s