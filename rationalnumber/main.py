from rationalnumber import RationalNumber

if __name__ == "__main__":

     r1 = RationalNumber(-6, 8)      
     r2 = RationalNumber(7, - 4)      
     r3 = RationalNumber("-5/-6") 
     r4 = RationalNumber("x/5") 
     r5 = RationalNumber("0")   
     r1 = RationalNumber("-5/2")

     print(r1)   
     print(r2) 

     r2 = RationalNumber(r1)

     print(repr(r4 + r2))
     print(str(r1 - r2))
     print(repr(r3 * r2))
     print(r1 == r2)
     print(str(r5 / r2))
     print(RationalNumber.count)

     

