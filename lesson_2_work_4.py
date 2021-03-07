my_string = input('Введите вашу строку: ')
string_list = my_string.split()
number = 1
for i in string_list:
    if len(i) < 11:
        print(number, i)
    else:
        print(number, i[:10])
    number += 1


