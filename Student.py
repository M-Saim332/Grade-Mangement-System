from Subject import Subjects

class Student:
    def __init__(self, name, roll_no, semester): # Standardized roll_no
        self.name = name
        self.roll_no = roll_no
        self.semester = semester
        self.subject_list = []

    def addsubject(self, subject):
        self.subject_list.append(subject)

    def calculategpa(self):
        total_points = 0
        total_credits = 0
        for subject in self.subject_list:
            grade_points = subject.Calculate_Grade_Points()
            total_points += grade_points * subject.credithour 
            total_credits += subject.credithour
            
        # Moved outside the loop
        if total_credits == 0: 
            return 0 
        return total_points / total_credits

    def display_report(self):
        print("\nStudent Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Semester:", self.semester)
        print("Subjects:")
        
        for subject in self.subject_list:  # Fixed variable name
            print(subject.subjectname, "-", subject.grade)

        print("GPA:", self.calculategpa()) # Fixed method name