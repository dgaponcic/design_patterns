from abstractions.composite import CompositeInterface
from abc import ABC

class LivingSpace(CompositeInterface, ABC):
  def get_temperature(self, season):
    seasons = {"autumn": "chilly", "winter": "normal", "spring": "norm", "summer": "hot"}
    return seasons[season]


class Apartament(LivingSpace):
  def __init__(self, rooms, apartament_nb):
    self.rooms = rooms
    self.apartament_nb = apartament_nb
    self.autonomous_heating = False
    self.air_conditioner = False
  
  def get_area(self):
    return self.rooms * 30


class Townhouse(LivingSpace):
  def __init__(self, rooms, house_nb):
    self.rooms = rooms
    self.house_nb = house_nb
    self.autonomous_heating = False
    self.air_conditioner = False
