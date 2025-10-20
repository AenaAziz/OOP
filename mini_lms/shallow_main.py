from student import Student
from student_list import StudentList
import copy

def main():
    stu1 = Student("Ahmed", 1)
    stu2 = Student("Ayesha", 2)
    stu3 = Student("Bilal", 3)

    dcs = StudentList(None, 7)
    #print(dcs)

    dcs.add_student(stu1)
    dcs.add_student(stu2)
    dcs.add_student(stu3)

    dcs_copy = copy.deepcopy(dcs)
    dcs_copy.add_student_at(1, Student("Fatima", 4))
    dcs.students[1].seat_no = 11
    dcs_copy.replace(1, Student("Hina", 1))
    dcs_copy.remove_student(2)
    print(dcs)
    print(dcs_copy)




if __name__ == "__main__":
    main()    