"""
Множественное наследование - класс имеет два или более родительских класса
Порядок разрешения метода ТОиР-порядок разрешения метода
Когда происходит наследование в форме ромба (наследование ромба), какой метод родительского класса наследуется подклассом
Python 2.x-поиск в глубину
Алгоритм Python 3.x-C3 аналогичен поиску в ширину
"""
class A():

    def say_hello(self):
        print('Hello, A')


class B(A):
    pass


class C(A):

    def say_hello(self):
        print('Hello, C')


class D(B, C):
    pass


class SetOnceMappingMixin():
    """Индивидуальный класс смешивания"""
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    """Пользовательский словарь"""
    pass


def main():
    print(D.mro())
    # print(D.__mro__)
    D().say_hello()
    print(SetOnceDict.__mro__)
    my_dict= SetOnceDict()
    my_dict['username'] = 'jackfrued'
    my_dict['username'] = 'hellokitty'


if __name__ == '__main__':
    main()
