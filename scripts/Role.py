import random
from Deck import Deck

def get_players(players: int) -> list:
    if players > 4 or players < 1:
        print("Invalid player count, setting to default (4 players)")
        players = 4    
    return random.sample([Dispatcher(), Medic(), Scientist(), Researcher(), Operations(), ContingencyPlanner(), QuarantineSpecialist()], players)

class Role():
    def __init__(self):
        self.hand = Deck()
"""
Dispatcher: Moves pawns and performs actions by clicking on icons
Medic: Helps treat patients
Scientist: Conducts research
Researcher: Shares knowledge by giving other players city cards
Operations Expert: Builds research stations and moves between them
Contingency Planner: Prepares for emergencies
Quarantine Specialist: Prevents outbreaks
"""

class Dispatcher(Role):
    """
    The Dispatcher, as an action, can either move any pawn, with the owner's agreement, to any city containing another pawn, or move another player's pawn, with the owner's agreement, as if it were his own. The Dispatcher is limited to moving other players' pawns and cannot direct them to perform other actions like Treating Disease. 
    """
    def __init__(self):
        super().__init__()

class Medic(Role):
    """
    The Medic, during the Treat Disease action, removes all cubes (not just one) of the same color. If a disease has been cured, the Medic automatically removes all cubes of that color from a city by entering it or being there. This does not consume an action. The Medic also prevents the placement of disease cubes (and outbreaks) of cured diseases in his location.
    """
    def __init__(self):
        super().__init__()

class Scientist(Role):
    """
    The Scientist requires only 4 (not 5) City cards of the same disease color to Discover a Cure for that disease. 
    """
    def __init__(self):
        super().__init__()

class Researcher(Role):
    """
    During the Share Knowledge action, the Researcher may give any City card from her hand to another player in the same city as her, without this card having to match her city. The transfer must be from her hand to the other player’s hand, but it can occur on either player’s turn. 
    """
    def __init__(self):
        super().__init__()

class Operations(Role):
    """
    The Operations Expert can, as an action, either build a research station in his current city without discarding (or using) a City card, or once per turn, move from a research station to any city by discarding any City card. 
    """
    def __init__(self):
        super().__init__()

class ContingencyPlanner(Role):
    """
    The Contingency Planner can, as an action, retrieve an Event card from anywhere in the Player Discard Pile and place it on his Role card. Only one Event card can be on his role card at a time, and it doesn't count against his hand limit. When the Contingency Planner plays the Event card on his role card, it is removed from the game instead of being discarded. 
    """
    def __init__(self):
        super().__init__()

class QuarantineSpecialist(Role):
    """
    The Quarantine Specialist prevents both outbreaks and the placement of disease cubes in the city she is in and all cities connected to that city. This prevention does not apply to cubes placed during setup. 
    """
    def __init__(self):
        super().__init__()