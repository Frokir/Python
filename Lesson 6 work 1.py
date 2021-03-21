import time


class TrafficLight:
    def __init__(self):
        self.__color = ''

    def running(self):
        color_list = ['Красный', 'Желтый', 'Зелёный']
        color_dict = {"Красный": 7, "Желтый": 2, "Зелёный": 5}
        for color in color_list:
            self.__color = color
            print(self.__color)
            time.sleep(color_dict[color])


var = TrafficLight()
var.running()
