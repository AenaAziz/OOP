class CreditCard:
    def __init__(self, custumer=None, bank=None, limit=0, acct=None):

        if isinstance(custumer, CreditCard):
         self._custumer = custumer._custumer
         self._bank = custumer._bank
         self._limit = custumer._limit
         self._account = custumer._account
         self._balance = custumer._balance   

        elif isinstance(custumer, str) and isinstance(bank, str) and isinstance(limit, (int, float)) and isinstance(acct, str):
         self._custumer = custumer
         self._bank = bank
         self._limit = limit
         self._account = acct
         self._balance = 0

        else: raise TypeError("Invalid information")

    @property
    def custumer(self): return self._custumer

    @property
    def bank(self): return self._bank

    @property
    def limit(self): return self._limit

    @property
    def account(self): return self._account

    @property
    def balance(self):
       return self._balance

    @custumer.setter
    def custumer(self, name):
        self._custumer = name

    @bank.setter
    def bank(self, name):
        self._bank = name

    @limit.setter
    def limit(self, value):
        self._limit = value   

    @account.setter
    def account(self, number):
        self._account = number

    def charge(self, price):
       if price > 0:
        if self._balance + price <= self._limit: 
          self._balance += price
          return self._balance 
        else: raise ValueError("price must be less than limit")
       else: raise ValueError("price must be greater than 0") 

    def make_payment(self, amount):
          if amount > 0:
           if amount <= self._balance:
            self._balance -= amount 
            return self._balance 
           else: raise ValueError("amount must be less or equal to balance")  
          else: raise ValueError("amount must be greater than 0")   
             
    def __repr__(self):
       return f"balance: {self._balance}"  
    
    def __str__(self):
       return f"balance is:{self._balance}"
    

      


       
             


    





