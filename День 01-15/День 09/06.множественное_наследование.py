"""
Множественное наследование
-С помощью множественного наследования вы можете предоставить класс объектов с множеством возможностей.
-Таким образом вы можете избежать создания слишком большого количества уровней сложных отношений наследования при разработке классов.
Название файла '06.множественное_наследование.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-09
"""


class Father(object):

    def __init__(self, name):
        self._name = name

    def gamble(self):
        print('%sиграет в карты.' % self._name)

    def eat(self):
        print('%sест и пьет.' % self._name)


class Monk(object):

    def __init__(self, name):
        self._name = name

    def eat(self):
        print('%sбыстро ест.' % self._name)

    def chant(self):
        print('%sпоет песни.' % self._name)


class Musician(object):

    def __init__(self, name):
        self._name = name

    def eat(self):
        print('%sмедленно жует.' % self._name)

    def play_piano(self):
        print('%sиграет на пианино.' % self._name)


# Попробуйте код ниже, чтобы увидеть разницу
# class Son(Monk, Father, Musician):
# class Son(Musician, Father, Monk):


class Son(Father, Monk, Musician):

    def __init__(self, name):
        Father.__init__(self, name)
        Monk.__init__(self, name)
        Musician.__init__(self, name)


son = Son('Король Кувалда')
son.gamble()
# Вызвать метод eat, унаследованный от отца
son.eat()
son.chant()
son.play_piano()
