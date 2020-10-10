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
Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

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

Factory method pattern is a creational pattern that uses factory methods to deal with the problem of creating objects without having to specify the exact class of the object that will be created.
Factories are used to create apartaments, parking lots, children playgrounds based on the budget.

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

We use it Builder Pattern when:
* We want to create a complex object (an object composed of many parts
and created in different steps that might need to follow a specific order).
* Different representations of an object are required, and we want to keep
the construction of an object decoupled from its representation
* We want to create an object at one point in time but access it at a later point

Builder is used for creating Housing Complex. We can set number of floors, entrances, number of paking lots, whether the lot is closed or has 
surveilance. Also, we can specify the number of rooms and balconies for apartaments. 

As implementation, I gather all information on the builder object. After that, the method build is responsible of creating(by sending data to the constructor of HousingComplex) and returning the newly created object.

The methods that build the objects have to return self so we can chain them(Fluent Builder). Some examples:
```
  def build_parking_lots(self, nb_places):
    self.parking_places += [self.factory.create_parking_place() for _ in range(nb_places)]
    return self
    
  def set_nb_floors(self, floors): 
    if floors <= 0:
      raise "Invalid number of floors"

    self.floors = floors
    return self
```
The building process happens in the build method and HousingComplex.
```
  def build(self):
    nb_apartaments_per_floor = 4
    total_nb_apartaments = self.entrances * self.floors * nb_apartaments_per_floor

    if total_nb_apartaments != len(self.apartaments):
      raise "Incorrect number of apartaments defined. Try again."

    return housingComplex.HousingComplex(self)
```

```
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
```

### Prototype
Prototype is a creational design pattern that lets you copy existing objects without making your code dependent on their classes.

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

### Result

```
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
```
![alt text](https://github.com/dgaponcic/design_patterns/blob/master/creational_DP/tmps.png)
