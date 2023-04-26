class Road:
    __color = None

    def __init__(self, length=1, width=1):
        self._length = length
        self._width = width

    def calculation(self):
        mass = int(self._length) * int(self._width) * 20 * 1
        print(str(mass))


if __name__ == '__main__':
    length = input('Введите длину: ')
    width = input('Введите ширину: ')
    if (width.isdigit()) and (length.isdigit()):
        Road(length, width).calculation()
