import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# Тесты для capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("a", "A"),         # тест на строку из 1 символа
    ("Sky", "Sky")      # тест на сразу заглавную букву в начале
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   ")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Тесты для функции trim
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),     # 1 пробел
    ("   skypro", "skypro"),   # 3 пробела
    ("skypro", "skypro"),      # строка без пробелов в начале
    ("\tskypro", "\tskypro")   # табуляция не удаляется
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                   # ничего
    ("   ", ""),                # только пробелы
    ("  skypro  ", "skypro  ")  # удаляет только пробелы в начале
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Тесты для функции contains
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),      # в верхнем регистре
    ("SkyPro", "y", True),      # в нижнем регистре
    ("SkyPro", "Sky", True),    # поиск подстроки
    ("", "", True),             # пустая строка содержит пустую подстроку
    ("123", "123", True)        # с цифрами
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "1234", False),    #
    ("", "a", False),             # пустая строка не содержит символ
    ("1235", "x", False),         #
    ("Python", "python", False)   # регистрозависимый поиск
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# Тесты для функции delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("hello", "l", "heo"),        # удаление всех вхождений
    ("aaaa", "a", ""),            # удаление всех символов
    ("test", "", "test"),         # пустой символ для удаления
    ("test 1", " ", "test1")      # удаление пробелов
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),    # удаление отсутствующего символа
    ("", "a", ""),                # удаление из пустой строки
    ("test", "TEST", "test")      # регистрозависимое удаление
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
