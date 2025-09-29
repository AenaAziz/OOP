from calculator_console import CalculationDisplay
class HandHeldCalculator:
    def __init__(self):
        self._c1 = CalculationDisplay()
        self._q_or_r = 'C'

    def run(self):
        while True:
         self.instructions()
         self._c1.input_first_operand()
         self._c1.input_operator()
         self._c1.input_second_operand()
         self._c1.input_equal_to()
         if not self.input_quit_or_exit():
            break

    def input_quit_or_exit(self):
        self._q_or_r = input("Press a button").strip().upper()

        if self._q_or_r not in ('C', 'Q'):
            raise TypeError("invalid type to exit or reset")
        elif self._q_or_r == 'C':
            self.reset()
            return True
        else:
            self.quit()
            return False  
        
    def instructions(self):
        print("Simple Handheld Calculator")
        print("Enter numbers and operators one by one.")
        print("Operators: +, -, *, /")
        print("Enter '=' to compute.")
        print("Enter 'C' to clear/reset.")
        print("Enter 'Q' to quit.")


    def reset(self):
        print("Screen cleared")
        print("Screen")

    def quit(self):
        print ("Calculator turned off") 

if __name__ == "__main__":
    hhc1  = HandHeldCalculator()
    hhc1.run()      