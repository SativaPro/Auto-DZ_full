import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def test_demo_purchase():

    driver = webdriver.Firefox(service=FirefoxService
                               (GeckoDriverManager().install()))
    driver.maximize_window()

    try:
        # 1. Открыть сайт магазина
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)

        # 2. Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Ждем загрузки
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )

        # 3. Добавить товары в корзину
        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        # Ищем все товары на странице
        all_products = driver.find_elements(By.CLASS_NAME, "inventory_item")

        for product in all_products:
            product_name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            if product_name in products_to_add:
                add_button = product.find_element(By.CSS_SELECTOR, ".btn_inventory")
                add_button.click()
                time.sleep(1)

        # 4. Перейти в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)

        # 5. Нажать Checkout
        driver.find_element(By.ID, "checkout").click()
        time.sleep(1)

        # 6. Заполнить форму данными
        driver.find_element(By.ID, "first-name").send_keys("Анастасия")
        driver.find_element(By.ID, "last-name").send_keys("Прокудина")
        driver.find_element(By.ID, "postal-code").send_keys("394016")

        # 7. Нажать Continue
        driver.find_element(By.ID, "continue").click()
        time.sleep(3)

        # 8. Прочитать итоговую стоимость
        # Прокручиваем вниз
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Находим итоговую сумму
        total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        total_amount = total_text.replace("Total: $", "").strip()
        print(f"Итоговая сумма: ${total_amount}")

        # 9. Проверить сумму
        assert total_amount == "58.29", f"Получено ${total_amount}"
        print(f"Сумма корректная: ${total_amount}")

    except Exception as e:
        print(f"Ошибка: {str(e)}")
        driver.save_screenshot("./screen/sauce_error.png")
        raise

    finally:
        driver.quit()

# python -m pytest lesson_06K/k3_test.py -v -s
