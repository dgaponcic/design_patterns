from abstractions.composite import CompositeInterface

class Basement(CompositeInterface):
  def __init__(self, area):
    self.area = area

  def get_area(self):
    return self.area
