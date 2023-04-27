- Магические методы, связанные с итераторами и генераторами / два способа создания генераторов /

### Магические методы, связанные с итераторами и генераторами (день 19)


### итераторы и генераторы

    итератор — это объект, реализующий протокол итератора.
        В Python нет ключевых слов, которые определяют протоколы, как это.protocolinterface
        Протокол представлен волшебным методом в Python.
        __iter__и волшебный метод является протоколом итератора.__next__


  ```Python
  class Fib(object):
      """迭代器"""
      
      def __init__(self, num):
          self.num = num
          self.a, self.b = 0, 1
          self.idx = 0
     
      def __iter__(self):
          return self
  
      def __next__(self):
          if self.idx < self.num:
              self.a, self.b = self.b, self.a + self.b
              self.idx += 1
              return self.a
          raise StopIteration()
  ```

- генератор — это итератор упрощенной версии синтаксиса.

  ```Python
  def fib(num):
      """生成器"""
      a, b = 0, 1
      for _ in range(num):
          a, b = b, a + b
          yield a
  ```

- генератор эволюционировал в ковариацию.

объект генератора может использовать метод для отправки данных, которые становятся значениями, полученными с помощью выражений в функции генератора. таким образом, генератор может использоваться в качестве совместной программы, которая, проще говоря, является подпрограммой, которая может сотрудничать друг с другом.send()yield
  ```Python
  def calc_avg():
      """流式计算平均值"""
      total, counter = 0, 0
      avg_value = None
      while True:
          value = yield avg_value
          total, counter = total + value, counter + 1
          avg_value = total / counter
  
  
  gen = calc_avg()
  next(gen)
  print(gen.send(10))
  print(gen.send(20))
  print(gen.send(30))
  ```
