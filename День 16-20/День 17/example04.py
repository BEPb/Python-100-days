"""
Python 3.9
Жадный метод: решая проблему, всегда делайте лучший выбор в текущем представлении,
Не ищите оптимального решения, быстро найдите удовлетворительное решение.
Название файла 'example04.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-18
"""
class Thing(object):
    """вещь"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """Соотношение цены и веса"""
        return self.price / self.weight


def input_thing():
    """Введите информацию о товаре"""
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


def main():
    """Основная функция"""
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'вор взял{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'Общее значение: {total_price}рублей')


if __name__ == '__main__':
    main()
