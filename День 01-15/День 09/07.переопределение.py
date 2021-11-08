"""
Python 3.9 Переопределение абстрактного класса / метода / полиморфизм
В компании, которая внедряет систему расчета заработной платы, есть три типа сотрудников.
-Месячная фиксированная заработная плата менеджера отдела составляет 12000 юаней в месяц.
-Программисты получают 100 юаней в час в зависимости от количества рабочих часов в месяц.
- Базовая зарплата продавца в размере 1500 юаней в месяц плюс 5% комиссионных с продаж в этом месяце.
Введите информацию о сотруднике и выведите информацию о ежемесячной заработной плате для каждого сотрудника
Название файла '07.переопределение.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-09
"""

from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):

    # Подумайте об этом: что произойдет, если вы не определите метод построения
    def __init__(self, name):
        # Подумайте: что произойдет, если вы не вызовете конструктор родительского класса
        super().__init__(name)

    def get_salary(self):
        return 12000


class Programmer(Employee):

    def __init__(self, name):
        super().__init__(name)

    def set_working_hour(self, working_hour):
        self._working_hour = working_hour

    def get_salary(self):
        return 100 * self._working_hour


class Salesman(Employee):

    def __init__(self, name):
        super().__init__(name)

    def set_sales(self, sales):
        self._sales = sales

    def get_salary(self):
        return 1500 + self._sales * 0.05


if __name__ == '__main__':
    emps = [Manager('Иван'), Programmer('Андрей'), Salesman('Женя')]
    for emp in emps:
        if isinstance(emp, Programmer):
            working_hour = int(input('Пожалуйста, введите время работы %s в этом месяце: ' % emp.name))
            emp.set_working_hour(working_hour)
        elif isinstance(emp, Salesman):
            sales = float(input('Введите %s продаж в этом месяце: ' % emp.name))
            emp.set_sales(sales)
        print('%sзарплата в этом месяце составляет: %.2fрублей' % (emp.name, emp.get_salary()))
