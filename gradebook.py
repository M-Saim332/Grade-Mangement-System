from Student import Student

class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no: # Fixed attribute name
                return student
        return None
    
    def top_student(self): # Standardized naming
        if not self.students: return None # Prevents crash on empty list
        
        TS = self.students[0]
        for student in self.students: # Fixed typo
            if student.calculategpa() > TS.calculategpa():
                TS = student # Fixed assignment (was assigning the Class)
        return TS         
    
    def class_average(self): # Standardized naming
        if not self.students: return 0.0 # Prevents division by zero
        
        total = 0
        for student in self.students:
            total += student.calculategpa() # Fixed to use student, not self
        return total / len(self.students) # Moved outside the loop

    def display_all(self):
        for student in self.students:
            student.display_report()    