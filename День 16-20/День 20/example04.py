"""
Python 3.10 Данный код является многопоточной программой, которая моделирует работу банковского счета. В
программе создается класс Account с методами, которые позволяют вносить и снимать деньги со счета. Для синхронизации
доступа к банковскому счету используется мьютекс (Lock).

В данной программе используется Condition. Класс Condition описывает условную переменную, которую потоки могут
использовать для ожидания определенных условий. Condition является расширенной версией блокировки, которая позволяет
потокам ожидать сигнала других потоков.

Таким образом, программа работает многопоточно и безопасно обрабатывает операции на банковском счете.
Название файла 'example04.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-18
"""
from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep

import threading


class Account():
    """Банковский счет"""

    def __init__(self, balance=0):
        self.balance = balance
        lock = threading.Lock()
        self.condition = threading.Condition(lock)

    def withdraw(self, money):
        """Снять деньги со счета"""
        with self.condition:
            while money > self.balance:
                self.condition.wait()
            new_balance = self.balance - money
            sleep(0.001)
            self.balance = new_balance

    def deposit(self, money):
        """Экономить деньги"""
        with self.condition:
            new_balance = self.balance + money
            sleep(0.001)
            self.balance = new_balance
            self.condition.notify_all()


def add_money(account):
    '''
    В функции add_money происходит внесение денег на счет. Функция генерирует случайное число (от 5 до 10) и добавляет
    его на счет. После этого функция выводит текущее состояние счета в консоль.
    '''
    while True:
        money = randint(5, 10)
        account.deposit(money)
        print(threading.current_thread().name,
              ':', money, '====>', account.balance)
        sleep(0.5)


def sub_money(account):
    '''
    В функции sub_money происходит снятие денег со счета. Функция генерирует случайное число (от 10 до 30) и пытается
    снять его со счета. Если счет не имеет достаточного количества денег, функция будет ждать пока не появятся новые
    деньги на счете. После снятия денег со счета функция выводит текущее состояние счета в консоль.
    '''
    while True:
        money = randint(10, 30)
        account.withdraw(money)
        print(threading.current_thread().name,
              ':', money, '<====', account.balance)
        sleep(1)


def main():
    '''
    В функции main создается объект класса Account и запускаются две функции add_money и sub_money в разных потоках.
    Количество потоков задается параметром max_workers при создании объекта ThreadPoolExecutor.
    '''
    account = Account()
    with ThreadPoolExecutor(max_workers=10) as pool:
        for _ in range(5):
            pool.submit(add_money, account)
            pool.submit(sub_money, account)


if __name__ == '__main__':
    main()
