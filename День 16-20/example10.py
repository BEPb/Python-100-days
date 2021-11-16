"""
декоратор декоративного класса - одноэлементный режим - класс может создавать только уникальные объекты
	контекстный синтаксис:
	__enter__ / __exit__
"""
import threading

from functools import wraps


def singleton(cls):
    """один случай декоратора"""
    instances = {}
    lock = threading.Lock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class President():

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f'{self.country}: {self.name}'


def main():
    print(President.__name__)
    p1 = President('Путин', 'Россия')
    p2 = President('Медведев', 'Россия')
    print(p1 == p2)
    print(p1)
    print(p2)


if __name__ == '__main__':
    main()
