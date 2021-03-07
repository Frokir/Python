month = input('Input month number: ')
dict_year = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
for key in dict_year.keys():
    if int(month) in dict_year[key]:
        print(key)