class Student:
    def __init__(self, name, seat_no = None):
        if isinstance(name, Student):
            other = name
            self._name = other._name
            self._seat_no = other._seat_no

        elif isinstance(name, str):
            self._name, self._seat_no = self._student_data_validation(name, seat_no)
        else:
            raise TypeError("Invalid Student data")    
        
    def _student_data_validation(self, name, seat_no):
        name = self._name_validation(name)
        seat_no = self._seat_no_validation(seat_no)
        return name, seat_no

    def _seat_no_validation(self, seat_no):
        if not isinstance(seat_no, int):
            raise TypeError("Seat number must be integer")
        return seat_no
    
    def _name_validation(self, name):
        if not isinstance(name, str):
         raise TypeError("Invalid student name")
        return name
        
    @property
    def name(self): return self._name
    @name.setter
    def name(self, new_name):
        self._name = self._name_validation(new_name)

    @property
    def seat_no(self): return self._seat_no
    @seat_no.setter
    def seat_no(self, new_seat_no):
        self._seat_no = self._seat_no_validation(new_seat_no)  

    def __str__(self):
        return (f"--- Student Info ---\n"
                f" Name is {self._name}\n"
                f" Seat_no is {self._seat_no}\n")

    def __repr__(self):
        return (f" Name: {self._name}\n"
                f" Seat_no: {self._seat_no}\n")

                    


            


            

            





