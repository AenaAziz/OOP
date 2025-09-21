class Even:
    def __init__(self, k):
        if isinstance(k, Even):
         self._k = k._k
        elif isinstance(k, int):
         self._k = k
        else:
         raise TypeError("\"k\" must be integer")
        
    @property
    def k(self): return self._k

    @k.setter
    def k(self, value):
      if not isinstance(value, int):
        raise TypeError("value must be integer")
      self._k = value
        
    def is_even(self):
      return (self._k & 1) == 0
 
    def __str__(self):
      return f"k is {self._k}"
    