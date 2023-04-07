"""
Выведите 10 строк треугольника Ян Хуэя - n-го коэффициента расширения двучлена.
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
... ... ...


Название файла '05.треугольник_Ян_Хуэя.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-03-04
"""


def main():  # главная функция
    num = int(input('Введите число строк: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':  # если запускаемая программа - эта (имя запущенной программы соответствует этой программе)
    main()  # то выполняем главную функцию
