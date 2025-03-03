import logging
import random
from Deck import Deck
from Card import Card
from Map import Map
from Role import Role, get_players

# game data
infection_cards = Deck()
infection_discard = Deck()
player_cards = Deck()
player_discard = Deck()
research_stations: dict[str, 0] = {}
disease_state = {"blue": 0, "red": 0, "yellow": 0, "black": 0}
outbreak_counter = 0
infection_counter = 0
infection_rate = [2, 2, 2, 3, 3, 4, 4]
board = Map()
game_over = 0

# game setup
def setup(list_of_players: list[Role], epidemic_no: int):
    # https://upload.wikimedia.org/wikipedia/commons/6/6f/Pandemic_game_graph.svg
    black_cities = ["Algiers", "Cairo", "Istanbul", "Moscow", "Baghdad", "Riyadh", "karachi", "Tehran", "Karachi", "Delhi", "Mumbai", "Kolkata", "Chennai"]
    blue_cities = ["San Francisco", "Chicago", "Atlanta", "Montreal", "New York", "Washington", "London", "Madrid", "Paris", "Essen", "St. Petersburg", "Milan"]
    red_cities = ["Seoul", "Tokyo", "Shanghai", "Taipei", "Osaka", "Hong Kong", "Manila", "Ho Chi Minh City", "Bangkok", "Jakarta", "Sydney"]
    yellow_cities = ["Los Angeles", "Mexico City", "Miami", "Sao Paulo", "Lagos", "Khartoum", "Santiago", "Lima", "Bogota", "Buenos Aires", "Kinshasa", "Johanesburg"]

    # Generate infection and player cards
    for lst, color in [(black_cities, "Black"), (blue_cities, "Blue"), (red_cities, "Red"), (yellow_cities, "Yellow")]:
        for city in lst:
            infection_cards.add_top(Card("Infection", color, city, color))
            player_cards.add_top(Card("Player", color, city, color))
    
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
    for i in range(epidemic_no):
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
            card = infection_cards.remove_top()
            print(card.city, "infected by", infect)
            board.infect_city(card.city, card.color, infect, False, card.city)
            infection_discard.add_top(card)

def run():
    pass

def turn():
    pass
logging.getLogger().setLevel(logging.DEBUG)
DIFFICULTY = 6
player_list = get_players(4)
setup(player_list, DIFFICULTY)
turn = 0
while(game_over):
    pass

