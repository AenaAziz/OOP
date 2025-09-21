class SquareSumCalculator:
    "aggregation"
    def __init__(self, n:int):
        if n < 0: raise ValueError("n can not be negative")
        self._n = n

    def sum_square(self):
        "pythonic"
        return sum(pow(i, 2) for i in range(1, self._n+1))

    def tra_sum_square(self):
        "traditional"
        tot = 0
        for i in range(1, self._n+1):
            tot += i ** 2
        return tot
       
    