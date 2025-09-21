class MakePayment:
    def __init__(self, given, charge, dom_obj):
        self._given = given
        self._charge = charge
        self._dominations = dom_obj
        self._count = {}

    def returning_charge(self):
        change = self._given - self._charge
        self._count = {}

        for v in self._dominations._currency:
            while change >= v:
                self._count[v] = self._count.get(v, 0)+1
                change -= v
        return self._count  