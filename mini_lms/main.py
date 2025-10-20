from student import Student
from student_list import StudentList

def main():
    stu1 = Student("Ahmed", 1)
    stu2 = Student("Ayesha", 2)
    stu3 = Student("Bilal", 3)

    dcs = StudentList(None, 7)
    #print(dcs)

    dcs.add_student(stu1)
    dcs.add_student(stu2)
    dcs.add_student(stu3)
    dcs.students[0].name = "Rizwana"

    print(dcs)

    print("dcs copy")
    dcs_copy = StudentList(dcs)
    print(dcs_copy)

    dcs_copy.add_student_at(1, Student("Fatima", 4))
   # print(dcs)
    #print(dcs_copy) #append/remove will not effect dcs

    #print("Ayeshs is at index", dcs.search_student(2))
    #print("Bilal is at index", dcs.search_student("Bilal"))
    
    dcs.replace(1, Student("Hina", 1))
   # print(dcs)
    #print(dcs_copy) # does not effect dcs_copy

    #dcs.students[0].name = "Rizwana"

    dcs_copy.remove_student(2)
    print(dcs)
    print(dcs_copy)

    print(dcs.size)
    print(dcs_copy.size)
    #print(dcs.capacity)
    


if __name__ == "__main__":
    main()
