# Creational Design Patterns

Creational patterns provide various object creation mechanisms, which increase flexibility and reuse of existing code.

## Task
To use reational design patterns in real life situations. 

The topic used is Housing Complexes. The process of building a big housing complex with many apartaments, parking lots, playgrounds etc for different budgets.

## Implementation
The project is written in Python 3.8.5

Patterns used in the repository:

* Abstract Factory
* Factory method
* Builder
* Prototype

### Abstract Factory

An abstract factory is used here in order to obtain a factory based on the budget allocated for the building. 

```
def get_factory(budget_type):
    if budget_type == Budget.econom:
        return FactoryEconom()
    elif budget_type == Budget.medium:
        return FactoryMedium()
    elif budget_type == Budget.luxous:
        return FactoryLuxous()
```

### Factory method

Factories are used to create apartaments, parking lots, children playgrounds grouped by budget.

```
class FactoryEconom(IFactory):
    def create_apartament(self):
        return EconomApartament()

    def create_parking_place(self):
        return EconomParkingLot()

    def create_childen_playground(self):
        return EconomPlaygroung()
```

### Builder

Builder is used for creating Housing Complex. We can set number of floors, entrances, number of paking lots, whether the lot is closed or has 
surveilance. Also, we can specify the number of rooms and balconies for apartaments. 

```
  housing_complex = (HousingComplex.Builder(factory)
                              .set_nb_floors(10)
                              .set_nb_entrances(4)
                              .build_parking_lots(100)
                              .build_children_playgrounds(2)
                              .close_teritory()
                              .build_apartaments(100, 2, 1)
                              .build_apartaments(60, 3, 2)
                              .build())
```

### Prototype
Prototype is used for copying the base apartament returned by a factory and changing it as needed.

```
  def build_apartaments(self, nb_apartaments, nb_rooms, nb_balconies):
    for _ in range(nb_apartaments):
      apartament = self.base_apartament.copy()
      apartament.set_nb_rooms(nb_rooms)
      apartament.set_nb_balconies(nb_balconies)
      self.apartaments.append(apartament)
    return self
```

