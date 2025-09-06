class Student:
    def __init__(self, name, rollno, marks, subject, attendence):
        self._name = name
        self._rollno = rollno
        self._marks = marks
        self._attendence = attendence
        self._subject = subject

    def result(self):
        if self._marks < 50:
            print(f"Fail")
        else:
            print(f"pass")

    @property
    def name(self): return self._name    

    @property
    def rollno(self): return self._rollno        

    @property
    def marks(self): return self._marks   

    @property
    def subject(self): return self._subject  

    @property
    def attendence(self): return self._attendence   