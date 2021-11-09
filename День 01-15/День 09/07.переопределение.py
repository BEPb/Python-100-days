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

from abc import ABCMeta, abstractmethod  # загрузка модулей работы с метаданными


class Employee(object, metaclass=ABCMeta):  # определяем класс, наследуем от метакласса

    def __init__(self, name):  # инициализируем класс
        self._name = name  # задаем значение атрибута, принятого от аргумента

    @property  # геттер
    def name(self):
        return self._name

    @abstractmethod  # геттер
    def get_salary(self):
        pass


class Manager(Employee):  # определяем класс, наследуем от класса Employee

    # Подумайте об этом: что произойдет, если вы не определите метод построения
    def __init__(self, name):  # инициализируем класс
        # Подумайте: что произойдет, если вы не вызовете конструктор родительского класса
        super().__init__(name)

    def get_salary(self):  # геттер
        return 12000


class Programmer(Employee):  # определяем класс, наследуем от класса Employee

    def __init__(self, name):  # инициализируем класс
        super().__init__(name)

    def set_working_hour(self, working_hour):
        self._working_hour = working_hour

    def get_salary(self):  # геттер
        return 100 * self._working_hour


class Salesman(Employee):  # определяем класс, наследуем от класса Employee

    def __init__(self, name):  # инициализируем класс
        super().__init__(name)

    def set_sales(self, sales):  # сеттер
        self._sales = sales

    def get_salary(self):  # геттер
        return 1500 + self._sales * 0.05


if __name__ == '__main__':  # если программа запущена как главная
    emps = [Manager('Иван'), Programmer('Андрей'), Salesman('Женя')]  # создаем список объектов
    for emp in emps:  # перебираем все объекты по списку
        if isinstance(emp, Programmer):  # если объект программист
            working_hour = int(input('Пожалуйста, введите время работы %s в этом месяце: ' % emp.name))
            emp.set_working_hour(working_hour)
        elif isinstance(emp, Salesman):  # если объект продавец
            sales = float(input('Введите %s продаж в этом месяце: ' % emp.name))
            emp.set_sales(sales)
        print('%s зарплата в этом месяце составляет: %.2f рублей' % (emp.name, emp.get_salary()))
