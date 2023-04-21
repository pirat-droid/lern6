class Worker:
    __color = None

    def __init__(self, name: [str], surname: [str], position: [str], wage: [int], bonus: [int]):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())


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
