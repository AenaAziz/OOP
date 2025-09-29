class DivisionCount:
    def __init__(self, n):
        if isinstance(n, DivisionCount):
            self._n = n._n
        elif isinstance(n, int):
            self._n = self._n_validation(n)
        else: 
            raise TypeError("Invalid number type") 
        self._count = 0 

    @property
    def n(self): return self._n

    @n.setter
    def n(self, value):
        self._n = self._n_validation(value) 
        self._count = 0 

    def _n_validation(self, n):
        if n <= 2:
            raise ValueError("number must be greater than 2")
        return n
    
    def division_counting(self):
        self._count = 0
        k = self._n
        while k > 2: 
            k /= 2
            self._count += 1
        return self._count 

    def __str__(self):
        return f"number is: {self._n} and division count is: {self.division_counting()}"  



        

