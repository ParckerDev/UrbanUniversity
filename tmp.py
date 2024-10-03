from queue import Queue
import random
from threading import Thread
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        sleep(random.randint(3, 11))


class Cafe:
    def __init__(self, *tables: Table):
        self.tables = [*tables]
        self.queue = Queue()

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            if any(table.guest == None for table in self.tables): # проверяем наличие свободного стола
                print(filter(lambda obj: obj.guest == None, self.tables))
            else:
                print(f'No free tables, {guest.name}')

    def discuss_guests(self, ):
        pass


cafe = Cafe(*[Table(str(i)) for i in range(1, 13)])
print(*(table.guest for table in cafe.tables))
for table in cafe.tables:
    if int(table.number) % 2 == 0:
        table.guest = Guest('Ivan') # type: ignore
print(*(table.guest for table in filter(lambda obj: obj.guest == None, cafe.tables)))
