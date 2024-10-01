import random
from threading import Lock, Thread
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

    def take(self):
        for _ in range(100):
            value_take = random.randrange(50, 100)
            print(f'Запрос на {value_take}')
            if value_take <= self.balance:
                self.balance -= value_take
                print(f'Снятие: {value_take}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


# TESTS

bank = Bank()

deposit = Thread(target=bank.deposit)
take = Thread(target=bank.take)

deposit.start()
take.start()

deposit.join()
take.join()

print(f'Итоговый баланс: {bank.balance}')