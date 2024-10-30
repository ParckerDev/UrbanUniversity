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
        super().__init__()
        self.name = name

    def run(self):
        sleep(random.randint(3, 15))


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
                    guest.join()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')


    def discuss_guests(self):
        while not self.queue.empty():
            #for table in self.tables:
            tables = filter(lambda x: x.guest != None, self.tables)
            for table in tables:
                if not table.guest.is_alive(): 
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)') 
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        table.guest.start()
                        table.guest.join()
                    else:
                        continue
                



# TESTS

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()