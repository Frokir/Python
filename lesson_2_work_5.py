def reshenie (a):
    global my_list
    if a in my_list:
        my_list.insert(my_list.index(a), a) #Первый вариант решения
    else:
        my_list.append(a)
        my_list.sort(reverse=True) # Второй вариант решения
    print(my_list)



my_list = [7, 5, 3, 3, 2]
print('Первичный лист', my_list)

while True:
    a = input(f'Введите значение. Для завершение нажмите Enter без значаения: ')
    if a:
        reshenie(int(a))
    else:
        break