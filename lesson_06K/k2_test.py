import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_slow_calculator():

    # Загружаем локаторы из JSON файла
    with open('lesson_06K/locators.json', 'r') as file:
        loc = json.load(file)

    driver = webdriver.Chrome(service=ChromeService
                              (ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        # 1. Открыть страницу калькулятора
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # 2. Ввести значение 45 в поле delay
        delay_input = driver.find_element(By.CSS_SELECTOR, loc["calc_delay_input"])
        delay_input.clear()  # Очищаем поле, если там есть значение
        delay_input.send_keys("45")

        # 3. Нажать кнопки: 7, +, 8, =
        button_7 = driver.find_element(By.XPATH, loc["calc_button_7"])
        button_7.click()

        button_plus = driver.find_element(By.XPATH, loc["calc_button_plus"])
        button_plus.click()

        button_8 = driver.find_element(By.XPATH, loc["calc_button_8"])
        button_8.click()

        button_equals = driver.find_element(By.XPATH, loc["calc_button_equals"])
        button_equals.click()

        # 4. Проверить, что результат 15 появится через 45 секунд
        start_time = time.time()  # время начала ожидания
        wait = WebDriverWait(driver, 50)  # timeout больше 45 секунд
        # Ожидаем, пока на экране не появится текст "15"
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, loc["calc_screen"]),
                "15"
            )
        )

        end_time = time.time()  # время окончания ожидания
        elapsed_time = end_time - start_time

        print(f"Результат появился через {elapsed_time:.1f} секунд")

        # 5. Получаем текущий текст на экране для проверки
        screen_element = driver.find_element(By.CSS_SELECTOR, loc["calc_screen"])
        current_result = screen_element.text

        # Проверяем, что результат равен 15
        assert current_result == "15", \
            f"Ожидался результат 15, но получили: {current_result}"

        print(f"Результат на экране: {current_result}")

        # Проверяем, что прошло не менее 40 секунд (с учетом погрешности)
        assert elapsed_time >= 40, \
            f"Результат появился через: {elapsed_time:.1f} секунд. Ожидалось ~45 секунд"

    except Exception as e:
        print(f"Ошибка в тесте: {str(e)}")
        driver.save_screenshot("./screen/test.png")  # скриншот при ошибке
        raise

    finally:
        driver.quit()

# python -m pytest lesson_06K/k2_test.py -v -s
