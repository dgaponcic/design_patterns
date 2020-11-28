from abstractions.observer import Subject, Observer
from typing import List


class AparatmentsBlock(Subject):
    residents = []
    administrators = []
    _observers: List[Observer] = []

    def attach(self, observer: Observer):
        print("Subject: Attached a new resident.")
        self._observers.append(observer)


    def detach(self, observer: Observer):
        self._observers.remove(observer)


    def notify(self, event):
        print("Subject: Notifying observers...\n")
        for observer in self._observers:
            observer.update(event)


    def new_resident(self, resident):
        print("A new family has moved to your house")
        self.residents.append(resident)
        event = resident.family + " moved to your house\n"
        self.notify(event)
    
    
    def new_manager(self, administrator):
        print("A new administartor for your block")
        self.administrators.append(administrator)
        event = administrator.family + " is a new administartor\n"
        self.notify(event)
