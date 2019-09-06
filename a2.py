#!/usr/bin/env python3
"""
Assignment 2 - Sleeping Coders
CSSE1001/7030
Semester 2, 2019
"""

import random

__author__ = "Knorringite"


class Card:
    def __str__(self):
        return 'Card()'

    def __repr__(self):
        return 'Card()'

    def play(self, player, game):
        pass

    def action(self, player, game, slot):
        pass


class NumberCard(Card):
    def __init__(self, number):
        self.__number = number

    def __str__(self):
        return 'NumberCard(' + str(self.__number) + ')'

    def __repr__(self):
        return 'NumberCard(' + str(self.__number) + ')'

    def get_number(self):
        return self.__number


class CoderCard(Card):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'CoderCard(' + self.__name + ')'

    def __repr__(self):
        return 'CoderCard(' + self.__name + ')'

    def get_name(self):
        return self.__name


class TutorCard(Card):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'TutorCard(' + self.__name + ')'

    def __repr__(self):
        return 'TutorCard(' + self.__name + ')'

    def get_name(self):
        return self.__name


class KeyboardKidnapperCard(Card):
    def __str__(self):
        return 'KeyboardKidnapperCard()'

    def __repr__(self):
        return 'KeyboardKidnapperCard()'


class AllNighterCard(Card):
    def __str__(self):
        return 'AllNighterCard()'

    def __repr__(self):
        return 'AllNighterCard()'


class Deck:
    def __init__(self, starting_cards=None):
        if starting_cards is None:
            self.__cards = []
        else:
            self.__cards = starting_cards

    def __str__(self):
        return 'Deck(' + ', '.join([i.__str__() for i in self.__cards]) + ')'

    def __repr__(self):
        return 'Deck(' + ', '.join([i.__str__() for i in self.__cards]) + ')'

    def get_cards(self):
        return [i for i in self.__cards]

    def get_card(self, slot):
        return self.__cards[slot]

    def top(self):
        return self.__cards[-1]

    def remove_card(self, slot):
        self.__cards.pop(slot)

    def get_amount(self):
        return len(self.__cards)

    def shuffle(self):
        random.shuffle(self.__cards)

    def pick(self, amount=1):
        pick_cards = []
        for _ in range(amount):
            pick_cards.append(self.__cards.pop())
        return pick_cards

    def add_card(self, card):
        self.__cards.append(card)

    def add_cards(self, cards):
        self.__cards = self.__cards + cards

    def copy(self, other_deck):
        self.__cards = self.__cards + other_deck.get_cards()


class Player:
    def __init__(self, name):
        self.__name = name
        self.__hand = Deck()
        self.__coders = Deck()

    def __str__(self):
        return 'Player(' + self.__name + ', ' + self.__hand.__str__()\
               + ', ' + self.__coders.__str__() + ')'

    def __repr__(self):
        return 'Player(' + self.__name + ', ' + self.__hand.__str__()\
               + ', ' + self.__coders.__str__() + ')'

    def get_name(self):
        return self.__name

    def get_hand(self):
        return self.__hand

    def get_coders(self):
        return self.__coders

    def has_won(self):
        if self.__coders.get_amount() >= 4:
            return True
        else:
            return False


def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()
