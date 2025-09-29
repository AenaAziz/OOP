from calculator_console import CalculationDisplay

class Printer:
    def __init__(self):
      """composition"""
      self._op1 = CalculationDisplay()

    def display(self):
        self._op1.input_first_operand()
        self._op1.input_operator()
        self._op1.input_second_operand()
        print(self._op1.input_equal_to())

if __name__ == "__main__":
   pri1 = Printer()
   pri1.display()
   
            

