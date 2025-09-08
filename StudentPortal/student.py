class Student:
    def __init__(self, first_name, last_name, DoB, student_id, username, password, year_group, subjects, clubs):
        self.first_name = first_name
        self.last_name = last_name
        self.DoB = DoB
        self.student_id = student_id
        self.username = username
        self.password = password 
        self.year_group = year_group
        self.subjects:list = subjects
        self.clubs = clubs
    
