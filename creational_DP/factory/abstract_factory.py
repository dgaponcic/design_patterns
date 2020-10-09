from enum import Enum
from factory.factories.econom_factory import FactoryEconom
from factory.factories.medium_factory import FactoryMedium
from factory.factories.luxous_factory import FactoryLuxous

class Budget(Enum):
    econom = "econom"
    medium = "medium"
    luxous = "luxous"


def get_factory(budget_type):
    if budget_type == Budget.econom:
        return FactoryEconom()
    elif budget_type == Budget.medium:
        return FactoryMedium()
    elif budget_type == Budget.luxous:
        return FactoryLuxous()
