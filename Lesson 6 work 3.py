class Worker:
    def __init__(self, name='', surname='', position=''):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': 0, 'bonus': 0}

    def set_incom(self, wage, bonus):
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker_1 = Position(name='Oleg', surname='Perepl')
worker_1.position = 'Boss'
worker_1.set_incom(10000, 5000)
print(worker_1.get_full_name())
print(worker_1.get_total_income())
print(worker_1.position)
