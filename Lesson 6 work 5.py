class Stationery:
    def __init__(self, title='base'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Ручка начала отрисовку с титулем {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Карандаш начал отрисовку с титулем {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Маркер начал отрисовку с титулем {self.title}')


var_1 = Pen('Parker').draw()
var_2 = Pencil(title='tree').draw()
var_3 = Handle()
var_3.draw()
var_4 = Stationery('boss').draw()
