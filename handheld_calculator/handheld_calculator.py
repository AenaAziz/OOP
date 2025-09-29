class HandHeldCalculator:
    def __init__(self):
        self._a = 0
        self._b = 0
        self._oper = None

    @property
    def a(self):return self._a 
    @property
    def b(self):return self._b 
    @property
    def operator(self):return self._oper

    def instructions(self): 
        print("Simple Handheld Calculator Enter numbers and operators one by one. \n Operators: +, -, *, /Enter '=' to compute.\n Enter 'C' to clear/reset. \nEnter 'Q' to quit.")

    def input_a(self):
        self._a = float(input("press a button"))
        print("Screen", self._a)

    def input_operator(self):
        oper = input("press a button").strip()
        if oper not in ['+', '-', '/', '*']:
            raise TypeError("Invalid operator type")
        self._oper = oper
        print("Screen", self._a , self._oper)

    def input_b(self):
        b = float(input("press a button"))
        if self._oper == '/' and b == 0: raise ZeroDivisionError("second operand can not bre zero")
        self._b = b
        print("Screen", self._a, self._oper, self._b) 

    def _operations(self):
        if self._oper == '+':
            return self._a + self._b    
        elif self._oper == '-':
            return self._a - self._b  
        elif self._oper == '*':
            return self._a * self._b  
        elif self._oper == '/':
            return self._a / self._b    

    def input_equal_to(self):
        eq = input("press a button").strip()
        if  eq != '=': raise TypeError("= must come")
        print("Screen", self._operations())




  

  





