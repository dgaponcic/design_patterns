from functools import reduce
from abstractions.composite import Composite

class Outside(Composite):
  def __init__(self):
    self.playgrounds = []
    self.parking_lots = []
    self._children = set()

  def add_parking_lot(self, parking_lot):
    self.parking_lots.append(parking_lot)
    self._children.add(parking_lot)

  def add_playground(self, playground):
    self.playgrounds.append(playground)
    self._children.add(playground)
    

class ParkingLots:
  def __init__(self, places, area):
    self.area = area
    self.places = places

  def get_area(self):
    return self.area


class Playgrounds:
  def __init__(self, area):
    self.area = area

  def get_area(self):
    return self.area
