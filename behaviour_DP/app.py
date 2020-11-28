from implementations.resident import Resident
from implementations.administrator import ApartamentsManager
from implementations.apartament_block import AparatmentsBlock


def if_subscribe(aparatments_block, person):
    val = input("Do you want to subscribe to block's updates? ").lower()
    if val == "yes" or val == "y":
        aparatments_block.attach(person)


if __name__ == "__main__":
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
