'''
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
'''


class Car:
    __color = None

    def __init__(self, speed: [int], color: [str], name: [str], is_police: [bool]):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "Машина едет"

    def stop(self):
        return "Машина стоит"

    def turn(self, direction):
        return f"Машина повернула на {direction}"


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость машины {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Скорость машины {self.name} выше положенной'
        else:
            return f'Скорость машины {self.name} в норме'


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость рабочей машины {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'Скорость рабочей машины {self.name} выше положенной'


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полицейского управления'
        else:
            return f'{self.name} не из полицейского управления'


if __name__ == '__main__':
    car_1 = SportCar(100, 'Red', 'Audi', False)
    car_2 = TownCar(30, 'Black', 'Audi', False)
    car_3 = WorkCar(70, 'White', 'Audi', True)
    car_4 = PoliceCar(110, 'Blue', 'Audi', True)

    print(car_1.turn('left'))
    print(car_1.stop())
    print(car_1.go())
    print(car_1.turn('left'))
    print(car_2.show_speed())
    print(car_3.show_speed())
    print(car_4.police())
