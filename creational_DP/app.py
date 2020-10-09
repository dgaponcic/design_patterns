import factory.abstract_factory as abstract_factory
from builder.housing_complex import HousingComplex
from factory.abstract_factory import Budget

def main():
  factory = abstract_factory.get_factory(Budget.luxous)

  housing_complex = (HousingComplex.Builder(factory)
                              .set_nb_floors(10)
                              .set_nb_entrances(4)
                              .build_parking_lots(100)
                              .build_children_playgrounds(2)
                              .close_teritory()
                              .build_apartaments(100, 2, 1)
                              .build_apartaments(60, 3, 2)
                              .build())

main()
