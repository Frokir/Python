import random

# Блок 1 запись в файл
number_text = ''
for _ in range(10):
    number_text = number_text + str(random.randint(1, 100)) + ' '

with open('text_5.txt', 'w') as my_file:
    my_file.write(number_text)

# Блок 2 чтение и подсчёт
with open('text_5.txt') as my_file:
    print(sum([int(o) for o in my_file.readline().split()]))
