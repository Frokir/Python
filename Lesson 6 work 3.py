class Worker:
    def __init__(self, name='', surname='', position=''):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': 0, 'bonus': 0}

    def incomer(self, wage, bonus):
        self.__income['wage'] = int(wage)
        self.__income['bonus'] = int(bonus)

class Position(Worker):
    def __init__(self, name='', surname='', position=''):
        self.__income = {'wage': 0, 'bonus': 0}
        super().__init__(name, surname, position,)


    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self.__income['wage'] * self.__income['bonus']

worker = Position(name='Oleg', surname='Perepl')
worker.position = 'Boss'
worker.incomer(10000, 5000)
print(worker.get_total_income())

print(worker.get_full_name())

