class Course:
    def __init__(self, title: str = None, id: str = None, credit_hours: int = 1):   
        if isinstance(title, Course):
            self._title = title._title
            self._course_id = title._course_id
            self._credit_hours = title._credit_hours

        elif isinstance(title, str):
            self._title, self._course_id, self._credit_hours = self._validation(title, id, credit_hours)    

        else:
            raise TypeError("Invalid course data")

    @property
    def title(self): return self._title
    @title.setter
    def title(self, new_title):
        self._title = self._title_validation(new_title)

    @property
    def course_id(self): return self._course_id
    @course_id.setter
    def course_id(self, new_course_id):
        self._course_id = self._course_id_validation(new_course_id)    

    @property
    def credit_hours(self): return self._credit_hours
    @credit_hours.setter
    def credit_hours(self, new_credit_hours):
        self._credit_hours = self._credit_hours_validation(new_credit_hours)    

    def __str__(self):
        return f"Course title is {self._title}\nCourse code is {self._course_id}\nCourse credit hours are {self._credit_hours}"    
    
    def __repr__(self):
        return f"{self._title}, {self._course_id}, {self._credit_hours}\n"  

    def _validation(self, title, id, credit_hours):
        title = self._title_validation(title)  
        id = self._course_id_validation(id)  
        credit_hours =self._credit_hours_validation(credit_hours)  
        return title, id, credit_hours
    
    def _title_validation(self, title):
        if not isinstance(title, str): raise TypeError("Invalid title")
        title = title.strip()
        if not title:
            raise ValueError("Course title cannot be empty")
        if len(title) > 40:
            raise ValueError("Course title too long")
        return title
    
    def _course_id_validation(self, id):
        if not isinstance(id, str): raise TypeError("Invalid course code")
        if len(id) != 6: raise ValueError("Invalid length for course_id")
        if not (id[:2].isupper() and id[:2].isalpha()): raise ValueError("Code must contain capital letters in the start")
        if id[2] != '-' : raise ValueError("course id must contain '-' after prefix")
        if not id[3:].isdigit(): raise ValueError("Code_id must contain numbers")
        return id
    
    def _credit_hours_validation(self, credit_hours):
        if not isinstance(credit_hours, int): raise TypeError("Invalid credit hours")
        if credit_hours <= 0: raise ValueError("Credit hours must be atleast one")
        return credit_hours

    
