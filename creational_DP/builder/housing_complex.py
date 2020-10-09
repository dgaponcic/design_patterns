import builder.builder as builder

class HousingComplex:
  Builder = builder.Builder

  def __init__(self, builder):
    self.entrances = builder.entrances
    self.floors = builder.floors
    self.surveilance = builder.surveilance
    self.closed_teritory = builder.closed_teritory
    self.apartaments = builder.apartaments
    self.parking_places = builder.parking_places
    self.playgrounds = builder.playgrounds
