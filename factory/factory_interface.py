from __future__ import annotations
from abc import ABC, abstractmethod


class IFactory(ABC):
    @abstractmethod
    def create_apartament(self):
        pass

    @abstractmethod
    def create_parking_place(self):
        pass

    @abstractmethod
    def create_childen_playground(self):
        pass
      