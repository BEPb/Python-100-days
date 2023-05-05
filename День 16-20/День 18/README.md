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

Полиморфизм - это один из принципов объектно-ориентированного программирования, который позволяет объектам класса 
иметь несколько форм. Это означает, что объект класса может проявлять различное поведение в зависимости от контекста,
в котором он используется.    

В программировании это достигается различными способами, например, через наследование, интерфейсы, абстрактные 
классы и перегрузку функций. При использовании полиморфизма объекты могут представлять собой экземпляры одного 
класса или разных классов, но они могут быть использованы одинаково в соответствующих контекстах. Это увеличивает 
гибкость и расширяемость программного кода и упрощает его сопровождение.    

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

### Взаимосвязь между классами

В Python классы могут быть связаны друг с другом через наследование, композицию или агрегацию. 

1) Наследование - это когда один класс наследует свойства и методы от другого класса. Например:

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def bark(self):
        print("Woof!")
```

Класс `Dog` наследует от класса `Animal` свойства `name` и `species`, и может иметь свои собственные методы, такие 
как `bark()`.  

2) Композиция - это когда один класс содержит экземпляры другого класса в качестве своих свойств. Например:

```python
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
class Company:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.employees = []
        
    def add_employee(self, person):
        self.employees.append(person)
```

Класс `Company` содержит экземпляры `Person` в виде свойства `employees`.

3) Агрегация - это когда один класс содержит экземпляры другого класса в виде своих свойств, но эти экземпляры могут 
   быть использованы и другими классами. Например: 

```python
class Guitar:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
class Band:
    def __init__(self, name):
        self.name = name
        self.guitarists = []
        
    def add_guitarist(self, guitarist):
        self.guitarists.append(guitarist)
```

Класс `Band` содержит экземпляры `Guitar` в виде свойства `guitarists`, и эти экземпляры могут быть использованы 
другими классами, такими как `Musician` или `Concert`.  

Это лишь некоторые примеры взаимосвязи между классами в Python. В зависимости от задачи, могут быть использованы и 
другие типы связей между классами. 

### Сборка мусора

В Python есть встроенная функция `garbage collection` (сборка мусора), которая автоматически удалит объекты, которые 
больше не используются в программе. Сборка мусора производится интерпретатором Python, поэтому программисту не нужно 
заботиться о освобождении памяти.   

Ниже приведены примеры использования сборки мусора в Python:

1. Пример использования `del` для удаления объектов:

```python
a = [1, 2, 3]
del a # удаление переменной a из памяти
```

2. Пример использования `gc.collect()` для явного вызова сборщика мусора:

```python
import gc

a = [1, 2, 3]
b = [4, 5, 6]
a.append(b) # создание ссылки на объект b
del a, b # удаление переменных a и b из памяти

gc.collect() # явный вызов сборщика мусора
```

3. Пример использования `gc.get_objects()` для получения списка всех объектов в памяти:

```python
import gc

a = [1, 2, 3]
b = [4, 5, 6]
a.append(b) # создание ссылки на объект b

objects = gc.get_objects() # список всех объектов в памяти
print(len(objects)) # количество объектов в памяти

del a, b # удаление переменных a и b из памяти
gc.collect() # явный вызов сборщика мусора
objects = gc.get_objects() # список всех объектов в памяти
print(len(objects)) # количество объектов в памяти после вызова сборщика мусора
```

Все эти примеры показывают, как можно использовать сборку мусора в Python для освобождения памяти и уменьшения 
потребления ресурсов. Однако, как уже упоминалось, Python автоматически заботится о сборке мусора, поэтому как 
правило, нет необходимости явно вызывать эту функцию в большинстве случаев.  

### Магические свойства и методы

Python - мощный язык программирования, который позволяет использовать множество магических методов и свойств. 
Магические методы - это методы в Python, которые начинаются и заканчиваются символом подчеркивания (_). Они 
позволяют использовать операции, такие как сложение, вычитание и доступ к элементам объекта в одной строке кода. 
Ниже приведены некоторые магические методы и свойства Python, используемые для разных целей:   

1. `__init__(self, args)` - магический метод инициализации, который вызывается при создании нового экземпляра 
   объекта. Он инициализирует все переменные и свойства объекта.  

```python
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = MyClass(3, 5)
```

2. `__str__(self)` - магический метод, который вызывается при попытке преобразовать объект в строку. Он возвращает 
   строковое представление объекта.  

```python
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "MyClass: ({}, {})".format(self.x, self.y)

obj = MyClass(3, 5)
print(obj) # выводит строку "MyClass: (3, 5)"
```

3. `__len__(self)` - магический метод, который возвращает длину объекта. Этот метод используется для объектов, 
   которые поддерживают операции индексации (например, списки, кортежи).  

```python
my_list = [1, 2, 3, 4, 5]
print(len(my_list)) # выводит 5
```

4. `__getitem__(self, index)` - магический метод, который возвращает элемент объекта по заданному индексу. 

```python
my_list = [1, 2, 3, 4, 5]
print(my_list[2]) # выводит 3
```

5. `__setitem__(self, index, value)` - магический метод, который устанавливает значение элемента объекта по 
   заданному индексу.  

```python
my_list = [1, 2, 3, 4, 5]
my_list[2] = 7
print(my_list) # выводит [1, 2, 7, 4, 5]
```

6. `__add__(self, other)` - магический метод, который позволяет выполнить операцию сложения (+) между двумя объектами. 

```python
class MyClass:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return MyClass(self.x + other.x)

