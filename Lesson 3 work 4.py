'''Формула гласит: число а в отрицательной степени n равно едениуце разделённой на a в положительной степени n: a^−n = 1/a^n
Функуия работает только при отрицательном значении y. '''


def exponentiation(x, y):  # Вариант 1
    return x ** y


def exponentiation_2(x, y):  # Вариант 2. Без использования встроенных функций.
    if x != 0:
        start = x
        for _ in range((y * -1) - 1):
            start = start * x
        x = start
        answear = 1 / x

    else:
        answear = 0

    return answear


if __name__ == '__main__':
    print(exponentiation_2(-2, -5))
    print(exponentiation(-2, -5))
    print(exponentiation_2(3, -6))
    print(exponentiation(3, -6))
    input('Enter for exit')
