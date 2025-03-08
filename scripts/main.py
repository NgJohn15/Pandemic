import logging
import random

# import pygame
from scripts.Deck import Deck
from Deck import Deck
from Card import Card
from Map import Map
from Role import Role, RoleType, get_players

# game data
infection_cards = Deck()
infection_discard = Deck()
player_cards = Deck()
player_discard = Deck()
research_stations: list[str] = []
disease_state = {"blue": 0, "red": 0, "yellow": 0, "black": 0}
outbreak_counter = 0
infection_counter = 0
infection_rate = [2, 2, 2, 3, 3, 4, 4]
board = Map()
game_over = 0


# import networkx as nx
# import matplotlib.pyplot as plt

def visualize_graph(adjacency_list):
    # Create a directed graph from the adjacency list
    G = nx.DiGraph()

    # Add edges to the graph
    for node, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Draw the graph
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_color='black', font_weight='bold', arrows=True)
    plt.title("Graph Visualization")
    plt.show()

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
            print(card.city, card.color, infect, False, card.city)
            board.infect_city(card.city, card.color, infect, False, card.city)
            infection_discard.add_top(card)

def run():
    pass

def turn():
    pass
logging.getLogger().setLevel(logging.DEBUG)
DIFFICULTY = 6
player_count = 4
player_list = get_players(player_count)
setup(player_list, DIFFICULTY)
turn = 0
# visualize_graph(board.map)
while(True):
    player: RoleType = player_list[turn]
    print(f"{player.name()} turn.")
    print("Your hand:")
    player.hand.print()

    if player.actions == 0:
        # next player's turn
        turn = (turn + 1) % player_count
        player.actions = 4 # reset actions
        continue

    print(f"You have {player.actions} actions left")
    print("[0] Drive/Ferry\n[1] Direct Flight\n[2] Charter Flight\n[3] Shuttle Flight\n[4] Build research\n[5] Treat Disease\n[6] Share Knowledge\n[7] Discover Cure")
    action = int(input("What action would you like to take?"))
    assert 0 <= action < 8, "Illegal input [0-7]"

    if action == 0:
        # drive/ferry
        neighbors = board.map.get(player.curr_city)
        print(neighbors)
        new_city = int(input(f"You are in {player.curr_city}. Where would you like to go?"))
        assert new_city in range(len(neighbors)), "Illegal entry"
        player.move_to(neighbors[new_city])
    elif action == 1:
        # direct flight
        player.hand.print(True)
        idx = int(input("Which city would you like to fly to?"))
        card = player.hand.remove_card(idx)
        player_discard.add_top(card)
        player.move_to(card.city)
    elif action == 2:
        # Charter Flight
        card = None
        city = player.curr_city
        for i in player_cards.deck:
            print(i.city, city)
            if i.city == city:
                card = i

        if card is None:
            print("You do not have the city card of the cit you are currently in.")
            continue
        else:
            new_city = input("What city would you like to travel to?")
            assert new_city in board.cities, f"{new_city}"
            player.move_to(new_city)
    elif action == 3:
        # Shuttle Flight
        if player.curr_city in research_stations:
            if len(research_stations < 1):
                print("No other research station to travel to.")
            else:
                count = 0
                new_city = input("Which other research station would you like to travel to?")
                for idx,i in enumerate(research_stations):
                    if i != player.curr_city:
                        print(f"[{count}]", i)
                player.move_to(research_stations[new_city])
        else:
            print(f"{player.name} is unable to use Shuttle Flight right now")
    elif action == 4:
        # Build Research
        if player.build_research():
            research_stations.appen(player.curr_city)
    elif action == 5:
        # Treat Disease
        print(board.disease_map.get(player.curr_city))
        color = input("What disease color would you like to treat?")
        remove_amt = player.treat_disease()
        # check for cured state
        if disease_state[color] > 0:
            remove_amt = 3
        if board.disease_map.get(player.curr_city)[color] > 0:
            curr = board.disease_map.get(player.curr_city)[color]
            if curr - remove_amt < 0:
                curr = 0
            else:
                curr -= remove_amt
            player.actions -= 1
        else:
            print("Not a valid city")
        pass
    elif action == 6:
        # Share Knowledge
        pass
    elif action == 7:
        # Discover cure
        pass
    else:
        print("An error occured.")
