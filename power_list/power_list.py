class PowerList:
    def __init__(self, pow=0, n=0):
        if isinstance(pow, PowerList):
            self._power = pow._power
            self._n = pow._n
            self._list = pow._list.copy()
        elif isinstance(pow, int) and isinstance(n, int):
            if pow < 0 : raise ValueError("power must be positive")
            self._power = pow
            self._n = n
            self._list = [].copy()
        else: raise TypeError("invalid power type")    

    def n_power_list(self):
        """pythonic"""
        return [pow(self._n, i) for i in range(self._power+1)]
    
    def tra_pow_list(self):
        """traditional"""
        self._list = []
        for i in range(self._power+1):
            self._list.append(self._n ** i)
        return self._list    


    




            

