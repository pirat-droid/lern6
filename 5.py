'''
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:

    def __init__(self, title: [str]):
        self.title = title

    def draw(self):
        return "Машина едет"


class Pen(Stationery):

    def __init__(self, title: [str]):
        super().__init__(title)

    def draw(self):
        return "Ручка"


class Pencil(Stationery):

    def __init__(self, title: [str]):
        super().__init__(title)

    def draw(self):
        return "Карандаш"


class Handle(Stationery):

    def __init__(self, title: [str]):
        super().__init__(title)

    def draw(self):
        return "Маркер"


if __name__ == '__main__':
    print(Pen('Ручка').draw())
    print(Pencil('Карандаш').draw())
    print(Handle('Маркер').draw())
