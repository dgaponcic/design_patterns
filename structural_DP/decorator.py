class WithAC:
  def __init__(self, apartament):
    self.apartament = apartament
    apartament.air_conditioner = True
  
  def get_temperature(self, season):
    return "normal" if season == "summer" else self.apartament.get_temperature(season)


class WithAutonomousHeating:
  def __init__(self, apartament):
    self.apartament = apartament
    apartament.autonomous_heating = True

  def get_temperature(self, season):
    return "normal" if season == "autumn" else self.apartament.get_temperature(season)
