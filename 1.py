import time


class TrafficLight:
    __color = None

    def __init__(self, couchange_count=1):
        self.change_count = change_count

    def running(self):
        i = 1
        while i <= int(self.change_count):
            print('Красный')
            time.sleep(7)
            print('Желтый')
            time.sleep(5)
            print('Зеленый')
            time.sleep(7)
            print('-------')
            i += 1


if __name__ == '__main__':
    change_count = input('Введите число повторений светофора: ')
    if change_count.isdigit():
        TrafficLight(change_count).running()
