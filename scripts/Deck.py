import random
from typing import List
import Card

class Deck():
    def __init__(self):
        self.deck: List = [] # queue data structure

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def add_top(self, card: Card):
        self.deck.insert(0, card)

    def remove_top(self) -> Card:
        # check for empty
        if len(self.deck) > 0:
            return self.deck.pop(0)
        else:
            return None

    def remove_bottom(self) -> Card:
        # check for empty
        if len(self.deck) > 0:
            return self.deck.pop(-1)
        else:
            return None
    
    def print(self):
        for card in self.deck:
            print(card.print())