from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/ajax")

# Нажимаем на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# Ожидаем появления зеленой плашки с текстом
waiter = WebDriverWait(driver, 30)
success_element = waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
)

# Получаем текст из зеленой плашки
success_text = success_element.text
print("Текст зеленой плашки:", success_text)

# Закрываем браузер
driver.quit()
