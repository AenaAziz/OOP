from student import Student
from student_list_clas import StudentList

def main():
    stu1 = Student("Ahmed", 1)
    stu2 = Student("Ayesha", 2)
    stu3 = Student("Bilal", 3)

    dcs = StudentList(7)
    #print(dcs)

    dcs.add_student(stu1)
    dcs.add_student(stu2)
    dcs.add_student(stu3)
    dcs.students[0].name = "Rizwana"

    print(dcs)

    dcs_copy = StudentList.from_existing(dcs)
    print(dcs_copy)

    dcs_copy.add_student(stu1)
    print(dcs_copy)

if __name__ == "__main__":
    main()