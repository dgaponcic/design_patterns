from factory.factory_interface import IFactory

class FactoryMedium(IFactory):
    def create_apartament(self):
        return MediumApartament()

    def create_parking_place(self):
        return MediumParkingLot()

    def create_childen_playground(self):
        return MediumPlaygroung()


class MediumApartament:
  def __init__(self):
    self.price_per_m2 = 650
    self.heating = "autonomous"
    self.sound_isolation_level = 6
    self.wall_resitance_level = 7

  def set_nb_rooms(self, nb):
    self.nb_rooms = nb

  def has_balconies(self, val):
    self.nb_balconies = val


class MediumParkingLot:
  def __init__(self):
    self.parking_type = "indoors"
    self.price = 800
    self.security = False


class MediumPlaygroung:
  def __init__(self):
    self.equipemnt = {"slider": 2, "swing": 3, "tunnel": 2, "see_saw": 1}
    self.bench_nb = 8
