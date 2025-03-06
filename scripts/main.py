import logging
import random
from Deck import Deck
from Card import Card
from Map import Map
from Role import Role, RoleType, get_players
from City import CityNames, DiseaseColor

# game data
infection_cards = Deck()
infection_discard = Deck()
player_cards = Deck()
player_discard = Deck()
research_stations: dict[str, 0] = {}
disease_state = {"blue": 0, "red": 0, "yellow": 0, "black": 0}
outbreak_counter = 0
infection_counter = 0
INFECTION_RATE = [2, 2, 2, 3, 3, 4, 4]
board = Map()
game_over = 0
DIFFICULTY = 6
PLAYER_COUNT = 4

# game setup
def setup(list_of_players: list[Role], epidemic_no: int):
    # https://upload.wikimedia.org/wikipedia/commons/6/6f/Pandemic_game_graph.svg

    # Generate infection and player cards
    for city in board.map.values():
        infection_cards.add_top(Card("Infection", "", city.city, city.color))
        player_cards.add_top(Card("Player", "", city.city, city.color))
    
    # Generate event cards
    player_cards.add_top(Card("Event",  "RESILIENT POPULATION: Remove any 1 card in the infection discard pile form the game. You may play this between the infect and intensify steps of an epidemic."))
    player_cards.add_top(Card("Event", "ONE QUIET NIGHT: Skip the next infect cities step."))
    player_cards.add_top(Card("Event", "FORECAST: Look and rearrange the top 6 cards of the infection deck."))
    player_cards.add_top(Card("Event", "AIRLIFT: Move any 1 player to any city."))
    player_cards.add_top(Card("Event", "GOVERNMENT GRANT: Add 1 research station to any city (no city card needed)."))

    # shuffle cards
    infection_cards.shuffle()
    player_cards.shuffle()

    # Deal 2 cards per player
    for player in list_of_players:
        count = 2
        if len(list_of_players) == 4:
            count = 2
        elif len(list_of_players) == 3:
            count = 3
        elif len(list_of_players) == 2:
            count = 4
        for i in range(count):
            player.hand.add_top(player_cards.remove_top())

    # add epidemic cards
    div = len(player_cards.deck) // epidemic_no
    start = 0
    end = div
    count = 0
    for _ in range(epidemic_no):
        if count == epidemic_no - 1:
            end = len(player_cards.deck)

        # random insert epidemic card into the deck
        ins = random.randint(start, end-1)
        player_cards.deck.insert(ins, Card("EPIDEMIC", "Increase epidemic level. Pull from bottom, and infect by 3. Shuffle disard pile and add to top of infection deck."))
        start += div+1
        end += div+1
        count += 1
    
    # reverse deck so smaller piles are on the bottom
    player_cards.deck.reverse()

    # infect initial cities
    for infect in range(3, 0, -1):
        for _ in range(3):
            card: Card = infection_cards.remove_top()
            board.infect_city(card.city, card.color, infect, False, card.city)
            infection_discard.add_top(card)

def epidemic() -> None:
    # Increase epidemic level.
    infection_counter += 1
    # Pull infection card from bottom, and infect by 3.
    card = infection_cards.remove_bottom()
    board.infect_city(card.city, card.color, 3, False, card.city)
    # Shuffle disard pile and add to top of infection deck.
    infection_cards.add_stack(infection_discard.shuffle())
    infection_discard.empty()    

def turn():
    pass
logging.getLogger().setLevel(logging.DEBUG)

player_list = get_players(PLAYER_COUNT)

setup(player_list, DIFFICULTY)
turn = 0

while(True):
    player: RoleType = player_list[turn]
    print(f"{player.name()} turn.")
    print("Your hand:")
    player.hand.print()

    if player.actions == 0:
        # next player's turn
        turn = (turn + 1) % PLAYER_COUNT

        print("Player Card Draw 2")
        # Draw 2 Player Cards
        for _ in range(2):
            card1 = player_cards.remove_top()
            if card1.card_type == "EPIDEMIC":
                print("EPIDEMIC PULLED")
                epidemic()
            else:
                player.hand.add_top(card1)
        # Draw {infection_rate} number of infections cards
        for _ in range(INFECTION_RATE[infection_counter]):
            card: Card = infection_cards.remove_top()
            board.infect_city(card.city, card.color, 1, False, card.city)
            infection_discard.add_top(card)
        # End of player's turn
        continue

    print(f"You have {player.actions} actions left")
    print("Drive/Ferry, Direct Flight, Charter Flight, Shuttle Flight, Build research, Treat Disease, Share Knowledge, Discover Cure")
    action = int(input("What action would you like to take?"))

    assert 0 <= action < 8, "Illegal input [0-7]"
    if action == 0:
        # ask player where they want to drive/ferry
        neighbors = board.map.get(player.curr_city).neighbors
        print([x.name for x in neighbors])
        new_city = int(input(f"You are in {player.curr_city.name}. Where would you like to go?"))
        assert new_city in range(len(neighbors)), "Illegal entry"
        player.move_to(neighbors[new_city])
    elif action == 1:
        # direct flight
        player.hand.print(True)
        idx = int(input("Which city would you like to fly to?"))
        card = player.hand.remove_card(idx)
        player_discard.add_top(card)
        player.move_to(card.city)
    else:
        player.actions -= 1