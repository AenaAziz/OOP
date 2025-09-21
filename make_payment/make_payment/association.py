
class MakePayment:
    def __init__(self, given, charge):
        self._given = given
        self._charge = charge
        self._count = {}

    def returning_change(self, dominations):
        change = self._given - self._charge
        self._count = {}

        for v in dominations._currency:
            while change >= v:
                self._count[v] = self._count.get(v, 0)+1
                change -= v
        return self._count  
