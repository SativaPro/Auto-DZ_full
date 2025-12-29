# Проект автоматизации тестирования с Page Object и Allure

## Описание проекта
Проект содержит автоматизированные тесты для демонстрационного интернет-магазина и онлайн-калькулятора с использованием паттерна Page Object и фреймворка Allure для отчетов.

## Структура проекта

lesson_10/
├── page/ # Page Object классы
│ ├── login_page.py # Страница авторизации
│ ├── inventory_page.py # Страница товаров
│ ├── cart_page.py # Страница корзины
│ ├── checkout_page.py # Страница оформления заказа
│ ├── calculator_page.py # Страница калькулятора
│ └── init.py
├── test/ # Тесты
│ ├── demo_purchase_test.py # Тест покупки товаров
│ ├── calculator_test.py # Тест калькулятора
│ └── init.py
├── conftest.py # Фикстуры pytest (настройка драйверов)
├── locators.json # Локаторы для калькулятора
└── README.md # Эта документация

## Установите Allure CLI на macOS:
# Установите Homebrew (если еще не установлен)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Установите Allure через brew
brew install allure

# Проверьте установку
allure --version

## ЗАПУСК ТЕСТОВ
# Из корневой папки проекта
python -m pytest lesson_10/test/ --alluredir=lesson_10/allure-results -v

# Тест покупки товаров
python -m pytest lesson_10/test/demo_purchase_test.py -v

# Тест калькулятора
python -m pytest lesson_10/test/calculator_test.py -v

# Запуск с отображением шагов в консоли
python -m pytest lesson_10/test/ --alluredir=lesson_10/allure-results -v -s

## Генерация статического HTML отчета
allure generate allure-results -o allure-report --clean

# Откройте отчет в браузере
open allure-report/index.html
