"""
Преобразование 100-балльной системы в американскую систему оценок
90 баллов или более, выход A
80 баллов до 89 баллов, результат B
От 70 до 79 баллов, результат C
От 60 минут до 69 минут, выход D
Менее 60 баллов, вывод E

Название файла '02.перевод_оценок.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-03-04
"""

print("Программа перевода оценки из стобальной системы в американскую систему (A, B, C, D, E)")
score = float(input('Пожалуйста, введите оценку по стобальной системе: '))  # присваиваем переменной score значение
# оценки
if score >= 90:  # если полученной значение больше или равно 90
    grade = 'A'  # то выходная оценка (grade) равна А
elif score >= 80:  # иначе, если полученной значение больше или равно 80
    grade = 'B'  # то выходная оценка (grade) равна B
elif score >= 70:  # иначе, если полученной значение больше или равно 70
    grade = 'C'  # то выходная оценка (grade) равна C
elif score >= 60:  # иначе, если полученной значение больше или равно 60
    grade = 'D'  # то выходная оценка (grade) равна D
else:    # иначе
    grade = 'E'  # то выходная оценка (grade) равна E
print('Соответствующая оценка:', grade)  # выводим результат
