import allure
import pytest
from lesson_07.page.login_page import LoginPage
from lesson_07.page.inventory_page import InventoryPage
from lesson_07.page.cart_page import CartPage
from lesson_07.page.checkout_page import CheckoutPage


@allure.feature("Демонстрационная покупка")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Полный цикл покупки товара в демо-магазине")
@allure.description("""
Тест проверяет полный цикл покупки товара:
1. Авторизация стандартного пользователя
2. Добавление товара в корзину
3. Оформление заказа
4. Подтверждение заказа
""")
def test_demo_purchase(firefox_driver):
    with allure.step("Инициализация Page Objects"):
        login_page = LoginPage(firefox_driver)
        inventory_page = InventoryPage(firefox_driver)
        cart_page = CartPage(firefox_driver)
        checkout_page = CheckoutPage(firefox_driver)

    with allure.step("Открыть сайт и авторизоваться"):
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        inventory_page.add_products_to_cart([
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ])

    with allure.step("Перейти в корзину"):
        inventory_page.go_to_cart()

    with allure.step("Нажать Checkout"):
        cart_page.checkout()

    with allure.step("Заполнить форму оформления заказа"):
        checkout_page.fill_form(
            first_name="Анастасия",
            last_name="Прокудина",
            postal_code="394016"
        )

    with allure.step("Проверить сумму заказа"):
        total = checkout_page.get_total_amount()
        allure.attach(f"Итоговая сумма: {total}", name="Total Amount",
                      attachment_type=allure.attachment_type.TEXT)
        assert total == "58.29", f"Ожидалось 58.29, получено {total}"

# python -m pytest lesson_10/test/demo_purchase_test.py -v -s
