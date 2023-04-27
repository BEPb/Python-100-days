"""
Python 3.9
Мета
Метаданные-данные, описывающие данные-метаданные
Метакласс - класс, описывающий метакласс класса, унаследованный от типа
Название файла 'example18.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-18
"""
import threading


class SingletonMeta(type):
    """Пользовательский метакласс"""

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.lock = threading.Lock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.lock:
                if cls.__instance is None:
                    cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President(metaclass=SingletonMeta):
    """Президент (одноэлементный класс)"""

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f'{self.country}: {self.name}'


def main():
    """Основная функция"""
    p1 = President('Путин', 'Россия')
    p2 = President('Медведев', 'Россия')
    p3 = President.__call__('Ельцин', 'Россия')
    print(p1 == p2)
    print(p1 == p3)
    print(p1, p2, p3, sep='\n')


if __name__ == '__main__':
    main()
