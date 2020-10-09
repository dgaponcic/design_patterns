from enum import Enum

class Parking_type(Enum):
    indoors = "indoors"
    outside = "outside"


class EconomParkingLot:
    def __init__(self):
        self.parking_type = Parking_type.outside
        self.price = 100
        self.security = False


class MediumParkingLot:
    def __init__(self):
        self.parking_type = Parking_type.indoors
        self.price = 800
        self.security = False


class LuxousParkingLot:
    def __init__(self):
        self.parking_type = Parking_type.indoors
        self.price = 1500
        self.security = True
