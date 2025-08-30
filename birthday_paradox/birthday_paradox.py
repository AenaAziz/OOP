import random

class BirthdayParadox:
    def __init__(self, repeat=10000, n=0):

        if isinstance(repeat, int) and isinstance(n, int):
            repeat, n = self.validation(repeat, n)
            self._repeat, self._n = repeat, n
            self._match = 0
            self._probability = 0
            self.matching()
            self.probability()

        elif isinstance(repeat, BirthdayParadox): 
            self._repeat, self._n = repeat._repeat, repeat._n
            self._match = repeat._match
            self._probability = repeat._probability
            return

        else: raise ValueError("repeating desired value is invalid")

    def validation(self, repeat, n):
        if repeat < 0 or n < 0:
            raise ValueError("the value of n or repeat can not be negative") 
        return repeat, n
    
    @property
    def repeat(self): return self._repeat

    @repeat.setter
    def repeat(self, value): 
        if isinstance(value, int) and value > 0:
         self._repeat = value
         self._match = 0
         self.matching()
         self.probability()
        else: raise ValueError("incorrecr repeat value for updating") 

    @property
    def n(self): return self._n

    @n.setter
    def n(self, value):
        if isinstance(value, int) and value > 0:
         self._n = value
         self._match = 0
         self.matching()
         self.probability()
        else: raise ValueError("unmatched n value for updating") 

    def is_same_exist(self, birthdays):
        return len(birthdays) != len(set(birthdays)) 
      
    def matching(self):
        for _ in range(self._repeat):
            birthdays = [random.randint(1, 365) for _ in range(self._n)]
            if self.is_same_exist(birthdays):
                self._match  += 1        

    def probability(self):
        self._probability = self._match / self._repeat

    def __str__(self):
        return f"for {self._n} people the chances of having the same birthday is {self._probability:.3f} "  

    def __repr__(self) :
        return f"people = {self._n} probability = {self._probability:.3f}" 



    








