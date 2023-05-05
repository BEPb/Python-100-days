- Расширенные объектно-ориентированные знания - «Три столпа» / Взаимосвязь между классами / Сборка мусора / 
  Магические свойства и методы / Смешивание / Метаклассы / Принципы объектно-ориентированного дизайна / Шаблон 
  проектирования GoF 

### Расширенные объектно-ориентированные знания (день 18)

### Три столпа: инкапсуляция, наследование, полиморфизм

Инкапсуляция, наследование и полиморфизм - это три основных принципа объектно-ориентированного программирования. 
Рассмотрим примеры этих принципов на языке Python. 

#### Инкапсуляция

Инкапсуляция - это принцип, который предписывает скрывать сложность кода и предоставлять доступ только к необходимым 
свойствам и методам класса. Вот пример: 

```python
class Car:
    def __init__(self, make, model, color):
        self.__make = make
        self.__model = model
        self.__color = color

    def drive(self):
        print("Driving...")

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_color(self):
        return self.__color

car = Car("Honda", "Civic", "red")
print(car.get_make()) # "Honda"
print(car.get_model()) # "Civic"
```

В этом примере мы определили класс Car, который имеет атрибуты make, model и color и методы drive, get_make, 
get_model и get_color. Мы также определили эти атрибуты как приватные (__make, __model и __color), что означает, что 
они не могут быть изменены непосредственно извне класса. Вместо этого мы предоставляем только методы получения 
доступа к этим атрибутам, которые позволяют получать значения этих атрибутов.   

#### Наследование

Наследование - это принцип, который позволяет создавать классы на основе уже существующих классов с добавлением 
новых свойств и методов или переопределением уже существующих методов. Вот пример: 

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Meow!")

dog = Dog("Spot")
cat = Cat("Whiskers")

dog.make_sound() # "Woof!"
cat.make_sound() # "Meow!"
```

В этом примере мы определили класс Animal с методом make_sound и два класса, Dog и Cat, которые наследуются от 
класса Animal. Когда мы вызываем метод make_sound на экземпляре класса Dog или Cat, мы получаем разные звуки - "Woof!
" или "Meow!" - в зависимости от типа животного.   

Пример:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, id_number):
        super().__init__(name, age)
        self.id_number = id_number

student = Student("John", 20, 12345)
print(student.name)
print(student.age)
print(student.id_number)
```

Результат:
```commandline
John
20
12345
```


#### Полиморфизм

Полиморфизм - это принцип, который позволяет использовать объекты разных классов с одинаковыми интерфейсами. Вот 
пример: 

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Meow!")

def make_animal_sound(animal):
    animal.make_sound()

dog = Dog("Spot")
cat = Cat("Whiskers")

make_animal_sound(dog) # "Woof!"
make_animal_sound(cat) # "Meow!"
```

В этом примере мы определили класс Animal с методом make_sound и два класса, Dog и Cat, которые наследуются от 
класса Animal и переопределяют метод make_sound. У нас также есть функция make_animal_sound, которая принимает 
экземпляр класса Animal и вызывает его метод make_sound. Когда мы вызываем эту функцию с экземплярами классов Dog и 
Cat, мы получаем разные звуки - "Woof!" или "Meow!" - но это не имеет значения для функции make_animal_sound, потому 
что она просто вызывает метод make_sound, который ожидается у любого экземпляра класса Animal. Это и есть пример 
полиморфизма.     




пример: система расчетов заработной платы.

```Python
  """
Python 3.10 ежемесячная система расчетов заработной платы - менеджер отдела 15000 программистов в месяц 200 продавцов 1800 нижней заработной платы плюс 5% увеличение продаж
пример ООП: инкапсуляция, наследование, полиморфизм
в этом примере мы создаем различные классы, в следующем примере мы их применяем (создаем экземпляры классов)
Название файла '01.Factory.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-05-03
"""
from abc import ABCMeta, abstractmethod

