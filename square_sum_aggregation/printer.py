from square_sum import SquareSumCalculator
class Printer:
    def __init__(self, data:SquareSumCalculator):
        self._data = data

    def display(self):
        print("Square sum:", self._data)
    
