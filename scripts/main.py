from Deck import Deck
from Card import Card
from Map import Map
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

# game setup
def setup():
    # https://upload.wikimedia.org/wikipedia/commons/6/6f/Pandemic_game_graph.svg
    black_cities = ["Algiers", "Cairo", "Istanbul", "Moscow", "Baghdad", "Riyadh", "karachi", "Tehran", "Karachi", "Delhi", "Mumbai", "Kolkata", "Chennai"]
    blue_cities = ["San Francisco", "Chicago", "Atlanta", "Montreal", "New York", "Washington", "London", "Madrid", "Paris", "Essen", "St. Petersburg", "Milan"]
    red_cities = ["Seoul", "Tokyo", "Shanghai", "Tapipei", "Osaka", "Hong Kong", "Manila", "Ho Chi Minh City", "Bangkok", "Jakarta", "Sydney"]
    yellow_cities = ["Los Angeles", "Mexico City", "Miami", "Sao Paulo", "Lagos", "Khartoum", "Santiago", "Lima", "Bogota", "Buenos Aires", "Kinshasa", "Johanesburg"]

    # Generate infection cards
    for lst, color in [(black_cities, "Black"), (blue_cities, "Blue"), (red_cities, "Red"), (yellow_cities, "Yellow")]:
        for city in lst:
            infection_cards.add_top(Card("Infection", color, city=city))
    # Generate 
    for lst, color in [(black_cities, "Black"), (blue_cities, "Blue"), (red_cities, "Red"), (yellow_cities, "Yellow")]:
        for city in lst:
            player_cards.add_top(Card("Player", color, city=city))

    # shuffle cards
    infection_cards.shuffle()
    player_cards.shuffle()

    
def run():
    pass

def turn():
    pass

setup()

board.infect_city("Washington", "black", 1, False, None)
board.infect_city("Washington", "black", 1, False, None)
board.infect_city("Washington", "black", 1, False, None)
# should cause an outbreak
board.infect_city("Washington", "black", 1, False, None)
board.print_state()