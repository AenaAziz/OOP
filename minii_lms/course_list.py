from course import Course

class CourseList:
    def __init__(self):
        self._capacity = 5
        self._course_list = [None] * self._capacity
        self._size = 0

    @property
    def course_list(self): return self._course_list
    @property
    def capacity(self): return self._capacity
    @property
    def size(self): return self._size

    def expand_capacity(self):
        self._capacity += 5
        self._course_list.extend([None]*5)

    def get_all_courses(self):
        return [(i+1, c) for i, c in enumerate(self._course_list) if c is not None]

    def add(self, course: Course):
        if not isinstance(course, Course):
            raise TypeError("Only Course objects can be added")
        if course in self._course_list:
            raise ValueError("This course already exists in the list")
        if self._size == self._capacity:
            self.expand_capacity()
        self._course_list[self._size] = course
        self._size += 1

    def add_at(self, index: int, course: Course):
        if not isinstance(course, Course) or not isinstance(index, int):
            raise TypeError("Only Course objects and integer index are allowed")
        
        # Remove existing occurrence if present
        if course in self._course_list:
            self.remove(course)
        
        if index < 1 or index > self._size + 1:
            raise IndexError("Index out of range")
        if self._size == self._capacity:
            self.expand_capacity()
        
        # Shift courses to the right
        for j in range(self._size, index-1, -1):
            self._course_list[j] = self._course_list[j-1]
        
        self._course_list[index-1] = course
        self._size += 1

    def remove(self, course: Course):
        if course not in self._course_list:
            raise ValueError("This course does not exist in the list")
        idx = self._course_list.index(course)
        # Shift courses to the left
        for j in range(idx, self._size-1):
            self._course_list[j] = self._course_list[j+1]
        self._course_list[self._size-1] = None
        self._size -= 1

    def remove_at(self, index: int):
        if index < 1 or index > self._size:
            raise IndexError("Index out of range")
        for j in range(index-1, self._size-1):
            self._course_list[j] = self._course_list[j+1]
        self._course_list[self._size-1] = None
        self._size -= 1

    def replace_by_index(self, index: int, course: Course):
        if index < 1 or index > self._size:
            raise IndexError("Index out of range")
        self._course_list[index-1] = course

    def exchange_by_index(self, i: int, j: int):
        if i == j:
            raise IndexError("Indexes cannot be same")
        if not (1 <= i <= self._size) or not (1 <= j <= self._size):
            raise IndexError("Index out of range")
        self._course_list[i-1], self._course_list[j-1] = self._course_list[j-1], self._course_list[i-1]

    def __str__(self):
        courses = [str(c) for c in self._course_list if c is not None]
        return "\n".join(courses) if courses else "No courses in the list."

        
            





        


        

        




            

        
            
             
