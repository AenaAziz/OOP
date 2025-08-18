import math

class RationalNumber:

    count = 0

    def __init__(self, neo=0, deno=1):

        if isinstance(neo, RationalNumber):
            self._neo = neo._neo
            self._deno = neo._deno

        elif isinstance(neo, int) and isinstance(deno, int): self.validation(neo, deno)

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
        self._neo = value

    @property
    def deno(self):
        return self._deno

    @deno.setter
    def deno(self, value):
        self._deno = value   

    @classmethod
    def num_rational(cls):
        return cls.count          

    def validation(self, neo, deno):

             if deno == 0:
              raise ZeroDivisionError("Denomenator must not be equal to \"0\"")
            
             self._neo, self._deno = neo, deno
        
        
    def letter_case(self, neo):

        parts  = neo.split("/")

        if len(parts) != 2:
            raise ValueError("your entered value must be in the form like neomenator/denomenator")
        
        try:
            neo, deno = int(parts[0]), int(parts[1])
        except ValueError:
         raise ValueError("Both numerator and denominator must be integers")    

        if deno == 0:
            raise ZeroDivisionError("Denominator must not be zero")
        self._neo, self._deno = neo, deno



    def simplification(self):

        gcd_value = math.gcd(self._neo, self._deno)

        self._neo //= gcd_value
        self._deno  //= gcd_value


    def signing(self):

        if self._deno < 0:
            self._neo = -self._neo
            self._deno = -self._deno

    def __add__(self, other):
        return RationalNumber((self._neo * other._deno) + (other._neo * self._deno),  self._deno * other._deno)    
    
    def __sub__(self, other):
        return RationalNumber((self._neo * other._deno) - (other._neo * self._deno), self._deno * other._deno)
 
    def __mul__(self, other):
        return RationalNumber((self._neo * other._neo), (self._deno * other._deno))
    
    def __truediv__(self, other):
        if other._neo == 0:
         raise ZeroDivisionError("Cannot divide by a fraction with numerator 0")
        return RationalNumber((self._neo * other._deno), (other._neo * self._deno))
    
    def __eq__(self, other):
     return self._neo == other._neo and self._deno == other._deno
        

    def __str__(self):
        return f"{self._neo}/{self._deno}"
    
    def __repr__(self):
        return f"RationalNumber({self._neo}, {self._deno})"    

