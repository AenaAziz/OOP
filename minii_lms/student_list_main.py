from course import Course
from course_list import CourseList
from student_list import StudentList
from student import Student
from person import Person

def main():
    c1 = Course("Introduction to Computer Science", "CS-101", 25)
    c2 = Course("Calculus I", "MA-101", 22)
    c3= Course("Physics I","PH-101", 20 )
    c4 = Course("English Literature", "EN-101", 19)
    c5 = Course("Data Structures", "CS-102", 27)

    clist = CourseList()

    # Add courses
    clist.add(c1)   
    clist.add(c2)

    per1 = Person("Ahmed", 21, "14/10/2006", "Male", "Ahmed345@gmail.org", "+923304828501")
    per2 = Person("Ayesha", 20, "30/11/2006", "Female", "Aye345sha@khn.pk", "+923103538610")
    per3 = Person("Hina", 23, "1-02-2003", "Non-Binary", "Hiiiiii@g.net.pk",  "03356778032")

    stu1 = Student(per1, "B24110006045", "computer science", 2, clist)#Ahmed
    stu2 = Student(per2, "B24110007011", "software engineering", 5, clist)#Ayesha
    stu4 = Student(per3, "B24110006352", "AI", 7, clist)#Hina
    stu3 = Student(stu1)#Bilal
    stu3.person.name = "Bilal"
    stu3.person.email = "lal000@lion.com"
    stu3.person.phone_no = "03318900045"
    stu3.seat_no = "B24110007011"


    slst = StudentList()
    #print("giving admissions to three students") 
    slst.add(stu1)
    slst.add(stu2)
    slst.add(stu3)
    #print(slst)

    slst.exchange_index(stu1, stu3)
    #print(slst)

    slst.replace(stu1, stu4)
    #print(slst)
    
   # print("A new student joined the semester in the middle")
    slst.add_at(2, stu4)
   # print(slst)

    
   #print("DSC office is in the searching of the student by seat no  and name ")
   #print(slst.search_by_seat_no("B24110006352"))
   # print(slst.search_by_stu_name("Ayesha"))

    #print("A student update his name in the dcs office")
    stu2.person.name = "Aisha"
    #print (slst.search_by_stu_name("aisha"))

    #print("A student update his seat number in the dcs office")
    stu1.seat_no = "B24110006044"
    #print (slst.search_by_seat_no("B24110006044"))

    print("A student leave the department through index")
    slst.remove_at(2)
   # print(slst.get_all_students())

   # slst.remove(stu1)
    #print(slst.get_all_students())
    slst.exchange_by_index(1, 2)
    slst.replace_by_index(1, stu1)
    print(slst.get_all_students())





    



    












if __name__ == "__main__":
    main()

