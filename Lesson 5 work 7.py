with open('text_7.txt') as my_file:
    lines = my_file.readlines()
firms_dict = {line.split()[0]: [line.split()[2], line.split()[3]] for line in lines}
profit_firms = {}
for firm in firms_dict.keys():
    balance = int(firms_dict[firm][0]) - int(firms_dict[firm][1])
    print(f'Фирма: {firm}, Баланс: {balance}')
    profit_firms[firm] = balance

summ_list = [i for i in profit_firms.values() if i > 0]
print(f'Средняя прибыль: {sum(summ_list) / len(summ_list)}')

summ_list = [i for i in profit_firms.values()]
my_sum = round(sum(summ_list) / len(summ_list), 2)
answear = [profit_firms, {'average_profit': my_sum}]
print(answear)
