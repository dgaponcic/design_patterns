from buildings.living_space import Apartament, Townhouse
from buildings.living_complex import ApartamentComplex, TownhouseComplex
from decorator import WithAirConditioner, WithAutonomousHeating
from services import DesignService, PlumbingService
from peripherical_building.outside import Outside, Playgrounds, ParkingLots
from peripherical_building.basement import Basement


if __name__ == "__main__":
  # Decorator
  print("Decorator")
  basic_apartament = Townhouse(5, 2)
  print(basic_apartament.get_temperature("summer"))
  print(basic_apartament.get_temperature("autumn"))

  nice_apartament = WithAirConditioner(WithAutonomousHeating(basic_apartament))
  print(nice_apartament.get_temperature("summer"))
  print(nice_apartament.get_temperature("autumn"))


  # Bridge
  print("\nBridge")
  print("Apartament complex:")
  design_service = DesignService()
  apartament_complex = ApartamentComplex(3, 5, 4, design_service, Outside(), Basement(100))
  apartament_complex.add_apartament(Apartament(2, 25))
  apartament_complex.use_service()

  print("\nTownhouse:")
  plumbing_service = PlumbingService()
  townhouse_complex = TownhouseComplex(3, 5, plumbing_service, Outside(), Basement(150))
  townhouse_complex.add_house(Townhouse(2, 5))
  townhouse_complex.use_service()


  # Composite
  print("\nComposite")
  designer_company = DesignService()
  apartament_complex = ApartamentComplex(3, 5, 4, designer_company, Outside(), Basement(150))
  apartament_complex.add_apartament(Apartament(2, 25))
  apartament_complex.add_apartament(Apartament(3, 26))
  apartament_complex.add_playground(Playgrounds(100))
  apartament_complex.add_parking_lot(ParkingLots(100, 200))
  print("The total area of the complex is: ", apartament_complex.get_area())
