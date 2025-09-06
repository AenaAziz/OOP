from student import Student

class StudentList:
    def run(self):
        data = []

        data.append(Student("Anaya Asim", 6, 67, "Physics", "70%"))
        data.append(Student("Anaya Asim", 6, 81, "English", "67%"))
        data.append(Student("Anaya Asim", 6, 50, "Maths", "90%"))

        for c in range(3):
            print(f"name: {data[c].name}")
            print(f"rollno: {data[c].rollno}")
            print(f"marks: {data[c].marks}")
            print(f"subject: {data[c].subject}")
            print(f"attendence: {data[c].attendence}")
            print()