import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():

    # Загружаем локаторы
    with open('lesson_06K/locators.json', 'r') as file:
        loc = json.load(file)

    driver = webdriver.Safari()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    try:
        # 1. Открыть страницу
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # 2. Заполнить все поля кроме Zip code
        fields_to_fill = [
            ("first_name", "Иван"),
            ("last_name", "Петров"),
            ("address", "Ленина, 55-3"),
            ("zip_code", ""),  # Оставляем пустым
            ("email", "test@skypro.com"),
            ("phone", "+7985899998787"),
            ("city", "Москва"),
            ("country", "Россия"),
            ("job_position", "QA"),
            ("company", "SkyPro")
        ]

        for field_id, value in fields_to_fill:
            driver.find_element(
                By.CSS_SELECTOR, loc[field_id]).send_keys(value)

        # 3. Нажать Submit
        driver.find_element(By.CSS_SELECTOR, loc["submit_button"]).click()

        # 4. Проверить (assert), что поле Zip code подсвечено красным
        # Ждем появления div с id="zip-code" и классом "alert-danger"
        zip_alert = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#zip-code.alert-danger"))
        )
        # Проверка с assert
        assert "alert-danger" in zip_alert.get_attribute("class"), \
            "Поле Zip code не красное (отсутствует alert-danger)"

        print("Поле Zip code подсвечено красным")

        # 5. Проверить (assert), что остальные поля подсвечены зеленым
        green_field_ids = [
            "first-name", "last-name", "address", "e-mail", "phone",
            "city", "country", "job-position", "company"
        ]

        for field_id in green_field_ids:
            # Ждем появления каждого зеленого поля
            element = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, f"#{field_id}.alert-success"))
            )
            # Проверка с assert для каждого поля
            assert "alert-success" in element.get_attribute("class"), \
                f"Поле {field_id} не зеленое (отсутствует класс alert-success)"

            print(f"Поле {field_id} подсвечено зеленым")

    except Exception as e:
        print(f"Ошибка в тесте: {str(e)}")
        raise  # Поднимаем исключение, чтобы тест упал

    finally:
        driver.quit()

# python -m pytest lesson_06K/k1_test.py -v -s
