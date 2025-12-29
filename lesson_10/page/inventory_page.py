from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_products_to_cart(self, product_names: list):
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
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()
