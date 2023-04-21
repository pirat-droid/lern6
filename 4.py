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
        return f"Машина повернула {direction}"


class TownCar(Car):

    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    pass


if __name__ == '__main__':
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    position = input("Введите должность: ")
    wage = input("Введите оклад: ")
    bonus = input("Введите премию: ")

    try:
        arg = Position(name, surname, position, int(wage), int(bonus))
        print(arg.get_full_name())
        print(str(arg.get_total_income()))
    except ValueError:
        print('Неверный формат')
