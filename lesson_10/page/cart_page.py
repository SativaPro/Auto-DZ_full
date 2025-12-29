from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Page Object для страницы корзины покупок."""

    def __init__(self, driver):
        """
        Инициализирует экземпляр CartPage.
        Args: driver: WebDriver для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self):
        """Выполняет переход к оформлению заказа из корзины."""
        self.driver.find_element(By.ID, "checkout").click()

        self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
