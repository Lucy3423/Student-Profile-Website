from student import Student
from club import Club
from bulletin_notice import Bulletin_notice

class System:
    def __init__(self):
        self.students:Student = []
        self.bulletin_notices: Bulletin_notice = []
        self.social_science_clubs: Club = []
        self.science_clubs: Club = []
        self.sport_clubs: Club = []
        self.music_clubs: Club = []
        self.all_clubs = [self.science_clubs, self.social_science_clubs, self.music_clubs, self.sport_clubs] 
    
    def set_up_students(self):
        student_club_structure1 = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
        student_club_structure = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
        
        self.students.append(Student("Lucy Fowler", "21/07/2008", 0, "Lucy", "Fowler", ["French", "Maths", "Computing"], student_club_structure1))
        self.students.append(Student("John Brown", "04/5/2007", 1, "John", "Brown", ["DT", "Maths", "Art", "English", "German"], student_club_structure))
        return self.students
    
    def set_up_clubs(self):
        self.science_clubs.append(Club(1, "coding club", 2, "monday"))
        self.science_clubs.append(Club(2, "space design", 2, "tuesday"))
        self.science_clubs.append(Club(3, "canSAT", 3, "wednesday"))        
        self.science_clubs.append(Club(4, "physics olympiad", 2, "thursday"))
        self.science_clubs.append(Club(5, "silver crest award", 1, "friday"))

        self.social_science_clubs.append(Club(6, "history podcast", 2, "tuesday")) 
        self.social_science_clubs.append(Club(7, "m u n", 2, "friday"))   
        self.social_science_clubs.append(Club(7, "debating", 2, "monday"))   
        self.social_science_clubs.append(Club(7, "fem soc", 2, "friday"))   
        self.social_science_clubs.append(Club(7, "amnesty internation", 2, "friday"))   

        self.music_clubs.append(Club(8, "choir", 0, "wednesday"))
        self.music_clubs.append(Club(9, "orchestra", 3, "thursday"))
        self.music_clubs.append(Club(9, "rock band", 3, "thursday"))
        self.music_clubs.append(Club(9, "wind ensemble", 3, "thursday"))
        self.music_clubs.append(Club(9, "cantante", 3, "thursday"))

        self.sport_clubs.append(Club(10, "netball", 0, "wednesday"))
        self.sport_clubs.append(Club(11, "basketball", 3, "friday"))
        self.sport_clubs.append(Club(12, "hockey", 1, "monday"))
        self.sport_clubs.append(Club(12, "badminton", 1, "tuesday"))
        self.sport_clubs.append(Club(12, "lacrosse ", 1, "monday"))



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
    
    def identify_club_time_slot(self, club: Club):
        if club.time_slot == 0:
            time_slot = "8:am -> 8:45am"
        elif club.time_slot == 1:
            time_slot = "12:05pm -> 12:25pm"
        elif club.time_slot == 2:
            time_slot = "12:25pm -> 1:05pm"
        else:
            time_slot = "3:50pm -> 5:00pm"
        
        return time_slot

    def identify_club_day_index(self, club):
        if club.day == "monday":
            day_index = 0
        elif club.day == "tuesday":
            day_index = 1
        elif club.day == "wednesday":
            day_index = 2
        elif club.day == "thursday":
            day_index = 3
        else:
            day_index = 4
        
        return day_index

    # a method to find the correct club to add
    def find_chosen_club(self, club_id, student:Student):
        chosen_club = self.all_clubs[0][0]
        for category in self.all_clubs:
            for club in category:
                if club.club_id == club_id:
                    chosen_club = club
                    club_day_index=self.identify_club_day_index(chosen_club) 
                    valid = any(chosen_club.name in row for row in student.clubs) 
                    if valid == True:
                        "<h3> You already have a club at that time! </h3>"
                    else:
                        student.clubs[club_day_index][chosen_club.time_slot] = chosen_club.name.title()
                        print(student.clubs)
                    break
        return student
        




        # return student  















 
    
