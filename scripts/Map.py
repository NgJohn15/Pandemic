import json
import logging


class Map():
    def __init__(self):
        try:
            with open('data/map.json', 'r') as file:
                self.map = json.load(file)
        except:
            print("Error: data.json not found.")
            self.map = {}
        self.disease_map = {}
        self.cities = ["Algiers", "Cairo", "Istanbul", "Moscow", "Baghdad", "Riyadh", "karachi", "Tehran", "Karachi", "Delhi", "Mumbai", "Kolkata", "Chennai", "San Francisco", "Chicago", "Atlanta", "Montreal", "New York", "Washington", "London", "Madrid", "Paris", "Essen", "St. Petersburg", "Milan", "Seoul", "Tokyo", "Shanghai", "Taipei", "Osaka", "Hong Kong", "Manila", "Ho Chi Minh City", "Bangkok", "Jakarta", "Sydney", "Los Angeles", "Mexico City", "Miami", "Sao Paulo", "Lagos", "Khartoum", "Santiago", "Lima", "Bogota", "Buenos Aires", "Kinshasa", "Johanesburg"]

        for city in self.cities:
            self.disease_map[city] = {"Blue": 0, "Red": 0, "Yellow": 0, "Black": 0}
    
    def add_city(self, city_name, adjacent_cities):
        self.map[city_name] = adjacent_cities
    
    def infect_city(self, city_name, disease_color, amount, fromOutbreak: bool, outbreakSource: str):
        current = self.disease_map.get(city_name)[disease_color]
        if current + amount > 3:
            # OUTBREAK
            for neighbor in self.map.get(city_name):
                # Don't outbreak back to the source if the source was an outbreak
                if fromOutbreak and outbreakSource == neighbor:
                    continue
                logging.info(f"OUTBREAK from {outbreakSource} infecting {neighbor}")
                self.infect_city(neighbor, disease_color, 1, True, city_name)
            pass
        else:
            self.disease_map[city_name][disease_color] = self.disease_map.get(city_name)[disease_color] + amount
            logging.info(f"Infected {city_name} curr={self.disease_map[city_name]}")

    def print_state(self):
        for city in self.cities:
            print(city, self.disease_map[city])