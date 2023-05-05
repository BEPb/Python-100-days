- Параллельное и асинхронное программирование - многопоточный / многопроцессорный / асинхронный ввод-вывод / 
  асинхронный и ожидающий


### Параллельное и асинхронное программирование (день 20)


### Параллельное программирование

Существует три сценария параллельного программирования в Python: многопоточный, многопроцессный и асинхронный 
ввод-вывод. Преимущество параллельного программирования заключается в повышении эффективности выполнения программ и 
улучшении взаимодействия с пользователем;

Многопоточный: класс предоставляется в Python и дополняется 、、、. Python имеет GIL, чтобы предотвратить несколько 
потоков от выполнения локальных байт-кодов одновременно, блокировка является обязательным для CPython, так как 
управление памятью CPython не является потокобезопасным, поскольку наличие GIL многопоточных не может играть 
многоядерные характеристики ЦП.ThreadLockConditionEventSemaphoreBarrier   
  ```Python
  """
  面试题：进程和线程的区别和联系？
  进程 - 操作系统分配内存的基本单位 - 一个进程可以包含一个或多个线程
  线程 - 操作系统分配CPU的基本单位
  并发编程（concurrent programming）
  1. 提升执行性能 - 让程序中没有因果关系的部分可以并发的执行
  2. 改善用户体验 - 让耗时间的操作不会造成程序的假死
  """
  import glob
  import os
  import threading
  
  from PIL import Image
  
  PREFIX = 'thumbnails'
  
  
  def generate_thumbnail(infile, size, format='PNG'):
      """生成指定图片文件的缩略图"""
  	file, ext = os.path.splitext(infile)
  	file = file[file.rfind('/') + 1:]
  	outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
  	img = Image.open(infile)
  	img.thumbnail(size, Image.ANTIALIAS)
  	img.save(outfile, format)
  
  
  def main():
      """主函数"""
  	if not os.path.exists(PREFIX):
  		os.mkdir(PREFIX)
  	for infile in glob.glob('images/*.png'):
  		for size in (32, 64, 128):
              # 创建并启动线程
  			threading.Thread(
  				target=generate_thumbnail, 
  				args=(infile, (size, size))
  			).start()
  			
  
  if __name__ == '__main__':
  	main()
  ```

