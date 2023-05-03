'''
Python 3.10 Пример применения модуля с ранее созданными классами сотрудниками завода
Название файла 'example13.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-05-03
'''
from example01 import EmployeeFactory


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
