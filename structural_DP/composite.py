from functools import reduce

class Composite:
  def get_area(self):
    return reduce((lambda x, y: x + y.get_area()), self._children, 0)
