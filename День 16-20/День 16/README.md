## Продвинутый язык Python 

### Общая структура данных (день 16)
В Python существует несколько типов структур данных. Некоторые основные из них:

1. Список (list) — упорядоченная коллекция элементов, которые могут быть различных типов. Список ограничен 
   квадратными скобками [] и может содержать любое количество элементов, разделенных запятыми. 

2. Кортеж (tuple) — упорядоченная неизменяемая коллекция элементов, которые могут быть различных типов. Кортеж 
   ограничен круглыми скобками () и может содержать любое количество элементов, разделенных запятыми. 

3. Словарь (dictionary) — неупорядоченная коллекция пар ключ-значение, где каждый ключ уникален. Ключи и значения 
   могут быть любого типа данных. Словарь ограничен фигурными скобками {}. 

4. Множество (set) — неупорядоченная коллекция уникальных элементов. Множество ограничено фигурными скобками {} и 
   может содержать любое количество элементов, разделенных запятыми. 

5. Строка (string) — это упорядоченная коллекция символов Unicode. Строка ограничена кавычками (одинарными или 
   двойными). 

Кроме того, в Python существует множество других типов структур данных, таких как массивы, стеки, очереди и др. Они 
реализованы с помощью библиотеки NumPy или других модулей. 






### Использование генеративного (производного) создания

```Python
# создадим словарь в котором ключ - имя компании, а значение - цена акции
prices = {  
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# а теперь на основе словаря prices создадим новый словарь в котором останутся только компании с ценой акций больше, 
# чем $ 100  
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)
```

  > Генеративное создание (производное) может использоваться для создания списков, наборов и словарей.

### Вложенный список

```Python
names = ['Вано' , 'Андре' , 'Антонио' , 'Алежа' , 'Тимон']
courses = ['немецкий' , 'математика' , 'English' ]
# Введите оценки пяти студентов в трех курсах
# scores = [[None] * len(courses)] * len(names)
scores = [[None] * len(courses) for _ in range(len(names))]  # создадим шаблон-список, а далее на основе двух 
# верхних списков и цикла создадим новый список
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'please enter {name} {course} results: '))
        print(scores)
```


### Модуль `heapq` (сортировка по куче)
Модуль heapq в несколько раз облегчает написание программ, использующих такую структуру данных как куча. Этот модуль обеспечивает реализацию алгоритма очереди с кучами, также известный как алгоритм очереди с приоритетами.
Для создания типа данных используется пустой список.

Все функции записывают изменения в ту переменную, которая передавалась параметру heap.

```Python
"""
сортировка по куче
"""
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(3, list1))  # Возвращает список с самыми большими 3 элементами от набора данных 
print(heapq.nsmallest(3, list1))  # Возвращает список с самыми наименьшими 3 элементами от набора данных 
print(heapq.nlargest(2, list2, key=lambda x: x['price']))  # Возвращает список с самыми большими 2 элементами от 
# набора данных по ключу 'price'
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))  # Возвращает список с самыми большими 2 элементами от 
# набора данных по ключу 'shares'
  ```

### модуль `itertools` - сборник полезных итераторов.
  Для выполнения продвинутой генерации списка в языке Python используется подключаемая библиотека под названием 
 itertools. С ее помощью можно создавать наборы значений по определенным правилам. Методы, которые содержит эта 
  библиотека, позволяют генерировать списки с использованием улучшенных циклов. Например, с ее помощью можно легко 
  создавать комбинации различных значений, как символьных, так и числовых. Следующий код является простым примером 
  генерации списка с вызовом функции repeat.


  - itertools.permutations(iterable, r=None) - перестановки длиной r из iterable.
  - itertools.combinations(iterable, [r]) - комбинации длиной r из iterable без повторяющихся элементов.
  - itertools.product(*iterables, repeat=1) - аналог вложенных циклов.
  - itertools.cycle(iterable) - возвращает по одному значению из последовательности, повторенной бесконечное число раз.
  - itertools.repeat(elem, n=Inf) - повторяет elem n раз.
  - itertools.count(start=0, step=1) - бесконечная арифметическая прогрессия с первым членом start и шагом step.
  - itertools.accumulate(iterable) - аккумулирует суммы.
  - itertools.chain(*iterables) - возвращает по одному элементу из первого итератора, потом из второго, до тех пор, 
    пока итераторы не кончатся. 
  - itertools.combinations_with_replacement(iterable, r) - комбинации длиной r из iterable с повторяющимися элементами.
  - itertools.compress(data, selectors) - (d[0] if s[0]), (d[1] if s[1]), ...
  - itertools.filterfalse(func, iterable) - все элементы, для которых func возвращает ложь.
  - itertools.groupby(iterable, key=None) - группирует элементы по значению. Значение получается применением 
    функции key к элементу (если аргумент key не указан, то значением является сам элемент).
  - 

