def fact(n):
    answear = 1
    for i in range(2, n + 1):
        answear = answear * i
        yield answear


"""Возможно я не так понял ТЗ. Моя фунция выводит факториалы всех чисел на пути к факториалу требуемого числа. Если 
необходимо вывести просто числовой ряд до достижения цели то это второй вариант фукции."""


def fact_2(n):
    for i in range(1, n + 1):
        yield i


for el in fact(4):
    print(el)

for el in fact_2(4):
    print(el)
