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
        player.get_hand().remove_card(player.get_hand().get_cards().index(self))
        player.get_hand().add_cards(game.pick_card())
        game.set_action('NO_ACTION')
        game.next_player()

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

    def play(self, player, game):
        game.set_action('NO_ACTION')
        game.next_player()

    def get_name(self):
        return self.__name


class TutorCard(Card):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'TutorCard(' + self.__name + ')'

    def __repr__(self):
        return 'TutorCard(' + self.__name + ')'

    def play(self, player, game):
        player_deck = player.get_hand()
        player_deck.remove_card(player_deck.get_cards().index(self))
        player_deck.add_card(game.pick_card()[0])
        game.set_action('PICKUP_CODER')

    def action(self, player, game, slot):
        selected_card = game.get_sleeping_coder(slot)
        player.get_coders().add_card(selected_card)
        game.set_sleeping_coder(game.get_sleeping_coders().index(selected_card), None)
        game.set_action('NO_ACTION')
        game.next_player()

    def get_name(self):
        return self.__name


class KeyboardKidnapperCard(Card):
    def __str__(self):
        return 'KeyboardKidnapperCard()'

    def __repr__(self):
        return 'KeyboardKidnapperCard()'

    def play(self, player, game):
        player_deck = player.get_hand()
        player_deck.remove_card(player_deck.get_cards().index(self))
        player_deck.add_card(game.pick_card()[0])
        game.set_action('STEAL_CODER')

    def action(self, player, game, slot):
        selected_card = player.get_coders().get_card(slot)
        player.get_coders().remove_card(slot)
        game.current_player().get_coders().add_card(selected_card)
        game.set_action('NO_ACTION')
        game.next_player()


class AllNighterCard(Card):
    def __str__(self):
        return 'AllNighterCard()'

    def __repr__(self):
        return 'AllNighterCard()'

    def play(self, player, game):
        player_deck = player.get_hand()
        player_deck.remove_card(player_deck.get_cards().index(self))
        player_deck.add_card(game.pick_card()[0])
        game.set_action('SLEEP_CODER')

    def action(self, player, game, slot):
        selected_card = player.get_coders().get_card(slot)
        player.get_coders().remove_card(slot)
        for i, card in enumerate(game.get_sleeping_coders()):
            if card is None:
                game.set_sleeping_coder(i, selected_card)
                break
        game.set_action('NO_ACTION')
        game.next_player()


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
        return self.__cards

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