```Python
"""
сборник полезных итераторов
"""
import itertools

itertools.permutations('ABCD')  # перестановки из символов 'ABCD'
itertools.combinations('ABCDE', 3)  # комбинации длиной 3 из символов 'ABCDE' без повторяющихся элементов
itertools.product('ABCD', '123')  # аналог вложенных циклов
itertools.cycle(('A', 'B', 'C'))

```

### модуль `collections`
этот модуль предоставляет специализированные типы данных, на основе словарей, кортежей, множеств, списков.

  часто используемые классы инструментов:


  - collections.Counter - вид словаря, который позволяет нам считать количество неизменяемых объектов (в 
    большинстве случаев, строк).
  - elements() - возвращает список элементов в лексикографическом порядке.
  - subtract([iterable-or-mapping]) - вычитание
  - collections.defaultdict ничем не отличается от обычного словаря за исключением того, что по умолчанию всегда 
    вызывается функция, возвращающая значение
  - collections.OrderedDict - ещё один похожий на словарь объект, но он помнит порядок, в котором ему были даны ключи. Методы:
    - popitem(last=True) - удаляет последний элемент если last=True, и первый, если last=False.
    - move_to_end(key, last=True) - добавляет ключ в конец если last=True, и в начало, если last=False
  - collections.namedtuple позволяет создать тип данных, ведущий себя как кортеж, с тем дополнением, что каждому 
    элементу присваивается имя, по которому можно в дальнейшем получать доступ


Наиболее часто употребляемые шаблоны для работы с Counter:
- sum(c.values()) - общее количество.
- c.clear() - очистить счётчик.
- list(c) - список уникальных элементов.
- set(c) - преобразовать в множество.
- dict(c) - преобразовать в словарь.
- c.most_common()[:-n:-1] - n наименее часто встречающихся элементов.
- c += Counter() - удалить элементы, встречающиеся менее одного раза.
Counter также поддерживает сложение, вычитание, пересечение и объединение


collections.deque(iterable, [maxlen]) - создаёт очередь из итерируемого объекта с максимальной длиной maxlen. 
Очереди очень похожи на списки, за исключением того, что добавлять и удалять элементы можно либо справа, либо слева.

Методы, определённые в deque:
- append(x) - добавляет x в конец.
- appendleft(x) - добавляет x в начало.
- clear() - очищает очередь.
- count(x) - количество элементов, равных x.
- extend(iterable) - добавляет в конец все элементы iterable.
- extendleft(iterable) - добавляет в начало все элементы iterable (начиная с последнего элемента iterable).
- pop() - удаляет и возвращает последний элемент очереди.
- popleft() - удаляет и возвращает первый элемент очереди.
- remove(value) - удаляет первое вхождение value.
- reverse() - разворачивает очередь.
- rotate(n) - последовательно переносит n элементов из начала в конец (если n отрицательно, то с конца в начало).
 
```Python
"""
работа с специализированными типами данных, на основе словарей, кортежей, множеств, списков.
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))
```

### структура данных и алгоритмы

- алгоритмы: методы и шаги для решения проблемы

- алгоритм оценки хорошо или плохо: ближе к сложности времени и ближе к пространственной сложности.

- БОЛЬШИЕ O-МАРКЕРЫ СЛОЖНОСТИ БЛИЖЕГО ВРЕМЕНИ:
  - <img src="http://latex.codecogs.com/gif.latex?O(c)" /> - константная сложность времени - bloon filter / хэш-хранилище
  - <img src="http://latex.codecogs.com/gif.latex?O(log_2n)" /> - логарифмический тайм-аут сложности - сложить половину поиска (дихотомия)
  - <img src="http://latex.codecogs.com/gif.latex?O(n)" /> - линейная сложность времени - сортировка последовательного поиска/подсчета
  - <img src="http://latex.codecogs.com/gif.latex?O(n*log_2n)" /> - логарифмическая линейная сложность времени - расширенный алгоритм сортировки (сортировка и сортировка, быстрая сортировка)
  - <img src="http://latex.codecogs.com/gif.latex?O(n^2)" /> - сложность квадратного времени - простой алгоритм сортировки (выбор сортировки, сортировка вставки, сортировка пузырьков)
  - <img src="http://latex.codecogs.com/gif.latex?O(n^3)" /> - Кубическая сложность времени - алгоритм Floyd / операции умножения матрицы
  - <img src="http://latex.codecogs.com/gif.latex?O(2^n)" /> - геометрическая градуированный временной сложности - ганнота
  - <img src="http://latex.codecogs.com/gif.latex?O(n!)" /> - СЛОЖНОСТЬ ВРЕМЕНИ УМНОЖЕНИЯ - ПРОБЛЕМА РЕСЕЛЛЕРА ПУТЕШЕСТВИЯ - NPC


