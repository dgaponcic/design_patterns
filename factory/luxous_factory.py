from factory.factory_interface import IFactory

class FactoryLuxous(IFactory):
    def create_apartament(self):
        return LuxousApartament()

    def create_parking_place(self):
        return LuxousParkingLot()

    def create_childen_playground(self):
        return LuxousPlaygroung()


class LuxousApartament:
  def __init__(self):
    self.price_per_m2 = 900
    self.heating = "autonomous"
    self.sound_isolation_level = 8
    self.wall_resitance_level = 9

  def set_nb_rooms(self, nb):
    self.nb_rooms = nb

  def has_balconies(self, val):
    self.nb_balconies = val


class LuxousParkingLot:
  def __init__(self):
    self.parking_type = "indoors" 
    self.price = 1500
    self.security = True


class LuxousPlaygroung:
  def __init__(self):
    self.equipemnt = {"slider": 3, "swing": 4, "trampoline": 1, "climbing_wall": 1, "see_saw": 2}
    self.bench_nb = 15
