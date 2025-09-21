from printer import Printer
from square_sum import SquareSumCalculator

if __name__ == "__main__":

 cal1 = SquareSumCalculator(4)
 sum1 = cal1.sum_square()
 sum2 = cal1.tra_sum_square()
 pri1 = Printer(sum1)
 pri1.display()
 pri2 = Printer(sum2)
 pri2.display()


