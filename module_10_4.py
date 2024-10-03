from queue import Queue
import random
from threading import Thread
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest: Guest | None = None


class Guest(Thread):
    def __init__(self, name: str):
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
                for table in filter(lambda table: table.guest == None, self.tables):
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    continue
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')


    def discuss_guests(self, ):
        pass