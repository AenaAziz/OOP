from handheld_calculator import HandHeldCalculator
class Printer:
    def __init__(self):
        self._hhc1 = HandHeldCalculator()

    def show(self):
        while True:
         self._hhc1.instructions()
         self._hhc1.input_a()
         self._hhc1.input_operator()
         self._hhc1.input_b()
         self._hhc1.input_equal_to()
         if not self.input_quit_or_exit():
            break

    def input_quit_or_exit(self):
        choice = input("Press a button").strip().upper()
        if choice == 'C':
            self._reset()
            return True
        elif choice == 'Q':
            self._quit()
            return False
        else:
            print("Invalid choice. Please press C or Q.")
            return True  # loop continues

    def _reset(self):
        print("Screen cleared")
        print("Screen")

    def _quit(self):
        print ("Calculator turned off") 
        
if __name__ == "__main__":
    app = Printer()
    app.show()        

        
        



