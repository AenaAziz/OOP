class OddSquareSum:
    "aggregation"
    def odd_squ_sum(self, n:int):
        "pythonic"
        return sum(pow(i, 2) for i in range(1, n+1, 2)) 
    
    def tra_odd_squ_sum(self, n:int):
        "traditional"
        tot = 0
        for i in range(1, n +1, 2):
            tot += i**2
        return tot    
 