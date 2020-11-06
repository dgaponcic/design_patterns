from living_space import Apartament, Townhouse
from living_complex import ApartamentComplex, TownhouseComplex
from decorator import WithAC, WithAutonomousHeating
from services import DesignService
from outside import Outside, Playgrounds, ParkingLots
from basement import Basement


if __name__ == "__main__":
  # Decorator

  # basic_apartament = Townhouse(5, 2)
  # print(basic_apartament.get_temperature("summer"))
  # print(basic_apartament.get_temperature("autumn"))

  # nice_apartament = WithAC(WithAutonomousHeating(basic_apartament))
  # print(nice_apartament.get_temperature("summer"))
  # print(nice_apartament.get_temperature("autumn"))


  # Bridge

  # designer_company = DesignService()
  # apartament_complex = ApartamentComplex(3, 5, 4, designer_company, Outside(), Basement())
  # apartament_complex.add_apartament(Apartament(2, 25))
  # apartament_complex.use_service()


  # Composite

  designer_company = DesignService()
  apartament_complex = ApartamentComplex(3, 5, 4, designer_company, Outside(), Basement())
  apartament_complex.add_apartament(Apartament(2, 25))
  apartament_complex.add_apartament(Apartament(3, 26))
  apartament_complex.add_playground(Playgrounds(100))
  apartament_complex.add_parking_lot(ParkingLots(100, 100))
  print(apartament_complex.get_area())
