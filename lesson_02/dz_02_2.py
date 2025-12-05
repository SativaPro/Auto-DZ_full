# Функция проверяет, является ли год високосным.

# Вариант 1
def is_year_leap(year):
    # Проверяем, делится ли год на 4 без остатка
    if year % 4 == 0:
        return True
    else:
        return False


year_check = 2025
result = is_year_leap(year_check)
print(f"год {year_check}: {result}")


# Вариант 2 с вводом года в консоли
def is_year_leap(year):
    return True if year % 4 == 0 else False


ye = int(input("Введите год: "))
result = is_year_leap(ye)
print(f"Високосный ли год {ye}? - {result}")
