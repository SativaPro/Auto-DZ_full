def month_to_season(month):

    # Проверка что число находится в допустимом диапазоне
    if month < 1 or month > 12:
        return "Ошибка: месяц должен быть от 1 до 12"

    season_index = (month % 12) // 3    # формула группирует месяцы по 3
    seasons = ["Зима", "Весна", "Лето", "Осень"]    # список сезонов индексам
    return seasons[season_index]


month = int(input("Введите номер месяца (1-12): "))
print(month_to_season(month))
