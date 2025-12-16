from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager

from page.MainPage import MainPage
from page.ResultPage import ResultPage
from page.CartPage import CartPage


def test_cart_counter():
    browser = webdriver.Chrome()

    main_page = MainPage(browser)
    main_page.set_cookie_polity()
    main_page.search('python')

    result_page = ResultPage(browser)
    to_be = result_page.add_books()  # Ожидаемый результат

    cart_page = CartPage(browser)
    cart_page.get()
    as_is = cart_page.get_counter()  # Фактический результат

    assert as_is == to_be


def test_empty_search_result():
    browser = webdriver.Chrome()

    main_page = MainPage(browser)
    main_page.set_cookie_polity()
    main_page.search('12345678901234567890')

    result_page = ResultPage(browser)
    msg = result_page.get_empty_result_message()   

    assert msg == "Пока не нашли для себя ничего в Лабиринте?"

    browser.quit()

# python -m pytest Urok_3/labirint_page_object_test.py -v -s