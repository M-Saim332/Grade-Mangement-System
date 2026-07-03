from gradebook import GradeBook
from Subject import Subjects
from Student import Student
# ---------------- Main Program ----------------

g = GradeBook()

s1 = Student("Ali", 101, 2)
s1.addsubject(Subjects("Math", 3, "A"))
s1.addsubject(Subjects("Physics", 4, "B"))

s2 = Student("Sara", 102, 2)
s2.addsubject(Subjects("Math", 3, "A"))
s2.addsubject(Subjects("Physics", 4, "A"))

g.add_student(s1)
g.add_student(s2)

g.display_all()

print("\nTop Student:", g.top_student().name)
print("Class Average GPA:", g.class_average())