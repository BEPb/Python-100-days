"""
Несколько потоков обмениваются данными без блокировки

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

from time import sleep
from threading import Thread, Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # Получить блокировку перед выполнением последующего кода
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # Этот код помещается наконец, чтобы гарантировать, что операция снятия блокировки должна быть выполнена
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    # Создайте 100 потоков депозита для внесения денег на тот же счет
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # Дождитесь выполнения всех потоков депозита ∫
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()
