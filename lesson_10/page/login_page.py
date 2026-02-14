from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Page Object для страницы авторизации."""

    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        """
        Инициализирует экземпляр LoginPage.
        Args: driver (WebDriver): WebDriver для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Открывает страницу авторизации в браузере."""
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        """
        Выполняет авторизацию пользователя.
        Args:
            username (str): Логин пользователя
            password (str): Пароль пользователя
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

        self.wait.until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
