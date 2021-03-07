my_list = []
my_list.append(1)
my_list.append('1')
my_list.append([])
my_list.append((1, 2))
my_list.append({'name': 'value'})

print(my_list)

for i in my_list:
    print("Тип файла: ", type(i))