from factory.factory_interface import IFactory
import copy

class FactoryEconom(IFactory):
    def create_apartament(self):
        return EconomApartament()

    def create_parking_place(self):
        return EconomParkingLot()

    def create_childen_playground(self):
        return EconomPlaygroung()


class EconomApartament:
  def __init__(self):
    self.price_per_m2 = 500
    self.heating = "centralized"
    self.sound_isolation_level = 3
    self.wall_resitance_level = 5

  def set_nb_rooms(self, nb):
    self.nb_rooms = nb

  def set_nb_balconies(self, val):
    self.nb_balconies = val

  def copy(self):
    # First, let's create copies of the nested objects.
    # some_li/
    # return new
    return copy.deepcopy(self)


class EconomParkingLot:
  def __init__(self):
    self.parking_type = "outside" 
    self.price = 100
    self.security = False


class EconomPlaygroung:
  def __init__(self):
    self.equipemnt = {"slider": 1, "swing": 2, "see_saw": 1}
    self.bench_nb = 5
