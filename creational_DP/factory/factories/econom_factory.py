from factory.factory_interface import IFactory
from factory.concrete_buildings.apartaments import EconomApartament
from factory.concrete_buildings.parking_lots import EconomParkingLot
from factory.concrete_buildings.playgrounds import EconomPlaygroung

class FactoryEconom(IFactory):
    def create_apartament(self):
        return EconomApartament()

    def create_parking_place(self):
        return EconomParkingLot()

    def create_childen_playground(self):
        return EconomPlaygroung()
