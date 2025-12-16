from lesson_07.page.login_page import LoginPage
from lesson_07.page.inventory_page import InventoryPage
from lesson_07.page.cart_page import CartPage
from lesson_07.page.checkout_page import CheckoutPage


def test_demo_purchase(firefox_driver):
    login_page = LoginPage(firefox_driver)
    inventory_page = InventoryPage(firefox_driver)
    cart_page = CartPage(firefox_driver)
    checkout_page = CheckoutPage(firefox_driver)

    # 1. Открыть сайт и авторизоваться
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # 2. Добавить товары
    inventory_page.add_products_to_cart([
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ])

    # 3. Перейти в корзину
    inventory_page.go_to_cart()

    # 4. Checkout
    cart_page.checkout()

    # 5. Заполнить форму
    checkout_page.fill_form(
        first_name="Анастасия",
        last_name="Прокудина",
        postal_code="394016"
    )

    # 6. Проверить сумму
    total = checkout_page.get_total_amount()
    assert total == "58.29", f"Ожидалось 58.29, получено {total}"

# python -m pytest lesson_07/test/demo_purchase_test.py -v -s
