tovari = []
schet = 1
names = []
costs = []
numbers = []
eds =[]



while True:
    corteg = []
    tov = {}
    name = input(f'Заполняем данные о {schet} товаре, введите название, для выхода нажмите Enter: ')
    if name:
        corteg.append(schet)
        tov['название'] = name
        names.append(name)
        cost = input(f'Введите цену за {name}: ')
        tov['цена'] = cost
        costs.append(cost)
        number = input('Введите количество: ')
        tov['количество'] = number
        numbers.append(number)
        ed = input('Введите еденицы измерения: ')
        tov['ед'] = ed
        eds.append(ed)
        corteg.append(tov)
        schet += 1
        corteg = tuple(corteg)
        tovari.append(corteg)


    else:
        break

for i in tovari:
    print(i)

analis_dict = {'название': names, 'цена': costs, 'количество': eds, 'ед': eds}

print(analis_dict)
