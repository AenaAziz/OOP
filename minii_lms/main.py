from person import Person
from course import Course
from course_list import CourseList

def run():
    per1 = Person("Aena", 19, "26-08-2006", "Female", "aenaaziz1246@gmail.com", "+923304828501")
    print(repr(per1))
    per1._date_of_birth = "17/12/1978"
    print(per1.phone_no)
    per2 = Person(per1)
    per2.phone_no = "03145475676"
    print(per2.phone_no)
  #  per3 = Person("donu", 67)

    course1 = Course("Object Oriented Programming", "CS-345", 24)
    print(repr(course1))
    course2 = Course(course1)
    course2.course_id = "CS-495"
    print(course2)
    course3 = Course("Descrete Structure", "CS-467", 20)
    print(course3)

    cl1 = CourseList()
    cl1.add(course1)
    cl1.add_at(2, course3)

    print(cl1.search_by_course_id("CS-467"))
    #print(cl1.get_all_courses)
    cl1.exchange_by_index(1, 2)
    print(cl1.get_all_courses())
    cl1.remove(course1)
    print(cl1.get_all_courses())
    cl1.remove_at(1)
    print(cl1.get_all_courses())
    



if __name__ == "__main__":
    run()    