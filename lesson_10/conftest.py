import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def chrome_driver():
    """
    Фикстура для создания экземпляра Chrome WebDriver.
    После завершения теста автоматически закрывает браузер.
    """
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver():
    """
    Фикстура для создания экземпляра Firefox WebDriver.
    После завершения теста автоматически закрывает браузер.
    """
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )
    driver.maximize_window()
    yield driver
    driver.quit()
