from student import Student
class StudentList:
    def __init__(self):
        self._capacity = 5
        self._student_list = [None] * self._capacity
        self._size = 0

    @property
    def capacity(self): return self._capacity

    @property
    def student_list(self): return self._student_list

    @property
    def size(self): return self._size

    def get_all_students(self):
        result = []
        for i, stu in enumerate(self._student_list):
            if stu is not None:
               result.append(f"{i+1}. {stu}")
        return "\n".join(result) if result else "No students found."
    
    def __str__(self):
        return f"Students in list:\n{self.get_all_students()}"
    
    def __repr__(self):
        return f"Students list:{self.get_all_students()}" 
    
    def expand_capacity(self):
        self._capacity += 5
        self._student_list.extend([None] * 5)

    def add(self, stu:Student):
        student = self._stu_validation(stu)
        student = self._has_stu(student)
        if self._for_empty_slot(student): return
        if self._size == self._capacity:
           self.expand_capacity()
        self._student_list[self._size] = student
        self._size += 1  

    def _for_empty_slot(self, student):
        for i in range(self._capacity):
            if self._student_list[i] is None:
                self._student_list[i] = student
                self._size += 1
                return True
        return False    

    def _has_stu(self, student):
        if student in self._student_list:
            raise ValueError("This student already exists in the list")      
        return student    
        
    def _stu_validation(self, student):
        if not isinstance(student, Student):
            raise TypeError("Only Student instances can be added to StudentList.") 
        return student 
    
    def remove(self, stu:Student):
        student = self._stu_validation(stu) 
        if self._does_stu_exist(student):
            i = self._student_list.index(student)
            for j in range(i, self._size-1):
                self._student_list[j] = self._student_list[j+1]
            self._student_list[self._size-1] = None
            self._size -= 1      

    def _does_stu_exist(self, student): 
        if not student in self._student_list:
            raise ValueError("This student does not exist in the student list")
        return True
    
    def search_by_stu_name(self, name:str):
        name = self._name_validation(name)
        for stu in self._student_list:
            if stu is not None and stu.person.name.rstrip().capitalize() == name:
                return stu
        return None    

    def _name_validation(self, name):
        if not isinstance(name, str):
            raise TypeError("Invalid name type to search")
        return name.rstrip().capitalize()
    
    def search_by_seat_no(self, seat_no:str):
        seat_no = self._seat_no_validation(seat_no)
        for stu in self.student_list:
            if stu is not None and stu.seat_no.rstrip().upper() == seat_no:
                return stu
        return None    

    def _seat_no_validation(self, seat_no):
        if not isinstance(seat_no, str):
            raise TypeError("Invalid seat number")
        return seat_no.rstrip().upper()

    def replace(self, stu1: Student, stu2:Student):
        stu1, stu2 = self._students_validation(stu1, stu2)
        if self._student_list[self._student_list.index(stu1)] is None:
            raise ValueError("There is no student at this index to replace")
        self._student_list[self._student_list.index(stu1)] = stu2

    def _students_validation(self, stu1, stu2):
        if not isinstance(stu1, Student) or not isinstance(stu2, Student):
            raise TypeError("Invalid Student types for replacement")  
        if not stu1 in self._student_list or stu2 in self._student_list :
            raise ValueError("Student1 is not in the list or student2 is already exist in the list")
        return stu1, stu2

    def _index_type_validation(self, index):
        if not isinstance(index, int):
            raise IndexError("Index must be integer")   
        if index < 1 or index > self._size + 1:
            raise IndexError("Index out of bound")
        return index
    
    def exchange_index(self, stu1:Student, stu2:Student):
        st1, st2 = self._students_validation(stu1, stu2)
        s1, s2 = self._do_students_exist(st1, st2)
        i, j = self._student_list.index(s1), self._student_list.index(s2)
        self._student_list[i], self._student_list[j] = self._student_list[j], self._student_list[i]

    def _students_validation(self, stu1, stu2):
        if not isinstance(stu1, Student) or not isinstance(stu2, Student):
            raise TypeError("Invalid student types for exchanging index")
        return stu1, stu2 

    def _do_students_exist(self, st1, st2):
        if not st1 in self._student_list or not st2 in self._student_list:
            raise ValueError("Student(s) do(es) not exist in the list") 
        return st1, st2 
    
    #Now by index

    def add_at(self, i: int, stu: Student):
        i = self._index_type_validation(i)
        stu = self._stu_validation(stu)
        if stu in self._student_list:
            self.remove(stu)
        for j in range(self._size, i-1, -1):
            self._student_list[j] = self._student_list[j-1]
        self._student_list[i-1] = stu
        self._size += 1     

    def remove_at(self, i: int):
        i = self._index_type_validation(i)
        if self._student_list[i-1] is None:
            raise IndexError("No Student is found at this index")
        for j in range(i-1, self._size-1):
            self._student_list[j] = self._student_list[j+1]
        self._student_list[self._size-1] = None
        self._size -=1

    def exchange_by_index(self, i, j):
        i, j = self._indices_validation(i, j) 
        self._student_list[i-1], self._student_list[j-1] = self._student_list[j-1], self._student_list[i-1]

    def _indices_validation(self, i, j):
        if not isinstance(i, int) or not isinstance(j, int):
            raise TypeError("Invalid indices typefor exchange")
        if i < 1 or i > self._size or j < 1 or j > self._size:
            raise IndexError("Index out of bound")
        if i == j:
            raise IndexError("Both index are same")
        return i, j
    
    def search_by_index(self, i: int):
        i = self._index_type_validation(i)
        return self._student_list[i-1]
    
    def replace_by_index(self, i: int, stu: Student):
        i = self._index_type_validation(i)
        stud = self._stu_validation(stu)
        student = self._has_stu(stud)
        if self._student_list[i-1] is None:
            raise ValueError("No student in the list to replace")
        self._student_list[i-1] = student
        
    def exchange_by_indices(self, i, j):
        i, j = self._indices_validation(i, j)
        self._student_list[i], self._student_list[j] = self._student_list[j], self._student_list[i]
        




    

        


    



            
        

    



    
    
        

        

       
               
        