### Алгоритм сортировки (выбор, всплытие и объединение) и алгоритм поиска (последовательность и деление пополам)

  ```Python
  def select_sort(items, comp=lambda x, y: x < y):
      """простая сортировка выбора"""
      items = items[:]
      for i in range(len(items) - 1):
          min_index = i
          for j in range(i + 1, len(items)):
              if comp(items[j], items[min_index]):
                  min_index = j
          items[i], items[min_index] = items[min_index], items[i]
      return items
  ```

  ```Python
  def bubble_sort(items, comp=lambda x, y: x > y):
      """пузырьковая сортировка"""
      items = items[:]
      for i in range(len(items) - 1):
          swapped = False
          for j in range(len(items) - 1 - i):
              if comp(items[j], items[j + 1]):
                  items[j], items[j + 1] = items[j + 1], items[j]
                  swapped = True
          if not swapped:
              break
      return items
  ```

  ```Python
  def bubble_sort(items, comp=lambda x, y: x > y):
      """Сортировка перемешивания (пузырьковая сортировка улучшена)"""
      items = items[:]
      for i in range(len(items) - 1):
          swapped = False
          for j in range(len(items) - 1 - i):
              if comp(items[j], items[j + 1]):
                  items[j], items[j + 1] = items[j + 1], items[j]
                  swapped = True
          if swapped:
              swapped = False
              for j in range(len(items) - 2 - i, i, -1):
                  if comp(items[j - 1], items[j]):
                      items[j], items[j - 1] = items[j - 1], items[j]
                      swapped = True
          if not swapped:
              break
      return items
  ```

  ```Python
  def merge(items1, items2, comp=lambda x, y: x < y):
      """Merge (объединить два упорядоченных списков в один упорядоченный список)"""
      items = []
      index1, index2 = 0, 0
      while index1 < len(items1) and index2 < len(items2):
          if comp(items1[index1], items2[index2]):
              items.append(items1[index1])
              index1 += 1
          else:
              items.append(items2[index2])
              index2 += 1
      items += items1[index1:]
      items += items2[index2:]
      return items
  
  
  def merge_sort(items, comp=lambda x, y: x < y):
      return _merge_sort(list(items), comp)
  
  
  def _merge_sort(items, comp):
      """Сортировка слиянием"""
      if len(items) < 2:
          return items
      mid = len(items) // 2
      left = _merge_sort(items[:mid], comp)
      right = _merge_sort(items[mid:], comp)
      return merge(left, right, comp)
  ```

  ```Python
  def seq_search(items, key):
      """Последовательный поиск"""
      for index, item in enumerate(items):
          if item == key:
              return index
      return -1
  ```

  ```Python
  def bin_search(items, key):
      """двоичный поиск"""
      start, end = 0, len(items) - 1
      while start <= end:
          mid = (start + end) // 2
          if key > items[mid]:
              start = mid + 1
          elif key < items[mid]:
              end = mid - 1
          else:
              return mid
      return -1
  ```

- распространенные алгоритмы:

  - метод бедности - также известный как насильственный взлом, проверяет все возможности до тех пор, пока не будет найден правильный ответ.
  - жадный метод - всегда делается в настоящее время при решении проблемы
  - лучший выбор, не преследуя оптимального решения, быстро найти удовлетворительное решение.
  - разделение - разделите сложную проблему на две или более идентичных или похожих подпрофех, а затем разделите 
    подпропорцию на более мелкие подпропорции до такой степени, что она может быть решена напрямую, и, наконец, объедините решение подпропорций, чтобы получить решение исходной проблемы.
  - backtracking - backtracking, также известный как пробный метод, выполняет поиск вперед на основе критериев 
    отбора и возвращается к повторному выбору, когда поиск на определенном этапе обнаруживает, что первоначальный выбор не является оптимальным или не соответствует цели.
  - динамическое планирование - основная идея заключается в том, чтобы разбить проблему, которую необходимо решить, 
    на несколько подпросов, сначала решить и сохранить решение этих подпроцеснований, чтобы избежать большого количества повторяющихся операций.

  пример бедности: 100-долларовая курица и пятичеловечная рыба.

