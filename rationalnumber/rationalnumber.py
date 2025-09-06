from functools import total_ordering
import math

@total_ordering
class RationalNumber:
    count = 0
    def __init__(self, neo=0, deno=1):

        if isinstance(neo, RationalNumber):
            self._neo = neo._neo
            self._deno = neo._deno

        elif isinstance(neo, int) and isinstance(deno, int): 
            self._neo, self._deno = neo, self.validation(deno)

        elif isinstance(neo, str) and deno == 1: self.letter_case(neo)

        else:
            raise TypeError("Invalid input type for RationalNumber")

        self.simplification()
        self.signing() 

        RationalNumber.count += 1  

    @property
    def neo(self):
        return self._neo

    @neo.setter
    def neo(self, value):
        if not isinstance(value, int):
            raise TypeError("Invalid neomenator for changing")
        self._neo = value
        self.simplification()
        self.signing() 

    @property
    def deno(self):
        return self._deno

    @deno.setter
    def deno(self, value):
        if not isinstance(value, int):
         raise TypeError("denomenator must be positive")
        self._deno = self.validation(value)  
        self.simplification()
        self.signing() 

    @classmethod
    def num_rational(cls):
        return cls.count          

    def validation(self, deno):
             if deno == 0:
              raise ZeroDivisionError("Denomenator must not be equal to \"0\"")
             return deno
             
    def letter_case(self, neo):
        parts  = neo.split("/")
        if len(parts) != 2:
            raise ValueError("your entered value must be in the form like neomenator/denomenator")  
        try:
            neo, deno = int(parts[0]), int(parts[1])
        except ValueError:
         raise ValueError("Both numerator and denominator must be integers")    
        self._neo, self._deno = neo, self.validation(deno)

    def simplification(self):
        gcd_value = math.gcd(self._neo, self._deno)
        self._neo //= gcd_value
        self._deno  //= gcd_value

    def signing(self):
        if self._deno < 0:
            self._neo = -self._neo
            self._deno = -self._deno

    def __add__(self, other):
         other = self.other_validation(other)
         return RationalNumber((self._neo * other._deno) + (other._neo * self._deno),  self._deno * other._deno)    
    
    def __sub__(self, other):
        other = self.other_validation(other)
        return RationalNumber((self._neo * other._deno) - (other._neo * self._deno), self._deno * other._deno)
 
    def __mul__(self, other):
        other = self.other_validation(other)
        return RationalNumber((self._neo * other._neo), (self._deno * other._deno))
    
    def __truediv__(self, other):
        other = self.other_validation(other)
        if other._neo == 0:
            raise ZeroDivisionError("Cannot divide by zero rational number")
        return RationalNumber((self._neo * other._deno), (other._neo * self._deno))
    
    def __eq__(self, other):
        other = self.other_validation(other)
        return self._neo == other._neo and self._deno == other._deno
    
    def __lt__(self, other):
        other = self.other_validation(other)
        return self._neo * other._deno < other._neo * self._deno

        
    def __str__(self):
        return f"{self._neo}/{self._deno}"
    
    def __repr__(self):
        return f"RationalNumber({self._neo}, {self._deno})"  

    def other_validation(self, other):
       if not isinstance(other, RationalNumber):
        raise TypeError("other type is invalid")
       return other 
