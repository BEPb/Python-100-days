"""
Python 3.10 расширенные возможности функции
Название файла '01.калькулятор.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-05-03
"""

'''Функция которая на входе принимает действие и две переменные'''
def calculator(operation, x, y):
    if operation == "add":
        return x+y
    elif operation == "subtract":
        return x-y
    elif operation == "multiply":
        return x*y
    elif operation == "divide":
        return x/y

def square(x):
    return x ** 2

result = calculator("multiply", 5, 6)
print(result)  # Выведет 30 = 5*6
print(square(5))  # Выведет 25 = 5*5
print(calculator(square, 5, 5))  # None
print(calculator("divide", square(10), 5))  # 20.0 =((10*10)/5)


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]