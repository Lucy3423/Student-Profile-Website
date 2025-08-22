from student import Student
from club import Club

class System:
    def __init__(self):
        self.students = []
        self.bulletin_notices = []
        self.social_science_clubs = []
        self.science_clubs = []
    
    def set_up_students(self):
        self.students.append(Student("Lucy Fowler", "21/07/2008", 0, "Lucy", "Fowler", ["French", "Maths", "Computing"], ["Space Design"]))
        self.students.append(Student("John Brown", "04/5/2007", 1, "John", "Brown", ["DT", "Maths", "Art", "English", "German"], ["Language Leaders"]))
        return self.students
    
    def set_up_clubs(self):
        self.science_clubs.append(Club("coding club", "science", 3, "monday"))
        self.science_clubs.append(Club("space design", "science", 3, "tuesday"))
        self.science_clubs.append(Club("canSAT", "science", 4, "wednesday"))        
        self.science_clubs.append(Club("physics olympiad", "science", 3, "thursday"))
        self.science_clubs.append(Club("silver crest award", "science", 2, "friday"))
        
        self.social_science_clubs.append(Club("History Podcast", "social science", 3, "tuesday"))    


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
    
    def identify_club_time_slot(self, club):
        if club.day == 1:
            time_slot = "8:am -> 8:45am"
        elif club.day == 2:
            time_slot = "12:05pm -> 12:25pm"
        elif club.day == 3:
            time_slot = "12:25pm -> 1:05pm"
        else:
            time_slot = "3:50pm -> 5:00pm"
        
        return time_slot