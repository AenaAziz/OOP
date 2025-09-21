class Printer:
    "composition"
    def __init__(self, n:int):
        if n < 0: raise ValueError("n must be positive")
        self._total = sum(pow(i, 2) for i in range(1, n+1))
        self._n =n #for traditional loop

    def display(self):
        print("Sum of Squares:", self._total)

    def _traditional_sum_square(self):
        tot = 0
        for i in range(1, self._n+1):
            tot += i ** 2
        return tot
    
    def traditional_result_display(self):
        result = self._traditional_sum_square()
        print("through traditional sum of square:", result)
       


