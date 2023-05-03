"""
Python 3.10 ежемесячная система расчетов заработной платы - менеджер отдела 15000 программистов в месяц 200 продавцов 1800 нижней заработной платы плюс 5% увеличение продаж
пример ООП: инкапсуляция, наследование, полиморфизм
в этом примере мы создаем различные классы, в следующем примере мы их применяем (создаем экземпляры классов)
Название файла '01.Factory.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-05-03
"""
from abc import ABCMeta, abstractmethod

'''создадим сначала мета класс сотрудника, который имеет имя и зарплату без указания конкретных значений'''
class Employee(metaclass=ABCMeta):
    """сотрудник (абстрактный класс)"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """расчет ежемесячной заработной платы (абстрактный метод)"""
        pass

'''создадим класс менеджера отдела, который наследутся от класса сотрудник, и переопределим его зарплату в 15000'''
class Manager(Employee):
    """Менеджер отдела"""

    def get_salary(self):
        return 15000.0

'''создадим класс программиста отдела, который наследутся от класса сотрудник, и переопределим его зарплату, 
которая зависит от количества часов его работы, за каждый час 200'''
class Programmer(Employee):
    """Программист отдела"""

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour

'''создадим класс продавец, который наследутся от класса сотрудник, и переопределим его зарплату, 
которая зависит от количества проданных товаров'''
class Salesman(Employee):
    """продавец"""

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05

'''На основании ранее созданных классов сотрудников создадим класс завода, который и будут использывать бухгалтерия 
при расчете заработной платы сотрудников, при этом для ускорения создания, начисления з.п. по профессии будет 
указываться только первый символ этой профессии'''
class EmployeeFactory():
    """создание фабрики сотрудников (заводской режим)"""

    @staticmethod
    def create(emp_type, *args, **kwargs):
        """создать сотрудника"""
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp
