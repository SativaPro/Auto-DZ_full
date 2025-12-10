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
driver.get("http://the-internet.herokuapp.com/login")

# Находим поле username и вводим значение
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

# Находим поле password и вводим значение
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

# Находим кнопку Login и кликаем
login_button = driver.find_element(
    By.CSS_SELECTOR, "i.fa-sign-in")
login_button.click()

# Находим зеленую плашку с сообщением об успехе
flash_message = driver.find_element(By.ID, "flash")

# Выводим текст из плашки в консоль
print("Текст зеленой плашки:", flash_message.text)

sleep(3)

# Закрываем браузер
driver.quit()
