"""
Python 3.9 Несколько потоков обмениваются данными с блокировкой
Название файла '06.многопоточная_работа.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""

import time  # подключаем модуль работы со временем
import threading  # подключаем модуль многопоточной работы


class Account(object):  # создаем класс

    def __init__(self):  # инициализация класса
        self._balance = 0
        self._lock = threading.Lock()

    def deposit(self, money):  # метод депозит (на входе сумма денег)
        # Код может продолжить выполнение после получения блокировки
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            time.sleep(0.01)
            self._balance = new_balance
        finally:
            # После завершения операции не забудьте снять блокировку
            self._lock.release()

    @property  # спец.метод (свойство) геттер или аксессор (устанавливает значение из вне класса)
    def balance(self):  # метод имени (т.е. при обращении к методу имени - вы получите значение этого атрибута)
        return self._balance  # возвращает значение атрибута имени


if __name__ == '__main__':  # проверка основной программы
    account = Account()
    # Создайте 100 потоков депозита для внесения денег на тот же счет
    for _ in range(100):
        threading.Thread(target=account.deposit, args=(1,)).start()
    # Дождитесь выполнения всех потоков депозита
    time.sleep(2)
    print('Щет пополнен, текущий баланс составляет: %d рублей' % account.balance)


