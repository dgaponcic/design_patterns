# Behaviour Design Patterns

Behavioral design patterns are concerned with algorithms and the assignment of responsibilities between objects.

## Task
To use structural design patterns in real life situations. 

The topic used is Housing Complexes. The process of adding residents and administrators to a block of apartaments and notifing all the current actors.
a big housing complex with many apartaments, parking lots, playgrounds etc.

## Implementation
The project is written in Python 3.8.6

Patterns used in the repository:

* Observer


### Observer
Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects 
about any events that happen to the object they’re observing.

The Observer is used in the project in order to notify all the residents and administrators of an apartament block about updates that happen.


```
    def notify(self, event):
        print("Subject: Notifying observers...\n")
        for observer in self._observers:
            observer.update(event)
```
In order to receive or stop receiving notifications use attach and detach functions:

```
    def attach(self, observer: Observer):
        print("Subject: Attached a new resident.")
        self._observers.append(observer)


    def detach(self, observer: Observer):
        self._observers.remove(observer)
```


The pattern is used in a small client app:
```
    aparatments_block = AparatmentsBlock()

    while True:
        print("Introduce 1 for moving in to the building")
        print("Introduce 2 to register as administrator")


        val = int(input())
        family = input("Your family name: ")

        if val == 1:
            resident = Resident(family)
            aparatments_block.new_resident(resident)
            if_subscribe(aparatments_block, resident)
        elif val == 2:
            manager = ApartamentsManager(family)
            aparatments_block.new_manager(manager)
            aparatments_block.attach(manager)

```
The result:

![alt text](https://github.com/dgaponcic/design_patterns/blob/master/behaviour_DP/result.png)



