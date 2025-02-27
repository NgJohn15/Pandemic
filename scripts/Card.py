# 48 Card

class Card():
    def __init__(self, card_type, card_contents, city=None):
        self.card_type = card_type
        self.card_contents = card_contents
        self.city = city
    
    def print(self):
        print(f"[{self.card_type} {self.card_contents} {self.city}]")