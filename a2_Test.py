import unittest
from a2 import *
import a2_support


class A2_test(unittest.TestCase):
    def setUp(self):
        peter = Player("Peter O'Shea")
        players = [peter, Player("Jason Storey"), Player("Mike Pham")]
        coders = [CoderCard("anna"), CoderCard("lochie")]
        deck = Deck([NumberCard(2), NumberCard(4), NumberCard(1)])
        game = a2_support.CodersGame(deck, coders, players)

    def test_NumberCard(self):
        card = NumberCard(3)
        self.assertEqual(card.get_number(), 3, 'Wrong card number')
        self.assertEqual(str(card), 'NumberCard(3)', 'Wrong str output')
        self.assertEqual(repr(card), 'NumberCard(3)', 'Wrong repr output')

    def test_CoderCard(self):
        card = CoderCard("hanwei")
        self.assertEqual(card.get_name(), 'hanwei', 'Wrong get_name output')
        self.assertEqual(str(card), 'CoderCard(hanwei)', 'Wrong str output')
        self.assertEqual(repr(card), 'CoderCard(hanwei)', 'Wrong repr output')

    def test_TutorCard(self):
        card = TutorCard("luis")
        self.assertEqual(card.get_name(), 'luis', 'Wrong ')
        self.assertEqual(str(card), 'TutorCard(luis)', 'Wrong str output')
        self.assertEqual(repr(card), 'TutorCard(luis)', 'Wrong repr output')

    def test_KeyboardKidnapperCard(self):
        card = KeyboardKidnapperCard()
        self.assertEqual(str(card), 'KeyboardKidnapperCard()', 'Wrong str output')
        self.assertEqual(repr(card), 'KeyboardKidnapperCard()', 'Wrong repr output')

    def test_AllNighterCard(self):
        card = AllNighterCard()
        self.assertEqual(str(card), 'AllNighterCard()', 'Wrong str output')
        self.assertEqual(repr(card), 'AllNighterCard()', 'Wrong repr output')

    def test_Deck(self):
        card = NumberCard(3)
        all_nighter = AllNighterCard()
        last_card = NumberCard(2)
        cards = [card, all_nighter, last_card]
        deck = Deck(cards)

        self.assertEqual(str(deck), 'Deck(NumberCard(3), '
                                    'AllNighterCard(), NumberCard(2))', 'Wrong str output')
        self.assertEqual(repr(deck), 'Deck(NumberCard(3), '
                                     'AllNighterCard(), NumberCard(2))', 'Wrong repr output')
        self.assertEqual(deck.get_cards(), [NumberCard(3), AllNighterCard(), NumberCard(2)], 'Wrong get_cards output')
        self.assertEqual(deck.get_amount(), 3, 'Wrong get_amount output')
        self.assertEqual(deck.get_card(0), NumberCard(3), 'Wrong get_card output')
        self.assertEqual(deck.get_card(2), NumberCard(2), 'Wrong get_card output')
        self.assertEqual(deck.top(), NumberCard(2), 'Wrong top output')

        new_card = AllNighterCard()
        deck.add_card(new_card)
        deck.add_cards([card, all_nighter, last_card])
        self.assertEqual(deck.get_amount(), 7, 'Wrong add_card output')
        self.assertEqual(deck.get_cards(), [NumberCard(3), AllNighterCard(), NumberCard(2),
                                            AllNighterCard(), NumberCard(3), AllNighterCard(),
                                            NumberCard(2)], 'Wrong add_card output')
        deck.remove_card(1)
        deck.remove_card(4)
        self.assertEqual(deck.get_cards(), [NumberCard(3), NumberCard(2), AllNighterCard(),
                                            NumberCard(3), NumberCard(2)], 'Wrong remove card output')
        self.assertEqual(deck.pick(), [NumberCard(2)], 'Wrong pick output')
