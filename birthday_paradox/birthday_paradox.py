import random

class BirthdayParadox:
    def __init__(self, repeat=10000, n=2):

        if isinstance(repeat, int) and isinstance(n, int):
            self._repeat, self._n = self._validation(repeat, n)
            self._match = 0

        elif isinstance(repeat, BirthdayParadox): 
            self._repeat, self._n = repeat._repeat, repeat._n
            self._match = repeat._match

        else: raise TypeError("invalid type of repeat and n")

    def _validation(self, repeat, n):
        if repeat < 0 or n < 0:
            raise ValueError("the value of n or repeat can not be negative") 
        if n < 2:
           raise ValueError("the probability can not be found if the number of people is less than 2 ") 
        return repeat, n
    
    @property
    def repeat(self): return self._repeat

    @repeat.setter
    def repeat(self, value): 
        if not isinstance(value, int): raise TypeError("incorrect repeat type for updating") 
        self._validation(value, self._n)
        self._repeat = value
        self._match = 0
        
    @property
    def n(self): return self._n

    @n.setter
    def n(self, value):
        if not isinstance(value, int):raise TypeError("unmatched n type for updating") 
        self._validation(self._repeat, value)
        self._n = value
        self._match = 0 

    def is_same_exist(self, birthdays):
        return len(birthdays) != len(set(birthdays)) 
      
    def _matching(self):
        for _ in range(self._repeat):
            birthdays = [random.randint(1, 365) for _ in range(self._n)]
            if self.is_same_exist(birthdays):
                self._match  += 1        

    def probability(self):
        self._match = 0
        self._matching()
        return self._match / self._repeat

    def __str__(self):
        return f"for {self._n} people the chances of having the same birthday is {self.probability()} "  

    def __repr__(self) :
        return f"people = {self._n} probability = {self.probability()}" 



    








