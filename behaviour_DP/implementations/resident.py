from abstractions.observer import Observer


class Resident(Observer):
    def __init__(self, family):
        self.family = family

    def update(self, event):
        print("The " + self.family + " was notified. " + event + "\n")
        