'''создадим сначала мета класс сотрудника, который имеет имя и зарплату без указания конкретных значений'''
class Employee(metaclass=ABCMeta):
    """сотрудник (абстрактный класс)"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """расчет ежемесячной заработной платы (абстрактный метод)"""
        pass

'''создадим класс менеджера отдела, который наследутся от класса сотрудник, и переопределим его зарплату в 15000'''
class Manager(Employee):
    """Менеджер отдела"""

    def get_salary(self):
        return 15000.0

'''создадим класс программиста отдела, который наследутся от класса сотрудник, и переопределим его зарплату, 
которая зависит от количества часов его работы, за каждый час 200'''
class Programmer(Employee):
    """Программист отдела"""

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour

'''создадим класс продавец, который наследутся от класса сотрудник, и переопределим его зарплату, 
которая зависит от количества проданных товаров'''
class Salesman(Employee):
    """продавец"""

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05

'''На основании ранее созданных классов сотрудников создадим класс завода, который и будут использывать бухгалтерия 
при расчете заработной платы сотрудников, при этом для ускорения создания, начисления з.п. по профессии будет 
указываться только первый символ этой профессии'''
class EmployeeFactory():
    """создание фабрики сотрудников (заводской режим)"""

    @staticmethod
    def create(emp_type, *args, **kwargs):
        """создать сотрудника"""
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp

```

```python
'''
Python 3.10 Пример применения модуля с ранее созданными классами сотрудниками завода
Название файла 'example13.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-05-03
'''
from example01 import EmployeeFactory


def main():
    """основная функция"""
    emps = [
        EmployeeFactory.create('M', 'тюлень'),
        EmployeeFactory.create('P', 'олень', 120),
        EmployeeFactory.create('P', 'заяц', 85),
        EmployeeFactory.create('S', 'волк', 123000),
    ]
    for emp in emps:
        print('%s: %.2f' % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()

```


- связь между классом и классом

    отношение is-a: наследование
    связь has-a: ассоциация/агрегация/композиция
    отношение use-a: зависимость

пример: игра в покер.

```Python
"""
Python 3.10 Игра в покер
Объектно-ориентированный
Название файла 'example03.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-05-05
"""
from enum import Enum, unique
import random


@unique
class Suite(Enum):
    """перечисление"""
    SPADE, HEART, CLUB, DIAMOND = range(4)

    def __lt__(self, other):
        return self.value < other.value

class Card():
    """Необычные (перечисление)"""
    
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        suites = ('♠️', '♥️', '♣️', '♦️')
        faces = ('', 'A', '2', '3', '4', '5', '6', 
                 '7', '8', '9', '10', 'J', 'Q', 'K')
        return f'{suites[self.suite.value]} {faces[self.face]}'


class Poker():
    """покер"""
    
    def __init__(self):
        self.index = 0
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]

    def shuffle(self):
        """Перемешать"""
        self.index = 0
        random.shuffle(self.cards)

    def deal(self):
        """Лицензирование"""
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        """Есть еще карточки?"""
        return self.index < len(self.cards)

class Player():
    """Игрок"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_card(self, card):
        """Коснитесь карты"""
        self.cards.append(card)

    def arrange(self):
        """Разложите карты в руке"""
        self.cards.sort(key=lambda card: (card.suite, card.face))


def main():
    """Основная функция"""
    poker = Poker()
    poker.shuffle()
    players = [
        Player('Игрок 1'), Player('Игрок 2'),
        Player('Игрок 3'), Player('Игрок 4')
    ]
    while poker.has_more:
        for player in players:
            player.get_card(poker.deal())
    for player in players:
        player.arrange()
        print(player.name, end=': ')
        print(player.cards)

if __name__ == '__main__':
    main()

