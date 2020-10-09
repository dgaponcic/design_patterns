from enum import Enum
import copy

class Heating(Enum):
    centralized = "centralized"
    autonomous = "autonomous"


class EconomApartament:
    def __init__(self):
        self.price_per_m2 = 500
        self.heating = Heating.centralized
        self.sound_isolation_level = 3
        self.wall_resitance_level = 5

    def set_nb_rooms(self, nb):
        self.nb_rooms = nb

    def set_nb_balconies(self, val):
        self.nb_balconies = val

    def copy(self):
        return copy.deepcopy(self)


class MediumApartament:
    def __init__(self):
        self.price_per_m2 = 650
        self.heating = Heating.autonomous
        self.sound_isolation_level = 6
        self.wall_resitance_level = 7

    def set_nb_rooms(self, nb):
        self.nb_rooms = nb

    def set_nb_balconies(self, val):
        self.nb_balconies = val

    def copy(self):
        return copy.deepcopy(self)

  
class LuxousApartament:
    def __init__(self):
        self.price_per_m2 = 900
        self.heating = Heating.autonomous
        self.sound_isolation_level = 8
        self.wall_resitance_level = 9

    def set_nb_rooms(self, nb):
        self.nb_rooms = nb

    def set_nb_balconies(self, val):
        self.nb_balconies = val

    def copy(self):
        return copy.deepcopy(self)
