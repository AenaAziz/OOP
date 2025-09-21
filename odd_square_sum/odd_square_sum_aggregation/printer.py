from odd_square_sum import OddSquareSum

class Printer:
    def __init__(self, cal:OddSquareSum, n:int):
        self._cal = cal
        self._n = n

    def display(self):
        print("odd square sum:", self._cal.odd_squ_sum(self._n)) 

    def show(self):
        print("odd square sum is", self._cal.tra_odd_squ_sum(self._n))       