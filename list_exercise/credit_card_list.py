from credit_card import CreditCard

class CreditCardList:
     
    wallet = []

    wallet.append(CreditCard("Kaneez Fatima", "AlHabib", 20000, "BH783021"))
    wallet.append(CreditCard("Kaneez Fatima", "Allied", 15000, "14672032"))
    wallet.append(CreditCard("Kaneez Fatima", "HBL", 40000, "567asd367"))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print(f"Custumer:{wallet[c].custumer}")  
        print(f"Bank:{wallet[c].bank}") 
        print(f"Limit:{wallet[c].limit}")  
        print(f"Account Number:{wallet[c].account}") 

        while wallet[c]._balance > 100:
            new_balance = wallet[c].make_payment(100) 
            print(f"new balnce = {new_balance}") 

        print()    
  
   






