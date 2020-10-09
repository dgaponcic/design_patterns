from enum import Enum

class Equipment(Enum):
    slider = "slider"
    swing = "swing"
    see_saw = "see_saw"
    tunnel = "tunnel"
    trampoline = "trampoline"
    climbing_wall = "climbing_wall"


class EconomPlaygroung:
    def __init__(self):
        self.equipment = {"slider": 1, "swing": 2, "see_saw": 1}
        self.bench_nb = 5


class MediumPlaygroung:
    def __init__(self):
        self.equipment = {"slider": 2, "swing": 3, "tunnel": 2, "see_saw": 1}
        self.bench_nb = 8


class LuxousPlaygroung:
    def __init__(self):
        self.equipment = {"slider": 3, "swing": 4, "trampoline": 1, "climbing_wall": 1, "see_saw": 2}
        self.bench_nb = 15
