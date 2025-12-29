from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Page Object для страницы оформления заказа."""

    def __init__(self, driver):
        """
        Инициализирует экземпляр CheckoutPage.
        Args: driver: WebDriver для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name, last_name, postal_code):
        """
        Заполняет форму оформления заказа данными пользователя.
        Args:
            first_name (str): Имя покупателя
            last_name (str): Фамилия покупателя
            postal_code (str): Почтовый индекс доставки
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total_amount(self) -> str:
        """
        Получает итоговую сумму заказа из сводки.
        Returns: str: Итоговая сумма заказа в строковом формате (без валюты)
        """
        total = self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return total.text.replace("Total: $", "").strip()
