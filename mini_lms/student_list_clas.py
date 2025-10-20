from student import Student

class StudentList:
    def __init__(self,  capacity: int = 5):                              
            self._capacity = capacity
            self._students: list[None | Student] = [None] * self._capacity
            self._size = 0

    @classmethod
    def from_existing(cls, other):
        return cls(other.capacity)        

    @property
    def capacity(self): return self._capacity
    @capacity.setter
    def capacity(self, new_capacity: int):
        self._capacity = self._capacity_validation(new_capacity)

    @property
    def students(self): return self._students

    @property
    def size(self): return self._size

    def _capacity_validation(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        return capacity
    
    def _expand_capacity(self):
        """Double the capacity when array is full"""
        self._capacity *= 2
        new_array: list[None | Student] = [None] * self._capacity
        for i in range(self._size):
            new_array[i] = self._students[i]
        self._students = new_array

    def add_student(self, student: Student):
        """Add the student if the seat number is unique."""
        student = self._student_validation(student)
        if self._size == self._capacity:
            self._expand_capacity()
        self._students[self._size] = student
        self._size += 1

    def add_student_at(self, idx: int, stu: Student):
        """Insert Student at a specific index (with shifting)."""
        stu = self._student_validation(stu)
        if idx < 0 or idx > self._size:
            raise IndexError("Index out of bound")
        if self._size == self._capacity:
            self._expand_capacity()
        for i in range(self._size, idx, -1):
            self._students[i] = self._students[i-1]
        self._students[idx] = stu
        self._size += 1

    def _student_validation(self, stu):
        """Check that the student is valid and unique."""
        if not isinstance(stu, Student):
            raise TypeError("Only Student objects can be added")
        for i in range(self._size):
            if self._students[i].seat_no == stu.seat_no:
                raise ValueError("Error: Seat number already exists!")
        return stu    

    def search_student(self, key):
        """Search by seat_no(int) or name(str); return index or -1."""
        for i in range(self._size):
            if isinstance(key, int) and self._students[i].seat_no == key:
                return i
            if isinstance(key, str) and self._students[i].name.lower() == key.lower():
                return i
        return -1   

    def replace(self, seat_no: int, new_student: Student):
        """Replace Student at a given seat number."""
        idx = self._find_index_by_seat_no(seat_no)
        if idx == -1:
            raise ValueError("Seat number does not exist in the list")
        self._students[idx] = new_student

    def remove_student(self, seat_no: int):
        """Remove student by seat number (shifting left)."""
        idx = self._find_index_by_seat_no(seat_no)
        if idx == -1:
            raise ValueError("Seat number does not exist in the list")
        for i in range(idx, self._size-1):
            self._students[i] = self._students[i+1]
        self._students[self._size-1] = None    
        self._size -= 1

    def _find_index_by_seat_no(self, seat_no):
        for i in range(self._size):
            if self._students[i].seat_no == seat_no:
                return i
        return -1
    
    def __str__(self):
        """String representation of the student list."""
        if self._size == 0:
            return "Student List is Empty"
        result = "Student List:\n"
        for i in range(self._size):
            result += f"{i+1}. {self.students[i]}\n"
        return result 
        



        

        



            
    











