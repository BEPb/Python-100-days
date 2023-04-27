"""
Python 3.10
Пример генеративного (производного) создания
Название файла 'example01.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-27
"""
from math import log2, factorial
from matplotlib import pyplot
import numpy


def seq_search(items: list, elem) -> int:  # на входе получаем список и переменную
    """Последовательный поиск"""
    for index, item in enumerate(items):
        '''
        Если range() позволяет получить только индексы элементов списка, то enumerate() – сразу индекс элемента и его значение.
        Функция enumerate() применяется для так называемых итерируемых объектов (список относится к таковым) и создает 
        объект-генератор, который генерирует кортежи, состоящие из двух элементов – индекса элемента и самого элемента. 
        '''
        if elem == item:  # если переменная равна элементу списка
            return index  # то возвращает индекс в списке
    return -1  # иначе возвращает -1


def bin_search(items, elem):  # на входе получаем список и переменную
    """Двухточечный поиск"""
    start, end = 0, len(items) - 1  # извлекаем длину списка, получаем номера первого и последнего элементов в списке
    while start <= end:  # цикл выполняется до тех пор, пока старт меньше или равен концу списка
        mid = (start + end) // 2  # вычисляем номер среднего элемента
        if elem > items[mid]:  # если элемент больше значения среднего в списке, то
            start = mid + 1  # значение стартового индекса увеличиваем на единицу
        elif elem < items[mid]:  # если элемент меньше значения среднего в списке, то
            end = mid - 1  # значение конечного индекса уменьшаем на единицу
        else:
            return mid  # в противном случае возвращаем индекс среднего элемента
    return -1  # иначе возвращает -1


def main():
    """"" "Основная функция (ввод программы)" """""
    num = 6  # максимальное значение по оси х
    styles = ['r-.', 'g-*', 'b-o', 'y-x', 'c-^', 'm-+', 'k-d']
    legends = ['логарифм', 'линейный', 'линейный логарифм', 'квадрат', 'кубический', 'геометрический ряд', 'факториал']
    x_data = [x for x in range(1, num + 1)]  # установим список значений по оси х от 1 до 6
    y_data1 = [log2(y) for y in range(1, num + 1)]  # вычисление двоичного логарифма у=log2(х)
    y_data2 = [y for y in range(1, num + 1)]  # вычисление линейной функции у=х
    y_data3 = [y * log2(y) for y in range(1, num + 1)]  # у=х*log2(х)
    y_data4 = [y ** 2 for y in range(1, num + 1)]  # у=х**2
    y_data5 = [y ** 3 for y in range(1, num + 1)]  # у=х**3
    y_data6 = [3 ** y for y in range(1, num + 1)]  # у=3**х
    y_data7 = [factorial(y) for y in range(1, num + 1)]  # у=factorial(х)

    y_datas = [y_data1, y_data2, y_data3, y_data4, y_data5, y_data6, y_data7]  # объединим все наши функции в список

    '''выведем на график все наши функции'''
    for index, y_data in enumerate(y_datas):
        pyplot.plot(x_data, y_data, styles[index])
    pyplot.legend(legends)
    pyplot.xticks(numpy.arange(1, 7, step=1))
    pyplot.yticks(numpy.arange(0, 751, step=50))
    pyplot.show()


if __name__ == '__main__':
    main()
