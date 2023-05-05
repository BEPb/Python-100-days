"""
Python 3.10 Метакласс
Название файла 'example04.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-05-05
"""
import threading



class SingletonMeta(type):
    """Пользовательский метакласс
    Этот код описывает пользовательский метакласс `SingletonMeta`, который реализует паттерн Singleton - паттерн,
    гарантирующий, что у класса может быть только один экземпляр.

    В методе `__init__` метакласса `SingletonMeta` задаются два атрибута для класса: `__instance` и `lock`. Первый
    атрибут будет использоваться для хранения единственного экземпляра класса, а второй атрибут - для контроля доступа к
    созданию экземпляра класса в многопоточной среде.

    Метод `__call__` метакласса `SingletonMeta` обрабатывает попытки создания экземпляра класса. Если экземпляр класса
    еще не создан, то используется блокировка `lock` для предотвращения создания нескольких экземпляров одновременно.
    Если экземпляр уже создан, то метод возвращает его.

    Применение метакласса `SingletonMeta` к классу позволит создать класс-синглтон - класс, который будет создаваться
    только один раз в приложении.
    """

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
