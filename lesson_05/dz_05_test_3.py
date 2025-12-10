from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Создаем драйвер для Firefox
driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))
driver.maximize_window()

# зайти на сайт
driver.get("https://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(
    By.TAG_NAME, "input")  # поиск поля ввода
input_field.send_keys("Sky")  # ввод текст
input_field.clear()  # очистка поля
input_field.send_keys("Pro")  # ввод текста

sleep(5)

driver.quit()  # закрыть браузер
