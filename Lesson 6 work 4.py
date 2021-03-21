class Car:
    def __init__(self, name='', color='black', speed=0, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is go')

    def stop(self):
        print(f'{self.name} is stopped')

    def turn(self, direction):
        print(f'{self.name} is turn {direction}')

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} speed is {self.speed}')
            print('Speed is over limit')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} speed is {self.speed}')
            print('Speed is over limit')


class PoliceCar(Car):
    pass


if __name__ == '__main__':
    sport_car_1 = SportCar(name='Ferrari', color='red')
    sport_car_1.go()
    sport_car_1.speed = 150
    sport_car_1.show_speed()

    town_car_1 = TownCar(name='Post', speed=70)
    town_car_1.turn('right')
    town_car_1.show_speed()
