"""Немного добавил фугкционал, строки прнимаются в любом порядке, не только как в шаблоне."""

numbers_dict = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}
with open('text4.txt', encoding="utf-8") as my_file:
    lines = [i.rstrip() for i in my_file.readlines()]
answear_file = open('answear_4.txt', 'w')
for line in lines:
    my_line = line.replace(line.split()[0], numbers_dict[line.split()[2]])

    print(my_line, file=answear_file)
answear_file.close()
