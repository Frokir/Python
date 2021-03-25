class Cell:
    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        answear = self.nucleus - other.nucleus
        if answear > 0:
            return answear
        else:
            print('Ошибка вычитания. Отрицательное значение разности недопустимо.')

    def __mul__(self, other):
        return Cell(self.nucleus * other.nucleus)

    def __truediv__(self, other):
        return Cell(self.nucleus // other.nucleus)

    def make_order(self, num):
        answear_str = ''
        residue = self.nucleus - (num * (self.nucleus // num))
        for _ in range(self.nucleus // num):
            answear_str += '*' * num + '\n'
        answear_str += '*' * residue

        return answear_str


cell_1 = Cell(10)
cell_2 = Cell(15)
cell_3 = cell_1 + cell_2
cell_4 = Cell(5)
cell_5 = cell_3 / cell_4

print(cell_5.make_order(2))
