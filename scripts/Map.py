class Map():
    def __init__(self):
        self.map = {"Algiers": ["Madrid", "Paris", "Istanbul", "Cairo"],
                    "Cairo": ["Algiers", "khartoum", "Istanbul", "Baghdad", "Riyadh"],
                    "Istanbul": ["Milan", "St. Petersburg", "Moscow", "Baghdad", "Cairo", "Aligers"],
                    "Moscow": ["St. Petersburg", "Istanbul", "Tehran"],
                    "Baghdad": [],
                    "Riyadh": [],
                    "karachi": [],
                    "Tehran": [],
                    "Karachi": [],
                    "Delhi": [],
                    "Mumbai": [], "Kolkata": [], "Chennai": [], "San Francisco": [], "Chicago": [], "Atlanta": [], "Montreal": [], "New York": [], "Washington": [], "London": [], "Madrid": [], "Paris": [], "Essen": [], "St. Petersburg": [], "Milan": [], "Seoul": [], "Tokyo": [], "Shanghai": [], "Tapipei": [], "Osaka": [], "Hong Kong": [], "Manila": [], "Ho Chi Minh City": [], "Bangkok": [], "Jakarta": [], "Sydney": [], "Los Angeles": [], "Mexico City": [], "Miami": [], "Sao Paulo": [], "Lagos": [], "Khartoum": [], "Santiago": [], "Lima": [], "Bogota": [], "Buenos Aires": [], "Kinshasa": [], "Johanesburg": []}
        self.disease_map = {}
        self.cities = ["Algiers", "Cairo", "Istanbul", "Moscow", "Baghdad", "Riyadh", "karachi", "Tehran", "Karachi", "Delhi", "Mumbai", "Kolkata", "Chennai", "San Francisco", "Chicago", "Atlanta", "Montreal", "New York", "Washington", "London", "Madrid", "Paris", "Essen", "St. Petersburg", "Milan", "Seoul", "Tokyo", "Shanghai", "Tapipei", "Osaka", "Hong Kong", "Manila", "Ho Chi Minh City", "Bangkok", "Jakarta", "Sydney", "Los Angeles", "Mexico City", "Miami", "Sao Paulo", "Lagos", "Khartoum", "Santiago", "Lima", "Bogota", "Buenos Aires", "Kinshasa", "Johanesburg"]

        for city in self.cities:
            self.disease_map[city] = {"blue": 0, "red": 0, "yellow": 0, "black": 0}
    
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
                print("OUTBREAK")
                self.infect_city(neighbor, disease_color, 1, True, city_name)
            pass
        else:
            self.disease_map[city_name][disease_color] = self.disease_map.get(city_name)[disease_color] + amount
            print("Infected", city_name, f"curr={self.disease_map[city_name]}")

    def print_state(self):
        for city in self.cities:
            print(city, self.disease_map[city])