n = int(input("Введите число:"))


# Функция печатает числа от 1 до n.
def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:  # делится на 3 и 5
            print("FizzBuzz")
        elif i % 3 == 0:               # делится на 3
            print("Fizz")
        elif i % 5 == 0:               # делится на 5
            print("Buzz")
        else:                          # если не делится на 3 или 5
            print(i)


fizz_buzz(n)
