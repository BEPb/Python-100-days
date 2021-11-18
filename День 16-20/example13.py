'''
Python 3.9
Название файла 'example13.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-18
'''
from example12 import EmployeeFactory


def main():
    """основная функция"""
    emps = [
        EmployeeFactory.create('M', 'тюлень'),
        EmployeeFactory.create('P', 'олень', 120),
        EmployeeFactory.create('P', 'заяц', 85),
        EmployeeFactory.create('S', 'волк', 123000),
    ]
    for emp in emps:
        print('%s: %.2f' % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
