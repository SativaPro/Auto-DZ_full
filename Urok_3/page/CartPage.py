from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, browser):
        self._driver = browser

    def get(self):
        # перехход на страницу корзины
        self._driver.get("https://www.labirint.ru/cart/")
    
    def get_counter(self):
        # проверить счетчик товаров (должет быть =числу нажатий)
        # 1. получить текущее значение
        txt = self._driver.find_element(By.ID, 'basket-default-prod-count2').text
        number_txt = txt.split()[0]  # приведение текста к числу для сравнения равенства
        # 2. сравнить с counter
        return int(number_txt)
