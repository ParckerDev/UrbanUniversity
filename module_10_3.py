import random
from threading import Lock
from time import sleep


class Bank:
    def __init__(self):
        self.balance: int = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            value_deposit = random.randrange(50, 100)
            self.balance += value_deposit
            print(f'Пополнение: {value_deposit}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)