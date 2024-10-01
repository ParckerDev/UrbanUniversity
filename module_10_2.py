from threading import Thread
from time import sleep


class Knight(Thread):
    
    def __init__(self, name, power):
        self.name = name
        self.power = power
        super().__init__()
        

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            enemies -= self.power
            sleep(1)
            days += 1
            print(f'{self.name} сражается {days}..., осталось {enemies} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')