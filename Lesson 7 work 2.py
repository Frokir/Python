from abc import ABC, abstractmethod


class Dress(ABC):
    def __init__(self, v, name=''):
        self.name = name
        self.v = int(v)

    @abstractmethod
    def calculate_fabric(self):
        pass


class Coat(Dress):
    @property
    def calculate_fabric(self):
        return self.v / 6.5 + 0.5


class Mens_suit(Dress):
    @property
    def calculate_fabric(self):
        return 2 * self.v + 0.3


def calculate(data):
    summ = 0
    for el in data:
        summ += el.calculate_fabric
    return summ


data_set = []  # Мини база данных.
data_set.append(Coat(34, 'Long Iland'))
data_set.append(Coat(40))
data_set.append(Mens_suit(41))
data_set.append(Mens_suit(44, 'BB Show'))

print('Общий расход ткани по всем вещам: ', round(calculate(data_set), 2))
