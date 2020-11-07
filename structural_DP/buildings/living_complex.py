from buildings.living_space import Apartament, Townhouse
from abstractions.composite import Composite
from abc import ABC

class LivingComplex(Composite, ABC):
  def add_parking_lot(self, parking_lot):
    self.outside.add_parking_lot(parking_lot)
  
  def add_playground(self, playground):
    self.outside.add_playground(playground)

  def use_service(self):
    self.service.provide_service()


class ApartamentComplex(LivingComplex):
  def __init__(self, entrances, floors, apartaments_per_floor, service, outside, basement):
    self.entrances = entrances
    self.floors = floors
    self.apartaments_per_floor = apartaments_per_floor
    self.apartaments = []
    self.service = service
    self.outside = outside
    self.basement = basement
    self._children = set([self.outside, self.basement])

  def add_apartament(self, apartament):
    max_nb_apartaments = self.entrances * self.apartaments_per_floor * self.floors

    if max_nb_apartaments == len(self.apartaments):
      raise "Maximum number of apartamens"
    else:
      self.apartaments.append(apartament)
      self._children.add(apartament)


class TownhouseComplex(LivingComplex):
  def __init__(self, floors, entrances, service, outside, basement):
    self.houses = []
    self.floors = floors
    self.entrances = entrances
    self.service = service
    self.outside = outside
    self.basement = basement
    self._children = set([self.outside, self.basement])

  def add_house(self, house):
    if self.entrances == len(self.houses):
      raise "Maximum number of houses"
    else:
      self.houses.append(house)
      self._children.add(house)
