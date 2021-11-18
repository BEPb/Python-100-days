"""
Python 3.9
Поиск-последовательный поиск и бинарный поиск
Алгоритмы: методы решения проблемы (шаги)
Существует два основных показателя для оценки качества алгоритма: асимптотическая временная сложность и
асимптотическая пространственная сложность. Обычно алгоритму трудно достичь низкой временной сложности и пространственной сложности (поскольку время и пространство несовместимы) противоречие)
Указывает, что асимптотическая временная сложность обычно использует большой знак O
O (c): Постоянное время сложности - Хэш-хранилище / фильтр Блума
O (log_2 n): логарифмическая временная сложность-двоичный поиск
O (n): последовательный поиск с линейной временной сложностью
O (n * log_2 n): - Логарифмическая линейная временная сложность - Расширенные алгоритмы сортировки (сортировка слиянием, быстрая сортировка)
O (n ** 2): простой алгоритм сортировки с квадратной временной сложностью (пузырьковая сортировка, сортировка выбора, сортировка вставкой)
O (n ** 3): алгоритм Флойда с кубической временной сложностью / операция умножения матриц
Также известна как полиномиальная временная сложность
O (2 ** n): временная сложность геометрической прогрессии - Ханойская башня
O (3 ** n): временная сложность геометрической прогрессии
Также известна как экспоненциальная временная сложность
O (n!): Факторная временная сложность - проблема дилера в путешествии - NP
Название файла 'example01.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-18
"""
from math import log2, factorial
from matplotlib import pyplot

import numpy


def seq_search(items: list, elem) -> int:
    """Последовательный поиск"""
    for index, item in enumerate(items):
        if elem == item:
            return index
    return -1


def bin_search(items, elem):
    """Двухточечный поиск"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if elem > items[mid]:
            start = mid + 1
        elif elem < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


def main():
    """"" "Основная функция (ввод программы)" """""
    num = 6
    styles = ['r-.', 'g-*', 'b-o', 'y-x', 'c-^', 'm-+', 'k-d']
    legends = [ 'логарифм' , 'линейный' , 'линейный логарифм' , 'квадрат' , 'кубический' , 'геометрический ряд' , 'факториал']
    x_data = [x for x in range(1, num + 1)]
    y_data1 = [log2(y) for y in range(1, num + 1)]
    y_data2 = [y for y in range(1, num + 1)]
    y_data3 = [y * log2(y) for y in range(1, num + 1)]
    y_data4 = [y ** 2 for y in range(1, num + 1)]
    y_data5 = [y ** 3 for y in range(1, num + 1)]
    y_data6 = [3 ** y for y in range(1, num + 1)]
    y_data7 = [factorial(y) for y in range(1, num + 1)]
    y_datas = [y_data1, y_data2, y_data3, y_data4, y_data5, y_data6, y_data7]
    for index, y_data in enumerate(y_datas):
        pyplot.plot(x_data, y_data, styles[index])
    pyplot.legend(legends)
    pyplot.xticks(numpy.arange(1, 7, step=1))
    pyplot.yticks(numpy.arange(0, 751, step=50))
    pyplot.show()


if __name__ == '__main__':
    main()
