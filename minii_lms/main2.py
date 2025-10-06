from person import Person
from student import Student
from student_list import StudentList
from course import Course
from course_list import CourseList

def run():
    per1 = Person("Ahmed", 21, "14/10/2006", "Male", "Ahmed345@gmail.org", "+923304828501")
    per2 = Person("Ayesha", 20, "30/11/2006", "Female", "Aye345sha@khn.pk", "+923103538610")
    per3 = Person("Hina", 23, "1-02-2003", "Non-Binary", "Hiiiiii@g.net.pk",  "03356778032")
    

    crs1 = Course("Object Oriented Programming", "CS-345", 24)
    crs2 = Course("Descrete Structure", "CS-467", 20)
    crs3 = Course("Digital and Electronic Design", "CS-289", 23)
    crs4 = Course("Applied Physics", "SE-289", 21)
    crs5 = Course("Data Structure", "SE-289", 22)
    crs6 = Course(crs2)
    crs6.course_id = "SE-299"
    crs7 = Course(crs4)
    crs7.course_id = "AT-101"
    crs8 = Course(crs1)
    crs8.course_id = "AI-644"

    crlst1 = CourseList()
    crlst1.add(crs1)
    crlst1.add(crs2)
    crlst1.add(crs3)

    crlst2 = CourseList()
    crlst2.add(crs4)
    crlst2.add(crs5)
    crlst2.add(crs6)

    crlst3 = CourseList()
    crlst3.add(crs7)
    crlst3.add(crs8) 


    stu1 = Student(per1, "B24110006045", "computer science", 2, crlst1)
    stu2 = Student(per2, "B24110007011", "software engineering", 5, crlst2)
    stu3 = Student(stu1)
    stu3.person.name = "Bilal"
    stu3.person.email = "lal000@lion.com"
    stu3.person.phone_no = "03318900045"
    stu3.seat_no = "B24110007011"
    stu4 = Student(per3, "B24110006352", "AI", 7, crlst3)


    stlst1 = StudentList()
    #print(stlst1.get_all_students())
    stlst1.add(stu1)
    #print(stlst1.get_all_students())
    stlst1.add(stu2)
    stlst1.add(stu3)
    stlst1.remove(stu1)
    stlst1.add(stu4)
    #stlst1.add(stu1)
    stlst1.replace(stu4, stu1)
    #print(repr(stlst1))

    stlst1.add_at(1, stu4)
    stlst1.remove_at(1)
    stlst1.exchange_by_index(1, 3)
    print(stlst1.get_all_students())
   # stlst1.add(stu4)
    #stlst1.add(stu4)

    #print(stlst1.size)
    #print(stlst1.capacity)

    
    #stlst1.exchange_index(stu4, stu3)


    #print(stlst1.get_all_students())

    #print(stlst1.search_by_stu_name("Ahmed"))   
    #print(repr(stlst1.search_by_seat_no("B24110007011")))

if __name__ == "__main__":
    run()        