Ситуация, когда несколько потоков конкурируют за ресурсы.

  ```Python
  """
  多线程程序如果没有竞争资源处理起来通常也比较简单
  当多个线程竞争临界资源的时候如果缺乏必要的保护措施就会导致数据错乱
  说明：临界资源就是被多个线程竞争的资源
  """
  import time
  import threading
  
  from concurrent.futures import ThreadPoolExecutor
  
  
  class Account(object):
      """银行账户"""
  
      def __init__(self):
          self.balance = 0.0
          self.lock = threading.Lock()
  
      def deposit(self, money):
          # 通过锁保护临界资源
          with self.lock:
              new_balance = self.balance + money
              time.sleep(0.001)
              self.balance = new_balance
  
  
  def main():
      """主函数"""
      account = Account()
      # 创建线程池
      pool = ThreadPoolExecutor(max_workers=10)
      futures = []
      for _ in range(100):
          future = pool.submit(account.deposit, 1)
          futures.append(future)
      # 关闭线程池
      pool.shutdown()
      for future in futures:
          future.result()
      print(account.balance)
  
  
  if __name__ == '__main__':
      main()
  ```
  
  измените приведенную выше программу, запустите 5 потоков, чтобы сэкономить деньги на счете, 5 потоков, чтобы снять деньги со счета, и приостановить поток, если баланс недостаточен. для достижения вышеуказанных целей необходимо планировать потоки, которые экономят деньги и снимают деньги, потоки, которые снимают деньги, когда баланс недостаточен, приостанавливаются и освобождаются блокировки, в то время как потоки, которые экономят деньги, вводят деньги и уведомляют потоки, которые снимают деньги, чтобы они проснулись от приостановления. модуль можно использовать для реализации планирования потоков, объект также создается на основе блокировок, код выглядит следующим образом:threadingCondition
  ```Python
  """
  多个线程竞争一个资源 - 保护临界资源 - 锁（Lock/RLock）
  多个线程竞争多个资源（线程数>资源数） - 信号量（Semaphore）
  多个线程的调度 - 暂停线程执行/唤醒等待中的线程 - Condition
  """
  from concurrent.futures import ThreadPoolExecutor
  from random import randint
  from time import sleep
  
  import threading
  
  
  class Account:
      """银行账户"""
  
      def __init__(self, balance=0):
          self.balance = balance
          lock = threading.RLock()
          self.condition = threading.Condition(lock)
  
      def withdraw(self, money):
          """取钱"""
          with self.condition:
              while money > self.balance:
                  self.condition.wait()
              new_balance = self.balance - money
              sleep(0.001)
              self.balance = new_balance
  
      def deposit(self, money):
          """存钱"""
          with self.condition:
              new_balance = self.balance + money
              sleep(0.001)
              self.balance = new_balance
              self.condition.notify_all()
  
  
  def add_money(account):
      while True:
          money = randint(5, 10)
          account.deposit(money)
          print(threading.current_thread().name, 
                ':', money, '====>', account.balance)
          sleep(0.5)
  
  
  def sub_money(account):
      while True:
          money = randint(10, 30)
          account.withdraw(money)
          print(threading.current_thread().name, 
                ':', money, '<====', account.balance)
          sleep(1)
  
  
  def main():
      account = Account()
      with ThreadPoolExecutor(max_workers=15) as pool:
          for _ in range(5):
              pool.submit(add_money, account)
          for _ in range(10):
              pool.submit(sub_money, account)
  
  
  if __name__ == '__main__':
      main()
  ```
  
- МНОГОПРОЦЕССНЫЙ: МНОГОПРОЦЕССНЫЙ МОЖЕТ ЭФФЕКТИВНО РЕШИТЬ ПРОБЛЕМУ GIL, РЕАЛИЗАЦИЯ МНОГОПРОЦЕССНОГО ОСНОВНОГО КЛАССА ЗАКЛЮЧАЕТСЯ В ТОМ, ЧТО ДРУГИЕ ВСПОМОГАТЕЛЬНЫЕ КЛАССЫ АНАЛОГИЧНЫ ТЕМ, КОТОРЫЕ НАХОДЯТСЯ В МОДУЛЕ, ОБМЕН ДАННЫМИ МЕЖДУ ПРОЦЕССАМИ МОЖЕТ ИСПОЛЬЗОВАТЬ КОНВЕЙЕР, СОКЕТ И Т.Д., В МОДУЛЕ ЕСТЬ КЛАСС, КОТОРЫЙ ПРЕДОСТАВЛЯЕТ НЕСКОЛЬКО ОЧЕРЕДЕЙ СОВМЕСТНОГО ИСПОЛЬЗОВАНИЯ ПРОЦЕССОВ НА ОСНОВЕ КОНВЕЙЕРА И МЕХАНИЗМА БЛОКИРОВКИ. НИЖЕ ПРИВЕДЕН ПРИМЕР МНОГОПРОЦЕССНОГО И ПУЛА ПРОЦЕССОВ В ОФИЦИАЛЬНОМ ДОКУМЕНТЕ.ProcessthreadingmultiprocessingQueue
  ```Python
  """
  多进程和进程池的使用
  多线程因为GIL的存在不能够发挥CPU的多核特性
  对于计算密集型任务应该考虑使用多进程
  time python3 example22.py
  real    0m11.512s
  user    0m39.319s
  sys     0m0.169s
  使用多进程后实际执行时间为11.512秒，而用户时间39.319秒约为实际执行时间的4倍
  这就证明我们的程序通过多进程使用了CPU的多核特性，而且这台计算机配置了4核的CPU
  """
  import concurrent.futures
  import math
  
  PRIMES = [
      1116281,
      1297337,
      104395303,
      472882027,
      533000389,
      817504243,
      982451653,
      112272535095293,
      112582705942171,
      112272535095293,
      115280095190773,
      115797848077099,
      1099726899285419
  ] * 5
  
  
  def is_prime(n):
      """判断素数"""
      if n % 2 == 0:
          return False
  
      sqrt_n = int(math.floor(math.sqrt(n)))
      for i in range(3, sqrt_n + 1, 2):
          if n % i == 0:
              return False
      return True
  
  
  def main():
      """主函数"""
      with concurrent.futures.ProcessPoolExecutor() as executor:
          for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
              print('%d is prime: %s' % (number, prime))
  
  
  if __name__ == '__main__':
      main()
  ```

  > ключевые моменты: многопоточное и многопроцессное сравнение.
  >
  > несколько потоков необходимы в следующих случаях:

    Программы должны поддерживать многие общие состояния( особенно переменные), а списки, словари и коллекции в Python являются потокобезопасными, поэтому обслуживание общего состояния с помощью потоков, а не процессов, обходится относительно не по цене.
    ПРОГРАММА ТРАТИТ МНОГО ВРЕМЕНИ НА ОПЕРАЦИИ ВВОДА-ВЫВОДА, НЕ ТРЕБУЕТ МНОГО ПАРАЛЛЕЛЬНЫХ ВЫЧИСЛЕНИЙ И НЕ ТРЕБУЕТ МНОГО ПАМЯТИ.

