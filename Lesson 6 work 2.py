class Road:
    def __init__(self, length, width, weight=25, depth=1):
        self._length = length
        self._width = width
        self.weight = weight
        self.depth = depth

    def calculate(self):
        answear = self._length * self._width * self.weight * self.depth
        return answear / 1000


var = Road(20, 5000, depth=5)
print(var.calculate())
