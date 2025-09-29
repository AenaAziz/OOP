class CalculationDisplay:
    def __init__(self):
         self._a = 0
         self._b = 0
         self._operator =None

    @property
    def a(self):
       return self._a
    
    @property
    def b(self):
       return self._b
    
    @property
    def operator(self):
       return self._operator 

    def input_first_operand(self):
       self._a = float(input("Enter First operand"))
       print(self._a)

    def input_operator(self):
       operator = input("Enter any operators from +,-,*,/").strip()
       if operator not in ['+', '-', '*', '/']: raise TypeError("invalid operator type")
       self._operator = operator
       print(self._operator)

    def input_second_operand(self):
       b = float(input("Enter Second operand"))
       if b == 0 and self._operator == '/': raise ZeroDivisionError("second operand can not be 0")
       self._b = b
       print(self._b) 
       
    def _operation(self):
       if self._operator == '+':
          return self._a + self._b
       elif self._operator == '-':
          return self._a- self._b
       elif self._operator == '/':
          return self._a / self._b
       elif self._operator == '*':
          return self._a * self._b

    def input_equal_to(self):
        eq = input("Enter =:") .strip()
        if eq != '=': raise TypeError("enter =")   
        return self._operation()
   
    
 


      
          
                     