"""
Несколько потоков разделяют блокировки данных

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

import time
import threading


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = threading.Lock()

    def deposit(self, money):
        # Код может продолжить выполнение после получения блокировки
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            time.sleep(0.01)
            self._balance = new_balance
        finally:
            # После завершения операции не забудьте снять блокировку
            self._lock.release()

    @property
    def balance(self):
        return self._balance


if __name__ == '__main__':
    account = Account()
    # Создайте 100 потоков депозита для внесения денег на тот же счет
    for _ in range(100):
        threading.Thread(target=account.deposit, args=(1,)).start()
    # Дождитесь выполнения всех потоков депозита
    time.sleep(2)
    print('账户余额为: ￥%d元' % account.balance)

# Подумайте, почему результат не те 100 юаней, которые мы ожидали