obj1 = MyClass(3)
obj2 = MyClass(5)
obj3 = obj1 + obj2
print(obj3.x) # выводит 8
```

7. `__sub__(self, other)` - магический метод, который позволяет выполнить операцию вычитания (-) между двумя объектами. 

```python
class MyClass:
    def __init__(self, x):
        self.x = x

    def __sub__(self, other):
        return MyClass(self.x - other.x)

obj1 = MyClass(8)
obj2 = MyClass(3)
obj3 = obj1 - obj2
print(obj3.x) # выводит 5
```

8. `__eq__(self, other)` - магический метод, который проверяет, равны ли два объекта. 

```python
class MyClass:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        if isinstance(other, MyClass):
            return self.x == other.x
        return False

obj1 = MyClass(3)
obj2 = MyClass(3)
print(obj1 == obj2) # выводит True
```

Это лишь некоторые из магических методов и свойств Python, которые могут сделать код более компактным и более 
удобным для использования. Зная их, разработчики могут написать более эффективный код и более быстро отлаживать 
программы.  

### Метапрограммирование и метаклассы

Метапрограммирование - это процесс создания программ, которые могут генерировать другие программы во время своего 
выполнения. В программировании оно используется для автоматической генерации кода и облегчения разработки. 

Метаклассы - это классы, которые создают другие классы. Они являются объектами, которые управляют созданием и 
поведением других классов. Метаклассы позволяют динамически создавать классы, добавлять и изменять методы классов, а 
также добавлять и изменять атрибуты и другие свойства классов. Они широко используются в различных фреймворках и 
библиотеках на языке Python.   

Объект создается через класс, а класс — через метакласс, который предоставляет метаинформацию для создания класса. 

Пример: реализация одноэлементного шаблона с метаклассом.

```Python
"""
Python 3.10 Метакласс
Название файла 'example04.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-05-05
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
```
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


###	ОБЪЕКТНО-ОРИЕНТИРОВАННЫЕ ПРИНЦИПЫ ПРОЕКТИРОВАНИЯ: ПРИНЦИПЫ SOLID

Принципы SOLID - это набор основных принципов объектно-ориентированного программирования, созданный Робертом 
Мартином. SOLID - это аббревиатура, которая означает: 

- Принцип единственной ответственности (Single Responsibility Principle, SRP)
- Принцип открытости/закрытости (Open/Closed Principle, OCP)
- Принцип подстановки Барбары Лисков (Liskov Substitution Principle, LSP)
- Принцип разделения интерфейса (Interface Segregation Principle, ISP)
- Принцип инверсии зависимостей (Dependency Inversion Principle, DIP)

Принцип SRP гласит, что каждый класс должен отвечать только за одну задачу. Принцип OCP заключается в том, чтобы 
программный код был открыт для расширения, но закрыт для изменений. Принцип LSP говорит о том, что любой экземпляр 
базового класса должен полностью заменяться экземпляром производного класса без изменения свойств той системы, в 
которой он используется. Принцип ISP утверждает, что клиенты не должны зависеть от методов, которые им не нужны. 
Принцип DIP гласит, что зависимости между модулями должны строиться на основе абстракций, а не на основе конкретных 
реализаций.      

Соблюдение принципов SOLID помогает создавать код, который легко поддерживать и расширять в будущем, а также 
улучшает его производительность и разработку. 

###	Объектно-ориентированный режим проектирования: режим проектирования GoF
Группа авторов, известная как GoF (Gang of Four), в 1994 году описала 23 шаблона проектирования программного 
обеспечения в своей книге "Design Patterns: Elements of Reusable Object-Oriented Software". Эти шаблоны, также 
называемые "шаблонами GoF", классифицируются на три типа: шаблоны создания (Creational), шаблоны структуры 
(Structural) и шаблоны поведения (Behavioral).   

Шаблоны создания предоставляют решения для создания объектов и гарантируют, что приложение правильно создает и 
настраивает объекты. Примеры шаблонов создания включают Singleton, Factory Method и Abstract Factory. 

Шаблоны структуры предоставляют решения для компоновки классов и объектов в более крупные структуры. Эти шаблоны 
позволяют избежать структурной запутанности и сделать проект более унифицированным и легким для понимания. Примеры 
шаблонов структуры это Proxy, Decorator и Adapter.  

Шаблоны поведения предоставляют решения для управления взаимодействием между объектами и улучшения их связи. Примеры 
шаблонов поведения включают Observer, Command и Strategy. 

Шаблоны GoF помогают разработчикам улучшить качество кода и повысить его поддерживаемость. Они позволяют сократить 
время разработки, упростить понимание функциональности и улучшить общее качество проекта. 

Примеры:
- example01.py
- example02.py
- example03.py
- example04.py



[Вернуться на главную](https://github.com/BEPb/Python-100-days)

[К следующему занятию](https://github.com/BEPb/Python-100-days/blob/master/%D0%94%D0%B5%D0%BD%D1%8C%2016-20/%D0%94%D0%B5%D0%BD%D1%8C%2019/README.md)
