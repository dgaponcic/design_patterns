from factory.factory_interface import IFactory
from factory.concrete_buildings.apartaments import LuxousApartament
from factory.concrete_buildings.parking_lots import LuxousParkingLot
from factory.concrete_buildings.playgrounds import LuxousPlaygroung

class FactoryLuxous(IFactory):
    def create_apartament(self):
        return LuxousApartament()

    def create_parking_place(self):
        return LuxousParkingLot()

    def create_childen_playground(self):
        return LuxousPlaygroung()
