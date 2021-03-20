with open('text_7.txt') as my_file:
    lines = my_file.readlines()
firms_dict = {line.split()[0]: [line.split()[2], line.split()[3]] for line in
              lines}  # Словарь фирм формата {Название: [прибыль, издержки]}
profit_firms = {}  # Словарь фирм формата {название: баланс}
for firm in firms_dict.keys():
    balance = int(firms_dict[firm][0]) - int(firms_dict[firm][1])
    print(f'Фирма: {firm}, Баланс: {balance}')
    profit_firms[firm] = balance

summ_list = [i for i in profit_firms.values() if
             i > 0]  # Генератор списка который берет только положительные значения баланса и добавляет их в списко
print(
    f'Средняя прибыль: {sum(summ_list) / len(summ_list)}')  # Принт который выводит баланс поделив сумму положительных балансов на их колличество

summ_list = [i for i in
             profit_firms.values()]  # Переделываем ненужный список. Создаем по новой только теперь без условий. В список попадут все балансы включая отрицательные.
my_sum = round(sum(summ_list) / len(summ_list), 2)  # Вычисляем средний доход уже с учётом отрицательных балансов
answear = [profit_firms, {'average_profit': my_sum}]  # Формируем список по заданию
print(answear)
