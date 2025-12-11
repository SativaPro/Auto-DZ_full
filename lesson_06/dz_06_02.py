from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/textinput")

# Находим поле ввода и вводим текст "SkyPro"
input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.send_keys("SkyPro")

# Нажимаем на синюю кнопку (у которой изначально другой текст)
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()

# Ожидаем, пока текст кнопки изменится на "SkyPro"
waiter = WebDriverWait(driver, 10)
waiter.until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
)

# Получаем текст кнопки после изменения
updated_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button_text = updated_button.text
print("Текст кнопки:", button_text)

# Закрываем браузер
driver.quit()
