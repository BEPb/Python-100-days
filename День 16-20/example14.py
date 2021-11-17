"""
Объектно-ориентированный
Перечисление. Возможны только ограниченные варианты значений переменной, наиболее подходящий тип - перечисление.
Посредством перечисления мы можем определять символические константы, символьные константы лучше, чем буквальные константы.
"""
from enum import Enum, unique

import random


@unique
class Suite(Enum):
    """花色（枚举）"""
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
        Player('восток'), Player('запад'),
        Player('юг'), Player('север')
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
