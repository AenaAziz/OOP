class Multiple:
    def __init__(self, n=0, m=0):
        if isinstance(n, Multiple):
            self._n, self._m = n._n, n._m
        elif isinstance(n, int) and isinstance(m, int):
            self._n, self._m = n, m
        else:
            raise TypeError("Invalid type")   

    @property
    def n(self): return self._n     
    @property
    def m(self): return self._m

    @n.setter
    def n(self, value):
        if not isinstance(value, int): raise TypeError("invalid n type")
        self._n = value
    @m.setter
    def m(self, value):
        if not isinstance(value, int): raise TypeError("invalid m type")
        self._m = value    
    
    def __str__(self):
        return f"n is {self._n} and m is {self._m}"    
    
    def is_multiple(self):
        if self._m == 0: 
            return self._n == self._m
        return self._n % self._m == 0