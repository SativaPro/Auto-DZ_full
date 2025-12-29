import allure
import time
import pytest
from lesson_07.page.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тестирование калькулятора с задержкой")
@allure.description("""
Тест проверяет работу калькулятора с задержкой:
1. Установка задержки 45 секунд
2. Выполнение операции 7 + 8
3. Проверка результата и времени выполнения
""")
def test_calculator(chrome_driver):
    with allure.step("Инициализация страницы калькулятора"):
        page = CalculatorPage(chrome_driver)

    with allure.step("Открыть страницу калькулятора"):
        page.open()

    with allure.step("Установить задержку 45 секунд"):
        page.set_delay("45")

    with allure.step("Выполнить операцию 7 + 8"):
        start_time = time.time()
        page.calculate_7_plus_8()

    with allure.step("Дождаться результата"):
        page.wait_result("15")
        end_time = time.time()

    with allure.step("Проверить результат вычислений"):
        result = page.get_result()
        allure.attach(f"Результат вычисления: {result}",
                      name="Calculation Result",
                      attachment_type=allure.attachment_type.TEXT)
        assert result == "15", f"Ожидали 15, получили {result}"

    with allure.step("Проверить время выполнения (не менее 40 секунд)"):
        elapsed = end_time - start_time
        allure.attach(f"Время выполнения: {elapsed:.2f} секунд",
                      name="Execution Time",
                      attachment_type=allure.attachment_type.TEXT)
        assert elapsed >= 40, f"Результат появился слишком быстро: {elapsed:.1f} сек"

# python -m pytest lesson_10/test/calculator_test.py -v -s
