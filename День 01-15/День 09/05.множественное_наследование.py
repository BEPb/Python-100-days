"""
Python 3.9 Множественное наследование
-Бриллиантовое наследование (алмазное наследование)
-C3 алгоритм (алгоритм замены DFS)
Название файла '05.множественное_наследование.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-09
"""


class A(object):

    def foo(self):
        print('foo of A')


class B(A):
    pass


class C(A):

    def foo(self):
        print('foo fo C')


class D(B, C):
    pass


class E(D):

    def foo(self):
        print('foo in E')
        super().foo()
        super(B, self).foo()
        super(C, self).foo()


if __name__ == '__main__':
    d = D()
    d.foo()
    e = E()
    e.foo()
