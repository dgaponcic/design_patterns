from factory.econom_factory import FactoryEconom
from factory.medium_factory import FactoryMedium
from factory.luxous_factory import FactoryLuxous


def get_factory(budget_type):
  if budget_type == "econom":
    return FactoryEconom()
  elif budget_type == "medium":
    return FactoryMedium()
  if budget_type == "luxous":
    return FactoryLuxous()
