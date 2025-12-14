import time
from lesson_07.page.calculator_page import CalculatorPage


def test_calculator(chrome_driver):
    page = CalculatorPage(chrome_driver)

    # 1. Открыть страницу
    page.open()

    # 2. Ввести delay = 45
    page.set_delay("45")

    # 3. Нажать 7 + 8 =
    start_time = time.time()
    page.calculate_7_plus_8()

    # 4. Ожидать результат
    page.wait_result("15")
    end_time = time.time()

    # 5. Проверка результата
    result = page.get_result()
    assert result == "15", f"Ожидали 15, получили {result}"

    # 6. Проверка времени
    elapsed = end_time - start_time
    assert elapsed >= 40, f"Результат появился слишком быстро: {elapsed:.1f} сек"

# python -m pytest lesson_07/test/calculator_test.py -v -s
