from threading import Thread
from time import sleep


class Knight(Thread):
    

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            enemies -= self.power
            sleep(1)
            days += 1
            print(f'{self.name} сражается {days} дней (дня)..., осталось {enemies} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')