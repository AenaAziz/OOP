from copy import deepcopy
from person import Person
from course_list import CourseList
class Student:
    def __init__(self, person: Person, seat_no = None, faculty = None, semester = None, course_list:CourseList = None):
        if isinstance(person, Student):
            other = person
            self._person = Person(other._person)
            self._seat_no = other._seat_no
            self._faculty = other._faculty
            self._semester = other._semester
            self._course_list = deepcopy(other._course_list)

        elif isinstance(person, Person):
            self._person, self._seat_no, self._faculty, self._semester, self._course_list = self._student_data_validation(person, seat_no, faculty, semester, course_list)

        else:
            raise TypeError("Invalid Student data")    
        
    def _student_data_validation(self, person, seat_no, faculty, semester, course_list):
        person = self._person_validation(person)
        seat_no = self._seat_no_validation(seat_no)
        faculty = self._faculty_validation(faculty)
        semester = self._semester_validation(semester)
        course_list = self._course_list_validation(course_list)
        return person, seat_no, faculty, semester, course_list

    def _seat_no_validation(self, seat_no):
        if not isinstance(seat_no, str):
            raise TypeError("Seat number must be string")
        return seat_no

    def _faculty_validation(self, faculty):    
        if not isinstance(faculty, str):
            raise TypeError("Faculty must be string")
        return faculty

    def _semester_validation(self, semester):  
        if not isinstance(semester, int) or semester <= 0:
            raise ValueError("Semester must be a positive integer")
        return semester

    def _course_list_validation(self, course_list):   
        if not isinstance(course_list, CourseList):
            raise TypeError("Courses must belong to the CoursList")   
        return course_list
    
    def _person_validation(self, person):
        if not isinstance(person, Person):
         raise TypeError("Invalid student personal data")
        return person
        
    @property
    def person(self): return self._person
    @person.setter
    def person(self, new_person):
        self._person = self._person_validation(new_person)

    @property
    def seat_no(self): return self._seat_no
    @seat_no.setter
    def seat_no(self, new_seat_no):
        self._seat_no = self._seat_no_validation(new_seat_no)  

    @property
    def faculty(self): return self._faculty
    @faculty.setter
    def faculty(self, new_faculty):
        self._faculty = self._faculty_validation(new_faculty)      

    @property
    def course_list(self): return self._course_list
    @course_list.setter
    def course_list(self, new_course_list):
        self._course_list = self._course_list_validation(new_course_list)    

    @property
    def semester(self): return self._semester
    @semester.setter
    def semester(self, new_semester):
        self._semester = self._semester_validation(new_semester)   

    def __str__(self):
        return (f"--- Student Info ---\n"
                f" Personal data: {self._person}\n"
                f" Seat_no is {self._seat_no}\n"
                f" Semester is {self._semester}\n"
                f" Faculty is {self._faculty}\n"
                f" Courses are {self._course_list}")

    def __repr__(self):
        return (f" Personal data: {self._person}\n"
                f" Seat_no: {self._seat_no}\n"
                f" Semester: {self._semester}\n"
                f" Faculty: {self._faculty}\n"
                f" Courses: {self._course_list}")

                    


            


            

            





