a = int(input('A: '))
b = int(input('B: '))

day = 1
while True:
    if a >= b:
        print(f'{day}-й день')
        break
    else:
        a = a*1.1
        day += 1
