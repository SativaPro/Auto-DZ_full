from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.maximize_window()

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Дожидаемся, когда надпись "Loading images..." сменится на "Done!"
waiter = WebDriverWait(driver, 20)
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), "Done!")
)

# После загрузки, находим 3-ю картинку (с id="award")
image3 = driver.find_element(By.CSS_SELECTOR, "#award")

# Получаем значение атрибута src
src_value = image3.get_attribute("src")
print("Значение атрибута src у 3-й картинки:", src_value)

# Закрываем браузер
driver.quit()
