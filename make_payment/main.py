from make_payment.composition import MakePayment
#from make_payment.aggregation import MakePayment
#from make_payment.domination import Dominations
#from make_payment.association import MakePayment


if __name__ == "__main__":
    pur1 = MakePayment(580, 45)
    print(pur1.returning_charge())

    #domin = Dominations()
    
    #pur2 = MakePayment(200, 100, domin)
    #print(pur2.returning_charge())

    #pur3 = MakePayment(200, 70)
    #print(pur3.returning_change(domin))

    print(pur1._dominations._currency)

    
