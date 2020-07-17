"""Cards in Uno

    all str

    color
    --------
        Blue
        Green
        Red
        Yellow
        Wild

    types
    --------
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        Reverse
        Skip
        Draw 2
        Wild Draw 4
        Wild
        Blank

"""

import random
import main

class Card:
    # Description of type
    description = None

    def __init__(self, color, type, name=None, action=None, description=None):
        """Card base class used by all cards."""

        # Color of card
        self.color = color
        # Type of card
        self.type = type
        # Name of card (referred to when saying ... played (name))
        self.name = name
        # Function to perform when card is played
        self.action = action
        # Description of indivisual card
        self.description = description


class NumberCard(Card):
    def __init__(self, color, type):
        Card.__init__(self, color, type)
        self.name = 'a ' + self.color + ' ' + str(self.type)


class ActionCard(Card):
    def __init__(self, color, type):
        Card.__init__(self, color, type)


class Draw2Card(ActionCard):
    def __init__(self, color):
        ActionCard.__init__(self, color, 'draw2')
        self.name = 'a ' + self.color + 'Draw 2 card'

    def action(self):
        pass


class ReverseCard(ActionCard):
    def __init__(self, color):
        ActionCard.__init__(self, color, 'reverse')
        self.name = 'a ' + self.color + 'Reverse card'

    def action(self):
        pass


class SkipCard(ActionCard):
    def __init__(self, color):
        ActionCard.__init__(self, color, 'skip')
        self.name = 'a ' + self.color + 'Skip card'

    def action(self):
        pass


class WildCard(Card):
    def __init__(self):
        Card.__init__(self, 'wild', 'wild')
        self.name = 'a Wild card'

    def action(self):
        pass


class WildDraw4Card(WildCard):
    def __init__(self):
        Card.__init__(self, 'wild', 'wilddraw4')
        self.name = 'a Wild Draw 4 card'

    def action(self):
        pass


class BlankCard(Card):
    def __init__(self):
        Card.__init__(self, None, None)


colors = ['blue', 'green', 'red', 'yellow']
types = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'reverse', 'skip', 'draw2', 'wilddraw4', 'wild']


deck = []

for color in colors:
    for i in range(2):
        for num in range(1, 10):
            deck.append(NumberCard(color, num))

        deck.append(ReverseCard(color))
        deck.append(SkipCard(color))
        deck.append(Draw2Card(color))

    deck.append(NumberCard(color, '0'))

    deck.append(WildCard())
    deck.append(WildDraw4Card())


def get_ordered_deck():
    newDeck = deck
    return newDeck

def get_shuffled_deck():
    newDeck = deck
    random.shuffle(newDeck)
    return newDeck

def shuffle(deck):
    random.shuffle(deck)

if __name__ == "__main__":
    pass


