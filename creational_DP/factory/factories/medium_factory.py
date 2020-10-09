from factory.factory_interface import IFactory
from factory.concrete_buildings.apartaments import MediumApartament
from factory.concrete_buildings.parking_lots import MediumParkingLot
from factory.concrete_buildings.playgrounds import MediumPlaygroung

class FactoryMedium(IFactory):
    def create_apartament(self):
        return MediumApartament()

    def create_parking_place(self):
        return MediumParkingLot()

    def create_childen_playground(self):
        return MediumPlaygroung()
