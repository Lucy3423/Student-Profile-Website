from student import Student

class System:
    def __init__(self):
        self.students = []
        self.bulletin_notices = []
    
    def set_up_students(self):
        self.students.append(Student("Lucy Fowler", "21/07/2008", 0, "Lucy", "Fowler", ["French", "Maths", "Computing"]))
        self.students.append(Student("John Brown", "04/5/2007", 1, "John", "Brown", ["DT", "Maths", "Art", "English", "German"]))
        return self.students
    


    def login(self, username, password):
        found = False
        student_id = 0
        for student in self.students:
            if student.username == username and student.password == password:
                found = True
                student_id = student.student_id
        return found, student_id
    
    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student