несколько процессов необходимы в следующих случаях:

    программа выполняет задачи с интенсивным использованием вычислений (например, операции байт-кода, обработка данных, научные вычисления).
    входные данные программы могут быть разделены параллельно на блоки, а результаты операции могут быть объединены.
    ПРОГРАММА НЕ ИМЕЕТ КАКИХ-ЛИБО ОГРАНИЧЕНИЙ НА ИСПОЛЬЗОВАНИЕ ПАМЯТИ И НЕ СИЛЬНО ЗАВИСИТ ОТ ОПЕРАЦИЙ ВВОДА-ВЫВОДА (НАПРИМЕР, ЧТЕНИЕ И ЗАПИСЬ ФАЙЛОВ, СОКЕТОВ И Т.Д.).


- Асинхронная обработка: Выбор задач из очереди задач планировщика, выполняющей эти задачи в перекрестном режиме, не гарантирует, что задачи будут выполняться в определенном порядке, поскольку порядок выполнения зависит от готовности одной задачи в очереди уступить время обработки ЦП другой задаче. Асинхронные задачи обычно выполняются с помощью многозадачной совместной работы, и из-за неопределенности в отношении времени и последовательности выполнения необходимо получить результаты выполнения задачи с помощью обратного программирования или объектов. Python 3 поддерживает асинхронную обработку с помощью модулей и ключевых слов, которые официально перечислены в Python 3.7.futureasyncioawaitasync
  ```Python
  """
  异步I/O - async / await
  """
  import asyncio
  
  
  def num_generator(m, n):
      """指定范围的数字生成器"""
      yield from range(m, n + 1)
  
  
  async def prime_filter(m, n):
      """素数过滤器"""
      primes = []
      for i in num_generator(m, n):
          flag = True
          for j in range(2, int(i ** 0.5 + 1)):
              if i % j == 0:
                  flag = False
                  break
          if flag:
              print('Prime =>', i)
              primes.append(i)
  
          await asyncio.sleep(0.001)
      return tuple(primes)
  
  
  async def square_mapper(m, n):
      """平方映射器"""
      squares = []
      for i in num_generator(m, n):
          print('Square =>', i * i)
          squares.append(i * i)
  
          await asyncio.sleep(0.001)
      return squares
  
  
  def main():
      """主函数"""
      loop = asyncio.get_event_loop()
      future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
      future.add_done_callback(lambda x: print(x.result()))
      loop.run_until_complete(future)
      loop.close()
  
  
  if __name__ == '__main__':
      main()
  ```

  > 

    описание: приведенный выше код использует функцию для получения цикла событий системы по умолчанию, функция может получить объект, объект может добавить функцию обратного вызова при выполнении, метод объекта может ждать результатов совместного выполнения через объект.get_event_loopgatherfuturefutureadd_done_callbacklooprun_until_completefuture

  Python имеет трехстороннюю библиотеку с именем, которая предоставляет асинхронные HTTP-клиенты и серверы, которые могут работать с модулями и обеспечивают поддержку объектов. Функции, определяющие асинхронное выполнение и созданные асинхронные контексты, были введены и определены в Python 3.6, и они официально стали ключевыми словами в Python 3.7. Следующий код асинхронно извлекает страницу из 5 URL-адресов и извлекает заголовок сайта через именованную группу захвата регулярного выражения.aiohttpasyncioFutureasyncawait
  ```Python
  import asyncio
  import re
  
  import aiohttp
  
  PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')
  
  
  async def fetch_page(session, url):
      async with session.get(url, ssl=False) as resp:
          return await resp.text()
  
  
  async def show_title(url):
      async with aiohttp.ClientSession() as session:
          html = await fetch_page(session, url)
          print(PATTERN.search(html).group('title'))
  
  
  def main():
      urls = ('https://www.python.org/',
              'https://git-scm.com/',
              'https://www.jd.com/',
              'https://www.taobao.com/',
              'https://www.douban.com/')
      loop = asyncio.get_event_loop()
      cos = [show_title(url) for url in urls]
      loop.run_until_complete(asyncio.wait(cos))
      loop.close()
  
  
  if __name__ == '__main__':
      main()
  ```

  > В центре внимания: сравнение асинхронного ввода-вывода с несколькими процессами.
  >
  > Это хороший выбор, когда программа не требует истинной параллели или параллели, но в большей степени зависит от асинхронной обработки и обратных вызовов. Если в программе много ожидания и спящего режима, следует также учитывать, что она идеально подходит для написания серверов веб-приложений, которые не имеют требований к обработке данных в режиме реального времени.asyncioasyncio
  > 
  PPython также имеет много трехсторонних библиотек для параллельных задач, таких как: и т.д. В реальной разработке для повышения масштабируемости и параллели системы обычно существует как вертикальное масштабирование (увеличение вычислительной мощности одного узла), так и горизонтальное масштабирование (преобразование одного узла в несколько узлов). Разъединение приложений может быть достигнуто с помощью очередей сообщений, эквивалентных расширенной версии многопоточной очереди синхронизации, приложений на разных компьютерах, эквивалентных потокам, и общей распределенной очереди сообщений, которая является Queue в исходной программе. Наиболее распространенной и стандартизированной реализацией очередей сообщений (промежуточного ПО для сообщений) является AMCP (Advanced Steet Referred), который происходит от финансовой отрасли и предоставляет такие функции, как очереди, маршрутизация, надежная передача, безопасность и многое другое, в том числе: ActiveMQ Apache, RabbitMQ и многое другое.joblibPyMP

Для асинхронизации задачи можно использовать трехстороннюю библиотеку с именем. — это распределенная очередь задач, 
написанная Python, которая работает с распределенными сообщениями и может выступать в качестве прокси-сервера 
сообщений для серверной части на основе RabbitMQ или Reds.CeleryCelery  


[Вернуться на главную](https://github.com/BEPb/Python-100-days)

[К следующему занятию](https://github.com/BEPb/Python-100-days/blob/master/%D0%94%D0%B5%D0%BD%D1%8C%2016-20/%D0%94%D0%B5%D0%BD%D1%8C%2020/README.md)
