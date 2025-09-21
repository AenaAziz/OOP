class SquareSum:
    "association"
    def sum_square(self, n):
        "pythonic looping"
        return sum(pow(i, 2) for i in range(1, n+1))

    def tradi_sum_square(self, n):
        "traditional looping" 
        tot = 0
        for i in range(1, n+1):
            tot += i**2
        return tot
        