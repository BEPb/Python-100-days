"""
Python 3.9 Несколько потоков обмениваются данными без блокировки
Название файла '05.многопоточная_работа.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""

from time import sleep  # подключаем модуль работы со временем
from threading import Thread, Lock  # подключаем модуль многопоточной работы


class Account(object):  # создаем класс

    def __init__(self):  # инициализация класса
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):  # метод депозит (на входе сумма денег)
        # Получить блокировку перед выполнением последующего кода
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # Этот код помещается наконец, чтобы гарантировать, что операция снятия блокировки должна быть выполнена
            self._lock.release()

    @property  # спец.метод (свойство) геттер или аксессор (устанавливает значение из вне класса)
    def balance(self):  # метод имени (т.е. при обращении к методу имени - вы получите значение этого атрибута)
        return self._balance  # возвращает значение атрибута имени


class AddMoneyThread(Thread):  # создаем класс

    def __init__(self, account, money):  # инициализация класса (на входе аргументы имя аккаунта и количество денег)
        super().__init__()
        self._account = account  # создаем атрибут равный аргументу аккаунта
        self._money = money  # создаем атрибут равный аргументу денег

    def run(self):  # метод выполнение перевода
        self._account.deposit(self._money)


def main():  # главная функция
    account = Account()  # создаем объект класса аккаунт
    threads = []  # создаем пустой список
    # Создаем 100 потоков депозита для внесения денег на тот же счет
    for _ in range(100):  # в диапазоне от 1 до 100
        t = AddMoneyThread(account, 1)  # создаем объект класса процесс добавить деньги (передаем имя акк, 1 рубль)
        threads.append(t)
        t.start()  # запускаем процесс
    # Дождитесь выполнения всех потоков депозита
    for t in threads:  # цикл перечисления всех потоков
        t.join()  # ожидает выполнение потока
    print('Щет пополнен, текущий баланс составляет: %d рублей' % account.balance)


if __name__ == '__main__':  # проверка основной программы
    main()  # запуск главной функции
