"""
Python 3.9
Модульное тестирование-тестирование самых маленьких функциональных модулей (функций и методов) в программе
Методы испытаний:
-Тест белого ящика: тест, написанный самой программой
-Тестирование черного ящика: тестировщики или QA, не знают деталей реализации кода, сосредотачиваются только на функциях
Напишите модульные тесты Python - определите классы для наследования TestCase, напишите методы тестирования (начиная с test_)
Выполните модульные тесты:
- unittest.main()
- python3 -m unittest test_example01.py
Сторонняя библиотека - nose2 / pytest
pip install pytest pytest-cov
pytest -v --cov
------------------------------
pip install nose2 cov-core
nose2 -v -C
"""
from unittest import TestCase

from example01 import seq_search, bin_search


class TestExample01(TestCase):
    """Тестовый пример для поиска функции"""

    # Метод, который будет выполняться перед выполнением каждой тестовой функции
    def setUp(self):
        self.data1 = [35, 97, 12, 68, 55, 73, 81, 40]
        self.data2 = [12, 35, 40, 55, 68, 73, 81, 97]

    # Метод, который будет выполняться после выполнения каждой тестовой функции
    def tearDown(self):
        pass

    def test_seq_search(self):
        """Поиск тестового заказа"""
        self.assertEqual(0, seq_search(self.data1, 35))
        self.assertEqual(2, seq_search(self.data1, 12))
        self.assertEqual(6, seq_search(self.data1, 81))
        self.assertEqual(7, seq_search(self.data1, 40))
        self.assertEqual(-1, seq_search(self.data1, 99))
        self.assertEqual(-1, seq_search(self.data1, 7))

    def test_bin_search(self):
        """Проверить двоичный поиск"""
        self.assertEqual(1, bin_search(self.data2, 35))
        self.assertEqual(0, bin_search(self.data2, 12))
        self.assertEqual(6, bin_search(self.data2, 81))
        self.assertEqual(2, bin_search(self.data2, 40))
        self.assertEqual(7, bin_search(self.data2, 97))
        self.assertEqual(-1, bin_search(self.data2, 7))
        self.assertEqual(-1, bin_search(self.data2, 99))
