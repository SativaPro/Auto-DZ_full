import math


def square(side):
    area = side * side
    # если сторона целая - не округляем
    if side % 1 == 0:
        return area
    else:
        return math.ceil(area)


side_input = float(input("Введите длину стороны квадрата: "))
result = square(side_input)
print(f"Площадь квадрата со стороной {side_input}: {result}")
