# Structural Design Patterns

Structural patterns explain how to assemble objects and classes into larger structures while keeping these structures flexible and efficient.

## Task
To use structural design patterns in real life situations. 

The topic used is Housing Complexes. The process of building a big housing complex with many apartaments, parking lots, playgrounds etc.

## Implementation
The project is written in Python 3.8.5

Patterns used in the repository:

* Decorator
* Bridge
* Composite


### Decorator
Decorator pattern allows a user to add new functionality to an existing object without altering its structure.

The Decorator is used to add air conditioner and autonomous heating to apartaments.
The temperatures in a default apartament or house:


```
  def get_temperature(self, season):
    seasons = {"autumn": "chilly", "winter": "normal", "spring": "norm", "summer": "hot"}
    return seasons[season]
```
An example of decorator is the one to add air conditioner:

```
class WithAC:
  def __init__(self, apartament):
    self.apartament = apartament
    apartament.air_conditioner = True
  
  def get_temperature(self, season):
    return "normal" if season == "summer" else self.apartament.get_temperature(season)
```
The code used to test the decorator:
```
  basic_apartament = Townhouse(5, 2)
  print(basic_apartament.get_temperature("summer"))
  print(basic_apartament.get_temperature("autumn"))

  nice_apartament = WithAC(WithAutonomousHeating(basic_apartament))
  print(nice_apartament.get_temperature("summer"))
  print(nice_apartament.get_temperature("autumn"))
```
The result:

![alt text](https://github.com/dgaponcic/design_patterns/blob/master/structural_DP/decorator.png)

### Bridge
The bridge pattern is a design pattern used in software engineering that is meant to decouple an abstraction from its implementation so that the two can vary independently.

The construction company cand build different types of complexes, for example a simple complex of apartaments or a townhouse.

For the building process the company might need different services: design services, plumbing services, electrician services.

We use bridge so that the buildings and services can be extended independently.

```
  design_service = DesignService()
  apartament_complex = ApartamentComplex(3, 5, 4, design_service, Outside(), Basement(100))
  apartament_complex.add_apartament(Apartament(2, 25))
  apartament_complex.use_service()

  plumbing_service = PlumbingService()
  townhouse_complex = TownhouseComplex(3, 5, plumbing_service, Outside(), Basement(150))
  townhouse_complex.add_house(Townhouse(2, 5))
  townhouse_complex.use_service()
```
The result:

![alt text](https://github.com/dgaponcic/design_patterns/blob/master/structural_DP/bridge.png)



### Composite

Composite is a structural design pattern that lets you compose objects into tree structures and then work with these structures as if they were individual objects.

We use composite pattern to calculate the total area of the complex. We have composite class that is used for composites elements(complexes or outside yard which is composed of parking places and playgrounds) and leaves(apartaments, playgrounds, basement). 

The diagram:

![alt text](https://github.com/dgaponcic/design_patterns/blob/master/structural_DP/composite_diagram.png)


The Composite class and the function for area calculation:
```
class Composite:
  def get_area(self):
    return reduce((lambda x, y: x + y.get_area()), self._children, 0)
```

And the classes inherit from the composite class:

```
class TownhouseComplex(LivingComplex):
```

The leaves have the function get_area():
```
class Apartament(LivingSpace):
  def __init__(self, rooms, apartament_nb):
    self.rooms = rooms
    self.apartament_nb = apartament_nb
    self.autonomous_heating = False
    self.air_conditioner = False
  
  def get_area(self):
    return self.rooms * 30
```

```
  designer_company = DesignService()
  apartament_complex = ApartamentComplex(3, 5, 4, designer_company, Outside(), Basement(150))
  apartament_complex.add_apartament(Apartament(2, 25))
  apartament_complex.add_apartament(Apartament(3, 26))
  apartament_complex.add_playground(Playgrounds(100))
  apartament_complex.add_parking_lot(ParkingLots(100, 200))
  print("The total area of the complex is: ", apartament_complex.get_area())
```

The result:

![alt text](https://github.com/dgaponcic/design_patterns/blob/master/structural_DP/composite.png)