```

> **Примечание**. В приведенном выше коде символы эмодзи используются для обозначения четырех мастей игральных карт, 
> которые могут не отображаться в некоторых системах, не поддерживающих символы эмодзи. 

- Дублирование объектов (глубокое копирование/глубокое копирование/глубокое клонирование и поверхностное 
  копирование/поверхностное копирование/теневое клонирование) 

- Сборка мусора, круговые и слабые ссылки

   Python использует автоматическое управление памятью, основанное на **подсчете ссылок**, а также вводит стратегии, 
  дополненные двумя механизмами: **маркировка-очистка** и **коллекция поколений**. 
  ```Python
  # 循环引用会导致内存泄露 - Python除了引用技术还引入了标记清理和分代回收
  # 在Python 3.6以前如果重写__del__魔术方法会导致循环引用处理失效
  # 如果不想造成循环引用可以使用弱引用
  list1 = []
  list2 = [] 
  list1.append(list2)
  list2.append(list1)
  ```

 - сборка мусора может быть вызвана следующими ситуациями:

    вызовgc.collect()
    gcсчетчик модуля достигает порогового значения
    программа завершает работу

Если оба объекта в циклической ссылке определяют методы, модуль не уничтожает недостижимые объекты, поскольку модуль gc не знает, какой объект следует вызывать первым, и эта проблема устранена в Python 3.6.__del__gc__del__

можно также решить проблему циклических ссылок, создав слабые ссылки с помощью модулей.weakref

- 

Магические атрибуты и методы (см. Руководство по магическим методам Python)

есть несколько небольших вопросов, которые вы можете рассмотреть:

    могут ли пользовательские объекты использовать операторы для операций?
    могут ли пользовательские объекты быть помещены в? не могли бы вы пойти тяжелым?set
    может ли пользовательский объект выступать в качестве ключа?dict
    могут ли пользовательские объекты использовать контекстный синтаксис?

Mixin

пример: пользовательские ограничения словаря могут задавать пары значений ключей в словаре только в том случае, если 
указанный ключ не существует. 
  ```Python
  class SetOnceMappingMixin:
      """自定义混入类"""
      __slots__ = ()
  
      def __setitem__(self, key, value):
          if key in self:
              raise KeyError(str(key) + ' already set')
          return super().__setitem__(key, value)
  
  
  class SetOnceDict(SetOnceMappingMixin, dict):
      """自定义字典"""
      pass
  
  
  my_dict= SetOnceDict()
  try:
      my_dict['username'] = 'jackfrued'
      my_dict['username'] = 'hellokitty'
  except KeyError:
      pass
  print(my_dict)
  ```

- метапрограммирование и метаклассы

объект создается через класс, а класс — через метакласс, который предоставляет метаинформацию для создания класса. 
все классы прямо или косвенно наследуются, а все метаклассы прямо или косвенно наследуются.objecttype 

пример: реализация одноэлементного шаблона с метаклассом.

  ```Python
  import threading
  
  
  class SingletonMeta(type):
      """自定义元类"""
  
      def __init__(cls, *args, **kwargs):
          cls.__instance = None
          cls.__lock = threading.RLock()
          super().__init__(*args, **kwargs)
  
      def __call__(cls, *args, **kwargs):
          if cls.__instance is None:
              with cls.__lock:
                  if cls.__instance is None:
                      cls.__instance = super().__call__(*args, **kwargs)
          return cls.__instance
  
  
  class President(metaclass=SingletonMeta):
      """总统(单例类)"""
      
      pass
  ```

###	ОБЪЕКТНО-ОРИЕНТИРОВАННЫЕ ПРИНЦИПЫ ПРОЕКТИРОВАНИЯ: ПРИНЦИПЫ SOLID
###	Объектно-ориентированный режим проектирования: режим проектирования GoF (один случай, фабрика, агент, политика, итератор)

принципы объектно-ориентированного проектирования

    Принцип единой ответственности(SRP) - класс делает только то, что он должен делать (классы предназначены для высокой сплоченности)
    Принцип открытия и закрытия(OCP) - Сущность программного обеспечения должна закрыть разработку расширений для изменений
    ПРИНЦИП ИНВЕРСИИ ЗАВИСИМОСТЕЙ (DIP) - АБСТРАКТНОЕ ПРОГРАММИРОВАНИЕ (ОСЛАБЛЕНО В СЛАБО ТИПИЗИРОВАННЫХ ЯЗЫКАХ)
    Принцип замены Рихтера(LSP) - родительский объект может быть заменен дочерним объектом в любое время
    Принцип изоляции интерфейса(ISP) - Интерфейс должен быть небольшим, но не большим и полным (концепция отсутствия интерфейса в Python)
    ПРИНЦИП ПОВТОРНОГО ИСПОЛЬЗОВАНИЯ СИНТЕТИЧЕСКИХ АГРЕГАТОВ (CARP) — ПРЕДПОЧТЕНИЕ ОТДАЕТСЯ КОДУ ПОВТОРНОГО ИСПОЛЬЗОВАНИЯ СИЛЬНЫХ СВЯЗЕЙ, А НЕ НАСЛЕДОВАНИЮ ОТНОШЕНИЙ
    Принцип наименьших знаний (закон Димита, LoD)- не отправляйте сообщения людям, которые не обязательно связаны

    


  > Описание: Полужирные буквы выше вместе называются объектно-ориентированными принципами SOLID.
。

- Режим проектирования GoF

    режим создания: один случай, завод, строитель, прототип
    структурный режим: адаптер, фасад (внешний вид), прокси
    поведенческие шаблоны: итераторы, наблюдатели, состояния, политики

пример: подключаемый хэш-алгоритм (режим политики).

  ```Python
  class StreamHasher():
      """哈希摘要生成器"""
  
      def __init__(self, alg='md5', size=4096):
          self.size = size
          alg = alg.lower()
          self.hasher = getattr(__import__('hashlib'), alg.lower())()
  
      def __call__(self, stream):
          return self.to_digest(stream)
  
      def to_digest(self, stream):
          """生成十六进制形式的摘要"""
          for buf in iter(lambda: stream.read(self.size), b''):
              self.hasher.update(buf)
          return self.hasher.hexdigest()
  
  def main():
      """主函数"""
      hasher1 = StreamHasher()
      with open('Python-3.7.6.tgz', 'rb') as stream:
          print(hasher1.to_digest(stream))
      hasher2 = StreamHasher('sha1')
      with open('Python-3.7.6.tgz', 'rb') as stream:
          print(hasher2(stream))
  
  
  if __name__ == '__main__':
      main()
  ```

[Вернуться на главную](https://github.com/BEPb/Python-100-days)

[К следующему занятию](https://github.com/BEPb/Python-100-days/blob/master/%D0%94%D0%B5%D0%BD%D1%8C%2016-20/%D0%94%D0%B5%D0%BD%D1%8C%2019/README.md)
