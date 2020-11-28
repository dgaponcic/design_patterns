from abstractions.observer import Observer

class ApartamentsManager(Observer):
    def __init__(self, family):
        self.family = family

    def update(self, event):
        print("Apartament Manager " + self.family + " was notified. " + event + "\n")
        