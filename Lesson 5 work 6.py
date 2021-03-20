my_dict = {}
with open('text_6.txt', encoding='utf-8') as my_file:
    lines = my_file.readlines()
for line in lines:
    splited_line = line.split()
    sum_time = 0
    for i in splited_line[1:]:
        number = ''
        for n in i:
            if n.isdigit():
                number = number + n
        if number != '':
            sum_time += int(number)
    if sum_time > 0:
        my_dict[splited_line[0][:-1]] = sum_time

print(my_dict)
