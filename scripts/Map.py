import json
import logging
from City import DiseaseColor, CityNames, City
from world import world_map


class Map():
    def __init__(self):
        # CITYNAME: City obj
        self.map = world_map
    
    def infect_city(self, cityname: CityNames, disease_color: DiseaseColor, amount, fromOutbreak: bool, outbreakSource: str):
        current = self.map.get(cityname).disease[disease_color]
        if current + amount > 3:
            # OUTBREAK
            for neighbor in self.map.get(cityname).neighbors:
                # Don't outbreak back to the source if the source was an outbreak
                if fromOutbreak and outbreakSource == neighbor:
                    continue
                logging.info(f"OUTBREAK from {outbreakSource} infecting {neighbor}")
                self.infect_city(neighbor, disease_color, 1, True, cityname)
            pass
        else:
            self.map.get(cityname).disease[disease_color] = self.map.get(cityname).disease[disease_color] + amount
            logging.info(f"Infected {cityname.name} curr={self.map.get(cityname).disease}")

    def print_state(self):
        for city in self.cities:
            print(city, self.disease_map[city])