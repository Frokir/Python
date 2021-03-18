with open('text1.txt') as my_file:
    text_list = my_file.readlines()

workers_dict = {line.split()[0]: int(line.split()[1]) for line in text_list}
summ_salary = 0
for key in workers_dict.keys():
    summ_salary += workers_dict[key]
    if workers_dict[key] < 20000:
        print(f'{key} имеет зарплату меньше 20000')

print(f'Средняя зарплата по штату {summ_salary / len(text_list)}')
