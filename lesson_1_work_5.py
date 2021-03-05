import math

profit = int(input('Значение прибыл:'))
lesion = int(input('Значение убытка:'))

if profit > lesion:
    print('Фирма работает в плюс')
    k = math.gcd(profit, lesion)
    print(f'С соотношением: {profit//k} к {lesion//k}')

    people = int(input('Введите число сотрудников: '))
    print(f"Прибыль на сотрудника составляет: {round((profit-lesion)/people), 2}")
else:
    print("Фирма работает в минус")