```Python
# Овца 5 юаней, курица, 3 юаней, немного курицы, 1 юаней, три 
# Купить 100 кур за 100 юаней и спросить , сколько петух / курица / курица каждый 
for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
            print(x, y, z)

# A, B, C, D, E - это пять человек рыбачили целый день и ночь на рыбалке и наконец устали и заснули 
# B - Второй человек просыпается и делит рыбу на 5 частей. Выбрасывает лишнюю. и забирает свою часть. 
# Затем C, D и E просыпаются по очереди и делят рыбу таким же образом 

fish = 6
while True:
    total = fish
    enough = True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            enough = False
            break
    if enough:
        print(fish)
        break
    fish += 5
```

  пример жадности: предполагая, что у вора есть рюкзак, способный содержать до 20 кг краденого, он ворвался в дом и 
  нашел предметы, показанные в таблице ниже. Очевидно, что он не может упаковать все вещи в рюкзак, поэтому он 
  должен определить, какие предметы (самые дорогие) взять.
  
  |  имя  | цена (в долл. сша) 	 | вес (кг) |
  | :----: | :----------: | :--------: |
  |  компьютер  |     200      |     20     |
  | радио |      20      |     4      |
  |   часы   |     175      |     10     |
  |  ваза  |      50      |     2      |
  |  книги   |      10      |     1      |
  |  масляная живопись 	  |      90      |     9      |

  ```Python
"""
 Жадный метод: решая проблему, всегда делайте лучший выбор, который кажется лучшим на данный момент, не ищите 
 оптимального решения и быстро находите удовлетворительное решение. 
  """
class Thing(object):
    """вещь"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """Отношение цены к весу"""
        return self.price / self.weight


def input_thing():
    """Введите информацию об элементе"""
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
    print(f'Итого украдено на сумму: {total_price} долл. США')


if __name__ == '__main__':
    main()
```

пример раздела: быстрая сортировка.
```Python
"""
Быстрая сортировка - выберите точку поворота для разделения элементов, левая часть меньше точки поворота, а правая больше точки поворота 
"""
def quick_sort(items, comp=lambda x, y: x <= y):
    items = list(items)[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, start, end, comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)


def _partition(items, start, end, comp):
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1
  ```

пример ретроспективного метода: рыцарский патруль.
```Python
"""
Рекурсивный метод обратного отслеживания: называется эвристическим методом, поиск вперед в соответствии с критериями выбора, при поиске определенного шага и обнаружении, что исходный выбор не подходит или не достигает цели, он возвращается на один шаг назад и повторно выбирает, a более классическая задача Включая рыцарский патруль, восемь королев и поиск в лабиринте и т. д. 
"""
import sys
import time

SIZE = 5
total = 0


def print_board(board):
    for row in board:
        for col in row:
            print(str(col).center(4), end='')
        print()


def patrol(board, row, col, step=1):
    if row >= 0 and row < SIZE and \
        col >= 0 and col < SIZE and \
        board[row][col] == 0:
        board[row][col] = step
        if step == SIZE * SIZE:
            global total
            total += 1
            print(f'всего {total} видов движений: ')
            print_board(board)
        patrol(board, row - 2, col - 1, step + 1)
        patrol(board, row - 1, col - 2, step + 1)
        patrol(board, row + 1, col - 2, step + 1)
        patrol(board, row + 2, col - 1, step + 1)
        patrol(board, row + 2, col + 1, step + 1)
        patrol(board, row + 1, col + 2, step + 1)
        patrol(board, row - 1, col + 2, step + 1)
        patrol(board, row - 2, col + 1, step + 1)
        board[row][col] = 0


def main():
    board = [[0] * SIZE for _ in range(SIZE)]
    patrol(board, SIZE - 1, SIZE - 1)


if __name__ == '__main__':
    main()
  ```

пример динамического планирования: максимальное значение для подлистовых элементов.

  > описание: подсегмент относится к списку, состоящим из последовательных элементов индекса (подстроки) в списке, 
  > элементы в списке являются типами int, которые могут содержать положительные целые числа, 0, отрицательные 
  > целые числа, элементы в списке ввода программы, максимальные значения суммирования выходных элементов подлиста, 
  > такие как:

    вход: 1 -2 3 5 -3 2
    выход: 8
    вход: 0 -2 3 5 -1 2
    выход: 9
    вход: -9 -2 -3 -5 -3
    выход: -2


  ```Python
  def main():
      items = list(map(int, input().split()))
      overall = partial = items[0]
      for i in range(1, len(items)):
          partial = max(items[i], partial + items[i])
          overall = max(partial, overall)
      print(overall)
  
  
  if __name__ == '__main__':
      main()
  ```

  > Описание: Самое простое решение этой темы заключается в использовании дуэта, но производительность кода во 
  > времени может стать очень плохой. Используя идею динамического планирования, просто используя две другие 
  > переменные, проблема сложности первоначального $O (N^2)$ превратилась в $O (N)$.

