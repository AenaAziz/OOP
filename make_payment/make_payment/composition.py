from make_payment.domination import Dominations
class MakePayment:
    def __init__(self, given, charge):
        self._given = given
        self._charge = charge  
        self._dominations = Dominations()
        self._count = {}

    @property
    def given(self): return self._given
    @property
    def charge(self): return self._charge


    def returning_charge(self):
        change = self._given - self._charge
        self._count = {}

        for v in self._dominations._currency:
            while change >= v:
                self._count[v] = self._count.get(v, 0)+1
                change -= v
        return self._count   