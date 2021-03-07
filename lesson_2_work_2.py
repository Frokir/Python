def lister(listik):
    list_len = len(listik)
    if (list_len % 2) != 0:
        list_len -= 1

    for i in range(0, list_len, 2):
        listik[i], listik[i+1] = listik[i+1], listik[i]
    return listik

my_list = []
iteration = 1
while True:
    a = input(f'Введите {iteration}й элемент списка. Для завершение нажмите Enter без значаения: ')
    if a:
        my_list.append(a)
        iteration += 1
    else:
        break

if len(my_list) <= 1:
    print('Список слишком мал =(')
else:
    print(lister(my_list))