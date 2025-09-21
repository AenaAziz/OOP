from square_sum import SquareSum

class Printer:
    def display(self, sum:SquareSum, n:int):
        print("Sum of Squares:", sum.sum_square(n))

    def traditional_display(self, sum:SquareSum, n:int):
        print("Sum of Squares traditionally:", sum.tradi_sum_square(n))  