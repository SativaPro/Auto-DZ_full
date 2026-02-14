from selenium.webdriver.common.by import By


class InventoryPage:
    """Page Object для страницы каталога товаров."""

    def __init__(self, driver):
        """
        Инициализирует экземпляр InventoryPage.
        Args: driver: WebDriver для управления браузером
        """
        self.driver = driver

    def add_products_to_cart(self, product_names: list):
        """ Добавляет товары в корзину по их названиям. """
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")

        for product in products:
            name = product.find_element(
                By.CLASS_NAME, "inventory_item_name"
            ).text

            if name in product_names:
                product.find_element(
                    By.CSS_SELECTOR, ".btn_inventory"
                ).click()

    def go_to_cart(self):
        """Переходит на страницу корзины покупок."""
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()
