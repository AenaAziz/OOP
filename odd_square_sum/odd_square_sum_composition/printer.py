class Printer:
    "composition"
    def __init__(self, n:int):
        if n < 0: raise ValueError("n must be positive")
        self._n = n
        self._result = sum(pow(i, 2) for i in range(1, self._n+1, 2))

    def display(self):
        "pythonic"
        print("Odd Square Sum:", self._result)   

    def _traditional_calculation(self):
        total = 0
        for i in range(1, self._n+1, 2):
            total += i ** 2
        return total    

    def show(self):
        "traditional"
        result = self._traditional_calculation()
        print("odd square sum is", result)


        



