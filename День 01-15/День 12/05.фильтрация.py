"""
Python 3.9 Фильтрация нежелательного содержания
Название файла '05.фильтрация.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-11
"""
import re


def main():
    sentence = 'Ты глуп? Я трахнул твоего дядю. Пошел ты на хуй.'
    purified = re.sub('[иметь]|на хуй|дерьмо|глупо[тупо]|урод',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)


if __name__ == '__main__':
    main()
