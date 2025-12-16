from selenium.webdriver.common.by import By

class ResultPage:

    def __init__(self, browser):
        self._driver = browser

    
    def add_books(self):
        # добавить все книги в корзину и посчитать кол-во
        cart_button = self._driver.find_elements(
            By.CSS_SELECTOR, "[data-carttext]")
    
        counter = 0
        for cart in cart_button:
            cart.click()
            counter += 1
        return counter
    
    def get_empty_result_message(self):
        element = self._driver.find_element(
          By.CSS_SELECTOR, ".b-rfooter-info-e-text"
        )
        full_text = element.text.strip()
        first_part = full_text.split("?")[0].strip()  # для получения только первой строчки
        return f"{first_part}?"