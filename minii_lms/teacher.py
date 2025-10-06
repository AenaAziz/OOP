from person import Person
from course import Course
class Teacher:
    def __init__(self, person: Person, ID: str = None, course:Course = None):
        if isinstance(person, Teacher):
            other = person
            self._person = Person(other._person)
            self._ID = other._ID
            self._course = Course(other._course)

        elif isinstance(person, Person):
            self._person, self._ID, self._course = self._validation(person, ID, course)

        else: raise TypeError("Invalid Teacher data") 


    @property
    def person(self): return self._person 
    @person.setter
    def person(self, new_person):
        self._person = self._person_validation(new_person)  

    @property
    def ID(self): return self._ID  
    @ID.setter
    def ID(self, new_ID):
        self._ID = self._ID_validation(new_ID)  

    @property
    def course(self): return self._course 
    @course.setter
    def course(self, new_course):
        self._course = self._course_validation(new_course)


    def _validation(self, person, ID, course):
        person = self._person_validation(person)   
        ID = self._ID_validation(ID)
        course = self._course_validation(course)
        return person, ID, course

    def _person_validation(self, person):
        if not isinstance(person, Person): raise TypeError("Invalid person data")
        return person

    def _ID_validation(self, ID):
        if not isinstance(ID, str): raise TypeError("Invalid ID")
        return ID
    
    def _course_validation(self, course):
        if not isinstance(course, Course): raise TypeError("Invalid Course")
        return course
    
    
    def __str__(self):
        return (f"Teacher personal data:\n"
                f"name is {self._person.name}\n"
                f"ID is {self._ID}\n"
                f"course is {self._course.title}")
     
    def __repr__(self):
        return (f"Teacher personal data:\n"
                f"name: {self._person.name}\n"
                f"ID: {self._ID}\n"
                f"course: {self._course.title}")
    
    



            