# 48 Card

from City import CityNames, DiseaseColor


class Card():
    def __init__(self, card_type: str, card_contents: str, city: CityNames=None, color: DiseaseColor=None):
        self.card_type = card_type
        self.card_contents = card_contents
        self.city = city
        self.color = color
    
    def print(self) -> str:
        if self.city != None and self.color != None:
            return f"[{self.city.name} {self.color.name} {self.card_contents}]"
        else:
            return f"[{self.card_type} {self.card_contents}]"