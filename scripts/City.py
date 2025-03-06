from enum import Enum, auto

class CityNames(Enum):
    ALGIERS = auto()
    CAIRO = auto()
    ISTANBUL = auto()
    MOSCOW = auto()
    BAGHDAD = auto()
    RIYADH = auto()
    KARACHI = auto()
    TEHRAN = auto()
    DELHI = auto()
    MUMBAI = auto()
    KOLKATA = auto()
    CHENNAI = auto()
    SAN_FRANCISCO = auto()
    CHICAGO = auto()
    ATLANTA = auto()
    MONTREAL = auto()
    NEW_YORK = auto()
    WASHINGTON = auto()
    LONDON = auto()
    MADRID = auto()
    PARIS = auto()
    ESSEN = auto()
    ST_PETERSBURG = auto()
    MILAN = auto()
    SEOUL = auto()
    BEIJING = auto()
    TOKYO = auto()
    SHANGHAI = auto()
    TAIPEI = auto()
    OSAKA = auto()
    HONG_KONG = auto()
    MANILA = auto()
    HO_CHI_MINH_CITY = auto()
    BANGKOK = auto()
    JAKARTA = auto()
    SYDNEY = auto()
    LOS_ANGELES = auto()
    MEXICO_CITY = auto()
    MIAMI = auto()
    SAO_PAULO = auto()
    LAGOS = auto()
    KHARTOUM = auto()
    SANTIAGO = auto()
    LIMA = auto()
    BOGOTA = auto()
    BUENOS_AIRES = auto()
    KINSHASA = auto()
    JOHANNESBURG = auto()

class DiseaseColor(Enum):
    BLACK = auto()
    RED = auto()
    BLUE = auto()
    YELLOW = auto()

class City():
    def __init__(self, city_name: CityNames, color: DiseaseColor, adjacent: list[CityNames], dictt):
        self.city = city_name
        self.color = color
        self.neighbors = adjacent
        self.disease = dictt