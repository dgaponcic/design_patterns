import builder.housing_complex as housing_complex

class Builder:
  def __init__(self, factory):
    self.entrances = None
    self.floors = None
    self.surveilance = False
    self.closed_teritory = False
    self.apartaments = []
    self.parking_places = []
    self.playgrounds = []
    self.factory = factory
    self.base_apartament = self.factory.create_apartament()

  def set_nb_floors(self, floors): 
    if floors <= 0:
      raise "Invalid number of floors"

    self.floors = floors
    return self
  
  def set_nb_entrances(self, entrances): 
    if entrances <= 0:
      raise "Invalid number of entrances"

    self.entrances = entrances
    return self

  def build_parking_lots(self, nb_places):
    self.parking_places += [self.factory.create_parking_place() for _ in range(nb_places)]
    return self

  def build_children_playgrounds(self, nb_grounds):
    self.playgrounds += [self.factory.create_childen_playground() for _ in range(nb_grounds)]
    return self

  def add_surveilance(self):
    self.surveilance = True
    return self
  
  def close_teritory(self):
    self.closed_teritory = True
    return self
  
  def build_apartaments(self, nb_apartaments, nb_rooms, nb_balconies):
    for _ in range(nb_apartaments):
      apartament = self.base_apartament.copy()
      apartament.set_nb_rooms(nb_rooms)
      apartament.set_nb_balconies(nb_balconies)
      self.apartaments.append(apartament)
    return self

  def build(self):
    nb_apartaments_per_floor = 4
    total_nb_apartaments = self.entrances * self.floors * nb_apartaments_per_floor

    if total_nb_apartaments != len(self.apartaments):
      raise "Incorrect number of apartaments defined. Try again."

    return housing_complex.ApartamentComplex(self)
    