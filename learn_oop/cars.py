"""
SOLID

S - Single responsibility
O - Open/Closed
L - Liskov substitution
I - Interface segragation
D - Dependesy inversion


DRY - Dont repeat yourself

Паттерны/Антипаттерны 
 - God class <- класс, который включает все и вся

!! Полиморфизм
"""
import time


class Player: pass


class Car:
    def __init__(self):
        self.color = 'black'
        self.speed = 0
        self.player = Player()

    def speed_up(self):
        self.speed += 1

    def move_forward(self, meters: int):
        if self.speed == 0:
            raise ValueError('Can not move with 0 speed')
        seconds = meters / self.speed
        time.sleep(seconds)

    def speed_down(self):
        if self.speed > 0:
            self.speed -= 1


class RedCar(Car):
    def __init__(self):
        super().__init__()
        self.color = 'red'

    def speed_up(self):
        self.speed += 5

    def speed_down(self):
        self.speed -= 5


class BMWCar(Car):
    def __init__(self):
        super().__init__()
        self.color = 'blue'

    @classmethod
    def create_red(cls):
        car = cls() # <-- BMWCar()
        car.color = 'red'
        return car

    @classmethod
    def create_brown(cls):
        car = cls()
        car.color = 'brown'
        return car

    def speed_up(self):
        self.speed += 10

    def speed_down(self):
        self.speed -= 10


class BMWPlusCar(BMWCar):
    def speed_up(self):
        self.speed += 15


def check_car(car: Car) -> bool:
    status = True
    try:
        car.speed_up()
        car.speed_up()
        car.speed_up()
        car.speed_up()

        car.move_forward(100)
        car.speed_down()
    except NotImplementedError as err:
        status = False
    return status


# def check_car(car) -> bool:
#     status = True
#     try:
#         if isinstance(car, RedCar):
#             car.move_forward(100)
#         elif isinstance(car, BMWCar):
#             car.speed_up()
#         car.speed_down()
#     except AttributeError as err:
#         status = False
#     return status


# def check_car(car: RedCar) -> bool:
#     status = True
#     try:
#         # car.speed_up()
#         car.move_forward(100)
#         car.speed_down()
#     except AttributeError as err:
#         status = False
#     return status


# def check_car(car: BMWCar) -> bool:
#     status = True
#     try:
#         car.speed_up()
#         # car.move_forward(100)
#         car.speed_down()
#     except AttributeError as err:
#         status = False
#     return status


# red_car = RedCar()
# bmw_car = BMWCar()
# print(check_car(red_car), check_car(bmw_car))


bmw_car = BMWCar.create_red()
bmw_plus_car = BMWPlusCar.create_brown()
print('well done')
