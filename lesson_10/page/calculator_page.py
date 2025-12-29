import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Page Object для страницы калькулятора с задержкой выполнения операций."""

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        """
        Инициализирует экземпляр CalculatorPage.
        Args: driver: WebDriver для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

        with open("lesson_07/locators.json", "r") as file:
            self.locators = json.load(file)

    def open(self):
        """Открывает страницу калькулятора в браузере."""
        self.driver.get(self.URL)

    def set_delay(self, value: str):
        """
        Устанавливает значение задержки вычислений в калькуляторе.
        Args: value (str): Значение задержки в секундах для установки в поле ввода
        """
        delay_input = self.driver.find_element(
            By.CSS_SELECTOR,
            self.locators["calc_delay_input"]
        )
        delay_input.clear()
        delay_input.send_keys(value)

    def click_button(self, locator_key: str):
        """
        Кликает по кнопке калькулятора, найденной по ключу локатора.
        Args: locator_key (str): Ключ для поиска локатора в словаре self.locators
        """
        button = self.driver.find_element(
            By.XPATH,
            self.locators[locator_key]
        )
        button.click()

    def calculate_7_plus_8(self):
        """Выполняет последовательное нажатие кнопок для вычисления 7 + 8."""
        self.click_button("calc_button_7")
        self.click_button("calc_button_plus")
        self.click_button("calc_button_8")
        self.click_button("calc_button_equals")

    def wait_result(self, expected_result: str):
        """
        Ожидает появления ожидаемого результата на экране калькулятора.
        Args: expected_result (str): Ожидаемое текстовое значение результата
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, self.locators["calc_screen"]),
                expected_result
            )
        )

    def get_result(self) -> str:
        """
        Получает текущий результат с экрана калькулятора.
        Returns: str: Текстовое значение, отображаемое на экране калькулятора
        """
        screen = self.driver.find_element(
            By.CSS_SELECTOR,
            self.locators["calc_screen"]
        )
        return screen.text
