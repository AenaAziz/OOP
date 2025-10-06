from teacher import Teacher
from person import Person
from course import Course

def main():
    per1 = Person("Humera", 42, "14/10/1980", "Female", "Hum345@eraaa.org", "+923304828501")
    per2 = Person("Mukesh", 45, "30/11/1978", "Male", "Muuk345sha@esh.pk", "+923103538610")
    per3 = Person("Bari", 32, "1-02-2003", "Male", "Biiiiii@g.net.pk",  "03356778032")

    c1 = Course("Oops", "CS-101", 25)
    c2 = Course("DS", "DS-101", 22)
    c3 = Course("DLD","DD-101", 20 )
    c4 = Course("ICT","IC-101", 21 )

    t1 = Teacher(per1, "Ub-125", c1)
    t2 = Teacher(per2, "Ub-145", c2)
    t3 = Teacher(per3, "Ub-199", c3)

    print(t1)
    print(repr(t2))
   # print(repr(t3))

    t3.course = c4
    t3.person.name = "SamiulHuda"

    print(t3)

if __name__ == "__main__":
    main()    