"""
объектно-ориентированные три столпа: инкапсуляция, наследование, полиморфизм
	ОБЪЕКТНО-ОРИЕНТИРОВАННЫЕ ПРИНЦИПЫ ПРОЕКТИРОВАНИЯ: ПРИНЦИПЫ SOLID
	Объектно-ориентированный режим проектирования: режим проектирования GoF (один случай, фабрика, агент, политика, итератор)
	ежемесячная система расчетов заработной платы - менеджер отдела 15000 программистов в месяц 200 продавцов 1800 нижней заработной платы плюс 5% увеличение продаж

"""
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """сотрудник (абстрактный класс)"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """расчет ежемесячной заработной платы (абстрактный метод)"""
        pass


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """менеджер отдела"""

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Employee):
    """продавец"""

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory():
    """создание фабрики сотрудников (заводской режим - разъединение между потребителями объектов и объектами через фабрику)"""

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
