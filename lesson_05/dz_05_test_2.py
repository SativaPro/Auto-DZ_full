from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.maximize_window()

# зайти на сайт
driver.get("http://uitestingplayground.com/dynamicid")

button_locator = "button.btn.btn-primary"  # объявление локатора
check_element = driver.find_element(
    By.CSS_SELECTOR, button_locator)  # поиск элемента
check_element.click()  # клик на элемент

sleep(5)
