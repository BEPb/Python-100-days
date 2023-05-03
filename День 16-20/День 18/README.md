- Расширенные объектно-ориентированные знания - «Три столпа» / Взаимосвязь между классами / Сборка мусора / 
  Магические свойства и методы / Смешивание / Метаклассы / Принципы объектно-ориентированного дизайна / Шаблон 
  проектирования GoF 

### Расширенные объектно-ориентированные знания (день 18)

### объектно-ориентированные знания

- три столпа: инкапсуляция, наследование, полиморфизм

пример: система расчетов заработной платы.

  ```Python
  """
  月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
  """
  from abc import ABCMeta, abstractmethod
  
  
  class Employee(metaclass=ABCMeta):
      """员工(抽象类)"""
  
      def __init__(self, name):
          self.name = name
  
      @abstractmethod
      def get_salary(self):
          """结算月薪(抽象方法)"""
          pass
  
  
  class Manager(Employee):
      """部门经理"""
  
      def get_salary(self):
          return 15000.0
  
  
  class Programmer(Employee):
      """程序员"""
  
      def __init__(self, name, working_hour=0):
          self.working_hour = working_hour
          super().__init__(name)
  
      def get_salary(self):
          return 200.0 * self.working_hour
  
  
  class Salesman(Employee):
      """销售员"""
  
      def __init__(self, name, sales=0.0):
          self.sales = sales
          super().__init__(name)
  
      def get_salary(self):
          return 1800.0 + self.sales * 0.05
  
  
  class EmployeeFactory:
      """创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合）"""
  
      @staticmethod
      def create(emp_type, *args, **kwargs):
          """创建员工"""
          all_emp_types = {'M': Manager, 'P': Programmer, 'S': Salesman}
          cls = all_emp_types[emp_type.upper()]
          return cls(*args, **kwargs) if cls else None
  
  
  def main():
      """主函数"""
      emps = [
          EmployeeFactory.create('M', '曹操'), 
          EmployeeFactory.create('P', '荀彧', 120),
          EmployeeFactory.create('P', '郭嘉', 85), 
          EmployeeFactory.create('S', '典韦', 123000),
      ]
      for emp in emps:
          print(f'{emp.name}: {emp.get_salary():.2f}元')
  
  
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
  经验：符号常量总是优于字面常量，枚举类型是定义符号常量的最佳选择
  """
  from enum import Enum, unique
  
  import random
  
  
  @unique
  class Suite(Enum):
      """花色"""
  
      SPADE, HEART, CLUB, DIAMOND = range(4)
  
      def __lt__(self, other):
          return self.value < other.value
  
  
  class Card():
      """牌"""
  
      def __init__(self, suite, face):
          """初始化方法"""
          self.suite = suite
          self.face = face
  
      def show(self):
          """显示牌面"""
          suites = ['♠︎', '♥︎', '♣︎', '♦︎']
          faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
          return f'{suites[self.suite.value]}{faces[self.face]}'
  
      def __repr__(self):
          return self.show()
  
  
  class Poker():
      """扑克"""
  
      def __init__(self):
          self.index = 0
          self.cards = [Card(suite, face)
                        for suite in Suite
                        for face in range(1, 14)]
  
      def shuffle(self):
          """洗牌（随机乱序）"""
          random.shuffle(self.cards)
          self.index = 0
  
      def deal(self):
          """发牌"""
          card = self.cards[self.index]
          self.index += 1
          return card
  
      @property
      def has_more(self):
          return self.index < len(self.cards)
  
  
  class Player():
      """玩家"""
  
      def __init__(self, name):
          self.name = name
          self.cards = []
  
      def get_one(self, card):
          """摸一张牌"""
          self.cards.append(card)
  
      def sort(self, comp=lambda card: (card.suite, card.face)):
          """整理手上的牌"""
          self.cards.sort(key=comp)
  
  
  def main():
      """主函数"""
      poker = Poker()
      poker.shuffle()
      players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
      while poker.has_more:
          for player in players:
                  player.get_one(poker.deal())
      for player in players:
          player.sort()
          print(player.name, end=': ')
          print(player.cards)
  
  
  if __name__ == '__main__':
      main()
  ```

  > **说明**：上面的代码中使用了Emoji字符来表示扑克牌的四种花色，在某些不支持Emoji字符的系统上可能无法显示。

- 对象的复制（深复制/深拷贝/深度克隆和浅复制/浅拷贝/影子克隆）

- 垃圾回收、循环引用和弱引用

  Python使用了自动化内存管理，这种管理机制以**引用计数**为基础，同时也引入了**标记-清除**和**分代收集**两种机制为辅的策略。

  ```C
  typedef struct _object {
      /* 引用计数 */
      int ob_refcnt;
      /* 对象指针 */
      struct _typeobject *ob_type;
  } PyObject;
  ```

  ```C
  /* 增加引用计数的宏定义 */
  #define Py_INCREF(op)   ((op)->ob_refcnt++)
  /* 减少引用计数的宏定义 */
  #define Py_DECREF(op) \ //减少计数
      if (--(op)->ob_refcnt != 0) \
          ; \
      else \
          __Py_Dealloc((PyObject *)(op))
  ```

  导致引用计数+1的情况：

  - 对象被创建，例如`a = 23`
  - 对象被引用，例如`b = a`
  - 对象被作为参数，传入到一个函数中，例如`f(a)`
  - 对象作为一个元素，存储在容器中，例如`list1 = [a, a]`

  导致引用计数-1的情况：

  - 对象的别名被显式销毁，例如`del a`
  - 对象的别名被赋予新的对象，例如`a = 24`
  - 一个对象离开它的作用域，例如f函数执行完毕时，f函数中的局部变量（全局变量不会）
  - 对象所在的容器被销毁，或从容器中删除对象

  引用计数可能会导致循环引用问题，而循环引用会导致内存泄露，如下面的代码所示。为了解决这个问题，Python中引入了“标记-清除”和“分代收集”。在创建一个对象的时候，对象被放在第一代中，如果在第一代的垃圾检查中对象存活了下来，该对象就会被放到第二代中，同理在第二代的垃圾检查中对象存活下来，该对象就会被放到第三代中。

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

пример: пользовательские ограничения словаря могут задавать пары значений ключей в словаре только в том случае, если указанный ключ не существует.
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

объект создается через класс, а класс — через метакласс, который предоставляет метаинформацию для создания класса. все классы прямо или косвенно наследуются, а все метаклассы прямо или косвенно наследуются.objecttype

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

- 

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
