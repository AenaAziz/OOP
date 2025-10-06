from course import Course
from course_list import CourseList 

def run():    
    c1 = Course("Introduction to Computer Science", "CS-101", 25)
    c2 = Course("Calculus I", "MA-101", 22)
    c3= Course("Physics I","PH-101", 20 )
    c4 = Course("English Literature", "EN-101", 19)
    c5 = Course("Data Structures", "CS-102", 27)

    clist = CourseList()

    # Add courses
    clist.add(c1)   
    clist.add(c2)
    clist.add(c3)

    #print("After adding 3 courses:")
    #print(clist)
    #print("----------")

    # Add a course at specific index (will shift elements if necessary)
    clist.add_at(2, c4)
    #print("After adding c4 at index 2:")
    #print(clist)
    #print("----------")

    clist.remove(c2)
    #print("After removing c2:")
    #print(clist)
    #print("----------")

# Replace a course at an index
    clist.replace_by_index(1, c5)
    #print("After replacing index 1 with c5:")
    #print(clist)
    #print("----------")

# Exchange courses by index
    clist.exchange_by_index(2, 3)
    #print("After exchanging courses at index 2 and 3:")
    #print(clist)
    #print("----------")

# Remove course at index
    clist.remove_at(2)
    #print("After removing course at index 2:")
    #print(clist)
    #print("----------")

    print(clist.get_all_courses())

if __name__ == "__main__":
    run()
