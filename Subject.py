class Subjects:
    def __init__(self, subjectname, credithour, grade):
        self.subjectname = subjectname
        self.credithour = credithour
        self.grade = grade.upper()  

    def Calculate_Grade_Points(self) -> float:  # Changed to float
        grade_points = {
            "A" : 4.0, "A-": 3.7, "B+": 3.3, "B" : 3.0, "B-": 2.7,
            "C+": 2.3, "C" : 2.0, "C-": 1.7, "D" : 1.0, "F" : 0.0
        }       
        
        if self.grade not in grade_points:
            raise ValueError("Invalid grade \n Please enter the Valid Grade") 
       
        return grade_points[self.grade] # Removed str() conversion